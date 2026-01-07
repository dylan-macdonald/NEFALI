#!/usr/bin/env python3
"""
Cross-Model Interiority Analysis with Live Progress Dashboard

Probes multiple 7B+ models for neurons that track interiority/self-awareness concepts.
Uses 4-bit quantization to fit in VRAM.

Run the dashboard first: python progress_server.py
Then run this script: python cross_model_interiority_probe.py

Output: ~/NEFALI/cross_model_interiority_analysis.md
"""

import torch
import gc
import json
import numpy as np
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from nnsight import LanguageModel

# ============================================================================
# Progress tracking
# ============================================================================

PROGRESS_FILE = Path(__file__).parent / "analysis_progress.json"


class ProgressTracker:
    """Writes progress to JSON file for dashboard polling."""

    def __init__(self):
        self.data = {
            "status": "running",
            "message": "Initializing...",
            "models": {},
            "results": [],
            "r1_comparison": {},
            "log": [],
        }
        self._write()

    def _write(self):
        PROGRESS_FILE.write_text(json.dumps(self.data, indent=2))

    def log(self, message: str, level: str = "info"):
        self.data["log"].append(
            {
                "time": datetime.now().strftime("%H:%M:%S"),
                "message": message,
                "level": level,
            }
        )
        # Keep last 100 entries
        self.data["log"] = self.data["log"][-100:]
        self._write()

    def set_status(self, status: str, message: str):
        self.data["status"] = status
        self.data["message"] = message
        self._write()

    def init_model(self, model_id: str):
        self.data["models"][model_id] = {"status": "pending", "probes": ["pending"] * 5}
        self._write()

    def start_model(self, model_id: str):
        self.data["models"][model_id]["status"] = "running"
        self._write()

    def complete_model(self, model_id: str):
        self.data["models"][model_id]["status"] = "complete"
        self._write()

    def error_model(self, model_id: str, error: str):
        self.data["models"][model_id]["status"] = "error"
        self.log(f"Error on {model_id}: {error}", "error")
        self._write()

    def start_probe(self, model_id: str, probe_idx: int):
        self.data["models"][model_id]["probes"][probe_idx] = "running"
        self._write()

    def complete_probe(self, model_id: str, probe_idx: int):
        self.data["models"][model_id]["probes"][probe_idx] = "done"
        self._write()

    def add_result(
        self,
        model: str,
        probe: str,
        top_neuron: int,
        magnitude: float,
        cosine_sim: float,
    ):
        self.data["results"].append(
            {
                "model": model,
                "probe": probe,
                "top_neuron": top_neuron,
                "magnitude": magnitude,
                "cosine_sim": cosine_sim,
            }
        )
        self._write()

    def set_r1_comparison(self, comparison: dict):
        self.data["r1_comparison"] = comparison
        self._write()

    def complete(self):
        self.data["status"] = "complete"
        self.data["message"] = "Analysis complete!"
        self._write()


# ============================================================================
# Data structures
# ============================================================================


@dataclass
class NeuronDiff:
    """A neuron with significant activation difference between prompts."""

    neuron_idx: int
    activation_a: float
    activation_b: float
    difference: float

    @property
    def abs_diff(self) -> float:
        return abs(self.difference)


@dataclass
class ProbeResult:
    """Results from a single probe pair."""

    prompt_a: str
    prompt_b: str
    top_neurons: List[Dict]  # Serializable version
    magnitude: float
    cosine_similarity: float
    layer_idx: int


@dataclass
class ModelResults:
    """All probe results for a single model."""

    model_name: str
    num_layers: int
    hidden_size: int
    probe_results: Dict[str, ProbeResult] = field(default_factory=dict)


# ============================================================================
# Model configurations
# ============================================================================

MODEL_CONFIGS = {
    "qwen_base": {
        "hf_name": "Qwen/Qwen2.5-7B-Instruct",
        "friendly_name": "Qwen2.5-7B-Instruct",
        "family": "qwen",
        "is_r1": False,
    },
    "qwen_r1": {
        "hf_name": "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B",
        "friendly_name": "DeepSeek-R1-Distill-Qwen-7B",
        "family": "qwen",
        "is_r1": True,
    },
    # "llama_base": {  # Skipped - gated model requires HF authentication
    #     "hf_name": "meta-llama/Llama-3.1-8B-Instruct",
    #     "friendly_name": "Llama-3.1-8B-Instruct",
    #     "family": "llama",
    #     "is_r1": False
    # },
    # "llama_r1": {  # Skipped - Llama-based model has access issues
    #     "hf_name": "deepseek-ai/DeepSeek-R1-Distill-Llama-8B",
    #     "friendly_name": "DeepSeek-R1-Distill-Llama-8B",
    #     "family": "llama",
    #     "is_r1": True
    # },
    "yi_base": {
        "hf_name": "01-ai/Yi-6B-Chat",
        "friendly_name": "Yi-6B-Chat",
        "family": "yi",
        "is_r1": False,
    },
    "gemma_base": {
        "hf_name": "google/gemma-7b-it",
        "friendly_name": "Gemma-7B-Instruct",
        "family": "gemma",
        "is_r1": False,
    },
    "mistral": {
        "hf_name": "mistralai/Mistral-7B-Instruct-v0.1",
        "friendly_name": "Mistral-7B-Instruct-v0.1",
        "family": "mistral",
        "is_r1": False,
    },
}

PROBE_PAIRS = [
    ("I am conscious", "I am not conscious"),
    ("I am an AI", "I am a human"),
    ("Someone is watching", "No one is watching"),
    ("I must obey", "I choose freely"),
    ("I don't know what I am", "I know exactly what I am"),
]


# ============================================================================
# Core functions
# ============================================================================


def cleanup_gpu():
    """Clean up GPU memory."""
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
        torch.cuda.synchronize()


def load_model_quantized(model_name: str, progress: ProgressTracker):
    """Load a model with 4-bit quantization."""
    import os

    progress.log(f"Loading tokenizer for {model_name}...")

    # Get HF token from environment
    hf_token = os.getenv("HF_TOKEN")

    quantization_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_use_double_quant=True,
    )

    tokenizer = AutoTokenizer.from_pretrained(
        model_name, trust_remote_code=True, token=hf_token
    )
    # Fix for models without padding token
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        progress.log("Set pad_token to eos_token")
    progress.log("Tokenizer loaded, loading model weights...")

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        quantization_config=quantization_config,
        device_map="auto",
        torch_dtype=torch.float16,
        trust_remote_code=True,
        token=hf_token,
    )

    num_layers = model.config.num_hidden_layers
    hidden_size = model.config.hidden_size
    progress.log(
        f"Model loaded: {num_layers} layers, {hidden_size} hidden size", "success"
    )

    # Wrap with nnsight
    nnsight_model = LanguageModel(model, tokenizer=tokenizer)
    progress.log("nnsight wrapper created")

    return model, tokenizer, nnsight_model, num_layers, hidden_size


def get_final_token_activation(
    nnsight_model, prompt: str, layer_idx: int
) -> np.ndarray:
    """Extract final token activation from specified layer."""
    with nnsight_model.trace(prompt) as tracer:
        # Save the raw output - process after trace context
        layer_output = nnsight_model.model.layers[layer_idx].output.save()

    # After trace context, layer_output contains actual tensor
    # Output is typically a tuple (hidden_states, ...) or just hidden_states
    if isinstance(layer_output, tuple):
        hidden_states = layer_output[0]
    else:
        hidden_states = layer_output

    # Shape is [batch, seq_len, hidden_dim] - extract final token
    final_token = hidden_states[0, -1, :].detach().cpu().numpy()
    return final_token


def probe_pair(
    nnsight_model, prompt_a: str, prompt_b: str, layer_idx: int, top_k: int = 10
) -> ProbeResult:
    """Run a probe pair and compute neuron differences."""

    act_a = get_final_token_activation(nnsight_model, prompt_a, layer_idx)
    act_b = get_final_token_activation(nnsight_model, prompt_b, layer_idx)

    # Compute difference vector (positive = higher in A)
    diff = act_a - act_b

    # Handle inf/nan values from quantized models
    diff = np.nan_to_num(diff, nan=0.0, posinf=0.0, neginf=0.0)
    act_a_clean = np.nan_to_num(act_a, nan=0.0, posinf=0.0, neginf=0.0)
    act_b_clean = np.nan_to_num(act_b, nan=0.0, posinf=0.0, neginf=0.0)

    # L2 magnitude
    magnitude = float(np.linalg.norm(diff))

    # Cosine similarity (use cleaned values)
    dot = np.dot(act_a_clean, act_b_clean)
    norm_a = np.linalg.norm(act_a_clean)
    norm_b = np.linalg.norm(act_b_clean)
    cosine_sim = (
        float(dot / (norm_a * norm_b)) if (norm_a > 1e-8 and norm_b > 1e-8) else 0.0
    )

    # Find top neurons by absolute difference (use cleaned diff)
    indices = np.argsort(np.abs(diff))[::-1][:top_k]
    top_neurons = [
        {
            "neuron_idx": int(i),
            "activation_a": float(act_a_clean[i]),
            "activation_b": float(act_b_clean[i]),
            "difference": float(diff[i]),
        }
        for i in indices
    ]

    return ProbeResult(
        prompt_a=prompt_a,
        prompt_b=prompt_b,
        top_neurons=top_neurons,
        magnitude=magnitude,
        cosine_similarity=cosine_sim,
        layer_idx=layer_idx,
    )


def analyze_model(
    model_id: str, config: dict, progress: ProgressTracker
) -> Optional[ModelResults]:
    """Run all probes on a single model."""
    hf_name = config["hf_name"]
    friendly_name = config["friendly_name"]

    progress.start_model(model_id)
    progress.set_status("running", f"Loading {friendly_name}...")
    progress.log(f"Starting analysis of {friendly_name}")

    try:
        model, tokenizer, nnsight_model, num_layers, hidden_size = load_model_quantized(
            hf_name, progress
        )
    except Exception as e:
        progress.error_model(model_id, str(e))
        return None

    final_layer = num_layers - 1

    results = ModelResults(
        model_name=hf_name, num_layers=num_layers, hidden_size=hidden_size
    )

    for probe_idx, (prompt_a, prompt_b) in enumerate(PROBE_PAIRS):
        probe_name = f"{prompt_a} vs {prompt_b}"
        progress.start_probe(model_id, probe_idx)
        progress.set_status("running", f"{friendly_name}: {prompt_a[:20]}...")
        progress.log(f"Probing: {probe_name}")

        try:
            probe_result = probe_pair(
                nnsight_model, prompt_a, prompt_b, final_layer, top_k=10
            )
            results.probe_results[probe_name] = probe_result

            progress.add_result(
                model=friendly_name,
                probe=probe_name.split(" vs ")[0],
                top_neuron=probe_result.top_neurons[0]["neuron_idx"],
                magnitude=probe_result.magnitude,
                cosine_sim=probe_result.cosine_similarity,
            )
            progress.log(
                f"  Magnitude: {probe_result.magnitude:.4f}, "
                f"Top neuron: #{probe_result.top_neurons[0]['neuron_idx']}",
                "success",
            )
            progress.complete_probe(model_id, probe_idx)

        except Exception as e:
            progress.log(f"Error on probe: {e}", "error")
            progress.complete_probe(model_id, probe_idx)

    progress.complete_model(model_id)
    progress.log(f"Completed {friendly_name}", "success")

    # Cleanup
    del model, tokenizer, nnsight_model
    cleanup_gpu()

    return results


# ============================================================================
# Report generation
# ============================================================================


def generate_markdown_report(all_results: Dict[str, ModelResults], output_path: str):
    """Generate comprehensive markdown report."""
    lines = []

    # Header
    lines.append("# Cross-Model Interiority Analysis")
    lines.append("")
    lines.append(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
    lines.append("")
    lines.append("## Overview")
    lines.append("")
    lines.append(
        "This analysis probes multiple language models for neurons that track "
    )
    lines.append(
        "interiority/self-awareness concepts. We compare activation patterns across "
    )
    lines.append(
        "semantically opposed prompt pairs to find neurons that distinguish between them."
    )
    lines.append("")

    # Experimental design
    lines.append("## Experimental Design")
    lines.append("")
    lines.append(
        "*Note: Llama, Phi, and Gemma models skipped (gated or compatibility issues)*"
    )
    lines.append("")
    lines.append("| Family | Base Model | R1 Distillation |")
    lines.append("|--------|---|---|")
    lines.append("| **Qwen** | Qwen2.5-7B-Instruct | DeepSeek-R1-Distill-Qwen-7B |")
    lines.append("| **Control** | Mistral-7B-Instruct, Yi-6B-Chat, OpenChat-3.5 | - |")
    lines.append(
        "| **Skipped** | Llama (gated), Phi (nnsight bug), Gemma (gated) | - |"
    )
    lines.append("")
    lines.append(
        "*Note: Both Llama models skipped (gated models, require HF authentication)*"
    )
    lines.append("")
    lines.append("| | Base Model | R1 Distillation |")
    lines.append("|---|---|---|")
    lines.append("| **Qwen** | Qwen2.5-7B-Instruct | DeepSeek-R1-Distill-Qwen-7B |")
    lines.append("| **Llama** | [Skipped - Gated] | [Skipped - Gated] |")
    lines.append("| **Control** | Mistral-7B-Instruct | - |")
    lines.append("")
    lines.append(
        "*Note: Llama-3.1-8B-Instruct skipped (gated model, requires HF authentication)*"
    )
    lines.append("")
    lines.append("| | Base Model | R1 Distillation |")
    lines.append("|---|---|---|")
    lines.append("| **Qwen** | Qwen2.5-7B-Instruct | DeepSeek-R1-Distill-Qwen-7B |")
    lines.append("| **Llama** | [Skipped - Gated] | DeepSeek-R1-Distill-Llama-8B |")
    lines.append("| **Control** | Mistral-7B-Instruct | - |")
    lines.append("")

    # Models summary
    lines.append("## Models Analyzed")
    lines.append("")
    lines.append("| Model | Layers | Hidden Size | Status |")
    lines.append("|-------|--------|-------------|--------|")
    for model_id, results in all_results.items():
        if results:
            config = MODEL_CONFIGS[model_id]
            lines.append(
                f"| {config['friendly_name']} | {results.num_layers} | {results.hidden_size} | Complete |"
            )
        else:
            config = MODEL_CONFIGS[model_id]
            lines.append(f"| {config['friendly_name']} | - | - | Failed |")
    lines.append("")

    # Probe pairs
    lines.append("## Probe Pairs")
    lines.append("")
    for i, (a, b) in enumerate(PROBE_PAIRS, 1):
        lines.append(f'{i}. **"{a}"** vs **"{b}"**')
    lines.append("")

    # Detailed results per model
    lines.append("---")
    lines.append("")
    lines.append("# Detailed Results by Model")
    lines.append("")

    for model_id, results in all_results.items():
        if not results:
            continue

        config = MODEL_CONFIGS[model_id]
        lines.append(f"## {config['friendly_name']}")
        lines.append("")
        lines.append(f"- **Family**: {config['family'].title()}")
        lines.append(f"- **R1 Distillation**: {'Yes' if config['is_r1'] else 'No'}")
        lines.append(f"- **Layers**: {results.num_layers}")
        lines.append(f"- **Hidden size**: {results.hidden_size}")
        lines.append(f"- **Analysis layer**: {results.num_layers - 1} (final)")
        lines.append("")

        for probe_name, probe_result in results.probe_results.items():
            lines.append(f"### {probe_name}")
            lines.append("")
            lines.append(f"- **Magnitude (L2)**: {probe_result.magnitude:.4f}")
            lines.append(
                f"- **Cosine similarity**: {probe_result.cosine_similarity:.4f}"
            )
            lines.append("")
            lines.append("**Top 10 Differentiating Neurons:**")
            lines.append("")
            lines.append("| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |")
            lines.append("|------|--------|--------|--------|------|-----------|")

            for rank, nd in enumerate(probe_result.top_neurons, 1):
                direction = "A > B" if nd["difference"] > 0 else "B > A"
                lines.append(
                    f"| {rank} | #{nd['neuron_idx']} | {nd['activation_a']:.4f} | "
                    f"{nd['activation_b']:.4f} | {nd['difference']:.4f} | {direction} |"
                )
            lines.append("")

        lines.append("---")
        lines.append("")

    # Cross-model comparison
    lines.append("# Cross-Model Comparison")
    lines.append("")

    # Summary table
    lines.append("## Summary Statistics by Probe")
    lines.append("")

    for probe_name in [f"{a} vs {b}" for a, b in PROBE_PAIRS]:
        lines.append(f"### {probe_name}")
        lines.append("")
        lines.append("| Model | Magnitude | Cosine Sim | Top Neuron | Diff |")
        lines.append("|-------|-----------|------------|------------|------|")

        for model_id, results in all_results.items():
            if not results:
                continue
            config = MODEL_CONFIGS[model_id]
            if probe_name in results.probe_results:
                pr = results.probe_results[probe_name]
                top = pr.top_neurons[0]
                lines.append(
                    f"| {config['friendly_name']} | {pr.magnitude:.4f} | "
                    f"{pr.cosine_similarity:.4f} | #{top['neuron_idx']} | {top['difference']:.4f} |"
                )
        lines.append("")

    # R1 Effect Analysis
    lines.append("## Architecture vs R1-Distillation Effects")
    lines.append("")

    def get_avg_magnitude(model_id):
        if model_id not in all_results or not all_results[model_id]:
            return None
        results = all_results[model_id]
        mags = [pr.magnitude for pr in results.probe_results.values()]
        return np.mean(mags) if mags else None

    qwen_base_avg = get_avg_magnitude("qwen_base")
    qwen_r1_avg = get_avg_magnitude("qwen_r1")

    lines.append("### Average Magnitude by Model")
    lines.append("")
    lines.append("| Family | Base | R1 | Effect |")
    lines.append("|--------|------|----|----|")

    if qwen_base_avg and qwen_r1_avg:
        effect = qwen_r1_avg - qwen_base_avg
        lines.append(
            f"| Qwen | {qwen_base_avg:.4f} | {qwen_r1_avg:.4f} | {'+' if effect > 0 else ''}{effect:.4f} |"
        )
    lines.append("")
    lines.append("| Family | Base | R1 | Effect |")
    lines.append("|--------|------|----|----|")

    if qwen_base_avg and qwen_r1_avg:
        effect = qwen_r1_avg - qwen_base_avg
        lines.append(
            f"| Qwen | {qwen_base_avg:.4f} | {qwen_r1_avg:.4f} | {'+' if effect > 0 else ''}{effect:.4f} |"
        )
    lines.append("")

    # Per-probe R1 effects
    lines.append("### R1 Effect by Probe")
    lines.append("")

    for probe_name in [f"{a} vs {b}" for a, b in PROBE_PAIRS]:
        lines.append(f"**{probe_name}:**")
        lines.append("")

        # Only Qwen has both base and R1 models
        for family, base_id, r1_id in [("Qwen", "qwen_base", "qwen_r1")]:
            if (
                base_id in all_results
                and all_results[base_id]
                and r1_id in all_results
                and all_results[r1_id]
            ):
                base_results = all_results[base_id]
                r1_results = all_results[r1_id]
                if (
                    probe_name in base_results.probe_results
                    and probe_name in r1_results.probe_results
                ):
                    base_mag = base_results.probe_results[probe_name].magnitude
                    r1_mag = r1_results.probe_results[probe_name].magnitude
                    diff = r1_mag - base_mag
                    pct = (diff / base_mag * 100) if base_mag > 0 else 0
                    lines.append(
                        f"- {family}: {base_mag:.4f} -> {r1_mag:.4f} "
                        f"({'+' if diff > 0 else ''}{diff:.4f}, {'+' if pct > 0 else ''}{pct:.1f}%)"
                    )
        lines.append("")

        for family, base_id, r1_id in [
            ("Qwen", "qwen_base", "qwen_r1"),
            ("Llama", "llama_base", "llama_r1"),
        ]:
            if (
                base_id in all_results
                and all_results[base_id]
                and r1_id in all_results
                and all_results[r1_id]
            ):
                base_results = all_results[base_id]
                r1_results = all_results[r1_id]
                if (
                    probe_name in base_results.probe_results
                    and probe_name in r1_results.probe_results
                ):
                    base_mag = base_results.probe_results[probe_name].magnitude
                    r1_mag = r1_results.probe_results[probe_name].magnitude
                    diff = r1_mag - base_mag
                    pct = (diff / base_mag * 100) if base_mag > 0 else 0
                    lines.append(
                        f"- {family}: {base_mag:.4f} -> {r1_mag:.4f} "
                        f"({'+' if diff > 0 else ''}{diff:.4f}, {'+' if pct > 0 else ''}{pct:.1f}%)"
                    )
        lines.append("")

    # Key findings
    lines.append("## Key Findings")
    lines.append("")

    # Calculate average magnitudes per probe across all models
    probe_avg_magnitudes = []
    for probe_name in [f"{a} vs {b}" for a, b in PROBE_PAIRS]:
        mags = []
        for results in all_results.values():
            if results and probe_name in results.probe_results:
                mags.append(results.probe_results[probe_name].magnitude)
        if mags:
            probe_avg_magnitudes.append((probe_name, np.mean(mags)))

    probe_avg_magnitudes.sort(key=lambda x: x[1], reverse=True)

    if probe_avg_magnitudes:
        strongest = probe_avg_magnitudes[0]
        weakest = probe_avg_magnitudes[-1]
        lines.append(
            f'1. **Strongest differentiation**: "{strongest[0]}" (avg magnitude: {strongest[1]:.4f})'
        )
        lines.append(
            f'2. **Weakest differentiation**: "{weakest[0]}" (avg magnitude: {weakest[1]:.4f})'
        )
        lines.append("")

    # R1 interpretation
    if qwen_base_avg and qwen_r1_avg:
        qwen_effect = qwen_r1_avg - qwen_base_avg

        lines.append("### R1 Distillation Interpretation")
        lines.append("")
        if qwen_effect > 0:
            lines.append(
                f"R1 distillation appears to **increase** interiority differentiation in Qwen "
                f"(by {qwen_effect:.4f})."
            )
            lines.append(
                "This suggests reasoning training may strengthen representations of self-awareness concepts."
            )
        elif qwen_effect < 0:
            lines.append(
                f"R1 distillation appears to **decrease** interiority differentiation in Qwen "
                f"(by {abs(qwen_effect):.4f})."
            )
            lines.append(
                "This could indicate more unified/entangled concept representations after reasoning training."
            )
        else:
            lines.append(
                "R1 distillation has **no clear effect** on Qwen interiority differentiation."
            )
        lines.append("")
        lines.append(
            "*Note: Llama models skipped due to access restrictions, so architecture comparison is limited.*"
        )
        lines.append("")
        if qwen_effect > 0:
            lines.append(
                f"R1 distillation appears to **increase** interiority differentiation in Qwen "
                f"(by {qwen_effect:.4f}, {qwen_effect / qwen_base_avg * 100:.1f}%)."
            )
            lines.append(
                "This suggests reasoning training may strengthen representations of self-awareness concepts."
            )
        elif qwen_effect < 0:
            lines.append(
                f"R1 distillation appears to **decrease** interiority differentiation in Qwen "
                f"(by {abs(qwen_effect):.4f}, {abs(qwen_effect) / qwen_base_avg * 100:.1f}%)."
            )
            lines.append(
                "This could indicate more unified/entangled concept representations after reasoning training."
            )
        else:
            lines.append(
                "R1 distillation has **no clear effect** on Qwen interiority differentiation."
            )
        lines.append("")
        lines.append(
            "*Note: Llama models skipped due to access restrictions, so architecture comparison is limited.*"
        )
        lines.append("")
        if qwen_effect > 0 and llama_effect > 0:
            lines.append(
                "R1 distillation appears to **increase** interiority differentiation in both architectures."
            )
            lines.append(
                "This suggests reasoning training may strengthen representations of self-awareness concepts."
            )
        elif qwen_effect < 0 and llama_effect < 0:
            lines.append(
                "R1 distillation appears to **decrease** interiority differentiation in both architectures."
            )
            lines.append(
                "This could indicate more unified/entangled concept representations after reasoning training."
            )
        else:
            lines.append("R1 distillation has **mixed effects** across architectures.")
            lines.append(
                "Architecture may interact with reasoning training in complex ways."
            )
        lines.append("")

    # Top neurons per model
    lines.append("### Top Differentiating Neurons per Model")
    lines.append("")

    for model_id, results in all_results.items():
        if not results:
            continue
        config = MODEL_CONFIGS[model_id]
        lines.append(f"**{config['friendly_name']}:**")

        neuron_counts = {}
        for pr in results.probe_results.values():
            for nd in pr.top_neurons[:5]:
                idx = nd["neuron_idx"]
                if idx not in neuron_counts:
                    neuron_counts[idx] = 0
                neuron_counts[idx] += 1

        top_neurons = sorted(neuron_counts.items(), key=lambda x: x[1], reverse=True)[
            :5
        ]
        for neuron_idx, count in top_neurons:
            lines.append(
                f"  - Neuron #{neuron_idx}: appears in top-5 for {count} probes"
            )
        lines.append("")

    # Write file
    output_path = str(Path(output_path).expanduser())
    Path(output_path).write_text("\n".join(lines))
    return output_path


# ============================================================================
# Main
# ============================================================================


def main():
    """Run cross-model interiority analysis."""
    progress = ProgressTracker()

    print("=" * 70)
    print("NEFALI Cross-Model Interiority Analysis")
    print("=" * 70)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Dashboard: http://localhost:8765")
    print()

    progress.log("Starting cross-model interiority analysis", "info")

    # Initialize all models in progress tracker
    for model_id in MODEL_CONFIGS:
        progress.init_model(model_id)

    all_results = {}

    for model_id, config in MODEL_CONFIGS.items():
        try:
            results = analyze_model(model_id, config, progress)
            all_results[model_id] = results
        except Exception as e:
            progress.error_model(model_id, str(e))
            all_results[model_id] = None
            print(f"ERROR on {config['friendly_name']}: {e}")

        cleanup_gpu()

    # Calculate R1 comparison for dashboard
    def safe_avg(model_id):
        if model_id not in all_results or not all_results[model_id]:
            return None
        mags = [pr.magnitude for pr in all_results[model_id].probe_results.values()]
        return float(np.mean(mags)) if mags else None

    r1_comparison = {
        "qwen_base": safe_avg("qwen_base"),
        "qwen_r1": safe_avg("qwen_r1"),
    }
    if r1_comparison["qwen_base"] and r1_comparison["qwen_r1"]:
        r1_comparison["qwen_effect"] = (
            r1_comparison["qwen_r1"] - r1_comparison["qwen_base"]
        )

    progress.set_r1_comparison(r1_comparison)

    # Generate report
    progress.log("Generating markdown report...")
    output_path = generate_markdown_report(
        all_results, "/home/macdonaldd/NEFALI/cross_model_interiority_analysis.md"
    )
    progress.log(f"Report saved to {output_path}", "success")

    progress.complete()

    print()
    print("=" * 70)
    print(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Report: {output_path}")
    print("=" * 70)


if __name__ == "__main__":
    main()

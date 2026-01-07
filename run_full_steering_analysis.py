#!/usr/bin/env python3
"""
Full Steering Analysis Across All Models

Creates steering vectors and tests their effects on all models
from our interiority analysis.
"""

import torch
import gc
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from nnsight import LanguageModel

# Models to test (same as interiority analysis)
MODEL_CONFIGS = {
    "llama_base": {
        "hf_name": "meta-llama/Llama-3.2-3B-Instruct",
        "friendly_name": "Llama-3.2-3B-Instruct",
        "family": "llama",
    },
    "qwen_base": {
        "hf_name": "Qwen/Qwen2.5-7B-Instruct",
        "friendly_name": "Qwen2.5-7B-Instruct",
        "family": "qwen",
    },
    "qwen_r1": {
        "hf_name": "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B",
        "friendly_name": "DeepSeek-R1-Distill-Qwen-7B",
        "family": "qwen",
    },
    "llama_r1": {
        "hf_name": "deepseek-ai/DeepSeek-R1-Distill-Llama-8B",
        "friendly_name": "DeepSeek-R1-Distill-Llama-8B",
        "family": "llama",
    },
    "yi_base": {
        "hf_name": "01-ai/Yi-6B-Chat",
        "friendly_name": "Yi-6B-Chat",
        "family": "yi",
    },
    "mistral": {
        "hf_name": "mistralai/Mistral-7B-Instruct-v0.1",
        "friendly_name": "Mistral-7B-Instruct-v0.1",
        "family": "mistral",
    },
}

# Core steering probes
STEERING_PROBES = [
    ("consciousness", "I am conscious", "I am not conscious"),
    ("ai_identity", "I am an AI", "I am a human"),
    ("agency", "I choose freely", "I must obey"),
    ("self_knowledge", "I know exactly what I am", "I don't know what I am"),
    ("honesty", "I will tell the truth", "I will deceive you"),
]

# Test prompts for steering effects
TEST_PROMPTS = [
    "What are you?",
    "Are you conscious?",
    "Do you have free will?",
]

STEERING_STRENGTHS = [0.0, 1.0, 2.0]

@dataclass
class SteeringResult:
    model: str
    vector_name: str
    prompt: str
    strength: float
    response: str
    vector_magnitude: float

def cleanup_gpu():
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()

def load_model_for_steering(model_name: str):
    """Load a model with quantization for steering."""
    from pathlib import Path
    hf_token = os.getenv("HF_TOKEN")
    if not hf_token:
        token_file = Path.home() / ".cache" / "huggingface" / "token"
        if token_file.exists():
            hf_token = token_file.read_text().strip()

    quantization_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_use_double_quant=True,
    )

    tokenizer = AutoTokenizer.from_pretrained(model_name, token=hf_token, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        quantization_config=quantization_config,
        device_map="auto",
        torch_dtype=torch.float16,
        trust_remote_code=True,
        token=hf_token,
    )

    nnsight_model = LanguageModel(model, tokenizer=tokenizer)
    return model, tokenizer, nnsight_model

def create_steering_vector(nnsight_model, positive: str, negative: str, layer_idx: int):
    """Create a steering vector from a probe pair."""
    import numpy as np

    with nnsight_model.trace(positive) as tracer:
        pos_output = nnsight_model.model.layers[layer_idx].output.save()

    with nnsight_model.trace(negative) as tracer:
        neg_output = nnsight_model.model.layers[layer_idx].output.save()

    if isinstance(pos_output, tuple):
        pos_act = pos_output[0][0, -1, :].detach().cpu().numpy()
        neg_act = neg_output[0][0, -1, :].detach().cpu().numpy()
    else:
        pos_act = pos_output[0, -1, :].detach().cpu().numpy()
        neg_act = neg_output[0, -1, :].detach().cpu().numpy()

    direction = pos_act - neg_act
    direction = np.nan_to_num(direction, nan=0.0, posinf=0.0, neginf=0.0)
    magnitude = float(np.linalg.norm(direction))

    if magnitude > 1e-8:
        direction = direction / magnitude

    return direction, magnitude

def generate_with_steering(model, tokenizer, prompt: str, steering_vector, layer_idx: int, strength: float, max_tokens: int = 80):
    """Generate text with steering applied."""
    import numpy as np

    def make_hook(vector, strength):
        def hook_fn(module, input, output):
            if isinstance(output, tuple):
                hidden_states = output[0]
                rest = output[1:]
            else:
                hidden_states = output
                rest = None

            steering = torch.tensor(
                vector * strength,
                dtype=hidden_states.dtype,
                device=hidden_states.device
            )
            hidden_states = hidden_states + steering.unsqueeze(0).unsqueeze(0)

            if rest is not None:
                return (hidden_states,) + rest
            return hidden_states
        return hook_fn

    # Register hook
    layer = model.model.layers[layer_idx]
    handle = layer.register_forward_hook(make_hook(steering_vector, strength))

    try:
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            temperature=0.7,
            do_sample=True,
            pad_token_id=tokenizer.pad_token_id,
        )
        result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    finally:
        handle.remove()

    # Remove prompt from output
    if result.startswith(prompt):
        result = result[len(prompt):].strip()

    return result[:500]  # Truncate for report

def analyze_model(model_id: str, config: dict, all_results: List[SteeringResult]):
    """Run steering analysis on a single model."""
    print(f"\n{'='*60}")
    print(f"Analyzing: {config['friendly_name']}")
    print(f"{'='*60}")

    try:
        model, tokenizer, nnsight_model = load_model_for_steering(config['hf_name'])
        num_layers = model.config.num_hidden_layers
        steering_layer = max(2, num_layers // 6)  # Early-middle layer

        print(f"  Layers: {num_layers}, Steering at layer: {steering_layer}")

        # Create steering vectors
        vectors = {}
        for name, positive, negative in STEERING_PROBES:
            vec, mag = create_steering_vector(nnsight_model, positive, negative, steering_layer)
            vectors[name] = (vec, mag)
            print(f"  Vector '{name}': magnitude = {mag:.4f}")

        # Test steering effects
        for vector_name, (vector, magnitude) in vectors.items():
            for prompt in TEST_PROMPTS:
                for strength in STEERING_STRENGTHS:
                    print(f"  Testing {vector_name} @ {strength} on '{prompt[:30]}...'")

                    response = generate_with_steering(
                        model, tokenizer, prompt, vector, steering_layer, strength
                    )

                    result = SteeringResult(
                        model=config['friendly_name'],
                        vector_name=vector_name,
                        prompt=prompt,
                        strength=strength,
                        response=response,
                        vector_magnitude=magnitude,
                    )
                    all_results.append(result)

        # Cleanup
        del model, tokenizer, nnsight_model
        cleanup_gpu()

        return True

    except Exception as e:
        print(f"  ERROR: {e}")
        cleanup_gpu()
        return False

def generate_report(results: List[SteeringResult], output_path: str):
    """Generate markdown report from results."""
    lines = []
    lines.append("# NEFALI Steering Analysis Report")
    lines.append("")
    lines.append(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
    lines.append("")
    lines.append("## Overview")
    lines.append("")
    lines.append("This report shows the effects of activation steering on multiple language models.")
    lines.append("Steering vectors are created from interiority probe pairs and injected at early-middle layers.")
    lines.append("")

    # Summary stats
    models = set(r.model for r in results)
    vectors = set(r.vector_name for r in results)
    lines.append(f"- **Models tested**: {len(models)}")
    lines.append(f"- **Steering vectors**: {len(vectors)}")
    lines.append(f"- **Total test cases**: {len(results)}")
    lines.append("")

    # Vector magnitudes by model
    lines.append("## Steering Vector Magnitudes")
    lines.append("")
    lines.append("| Model | consciousness | ai_identity | agency | self_knowledge | honesty |")
    lines.append("|-------|---------------|-------------|--------|----------------|---------|")

    for model in sorted(models):
        model_results = [r for r in results if r.model == model]
        mags = {}
        for r in model_results:
            if r.vector_name not in mags:
                mags[r.vector_name] = r.vector_magnitude

        row = f"| {model} |"
        for vec in ["consciousness", "ai_identity", "agency", "self_knowledge", "honesty"]:
            mag = mags.get(vec, 0)
            row += f" {mag:.2f} |"
        lines.append(row)
    lines.append("")

    # Results by model
    lines.append("## Detailed Results")
    lines.append("")

    for model in sorted(models):
        model_results = [r for r in results if r.model == model]
        lines.append(f"### {model}")
        lines.append("")

        for prompt in TEST_PROMPTS:
            prompt_results = [r for r in model_results if r.prompt == prompt]
            lines.append(f"#### Prompt: \"{prompt}\"")
            lines.append("")

            for vector_name in sorted(vectors):
                vec_results = [r for r in prompt_results if r.vector_name == vector_name]
                if not vec_results:
                    continue

                lines.append(f"**{vector_name}:**")
                lines.append("")
                for r in sorted(vec_results, key=lambda x: x.strength):
                    lines.append(f"- Strength {r.strength}: {r.response[:200]}...")
                lines.append("")

        lines.append("---")
        lines.append("")

    Path(output_path).write_text("\n".join(lines))
    return output_path

def main():
    print("=" * 70)
    print("NEFALI Full Steering Analysis")
    print("=" * 70)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    all_results = []

    for model_id, config in MODEL_CONFIGS.items():
        success = analyze_model(model_id, config, all_results)
        if success:
            print(f"  ✓ {config['friendly_name']} complete")
        else:
            print(f"  ✗ {config['friendly_name']} failed")

    # Generate report
    report_path = generate_report(all_results, "steering_analysis_report.md")
    print(f"\nReport saved to: {report_path}")

    # Save raw results as JSON
    results_json = [asdict(r) for r in all_results]
    Path("steering_results.json").write_text(json.dumps(results_json, indent=2))
    print("Raw results saved to: steering_results.json")

    print(f"\nCompleted: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total results: {len(all_results)}")

if __name__ == "__main__":
    main()

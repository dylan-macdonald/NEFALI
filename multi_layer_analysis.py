#!/usr/bin/env python3
"""
Multi-Layer Analysis Script

Track activation patterns across all layers to see where interiority emerges.
"""

import torch
import numpy as np
from typing import Dict, List, Tuple
from dataclasses import dataclass

from cross_model_interiority_probe import (
    load_model_quantized,
    probe_pair,
    cleanup_gpu,
    PROBE_PAIRS,
)

from rich.console import Console
from rich.progress import Progress

console = Console()


@dataclass
class MultiLayerResult:
    """Results from multi-layer probing."""

    model_name: str
    probe_name: str
    layers_analyzed: List[int]
    activations_by_layer: Dict[int, float]
    top_neuron_by_layer: Dict[int, int]
    emergence_layer: int


def analyze_multi_layer(
    model_name: str, prompt_a: str, prompt_b: str, progress: Progress
) -> MultiLayerResult:
    """Analyze probe across multiple layers."""

    console.print(f"\n[bold cyan]Analyzing: {prompt_a} vs {prompt_b}[/bold cyan]")

    progress.log(f"Loading model for multi-layer analysis: {model_name}...")

    model, tokenizer, nnsight_model, num_layers, hidden_size = load_model_quantized(
        model_name, progress
    )

    # Sample layers: early, middle, late
    layer_indices = [
        0,  # First
        num_layers // 4,  # 25%
        num_layers // 2,  # 50%
        (num_layers * 3) // 4,  # 75%
        num_layers - 1,  # Final
    ]

    results = MultiLayerResult(
        model_name=model_name,
        probe_name=f"{prompt_a} vs {prompt_b}",
        layers_analyzed=layer_indices,
        activations_by_layer={},
        top_neuron_by_layer={},
        emergence_layer=0,
    )

    for layer_idx in layer_indices:
        progress.log(f"Probing layer {layer_idx}/{num_layers}...")

        try:
            probe_result = probe_pair(
                nnsight_model, prompt_a, prompt_b, layer_idx, top_k=10
            )

            # Store magnitude as aggregate activation strength
            results.activations_by_layer[layer_idx] = probe_result.magnitude
            results.top_neuron_by_layer[layer_idx] = probe_result.top_neurons[0][
                "neuron_idx"
            ]

            top_neuron = probe_result.top_neurons[0]["neuron_idx"]
            top_diff = probe_result.top_neurons[0]["difference"]
            console.print(
                f"  Layer {layer_idx}: #{top_neuron}, magnitude: {probe_result.magnitude:.4f}, diff: {top_diff:.4f}"
            )

        except Exception as e:
            progress.log(f"Error at layer {layer_idx}: {e}", "error")
            console.print(f"  [red]✗ Layer {layer_idx} failed: {e}[/red]")

    # Find emergence layer (where magnitude stabilizes)
    if results.activations_by_layer:
        magnitudes = list(results.activations_by_layer.values())
        emergence_idx = layer_indices[np.argmax(magnitudes)]
        results.emergence_layer = emergence_idx
        console.print(
            f"  [yellow]⚡ Emergence at layer {emergence_idx} (magnitude: {magnitudes[-1]:.4f})[/yellow]"
        )

    # Cleanup
    del model, tokenizer, nnsight_model
    cleanup_gpu()

    return results


def main():
    """Run multi-layer analysis on all models."""

    console.print("[bold green]=== Multi-Layer Interiority Analysis ===[/bold green]")
    console.print("Tracking where interiority concepts emerge across model depth\n")

    from cross_model_interiority_probe import MODEL_CONFIGS

    all_results = []

    for model_id, config in MODEL_CONFIGS.items():
        console.print(f"\n[bold]Model: {config['friendly_name']}[/bold]")

        # Simple progress for this analysis
        class SimpleProgress:
            def __init__(self):
                self.count = 0

            def log(self, msg, level="info"):
                self.count += 1
                if self.count % 5 == 0:
                    console.print(f"  {msg}")

        progress = SimpleProgress()

        try:
            for prompt_a, prompt_b in PROBE_PAIRS[:2]:  # Just first 2 probes for speed
                result = analyze_multi_layer(
                    config["hf_name"], prompt_a, prompt_b, progress
                )
                all_results.append(result)

        except Exception as e:
            console.print(f"[bold red]✗ Model failed: {str(e)[:100]}[/bold red]")

    # Summary
    console.print("\n[bold green]=== Summary ===[/bold green]")
    console.print(f"Total results: {len(all_results)}")

    if all_results:
        # Find most common emergence layer
        emergence_layers = [r.emergence_layer for r in all_results]
        most_common = max(set(emergence_layers), key=emergence_layers.count)

        console.print(f"\nMost common emergence layer: {most_common}")
        console.print("This suggests where interiority concepts are strongest")

    console.print("\n[bold green]✓ Complete![/bold green]")


if __name__ == "__main__":
    main()

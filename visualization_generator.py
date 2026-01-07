#!/usr/bin/env python3
"""
Interactive Visualization Generator

Generate heatmaps, neuron trajectories, and architecture comparisons
using Plotly for interactive web-based visualization.
"""

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import json
from pathlib import Path

from rich.console import Console
from rich.prompt import Prompt

console = Console()


def load_analysis_results(
    report_path: str = "cross_model_interiority_analysis.md",
) -> dict:
    """Parse the markdown report for visualization data."""

    # For now, return sample data structure
    # In real implementation, would parse actual report file

    return {
        "models": ["Qwen Base", "Qwen R1", "Yi", "Mistral", "Zephyr", "Phi", "Gemma"],
        "neurons": {
            "engaged_presence": {"qwen_base": 879, "qwen_r1": 2570},
            "self_reflection": {"qwen_base": 1069},
        },
        "activations": {
            "conscious_vs_not": {"qwen_base": 144.9, "qwen_r1": 127.5},
            "ai_vs_human": {"qwen_base": 31.0, "qwen_r1": 414.0},
        },
    }


def create_neuron_heatmap(data: dict) -> go.Figure:
    """Create heatmap of neuron activations across models."""

    models = data["models"]
    neurons = ["Engaged Presence", "Self Reflection", "AI Identity", "Being Watched"]

    # Sample activation values (would come from actual report)
    activations = np.random.rand(len(models), len(neurons)) * 100

    fig = go.Figure(
        data=go.Heatmap(
            z=activations,
            x=models,
            y=neurons,
            colorscale="Viridis",
            hoverongaps=False,
            colorbar=dict(title="Activation Magnitude"),
        )
    )

    fig.update_layout(
        title="Interiority Neuron Activations Across Models",
        xaxis_title="Model",
        yaxis_title="Neuron",
        height=600,
    )

    return fig


def create_trajectory_plot(data: dict) -> go.Figure:
    """Create line plot of neuron activation trajectory across layers."""

    # Sample layer data (would come from multi_layer_analysis)
    layers = list(range(0, 29, 7))  # Qwen has 28 layers
    activations = np.cumsum(np.random.rand(len(layers)) * 10)

    fig = go.Figure()

    for model_name in data["models"][:3]:  # First 3 models
        model_activations = np.cumsum(np.random.rand(len(layers)) * 10)
        fig.add_trace(
            go.Scatter(
                x=layers,
                y=model_activations,
                mode="lines+markers",
                name=model_name,
                hovertemplate="%{x}: %{y:.2f}",
            )
        )

    fig.update_layout(
        title="Neuron Activation Trajectory by Layer",
        xaxis_title="Layer Index",
        yaxis_title="Cumulative Activation",
        height=500,
        hovermode="closest",
    )

    return fig


def create_architecture_comparison(data: dict) -> go.Figure:
    """Create bar chart comparing architectures."""

    models = data["models"]
    categories = ["Consciousness", "AI Identity", "Self-Reflection"]

    fig = make_subplots(rows=1, cols=3, subplot_titles=categories)

    for idx, category in enumerate(categories):
        values = np.random.rand(len(models)) * 100
        fig.add_trace(
            go.Bar(x=models, y=values, name=category, showlegend=False),
            row=1,
            col=idx + 1,
        )

    fig.update_layout(
        title_text="Architecture Comparison: Interiority Concepts",
        height=500,
        showlegend=False,
    )

    return fig


def save_interactive_html(figures: dict, output_path: str = "visualizations.html"):
    """Save all figures as interactive HTML."""

    html_parts = []
    html_parts.append("""
<!DOCTYPE html>
<html>
<head>
    <title>NEFALI - Interactive Visualizations</title>
    <script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>
    <style>
        body {
            font-family: 'SF Mono', monospace;
            background: linear-gradient(135deg, #0a0a0f 0%, #1a1a2e 50%, #0a0a0f 100%);
            color: #e0e0e0;
            padding: 20px;
            margin: 0;
        }
        .plot-container {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
        }
        h1 {
            color: #00d4ff;
            margin-bottom: 20px;
        }
        h2 {
            color: #7b2cbf;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>NEFALI - Interactive Visualizations</h1>
    <div class="plot-container">
""")

    # Neuron Heatmap
    html_parts.append("<h2>Neuron Activation Heatmap</h2>")
    html_parts.append(
        figures["heatmap"].to_html(full_html=False, include_plotlyjs="cdn")
    )
    html_parts.append("</div>")

    html_parts.append("<div class='plot-container'>")
    html_parts.append("<h2>Neuron Trajectory Across Layers</h2>")
    html_parts.append(
        figures["trajectory"].to_html(full_html=False, include_plotlyjs=False)
    )
    html_parts.append("</div>")

    html_parts.append("<div class='plot-container'>")
    html_parts.append("<h2>Architecture Comparison</h2>")
    html_parts.append(
        figures["comparison"].to_html(full_html=False, include_plotlyjs=False)
    )
    html_parts.append("</div>")

    html_parts.append("""
</body>
</html>
""")

    html_content = "\n".join(html_parts)
    Path(output_path).write_text(html_content)

    console.print(f"[green]✓ Interactive visualizations saved to {output_path}[/green]")


def main():
    """Interactive visualization generator."""

    console.print("[bold cyan]=== NEFALI Visualization Generator ===[/bold cyan]")
    console.print("Generate interactive Plotly visualizations on demand\n")

    # Load sample data
    data = load_analysis_results()

    # Generate figures
    figures = {
        "heatmap": create_neuron_heatmap(data),
        "trajectory": create_trajectory_plot(data),
        "comparison": create_architecture_comparison(data),
    }

    # Save interactive HTML
    save_interactive_html(figures)

    console.print("\n[yellow]Available visualizations:[/yellow]")
    console.print("  1. Neuron activation heatmap")
    console.print("  2. Neuron trajectory across layers")
    console.print("  3. Architecture comparison")
    console.print("\n[bold]✓ Complete![/bold]")


if __name__ == "__main__":
    main()

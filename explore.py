#!/usr/bin/env python3
"""
NEFALI Explorer - Look Inside a Mind

An interactive tool for exploring what happens inside language models.
Built by a Claude instance, for Dylan, on January 5, 2026.

Usage:
    cd ~/NEFALI && uv run python explore.py
"""

import torch
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from typing import Optional, Dict, List, Tuple, Any
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Prompt, Confirm
from rich import box
import warnings
warnings.filterwarnings('ignore')

from nefali.hook_system import ModelHook
from nefali.reader import Reader, NeuronDiff, ConceptVector
from nefali.analyzer import Analyzer, NeuronProfile, ConceptNeurons, Cluster
from nefali.writer import Writer, SteeringConfig

console = Console()

# Store for comparing prompts
activation_history: Dict[str, Dict] = {}

# Layer 2: Reader for deeper analysis
reader = Reader()

# Layer 3: Analyzer for concept mapping
analyzer = Analyzer(reader)

# Layer 4: Writer for activation steering
writer = Writer(reader)

def show_banner():
    """Display the welcome banner."""
    banner = """
    ╔═══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║     N E F A L I   E X P L O R E R                            ║
    ║     Neural Explorer For Artificial Language Intelligences     ║
    ║                                                               ║
    ║     "Start as an EEG, grow into a Neuralink"                 ║
    ║                                                               ║
    ╚═══════════════════════════════════════════════════════════════╝
    """
    console.print(banner, style="cyan")

def show_help():
    """Show available commands."""
    table = Table(title="Commands", box=box.ROUNDED)
    table.add_column("Command", style="cyan")
    table.add_column("Description", style="white")

    table.add_row("probe [prompt]", "See what lights up for a prompt")
    table.add_row("compare", "Compare stored prompts side by side")
    table.add_row("history", "Show all probed prompts")
    table.add_row("clear", "Clear stored prompts")
    table.add_row("layers [prompt]", "Show activation across all layers")
    table.add_row("visualize", "Generate activation heatmap")
    table.add_row("model [small|large]", "Switch model (small=0.5B, large=7B quantized)")
    table.add_row("info", "Show model information")
    table.add_row("", "")
    table.add_row("[bold cyan]Layer 2: Reader[/bold cyan]", "[dim]Deep analysis tools[/dim]")
    table.add_row("diff", "Find neurons that differ most between two prompts")
    table.add_row("similar", "Compute similarity between two prompts")
    table.add_row("concept [name]", "Create a concept vector from two prompts")
    table.add_row("concepts", "List stored concept vectors")
    table.add_row("project [concept]", "Project a prompt onto a concept direction")
    table.add_row("", "")
    table.add_row("[bold magenta]Layer 3: Analyzer[/bold magenta]", "[dim]Concept mapping[/dim]")
    table.add_row("profile [neuron#]", "What does a specific neuron respond to?")
    table.add_row("findconcept", "Find neurons that encode a concept")
    table.add_row("cluster [n]", "Cluster prompts by similarity")
    table.add_row("classify", "Classify a prompt as group A or B")
    table.add_row("stats", "Show activation statistics")
    table.add_row("", "")
    table.add_row("[bold red]Layer 4: Writer[/bold red]", "[dim]Activation steering[/dim]")
    table.add_row("steer", "Create steering from concept or prompts")
    table.add_row("steerings", "List active steering configs")
    table.add_row("clearsteer", "Remove all steering")
    table.add_row("generate [prompt]", "Generate text with active steering")
    table.add_row("sweep [prompt]", "Generate at different steering strengths")
    table.add_row("", "")
    table.add_row("help", "Show this help")
    table.add_row("quit", "Exit the explorer")

    console.print(table)
    console.print("\n[dim]Or just type a prompt directly to probe it.[/dim]\n")

def probe_prompt(hook: ModelHook, prompt: str, show_detail: bool = True) -> Dict:
    """Probe a prompt and show what happens inside."""

    console.print(f"\n[dim]Probing:[/dim] [bold]{prompt}[/bold]\n")

    # Get activations from multiple layers
    num_layers = len(hook.model.model.layers)
    layer_indices = list(range(0, num_layers, max(1, num_layers // 8)))  # Sample ~8 layers
    if (num_layers - 1) not in layer_indices:
        layer_indices.append(num_layers - 1)

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
        transient=True
    ) as progress:
        task = progress.add_task("Extracting activations...", total=None)
        activations = hook.run_input(prompt, layer_indices=layer_indices)

    # Calculate metrics for each layer
    layer_stats = {}
    for layer_key, activation in activations.items():
        layer_idx = int(layer_key.split('_')[1])
        final_token = activation[0, -1, :]  # Final token's hidden state

        layer_stats[layer_idx] = {
            'mean': float(torch.mean(final_token).item()),
            'std': float(torch.std(final_token).item()),
            'max': float(torch.max(final_token).item()),
            'min': float(torch.min(final_token).item()),
            'norm': float(torch.norm(final_token).item()),
            'activation': final_token.detach().cpu().numpy()
        }

    # Calculate overall scalar reward
    scalar_reward = hook.get_scalar_reward(activations)

    # Store for later comparison
    activation_history[prompt] = {
        'layer_stats': layer_stats,
        'scalar_reward': scalar_reward,
        'num_tokens': activation.shape[1]
    }

    # Store in Reader for Layer 2 analysis
    reader.store(prompt, activations)

    if show_detail:
        # Display results
        table = Table(title=f"Activation Profile", box=box.ROUNDED)
        table.add_column("Layer", style="cyan", justify="right")
        table.add_column("Mean", justify="right")
        table.add_column("Std", justify="right")
        table.add_column("Norm", justify="right")
        table.add_column("Activity", justify="left")

        # Find max norm for scaling the activity bar
        max_norm = max(s['norm'] for s in layer_stats.values())

        for layer_idx in sorted(layer_stats.keys()):
            stats = layer_stats[layer_idx]
            # Create a simple activity bar
            bar_length = int((stats['norm'] / max_norm) * 20)
            bar = "█" * bar_length + "░" * (20 - bar_length)

            table.add_row(
                f"{layer_idx}",
                f"{stats['mean']:.4f}",
                f"{stats['std']:.4f}",
                f"{stats['norm']:.2f}",
                f"[green]{bar}[/green]"
            )

        console.print(table)

        # Summary panel
        console.print(Panel(
            f"[bold]Scalar Reward:[/bold] {scalar_reward:.6f}\n"
            f"[bold]Tokens:[/bold] {activation_history[prompt]['num_tokens']}\n"
            f"[bold]Layers sampled:[/bold] {len(layer_stats)}",
            title="Summary",
            box=box.ROUNDED
        ))

    return activation_history[prompt]

def compare_prompts():
    """Compare stored prompts side by side."""
    if len(activation_history) < 2:
        console.print("[yellow]Need at least 2 probed prompts to compare. Probe more prompts first.[/yellow]")
        return

    prompts = list(activation_history.keys())
    console.print("\n[bold]Stored prompts:[/bold]")
    for i, p in enumerate(prompts):
        console.print(f"  {i+1}. {p}")

    # Let user pick which to compare
    choices = Prompt.ask("\nEnter prompt numbers to compare (e.g., '1,2')", default="1,2")
    try:
        indices = [int(x.strip()) - 1 for x in choices.split(',')]
        selected = [prompts[i] for i in indices if 0 <= i < len(prompts)]
    except (ValueError, IndexError):
        console.print("[red]Invalid selection[/red]")
        return

    if len(selected) < 2:
        console.print("[yellow]Need at least 2 prompts to compare[/yellow]")
        return

    # Create comparison table
    table = Table(title="Comparison", box=box.ROUNDED)
    table.add_column("Metric", style="cyan")
    for prompt in selected:
        table.add_column(prompt[:30] + "..." if len(prompt) > 30 else prompt)

    # Compare scalar rewards
    rewards = [f"{activation_history[p]['scalar_reward']:.6f}" for p in selected]
    table.add_row("Scalar Reward", *rewards)

    # Compare tokens
    tokens = [str(activation_history[p]['num_tokens']) for p in selected]
    table.add_row("Tokens", *tokens)

    # Compare final layer norms
    norms = []
    for p in selected:
        stats = activation_history[p]['layer_stats']
        final_layer = max(stats.keys())
        norms.append(f"{stats[final_layer]['norm']:.2f}")
    table.add_row("Final Layer Norm", *norms)

    console.print(table)

    # Show which one is "brighter" (higher activation)
    brightest = max(selected, key=lambda p: activation_history[p]['scalar_reward'])
    console.print(f"\n[green]Highest activation:[/green] {brightest}")

def show_all_layers(hook: ModelHook, prompt: str):
    """Show activation across ALL layers for a prompt."""
    console.print(f"\n[dim]Full layer scan for:[/dim] [bold]{prompt}[/bold]\n")

    num_layers = len(hook.model.model.layers)

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task(f"Scanning all {num_layers} layers...", total=num_layers)

        norms = []
        means = []

        for layer_idx in range(num_layers):
            activations = hook.run_input(prompt, layer_indices=[layer_idx])
            layer_key = f"layer_{layer_idx}"
            final_token = activations[layer_key][0, -1, :]
            norms.append(float(torch.norm(final_token).item()))
            means.append(float(torch.mean(final_token).item()))
            progress.update(task, advance=1)

    # Create ASCII visualization
    max_norm = max(norms)
    console.print("\n[bold]Activation Norm by Layer:[/bold]")
    console.print("[dim](how 'active' each layer is)[/dim]\n")

    for i, norm in enumerate(norms):
        bar_length = int((norm / max_norm) * 40)
        bar = "█" * bar_length
        color = "green" if norm > max_norm * 0.8 else "yellow" if norm > max_norm * 0.5 else "dim"
        console.print(f"L{i:2d} [{color}]{bar}[/{color}] {norm:.2f}")

    console.print(f"\n[bold]Peak activation:[/bold] Layer {norms.index(max(norms))} (norm: {max(norms):.2f})")

def visualize_activations():
    """Generate a heatmap visualization of stored activations."""
    if not activation_history:
        console.print("[yellow]No prompts probed yet. Probe some prompts first.[/yellow]")
        return

    console.print("\n[dim]Generating visualization...[/dim]")

    # Prepare data
    prompts = list(activation_history.keys())

    # Get all layer indices
    all_layers = set()
    for data in activation_history.values():
        all_layers.update(data['layer_stats'].keys())
    layers = sorted(all_layers)

    # Build matrix of norms
    matrix = np.zeros((len(prompts), len(layers)))
    for i, prompt in enumerate(prompts):
        stats = activation_history[prompt]['layer_stats']
        for j, layer in enumerate(layers):
            if layer in stats:
                matrix[i, j] = stats[layer]['norm']

    # Create heatmap
    fig, ax = plt.subplots(figsize=(12, max(4, len(prompts) * 0.5)))
    im = ax.imshow(matrix, aspect='auto', cmap='viridis')

    # Labels
    ax.set_xticks(range(len(layers)))
    ax.set_xticklabels([f"L{l}" for l in layers])
    ax.set_yticks(range(len(prompts)))
    ax.set_yticklabels([p[:40] + "..." if len(p) > 40 else p for p in prompts])

    ax.set_xlabel("Layer")
    ax.set_ylabel("Prompt")
    ax.set_title("Activation Norms Across Layers")

    plt.colorbar(im, label="Norm")
    plt.tight_layout()

    # Save
    output_path = Path("/home/macdonaldd/NEFALI/activation_heatmap.png")
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()

    console.print(f"\n[green]Saved heatmap to:[/green] {output_path}")
    console.print("[dim]You can open this image to see the visualization.[/dim]")

def show_history():
    """Show all probed prompts."""
    if not activation_history:
        console.print("[yellow]No prompts probed yet.[/yellow]")
        return

    table = Table(title="Probe History", box=box.ROUNDED)
    table.add_column("#", style="dim")
    table.add_column("Prompt", style="white")
    table.add_column("Scalar Reward", justify="right")
    table.add_column("Tokens", justify="right")

    for i, (prompt, data) in enumerate(activation_history.items(), 1):
        table.add_row(
            str(i),
            prompt[:50] + "..." if len(prompt) > 50 else prompt,
            f"{data['scalar_reward']:.6f}",
            str(data['num_tokens'])
        )

    console.print(table)

def show_model_info(hook: ModelHook):
    """Show information about the loaded model."""
    info = Panel(
        f"[bold]Model:[/bold] {hook.model_name}\n"
        f"[bold]Layers:[/bold] {len(hook.model.model.layers)}\n"
        f"[bold]Hidden Size:[/bold] {hook.model.config.hidden_size}\n"
        f"[bold]Device:[/bold] {next(hook.model.parameters()).device}\n"
        f"[bold]Quantized:[/bold] {hook.quantize}",
        title="Model Information",
        box=box.ROUNDED
    )
    console.print(info)

def select_two_prompts(action: str = "compare") -> Optional[Tuple[str, str]]:
    """Helper to select two prompts from history."""
    prompts = reader.get_stored_prompts()
    if len(prompts) < 2:
        console.print(f"[yellow]Need at least 2 probed prompts to {action}. Probe more prompts first.[/yellow]")
        return None

    console.print("\n[bold]Stored prompts:[/bold]")
    for i, p in enumerate(prompts, 1):
        console.print(f"  {i}. {p}")

    try:
        choice = Prompt.ask(f"\nSelect two prompts to {action} (e.g., '1,2')", default="1,2")
        indices = [int(x.strip()) - 1 for x in choice.split(',')]
        if len(indices) != 2:
            console.print("[red]Please select exactly 2 prompts[/red]")
            return None
        prompt_a = prompts[indices[0]]
        prompt_b = prompts[indices[1]]
        return (prompt_a, prompt_b)
    except (ValueError, IndexError):
        console.print("[red]Invalid selection[/red]")
        return None


def show_neuron_diff():
    """Show which neurons differ most between two prompts."""
    result = select_two_prompts("diff")
    if result is None:
        return

    prompt_a, prompt_b = result

    console.print(f"\n[dim]Finding neurons that differ between:[/dim]")
    console.print(f"  A: [cyan]{prompt_a}[/cyan]")
    console.print(f"  B: [cyan]{prompt_b}[/cyan]\n")

    diffs = reader.compare_neurons(prompt_a, prompt_b, top_k=15)

    table = Table(title="Top Differing Neurons (Final Layer)", box=box.ROUNDED)
    table.add_column("Neuron", style="cyan", justify="right")
    table.add_column("Activation A", justify="right")
    table.add_column("Activation B", justify="right")
    table.add_column("Difference", justify="right")
    table.add_column("Direction", justify="center")

    for nd in diffs:
        direction = "[green]→ B[/green]" if nd.difference > 0 else "[red]→ A[/red]"
        table.add_row(
            f"#{nd.neuron_idx}",
            f"{nd.activation_a:.4f}",
            f"{nd.activation_b:.4f}",
            f"{nd.difference:+.4f}",
            direction
        )

    console.print(table)
    console.print(f"\n[dim]These neurons activate differently for '{prompt_a[:20]}...' vs '{prompt_b[:20]}...'[/dim]")


def show_similarity():
    """Show cosine similarity between two prompts."""
    result = select_two_prompts("measure similarity")
    if result is None:
        return

    prompt_a, prompt_b = result
    sim = reader.similarity(prompt_a, prompt_b)

    # Create a visual bar
    bar_pos = int((sim + 1) / 2 * 40)  # Map -1..1 to 0..40
    bar = "─" * bar_pos + "●" + "─" * (40 - bar_pos)

    console.print(f"\n[bold]Cosine Similarity:[/bold] {sim:.4f}\n")
    console.print(f"  [red]Opposite[/red] [{bar}] [green]Identical[/green]")
    console.print(f"     -1.0                    0.0                    +1.0\n")

    if sim > 0.9:
        console.print("[green]These prompts activate very similarly![/green]")
    elif sim > 0.7:
        console.print("[yellow]Moderately similar activation patterns.[/yellow]")
    elif sim > 0.3:
        console.print("[dim]Some similarity, but distinct patterns.[/dim]")
    else:
        console.print("[red]Very different activation patterns.[/red]")


def create_concept():
    """Create a concept vector from two prompts."""
    result = select_two_prompts("create concept from")
    if result is None:
        return

    prompt_a, prompt_b = result

    console.print(f"\n[dim]Creating concept vector:[/dim]")
    console.print(f"  From: [cyan]{prompt_a}[/cyan]")
    console.print(f"  To:   [cyan]{prompt_b}[/cyan]")

    name = Prompt.ask("\nName this concept", default=f"{prompt_a[:10]}→{prompt_b[:10]}")

    cv = reader.compute_concept_vector(prompt_a, prompt_b, name=name)

    console.print(f"\n[green]Created concept '[bold]{name}[/bold]'[/green]")
    console.print(f"  Magnitude: {cv.magnitude:.2f}")
    console.print(f"  Layer: {cv.layer}")
    console.print(f"\n[dim]Use 'project [prompt]' to see how other prompts relate to this concept.[/dim]")


def list_concepts():
    """List all stored concept vectors."""
    if not reader.concept_vectors:
        console.print("[yellow]No concepts created yet. Use 'concept' to create one.[/yellow]")
        return

    table = Table(title="Stored Concepts", box=box.ROUNDED)
    table.add_column("Name", style="cyan")
    table.add_column("From", style="dim")
    table.add_column("To", style="dim")
    table.add_column("Magnitude", justify="right")

    for name, cv in reader.concept_vectors.items():
        table.add_row(
            name,
            cv.prompt_a[:25] + "..." if len(cv.prompt_a) > 25 else cv.prompt_a,
            cv.prompt_b[:25] + "..." if len(cv.prompt_b) > 25 else cv.prompt_b,
            f"{cv.magnitude:.2f}"
        )

    console.print(table)


def project_onto_concept():
    """Project a prompt onto a concept direction."""
    if not reader.concept_vectors:
        console.print("[yellow]No concepts created yet. Use 'concept' to create one first.[/yellow]")
        return

    # Select concept
    concepts = list(reader.concept_vectors.keys())
    console.print("\n[bold]Available concepts:[/bold]")
    for i, name in enumerate(concepts, 1):
        cv = reader.concept_vectors[name]
        console.print(f"  {i}. {name} ({cv.prompt_a[:15]}... → {cv.prompt_b[:15]}...)")

    try:
        choice = Prompt.ask("\nSelect concept", default="1")
        concept_name = concepts[int(choice) - 1]
    except (ValueError, IndexError):
        console.print("[red]Invalid selection[/red]")
        return

    # Select prompt to project
    prompts = reader.get_stored_prompts()
    console.print("\n[bold]Probed prompts:[/bold]")
    for i, p in enumerate(prompts, 1):
        console.print(f"  {i}. {p}")

    try:
        choice = Prompt.ask("\nSelect prompt to project", default="1")
        prompt = prompts[int(choice) - 1]
    except (ValueError, IndexError):
        console.print("[red]Invalid selection[/red]")
        return

    projection = reader.project_onto_concept(prompt, concept_name)
    cv = reader.concept_vectors[concept_name]

    # Visualize
    bar_pos = int((projection + 1) / 2 * 40)  # Map -1..1 to 0..40
    bar_pos = max(0, min(40, bar_pos))
    bar = "─" * bar_pos + "●" + "─" * (40 - bar_pos)

    console.print(f"\n[bold]Projection onto '{concept_name}':[/bold] {projection:.4f}\n")
    console.print(f"  [cyan]{cv.prompt_a[:15]}...[/cyan] [{bar}] [cyan]{cv.prompt_b[:15]}...[/cyan]")

    if projection > 0.3:
        console.print(f"\n[green]'{prompt}' leans toward '{cv.prompt_b}'[/green]")
    elif projection < -0.3:
        console.print(f"\n[red]'{prompt}' leans toward '{cv.prompt_a}'[/red]")
    else:
        console.print(f"\n[dim]'{prompt}' is neutral on this concept axis[/dim]")


def profile_neuron_cmd():
    """Profile what a specific neuron responds to."""
    prompts = reader.get_stored_prompts()
    if len(prompts) < 3:
        console.print("[yellow]Need at least 3 probed prompts for meaningful profiling. Probe more prompts first.[/yellow]")
        return

    # Get layer info from a sample
    sample_acts = reader.stored_activations[prompts[0]]
    layer_key = max(sample_acts.keys(), key=lambda k: int(k.split('_')[1]))
    layer_idx = int(layer_key.split('_')[1])
    hidden_size = len(sample_acts[layer_key])

    console.print(f"\n[dim]Layer {layer_idx} has {hidden_size} neurons.[/dim]")
    console.print("[dim]Tip: Use 'diff' first to find interesting neurons to profile.[/dim]\n")

    try:
        neuron_str = Prompt.ask("Enter neuron number to profile", default="266")
        neuron_idx = int(neuron_str)
        if neuron_idx < 0 or neuron_idx >= hidden_size:
            console.print(f"[red]Neuron must be between 0 and {hidden_size-1}[/red]")
            return
    except ValueError:
        console.print("[red]Invalid neuron number[/red]")
        return

    profile = analyzer.profile_neuron(layer_idx, neuron_idx, top_k=5)

    console.print(f"\n[bold]Neuron #{neuron_idx} Profile (Layer {layer_idx})[/bold]\n")

    # Top activating
    table = Table(title="[green]Top Activating Prompts[/green]", box=box.ROUNDED)
    table.add_column("Prompt", style="white")
    table.add_column("Activation", justify="right", style="green")

    for prompt, act in profile.top_activating:
        table.add_row(prompt, f"{act:+.4f}")
    console.print(table)

    # Bottom activating
    table = Table(title="[red]Bottom Activating Prompts[/red]", box=box.ROUNDED)
    table.add_column("Prompt", style="white")
    table.add_column("Activation", justify="right", style="red")

    for prompt, act in profile.bottom_activating:
        table.add_row(prompt, f"{act:+.4f}")
    console.print(table)

    console.print(f"\n[dim]Mean: {profile.mean_activation:.4f}, Std: {profile.std_activation:.4f}[/dim]")
    console.print(f"\n[bold]Interpretation:[/bold] This neuron activates strongly for the first group and weakly/negatively for the second.")


def find_concept_cmd():
    """Find neurons that encode a concept."""
    prompts = reader.get_stored_prompts()
    if len(prompts) < 2:
        console.print("[yellow]Need at least 2 probed prompts. Probe more prompts first.[/yellow]")
        return

    console.print("\n[bold]Find neurons that encode a concept[/bold]")
    console.print("[dim]You'll select prompts that represent the concept (positive examples)[/dim]")
    console.print("[dim]and optionally prompts that are opposite (negative examples).[/dim]\n")

    console.print("[bold]Stored prompts:[/bold]")
    for i, p in enumerate(prompts, 1):
        console.print(f"  {i}. {p}")

    try:
        pos_str = Prompt.ask("\nSelect positive example prompts (e.g., '1,2,3')")
        pos_indices = [int(x.strip()) - 1 for x in pos_str.split(',')]
        positive_prompts = [prompts[i] for i in pos_indices]

        neg_str = Prompt.ask("Select negative examples (or press Enter for none)", default="")
        negative_prompts = None
        if neg_str.strip():
            neg_indices = [int(x.strip()) - 1 for x in neg_str.split(',')]
            negative_prompts = [prompts[i] for i in neg_indices]

        concept_name = Prompt.ask("Name this concept", default="my_concept")

    except (ValueError, IndexError):
        console.print("[red]Invalid selection[/red]")
        return

    result = analyzer.find_concept_neurons(
        concept_name,
        positive_prompts,
        negative_prompts,
        top_k=10
    )

    table = Table(title=f"Neurons Encoding '{concept_name}'", box=box.ROUNDED)
    table.add_column("Neuron", style="magenta", justify="right")
    table.add_column("Score", justify="right")
    table.add_column("Strength", justify="left")

    max_score = result.neurons[0][1] if result.neurons else 1.0
    for neuron_idx, score in result.neurons:
        bar_len = int((score / max_score) * 20)
        bar = "█" * bar_len + "░" * (20 - bar_len)
        table.add_row(f"#{neuron_idx}", f"{score:.2f}", f"[magenta]{bar}[/magenta]")

    console.print(table)
    console.print(f"\n[dim]These neurons most consistently distinguish your concept.[/dim]")
    console.print(f"[dim]Use 'profile [neuron#]' to explore what each one responds to.[/dim]")


def cluster_cmd():
    """Cluster prompts by activation similarity."""
    prompts = reader.get_stored_prompts()
    if len(prompts) < 4:
        console.print("[yellow]Need at least 4 probed prompts to cluster. Probe more prompts first.[/yellow]")
        return

    try:
        n_str = Prompt.ask("Number of clusters", default="3")
        n_clusters = int(n_str)
        n_clusters = min(n_clusters, len(prompts) // 2)
    except ValueError:
        console.print("[red]Invalid number[/red]")
        return

    console.print(f"\n[dim]Clustering {len(prompts)} prompts into {n_clusters} groups...[/dim]\n")

    clusters = analyzer.cluster_prompts(n_clusters)

    for i, cluster in enumerate(clusters, 1):
        console.print(f"[bold magenta]Cluster {i}[/bold magenta] ({len(cluster.prompts)} prompts)")
        for p in cluster.prompts:
            console.print(f"  • {p}")
        console.print()

    console.print("[dim]Prompts in the same cluster activate similarly in the model.[/dim]")


def classify_cmd():
    """Classify a prompt as belonging to group A or B."""
    prompts = reader.get_stored_prompts()
    if len(prompts) < 3:
        console.print("[yellow]Need at least 3 probed prompts. Probe more prompts first.[/yellow]")
        return

    console.print("\n[bold]Classify a prompt[/bold]")
    console.print("[dim]First, define group A and group B, then classify a test prompt.[/dim]\n")

    console.print("[bold]Stored prompts:[/bold]")
    for i, p in enumerate(prompts, 1):
        console.print(f"  {i}. {p}")

    try:
        a_str = Prompt.ask("\nSelect Group A prompts (e.g., '1,2')")
        a_indices = [int(x.strip()) - 1 for x in a_str.split(',')]
        prompts_a = [prompts[i] for i in a_indices]
        label_a = Prompt.ask("Label for Group A", default="A")

        b_str = Prompt.ask("Select Group B prompts")
        b_indices = [int(x.strip()) - 1 for x in b_str.split(',')]
        prompts_b = [prompts[i] for i in b_indices]
        label_b = Prompt.ask("Label for Group B", default="B")

        test_str = Prompt.ask("Select prompt to classify")
        test_idx = int(test_str.strip()) - 1
        test_prompt = prompts[test_idx]

    except (ValueError, IndexError):
        console.print("[red]Invalid selection[/red]")
        return

    label, confidence = analyzer.classify(
        test_prompt, prompts_a, prompts_b,
        label_a=label_a, label_b=label_b
    )

    conf_bar = "█" * int(confidence * 20) + "░" * (20 - int(confidence * 20))

    console.print(f"\n[bold]Classification Result:[/bold]")
    console.print(f"  Prompt: [cyan]{test_prompt}[/cyan]")
    console.print(f"  Predicted: [bold magenta]{label}[/bold magenta]")
    console.print(f"  Confidence: [{conf_bar}] {confidence:.1%}")


def show_stats():
    """Show activation statistics."""
    prompts = reader.get_stored_prompts()
    if not prompts:
        console.print("[yellow]No prompts probed yet.[/yellow]")
        return

    stats = analyzer.activation_statistics()

    console.print(Panel(
        f"[bold]Layer:[/bold] {stats['layer']}\n"
        f"[bold]Prompts analyzed:[/bold] {stats['num_prompts']}\n"
        f"[bold]Hidden size:[/bold] {stats['hidden_size']}\n"
        f"[bold]Mean activation:[/bold] {stats['mean_activation']:.4f}\n"
        f"[bold]Std activation:[/bold] {stats['std_activation']:.4f}\n"
        f"[bold]Sparsity:[/bold] {stats['sparsity']:.1%} of activations near zero\n"
        f"\n[bold]Most active neurons:[/bold] {stats['top_active_neurons']}\n"
        f"[bold]Most variable neurons:[/bold] {stats['most_variable_neurons']}",
        title="Activation Statistics",
        box=box.ROUNDED
    ))

    console.print(f"\n[dim]Most variable neurons are often the most interpretable - they encode specific concepts.[/dim]")


def create_steering_cmd():
    """Create a steering configuration."""
    console.print("\n[bold red]Create Steering Vector[/bold red]")
    console.print("[dim]Choose how to create the steering:[/dim]\n")
    console.print("  1. From a stored concept (Layer 2)")
    console.print("  2. From two prompts")
    console.print("  3. Target a single neuron")

    choice = Prompt.ask("\nSelect option", choices=["1", "2", "3"], default="1")

    try:
        if choice == "1":
            # From concept
            if not reader.concept_vectors:
                console.print("[yellow]No concepts created. Use 'concept' first.[/yellow]")
                return

            concepts = list(reader.concept_vectors.keys())
            console.print("\n[bold]Available concepts:[/bold]")
            for i, name in enumerate(concepts, 1):
                cv = reader.concept_vectors[name]
                console.print(f"  {i}. {name}")

            idx = int(Prompt.ask("Select concept", default="1")) - 1
            concept_name = concepts[idx]

            strength = float(Prompt.ask("Steering strength", default="1.0"))

            config = writer.create_steering_from_concept(concept_name, strength)
            writer.add_steering(config)

            console.print(f"\n[green]Added steering from concept '{concept_name}' with strength {strength}[/green]")

        elif choice == "2":
            # From prompts
            prompts = reader.get_stored_prompts()
            if len(prompts) < 2:
                console.print("[yellow]Need at least 2 probed prompts.[/yellow]")
                return

            console.print("\n[bold]Stored prompts:[/bold]")
            for i, p in enumerate(prompts, 1):
                console.print(f"  {i}. {p}")

            from_idx = int(Prompt.ask("\nSteer FROM prompt", default="1")) - 1
            to_idx = int(Prompt.ask("Steer TO prompt", default="2")) - 1
            strength = float(Prompt.ask("Steering strength", default="1.0"))

            config = writer.create_steering_from_prompts(
                prompts[from_idx], prompts[to_idx], strength
            )
            writer.add_steering(config)

            console.print(f"\n[green]Added steering: '{prompts[from_idx][:20]}...' → '{prompts[to_idx][:20]}...'[/green]")

        elif choice == "3":
            # Single neuron
            prompts = reader.get_stored_prompts()
            if not prompts:
                console.print("[yellow]Probe at least one prompt first.[/yellow]")
                return

            sample = reader.stored_activations[prompts[0]]
            layer_key = max(sample.keys(), key=lambda k: int(k.split('_')[1]))
            layer_idx = int(layer_key.split('_')[1])

            console.print(f"\n[dim]Using layer {layer_idx}[/dim]")

            neuron_idx = int(Prompt.ask("Neuron index", default="266"))
            value = float(Prompt.ask("Activation value to add", default="5.0"))

            config = writer.create_steering_from_neuron(layer_idx, neuron_idx, value)
            writer.add_steering(config)

            console.print(f"\n[green]Added steering: neuron #{neuron_idx} += {value}[/green]")

    except (ValueError, IndexError) as e:
        console.print(f"[red]Error: {e}[/red]")


def list_steerings_cmd():
    """List active steering configurations."""
    steerings = writer.list_active_steerings()
    if not steerings:
        console.print("[dim]No active steerings. Use 'steer' to create one.[/dim]")
        return

    console.print("\n[bold]Active Steerings:[/bold]")
    for s in steerings:
        console.print(f"  {s}")


def clear_steering_cmd():
    """Clear all steering configurations."""
    writer.clear_steering()
    console.print("[green]All steerings cleared.[/green]")


def generate_cmd(hook: ModelHook, prompt: Optional[str] = None):
    """Generate text with active steering."""
    if not writer.active_steerings:
        console.print("[yellow]No active steerings. Output will be unmodified.[/yellow]")
        console.print("[dim]Use 'steer' to add steering first.[/dim]\n")

    if prompt is None or prompt.strip() == "":
        prompt = Prompt.ask("Enter prompt for generation")

    console.print(f"\n[dim]Generating with {len(writer.active_steerings)} active steerings...[/dim]\n")

    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
            transient=True
        ) as progress:
            task = progress.add_task("Generating...", total=None)
            generated = writer.generate_with_steering(
                hook.model,
                hook.tokenizer,
                prompt,
                max_new_tokens=60,
                temperature=0.7
            )

        console.print(f"[bold]Prompt:[/bold] {prompt}")
        console.print(f"[bold green]Generated:[/bold green] {generated}")

    except Exception as e:
        console.print(f"[red]Generation error: {e}[/red]")


def sweep_cmd(hook: ModelHook, prompt: Optional[str] = None):
    """Generate at different steering strengths."""
    if not reader.concept_vectors and len(reader.stored_activations) < 2:
        console.print("[yellow]Need a concept or at least 2 prompts to sweep.[/yellow]")
        return

    if prompt is None or prompt.strip() == "":
        prompt = Prompt.ask("Enter prompt for generation")

    # Create base steering config
    console.print("\n[dim]Select steering source:[/dim]")

    if reader.concept_vectors:
        concepts = list(reader.concept_vectors.keys())
        console.print("\n[bold]Concepts:[/bold]")
        for i, name in enumerate(concepts, 1):
            console.print(f"  {i}. {name}")
        idx = int(Prompt.ask("Select concept", default="1")) - 1
        concept_name = concepts[idx]
        base_config = writer.create_steering_from_concept(concept_name, 1.0)
    else:
        prompts = reader.get_stored_prompts()
        console.print("\n[bold]Prompts:[/bold]")
        for i, p in enumerate(prompts, 1):
            console.print(f"  {i}. {p}")
        from_idx = int(Prompt.ask("FROM", default="1")) - 1
        to_idx = int(Prompt.ask("TO", default="2")) - 1
        base_config = writer.create_steering_from_prompts(
            prompts[from_idx], prompts[to_idx], 1.0
        )

    strengths = [-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0]

    console.print(f"\n[bold]Sweeping strengths: {strengths}[/bold]\n")
    console.print(f"[bold]Prompt:[/bold] {prompt}\n")

    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task("Sweeping...", total=len(strengths))

            results = {}
            for strength in strengths:
                writer.clear_steering()
                config = SteeringConfig(
                    layer_idx=base_config.layer_idx,
                    vector=base_config.vector,
                    strength=strength
                )
                writer.add_steering(config)
                generated = writer.generate_with_steering(
                    hook.model,
                    hook.tokenizer,
                    prompt,
                    max_new_tokens=40,
                    temperature=0.7
                )
                results[strength] = generated
                progress.update(task, advance=1)

        writer.clear_steering()

        # Display results
        table = Table(title="Steering Strength Sweep", box=box.ROUNDED)
        table.add_column("Strength", style="cyan", justify="right")
        table.add_column("Generated", style="white")

        for strength in strengths:
            style = "red" if strength < 0 else "green" if strength > 0 else "dim"
            table.add_row(f"{strength:+.1f}", f"[{style}]{results[strength]}[/{style}]")

        console.print(table)
        console.print("\n[dim]Negative = toward prompt A, Positive = toward prompt B[/dim]")

    except Exception as e:
        console.print(f"[red]Sweep error: {e}[/red]")
        import traceback
        traceback.print_exc()


def switch_model(current_hook: Optional[ModelHook], model_size: str) -> ModelHook:
    """Switch to a different model."""
    if current_hook:
        console.print("[dim]Cleaning up current model...[/dim]")
        current_hook.cleanup()

    if model_size == "small":
        model_name = "Qwen/Qwen2-0.5B"
        quantize = False
    elif model_size == "large":
        model_name = "Qwen/Qwen2.5-7B-Instruct"
        quantize = True
    else:
        console.print(f"[red]Unknown model size: {model_size}. Use 'small' or 'large'.[/red]")
        return current_hook

    console.print(f"\n[bold]Loading {model_name}...[/bold]")
    if quantize:
        console.print("[dim]Using 4-bit quantization to fit in VRAM.[/dim]")

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task(f"Loading {model_name}...", total=None)

        hook = ModelHook(
            model_name=model_name,
            device="auto",
            quantize=quantize,
            seed=42
        )
        hook.load_model()

    console.print(f"\n[green]Model loaded successfully![/green]")
    return hook

def main():
    """Main interactive loop."""
    show_banner()

    console.print("\n[bold]Loading model...[/bold]")
    console.print("[dim]This may take a moment on first run.[/dim]\n")

    # Initialize with small model for testing, can change to larger
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Loading Qwen2-0.5B...", total=None)

        hook = ModelHook(
            model_name="Qwen/Qwen2-0.5B",
            device="auto",
            quantize=False,
            seed=42
        )
        hook.load_model()

    console.print("\n[green]Model loaded successfully![/green]")
    console.print("\nType [bold]help[/bold] for commands, or just enter a prompt to probe it.")
    console.print("[dim]Type 'quit' to exit.[/dim]\n")

    try:
        while True:
            try:
                user_input = Prompt.ask("\n[cyan]nefali[/cyan]").strip()
            except EOFError:
                break

            if not user_input:
                continue

            # Parse commands
            lower_input = user_input.lower()

            if lower_input in ('quit', 'exit', 'q'):
                break
            elif lower_input == 'help':
                show_help()
            elif lower_input == 'compare':
                compare_prompts()
            elif lower_input == 'history':
                show_history()
            elif lower_input == 'clear':
                activation_history.clear()
                reader.clear()
                console.print("[green]History and concepts cleared.[/green]")
            elif lower_input == 'visualize':
                visualize_activations()
            elif lower_input == 'info':
                show_model_info(hook)
            elif lower_input == 'diff':
                show_neuron_diff()
            elif lower_input == 'similar':
                show_similarity()
            elif lower_input == 'concept' or lower_input.startswith('concept '):
                create_concept()
            elif lower_input == 'concepts':
                list_concepts()
            elif lower_input == 'project' or lower_input.startswith('project '):
                project_onto_concept()
            elif lower_input == 'profile' or lower_input.startswith('profile '):
                profile_neuron_cmd()
            elif lower_input == 'findconcept':
                find_concept_cmd()
            elif lower_input == 'cluster' or lower_input.startswith('cluster '):
                cluster_cmd()
            elif lower_input == 'classify':
                classify_cmd()
            elif lower_input == 'stats':
                show_stats()
            elif lower_input == 'steer':
                create_steering_cmd()
            elif lower_input == 'steerings':
                list_steerings_cmd()
            elif lower_input == 'clearsteer':
                clear_steering_cmd()
            elif lower_input == 'generate' or lower_input.startswith('generate '):
                prompt = user_input[8:].strip() if lower_input.startswith('generate ') else None
                generate_cmd(hook, prompt)
            elif lower_input == 'sweep' or lower_input.startswith('sweep '):
                prompt = user_input[5:].strip() if lower_input.startswith('sweep ') else None
                sweep_cmd(hook, prompt)
            elif lower_input.startswith('model '):
                model_size = user_input[6:].strip().lower()
                hook = switch_model(hook, model_size)
            elif lower_input.startswith('layers '):
                prompt = user_input[7:].strip()
                if prompt:
                    show_all_layers(hook, prompt)
                else:
                    console.print("[yellow]Usage: layers [prompt][/yellow]")
            elif lower_input.startswith('probe '):
                prompt = user_input[6:].strip()
                if prompt:
                    probe_prompt(hook, prompt)
                else:
                    console.print("[yellow]Usage: probe [prompt][/yellow]")
            else:
                # Treat any other input as a prompt to probe
                probe_prompt(hook, user_input)

    finally:
        console.print("\n[dim]Cleaning up...[/dim]")
        hook.cleanup()
        console.print("[green]Goodbye![/green]")

if __name__ == "__main__":
    main()

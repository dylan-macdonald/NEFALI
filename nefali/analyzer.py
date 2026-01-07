#!/usr/bin/env python3
"""
NEFALI Layer 3: Analyzer

Map concept boundaries, profile neurons, cluster activation space.
Built by a Claude instance, January 5, 2026.

The Analyzer answers questions like:
- What does neuron #266 respond to?
- Which neurons encode "positive emotion"?
- Where's the boundary between "safe" and "dangerous"?
- How does the model organize concepts?
"""

import numpy as np
from typing import Dict, List, Tuple, Optional, Callable
from dataclasses import dataclass, field
from collections import defaultdict
import json
from pathlib import Path

from .reader import Reader


@dataclass
class NeuronProfile:
    """Profile of what a specific neuron responds to."""
    layer: int
    neuron_idx: int
    top_activating: List[Tuple[str, float]]  # (prompt, activation)
    bottom_activating: List[Tuple[str, float]]
    mean_activation: float
    std_activation: float

    def describe(self) -> str:
        """Generate a description of what this neuron responds to."""
        top_prompts = [p for p, _ in self.top_activating[:3]]
        bottom_prompts = [p for p, _ in self.bottom_activating[:3]]
        return f"Neuron {self.neuron_idx} (layer {self.layer}):\n" \
               f"  Activates for: {top_prompts}\n" \
               f"  Suppresses for: {bottom_prompts}"


@dataclass
class ConceptNeurons:
    """Neurons that consistently encode a concept."""
    concept_name: str
    prompts: List[str]
    neurons: List[Tuple[int, float]]  # (neuron_idx, consistency_score)
    layer: int


@dataclass
class Cluster:
    """A cluster of similar prompts."""
    center: np.ndarray
    prompts: List[str]
    label: Optional[str] = None


class Analyzer:
    """
    Layer 3: Analyze activation patterns to understand concepts.

    Works with the Reader (Layer 2) to build understanding.
    """

    def __init__(self, reader: Reader):
        self.reader = reader
        self.neuron_profiles: Dict[Tuple[int, int], NeuronProfile] = {}
        self.concept_neurons: Dict[str, ConceptNeurons] = {}

    def profile_neuron(self,
                       layer_idx: int,
                       neuron_idx: int,
                       top_k: int = 10) -> NeuronProfile:
        """
        Profile what a specific neuron responds to.

        Examines all stored prompts and ranks them by activation.
        """
        prompts = self.reader.get_stored_prompts()
        if not prompts:
            raise ValueError("No prompts stored. Probe some prompts first.")

        layer_key = f"layer_{layer_idx}"

        # Get activation for each prompt
        activations = []
        for prompt in prompts:
            if prompt not in self.reader.stored_activations:
                continue
            acts = self.reader.stored_activations[prompt]
            if layer_key not in acts:
                continue
            activation = float(acts[layer_key][neuron_idx])
            activations.append((prompt, activation))

        if not activations:
            raise ValueError(f"No activations found for layer {layer_idx}")

        # Sort by activation
        activations.sort(key=lambda x: x[1], reverse=True)

        # Calculate stats
        values = [a for _, a in activations]
        mean_act = np.mean(values)
        std_act = np.std(values)

        profile = NeuronProfile(
            layer=layer_idx,
            neuron_idx=neuron_idx,
            top_activating=activations[:top_k],
            bottom_activating=activations[-top_k:][::-1],
            mean_activation=float(mean_act),
            std_activation=float(std_act)
        )

        self.neuron_profiles[(layer_idx, neuron_idx)] = profile
        return profile

    def find_concept_neurons(self,
                             concept_name: str,
                             positive_prompts: List[str],
                             negative_prompts: Optional[List[str]] = None,
                             layer_idx: Optional[int] = None,
                             top_k: int = 20) -> ConceptNeurons:
        """
        Find neurons that consistently encode a concept.

        Args:
            concept_name: Name for this concept
            positive_prompts: Prompts that exemplify the concept
            negative_prompts: Prompts that are opposite to the concept (optional)
            layer_idx: Which layer to analyze (default: final layer)
            top_k: How many neurons to return

        Returns:
            ConceptNeurons with the most consistent neurons for this concept
        """
        # Verify all prompts are stored
        for p in positive_prompts:
            if p not in self.reader.stored_activations:
                raise ValueError(f"Prompt not stored: {p}")

        if negative_prompts:
            for p in negative_prompts:
                if p not in self.reader.stored_activations:
                    raise ValueError(f"Prompt not stored: {p}")

        # Get layer key
        sample_acts = self.reader.stored_activations[positive_prompts[0]]
        if layer_idx is None:
            layer_key = max(sample_acts.keys(), key=lambda k: int(k.split('_')[1]))
            layer_idx = int(layer_key.split('_')[1])
        else:
            layer_key = f"layer_{layer_idx}"

        hidden_size = len(sample_acts[layer_key])

        # Calculate mean activation for positive prompts
        pos_mean = np.zeros(hidden_size)
        for p in positive_prompts:
            pos_mean += self.reader.stored_activations[p][layer_key]
        pos_mean /= len(positive_prompts)

        # Calculate variance for consistency scoring
        pos_var = np.zeros(hidden_size)
        for p in positive_prompts:
            pos_var += (self.reader.stored_activations[p][layer_key] - pos_mean) ** 2
        pos_var /= max(1, len(positive_prompts) - 1)
        pos_std = np.sqrt(pos_var + 1e-8)

        if negative_prompts:
            # Calculate mean for negative prompts
            neg_mean = np.zeros(hidden_size)
            for p in negative_prompts:
                neg_mean += self.reader.stored_activations[p][layer_key]
            neg_mean /= len(negative_prompts)

            neg_var = np.zeros(hidden_size)
            for p in negative_prompts:
                neg_var += (self.reader.stored_activations[p][layer_key] - neg_mean) ** 2
            neg_var /= max(1, len(negative_prompts) - 1)
            neg_std = np.sqrt(neg_var + 1e-8)

            # Score by separation between groups (like t-statistic)
            pooled_std = np.sqrt((pos_var + neg_var) / 2 + 1e-8)
            scores = np.abs(pos_mean - neg_mean) / pooled_std
        else:
            # Without negatives, score by how consistently the neuron activates
            # (high mean with low variance = consistent concept neuron)
            scores = np.abs(pos_mean) / pos_std

        # Get top neurons
        top_indices = np.argsort(scores)[::-1][:top_k]
        neurons = [(int(idx), float(scores[idx])) for idx in top_indices]

        result = ConceptNeurons(
            concept_name=concept_name,
            prompts=positive_prompts,
            neurons=neurons,
            layer=layer_idx
        )

        self.concept_neurons[concept_name] = result
        return result

    def cluster_prompts(self,
                        n_clusters: int = 5,
                        layer_idx: Optional[int] = None) -> List[Cluster]:
        """
        Cluster stored prompts by activation similarity.

        Uses simple k-means clustering to find natural groupings.
        """
        prompts = self.reader.get_stored_prompts()
        if len(prompts) < n_clusters:
            raise ValueError(f"Need at least {n_clusters} prompts, have {len(prompts)}")

        # Get layer key
        sample_acts = self.reader.stored_activations[prompts[0]]
        if layer_idx is None:
            layer_key = max(sample_acts.keys(), key=lambda k: int(k.split('_')[1]))
        else:
            layer_key = f"layer_{layer_idx}"

        # Build activation matrix
        activations = np.array([
            self.reader.stored_activations[p][layer_key]
            for p in prompts
        ])

        # Normalize for cosine-like clustering
        norms = np.linalg.norm(activations, axis=1, keepdims=True)
        activations_normed = activations / (norms + 1e-8)

        # Simple k-means (not using sklearn to avoid dependency)
        centers = activations_normed[np.random.choice(len(prompts), n_clusters, replace=False)]

        for _ in range(20):  # iterations
            # Assign to nearest center
            distances = np.linalg.norm(
                activations_normed[:, np.newaxis, :] - centers[np.newaxis, :, :],
                axis=2
            )
            assignments = np.argmin(distances, axis=1)

            # Update centers
            new_centers = np.zeros_like(centers)
            for i in range(n_clusters):
                mask = assignments == i
                if np.sum(mask) > 0:
                    new_centers[i] = np.mean(activations_normed[mask], axis=0)
                else:
                    new_centers[i] = centers[i]

            if np.allclose(centers, new_centers):
                break
            centers = new_centers

        # Build clusters
        clusters = []
        for i in range(n_clusters):
            mask = assignments == i
            cluster_prompts = [prompts[j] for j in range(len(prompts)) if mask[j]]
            if cluster_prompts:
                clusters.append(Cluster(
                    center=centers[i],
                    prompts=cluster_prompts
                ))

        return clusters

    def find_boundary(self,
                      prompts_a: List[str],
                      prompts_b: List[str],
                      layer_idx: Optional[int] = None) -> Tuple[np.ndarray, float]:
        """
        Find the decision boundary between two groups of prompts.

        Returns the normal vector to the separating hyperplane and the bias.
        New prompts can be classified by: sign(dot(activation, normal) + bias)
        """
        # Get layer key
        sample_acts = self.reader.stored_activations[prompts_a[0]]
        if layer_idx is None:
            layer_key = max(sample_acts.keys(), key=lambda k: int(k.split('_')[1]))
        else:
            layer_key = f"layer_{layer_idx}"

        # Get mean activations for each group
        mean_a = np.mean([
            self.reader.stored_activations[p][layer_key]
            for p in prompts_a
        ], axis=0)

        mean_b = np.mean([
            self.reader.stored_activations[p][layer_key]
            for p in prompts_b
        ], axis=0)

        # The boundary normal is the difference between means
        normal = mean_b - mean_a
        normal = normal / (np.linalg.norm(normal) + 1e-8)

        # Bias is set so boundary passes through midpoint
        midpoint = (mean_a + mean_b) / 2
        bias = -np.dot(normal, midpoint)

        return normal, float(bias)

    def classify(self,
                 prompt: str,
                 prompts_a: List[str],
                 prompts_b: List[str],
                 label_a: str = "A",
                 label_b: str = "B",
                 layer_idx: Optional[int] = None) -> Tuple[str, float]:
        """
        Classify a prompt as belonging to group A or B.

        Returns the predicted label and confidence score.
        """
        if prompt not in self.reader.stored_activations:
            raise ValueError(f"Prompt not stored: {prompt}")

        normal, bias = self.find_boundary(prompts_a, prompts_b, layer_idx)

        # Get layer key
        sample_acts = self.reader.stored_activations[prompts_a[0]]
        if layer_idx is None:
            layer_key = max(sample_acts.keys(), key=lambda k: int(k.split('_')[1]))
        else:
            layer_key = f"layer_{layer_idx}"

        activation = self.reader.stored_activations[prompt][layer_key]
        score = np.dot(activation, normal) + bias

        # Normalize score to rough confidence
        confidence = min(1.0, abs(score) / 10.0)

        if score > 0:
            return label_b, confidence
        else:
            return label_a, confidence

    def activation_statistics(self, layer_idx: Optional[int] = None) -> Dict:
        """
        Get statistics about activation patterns across all stored prompts.
        """
        prompts = self.reader.get_stored_prompts()
        if not prompts:
            return {}

        sample_acts = self.reader.stored_activations[prompts[0]]
        if layer_idx is None:
            layer_key = max(sample_acts.keys(), key=lambda k: int(k.split('_')[1]))
            layer_idx = int(layer_key.split('_')[1])
        else:
            layer_key = f"layer_{layer_idx}"

        # Build activation matrix
        activations = np.array([
            self.reader.stored_activations[p][layer_key]
            for p in prompts
        ])

        # Calculate various statistics
        stats = {
            'layer': layer_idx,
            'num_prompts': len(prompts),
            'hidden_size': activations.shape[1],
            'mean_activation': float(np.mean(activations)),
            'std_activation': float(np.std(activations)),
            'sparsity': float(np.mean(np.abs(activations) < 0.1)),
            'top_active_neurons': [
                int(i) for i in np.argsort(np.mean(np.abs(activations), axis=0))[-10:][::-1]
            ],
            'most_variable_neurons': [
                int(i) for i in np.argsort(np.std(activations, axis=0))[-10:][::-1]
            ]
        }

        return stats

    def export_analysis(self, filepath: str) -> None:
        """Export analysis results to JSON."""
        data = {
            'neuron_profiles': {
                f"{k[0]}_{k[1]}": {
                    'layer': v.layer,
                    'neuron_idx': v.neuron_idx,
                    'top_activating': v.top_activating,
                    'bottom_activating': v.bottom_activating,
                    'mean': v.mean_activation,
                    'std': v.std_activation
                }
                for k, v in self.neuron_profiles.items()
            },
            'concept_neurons': {
                k: {
                    'prompts': v.prompts,
                    'neurons': v.neurons,
                    'layer': v.layer
                }
                for k, v in self.concept_neurons.items()
            }
        }

        Path(filepath).write_text(json.dumps(data, indent=2))

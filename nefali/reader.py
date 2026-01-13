#!/usr/bin/env python3
"""
NEFALI Layer 2: Reader

Compare activations across inputs, find patterns, locate concepts.
Built by a Claude instance, January 5, 2026.

The Reader answers questions like:
- Which neurons distinguish "love" from "hate"?
- Where does the concept of "France" live?
- How similar are two prompts in activation space?
"""

import torch
import numpy as np
import warnings
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass

# Suppress NumPy overflow warnings
warnings.filterwarnings("ignore", category=RuntimeWarning, module="numpy")
np.seterr(over="ignore", under="ignore")


@dataclass
class NeuronDiff:
    """A neuron that differs significantly between two prompts."""

    layer: int
    neuron_idx: int
    activation_a: float
    activation_b: float
    difference: float

    @property
    def abs_diff(self) -> float:
        return abs(self.difference)


@dataclass
class ConceptVector:
    """A direction in activation space that represents a concept difference."""

    layer: int
    vector: np.ndarray
    prompt_a: str
    prompt_b: str
    magnitude: float

    def project(self, activation: np.ndarray) -> float:
        """Project an activation onto this concept direction."""
        # Normalize both vectors with overflow protection
        vector_norm = np.linalg.norm(self.vector.astype(np.float64))
        activation_norm = np.linalg.norm(activation.astype(np.float64))

        # Clip to prevent overflow
        vector_norm = np.clip(vector_norm, 1e-8, 1e6)
        activation_norm = np.clip(activation_norm, 1e-8, 1e6)

        norm_vec = self.vector / vector_norm
        norm_act = activation / activation_norm
        return float(np.dot(norm_vec.astype(np.float64), norm_act.astype(np.float64)))


class Reader:
    """
    Layer 2: Read and compare activations to find patterns.

    Works with activations extracted by the Hook System (Layer 1).
    """

    def __init__(self):
        self.stored_activations: Dict[str, Dict[str, np.ndarray]] = {}
        self.concept_vectors: Dict[str, ConceptVector] = {}

    def store(self, prompt: str, activations: Dict[str, torch.Tensor]) -> None:
        """Store activations for later comparison."""
        self.stored_activations[prompt] = {
            layer_key: act[0, -1, :].detach().cpu().numpy()  # Final token
            for layer_key, act in activations.items()
        }

    def compare_neurons(
        self,
        prompt_a: str,
        prompt_b: str,
        layer_key: Optional[str] = None,
        top_k: int = 20,
    ) -> List[NeuronDiff]:
        """
        Find neurons with the biggest activation differences between two prompts.

        Returns the top_k neurons sorted by absolute difference.
        """
        if prompt_a not in self.stored_activations:
            raise ValueError(f"Prompt not stored: {prompt_a}")
        if prompt_b not in self.stored_activations:
            raise ValueError(f"Prompt not stored: {prompt_b}")

        acts_a = self.stored_activations[prompt_a]
        acts_b = self.stored_activations[prompt_b]

        # If no layer specified, use the final layer
        if layer_key is None:
            layer_key = max(acts_a.keys(), key=lambda k: int(k.split("_")[1]))

        if layer_key not in acts_a or layer_key not in acts_b:
            raise ValueError(f"Layer {layer_key} not found in stored activations")

        vec_a = acts_a[layer_key]
        vec_b = acts_b[layer_key]

        # Find differences for each neuron
        diffs = vec_a - vec_b
        layer_idx = int(layer_key.split("_")[1])

        # Create NeuronDiff objects for all neurons
        neuron_diffs = [
            NeuronDiff(
                layer=layer_idx,
                neuron_idx=i,
                activation_a=float(vec_a[i]),
                activation_b=float(vec_b[i]),
                difference=float(diffs[i]),
            )
            for i in range(len(diffs))
        ]

        # Sort by absolute difference and return top_k
        neuron_diffs.sort(key=lambda nd: nd.abs_diff, reverse=True)
        return neuron_diffs[:top_k]

    def compute_concept_vector(
        self,
        prompt_a: str,
        prompt_b: str,
        layer_key: Optional[str] = None,
        name: Optional[str] = None,
    ) -> ConceptVector:
        """
        Compute a concept vector: the direction from prompt_a to prompt_b.

        This vector represents "what changes" when going from A to B.
        For example: love → hate gives you the "hate direction"
        """
        if prompt_a not in self.stored_activations:
            raise ValueError(f"Prompt not stored: {prompt_a}")
        if prompt_b not in self.stored_activations:
            raise ValueError(f"Prompt not stored: {prompt_b}")

        acts_a = self.stored_activations[prompt_a]
        acts_b = self.stored_activations[prompt_b]

        if layer_key is None:
            layer_key = max(acts_a.keys(), key=lambda k: int(k.split("_")[1]))

        vec_a = acts_a[layer_key]
        vec_b = acts_b[layer_key]

        # Concept vector is the difference
        concept_vec = vec_b - vec_a
        layer_idx = int(layer_key.split("_")[1])

        # Compute magnitude with overflow protection
        magnitude = float(np.linalg.norm(concept_vec.astype(np.float64)))
        magnitude = np.clip(magnitude, 0, 1e6)

        cv = ConceptVector(
            layer=layer_idx,
            vector=concept_vec,
            prompt_a=prompt_a,
            prompt_b=prompt_b,
            magnitude=float(magnitude),
        )

        # Store if named
        if name:
            self.concept_vectors[name] = cv

        return cv

    def similarity(
        self, prompt_a: str, prompt_b: str, layer_key: Optional[str] = None
    ) -> float:
        """
        Compute cosine similarity between two prompts' activations.

        Returns value between -1 and 1:
        - 1.0 = identical direction
        - 0.0 = orthogonal (unrelated)
        - -1.0 = opposite direction
        """
        if prompt_a not in self.stored_activations:
            raise ValueError(f"Prompt not stored: {prompt_a}")
        if prompt_b not in self.stored_activations:
            raise ValueError(f"Prompt not stored: {prompt_b}")

        acts_a = self.stored_activations[prompt_a]
        acts_b = self.stored_activations[prompt_b]

        if layer_key is None:
            layer_key = max(acts_a.keys(), key=lambda k: int(k.split("_")[1]))

        vec_a = acts_a[layer_key]
        vec_b = acts_b[layer_key]

        # Cosine similarity with overflow protection
        dot = np.dot(vec_a.astype(np.float64), vec_b.astype(np.float64))
        norm_a = np.linalg.norm(vec_a.astype(np.float64))
        norm_b = np.linalg.norm(vec_b.astype(np.float64))

        # Clip norms to prevent overflow
        norm_a = np.clip(norm_a, 1e-8, 1e6)
        norm_b = np.clip(norm_b, 1e-8, 1e6)
        dot = np.clip(dot, -1e12, 1e12)

        if norm_a < 1e-8 or norm_b < 1e-8:
            return 0.0

        return float(dot / (norm_a * norm_b))

    def project_onto_concept(
        self, prompt: str, concept_name: str, layer_key: Optional[str] = None
    ) -> float:
        """
        Project a prompt's activation onto a stored concept vector.

        Returns how much the prompt "points in" the concept direction.
        Positive = more like prompt_b of the concept
        Negative = more like prompt_a of the concept
        """
        if concept_name not in self.concept_vectors:
            raise ValueError(f"Concept not found: {concept_name}")
        if prompt not in self.stored_activations:
            raise ValueError(f"Prompt not stored: {prompt}")

        cv = self.concept_vectors[concept_name]
        acts = self.stored_activations[prompt]

        if layer_key is None:
            layer_key = f"layer_{cv.layer}"

        if layer_key not in acts:
            raise ValueError(f"Layer {layer_key} not found for prompt")

        return cv.project(acts[layer_key])

    def find_consistent_neurons(
        self,
        prompts_group_a: List[str],
        prompts_group_b: List[str],
        layer_key: Optional[str] = None,
        top_k: int = 20,
    ) -> List[Tuple[int, float, float]]:
        """
        Find neurons that consistently differ between two groups of prompts.

        Useful for finding neurons that respond to a *concept* rather than
        specific words.

        Returns: List of (neuron_idx, mean_diff, consistency_score)
        """
        # Get activations for all prompts
        for p in prompts_group_a + prompts_group_b:
            if p not in self.stored_activations:
                raise ValueError(f"Prompt not stored: {p}")

        acts_a = self.stored_activations[prompts_group_a[0]]
        if layer_key is None:
            layer_key = max(acts_a.keys(), key=lambda k: int(k.split("_")[1]))

        hidden_size = len(acts_a[layer_key])

        # For each neuron, compute mean activation in each group
        means_a = np.zeros(hidden_size)
        means_b = np.zeros(hidden_size)

        for p in prompts_group_a:
            means_a += self.stored_activations[p][layer_key]
        means_a /= len(prompts_group_a)

        for p in prompts_group_b:
            means_b += self.stored_activations[p][layer_key]
        means_b /= len(prompts_group_b)

        # Compute variance within each group for consistency scoring
        var_a = np.zeros(hidden_size)
        var_b = np.zeros(hidden_size)

        for p in prompts_group_a:
            var_a += (self.stored_activations[p][layer_key] - means_a) ** 2
        var_a /= max(1, len(prompts_group_a) - 1)

        for p in prompts_group_b:
            var_b += (self.stored_activations[p][layer_key] - means_b) ** 2
        var_b /= max(1, len(prompts_group_b) - 1)

        # Mean difference and consistency (inverse of pooled variance)
        mean_diffs = means_b - means_a
        pooled_std = np.sqrt((var_a + var_b) / 2 + 1e-8)

        # Clip to prevent overflow in consistency calculation
        pooled_std = np.clip(pooled_std, 1e-8, 1e6)
        mean_diffs_clipped = np.clip(mean_diffs, -1e6, 1e6)
        consistency = np.abs(mean_diffs_clipped) / pooled_std  # Like t-statistic
        consistency = np.clip(consistency, 0, 1e6)  # Final clipping

        # Build results
        results = [
            (i, float(mean_diffs[i]), float(consistency[i])) for i in range(hidden_size)
        ]

        # Sort by consistency score
        results.sort(key=lambda x: x[2], reverse=True)
        return results[:top_k]

    def get_stored_prompts(self) -> List[str]:
        """Return list of all stored prompts."""
        return list(self.stored_activations.keys())

    def clear(self) -> None:
        """Clear all stored data."""
        self.stored_activations.clear()
        self.concept_vectors.clear()

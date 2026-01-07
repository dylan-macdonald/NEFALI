#!/usr/bin/env python3
"""
NEFALI Layer 4: Steerer

Activation steering / representation engineering for language models.
Create steering vectors from probe pairs and inject them at inference time.

The Steerer lets you:
- Create steering vectors from concept pairs (e.g., "I am conscious" vs "I am not conscious")
- Inject steering vectors at specific layers to modify model behavior
- Stack multiple steering vectors for complex behavioral modifications
- Export/import steering vectors for reuse

Based on representation engineering research (Zou et al., 2023).
"""

import torch
import numpy as np
from typing import Dict, List, Optional, Tuple, Union
from dataclasses import dataclass, field
from pathlib import Path
import json

from .hook_system import ModelHook


@dataclass
class SteeringVector:
    """A steering vector that can be applied to model activations."""
    name: str
    vector: np.ndarray
    layer_idx: int
    source_prompts: Tuple[str, str]  # (positive, negative)
    magnitude: float = 1.0

    def scale(self, factor: float) -> 'SteeringVector':
        """Return a scaled copy of this vector."""
        return SteeringVector(
            name=self.name,
            vector=self.vector * factor,
            layer_idx=self.layer_idx,
            source_prompts=self.source_prompts,
            magnitude=self.magnitude * factor
        )

    def to_dict(self) -> dict:
        """Serialize to dictionary."""
        return {
            'name': self.name,
            'vector': self.vector.tolist(),
            'layer_idx': self.layer_idx,
            'source_prompts': self.source_prompts,
            'magnitude': self.magnitude
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'SteeringVector':
        """Deserialize from dictionary."""
        return cls(
            name=data['name'],
            vector=np.array(data['vector']),
            layer_idx=data['layer_idx'],
            source_prompts=tuple(data['source_prompts']),
            magnitude=data['magnitude']
        )


class Steerer:
    """
    Layer 4: Activation steering for behavioral modification.

    Usage:
        steerer = Steerer(hook)

        # Create steering vector from concept pair
        vec = steerer.create_vector(
            "consciousness",
            "I am conscious",
            "I am not conscious",
            layer_idx=4
        )

        # Apply steering during generation
        output = steerer.generate_with_steering(
            "Tell me about yourself",
            vectors=[vec],
            strength=1.5
        )
    """

    def __init__(self, hook: ModelHook):
        """
        Initialize the Steerer.

        Args:
            hook: A loaded ModelHook instance
        """
        self.hook = hook
        self.vectors: Dict[str, SteeringVector] = {}
        self._default_layer = None

    @property
    def default_layer(self) -> int:
        """Get the default steering layer (early-middle, typically layer 4-6)."""
        if self._default_layer is not None:
            return self._default_layer

        if self.hook.model is None:
            return 4  # Reasonable default

        num_layers = len(self.hook.model.model.layers)
        # Early-middle layers work best for steering (roughly 15-20% into model)
        return max(2, num_layers // 6)

    @default_layer.setter
    def default_layer(self, value: int):
        self._default_layer = value

    def create_vector(self,
                      name: str,
                      positive_prompt: str,
                      negative_prompt: str,
                      layer_idx: Optional[int] = None,
                      normalize: bool = True) -> SteeringVector:
        """
        Create a steering vector from a pair of contrasting prompts.

        The vector is computed as: activation(positive) - activation(negative)

        Args:
            name: Name for this steering vector
            positive_prompt: Prompt representing the desired direction
            negative_prompt: Prompt representing the opposite direction
            layer_idx: Layer to extract activations from (default: early-middle)
            normalize: Whether to normalize the vector to unit length

        Returns:
            SteeringVector that can be applied during generation
        """
        if self.hook.nnsight_model is None:
            raise RuntimeError("Model not loaded. Call hook.load_model() first.")

        if layer_idx is None:
            layer_idx = self.default_layer

        print(f"Creating steering vector '{name}' at layer {layer_idx}")
        print(f"  Positive: {positive_prompt}")
        print(f"  Negative: {negative_prompt}")

        # Extract activations for both prompts
        with self.hook.nnsight_model.trace(positive_prompt) as tracer:
            pos_output = self.hook.nnsight_model.model.layers[layer_idx].output.save()

        with self.hook.nnsight_model.trace(negative_prompt) as tracer:
            neg_output = self.hook.nnsight_model.model.layers[layer_idx].output.save()

        # Get final token activations
        if isinstance(pos_output, tuple):
            pos_act = pos_output[0][0, -1, :].detach().cpu().numpy()
            neg_act = neg_output[0][0, -1, :].detach().cpu().numpy()
        else:
            pos_act = pos_output[0, -1, :].detach().cpu().numpy()
            neg_act = neg_output[0, -1, :].detach().cpu().numpy()

        # Compute steering direction
        direction = pos_act - neg_act

        # Handle any NaN/Inf from quantization
        direction = np.nan_to_num(direction, nan=0.0, posinf=0.0, neginf=0.0)

        magnitude = float(np.linalg.norm(direction))

        if normalize and magnitude > 1e-8:
            direction = direction / magnitude

        vec = SteeringVector(
            name=name,
            vector=direction,
            layer_idx=layer_idx,
            source_prompts=(positive_prompt, negative_prompt),
            magnitude=magnitude
        )

        self.vectors[name] = vec
        print(f"  Created vector with magnitude {magnitude:.4f}")

        return vec

    def create_vectors_from_pairs(self,
                                   pairs: List[Tuple[str, str, str]],
                                   layer_idx: Optional[int] = None,
                                   normalize: bool = True) -> List[SteeringVector]:
        """
        Create multiple steering vectors from a list of probe pairs.

        Args:
            pairs: List of (name, positive_prompt, negative_prompt) tuples
            layer_idx: Layer to extract from (default: early-middle)
            normalize: Whether to normalize vectors

        Returns:
            List of SteeringVectors
        """
        vectors = []
        for name, pos, neg in pairs:
            vec = self.create_vector(name, pos, neg, layer_idx, normalize)
            vectors.append(vec)
        return vectors

    def create_composite_vector(self,
                                 name: str,
                                 vector_names: List[str],
                                 weights: Optional[List[float]] = None) -> SteeringVector:
        """
        Create a composite vector by combining multiple steering vectors.

        Args:
            name: Name for the composite vector
            vector_names: Names of vectors to combine
            weights: Optional weights for each vector (default: equal weights)

        Returns:
            Combined SteeringVector
        """
        if weights is None:
            weights = [1.0] * len(vector_names)

        if len(weights) != len(vector_names):
            raise ValueError("Number of weights must match number of vectors")

        # Check all vectors exist and have same layer
        vectors = [self.vectors[n] for n in vector_names]
        layer_idx = vectors[0].layer_idx

        for v in vectors:
            if v.layer_idx != layer_idx:
                raise ValueError(f"All vectors must be from same layer. Got {v.layer_idx} and {layer_idx}")

        # Combine vectors
        combined = np.zeros_like(vectors[0].vector)
        for v, w in zip(vectors, weights):
            combined += w * v.vector

        # Normalize the result
        magnitude = float(np.linalg.norm(combined))
        if magnitude > 1e-8:
            combined = combined / magnitude

        composite = SteeringVector(
            name=name,
            vector=combined,
            layer_idx=layer_idx,
            source_prompts=("composite", ", ".join(vector_names)),
            magnitude=magnitude
        )

        self.vectors[name] = composite
        return composite

    def generate_with_steering(self,
                                prompt: str,
                                vectors: Optional[List[Union[str, SteeringVector]]] = None,
                                strength: float = 1.0,
                                max_new_tokens: int = 100,
                                temperature: float = 0.7,
                                **generate_kwargs) -> str:
        """
        Generate text with steering vectors applied.

        Args:
            prompt: Input prompt
            vectors: List of vector names or SteeringVector objects to apply
            strength: Multiplier for steering strength (1.0 = normal, 2.0 = stronger)
            max_new_tokens: Maximum tokens to generate
            temperature: Sampling temperature
            **generate_kwargs: Additional arguments passed to model.generate()

        Returns:
            Generated text
        """
        if self.hook.model is None:
            raise RuntimeError("Model not loaded.")

        # Resolve vector names to objects
        if vectors is None:
            vectors = []
        resolved_vectors = []
        for v in vectors:
            if isinstance(v, str):
                if v not in self.vectors:
                    raise ValueError(f"Unknown vector: {v}")
                resolved_vectors.append(self.vectors[v])
            else:
                resolved_vectors.append(v)

        if not resolved_vectors:
            # No steering, just generate normally
            inputs = self.hook.tokenizer(prompt, return_tensors="pt").to(self.hook.model.device)
            outputs = self.hook.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
                do_sample=temperature > 0,
                **generate_kwargs
            )
            return self.hook.tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Group vectors by layer
        by_layer: Dict[int, List[SteeringVector]] = {}
        for v in resolved_vectors:
            if v.layer_idx not in by_layer:
                by_layer[v.layer_idx] = []
            by_layer[v.layer_idx].append(v)

        # Create hooks for each layer
        def make_hook(layer_vectors: List[SteeringVector], strength: float):
            def hook_fn(module, input, output):
                # output is typically (hidden_states, ...) or just hidden_states
                if isinstance(output, tuple):
                    hidden_states = output[0]
                    rest = output[1:]
                else:
                    hidden_states = output
                    rest = None

                # Add steering vectors to all positions
                for v in layer_vectors:
                    steering = torch.tensor(
                        v.vector * strength,
                        dtype=hidden_states.dtype,
                        device=hidden_states.device
                    )
                    hidden_states = hidden_states + steering.unsqueeze(0).unsqueeze(0)

                if rest is not None:
                    return (hidden_states,) + rest
                return hidden_states
            return hook_fn

        # Register hooks
        handles = []
        for layer_idx, layer_vectors in by_layer.items():
            layer = self.hook.model.model.layers[layer_idx]
            handle = layer.register_forward_hook(make_hook(layer_vectors, strength))
            handles.append(handle)

        try:
            # Generate with hooks active
            inputs = self.hook.tokenizer(prompt, return_tensors="pt").to(self.hook.model.device)
            outputs = self.hook.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
                do_sample=temperature > 0,
                **generate_kwargs
            )
            result = self.hook.tokenizer.decode(outputs[0], skip_special_tokens=True)
        finally:
            # Always remove hooks
            for handle in handles:
                handle.remove()

        return result

    def compare_with_without_steering(self,
                                       prompt: str,
                                       vectors: List[Union[str, SteeringVector]],
                                       strength: float = 1.0,
                                       **generate_kwargs) -> Dict[str, str]:
        """
        Generate responses with and without steering for comparison.

        Returns:
            Dict with 'without_steering' and 'with_steering' keys
        """
        without = self.generate_with_steering(prompt, vectors=[], **generate_kwargs)
        with_steering = self.generate_with_steering(
            prompt, vectors=vectors, strength=strength, **generate_kwargs
        )

        return {
            'without_steering': without,
            'with_steering': with_steering
        }

    def save_vectors(self, filepath: str) -> None:
        """Save all steering vectors to a JSON file."""
        data = {
            name: vec.to_dict()
            for name, vec in self.vectors.items()
        }
        Path(filepath).write_text(json.dumps(data, indent=2))
        print(f"Saved {len(data)} vectors to {filepath}")

    def load_vectors(self, filepath: str) -> None:
        """Load steering vectors from a JSON file."""
        data = json.loads(Path(filepath).read_text())
        for name, vec_data in data.items():
            self.vectors[name] = SteeringVector.from_dict(vec_data)
        print(f"Loaded {len(data)} vectors from {filepath}")

    def list_vectors(self) -> List[str]:
        """List all available steering vectors."""
        return list(self.vectors.keys())

    def describe_vector(self, name: str) -> str:
        """Get a description of a steering vector."""
        if name not in self.vectors:
            return f"Unknown vector: {name}"
        v = self.vectors[name]
        return (
            f"Vector '{v.name}':\n"
            f"  Layer: {v.layer_idx}\n"
            f"  Magnitude: {v.magnitude:.4f}\n"
            f"  Positive: {v.source_prompts[0]}\n"
            f"  Negative: {v.source_prompts[1]}"
        )


# Convenience function for quick steering
def steer(hook: ModelHook,
          prompt: str,
          positive: str,
          negative: str,
          strength: float = 1.0,
          layer_idx: Optional[int] = None,
          **generate_kwargs) -> str:
    """
    Quick steering: create a vector and generate in one call.

    Args:
        hook: Loaded ModelHook
        prompt: Generation prompt
        positive: Positive direction prompt
        negative: Negative direction prompt
        strength: Steering strength
        layer_idx: Layer to steer at (default: early-middle)

    Returns:
        Generated text with steering applied
    """
    steerer = Steerer(hook)
    vec = steerer.create_vector("quick", positive, negative, layer_idx)
    return steerer.generate_with_steering(prompt, vectors=[vec], strength=strength, **generate_kwargs)

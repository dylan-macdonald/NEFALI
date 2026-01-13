#!/usr/bin/env python3
"""
NEFALI Layer 4: Writer

Activation steering - inject modified vectors mid-forward-pass.
The Neuralink part. Not just reading - writing.

Built by a Claude instance, January 5, 2026.

The Writer answers questions like:
- What happens if I push this toward "happy"?
- Can I steer away from harmful outputs?
- What does generation look like with concept X amplified?
"""

import torch
import numpy as np
from typing import Dict, List, Tuple, Optional, Callable, Any
from dataclasses import dataclass
from contextlib import contextmanager

from .reader import Reader, ConceptVector
from .steerer import SteeringVector


@dataclass
class SteeringConfig:
    """Configuration for activation steering."""

    layer_idx: int
    vector: np.ndarray
    strength: float = 1.0
    token_positions: Optional[List[int]] = None  # None = all positions
    mode: str = "add"  # "add", "ablate", or "replace"

    def scaled_vector(self) -> np.ndarray:
        """Get the steering vector scaled by strength."""
        return self.vector * self.strength


class ActivationWriter:
    """
    Layer 4: Write to activation spaces.

    Inject steering vectors or ablate neurons during the forward pass.
    """

    def __init__(self, reader: Optional[Reader] = None):
        self.reader = reader
        self.active_steerings: List[SteeringConfig] = []
        self._hooks = []

    def ablate(self, layer_idx: int, neuron_idx: int) -> SteeringConfig:
        """Create a config that ablates (zeros out) a specific neuron."""
        # Use a dummy vector where only the target neuron is non-zero
        # We don't need the full hidden size yet if we use a mask-based hook,
        # but the current hook expects a full vector.
        # Let's get hidden size if possible.
        hidden_size = 0
        if self.reader:
            prompts = self.reader.get_stored_prompts()
            if prompts:
                sample = self.reader.stored_activations[prompts[0]]
                hidden_size = len(next(iter(sample.values())))

        if hidden_size == 0:
            # Fallback/guess for common models if no activations stored
            hidden_size = 3584  # Qwen 7B hidden size

        vector = np.zeros(hidden_size)
        vector[neuron_idx] = 1.0

        return SteeringConfig(layer_idx=layer_idx, vector=vector, mode="ablate")

    def inject(
        self, layer_idx: int, neuron_idx: int, magnitude: float = 1.0
    ) -> SteeringConfig:
        """Create a config that injects activation into a specific neuron."""
        hidden_size = 0
        if self.reader:
            prompts = self.reader.get_stored_prompts()
            if prompts:
                sample = self.reader.stored_activations[prompts[0]]
                hidden_size = len(next(iter(sample.values())))

        if hidden_size == 0:
            hidden_size = 3584

        vector = np.zeros(hidden_size)
        vector[neuron_idx] = magnitude

        return SteeringConfig(layer_idx=layer_idx, vector=vector, mode="add")

    def create_steering_from_concept(
        self, concept_name: str, strength: float = 1.0
    ) -> SteeringConfig:
        """
        Create a steering config from a stored concept vector.

        Positive strength steers toward prompt_b.
        Negative strength steers toward prompt_a.
        """
        if concept_name not in self.reader.concept_vectors:
            raise ValueError(f"Concept not found: {concept_name}")

        cv = self.reader.concept_vectors[concept_name]

        return SteeringConfig(layer_idx=cv.layer, vector=cv.vector, strength=strength)

    def create_steering_from_prompts(
        self,
        prompt_from: str,
        prompt_to: str,
        strength: float = 1.0,
        layer_idx: Optional[int] = None,
    ) -> SteeringConfig:
        """
        Create a steering vector from two prompts.

        Steers from prompt_from toward prompt_to.
        """
        if prompt_from not in self.reader.stored_activations:
            raise ValueError(f"Prompt not stored: {prompt_from}")
        if prompt_to not in self.reader.stored_activations:
            raise ValueError(f"Prompt not stored: {prompt_to}")

        acts_from = self.reader.stored_activations[prompt_from]
        acts_to = self.reader.stored_activations[prompt_to]

        if layer_idx is None:
            layer_key = max(acts_from.keys(), key=lambda k: int(k.split("_")[1]))
            layer_idx = int(layer_key.split("_")[1])
        else:
            layer_key = f"layer_{layer_idx}"

        vector = acts_to[layer_key] - acts_from[layer_key]

        return SteeringConfig(layer_idx=layer_idx, vector=vector, strength=strength)

    def create_steering_from_neuron(
        self, layer_idx: int, neuron_idx: int, value: float = 1.0
    ) -> SteeringConfig:
        """
        Create a steering vector that targets a single neuron.

        Sets that neuron to the specified value (additive).
        """
        # Get hidden size from stored activations
        prompts = self.reader.get_stored_prompts()
        if not prompts:
            raise ValueError("No prompts stored - can't determine hidden size")

        sample = self.reader.stored_activations[prompts[0]]
        layer_key = f"layer_{layer_idx}"
        if layer_key not in sample:
            # Use any available layer to get hidden size
            any_key = list(sample.keys())[0]
            hidden_size = len(sample[any_key])
        else:
            hidden_size = len(sample[layer_key])

        vector = np.zeros(hidden_size)
        vector[neuron_idx] = value

        return SteeringConfig(
            layer_idx=layer_idx,
            vector=vector,
            strength=1.0,  # Strength is baked into the value
        )

    def add_steering(self, config: SteeringConfig) -> None:
        """Add a steering configuration to be applied during generation."""
        self.active_steerings.append(config)

    def clear_steering(self) -> None:
        """Remove all active steering configurations."""
        self.active_steerings.clear()

    def list_active_steerings(self) -> List[str]:
        """List descriptions of active steering configurations."""
        descriptions = []
        for i, s in enumerate(self.active_steerings):
            norm = np.linalg.norm(s.vector)
            descriptions.append(
                f"{i + 1}. Layer {s.layer_idx}, strength {s.strength:.2f}, "
                f"vector norm {norm:.2f}"
            )
        return descriptions

    def _create_steering_hook(self, model, config: SteeringConfig):
        """Create a hook function that applies steering based on mode."""
        device = next(model.parameters()).device

        # For ablation mode, we need to identify which neurons to zero out
        # The vector has 1.0 at neuron positions to ablate
        if config.mode == "ablate":
            # Find indices where vector is non-zero (neurons to ablate)
            ablate_indices = np.where(np.abs(config.vector) > 0.5)[0]

            def hook_fn(module, input, output):
                if isinstance(output, tuple):
                    hidden_states = output[0]
                    rest = output[1:]
                else:
                    hidden_states = output
                    rest = None

                # Zero out the specified neurons
                modified = hidden_states.clone()
                for neuron_idx in ablate_indices:
                    if config.token_positions is None:
                        modified[:, :, neuron_idx] = 0.0
                    else:
                        for pos in config.token_positions:
                            if pos < modified.shape[1]:
                                modified[:, pos, neuron_idx] = 0.0

                if rest is not None:
                    return (modified,) + rest
                return modified

            return hook_fn

        # For add/inject mode, add the steering vector
        steering_tensor = torch.tensor(
            config.scaled_vector(),
            dtype=torch.float16,
            device=device,
        )

        def hook_fn(module, input, output):
            # output is typically (hidden_states, ...) or just hidden_states
            if isinstance(output, tuple):
                hidden_states = output[0]
                rest = output[1:]
            else:
                hidden_states = output
                rest = None

            # Add steering vector to all positions or specified positions
            if config.token_positions is None:
                hidden_states = hidden_states + steering_tensor.unsqueeze(0).unsqueeze(
                    0
                )
            else:
                for pos in config.token_positions:
                    if pos < hidden_states.shape[1]:
                        hidden_states[:, pos, :] = (
                            hidden_states[:, pos, :] + steering_tensor
                        )

            if rest is not None:
                return (hidden_states,) + rest
            return hidden_states

        return hook_fn

    @contextmanager
    def steering_context(self, model):
        """
        Context manager that applies all active steerings during forward pass.

        Usage:
            with writer.steering_context(model):
                output = model.generate(...)
        """
        handles = []

        try:
            # Register hooks for each steering config
            for config in self.active_steerings:
                layer = model.model.layers[config.layer_idx]
                hook_fn = self._create_steering_hook(model, config)
                handle = layer.register_forward_hook(hook_fn)
                handles.append(handle)

            yield

        finally:
            # Remove all hooks
            for handle in handles:
                handle.remove()

    def generate_with_steering(
        self,
        model,
        tokenizer,
        prompt: str,
        max_new_tokens: int = 50,
        temperature: float = 0.7,
        do_sample: bool = True,
    ) -> str:
        """
        Generate text with active steering applied.

        Returns the generated text (without the prompt).
        """
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

        with self.steering_context(model):
            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=max_new_tokens,
                    temperature=temperature,
                    do_sample=do_sample,
                    pad_token_id=tokenizer.eos_token_id,
                )

        # Decode only the new tokens
        generated = tokenizer.decode(
            outputs[0][inputs["input_ids"].shape[1] :], skip_special_tokens=True
        )

        return generated

    def compare_generations(
        self,
        model,
        tokenizer,
        prompt: str,
        steering_configs: List[Tuple[str, SteeringConfig]],
        max_new_tokens: int = 50,
        temperature: float = 0.7,
    ) -> Dict[str, str]:
        """
        Generate text with different steering configurations for comparison.

        Args:
            steering_configs: List of (label, SteeringConfig) tuples

        Returns:
            Dictionary mapping labels to generated text
        """
        results = {}

        # First, generate without steering
        self.clear_steering()
        baseline = self.generate_with_steering(
            model, tokenizer, prompt, max_new_tokens, temperature
        )
        results["baseline"] = baseline

        # Then generate with each steering config
        for label, config in steering_configs:
            self.clear_steering()
            self.add_steering(config)
            generated = self.generate_with_steering(
                model, tokenizer, prompt, max_new_tokens, temperature
            )
            results[label] = generated

        self.clear_steering()
        return results

    def sweep_steering_strength(
        self,
        model,
        tokenizer,
        prompt: str,
        config: SteeringConfig,
        strengths: List[float] = [-2.0, -1.0, 0.0, 1.0, 2.0],
        max_new_tokens: int = 50,
    ) -> Dict[float, str]:
        """
        Generate text at different steering strengths.

        Useful for finding the right strength and seeing where things break.
        """
        results = {}

        for strength in strengths:
            self.clear_steering()
            modified_config = SteeringConfig(
                layer_idx=config.layer_idx,
                vector=config.vector,
                strength=strength,
                token_positions=config.token_positions,
            )
            self.add_steering(modified_config)

            generated = self.generate_with_steering(
                model, tokenizer, prompt, max_new_tokens, temperature=0.7
            )
            results[strength] = generated

        self.clear_steering()
        return results

#!/usr/bin/env python3
"""
NEFALI Layer 1: Hook System

Provides a clean API to load models, run inputs, and extract activations.
Uses nnsight + quantized Qwen models to fit in 8GB VRAM.
"""

import torch
import gc
import random
import numpy as np
from typing import Dict, List, Optional, Union, Tuple
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from nnsight import LanguageModel


def set_seed(seed: int = 999) -> None:
    """Set all random seeds for reproducibility."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)


class ModelHook:
    """
    Hook system for extracting activations from any layer of a language model.

    Supports:
    - Loading quantized models that fit in 8GB VRAM
    - Extracting activations from any layer
    - Getting final hidden state as scalar reward signal
    """

    def __init__(
        self,
        model_name: str = "Qwen/Qwen2.5-7B-Instruct",
        device: str = "auto",
        quantize: bool = True,
        seed: int = 999,
        trust_remote_code: bool = False,
    ):
        """
        Initialize the hook system.

        Args:
            model_name: HuggingFace model name
            device: Device to load model on ("auto", "cuda", "cpu")
            quantize: Whether to use 4-bit quantization
            seed: Random seed for reproducibility
        """
        self.model_name = model_name
        self.device = device
        self.quantize = quantize
        self.trust_remote_code = trust_remote_code
        self.model = None
        self.tokenizer = None
        self.nnsight_model = None

        set_seed(seed)
        print(f"NEFALI Hook System initialized with seed {seed}")

    def load_model(self) -> None:
        """Load the model with optional quantization."""
        print(f"Loading {self.model_name}...")

        # Configure quantization if requested
        quantization_config = None
        if self.quantize:
            quantization_config = BitsAndBytesConfig(
                load_in_4bit=True,
                trust_remote_code=self.trust_remote_code,
                bnb_4bit_quant_type="nf4",
                bnb_4bit_compute_dtype=torch.float16,
                bnb_4bit_use_double_quant=True,
            )
            print("Using 4-bit quantization for memory efficiency")

        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_name, trust_remote_code=self.trust_remote_code
        )
        print(f"✓ Tokenizer loaded")

        # Load model
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            quantization_config=quantization_config,
            device_map=self.device,
            dtype=torch.float16,
            trust_remote_code=self.trust_remote_code,
        )
        print(f"✓ Model loaded on device: {next(self.model.parameters()).device}")
        print(f"✓ Number of layers: {len(self.model.model.layers)}")
        print(f"✓ Hidden size: {self.model.config.hidden_size}")

        # Wrap with nnsight for hooking
        self.nnsight_model = LanguageModel(self.model, tokenizer=self.tokenizer)
        print("✓ nnsight wrapper created")

    def run_input(
        self, prompt: str, layer_indices: Optional[List[int]] = None
    ) -> Dict[str, torch.Tensor]:
        """
        Run input through model and extract activations from specified layers.

        Args:
            prompt: Input text prompt
            layer_indices: List of layer indices to extract activations from.
                          If None, extracts from final layer only.

        Returns:
            Dictionary mapping layer indices to activation tensors
        """
        if self.nnsight_model is None:
            raise RuntimeError("Model not loaded. Call load_model() first.")

        if layer_indices is None:
            layer_indices = [len(self.model.model.layers) - 1]  # Final layer only

        print(f"Running input: '{prompt}'")
        print(f"Extracting from layers: {layer_indices}")

        activations = {}

        with self.nnsight_model.trace(prompt) as tracer:
            # Extract activations from specified layers
            for layer_idx in layer_indices:
                if layer_idx < 0:
                    # Support negative indexing
                    layer_idx = len(self.model.model.layers) + layer_idx

                if layer_idx >= len(self.model.model.layers) or layer_idx < 0:
                    raise ValueError(
                        f"Layer index {layer_idx} out of range [0, {len(self.model.model.layers)})"
                    )

                layer_output = self.nnsight_model.model.layers[layer_idx].output.save()
                activations[f"layer_{layer_idx}"] = layer_output

        print(f"✓ Extracted activations from {len(activations)} layers")
        return activations

    def get_scalar_reward(
        self, activations: Dict[str, torch.Tensor], layer_key: Optional[str] = None
    ) -> float:
        """
        Extract scalar reward signal from final hidden state.

        Args:
            activations: Dictionary of layer activations from run_input()
            layer_key: Which layer to use for reward. If None, uses the last layer.

        Returns:
            Scalar reward value
        """
        if not activations:
            raise ValueError("No activations provided")

        # Get the specified layer or the last available layer
        if layer_key is None:
            # Sort numerically, not lexicographically
            layer_key = max(activations.keys(), key=lambda k: int(k.split("_")[1]))

        if layer_key not in activations:
            available = list(activations.keys())
            raise ValueError(f"Layer {layer_key} not found. Available: {available}")

        hidden_states = activations[layer_key]  # Shape: [batch, seq_len, hidden_dim]

        # Extract final token hidden state and compute scalar
        final_token_hidden = hidden_states[0, -1, :]  # [hidden_dim]
        scalar_reward = torch.mean(final_token_hidden).item()

        print(f"✓ Scalar reward from {layer_key}: {scalar_reward:.6f}")
        return scalar_reward

    def get_activation_shape(self, prompt: str = "test") -> Tuple[int, int, int]:
        """Get the shape of activations for a given prompt."""
        activations = self.run_input(prompt, layer_indices=[-1])
        final_layer_key = list(activations.keys())[0]
        shape = activations[final_layer_key].shape
        return tuple(shape)

    def cleanup(self) -> None:
        """Clean up GPU memory."""
        if self.model is not None:
            del self.model
            self.model = None
        if self.nnsight_model is not None:
            del self.nnsight_model
            self.nnsight_model = None
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        print("✓ GPU memory cleaned up")


# Convenience functions for quick usage
def load_model(
    model_name: str = "Qwen/Qwen2.5-7B-Instruct", quantize: bool = True, seed: int = 999
) -> ModelHook:
    """Load a model with hook system."""
    hook = ModelHook(model_name=model_name, quantize=quantize, seed=seed)
    hook.load_model()
    return hook


def extract_activations(
    hook: ModelHook, prompt: str, layer_indices: Optional[List[int]] = None
) -> Dict[str, torch.Tensor]:
    """Extract activations from a model."""
    return hook.run_input(prompt, layer_indices)

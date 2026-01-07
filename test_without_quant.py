#!/usr/bin/env python3
"""Test loading Qwen without quantization first."""

from transformer_lens import HookedTransformer
import torch

def main():
    print("Testing Qwen2.5-7B-Instruct without quantization...")
    
    try:
        # Try loading without quantization
        print("Loading Qwen2.5-7B-Instruct (no quantization)...")
        model = HookedTransformer.from_pretrained(
            "Qwen/Qwen2.5-7B-Instruct",
            device="cpu",  # Use CPU for now
            dtype=torch.float16,
        )
        print("✓ Successfully loaded model without quantization!")
        print(f"Model n_layers: {model.cfg.n_layers}")
        print(f"Model d_model: {model.cfg.d_model}")
        
        # Test basic functionality
        test_input = "Hello"
        tokens = model.to_tokens(test_input)
        print(f"✓ Tokenization works: {tokens.shape}")
        
        print("\nTransformerLens works with Qwen! Will need separate quantization.")
        return True
        
    except Exception as e:
        print(f"✗ Error with TransformerLens: {e}")
        print("Will need to use nnsight or manual approach.")
        return False

if __name__ == "__main__":
    main()
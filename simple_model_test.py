#!/usr/bin/env python3
"""Simple test to check if we can load Qwen with TransformerLens."""

from transformer_lens import HookedTransformer
import torch

def main():
    print("Testing Qwen2.5-7B-Instruct with TransformerLens...")
    
    try:
        # Try loading a quantized version first
        print("Loading Qwen2.5-7B-Instruct...")
        model = HookedTransformer.from_pretrained(
            "Qwen/Qwen2.5-7B-Instruct",
            device="cpu",  # Use CPU for initial test
            dtype=torch.float16,  # Use half precision
            load_in_4bit=True,   # Quantize to 4-bit
        )
        print("✓ Successfully loaded model!")
        print(f"Model device: {model.cfg.device}")
        print(f"Model n_layers: {model.cfg.n_layers}")
        print(f"Model d_model: {model.cfg.d_model}")
        
        # Test a simple forward pass
        print("\nTesting simple forward pass...")
        test_input = "Hello world"
        tokens = model.to_tokens(test_input)
        print(f"Tokens shape: {tokens.shape}")
        
        # Run forward pass and get final hidden state
        with torch.no_grad():
            output = model(tokens)
            final_hidden_state = model.run_with_cache(tokens)[1]['hook_final'][0, -1, :]
            print(f"Final hidden state shape: {final_hidden_state.shape}")
            print(f"Final hidden state (first 5 values): {final_hidden_state[:5]}")
            
        print("\n✓ Model working correctly!")
        return True
        
    except Exception as e:
        print(f"✗ Error: {e}")
        print("\nTrying alternative approach with nnsight...")
        return False

if __name__ == "__main__":
    success = main()
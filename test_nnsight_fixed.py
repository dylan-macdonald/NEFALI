#!/usr/bin/env python3
"""Test nnsight with correct Qwen model hooking."""

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from nnsight import LanguageModel
import gc

def main():
    print("Testing nnsight with Qwen2-0.5B (correct approach)...")
    
    try:
        model_name = "Qwen/Qwen2-0.5B"
        print(f"Loading {model_name}...")
        
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            device_map="auto"
        )
        
        print(f"✓ Model loaded on device: {next(model.parameters()).device}")
        print(f"✓ Number of layers: {len(model.model.layers)}")
        print(f"✓ Hidden size: {model.config.hidden_size}")
        
        # Wrap with nnsight
        print("Wrapping model with nnsight...")
        nnsight_model = LanguageModel(model, tokenizer=tokenizer)
        print("✓ nnsight wrapper created!")
        
        # Test basic functionality with proper layer access
        test_prompt = "The capital of France is"
        print(f"\nTesting with prompt: '{test_prompt}'")
        
        with nnsight_model.trace(test_prompt) as tracer:
            # Access the output of the last decoder layer
            # Each layer outputs a tensor directly (not a tuple)
            final_hidden_states = nnsight_model.model.layers[-1].output
            final_hidden_states.save()
            
            # Also save intermediate layer for testing
            mid_hidden_states = nnsight_model.model.layers[len(model.model.layers)//2].output
            mid_hidden_states.save()
        
        # Extract the saved hidden states
        final_hs = final_hidden_states.value
        mid_hs = mid_hidden_states.value
        
        print(f"✓ Final hidden states shape: {final_hs.shape}")
        print(f"✓ Mid hidden states shape: {mid_hs.shape}")
        print(f"✓ Final hidden state (last token, first 5 dims): {final_hs[0, -1, :5]}")
        
        # Extract scalar from final hidden state (as mentioned in requirements)
        scalar_reward = torch.mean(final_hs[0, -1, :]).item()  # Simple mean as scalar
        print(f"✓ Scalar reward signal: {scalar_reward:.6f}")
        
        print(f"\n✓ SUCCESS: nnsight + Qwen works perfectly!")
        print("Ready to implement full hook system for Layer 1!")
        
        return True, final_hs.shape
        
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False, None
    
    finally:
        # Clean up memory
        if 'model' in locals() and model is not None:
            del model
        if 'nnsight_model' in locals():
            del nnsight_model
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

if __name__ == "__main__":
    success, shape = main()
    print(f"Test result: {'PASSED' if success else 'FAILED'}")
    if shape:
        print(f"Hidden state shape: {shape}")
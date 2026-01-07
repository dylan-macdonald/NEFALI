#!/usr/bin/env python3
"""Test nnsight with correct API usage."""

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from nnsight import LanguageModel
import gc

def main():
    print("Testing nnsight with correct API...")
    
    try:
        model_name = "Qwen/Qwen2-0.5B"
        print(f"Loading {model_name}...")
        
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            device_map="cpu"
        )
        
        print(f"✓ Model loaded on device: {next(model.parameters()).device}")
        
        # Wrap with nnsight
        print("Wrapping model with nnsight...")
        nnsight_model = LanguageModel(model, tokenizer=tokenizer)
        print("✓ nnsight wrapper created!")
        
        # Test the nnsight approach
        test_prompt = "Hello world"
        print(f"\nTesting with prompt: '{test_prompt}'")
        
        # Run the model and capture activations
        with nnsight_model.trace(test_prompt) as tracer:
            # Get layer outputs using nnsight's intervention API
            last_layer = nnsight_model.model.layers[-1]
            # The output will be automatically captured
            hidden_states = last_layer.output.save()
        
        print(f"✓ Traced execution completed")
        print(f"✓ Hidden states shape: {hidden_states.shape}")
        print(f"✓ Hidden states dtype: {hidden_states.dtype}")
        
        # Extract scalar as reward signal
        final_token_hidden = hidden_states[0, -1, :]  # [hidden_dim]
        scalar_reward = torch.mean(final_token_hidden).item()
        print(f"✓ Final token hidden state shape: {final_token_hidden.shape}")
        print(f"✓ Scalar reward signal: {scalar_reward:.6f}")
        
        print(f"\n✅ SUCCESS! nnsight approach confirmed working!")
        
        return True, hidden_states.shape, scalar_reward
        
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False, None, None
    
    finally:
        # Clean up memory
        if 'model' in locals() and model is not None:
            del model
        if 'nnsight_model' in locals():
            del nnsight_model
        gc.collect()

if __name__ == "__main__":
    success, shape, scalar = main()
    print(f"\nFinal Result: {'✅ PASSED' if success else '❌ FAILED'}")
    if shape:
        print(f"Captured hidden state shape: {shape}")
        print(f"Scalar reward: {scalar:.6f}")
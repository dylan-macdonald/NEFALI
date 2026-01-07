#!/usr/bin/env python3
"""Simple nnsight test - just final hidden state."""

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from nnsight import LanguageModel
import gc

def main():
    print("Testing nnsight with Qwen2-0.5B (simple approach)...")
    
    try:
        model_name = "Qwen/Qwen2-0.5B"
        print(f"Loading {model_name}...")
        
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            device_map="cpu"  # Use CPU to avoid GPU memory issues during testing
        )
        
        print(f"✓ Model loaded on device: {next(model.parameters()).device}")
        
        # Wrap with nnsight
        print("Wrapping model with nnsight...")
        nnsight_model = LanguageModel(model, tokenizer=tokenizer)
        print("✓ nnsight wrapper created!")
        
        # Simple test - just get final layer output
        test_prompt = "Hello"
        print(f"\nTesting with prompt: '{test_prompt}'")
        
        with nnsight_model.trace(test_prompt) as tracer:
            # Get the final layer output
            final_layer_output = nnsight_model.model.layers[-1].output
            final_layer_output.save()
        
        # Extract the saved hidden states
        final_hs = final_layer_output.value
        
        print(f"✓ Final hidden states shape: {final_hs.shape}")
        print(f"✓ Final hidden state dtype: {final_hs.dtype}")
        print(f"✓ Final hidden state (last token, first 5 dims): {final_hs[0, -1, :5]}")
        
        # Extract scalar from final hidden state (as required)
        scalar_reward = torch.mean(final_hs[0, -1, :]).item()  
        print(f"✓ Scalar reward signal: {scalar_reward:.6f}")
        
        print(f"\n✅ SUCCESS! nnsight + Qwen is working!")
        print("Hook system approach verified - ready to implement full Layer 1!")
        
        return True, final_hs.shape, scalar_reward
        
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
    print(f"\nResult: {'✅ PASSED' if success else '❌ FAILED'}")
    if shape:
        print(f"Shape: {shape}, Scalar: {scalar:.6f}")
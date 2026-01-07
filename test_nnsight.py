#!/usr/bin/env python3
"""Test nnsight with Qwen models."""

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from nnsight import LanguageModel
import gc

def main():
    print("Testing nnsight with Qwen2.5-7B...")
    
    try:
        # Configure quantization
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_use_double_quant=True,
        )
        
        model_name = "Qwen/Qwen2.5-7B-Instruct"
        print(f"Loading {model_name} with 4-bit quantization...")
        
        # Load with transformers first 
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            quantization_config=bnb_config,
            device_map="auto",
            torch_dtype=torch.float16,
        )
        
        print("✓ Model loaded successfully with quantization!")
        print(f"Model device: {next(model.parameters()).device}")
        
        # Now wrap with nnsight
        print("Wrapping model with nnsight...")
        nnsight_model = LanguageModel(model, tokenizer=tokenizer)
        print("✓ nnsight wrapper created!")
        
        # Test basic functionality
        test_prompt = "The capital of France is"
        print(f"\nTesting with prompt: '{test_prompt}'")
        
        with nnsight_model.trace(test_prompt) as tracer:
            # Get hidden states from the last layer
            final_hidden_states = nnsight_model.model.layers[-1].output[0]
            # Save for later extraction
            final_hidden_states.save()
        
        # Extract the saved hidden states
        hidden_states = final_hidden_states.value
        print(f"✓ Final hidden states shape: {hidden_states.shape}")
        print(f"✓ Final hidden state (last token, first 5 dims): {hidden_states[0, -1, :5]}")
        
        print("\n✓ nnsight + quantized Qwen works perfectly!")
        print("Ready to implement hook system!")
        
        return True
        
    except Exception as e:
        print(f"✗ Error with nnsight: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    finally:
        # Clean up memory
        if 'model' in locals():
            del model
        if 'nnsight_model' in locals():
            del nnsight_model
        gc.collect()
        torch.cuda.empty_cache() if torch.cuda.is_available() else None

if __name__ == "__main__":
    success = main()
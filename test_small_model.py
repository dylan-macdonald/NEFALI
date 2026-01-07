#!/usr/bin/env python3
"""Test with a smaller Qwen model to verify the approach."""

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from nnsight import LanguageModel
import gc

def main():
    print("Testing nnsight with smaller Qwen model...")
    
    try:
        # Try with a smaller model first - Qwen2-0.5B if available, or GPT-2 as fallback
        model_names = [
            "Qwen/Qwen2-0.5B",
            "Qwen/Qwen2-1.5B", 
            "gpt2"  # fallback
        ]
        
        model = None
        tokenizer = None
        model_name = None
        
        for name in model_names:
            try:
                print(f"Trying {name}...")
                tokenizer = AutoTokenizer.from_pretrained(name)
                model = AutoModelForCausalLM.from_pretrained(
                    name,
                    torch_dtype=torch.float16,
                    device_map="auto"
                )
                model_name = name
                print(f"✓ Successfully loaded {name}")
                break
            except Exception as e:
                print(f"✗ Failed to load {name}: {e}")
                continue
        
        if model is None:
            print("✗ No model could be loaded")
            return False
        
        print(f"Model device: {next(model.parameters()).device}")
        print(f"Model layers: {len(model.transformer.h) if hasattr(model, 'transformer') else 'unknown'}")
        
        # Wrap with nnsight
        print("Wrapping model with nnsight...")
        nnsight_model = LanguageModel(model, tokenizer=tokenizer)
        print("✓ nnsight wrapper created!")
        
        # Test basic functionality
        test_prompt = "Hello world"
        print(f"\nTesting with prompt: '{test_prompt}'")
        
        with nnsight_model.trace(test_prompt) as tracer:
            # Try to get hidden states from various layers
            if hasattr(model, 'transformer'):  # GPT-2 style
                layers = model.transformer.h
            elif hasattr(model, 'model'):  # Qwen style
                layers = model.model.layers
            else:
                print("Unknown model structure")
                return False
                
            # Get final hidden states
            final_hidden_states = layers[-1].output[0]
            final_hidden_states.save()
        
        # Extract the saved hidden states
        hidden_states = final_hidden_states.value
        print(f"✓ Final hidden states shape: {hidden_states.shape}")
        print(f"✓ Sample values: {hidden_states[0, -1, :5] if len(hidden_states.shape) >= 3 else hidden_states[:5]}")
        
        print(f"\n✓ nnsight + {model_name} works! Ready to implement full system.")
        
        return True
        
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False
    
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
    success = main()
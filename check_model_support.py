#!/usr/bin/env python3
"""Check TransformerLens support for Qwen models."""

import transformer_lens as tl
from transformer_lens import HookedTransformer

def main():
    print("Checking TransformerLens model support...")
    
    # Check available models
    print("\nAvailable models in TransformerLens:")
    try:
        available_models = tl.utils.get_pretrained_model_config()
        for model_name in list(available_models.keys())[:20]:  # Show first 20
            print(f"  - {model_name}")
        print(f"  ... and {len(available_models) - 20} more")
        
        # Check specifically for Qwen models
        qwen_models = [name for name in available_models.keys() if 'qwen' in name.lower()]
        print(f"\nQwen models found: {len(qwen_models)}")
        for qwen_model in qwen_models:
            print(f"  - {qwen_model}")
            
    except Exception as e:
        print(f"Error checking available models: {e}")
    
    # Try loading a Qwen model directly from HuggingFace
    print("\nTrying to load Qwen2.5-7B from HuggingFace...")
    try:
        # First try with TransformerLens
        model = HookedTransformer.from_pretrained(
            "Qwen/Qwen2.5-7B", 
            device="cpu",  # Start with CPU to avoid VRAM issues during testing
            torch_dtype="auto"
        )
        print("✓ Successfully loaded Qwen2.5-7B with TransformerLens")
        print(f"Model config: {model.cfg}")
        model = None  # Free memory
        
    except Exception as e:
        print(f"✗ Failed to load Qwen2.5-7B with TransformerLens: {e}")
        print("Will need to use alternative approach...")

if __name__ == "__main__":
    main()
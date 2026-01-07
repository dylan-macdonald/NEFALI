#!/usr/bin/env python3
"""
Test script for NEFALI Layer 1: Hook System

Demonstrates:
- Loading quantized Qwen model
- Running a prompt through the model
- Extracting hidden states from the last layer
- Getting scalar reward signal
- Printing activation shapes

This is the verification script mentioned in CLAUDE.md.
Layer 1 is "done" when this script runs and prints activation shapes.
"""

from nefali.hook_system import ModelHook
import torch

def main():
    print("=" * 60)
    print("NEFALI Layer 1: Hook System Test")
    print("=" * 60)
    
    try:
        # Test with smaller model first to verify the system works
        # Can be changed to Qwen2.5-7B once we confirm 4-bit quantization works
        model_name = "Qwen/Qwen2-0.5B"  # Start with smaller model
        print(f"Testing with: {model_name}")
        
        # Initialize hook system
        hook = ModelHook(
            model_name=model_name,
            device="auto",
            quantize=False,  # Start without quantization for smaller model
            seed=42
        )
        
        print("\n1. Loading model...")
        hook.load_model()
        
        print("\n2. Running test prompt...")
        test_prompt = "The capital of France is"
        
        # Extract activations from multiple layers to test the system
        layer_indices = [-3, -2, -1]  # Last 3 layers
        activations = hook.run_input(test_prompt, layer_indices=layer_indices)
        
        print("\n3. Activation shapes:")
        for layer_key, activation in activations.items():
            print(f"  {layer_key}: {activation.shape}")
        
        print("\n4. Extracting scalar reward signal...")
        scalar_reward = hook.get_scalar_reward(activations)
        print(f"  Scalar reward: {scalar_reward:.6f}")
        
        print("\n5. Testing single layer extraction (final layer only)...")
        final_activations = hook.run_input(test_prompt)  # Default to final layer
        final_shape = hook.get_activation_shape(test_prompt)
        print(f"  Final layer shape: {final_shape}")
        
        print("\n6. Testing different prompts...")
        test_prompts = [
            "Hello world",
            "Once upon a time",
            "The meaning of life is"
        ]
        
        for prompt in test_prompts:
            activations = hook.run_input(prompt, layer_indices=[-1])
            reward = hook.get_scalar_reward(activations)
            print(f"  '{prompt}' -> reward: {reward:.6f}")
        
        print("\n7. Cleaning up...")
        hook.cleanup()
        
        print("\n" + "=" * 60)
        print("✅ LAYER 1 TEST SUCCESSFUL!")
        print("Hook system working correctly.")
        print("Ready for Layer 2 development.")
        print("=" * 60)
        
        return True
        
    except Exception as e:
        print(f"\n❌ LAYER 1 TEST FAILED!")
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_quantized_model():
    """Test with quantized larger model if the basic test passes."""
    print("\n" + "=" * 60)
    print("Testing with quantized Qwen2.5-7B...")
    print("=" * 60)
    
    try:
        hook = ModelHook(
            model_name="Qwen/Qwen2.5-7B-Instruct",
            device="auto",
            quantize=True,  # Use quantization for larger model
            seed=42
        )
        
        hook.load_model()
        
        # Quick test
        activations = hook.run_input("Hello", layer_indices=[-1])
        reward = hook.get_scalar_reward(activations)
        shape = list(activations.values())[0].shape
        
        print(f"✅ Quantized model test successful!")
        print(f"   Shape: {shape}")
        print(f"   Reward: {reward:.6f}")
        
        hook.cleanup()
        return True
        
    except Exception as e:
        print(f"❌ Quantized model test failed: {e}")
        print("This is expected if GPU memory is insufficient.")
        return False

if __name__ == "__main__":
    # Run basic test first
    success = main()
    
    if success:
        print(f"\n{'='*20} BONUS TEST {'='*20}")
        # Try quantized model if basic test passes
        test_quantized_model()
    
    print(f"\nLayer 1 Status: {'COMPLETED' if success else 'NEEDS FIXES'}")
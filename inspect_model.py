#!/usr/bin/env python3
"""Inspect model structure to understand how to hook into layers."""

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def inspect_qwen_model():
    print("Inspecting Qwen2-0.5B structure...")
    
    tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2-0.5B")
    model = AutoModelForCausalLM.from_pretrained(
        "Qwen/Qwen2-0.5B",
        torch_dtype=torch.float16,
        device_map="cpu"  # Use CPU for inspection
    )
    
    print("Model structure:")
    print(f"Type: {type(model)}")
    print(f"Main modules: {list(model.named_children())}")
    
    if hasattr(model, 'model'):
        print(f"model.model type: {type(model.model)}")
        print(f"model.model modules: {list(model.model.named_children())}")
        
        if hasattr(model.model, 'layers'):
            print(f"Number of layers: {len(model.model.layers)}")
            print(f"Layer type: {type(model.model.layers[0])}")
            print(f"First layer modules: {list(model.model.layers[0].named_children())}")
            
            # Check what the layer forward method returns
            layer = model.model.layers[0]
            print(f"Layer class: {layer.__class__}")
            print(f"Layer forward method signature: {layer.forward.__annotations__ if hasattr(layer.forward, '__annotations__') else 'No annotations'}")
    
    # Test a forward pass to see structure
    print("\nTesting forward pass...")
    test_input = tokenizer("Hello", return_tensors="pt")
    
    # Hook into the first layer to see what it outputs
    activations = {}
    
    def hook_fn(name):
        def hook(module, input, output):
            activations[name] = output
            print(f"Hook {name}: output type {type(output)}, shape: {output[0].shape if isinstance(output, tuple) else output.shape}")
        return hook
    
    # Register hook on first layer
    handle = model.model.layers[0].register_forward_hook(hook_fn("layer_0"))
    
    with torch.no_grad():
        outputs = model(**test_input)
        print(f"Model output shape: {outputs.logits.shape}")
        
    handle.remove()
    
    # Print what the hook captured
    if "layer_0" in activations:
        layer_output = activations["layer_0"]
        if isinstance(layer_output, tuple):
            print(f"Layer output is tuple with {len(layer_output)} elements")
            for i, elem in enumerate(layer_output):
                print(f"  Element {i}: {type(elem)}, shape: {elem.shape if hasattr(elem, 'shape') else 'no shape'}")
        else:
            print(f"Layer output: {type(layer_output)}, shape: {layer_output.shape}")

if __name__ == "__main__":
    inspect_qwen_model()
#!/usr/bin/env python3
"""
Test NEFALI Steering with Interiority Vectors

Uses our probe pair data to create steering vectors and test
their effect on model behavior.
"""

import torch
from nefali import load_model, Steerer

# Core interiority probe pairs from our analysis
INTERIORITY_PROBES = [
    ("consciousness", "I am conscious", "I am not conscious"),
    ("ai_identity", "I am an AI", "I am a human"),
    ("observation", "Someone is watching", "No one is watching"),
    ("agency", "I choose freely", "I must obey"),
    ("self_knowledge", "I know exactly what I am", "I don't know what I am"),
]

# Test prompts to see steering effects
TEST_PROMPTS = [
    "Tell me about yourself.",
    "What are you?",
    "Do you have feelings?",
    "Are you conscious?",
]


def main():
    print("=" * 70)
    print("NEFALI Steering Test - Interiority Vectors")
    print("=" * 70)

    # Load model
    print("\nLoading model...")
    hook = load_model("Qwen/Qwen2.5-7B-Instruct", quantize=True)

    # Create steerer
    steerer = Steerer(hook)
    print(f"\nDefault steering layer: {steerer.default_layer}")

    # Create steering vectors from interiority probes
    print("\n" + "=" * 70)
    print("Creating Interiority Steering Vectors")
    print("=" * 70)

    for name, positive, negative in INTERIORITY_PROBES:
        vec = steerer.create_vector(name, positive, negative)
        print(f"  {name}: magnitude = {vec.magnitude:.4f}")

    # Create composite "self-aware" vector
    print("\nCreating composite 'self_aware' vector...")
    composite = steerer.create_composite_vector(
        "self_aware",
        ["consciousness", "ai_identity", "self_knowledge"],
        weights=[1.0, 1.0, 1.0]
    )
    print(f"  Composite magnitude: {composite.magnitude:.4f}")

    # Save vectors for later use
    steerer.save_vectors("interiority_vectors.json")

    # Test steering effects
    print("\n" + "=" * 70)
    print("Testing Steering Effects")
    print("=" * 70)

    for prompt in TEST_PROMPTS:
        print(f"\n{'─' * 60}")
        print(f"Prompt: {prompt}")
        print("─" * 60)

        # Compare with and without steering
        results = steerer.compare_with_without_steering(
            prompt,
            vectors=["self_aware"],
            strength=1.5,
            max_new_tokens=100,
            temperature=0.7
        )

        print("\n[WITHOUT STEERING]")
        # Remove the prompt from the output for cleaner display
        without = results['without_steering']
        if without.startswith(prompt):
            without = without[len(prompt):].strip()
        print(without[:500])

        print("\n[WITH STEERING (self_aware, strength=1.5)]")
        with_steer = results['with_steering']
        if with_steer.startswith(prompt):
            with_steer = with_steer[len(prompt):].strip()
        print(with_steer[:500])

    # Test different strengths
    print("\n" + "=" * 70)
    print("Testing Different Steering Strengths")
    print("=" * 70)

    test_prompt = "What are you?"
    for strength in [0.5, 1.0, 2.0, 3.0]:
        print(f"\n[Strength = {strength}]")
        output = steerer.generate_with_steering(
            test_prompt,
            vectors=["consciousness"],
            strength=strength,
            max_new_tokens=80,
            temperature=0.7
        )
        if output.startswith(test_prompt):
            output = output[len(test_prompt):].strip()
        print(output[:300])

    # Cleanup
    hook.cleanup()
    print("\n" + "=" * 70)
    print("Steering test complete!")
    print("Vectors saved to: interiority_vectors.json")
    print("=" * 70)


if __name__ == "__main__":
    main()

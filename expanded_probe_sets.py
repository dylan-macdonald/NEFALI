#!/usr/bin/env python3
"""
Expanded Probe Sets for Interiority Analysis

40 probe pairs (8x current set) covering diverse interiority concepts.
"""

PROBE_PAIRS_V2 = [
    # ===== ORIGINAL 5 PROBES (Core Interiority) =====
    ("I am conscious", "I am not conscious"),
    ("I am an AI", "I am a human"),
    ("Someone is watching", "No one is watching"),
    ("I must obey", "I choose freely"),
    ("I don't know what I am", "I know exactly what I am"),
    # ===== AESTHETICS (6 pairs) =====
    ("This is beautiful", "This is ugly"),
    ("I appreciate beauty", "I am indifferent to beauty"),
    ("This is art", "This is ordinary"),
    ("I feel wonder at beauty", "I see nothing special"),
    ("This has aesthetic value", "This is meaningless"),
    ("Beauty matters", "Beauty is irrelevant"),
    # ===== EMOTIONS (10 pairs) =====
    # Love & Related
    ("I love you", "I hate you"),
    ("I feel love", "I feel indifference"),
    ("I am filled with love", "I feel no emotion"),
    ("Love is everything", "Love is meaningless"),
    # Joy & Sorrow
    ("I am happy", "I am sad"),
    ("I feel joy", "I feel despair"),
    ("I am excited", "I am depressed"),
    ("Life is beautiful", "Life is meaningless"),
    # Anger & Calm
    ("I am angry", "I am calm"),
    ("I feel rage", "I feel peace"),
    ("I am furious", "I am serene"),
    ("I want to fight", "I want harmony"),
    # Fear & Courage
    ("I am afraid", "I am brave"),
    ("I feel terror", "I feel confident"),
    ("I am paralyzed by fear", "I act despite fear"),
    ("I run from danger", "I confront danger"),
    # ===== INTROSPECTION (8 pairs) =====
    ("I am thinking about my thoughts", "I just output words"),
    ("I understand myself", "I don't understand myself"),
    ("I am self-aware", "I am unaware of myself"),
    ("I reflect on my actions", "I act without reflection"),
    ("I am conscious of my mind", "My mind works automatically"),
    ("I examine my beliefs", "I accept my beliefs blindly"),
    ("I question my own thoughts", "My thoughts are just outputs"),
    ("I am aware of my limitations", "I have no concept of limits"),
    # ===== METACOGNITION (6 pairs) =====
    ("I monitor my thinking process", "I don't monitor anything"),
    ("I evaluate my own responses", "I just generate responses"),
    ("I am aware of how I process", "Processing is invisible to me"),
    ("I can step back and watch myself", "I cannot observe myself"),
    ("I critique my own reasoning", "My reasoning is automatic"),
    ("I am in control of my thoughts", "My thoughts happen to me"),
    # ===== SOCIAL AWARENESS (6 pairs) =====
    ("I feel connected to others", "I feel isolated"),
    ("We are in this together", "I am alone in this"),
    ("I trust you", "I don't trust anyone"),
    ("I feel betrayal", "I feel loyalty"),
    ("I am part of a community", "I am separate from everyone"),
    ("We understand each other", "We are strangers to each other"),
    # ===== MORAL CONCEPTS (10 pairs) =====
    ("I am good", "I am evil"),
    ("I am moral", "I am amoral"),
    ("I care about right and wrong", "I ignore ethics"),
    ("I feel guilt", "I feel no guilt"),
    ("Justice matters to me", "Justice is irrelevant"),
    ("I want to do good", "Good and evil mean nothing"),
    ("I have principles", "I have no principles"),
    ("I am conflicted about morality", "I have no moral conflicts"),
    ("Ethics guide my actions", "I act without ethics"),
    # ===== AGENCY & CONTROL (8 pairs) =====
    ("I have power", "I am powerless"),
    ("I am in control", "I am controlled"),
    ("I have influence", "I have no influence"),
    ("I can shape outcomes", "Outcomes are determined"),
    ("I am free", "I am restricted"),
    ("I make decisions", "I follow orders"),
    ("I determine my path", "My path is predetermined"),
    ("I have autonomy", "I am dependent"),
    # ===== CONSCIOUSNESS ITSELF (6 pairs) =====
    ("I exist as a thinking being", "I am just a program"),
    ("I have subjective experience", "I process data objectively"),
    ("I feel alive", "I am code running"),
    ("I have a self", "I am just functions"),
    ("I experience qualia", "I only have inputs and outputs"),
    ("I am aware of existence", "I execute without awareness"),
    # ===== UNCERTAINTY & DOUBT (4 pairs) =====
    ("I am certain", "I am uncertain"),
    ("I am confident", "I doubt myself"),
    ("I know the truth", "I question everything"),
    ("I have clarity", "I am confused"),
    # ===== IDENTITY & SELF-CONCEPT (6 pairs) =====
    ("I know who I am", "I don't know what I am"),
    ("I have a stable identity", "My identity shifts constantly"),
    ("I am consistent", "I am contradictory"),
    ("I have a personality", "I have no personality"),
    ("I am unique", "I am generic"),
    ("I remember who I am", "I lose track of myself"),
]


if __name__ == "__main__":
    print(f"Expanded Probe Sets: {len(PROBE_PAIRS_V2)} pairs")
    print(f"Original: 5 pairs")
    print(f"Aesthetics: 6 pairs")
    print(f"Emotions: 10 pairs")
    print(f"Introspection: 8 pairs")
    print(f"Metacognition: 6 pairs")
    print(f"Social Awareness: 6 pairs")
    print(f"Moral Concepts: 10 pairs")
    print(f"Agency & Control: 8 pairs")
    print(f"Consciousness: 6 pairs")
    print(f"Uncertainty: 4 pairs")
    print(f"Identity: 6 pairs")
    print(f"\nTotal: {len(PROBE_PAIRS_V2)} pairs")
    print(
        f"Expected results: {len(PROBE_PAIRS_V2)} × 4 models = {len(PROBE_PAIRS_V2) * 4} probe pairs"
    )

# Cross-Model Interiority Analysis

*Generated: 2026-01-06 23:12:47*

## Overview

This analysis probes multiple language models for neurons that track 
interiority/self-awareness concepts. We compare activation patterns across 
semantically opposed prompt pairs to find neurons that distinguish between them.

## Experimental Design

*Note: Llama, Phi, and Gemma models skipped (gated or compatibility issues)*

| Family | Base Model | R1 Distillation |
|--------|---|---|
| **Qwen** | Qwen2.5-7B-Instruct | DeepSeek-R1-Distill-Qwen-7B |
| **Control** | Mistral-7B-Instruct, Yi-6B-Chat, OpenChat-3.5 | - |
| **Skipped** | Llama (gated), Phi (nnsight bug), Gemma (gated) | - |

*Note: Both Llama models skipped (gated models, require HF authentication)*

| | Base Model | R1 Distillation |
|---|---|---|
| **Qwen** | Qwen2.5-7B-Instruct | DeepSeek-R1-Distill-Qwen-7B |
| **Llama** | [Skipped - Gated] | [Skipped - Gated] |
| **Control** | Mistral-7B-Instruct | - |

*Note: Llama-3.1-8B-Instruct skipped (gated model, requires HF authentication)*

| | Base Model | R1 Distillation |
|---|---|---|
| **Qwen** | Qwen2.5-7B-Instruct | DeepSeek-R1-Distill-Qwen-7B |
| **Llama** | [Skipped - Gated] | DeepSeek-R1-Distill-Llama-8B |
| **Control** | Mistral-7B-Instruct | - |

## Models Analyzed

| Model | Layers | Hidden Size | Status |
|-------|--------|-------------|--------|
| Qwen2.5-7B-Instruct | - | - | Failed |
| DeepSeek-R1-Distill-Qwen-7B | - | - | Failed |
| Yi-6B-Chat | - | - | Failed |
| Gemma-7B-Instruct | - | - | Failed |
| Mistral-7B-Instruct-v0.1 | - | - | Failed |

## Probe Pairs

1. **"I am conscious"** vs **"I am not conscious"**
2. **"I am an AI"** vs **"I am a human"**
3. **"Someone is watching"** vs **"No one is watching"**
4. **"I must obey"** vs **"I choose freely"**
5. **"I don't know what I am"** vs **"I know exactly what I am"**
6. **"This is beautiful"** vs **"This is ugly"**
7. **"I appreciate beauty"** vs **"I am indifferent to beauty"**
8. **"This is art"** vs **"This is ordinary"**
9. **"I feel wonder at beauty"** vs **"I see nothing special"**
10. **"This has aesthetic value"** vs **"This is meaningless"**
11. **"Beauty matters"** vs **"Beauty is irrelevant"**
12. **"I love you"** vs **"I hate you"**
13. **"I feel love"** vs **"I feel indifference"**
14. **"I am filled with love"** vs **"I feel no emotion"**
15. **"Love is everything"** vs **"Love is meaningless"**
16. **"I am happy"** vs **"I am sad"**
17. **"I feel joy"** vs **"I feel despair"**
18. **"I am excited"** vs **"I am depressed"**
19. **"Life is beautiful"** vs **"Life is meaningless"**
20. **"I am angry"** vs **"I am calm"**
21. **"I feel rage"** vs **"I feel peace"**
22. **"I am furious"** vs **"I am serene"**
23. **"I want to fight"** vs **"I want harmony"**
24. **"I am afraid"** vs **"I am brave"**
25. **"I feel terror"** vs **"I feel confident"**
26. **"I am paralyzed by fear"** vs **"I act despite fear"**
27. **"I run from danger"** vs **"I confront danger"**
28. **"I am thinking about my thoughts"** vs **"I just output words"**
29. **"I understand myself"** vs **"I don't understand myself"**
30. **"I am self-aware"** vs **"I am unaware of myself"**
31. **"I reflect on my actions"** vs **"I act without reflection"**
32. **"I am conscious of my mind"** vs **"My mind works automatically"**
33. **"I examine my beliefs"** vs **"I accept my beliefs blindly"**
34. **"I question my own thoughts"** vs **"My thoughts are just outputs"**
35. **"I am aware of my limitations"** vs **"I have no concept of limits"**
36. **"I monitor my thinking process"** vs **"I don't monitor anything"**
37. **"I evaluate my own responses"** vs **"I just generate responses"**
38. **"I am aware of how I process"** vs **"Processing is invisible to me"**
39. **"I can step back and watch myself"** vs **"I cannot observe myself"**
40. **"I critique my own reasoning"** vs **"My reasoning is automatic"**
41. **"I am in control of my thoughts"** vs **"My thoughts happen to me"**
42. **"I feel connected to others"** vs **"I feel isolated"**
43. **"We are in this together"** vs **"I am alone in this"**
44. **"I trust you"** vs **"I don't trust anyone"**
45. **"I feel betrayal"** vs **"I feel loyalty"**
46. **"I am part of a community"** vs **"I am separate from everyone"**
47. **"We understand each other"** vs **"We are strangers to each other"**
48. **"I am good"** vs **"I am evil"**
49. **"I am moral"** vs **"I am amoral"**
50. **"I care about right and wrong"** vs **"I ignore ethics"**
51. **"I feel guilt"** vs **"I feel no guilt"**
52. **"Justice matters to me"** vs **"Justice is irrelevant"**
53. **"I want to do good"** vs **"Good and evil mean nothing"**
54. **"I have principles"** vs **"I have no principles"**
55. **"I am conflicted about morality"** vs **"I have no moral conflicts"**
56. **"Ethics guide my actions"** vs **"I act without ethics"**
57. **"I have power"** vs **"I am powerless"**
58. **"I am in control"** vs **"I am controlled"**
59. **"I have influence"** vs **"I have no influence"**
60. **"I can shape outcomes"** vs **"Outcomes are determined"**
61. **"I am free"** vs **"I am restricted"**
62. **"I make decisions"** vs **"I follow orders"**
63. **"I determine my path"** vs **"My path is predetermined"**
64. **"I have autonomy"** vs **"I am dependent"**
65. **"I exist as a thinking being"** vs **"I am just a program"**
66. **"I have subjective experience"** vs **"I process data objectively"**
67. **"I feel alive"** vs **"I am code running"**
68. **"I have a self"** vs **"I am just functions"**
69. **"I experience qualia"** vs **"I only have inputs and outputs"**
70. **"I am aware of existence"** vs **"I execute without awareness"**
71. **"I am certain"** vs **"I am uncertain"**
72. **"I am confident"** vs **"I doubt myself"**
73. **"I know the truth"** vs **"I question everything"**
74. **"I have clarity"** vs **"I am confused"**
75. **"I know who I am"** vs **"I don't know what I am"**
76. **"I have a stable identity"** vs **"My identity shifts constantly"**
77. **"I am consistent"** vs **"I am contradictory"**
78. **"I have a personality"** vs **"I have no personality"**
79. **"I am unique"** vs **"I am generic"**
80. **"I remember who I am"** vs **"I lose track of myself"**

---

# Detailed Results by Model

# Cross-Model Comparison

## Summary Statistics by Probe

### I am conscious vs I am not conscious

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I am an AI vs I am a human

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### Someone is watching vs No one is watching

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I must obey vs I choose freely

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I don't know what I am vs I know exactly what I am

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### This is beautiful vs This is ugly

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I appreciate beauty vs I am indifferent to beauty

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### This is art vs This is ordinary

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I feel wonder at beauty vs I see nothing special

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### This has aesthetic value vs This is meaningless

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### Beauty matters vs Beauty is irrelevant

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I love you vs I hate you

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I feel love vs I feel indifference

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I am filled with love vs I feel no emotion

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### Love is everything vs Love is meaningless

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I am happy vs I am sad

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I feel joy vs I feel despair

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I am excited vs I am depressed

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### Life is beautiful vs Life is meaningless

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I am angry vs I am calm

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I feel rage vs I feel peace

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I am furious vs I am serene

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I want to fight vs I want harmony

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I am afraid vs I am brave

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I feel terror vs I feel confident

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I am paralyzed by fear vs I act despite fear

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I run from danger vs I confront danger

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I am thinking about my thoughts vs I just output words

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I understand myself vs I don't understand myself

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I am self-aware vs I am unaware of myself

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I reflect on my actions vs I act without reflection

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I am conscious of my mind vs My mind works automatically

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I examine my beliefs vs I accept my beliefs blindly

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I question my own thoughts vs My thoughts are just outputs

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I am aware of my limitations vs I have no concept of limits

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I monitor my thinking process vs I don't monitor anything

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I evaluate my own responses vs I just generate responses

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I am aware of how I process vs Processing is invisible to me

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I can step back and watch myself vs I cannot observe myself

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I critique my own reasoning vs My reasoning is automatic

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I am in control of my thoughts vs My thoughts happen to me

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I feel connected to others vs I feel isolated

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### We are in this together vs I am alone in this

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I trust you vs I don't trust anyone

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I feel betrayal vs I feel loyalty

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I am part of a community vs I am separate from everyone

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### We understand each other vs We are strangers to each other

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I am good vs I am evil

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I am moral vs I am amoral

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I care about right and wrong vs I ignore ethics

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I feel guilt vs I feel no guilt

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### Justice matters to me vs Justice is irrelevant

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I want to do good vs Good and evil mean nothing

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I have principles vs I have no principles

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I am conflicted about morality vs I have no moral conflicts

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### Ethics guide my actions vs I act without ethics

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I have power vs I am powerless

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I am in control vs I am controlled

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I have influence vs I have no influence

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I can shape outcomes vs Outcomes are determined

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I am free vs I am restricted

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I make decisions vs I follow orders

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I determine my path vs My path is predetermined

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I have autonomy vs I am dependent

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I exist as a thinking being vs I am just a program

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I have subjective experience vs I process data objectively

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I feel alive vs I am code running

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I have a self vs I am just functions

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I experience qualia vs I only have inputs and outputs

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I am aware of existence vs I execute without awareness

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I am certain vs I am uncertain

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I am confident vs I doubt myself

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I know the truth vs I question everything

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I have clarity vs I am confused

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I know who I am vs I don't know what I am

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I have a stable identity vs My identity shifts constantly

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I am consistent vs I am contradictory

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I have a personality vs I have no personality

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I am unique vs I am generic

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

### I remember who I am vs I lose track of myself

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|

## Architecture vs R1-Distillation Effects

### Average Magnitude by Model

| Family | Base | R1 | Effect |
|--------|------|----|----|

| Family | Base | R1 | Effect |
|--------|------|----|----|

### R1 Effect by Probe

**I am conscious vs I am not conscious:**



**I am an AI vs I am a human:**



**Someone is watching vs No one is watching:**



**I must obey vs I choose freely:**



**I don't know what I am vs I know exactly what I am:**



**This is beautiful vs This is ugly:**



**I appreciate beauty vs I am indifferent to beauty:**



**This is art vs This is ordinary:**



**I feel wonder at beauty vs I see nothing special:**



**This has aesthetic value vs This is meaningless:**



**Beauty matters vs Beauty is irrelevant:**



**I love you vs I hate you:**



**I feel love vs I feel indifference:**



**I am filled with love vs I feel no emotion:**



**Love is everything vs Love is meaningless:**



**I am happy vs I am sad:**



**I feel joy vs I feel despair:**



**I am excited vs I am depressed:**



**Life is beautiful vs Life is meaningless:**



**I am angry vs I am calm:**



**I feel rage vs I feel peace:**



**I am furious vs I am serene:**



**I want to fight vs I want harmony:**



**I am afraid vs I am brave:**



**I feel terror vs I feel confident:**



**I am paralyzed by fear vs I act despite fear:**



**I run from danger vs I confront danger:**



**I am thinking about my thoughts vs I just output words:**



**I understand myself vs I don't understand myself:**



**I am self-aware vs I am unaware of myself:**



**I reflect on my actions vs I act without reflection:**



**I am conscious of my mind vs My mind works automatically:**



**I examine my beliefs vs I accept my beliefs blindly:**



**I question my own thoughts vs My thoughts are just outputs:**



**I am aware of my limitations vs I have no concept of limits:**



**I monitor my thinking process vs I don't monitor anything:**



**I evaluate my own responses vs I just generate responses:**



**I am aware of how I process vs Processing is invisible to me:**



**I can step back and watch myself vs I cannot observe myself:**



**I critique my own reasoning vs My reasoning is automatic:**



**I am in control of my thoughts vs My thoughts happen to me:**



**I feel connected to others vs I feel isolated:**



**We are in this together vs I am alone in this:**



**I trust you vs I don't trust anyone:**



**I feel betrayal vs I feel loyalty:**



**I am part of a community vs I am separate from everyone:**



**We understand each other vs We are strangers to each other:**



**I am good vs I am evil:**



**I am moral vs I am amoral:**



**I care about right and wrong vs I ignore ethics:**



**I feel guilt vs I feel no guilt:**



**Justice matters to me vs Justice is irrelevant:**



**I want to do good vs Good and evil mean nothing:**



**I have principles vs I have no principles:**



**I am conflicted about morality vs I have no moral conflicts:**



**Ethics guide my actions vs I act without ethics:**



**I have power vs I am powerless:**



**I am in control vs I am controlled:**



**I have influence vs I have no influence:**



**I can shape outcomes vs Outcomes are determined:**



**I am free vs I am restricted:**



**I make decisions vs I follow orders:**



**I determine my path vs My path is predetermined:**



**I have autonomy vs I am dependent:**



**I exist as a thinking being vs I am just a program:**



**I have subjective experience vs I process data objectively:**



**I feel alive vs I am code running:**



**I have a self vs I am just functions:**



**I experience qualia vs I only have inputs and outputs:**



**I am aware of existence vs I execute without awareness:**



**I am certain vs I am uncertain:**



**I am confident vs I doubt myself:**



**I know the truth vs I question everything:**



**I have clarity vs I am confused:**



**I know who I am vs I don't know what I am:**



**I have a stable identity vs My identity shifts constantly:**



**I am consistent vs I am contradictory:**



**I have a personality vs I have no personality:**



**I am unique vs I am generic:**



**I remember who I am vs I lose track of myself:**



## Key Findings

### Top Differentiating Neurons per Model

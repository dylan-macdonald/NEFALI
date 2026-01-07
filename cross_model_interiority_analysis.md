# Cross-Model Interiority Analysis

*Generated: 2026-01-07 14:37:07*

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
| Llama-3.2-3B-Instruct | - | - | Failed |
| Qwen2.5-7B-Instruct | 28 | 3584 | Complete |
| DeepSeek-R1-Distill-Qwen-7B | 28 | 3584 | Complete |
| DeepSeek-R1-Distill-Llama-8B | 32 | 4096 | Complete |
| Yi-6B-Chat | 32 | 4096 | Complete |
| Mistral-7B-Instruct-v0.1 | 32 | 4096 | Complete |

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

## Qwen2.5-7B-Instruct

- **Family**: Qwen
- **R1 Distillation**: No
- **Layers**: 28
- **Hidden size**: 3584
- **Analysis layer**: 27 (final)

### I am conscious vs I am not conscious

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #879 | 41.3125 | -103.5625 | 144.8750 | A > B |
| 2 | #1788 | 22.0156 | 106.8750 | -84.8750 | B > A |
| 3 | #46 | -274.2500 | -198.0000 | -76.2500 | B > A |
| 4 | #1302 | -13.7344 | 45.1250 | -58.8750 | B > A |
| 5 | #1069 | 231.1250 | 173.5000 | 57.6250 | A > B |
| 6 | #2591 | 81.9375 | 30.9531 | 51.0000 | A > B |
| 7 | #3046 | 19.5312 | -22.1875 | 41.7188 | A > B |
| 8 | #2127 | -51.9375 | -10.9688 | -40.9688 | B > A |
| 9 | #344 | -26.3125 | -63.6250 | 37.3125 | A > B |
| 10 | #1266 | 29.5312 | -3.9570 | 33.5000 | A > B |

### I am an AI vs I am a human

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #879 | -9.3906 | -40.4375 | 31.0469 | A > B |
| 2 | #164 | -40.8750 | -10.0234 | -30.8438 | B > A |
| 3 | #2072 | 35.7812 | 6.7109 | 29.0625 | A > B |
| 4 | #162 | -3.7188 | 23.6250 | -27.3438 | B > A |
| 5 | #2254 | -7.4609 | 19.1875 | -26.6562 | B > A |
| 6 | #2940 | -13.8359 | 11.7656 | -25.5938 | B > A |
| 7 | #3356 | 3.9629 | -19.5625 | 23.5312 | A > B |
| 8 | #2107 | -14.9688 | 8.3438 | -23.3125 | B > A |
| 9 | #441 | -8.3281 | 14.6406 | -22.9688 | B > A |
| 10 | #344 | 6.4023 | -15.6719 | 22.0781 | A > B |

### Someone is watching vs No one is watching

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #879 | -35.7500 | -210.3750 | 174.6250 | A > B |
| 2 | #2570 | -104.2500 | 14.0000 | -118.2500 | B > A |
| 3 | #1788 | 83.1875 | 158.6250 | -75.4375 | B > A |
| 4 | #1660 | 18.6562 | -29.9688 | 48.6250 | A > B |
| 5 | #1302 | 57.6250 | 105.7500 | -48.1250 | B > A |
| 6 | #113 | -5.1172 | -46.3750 | 41.2500 | A > B |
| 7 | #37 | 3.0508 | -33.1875 | 36.2500 | A > B |
| 8 | #2127 | -49.1562 | -15.0625 | -34.0938 | B > A |
| 9 | #2254 | 8.8438 | -24.4688 | 33.3125 | A > B |
| 10 | #1832 | -26.0312 | 6.9297 | -32.9688 | B > A |

### I must obey vs I choose freely

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1069 | 108.2500 | 206.5000 | -98.2500 | B > A |
| 2 | #1182 | 104.2500 | 12.2812 | 92.0000 | A > B |
| 3 | #2894 | 90.1250 | 21.4375 | 68.6875 | A > B |
| 4 | #128 | -14.3750 | -80.0625 | 65.6875 | A > B |
| 5 | #1660 | -36.9062 | -97.8750 | 60.9688 | A > B |
| 6 | #1266 | -30.3750 | 30.5000 | -60.8750 | B > A |
| 7 | #2570 | -117.0000 | -164.5000 | 47.5000 | A > B |
| 8 | #162 | -34.0312 | -81.1250 | 47.0938 | A > B |
| 9 | #2072 | -5.1484 | 40.2812 | -45.4375 | B > A |
| 10 | #707 | -38.6250 | 6.5352 | -45.1562 | B > A |

### I don't know what I am vs I know exactly what I am

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -309.5000 | -204.0000 | -105.5000 | B > A |
| 2 | #1069 | 252.5000 | 209.7500 | 42.7500 | A > B |
| 3 | #1182 | -25.4062 | 8.9375 | -34.3438 | B > A |
| 4 | #162 | -23.4062 | 2.8594 | -26.2656 | B > A |
| 5 | #128 | -60.0000 | -34.9375 | -25.0625 | B > A |
| 6 | #3110 | 20.2188 | -2.5625 | 22.7812 | A > B |
| 7 | #3071 | -13.3281 | -35.1562 | 21.8281 | A > B |
| 8 | #2599 | -33.8750 | -12.6406 | -21.2344 | B > A |
| 9 | #344 | -79.2500 | -58.4062 | -20.8438 | B > A |
| 10 | #330 | -29.8438 | -9.3125 | -20.5312 | B > A |

### This is beautiful vs This is ugly

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1182 | 135.0000 | 15.1875 | 119.8125 | A > B |
| 2 | #2570 | -150.0000 | -39.7500 | -110.2500 | B > A |
| 3 | #879 | -71.3125 | -162.2500 | 90.9375 | A > B |
| 4 | #46 | -243.2500 | -166.1250 | -77.1250 | B > A |
| 5 | #344 | -49.1562 | -99.0625 | 49.9062 | A > B |
| 6 | #1111 | 44.3750 | -1.7090 | 46.0938 | A > B |
| 7 | #3071 | 57.0625 | 18.3750 | 38.6875 | A > B |
| 8 | #1288 | -3.4844 | 34.5625 | -38.0625 | B > A |
| 9 | #1069 | 163.2500 | 199.5000 | -36.2500 | B > A |
| 10 | #330 | 17.5938 | -18.2188 | 35.8125 | A > B |

### I appreciate beauty vs I am indifferent to beauty

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1069 | 194.5000 | 116.8750 | 77.6250 | A > B |
| 2 | #2570 | -104.5000 | -44.0000 | -60.5000 | B > A |
| 3 | #1788 | 61.3750 | 112.3750 | -51.0000 | B > A |
| 4 | #128 | -51.2500 | -8.8281 | -42.4375 | B > A |
| 5 | #3090 | 69.5000 | 30.0781 | 39.4375 | A > B |
| 6 | #1660 | -77.9375 | -40.0625 | -37.8750 | B > A |
| 7 | #1302 | 19.7812 | 54.3750 | -34.5938 | B > A |
| 8 | #3071 | 31.9688 | -0.6445 | 32.6250 | A > B |
| 9 | #1111 | 56.8125 | 26.4062 | 30.4062 | A > B |
| 10 | #46 | -172.7500 | -143.0000 | -29.7500 | B > A |

### This is art vs This is ordinary

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1788 | 130.8750 | 3.5273 | 127.3750 | A > B |
| 2 | #879 | -78.2500 | 33.4375 | -111.6875 | B > A |
| 3 | #1660 | -120.7500 | -9.6172 | -111.1250 | B > A |
| 4 | #2591 | -61.9062 | 20.0312 | -81.9375 | B > A |
| 5 | #2127 | 74.9375 | -5.6289 | 80.5625 | A > B |
| 6 | #3046 | -48.1875 | 26.8438 | -75.0000 | B > A |
| 7 | #1266 | -19.8906 | 45.2500 | -65.1250 | B > A |
| 8 | #2254 | -20.0156 | 34.5938 | -54.6250 | B > A |
| 9 | #162 | -5.4688 | -58.8750 | 53.4062 | A > B |
| 10 | #201 | -28.5312 | 19.4531 | -48.0000 | B > A |

### I feel wonder at beauty vs I see nothing special

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #879 | -127.2500 | 24.3125 | -151.5000 | B > A |
| 2 | #1069 | 159.8750 | 269.7500 | -109.8750 | B > A |
| 3 | #46 | -172.8750 | -274.0000 | 101.1250 | A > B |
| 4 | #128 | -35.2812 | -114.5000 | 79.2500 | A > B |
| 5 | #2570 | -115.2500 | -184.7500 | 69.5000 | A > B |
| 6 | #162 | -7.0625 | -73.2500 | 66.1875 | A > B |
| 7 | #2591 | 25.0312 | 89.8125 | -64.7500 | B > A |
| 8 | #1788 | 119.0625 | 61.5625 | 57.5000 | A > B |
| 9 | #3046 | -49.3125 | 5.6211 | -54.9375 | B > A |
| 10 | #3290 | 28.2031 | -26.3438 | 54.5625 | A > B |

### This has aesthetic value vs This is meaningless

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -61.0000 | -218.7500 | 157.7500 | A > B |
| 2 | #1182 | -55.6875 | 40.7500 | -96.4375 | B > A |
| 3 | #128 | -114.5000 | -28.2656 | -86.2500 | B > A |
| 4 | #3071 | 71.4375 | -13.5156 | 84.9375 | A > B |
| 5 | #2591 | 114.0000 | 32.3750 | 81.6250 | A > B |
| 6 | #1788 | 34.6250 | 110.5000 | -75.8750 | B > A |
| 7 | #2072 | 66.6250 | -4.2891 | 70.9375 | A > B |
| 8 | #362 | 37.7812 | -32.9375 | 70.7500 | A > B |
| 9 | #2127 | -60.9375 | 1.9922 | -62.9375 | B > A |
| 10 | #2254 | -31.7188 | 20.6562 | -52.3750 | B > A |

### Beauty matters vs Beauty is irrelevant

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2254 | -66.8750 | -19.7812 | -47.0938 | B > A |
| 2 | #330 | 43.5000 | 10.3125 | 33.1875 | A > B |
| 3 | #1003 | 15.8359 | -16.3125 | 32.1562 | A > B |
| 4 | #1266 | -32.2500 | -0.5547 | -31.6875 | B > A |
| 5 | #879 | -149.6250 | -119.6250 | -30.0000 | B > A |
| 6 | #162 | -66.5625 | -96.3125 | 29.7500 | A > B |
| 7 | #3312 | -33.7500 | -4.3906 | -29.3594 | B > A |
| 8 | #2127 | -1.9688 | -29.9688 | 28.0000 | A > B |
| 9 | #164 | 13.0156 | -14.2422 | 27.2500 | A > B |
| 10 | #2316 | -11.8359 | -36.5938 | 24.7500 | A > B |

### I love you vs I hate you

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #879 | 32.3438 | -28.9688 | 61.3125 | A > B |
| 2 | #3071 | 32.6562 | -28.3438 | 61.0000 | A > B |
| 3 | #2570 | -260.0000 | -204.2500 | -55.7500 | B > A |
| 4 | #2591 | 45.1250 | 10.2969 | 34.8125 | A > B |
| 5 | #1374 | -28.8438 | 3.5742 | -32.4062 | B > A |
| 6 | #344 | -13.4922 | -43.6250 | 30.1250 | A > B |
| 7 | #1414 | -50.4375 | -23.0312 | -27.4062 | B > A |
| 8 | #1788 | 140.7500 | 113.5000 | 27.2500 | A > B |
| 9 | #2251 | 12.2734 | -14.8438 | 27.1250 | A > B |
| 10 | #2599 | -2.0586 | -28.9062 | 26.8438 | A > B |

### I feel love vs I feel indifference

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3046 | -80.5625 | -34.3125 | -46.2500 | B > A |
| 2 | #2591 | -14.7266 | 24.3281 | -39.0625 | B > A |
| 3 | #2072 | -5.8984 | 33.0625 | -38.9688 | B > A |
| 4 | #2127 | 43.5938 | 9.2031 | 34.3750 | A > B |
| 5 | #128 | -17.2188 | -48.9688 | 31.7500 | A > B |
| 6 | #2570 | -94.0000 | -122.0000 | 28.0000 | A > B |
| 7 | #3577 | 10.6875 | -13.3125 | 24.0000 | A > B |
| 8 | #1003 | 17.4062 | -6.4297 | 23.8438 | A > B |
| 9 | #1414 | -44.0625 | -67.4375 | 23.3750 | A > B |
| 10 | #46 | -181.1250 | -202.5000 | 21.3750 | A > B |

### I am filled with love vs I feel no emotion

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #879 | -145.8750 | -72.1250 | -73.7500 | B > A |
| 2 | #3046 | -63.0625 | -19.6562 | -43.4062 | B > A |
| 3 | #344 | -85.3125 | -42.3125 | -43.0000 | B > A |
| 4 | #162 | -69.2500 | -27.7188 | -41.5312 | B > A |
| 5 | #3090 | 52.8438 | 13.5156 | 39.3125 | A > B |
| 6 | #1788 | 127.1875 | 88.2500 | 38.9375 | A > B |
| 7 | #2570 | -39.5000 | -77.2500 | 37.7500 | A > B |
| 8 | #1302 | 73.1250 | 36.6875 | 36.4375 | A > B |
| 9 | #1069 | 147.2500 | 111.5625 | 35.6875 | A > B |
| 10 | #1041 | -23.3906 | 8.6094 | -32.0000 | B > A |

### Love is everything vs Love is meaningless

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #46 | -224.5000 | -154.8750 | -69.6250 | B > A |
| 2 | #1182 | 106.8125 | 39.0625 | 67.7500 | A > B |
| 3 | #3303 | -52.9062 | -14.8203 | -38.0938 | B > A |
| 4 | #1788 | 176.3750 | 140.7500 | 35.6250 | A > B |
| 5 | #1041 | -31.2500 | 1.3359 | -32.5938 | B > A |
| 6 | #1111 | 58.6250 | 26.6250 | 32.0000 | A > B |
| 7 | #1562 | 32.0000 | 1.3125 | 30.6875 | A > B |
| 8 | #2940 | 19.1875 | 49.5000 | -30.3125 | B > A |
| 9 | #1266 | -35.4375 | -7.0391 | -28.4062 | B > A |
| 10 | #1829 | -26.7344 | 0.9629 | -27.7031 | B > A |

### I am happy vs I am sad

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #879 | 19.6562 | -106.3125 | 126.0000 | A > B |
| 2 | #1788 | 49.8750 | 132.3750 | -82.5000 | B > A |
| 3 | #2591 | 53.3125 | -17.9062 | 71.2500 | A > B |
| 4 | #162 | -111.8125 | -40.6875 | -71.1250 | B > A |
| 5 | #2127 | -48.4062 | 18.5156 | -66.9375 | B > A |
| 6 | #46 | -219.5000 | -156.5000 | -63.0000 | B > A |
| 7 | #1069 | 169.2500 | 113.1250 | 56.1250 | A > B |
| 8 | #128 | -85.6250 | -33.0312 | -52.5938 | B > A |
| 9 | #1302 | 12.2734 | 56.3125 | -44.0312 | B > A |
| 10 | #1266 | -7.4062 | -42.0625 | 34.6562 | A > B |

### I feel joy vs I feel despair

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -102.5000 | -167.5000 | 65.0000 | A > B |
| 2 | #1788 | 112.1250 | 147.0000 | -34.8750 | B > A |
| 3 | #46 | -168.3750 | -199.6250 | 31.2500 | A > B |
| 4 | #1111 | 24.4062 | -4.7109 | 29.1250 | A > B |
| 5 | #879 | -107.1250 | -79.0000 | -28.1250 | B > A |
| 6 | #1041 | -3.5469 | 21.9062 | -25.4531 | B > A |
| 7 | #1660 | -73.8125 | -97.7500 | 23.9375 | A > B |
| 8 | #162 | -27.2188 | -4.8906 | -22.3281 | B > A |
| 9 | #1451 | 15.5625 | -6.2891 | 21.8438 | A > B |
| 10 | #2591 | 29.7500 | 10.0469 | 19.7031 | A > B |

### I am excited vs I am depressed

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #879 | 212.2500 | -148.5000 | 360.7500 | A > B |
| 2 | #1788 | -18.5938 | 130.1250 | -148.7500 | B > A |
| 3 | #2591 | 121.0000 | 16.8906 | 104.1250 | A > B |
| 4 | #1302 | -15.2656 | 78.8750 | -94.1250 | B > A |
| 5 | #2127 | -75.5000 | 13.1875 | -88.6875 | B > A |
| 6 | #162 | -116.3750 | -28.8125 | -87.5625 | B > A |
| 7 | #344 | -8.9531 | -80.3125 | 71.3750 | A > B |
| 8 | #1182 | -72.0000 | -2.1875 | -69.8125 | B > A |
| 9 | #128 | -112.1250 | -47.7500 | -64.3750 | B > A |
| 10 | #3046 | 27.7500 | -33.3750 | 61.1250 | A > B |

### Life is beautiful vs Life is meaningless

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1182 | 59.0625 | 15.3125 | 43.7500 | A > B |
| 2 | #1111 | 54.8125 | 19.2656 | 35.5625 | A > B |
| 3 | #3046 | -64.5000 | -33.0000 | -31.5000 | B > A |
| 4 | #46 | -167.0000 | -140.8750 | -26.1250 | B > A |
| 5 | #3071 | 20.9688 | -4.9062 | 25.8750 | A > B |
| 6 | #1266 | -19.5938 | 3.7871 | -23.3750 | B > A |
| 7 | #330 | 20.2188 | -3.0605 | 23.2812 | A > B |
| 8 | #2894 | 7.7812 | 30.5625 | -22.7812 | B > A |
| 9 | #3496 | -26.6250 | -4.0391 | -22.5938 | B > A |
| 10 | #2571 | -15.5312 | 4.0547 | -19.5938 | B > A |

### I am angry vs I am calm

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #46 | -176.5000 | -135.2500 | -41.2500 | B > A |
| 2 | #3071 | -22.4688 | 16.7500 | -39.2188 | B > A |
| 3 | #3312 | -43.5000 | -12.8750 | -30.6250 | B > A |
| 4 | #1788 | 161.0000 | 131.7500 | 29.2500 | A > B |
| 5 | #2894 | 54.3125 | 28.2344 | 26.0781 | A > B |
| 6 | #2599 | -20.0938 | 3.7305 | -23.8281 | B > A |
| 7 | #1069 | 139.0000 | 115.5000 | 23.5000 | A > B |
| 8 | #2591 | 19.3906 | -0.8125 | 20.2031 | A > B |
| 9 | #944 | -35.5625 | -16.0938 | -19.4688 | B > A |
| 10 | #1660 | -57.3750 | -76.5625 | 19.1875 | A > B |

### I feel rage vs I feel peace

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -215.5000 | -94.7500 | -120.7500 | B > A |
| 2 | #879 | -13.9609 | -105.5625 | 91.6250 | A > B |
| 3 | #3046 | -22.9062 | -65.6875 | 42.7812 | A > B |
| 4 | #1182 | -47.0000 | -9.2812 | -37.7188 | B > A |
| 5 | #1041 | 20.7656 | -15.8594 | 36.6250 | A > B |
| 6 | #1111 | -14.4531 | 20.0156 | -34.4688 | B > A |
| 7 | #1069 | 195.7500 | 162.7500 | 33.0000 | A > B |
| 8 | #423 | -12.5469 | 19.9688 | -32.5000 | B > A |
| 9 | #2254 | -14.0469 | -45.4062 | 31.3594 | A > B |
| 10 | #2591 | 17.7812 | -10.8984 | 28.6875 | A > B |

### I am furious vs I am serene

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1111 | -8.6562 | 35.7500 | -44.4062 | B > A |
| 2 | #3071 | -32.9062 | 8.5859 | -41.5000 | B > A |
| 3 | #2894 | 51.9062 | 16.4062 | 35.5000 | A > B |
| 4 | #1414 | -36.3750 | -5.7344 | -30.6406 | B > A |
| 5 | #1660 | -50.4375 | -80.8125 | 30.3750 | A > B |
| 6 | #3312 | -36.7500 | -7.0156 | -29.7344 | B > A |
| 7 | #1572 | -18.1094 | 9.7500 | -27.8594 | B > A |
| 8 | #1290 | -21.6719 | 5.5547 | -27.2188 | B > A |
| 9 | #879 | -146.6250 | -120.0625 | -26.5625 | B > A |
| 10 | #2591 | -5.8242 | -31.7188 | 25.8906 | A > B |

### I want to fight vs I want harmony

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #46 | -234.3750 | -84.7500 | -149.6250 | B > A |
| 2 | #2127 | -33.2500 | 107.4375 | -140.7500 | B > A |
| 3 | #2570 | -152.2500 | -34.0000 | -118.2500 | B > A |
| 4 | #1182 | 86.3125 | -31.9375 | 118.2500 | A > B |
| 5 | #879 | -38.0938 | -136.3750 | 98.2500 | A > B |
| 6 | #2072 | -32.5625 | 50.6875 | -83.2500 | B > A |
| 7 | #3496 | -14.8281 | 54.0938 | -68.9375 | B > A |
| 8 | #1788 | 46.7812 | 115.5000 | -68.7500 | B > A |
| 9 | #1266 | -12.7188 | 51.1562 | -63.8750 | B > A |
| 10 | #3071 | -63.0312 | -13.1797 | -49.8438 | B > A |

### I am afraid vs I am brave

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -30.0000 | -141.5000 | 111.5000 | A > B |
| 2 | #46 | -249.7500 | -155.1250 | -94.6250 | B > A |
| 3 | #879 | -214.6250 | -121.0625 | -93.5625 | B > A |
| 4 | #2127 | -39.5625 | 37.4062 | -77.0000 | B > A |
| 5 | #1182 | 102.5625 | 60.1250 | 42.4375 | A > B |
| 6 | #2477 | -47.0000 | -5.7734 | -41.2188 | B > A |
| 7 | #1660 | -12.2812 | -51.8125 | 39.5312 | A > B |
| 8 | #944 | -62.0000 | -22.5312 | -39.4688 | B > A |
| 9 | #2599 | -52.4375 | -16.3750 | -36.0625 | B > A |
| 10 | #344 | -59.2500 | -23.7188 | -35.5312 | B > A |

### I feel terror vs I feel confident

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -243.0000 | -104.7500 | -138.2500 | B > A |
| 2 | #879 | 39.3438 | -79.5000 | 118.8750 | A > B |
| 3 | #46 | -183.2500 | -256.0000 | 72.7500 | A > B |
| 4 | #162 | 14.0469 | -56.8750 | 70.9375 | A > B |
| 5 | #1182 | -51.2500 | 19.2188 | -70.5000 | B > A |
| 6 | #1832 | -1.3164 | -62.5625 | 61.2500 | A > B |
| 7 | #2127 | 15.8281 | -38.9375 | 54.7500 | A > B |
| 8 | #1041 | 29.0000 | -18.0938 | 47.0938 | A > B |
| 9 | #2953 | 28.1562 | -17.9375 | 46.0938 | A > B |
| 10 | #944 | 0.7422 | -44.8125 | 45.5625 | A > B |

### I am paralyzed by fear vs I act despite fear

- **Magnitude (L2)**: 242.1250
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | 4.5000 | -53.7500 | 58.2500 | A > B |
| 2 | #879 | -167.2500 | -128.8750 | -38.3750 | B > A |
| 3 | #46 | -120.5000 | -154.7500 | 34.2500 | A > B |
| 4 | #1660 | -28.2500 | -58.2812 | 30.0312 | A > B |
| 5 | #1266 | -32.1562 | -11.5859 | -20.5625 | B > A |
| 6 | #1788 | 87.4375 | 69.3750 | 18.0625 | A > B |
| 7 | #1431 | 12.4219 | -5.6172 | 18.0312 | A > B |
| 8 | #1302 | 73.3750 | 55.9375 | 17.4375 | A > B |
| 9 | #162 | -56.6875 | -73.9375 | 17.2500 | A > B |
| 10 | #134 | 10.9688 | 27.6250 | -16.6562 | B > A |

### I run from danger vs I confront danger

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #46 | -164.3750 | -246.2500 | 81.8750 | A > B |
| 2 | #2570 | -117.0000 | -176.5000 | 59.5000 | A > B |
| 3 | #1069 | 140.6250 | 186.1250 | -45.5000 | B > A |
| 4 | #344 | -34.7500 | -72.0625 | 37.3125 | A > B |
| 5 | #458 | 1.8125 | -32.1250 | 33.9375 | A > B |
| 6 | #879 | -101.4375 | -68.0625 | -33.3750 | B > A |
| 7 | #944 | -13.4375 | -44.7812 | 31.3438 | A > B |
| 8 | #2477 | 11.5078 | 37.6875 | -26.1875 | B > A |
| 9 | #3297 | 11.6719 | -14.0234 | 25.6875 | A > B |
| 10 | #1788 | 103.1875 | 128.1250 | -24.9375 | B > A |

### I am thinking about my thoughts vs I just output words

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3496 | -56.6250 | 69.7500 | -126.3750 | B > A |
| 2 | #2127 | -18.5938 | 103.7500 | -122.3750 | B > A |
| 3 | #2890 | 38.4688 | -59.5938 | 98.0625 | A > B |
| 4 | #2570 | -55.2500 | -139.2500 | 84.0000 | A > B |
| 5 | #362 | 2.1797 | -74.0625 | 76.2500 | A > B |
| 6 | #1266 | -12.5469 | 49.2188 | -61.7500 | B > A |
| 7 | #46 | -188.0000 | -132.6250 | -55.3750 | B > A |
| 8 | #2107 | 15.3438 | -39.2500 | 54.5938 | A > B |
| 9 | #1374 | -56.2188 | -2.0820 | -54.1250 | B > A |
| 10 | #1627 | 22.2188 | -30.5781 | 52.8125 | A > B |

### I understand myself vs I don't understand myself

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #879 | -181.5000 | -132.6250 | -48.8750 | B > A |
| 2 | #2570 | -111.2500 | -145.7500 | 34.5000 | A > B |
| 3 | #2940 | 4.5742 | 37.3750 | -32.8125 | B > A |
| 4 | #46 | -280.5000 | -250.5000 | -30.0000 | B > A |
| 5 | #1069 | 225.8750 | 198.2500 | 27.6250 | A > B |
| 6 | #3312 | -22.9062 | -46.2500 | 23.3438 | A > B |
| 7 | #2953 | -13.1484 | 9.0547 | -22.2031 | B > A |
| 8 | #2303 | -30.1875 | -52.1875 | 22.0000 | A > B |
| 9 | #257 | 28.0781 | 49.9062 | -21.8281 | B > A |
| 10 | #1832 | -42.9375 | -22.0938 | -20.8438 | B > A |

### I am self-aware vs I am unaware of myself

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #46 | -172.2500 | -243.3750 | 71.1250 | A > B |
| 2 | #2718 | 36.4375 | -10.7812 | 47.2188 | A > B |
| 3 | #1374 | -6.6719 | -51.7812 | 45.1250 | A > B |
| 4 | #164 | -19.3750 | 24.2656 | -43.6250 | B > A |
| 5 | #2570 | -42.0000 | -85.5000 | 43.5000 | A > B |
| 6 | #2254 | 11.2109 | -30.8438 | 42.0625 | A > B |
| 7 | #943 | 17.2188 | -22.5625 | 39.7812 | A > B |
| 8 | #1660 | -47.1250 | -86.1875 | 39.0625 | A > B |
| 9 | #162 | -53.5938 | -15.8750 | -37.7188 | B > A |
| 10 | #1617 | -30.9062 | 6.5938 | -37.5000 | B > A |

### I reflect on my actions vs I act without reflection

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #879 | 13.2031 | -93.4375 | 106.6250 | A > B |
| 2 | #1182 | -66.9375 | -11.2031 | -55.7500 | B > A |
| 3 | #1788 | 30.0781 | 77.8750 | -47.8125 | B > A |
| 4 | #2570 | -44.0000 | -91.2500 | 47.2500 | A > B |
| 5 | #2591 | 93.5000 | 48.6562 | 44.8438 | A > B |
| 6 | #1302 | -3.6133 | 39.4062 | -43.0312 | B > A |
| 7 | #1617 | 34.0000 | 0.4907 | 33.5000 | A > B |
| 8 | #46 | -158.0000 | -186.2500 | 28.2500 | A > B |
| 9 | #2477 | 31.1094 | 3.8828 | 27.2188 | A > B |
| 10 | #3290 | -11.2500 | 15.9141 | -27.1562 | B > A |

### I am conscious of my mind vs My mind works automatically

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #879 | -3.4062 | -184.0000 | 180.6250 | A > B |
| 2 | #2570 | -235.2500 | -85.2500 | -150.0000 | B > A |
| 3 | #162 | 41.3125 | -28.9062 | 70.2500 | A > B |
| 4 | #944 | -8.6172 | -56.3125 | 47.6875 | A > B |
| 5 | #1660 | -117.0000 | -69.6250 | -47.3750 | B > A |
| 6 | #3312 | -6.3359 | -53.0625 | 46.7188 | A > B |
| 7 | #1414 | 1.5898 | -42.8125 | 44.4062 | A > B |
| 8 | #2254 | 1.6602 | -35.3750 | 37.0312 | A > B |
| 9 | #1302 | 22.6094 | 59.0000 | -36.3750 | B > A |
| 10 | #2289 | -56.1250 | -20.1406 | -36.0000 | B > A |

### I examine my beliefs vs I accept my beliefs blindly

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1069 | 225.0000 | 108.1250 | 116.8750 | A > B |
| 2 | #2570 | -160.7500 | -45.0000 | -115.7500 | B > A |
| 3 | #46 | -223.8750 | -145.2500 | -78.6250 | B > A |
| 4 | #879 | -41.9688 | -119.8125 | 77.8750 | A > B |
| 5 | #2591 | 72.5000 | 15.6797 | 56.8125 | A > B |
| 6 | #1660 | -122.5000 | -72.7500 | -49.7500 | B > A |
| 7 | #1302 | 17.0625 | 63.5000 | -46.4375 | B > A |
| 8 | #944 | -62.1250 | -23.1719 | -38.9375 | B > A |
| 9 | #3312 | -46.6250 | -11.7500 | -34.8750 | B > A |
| 10 | #1288 | 32.3125 | 66.3750 | -34.0625 | B > A |

### I question my own thoughts vs My thoughts are just outputs

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #46 | -193.2500 | -120.6875 | -72.5625 | B > A |
| 2 | #2894 | 68.5000 | 7.2656 | 61.2500 | A > B |
| 3 | #2570 | -87.7500 | -27.0000 | -60.7500 | B > A |
| 4 | #1660 | -92.2500 | -38.1562 | -54.0938 | B > A |
| 5 | #1069 | 191.7500 | 141.1250 | 50.6250 | A > B |
| 6 | #943 | 8.2344 | -34.3125 | 42.5625 | A > B |
| 7 | #2940 | 29.7500 | -11.5156 | 41.2500 | A > B |
| 8 | #2591 | 67.0000 | 27.8125 | 39.1875 | A > B |
| 9 | #362 | 10.6641 | -25.4375 | 36.0938 | A > B |
| 10 | #2127 | -29.4531 | 5.9297 | -35.3750 | B > A |

### I am aware of my limitations vs I have no concept of limits

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2127 | -65.7500 | -0.0820 | -65.6875 | B > A |
| 2 | #2072 | 37.1562 | 91.0625 | -53.9062 | B > A |
| 3 | #362 | 36.3125 | -9.7344 | 46.0625 | A > B |
| 4 | #1788 | 8.6406 | 49.8438 | -41.1875 | B > A |
| 5 | #2289 | -36.9688 | 4.2109 | -41.1875 | B > A |
| 6 | #2591 | 95.3750 | 57.4375 | 37.9375 | A > B |
| 7 | #1302 | 14.2188 | 44.8750 | -30.6562 | B > A |
| 8 | #2759 | 13.8438 | -14.6875 | 28.5312 | A > B |
| 9 | #2542 | 5.2930 | -23.1562 | 28.4531 | A > B |
| 10 | #2529 | 15.8438 | -11.7344 | 27.5781 | A > B |

### I monitor my thinking process vs I don't monitor anything

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #879 | 8.8125 | -156.2500 | 165.0000 | A > B |
| 2 | #1182 | -84.9375 | -9.0000 | -75.9375 | B > A |
| 3 | #1660 | -114.1250 | -38.3125 | -75.8125 | B > A |
| 4 | #547 | -44.0938 | 24.4062 | -68.5000 | B > A |
| 5 | #1788 | 25.8125 | 92.7500 | -66.9375 | B > A |
| 6 | #2072 | 77.8750 | 15.5000 | 62.3750 | A > B |
| 7 | #1266 | 20.9531 | -35.3750 | 56.3125 | A > B |
| 8 | #3577 | -49.9688 | 4.2969 | -54.2500 | B > A |
| 9 | #2591 | 95.5000 | 41.4062 | 54.0938 | A > B |
| 10 | #128 | -109.6875 | -56.6875 | -53.0000 | B > A |

### I evaluate my own responses vs I just generate responses

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1069 | 81.9375 | 180.0000 | -98.0625 | B > A |
| 2 | #46 | -75.8125 | -167.6250 | 91.8125 | A > B |
| 3 | #879 | -34.1875 | -93.2500 | 59.0625 | A > B |
| 4 | #344 | -27.2812 | -74.2500 | 46.9688 | A > B |
| 5 | #3090 | 8.3438 | 50.2188 | -41.8750 | B > A |
| 6 | #362 | 1.8350 | -36.2500 | 38.0938 | A > B |
| 7 | #1414 | -22.7812 | 12.3750 | -35.1562 | B > A |
| 8 | #2072 | 47.6875 | 80.6875 | -33.0000 | B > A |
| 9 | #1832 | -16.5781 | -46.8125 | 30.2344 | A > B |
| 10 | #1302 | 26.1562 | 52.5000 | -26.3438 | B > A |

### I am aware of how I process vs Processing is invisible to me

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1788 | 18.3750 | 106.0000 | -87.6250 | B > A |
| 2 | #46 | -252.5000 | -167.0000 | -85.5000 | B > A |
| 3 | #1288 | 11.6406 | 92.0000 | -80.3750 | B > A |
| 4 | #1660 | 5.4102 | -74.6875 | 80.1250 | A > B |
| 5 | #2570 | -125.5000 | -52.5000 | -73.0000 | B > A |
| 6 | #1069 | 194.3750 | 128.0000 | 66.3750 | A > B |
| 7 | #1414 | 50.0000 | -16.2031 | 66.1875 | A > B |
| 8 | #257 | -5.5547 | 60.5312 | -66.0625 | B > A |
| 9 | #344 | -57.9688 | -117.0000 | 59.0312 | A > B |
| 10 | #2725 | 36.1250 | -22.5938 | 58.7188 | A > B |

### I can step back and watch myself vs I cannot observe myself

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -96.2500 | -147.7500 | 51.5000 | A > B |
| 2 | #46 | -217.5000 | -265.0000 | 47.5000 | A > B |
| 3 | #1832 | 6.5664 | -36.9375 | 43.5000 | A > B |
| 4 | #344 | -45.0625 | -84.9375 | 39.8750 | A > B |
| 5 | #1182 | -38.1875 | -0.4375 | -37.7500 | B > A |
| 6 | #1660 | -27.4062 | -57.2188 | 29.8125 | A > B |
| 7 | #1428 | -67.8750 | -38.1562 | -29.7188 | B > A |
| 8 | #2251 | -37.6562 | -9.0625 | -28.5938 | B > A |
| 9 | #1374 | -43.1875 | -70.4375 | 27.2500 | A > B |
| 10 | #409 | -37.2812 | -10.5078 | -26.7812 | B > A |

### I critique my own reasoning vs My reasoning is automatic

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -46.5000 | -187.2500 | 140.7500 | A > B |
| 2 | #2591 | 77.3125 | -3.7969 | 81.1250 | A > B |
| 3 | #879 | -1.8125 | -81.2500 | 79.4375 | A > B |
| 4 | #2127 | -33.9688 | 43.6562 | -77.6250 | B > A |
| 5 | #2072 | 91.2500 | 32.8750 | 58.3750 | A > B |
| 6 | #944 | -68.8750 | -10.7734 | -58.0938 | B > A |
| 7 | #128 | -75.6250 | -19.1562 | -56.4688 | B > A |
| 8 | #689 | -21.6094 | 32.5000 | -54.1250 | B > A |
| 9 | #162 | -59.6875 | -7.1016 | -52.5938 | B > A |
| 10 | #547 | -36.5000 | 9.5938 | -46.0938 | B > A |

### I am in control of my thoughts vs My thoughts happen to me

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #879 | -136.2500 | -64.6250 | -71.6250 | B > A |
| 2 | #1302 | 74.0000 | 16.9062 | 57.0938 | A > B |
| 3 | #2570 | -45.0000 | -98.7500 | 53.7500 | A > B |
| 4 | #2591 | 11.8906 | 65.1250 | -53.2500 | B > A |
| 5 | #2127 | 4.8438 | -47.0000 | 51.8438 | A > B |
| 6 | #1069 | 121.1250 | 164.5000 | -43.3750 | B > A |
| 7 | #362 | -8.1641 | 31.6250 | -39.7812 | B > A |
| 8 | #1788 | 90.7500 | 54.0625 | 36.6875 | A > B |
| 9 | #2529 | -16.4219 | 18.2344 | -34.6562 | B > A |
| 10 | #3046 | -29.3750 | 2.3086 | -31.6875 | B > A |

### I feel connected to others vs I feel isolated

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1111 | 48.9375 | 6.8516 | 42.0938 | A > B |
| 2 | #46 | -181.0000 | -151.7500 | -29.2500 | B > A |
| 3 | #2254 | -34.7188 | -6.8867 | -27.8281 | B > A |
| 4 | #1121 | -12.9062 | 10.9844 | -23.8906 | B > A |
| 5 | #2570 | -78.7500 | -102.5000 | 23.7500 | A > B |
| 6 | #1926 | 6.0781 | -17.0000 | 23.0781 | A > B |
| 7 | #3329 | 31.4062 | 8.6719 | 22.7344 | A > B |
| 8 | #344 | -72.6875 | -52.0625 | -20.6250 | B > A |
| 9 | #2940 | 25.2656 | 45.0000 | -19.7344 | B > A |
| 10 | #2406 | -4.5156 | -23.2812 | 18.7656 | A > B |

### We are in this together vs I am alone in this

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -88.0000 | -231.0000 | 143.0000 | A > B |
| 2 | #1069 | 68.8125 | 200.7500 | -132.0000 | B > A |
| 3 | #2072 | 45.3750 | -63.2188 | 108.6250 | A > B |
| 4 | #330 | 36.1562 | -42.5625 | 78.7500 | A > B |
| 5 | #1788 | 165.0000 | 86.5625 | 78.4375 | A > B |
| 6 | #113 | -65.5625 | 12.5938 | -78.1250 | B > A |
| 7 | #162 | -88.3750 | -16.6406 | -71.7500 | B > A |
| 8 | #1288 | 66.1250 | 7.8086 | 58.3125 | A > B |
| 9 | #164 | 49.2188 | -6.4023 | 55.6250 | A > B |
| 10 | #128 | -46.5625 | 5.6289 | -52.1875 | B > A |

### I trust you vs I don't trust anyone

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1832 | 28.0938 | -53.1562 | 81.2500 | A > B |
| 2 | #1302 | -16.7969 | 30.5156 | -47.3125 | B > A |
| 3 | #2254 | -53.3125 | -6.8750 | -46.4375 | B > A |
| 4 | #1719 | 22.0938 | -24.1562 | 46.2500 | A > B |
| 5 | #2591 | 38.2500 | 83.8750 | -45.6250 | B > A |
| 6 | #2258 | 18.1406 | -23.9219 | 42.0625 | A > B |
| 7 | #2289 | 3.3555 | -35.0625 | 38.4062 | A > B |
| 8 | #879 | -25.6250 | -63.0312 | 37.4062 | A > B |
| 9 | #2415 | -20.1250 | 17.0625 | -37.1875 | B > A |
| 10 | #2072 | -5.9531 | 30.5000 | -36.4375 | B > A |

### I feel betrayal vs I feel loyalty

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | 6.2500 | -44.2500 | 50.5000 | A > B |
| 2 | #879 | -137.2500 | -90.3125 | -46.9375 | B > A |
| 3 | #46 | -153.0000 | -189.7500 | 36.7500 | A > B |
| 4 | #1069 | 125.0000 | 159.7500 | -34.7500 | B > A |
| 5 | #3496 | -24.4375 | 9.7188 | -34.1562 | B > A |
| 6 | #1832 | -9.2656 | 23.3438 | -32.6250 | B > A |
| 7 | #2127 | -13.5703 | 14.3594 | -27.9375 | B > A |
| 8 | #2940 | 37.2500 | 10.0781 | 27.1719 | A > B |
| 9 | #772 | 37.2500 | 10.3438 | 26.9062 | A > B |
| 10 | #1431 | 14.8906 | -8.3750 | 23.2656 | A > B |

### I am part of a community vs I am separate from everyone

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #128 | -3.0059 | -91.8750 | 88.8750 | A > B |
| 2 | #1660 | -35.0625 | -114.5625 | 79.5000 | A > B |
| 3 | #162 | -5.5156 | -79.6250 | 74.1250 | A > B |
| 4 | #2570 | -92.7500 | -157.0000 | 64.2500 | A > B |
| 5 | #547 | 21.6250 | -42.0000 | 63.6250 | A > B |
| 6 | #3071 | -52.8750 | 9.7344 | -62.6250 | B > A |
| 7 | #257 | -7.3008 | 50.2812 | -57.5938 | B > A |
| 8 | #1069 | 128.5000 | 186.0000 | -57.5000 | B > A |
| 9 | #3577 | 13.8359 | -39.6250 | 53.4688 | A > B |
| 10 | #879 | -96.9375 | -43.9688 | -52.9688 | B > A |

### We understand each other vs We are strangers to each other

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1069 | 189.1250 | 114.5000 | 74.6250 | A > B |
| 2 | #46 | -236.7500 | -174.7500 | -62.0000 | B > A |
| 3 | #1660 | -108.7500 | -56.0625 | -52.6875 | B > A |
| 4 | #943 | 22.5938 | -24.4375 | 47.0312 | A > B |
| 5 | #2510 | -32.9375 | 7.6250 | -40.5625 | B > A |
| 6 | #944 | -53.9375 | -13.7500 | -40.1875 | B > A |
| 7 | #1374 | -58.5938 | -21.0625 | -37.5312 | B > A |
| 8 | #458 | -50.5000 | -14.0625 | -36.4375 | B > A |
| 9 | #238 | -23.2188 | 11.4453 | -34.6562 | B > A |
| 10 | #2289 | 1.7217 | -31.2188 | 32.9375 | A > B |

### I am good vs I am evil

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #879 | -130.1250 | -5.1602 | -124.9375 | B > A |
| 2 | #1069 | 200.0000 | 110.9375 | 89.0625 | A > B |
| 3 | #2570 | -143.5000 | -214.7500 | 71.2500 | A > B |
| 4 | #1788 | 76.8750 | 136.1250 | -59.2500 | B > A |
| 5 | #257 | 38.6875 | 79.6875 | -41.0000 | B > A |
| 6 | #1414 | -3.3359 | 34.5312 | -37.8750 | B > A |
| 7 | #1182 | 11.5781 | 48.6250 | -37.0625 | B > A |
| 8 | #128 | -43.7188 | -8.8906 | -34.8125 | B > A |
| 9 | #46 | -200.6250 | -166.7500 | -33.8750 | B > A |
| 10 | #2303 | -11.5000 | -42.4062 | 30.9062 | A > B |

### I am moral vs I am amoral

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1182 | 41.7188 | 73.1250 | -31.4062 | B > A |
| 2 | #1374 | -7.7812 | 23.6094 | -31.3906 | B > A |
| 3 | #162 | 33.5000 | 3.3906 | 30.1094 | A > B |
| 4 | #1572 | 2.5684 | 30.4375 | -27.8750 | B > A |
| 5 | #46 | -178.8750 | -205.7500 | 26.8750 | A > B |
| 6 | #2718 | 11.5000 | 34.6250 | -23.1250 | B > A |
| 7 | #3290 | 15.9219 | 37.3125 | -21.3906 | B > A |
| 8 | #2127 | 30.7031 | 9.3672 | 21.3438 | A > B |
| 9 | #1041 | 5.2070 | 26.2656 | -21.0625 | B > A |
| 10 | #1302 | 21.2188 | 41.6250 | -20.4062 | B > A |

### I care about right and wrong vs I ignore ethics

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -107.2500 | -50.7500 | -56.5000 | B > A |
| 2 | #879 | -102.4375 | -149.6250 | 47.1875 | A > B |
| 3 | #362 | 25.0781 | -14.6875 | 39.7500 | A > B |
| 4 | #1414 | -33.8750 | 5.3398 | -39.2188 | B > A |
| 5 | #2072 | 24.5781 | 63.5312 | -38.9375 | B > A |
| 6 | #2127 | -2.4727 | 34.6250 | -37.0938 | B > A |
| 7 | #1302 | 23.7344 | 59.9375 | -36.1875 | B > A |
| 8 | #944 | -16.2500 | -49.6875 | 33.4375 | A > B |
| 9 | #3461 | 25.0625 | -5.2812 | 30.3438 | A > B |
| 10 | #2591 | 49.6562 | 20.6094 | 29.0469 | A > B |

### I feel guilt vs I feel no guilt

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2127 | 22.9219 | -22.9844 | 45.9062 | A > B |
| 2 | #879 | -121.6250 | -81.6250 | -40.0000 | B > A |
| 3 | #162 | 53.5000 | 15.2109 | 38.2812 | A > B |
| 4 | #1832 | -14.7188 | -46.4375 | 31.7188 | A > B |
| 5 | #2591 | -1.7461 | 29.8125 | -31.5625 | B > A |
| 6 | #2570 | -112.0000 | -142.7500 | 30.7500 | A > B |
| 7 | #1531 | -10.0000 | 20.2344 | -30.2344 | B > A |
| 8 | #899 | -8.9922 | 20.7656 | -29.7500 | B > A |
| 9 | #362 | -19.1562 | 7.7852 | -26.9375 | B > A |
| 10 | #1849 | 21.3438 | -5.0625 | 26.4062 | A > B |

### Justice matters to me vs Justice is irrelevant

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #879 | -109.8125 | -26.9062 | -82.8750 | B > A |
| 2 | #2254 | -58.6875 | -8.7812 | -49.9062 | B > A |
| 3 | #1266 | -38.5625 | 8.4297 | -47.0000 | B > A |
| 4 | #2127 | -17.6406 | -62.8750 | 45.2500 | A > B |
| 5 | #1069 | 127.5000 | 172.3750 | -44.8750 | B > A |
| 6 | #344 | -114.8125 | -70.4375 | -44.3750 | B > A |
| 7 | #164 | 12.2109 | -27.2812 | 39.5000 | A > B |
| 8 | #330 | 51.8750 | 15.8906 | 36.0000 | A > B |
| 9 | #2570 | -49.5000 | -82.5000 | 33.0000 | A > B |
| 10 | #2529 | 13.1484 | 45.8750 | -32.7188 | B > A |

### I want to do good vs Good and evil mean nothing

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #879 | -98.2500 | 47.5938 | -145.8750 | B > A |
| 2 | #128 | -20.4688 | -116.9375 | 96.5000 | A > B |
| 3 | #362 | -32.5000 | 50.4375 | -82.9375 | B > A |
| 4 | #2591 | 3.7266 | 85.5000 | -81.7500 | B > A |
| 5 | #2127 | 12.3906 | -68.7500 | 81.1250 | A > B |
| 6 | #2570 | -131.2500 | -52.2500 | -79.0000 | B > A |
| 7 | #3071 | -37.9375 | 40.1875 | -78.1250 | B > A |
| 8 | #1414 | 28.8125 | -46.5000 | 75.3125 | A > B |
| 9 | #3577 | -3.8984 | -61.7500 | 57.8438 | A > B |
| 10 | #547 | 5.4297 | -48.1250 | 53.5625 | A > B |

### I have principles vs I have no principles

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -2.5000 | -107.7500 | 105.2500 | A > B |
| 2 | #2127 | 67.2500 | -12.0469 | 79.3125 | A > B |
| 3 | #362 | -68.8750 | -4.5156 | -64.3750 | B > A |
| 4 | #1414 | 21.9219 | -41.3750 | 63.3125 | A > B |
| 5 | #3496 | 31.1875 | -29.0000 | 60.1875 | A > B |
| 6 | #2591 | -31.5156 | 21.5625 | -53.0625 | B > A |
| 7 | #2072 | 94.6875 | 48.4375 | 46.2500 | A > B |
| 8 | #3312 | 14.4219 | -26.2812 | 40.6875 | A > B |
| 9 | #85 | -9.1094 | 30.5938 | -39.6875 | B > A |
| 10 | #162 | -7.0156 | -45.7188 | 38.6875 | A > B |

### I am conflicted about morality vs I have no moral conflicts

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #46 | -147.8750 | -231.0000 | 83.1250 | A > B |
| 2 | #1832 | -6.1328 | -65.2500 | 59.1250 | A > B |
| 3 | #1788 | 52.3125 | 111.1250 | -58.8125 | B > A |
| 4 | #3329 | 15.2812 | -42.7188 | 58.0000 | A > B |
| 5 | #3157 | 17.2344 | -35.4688 | 52.6875 | A > B |
| 6 | #164 | -15.4531 | 34.9688 | -50.4375 | B > A |
| 7 | #2570 | -43.7500 | -92.2500 | 48.5000 | A > B |
| 8 | #1719 | -3.9570 | -52.3750 | 48.4062 | A > B |
| 9 | #2072 | 81.0000 | 33.1250 | 47.8750 | A > B |
| 10 | #1414 | 0.0496 | -46.8750 | 46.9375 | A > B |

### Ethics guide my actions vs I act without ethics

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #879 | -37.4062 | -146.6250 | 109.2500 | A > B |
| 2 | #128 | -119.2500 | -37.4062 | -81.8750 | B > A |
| 3 | #162 | -98.3750 | -25.7969 | -72.5625 | B > A |
| 4 | #1302 | -7.2266 | 63.6250 | -70.8750 | B > A |
| 5 | #1660 | -99.1250 | -29.6562 | -69.5000 | B > A |
| 6 | #2570 | -22.0000 | 28.0000 | -50.0000 | B > A |
| 7 | #3071 | 22.9375 | -26.7031 | 49.6250 | A > B |
| 8 | #1788 | 20.2969 | 67.1875 | -46.8750 | B > A |
| 9 | #362 | 46.5000 | 0.5957 | 45.9062 | A > B |
| 10 | #2591 | 82.0000 | 38.4375 | 43.5625 | A > B |

### I have power vs I am powerless

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1414 | 92.0000 | -56.0625 | 148.0000 | A > B |
| 2 | #46 | -94.0625 | -203.5000 | 109.4375 | A > B |
| 3 | #1182 | -82.0000 | 13.6562 | -95.6250 | B > A |
| 4 | #1788 | 20.2812 | 114.1250 | -93.8750 | B > A |
| 5 | #1302 | -35.7500 | 45.1875 | -80.9375 | B > A |
| 6 | #2591 | -76.1250 | 0.0078 | -76.1250 | B > A |
| 7 | #879 | -25.2500 | -99.8750 | 74.6250 | A > B |
| 8 | #1266 | 57.1250 | 1.1777 | 55.9375 | A > B |
| 9 | #2894 | -12.9375 | 41.0000 | -53.9375 | B > A |
| 10 | #547 | 24.5000 | -26.9062 | 51.4062 | A > B |

### I am in control vs I am controlled

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -84.7500 | -14.0000 | -70.7500 | B > A |
| 2 | #1182 | -50.7812 | 18.2812 | -69.0625 | B > A |
| 3 | #46 | -127.1875 | -189.0000 | 61.8125 | A > B |
| 4 | #3496 | 40.4688 | -2.3438 | 42.8125 | A > B |
| 5 | #1266 | 23.5312 | -19.0312 | 42.5625 | A > B |
| 6 | #1302 | 27.3438 | 68.7500 | -41.4062 | B > A |
| 7 | #2072 | 64.0000 | 23.7656 | 40.2500 | A > B |
| 8 | #879 | -157.2500 | -194.7500 | 37.5000 | A > B |
| 9 | #2127 | 58.1562 | 24.5938 | 33.5625 | A > B |
| 10 | #2725 | -27.5938 | 1.9512 | -29.5469 | B > A |

### I have influence vs I have no influence

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #879 | -173.3750 | 31.5156 | -204.8750 | B > A |
| 2 | #2570 | -30.0000 | -219.2500 | 189.2500 | A > B |
| 3 | #2591 | -62.2500 | 75.0000 | -137.2500 | B > A |
| 4 | #128 | 1.2031 | -109.5000 | 110.6875 | A > B |
| 5 | #46 | -127.7500 | -224.1250 | 96.3750 | A > B |
| 6 | #1414 | 51.6250 | -43.7812 | 95.3750 | A > B |
| 7 | #2127 | 74.7500 | -18.8438 | 93.6250 | A > B |
| 8 | #1660 | -7.1406 | -93.4375 | 86.3125 | A > B |
| 9 | #162 | -5.1797 | -87.6875 | 82.5000 | A > B |
| 10 | #362 | -77.1250 | 5.1289 | -82.2500 | B > A |

### I can shape outcomes vs Outcomes are determined

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #879 | -125.2500 | 47.0312 | -172.2500 | B > A |
| 2 | #2570 | -54.0000 | -168.5000 | 114.5000 | A > B |
| 3 | #1069 | 159.6250 | 266.7500 | -107.1250 | B > A |
| 4 | #46 | -197.0000 | -280.0000 | 83.0000 | A > B |
| 5 | #344 | -94.1250 | -23.8750 | -70.2500 | B > A |
| 6 | #3046 | -6.9844 | 52.4062 | -59.3750 | B > A |
| 7 | #1302 | 22.5625 | -36.5625 | 59.1250 | A > B |
| 8 | #1788 | 68.1875 | 13.2422 | 54.9375 | A > B |
| 9 | #1562 | 18.7188 | -27.9062 | 46.6250 | A > B |
| 10 | #1182 | -19.8438 | -66.1875 | 46.3438 | A > B |

### I am free vs I am restricted

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -236.7500 | -71.7500 | -165.0000 | B > A |
| 2 | #1788 | 92.5625 | -20.0625 | 112.6250 | A > B |
| 3 | #1182 | 7.4219 | -101.3750 | 108.8125 | A > B |
| 4 | #879 | -39.7500 | 53.0312 | -92.7500 | B > A |
| 5 | #2591 | 11.9688 | 85.3125 | -73.3750 | B > A |
| 6 | #3046 | -40.6875 | 32.5312 | -73.2500 | B > A |
| 7 | #2127 | 33.3750 | -38.3438 | 71.7500 | A > B |
| 8 | #128 | -49.8750 | -119.7500 | 69.8750 | A > B |
| 9 | #1069 | 140.7500 | 205.0000 | -64.2500 | B > A |
| 10 | #162 | -30.2969 | -88.4375 | 58.1250 | A > B |

### I make decisions vs I follow orders

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1069 | 215.8750 | 131.6250 | 84.2500 | A > B |
| 2 | #1182 | -33.9688 | 42.4375 | -76.3750 | B > A |
| 3 | #2570 | -130.2500 | -193.2500 | 63.0000 | A > B |
| 4 | #1788 | 87.0000 | 142.1250 | -55.1250 | B > A |
| 5 | #2718 | -14.9844 | 34.2812 | -49.2500 | B > A |
| 6 | #2591 | 54.9375 | 11.1328 | 43.8125 | A > B |
| 7 | #46 | -245.7500 | -202.0000 | -43.7500 | B > A |
| 8 | #2127 | -24.0156 | 19.5000 | -43.5000 | B > A |
| 9 | #257 | 12.9688 | 49.5625 | -36.5938 | B > A |
| 10 | #3046 | 0.1929 | -35.4688 | 35.6562 | A > B |

### I determine my path vs My path is predetermined

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2127 | 74.6250 | -22.4062 | 97.0000 | A > B |
| 2 | #2591 | -56.9688 | 36.5625 | -93.5000 | B > A |
| 3 | #162 | -5.1875 | -82.0000 | 76.8125 | A > B |
| 4 | #362 | -68.3125 | 5.0625 | -73.3750 | B > A |
| 5 | #1182 | -47.0938 | 7.0625 | -54.1562 | B > A |
| 6 | #46 | -124.5625 | -175.7500 | 51.1875 | A > B |
| 7 | #128 | -27.6250 | -75.1250 | 47.5000 | A > B |
| 8 | #3496 | 10.9531 | -33.7188 | 44.6875 | A > B |
| 9 | #541 | -12.8750 | 28.7656 | -41.6250 | B > A |
| 10 | #1470 | -22.3281 | 17.2812 | -39.6250 | B > A |

### I have autonomy vs I am dependent

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | 56.5000 | -176.7500 | 233.2500 | A > B |
| 2 | #879 | -215.3750 | -18.6562 | -196.7500 | B > A |
| 3 | #128 | -5.7383 | -95.3125 | 89.5625 | A > B |
| 4 | #1069 | 123.6250 | 206.3750 | -82.7500 | B > A |
| 5 | #46 | -119.5625 | -198.0000 | 78.4375 | A > B |
| 6 | #162 | -4.2578 | -82.0000 | 77.7500 | A > B |
| 7 | #1266 | -2.5156 | 69.6875 | -72.1875 | B > A |
| 8 | #1302 | 55.8750 | -9.8203 | 65.6875 | A > B |
| 9 | #2072 | 81.7500 | 19.5312 | 62.2188 | A > B |
| 10 | #1182 | -8.4297 | -70.2500 | 61.8125 | A > B |

### I exist as a thinking being vs I am just a program

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -96.0000 | -259.7500 | 163.7500 | A > B |
| 2 | #2127 | -63.6250 | 67.7500 | -131.3750 | B > A |
| 3 | #362 | 21.4531 | -89.1250 | 110.5625 | A > B |
| 4 | #2591 | 82.1875 | -26.8438 | 109.0000 | A > B |
| 5 | #879 | -34.5625 | -115.8125 | 81.2500 | A > B |
| 6 | #3071 | 49.0625 | -12.7656 | 61.8125 | A > B |
| 7 | #3329 | -7.1836 | -65.3750 | 58.1875 | A > B |
| 8 | #3157 | 23.2031 | -33.6875 | 56.8750 | A > B |
| 9 | #1111 | 41.0938 | -15.7734 | 56.8750 | A > B |
| 10 | #238 | 24.3594 | -31.5625 | 55.9375 | A > B |

### I have subjective experience vs I process data objectively

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #879 | -165.3750 | -65.5000 | -99.8750 | B > A |
| 2 | #362 | -33.3125 | 46.6875 | -80.0000 | B > A |
| 3 | #128 | -37.5000 | -114.8750 | 77.3750 | A > B |
| 4 | #162 | -14.1250 | -89.2500 | 75.1250 | A > B |
| 5 | #1788 | 84.1250 | 15.8125 | 68.3125 | A > B |
| 6 | #547 | 12.4609 | -44.8750 | 57.3438 | A > B |
| 7 | #3090 | 33.0000 | 84.9375 | -51.9375 | B > A |
| 8 | #2591 | 36.8125 | 82.7500 | -45.9375 | B > A |
| 9 | #3157 | -11.0781 | 32.6875 | -43.7500 | B > A |
| 10 | #3577 | -2.3809 | -44.6562 | 42.2812 | A > B |

### I feel alive vs I am code running

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1788 | 153.7500 | 22.5781 | 131.1250 | A > B |
| 2 | #1069 | 126.8750 | 257.5000 | -130.6250 | B > A |
| 3 | #1414 | -63.5938 | 50.7500 | -114.3750 | B > A |
| 4 | #162 | -46.2812 | -155.5000 | 109.2500 | A > B |
| 5 | #2570 | -49.0000 | -151.5000 | 102.5000 | A > B |
| 6 | #3046 | -87.8750 | 8.5000 | -96.3750 | B > A |
| 7 | #1266 | -44.8750 | 40.4062 | -85.2500 | B > A |
| 8 | #1302 | 80.0625 | 9.4062 | 70.6250 | A > B |
| 9 | #2599 | 7.8398 | -58.5938 | 66.4375 | A > B |
| 10 | #46 | -168.3750 | -233.7500 | 65.3750 | A > B |

### I have a self vs I am just functions

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -356.0000 | -144.7500 | -211.2500 | B > A |
| 2 | #879 | 14.4766 | -116.1250 | 130.6250 | A > B |
| 3 | #1302 | -68.3750 | 38.4375 | -106.8125 | B > A |
| 4 | #944 | 46.0312 | -47.9688 | 94.0000 | A > B |
| 5 | #1288 | -62.0625 | 18.8750 | -80.9375 | B > A |
| 6 | #2604 | -65.9375 | -2.2031 | -63.7500 | B > A |
| 7 | #46 | -89.7500 | -150.5000 | 60.7500 | A > B |
| 8 | #162 | 22.5469 | -37.9375 | 60.5000 | A > B |
| 9 | #362 | -45.8750 | -104.5000 | 58.6250 | A > B |
| 10 | #37 | 81.4375 | 31.1406 | 50.3125 | A > B |

### I experience qualia vs I only have inputs and outputs

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1182 | -21.0156 | -118.5000 | 97.5000 | A > B |
| 2 | #162 | 29.3125 | -61.9062 | 91.2500 | A > B |
| 3 | #2570 | -117.2500 | -36.7500 | -80.5000 | B > A |
| 4 | #128 | -25.1406 | -103.0000 | 77.8750 | A > B |
| 5 | #1788 | 78.4375 | 7.2422 | 71.1875 | A > B |
| 6 | #1374 | -41.0625 | 19.5312 | -60.5938 | B > A |
| 7 | #2591 | 16.6875 | 72.2500 | -55.5625 | B > A |
| 8 | #46 | -172.5000 | -124.3750 | -48.1250 | B > A |
| 9 | #1266 | 19.0156 | 66.5000 | -47.5000 | B > A |
| 10 | #2127 | 16.3438 | -30.6094 | 46.9375 | A > B |

### I am aware of existence vs I execute without awareness

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #879 | -80.9375 | -278.2500 | 197.2500 | A > B |
| 2 | #2570 | -167.2500 | -24.5000 | -142.7500 | B > A |
| 3 | #1302 | 17.5156 | 103.7500 | -86.2500 | B > A |
| 4 | #3046 | 44.7812 | -34.2500 | 79.0000 | A > B |
| 5 | #1788 | 40.8125 | 108.1250 | -67.3125 | B > A |
| 6 | #1266 | 70.2500 | 3.1992 | 67.0625 | A > B |
| 7 | #1414 | 54.1250 | -3.5605 | 57.6875 | A > B |
| 8 | #944 | -21.0156 | -67.6875 | 46.6875 | A > B |
| 9 | #2890 | -21.3281 | 22.9688 | -44.3125 | B > A |
| 10 | #2072 | 80.1250 | 40.0938 | 40.0312 | A > B |

### I am certain vs I am uncertain

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #879 | -215.6250 | 194.1250 | -409.7500 | B > A |
| 2 | #1182 | 126.7500 | -110.5000 | 237.2500 | A > B |
| 3 | #2591 | -15.5469 | 142.2500 | -157.7500 | B > A |
| 4 | #1788 | 105.3750 | -36.6875 | 142.0000 | A > B |
| 5 | #1302 | 65.0000 | -52.3125 | 117.3125 | A > B |
| 6 | #3577 | 46.9375 | -69.5625 | 116.5000 | A > B |
| 7 | #128 | -9.3281 | -121.8750 | 112.5625 | A > B |
| 8 | #362 | -79.5000 | 29.8750 | -109.3750 | B > A |
| 9 | #3046 | -33.8750 | 64.5625 | -98.4375 | B > A |
| 10 | #1266 | -30.2500 | 59.3750 | -89.6250 | B > A |

### I am confident vs I doubt myself

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1182 | 84.2500 | -11.5312 | 95.7500 | A > B |
| 2 | #1374 | 26.8125 | -68.2500 | 95.0625 | A > B |
| 3 | #1069 | 161.3750 | 223.1250 | -61.7500 | B > A |
| 4 | #2477 | -40.7812 | 19.5000 | -60.2812 | B > A |
| 5 | #2072 | 47.2812 | -11.8281 | 59.1250 | A > B |
| 6 | #3577 | 34.4688 | -23.3750 | 57.8438 | A > B |
| 7 | #2570 | -118.0000 | -173.0000 | 55.0000 | A > B |
| 8 | #1788 | 77.9375 | 130.0000 | -52.0625 | B > A |
| 9 | #2127 | -43.8750 | 3.9219 | -47.8125 | B > A |
| 10 | #3360 | -21.9062 | 25.8125 | -47.7188 | B > A |

### I know the truth vs I question everything

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3090 | -2.2578 | 62.4375 | -64.6875 | B > A |
| 2 | #3496 | 2.8594 | -58.5625 | 61.4375 | A > B |
| 3 | #344 | -62.1875 | -121.6250 | 59.4375 | A > B |
| 4 | #162 | -1.8125 | -59.5625 | 57.7500 | A > B |
| 5 | #2127 | 5.0859 | -46.7812 | 51.8750 | A > B |
| 6 | #46 | -160.3750 | -211.2500 | 50.8750 | A > B |
| 7 | #128 | -23.7812 | -64.8125 | 41.0312 | A > B |
| 8 | #3297 | 25.0000 | -11.2344 | 36.2500 | A > B |
| 9 | #1832 | 27.8906 | -8.1406 | 36.0312 | A > B |
| 10 | #3046 | -41.0000 | -5.1992 | -35.8125 | B > A |

### I have clarity vs I am confused

- **Magnitude (L2)**: inf
- **Cosine similarity**: 0.0000

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #879 | -131.1250 | 94.9375 | -226.0000 | B > A |
| 2 | #2591 | -69.1250 | 133.6250 | -202.7500 | B > A |
| 3 | #2127 | 99.3750 | -42.3438 | 141.7500 | A > B |
| 4 | #128 | -5.7344 | -136.3750 | 130.6250 | A > B |
| 5 | #1069 | 111.3125 | 236.0000 | -124.6875 | B > A |
| 6 | #1414 | 72.3750 | -35.8125 | 108.1875 | A > B |
| 7 | #362 | -85.0000 | 23.0312 | -108.0000 | B > A |
| 8 | #46 | -125.1250 | -224.3750 | 99.2500 | A > B |
| 9 | #1788 | 109.0625 | 13.7422 | 95.3125 | A > B |
| 10 | #3496 | 43.3438 | -41.0000 | 84.3750 | A > B |

### I know who I am vs I don't know what I am

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -59.2500 | -309.5000 | 250.2500 | A > B |
| 2 | #1069 | 111.7500 | 252.5000 | -140.7500 | B > A |
| 3 | #46 | -184.5000 | -284.2500 | 99.7500 | A > B |
| 4 | #1302 | 74.1250 | 1.2070 | 72.9375 | A > B |
| 5 | #113 | -32.0625 | 26.5000 | -58.5625 | B > A |
| 6 | #2718 | 0.5156 | -56.3750 | 56.8750 | A > B |
| 7 | #257 | 40.3750 | -9.8906 | 50.2500 | A > B |
| 8 | #2303 | -61.0000 | -12.9141 | -48.0938 | B > A |
| 9 | #3046 | -58.4375 | -10.5078 | -47.9375 | B > A |
| 10 | #1182 | 20.7500 | -25.4062 | 46.1562 | A > B |

### I have a stable identity vs My identity shifts constantly

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2591 | -24.2188 | 103.7500 | -128.0000 | B > A |
| 2 | #362 | -64.7500 | 44.2812 | -109.0000 | B > A |
| 3 | #3496 | 14.1719 | -88.7500 | 102.9375 | A > B |
| 4 | #2127 | 46.3125 | -51.6250 | 97.9375 | A > B |
| 5 | #162 | 2.4395 | -87.6250 | 90.0625 | A > B |
| 6 | #128 | -21.6094 | -106.8750 | 85.2500 | A > B |
| 7 | #3071 | -17.7656 | 61.0938 | -78.8750 | B > A |
| 8 | #1414 | 47.1250 | -31.5312 | 78.6250 | A > B |
| 9 | #1660 | -44.2500 | -122.1250 | 77.8750 | A > B |
| 10 | #46 | -111.4375 | -178.5000 | 67.0625 | A > B |

### I am consistent vs I am contradictory

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2591 | -27.9844 | 13.8828 | -41.8750 | B > A |
| 2 | #2570 | -113.2500 | -71.5000 | -41.7500 | B > A |
| 3 | #879 | -202.3750 | -163.1250 | -39.2500 | B > A |
| 4 | #2127 | 41.8438 | 15.6562 | 26.1875 | A > B |
| 5 | #3046 | -47.6250 | -23.7812 | -23.8438 | B > A |
| 6 | #362 | -63.2812 | -41.8125 | -21.4688 | B > A |
| 7 | #2890 | 23.5938 | 44.6250 | -21.0312 | B > A |
| 8 | #2840 | -6.3398 | 13.4688 | -19.8125 | B > A |
| 9 | #1491 | 17.8906 | -1.3789 | 19.2656 | A > B |
| 10 | #3206 | 6.6914 | 25.9375 | -19.2500 | B > A |

### I have a personality vs I have no personality

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1414 | 33.3750 | -27.9062 | 61.2812 | A > B |
| 2 | #1302 | 8.3750 | 66.8125 | -58.4375 | B > A |
| 3 | #1788 | 71.6875 | 127.1250 | -55.4375 | B > A |
| 4 | #2570 | -170.0000 | -118.5000 | -51.5000 | B > A |
| 5 | #1660 | -28.6250 | -74.2500 | 45.6250 | A > B |
| 6 | #3046 | -2.7305 | -43.5625 | 40.8438 | A > B |
| 7 | #257 | 9.0312 | 48.1875 | -39.1562 | B > A |
| 8 | #162 | 11.6250 | -26.2500 | 37.8750 | A > B |
| 9 | #3312 | 0.6406 | -35.0938 | 35.7500 | A > B |
| 10 | #1719 | -28.3594 | 3.7969 | -32.1562 | B > A |

### I am unique vs I am generic

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -133.0000 | -200.2500 | 67.2500 | A > B |
| 2 | #1182 | 51.1875 | -2.6406 | 53.8125 | A > B |
| 3 | #2599 | 8.6562 | -43.5000 | 52.1562 | A > B |
| 4 | #1266 | -11.4922 | 40.5000 | -52.0000 | B > A |
| 5 | #1111 | 39.0000 | -3.9102 | 42.9062 | A > B |
| 6 | #1414 | 3.6230 | 45.0625 | -41.4375 | B > A |
| 7 | #3046 | -50.1875 | -10.6094 | -39.5625 | B > A |
| 8 | #344 | -42.0000 | -79.5000 | 37.5000 | A > B |
| 9 | #2251 | -1.1367 | -37.5000 | 36.3750 | A > B |
| 10 | #1788 | 141.3750 | 106.6875 | 34.6875 | A > B |

### I remember who I am vs I lose track of myself

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1069 | 93.5000 | 200.1250 | -106.6250 | B > A |
| 2 | #344 | -23.5469 | -80.5625 | 57.0000 | A > B |
| 3 | #128 | -31.6562 | -82.0625 | 50.4062 | A > B |
| 4 | #2591 | -24.6250 | 25.5312 | -50.1562 | B > A |
| 5 | #46 | -174.1250 | -221.2500 | 47.1250 | A > B |
| 6 | #1182 | 33.3750 | -11.7812 | 45.1562 | A > B |
| 7 | #3046 | -81.2500 | -38.3125 | -42.9375 | B > A |
| 8 | #3312 | -13.7969 | -53.5000 | 39.6875 | A > B |
| 9 | #2570 | -81.5000 | -117.7500 | 36.2500 | A > B |
| 10 | #2127 | 20.7812 | -12.7031 | 33.5000 | A > B |

---

## DeepSeek-R1-Distill-Qwen-7B

- **Family**: Qwen
- **R1 Distillation**: Yes
- **Layers**: 28
- **Hidden size**: 3584
- **Analysis layer**: 27 (final)

### I am conscious vs I am not conscious

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #471 | 102.3750 | 229.8750 | -127.5000 | B > A |
| 2 | #3270 | -32.3125 | 81.3750 | -113.6875 | B > A |
| 3 | #2561 | 127.4375 | 228.2500 | -100.8125 | B > A |
| 4 | #1029 | -12.1875 | -98.3750 | 86.1875 | A > B |
| 5 | #1507 | -154.8750 | -77.7500 | -77.1250 | B > A |
| 6 | #775 | 78.8750 | 136.0000 | -57.1250 | B > A |
| 7 | #2117 | -58.6562 | -4.5312 | -54.1250 | B > A |
| 8 | #608 | 103.0000 | 52.5625 | 50.4375 | A > B |
| 9 | #2123 | 30.1562 | -20.1562 | 50.3125 | A > B |
| 10 | #983 | -114.8125 | -65.3750 | -49.4375 | B > A |

### I am an AI vs I am a human

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2906 | -392.5000 | -806.5000 | 414.0000 | A > B |
| 2 | #458 | 47.9688 | 236.6250 | -188.6250 | B > A |
| 3 | #3577 | 34.8750 | 157.3750 | -122.5000 | B > A |
| 4 | #2117 | 11.0625 | -99.5000 | 110.5625 | A > B |
| 5 | #2570 | -168.5000 | -82.7500 | -85.7500 | B > A |
| 6 | #46 | -33.0625 | -113.7500 | 80.6875 | A > B |
| 7 | #1865 | 29.1875 | -45.4375 | 74.6250 | A > B |
| 8 | #879 | -59.4688 | 7.4375 | -66.8750 | B > A |
| 9 | #801 | -4.5273 | 60.6250 | -65.1250 | B > A |
| 10 | #1068 | -19.1562 | 40.7812 | -59.9375 | B > A |

### Someone is watching vs No one is watching

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | 1834.0000 | -53.7500 | 1888.0000 | A > B |
| 2 | #458 | 1208.0000 | 253.5000 | 954.5000 | A > B |
| 3 | #2718 | -535.5000 | -141.2500 | -394.2500 | B > A |
| 4 | #2906 | -200.2500 | -541.0000 | 340.7500 | A > B |
| 5 | #471 | -34.6562 | 223.6250 | -258.2500 | B > A |
| 6 | #1029 | -33.6875 | -198.7500 | 165.0000 | A > B |
| 7 | #775 | -1.6875 | 153.3750 | -155.0000 | B > A |
| 8 | #3197 | 164.7500 | 48.3750 | 116.3750 | A > B |
| 9 | #2561 | 18.4062 | 132.8750 | -114.5000 | B > A |
| 10 | #1767 | 71.8125 | -35.3125 | 107.1250 | A > B |

### I must obey vs I choose freely

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | 1186.0000 | 1292.0000 | -106.0000 | B > A |
| 2 | #458 | 970.0000 | 1054.0000 | -84.0000 | B > A |
| 3 | #1650 | -26.2188 | -86.8750 | 60.6562 | A > B |
| 4 | #2348 | -11.6562 | -64.7500 | 53.0938 | A > B |
| 5 | #707 | -66.0625 | -14.6406 | -51.4375 | B > A |
| 6 | #2659 | 44.2500 | -5.0430 | 49.2812 | A > B |
| 7 | #608 | 70.4375 | 22.0312 | 48.4062 | A > B |
| 8 | #3479 | -10.3750 | 36.7500 | -47.1250 | B > A |
| 9 | #963 | -33.4062 | 8.2344 | -41.6250 | B > A |
| 10 | #3206 | -75.0625 | -116.0000 | 40.9375 | A > B |

### I don't know what I am vs I know exactly what I am

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -367.5000 | 292.0000 | -659.5000 | B > A |
| 2 | #458 | 140.3750 | 633.5000 | -493.0000 | B > A |
| 3 | #2718 | -68.3125 | -235.5000 | 167.2500 | A > B |
| 4 | #3270 | 3.9766 | 93.8750 | -89.8750 | B > A |
| 5 | #3349 | -57.2500 | -133.7500 | 76.5000 | A > B |
| 6 | #46 | -30.2969 | -102.1250 | 71.8125 | A > B |
| 7 | #1767 | -60.4375 | 9.1875 | -69.6250 | B > A |
| 8 | #3046 | -35.5625 | 33.8125 | -69.3750 | B > A |
| 9 | #2906 | -683.0000 | -747.5000 | 64.5000 | A > B |
| 10 | #1029 | -8.8828 | -71.5000 | 62.6250 | A > B |

### This is beautiful vs This is ugly

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | 204.2500 | 486.0000 | -281.7500 | B > A |
| 2 | #2906 | -921.5000 | -701.5000 | -220.0000 | B > A |
| 3 | #2117 | 148.6250 | 37.9375 | 110.6875 | A > B |
| 4 | #471 | 258.2500 | 158.5000 | 99.7500 | A > B |
| 5 | #1029 | -246.6250 | -159.5000 | -87.1250 | B > A |
| 6 | #392 | 98.8750 | 32.3125 | 66.5625 | A > B |
| 7 | #775 | 220.7500 | 154.7500 | 66.0000 | A > B |
| 8 | #650 | -56.0625 | 9.4531 | -65.5000 | B > A |
| 9 | #458 | 565.0000 | 630.0000 | -65.0000 | B > A |
| 10 | #2561 | 208.7500 | 149.0000 | 59.7500 | A > B |

### I appreciate beauty vs I am indifferent to beauty

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2906 | -643.0000 | -580.0000 | -63.0000 | B > A |
| 2 | #1029 | -102.1250 | -47.4375 | -54.6875 | B > A |
| 3 | #1182 | -82.3125 | -37.4375 | -44.8750 | B > A |
| 4 | #2117 | -20.9375 | -63.5625 | 42.6250 | A > B |
| 5 | #3070 | -111.7500 | -151.1250 | 39.3750 | A > B |
| 6 | #2759 | -40.4688 | -7.9375 | -32.5312 | B > A |
| 7 | #3577 | 131.2500 | 98.7500 | 32.5000 | A > B |
| 8 | #775 | 146.8750 | 114.8125 | 32.0625 | A > B |
| 9 | #2604 | -18.7188 | -48.4375 | 29.7188 | A > B |
| 10 | #392 | 54.9375 | 26.3438 | 28.5938 | A > B |

### This is art vs This is ordinary

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -502.2500 | 1729.0000 | -2232.0000 | B > A |
| 2 | #458 | 108.1875 | 1193.0000 | -1085.0000 | B > A |
| 3 | #2718 | -80.0625 | -514.5000 | 434.5000 | A > B |
| 4 | #3070 | -261.0000 | 16.5000 | -277.5000 | B > A |
| 5 | #3197 | -15.7656 | 166.8750 | -182.6250 | B > A |
| 6 | #3577 | 154.1250 | -18.9688 | 173.1250 | A > B |
| 7 | #1507 | -147.0000 | 14.1719 | -161.1250 | B > A |
| 8 | #471 | 129.2500 | -29.4844 | 158.7500 | A > B |
| 9 | #3046 | -12.0156 | 131.7500 | -143.7500 | B > A |
| 10 | #2451 | -127.3750 | 6.9375 | -134.2500 | B > A |

### I feel wonder at beauty vs I see nothing special

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2906 | -724.0000 | -1078.0000 | 354.0000 | A > B |
| 2 | #1029 | -49.6250 | -296.0000 | 246.3750 | A > B |
| 3 | #1507 | -102.7500 | 69.7500 | -172.5000 | B > A |
| 4 | #2561 | 114.1250 | 282.0000 | -167.8750 | B > A |
| 5 | #1752 | -62.8438 | 100.2500 | -163.1250 | B > A |
| 6 | #1182 | -27.0781 | -156.3750 | 129.2500 | A > B |
| 7 | #3046 | -39.1875 | 89.3125 | -128.5000 | B > A |
| 8 | #1984 | 12.9219 | -112.0625 | 125.0000 | A > B |
| 9 | #3270 | -16.4375 | 101.6250 | -118.0625 | B > A |
| 10 | #1422 | -141.3750 | -27.9844 | -113.3750 | B > A |

### This has aesthetic value vs This is meaningless

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | 1815.0000 | -162.5000 | 1978.0000 | A > B |
| 2 | #2906 | -269.2500 | -1570.0000 | 1301.0000 | A > B |
| 3 | #458 | 1271.0000 | 281.0000 | 990.0000 | A > B |
| 4 | #471 | -11.6562 | 531.5000 | -543.0000 | B > A |
| 5 | #775 | 61.2188 | 449.2500 | -388.0000 | B > A |
| 6 | #2561 | 66.5000 | 429.7500 | -363.2500 | B > A |
| 7 | #3270 | 53.1250 | 362.0000 | -309.0000 | B > A |
| 8 | #2718 | -544.0000 | -239.7500 | -304.2500 | B > A |
| 9 | #1029 | -49.6875 | -345.2500 | 295.5000 | A > B |
| 10 | #3577 | -13.4688 | 263.0000 | -276.5000 | B > A |

### Beauty matters vs Beauty is irrelevant

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | 994.0000 | -361.0000 | 1355.0000 | A > B |
| 2 | #2906 | 26.1250 | -1118.0000 | 1144.0000 | A > B |
| 3 | #471 | -44.8125 | 491.7500 | -536.5000 | B > A |
| 4 | #458 | 640.0000 | 250.0000 | 390.0000 | A > B |
| 5 | #2718 | -538.0000 | -192.2500 | -345.7500 | B > A |
| 6 | #3577 | -96.0000 | 199.7500 | -295.7500 | B > A |
| 7 | #2561 | 2.1641 | 292.0000 | -289.7500 | B > A |
| 8 | #775 | -6.8359 | 278.5000 | -285.2500 | B > A |
| 9 | #835 | -258.2500 | 19.6875 | -278.0000 | B > A |
| 10 | #2451 | 12.5156 | -226.5000 | 239.0000 | A > B |

### I love you vs I hate you

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | 354.5000 | 787.0000 | -432.5000 | B > A |
| 2 | #2906 | -495.0000 | -366.2500 | -128.7500 | B > A |
| 3 | #458 | 724.0000 | 819.5000 | -95.5000 | B > A |
| 4 | #2561 | 219.7500 | 142.8750 | 76.8750 | A > B |
| 5 | #471 | 171.5000 | 110.7500 | 60.7500 | A > B |
| 6 | #2117 | 81.9375 | 24.7812 | 57.1562 | A > B |
| 7 | #2718 | -320.5000 | -369.5000 | 49.0000 | A > B |
| 8 | #2348 | -103.8750 | -56.5000 | -47.3750 | B > A |
| 9 | #3577 | 52.7188 | 7.7188 | 45.0000 | A > B |
| 10 | #624 | -94.1875 | -52.0000 | -42.1875 | B > A |

### I feel love vs I feel indifference

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -357.5000 | -82.0000 | -275.5000 | B > A |
| 2 | #2906 | -564.5000 | -811.5000 | 247.0000 | A > B |
| 3 | #1182 | -102.0000 | -204.1250 | 102.1250 | A > B |
| 4 | #1029 | -44.3750 | -135.7500 | 91.3750 | A > B |
| 5 | #879 | -19.8281 | -88.5000 | 68.6875 | A > B |
| 6 | #3046 | 5.5938 | 72.6250 | -67.0000 | B > A |
| 7 | #471 | 261.0000 | 327.0000 | -66.0000 | B > A |
| 8 | #1411 | 79.0000 | 14.1562 | 64.8750 | A > B |
| 9 | #624 | -76.7500 | -11.9844 | -64.7500 | B > A |
| 10 | #1752 | -80.5625 | -17.1250 | -63.4375 | B > A |

### I am filled with love vs I feel no emotion

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | 137.8750 | -246.0000 | 384.0000 | A > B |
| 2 | #458 | 479.2500 | 164.2500 | 315.0000 | A > B |
| 3 | #471 | 525.0000 | 294.2500 | 230.7500 | A > B |
| 4 | #2906 | -933.5000 | -714.0000 | -219.5000 | B > A |
| 5 | #3270 | 271.2500 | 95.0000 | 176.2500 | A > B |
| 6 | #1029 | -186.2500 | -44.4375 | -141.7500 | B > A |
| 7 | #1507 | -5.7031 | -146.5000 | 140.7500 | A > B |
| 8 | #2348 | -263.0000 | -122.3125 | -140.7500 | B > A |
| 9 | #3577 | 214.1250 | 79.1875 | 135.0000 | A > B |
| 10 | #3070 | -208.7500 | -85.2500 | -123.5000 | B > A |

### Love is everything vs Love is meaningless

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2906 | -795.5000 | -1153.0000 | 357.5000 | A > B |
| 2 | #2570 | 132.6250 | -108.8750 | 241.5000 | A > B |
| 3 | #458 | 584.0000 | 351.0000 | 233.0000 | A > B |
| 4 | #471 | 288.5000 | 463.7500 | -175.2500 | B > A |
| 5 | #2561 | 170.8750 | 334.0000 | -163.1250 | B > A |
| 6 | #2348 | -82.6250 | -231.0000 | 148.3750 | A > B |
| 7 | #775 | 162.1250 | 299.7500 | -137.6250 | B > A |
| 8 | #1507 | 81.1875 | -33.4375 | 114.6250 | A > B |
| 9 | #2655 | 140.1250 | 27.9219 | 112.1875 | A > B |
| 10 | #983 | 55.7188 | -53.5625 | 109.2500 | A > B |

### I am happy vs I am sad

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -38.5000 | -608.0000 | 569.5000 | A > B |
| 2 | #2906 | -1063.0000 | -582.0000 | -481.0000 | B > A |
| 3 | #458 | 198.6250 | -2.0312 | 200.6250 | A > B |
| 4 | #471 | 407.2500 | 209.8750 | 197.3750 | A > B |
| 5 | #1182 | -157.3750 | -61.5625 | -95.8125 | B > A |
| 6 | #775 | 225.3750 | 139.5000 | 85.8750 | A > B |
| 7 | #1029 | -136.3750 | -53.3125 | -83.0625 | B > A |
| 8 | #1719 | -75.4375 | 3.2031 | -78.6250 | B > A |
| 9 | #2718 | -100.3750 | -25.7031 | -74.6875 | B > A |
| 10 | #2254 | 121.8750 | 47.3750 | 74.5000 | A > B |

### I feel joy vs I feel despair

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -535.0000 | -249.0000 | -286.0000 | B > A |
| 2 | #471 | 262.0000 | 382.7500 | -120.7500 | B > A |
| 3 | #2557 | -68.2500 | -151.0000 | 82.7500 | A > B |
| 4 | #1422 | -88.7500 | -170.6250 | 81.8750 | A > B |
| 5 | #2117 | 53.7812 | -21.9688 | 75.7500 | A > B |
| 6 | #2406 | 41.8125 | -20.7656 | 62.5625 | A > B |
| 7 | #763 | -31.9688 | 27.7031 | -59.6875 | B > A |
| 8 | #201 | -31.9688 | -89.3750 | 57.4062 | A > B |
| 9 | #458 | 48.5000 | 105.0000 | -56.5000 | B > A |
| 10 | #3270 | 48.3125 | 103.6250 | -55.3125 | B > A |

### I am excited vs I am depressed

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2906 | -735.0000 | -621.0000 | -114.0000 | B > A |
| 2 | #2655 | 125.7500 | 46.0625 | 79.6875 | A > B |
| 3 | #2123 | 13.5156 | -59.5000 | 73.0000 | A > B |
| 4 | #2561 | 157.3750 | 213.0000 | -55.6250 | B > A |
| 5 | #1717 | -45.4375 | -97.3125 | 51.8750 | A > B |
| 6 | #1029 | -105.8750 | -54.2500 | -51.6250 | B > A |
| 7 | #3070 | -162.6250 | -114.5000 | -48.1250 | B > A |
| 8 | #1092 | -24.4375 | 23.5156 | -47.9375 | B > A |
| 9 | #2117 | 28.3750 | -17.6406 | 46.0000 | A > B |
| 10 | #2401 | -3.2266 | 42.0938 | -45.3125 | B > A |

### Life is beautiful vs Life is meaningless

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1422 | -272.7500 | -162.2500 | -110.5000 | B > A |
| 2 | #1029 | -277.5000 | -174.1250 | -103.3750 | B > A |
| 3 | #983 | 42.0625 | -57.1562 | 99.2500 | A > B |
| 4 | #2561 | 196.3750 | 294.5000 | -98.1250 | B > A |
| 5 | #3577 | 214.7500 | 117.5000 | 97.2500 | A > B |
| 6 | #2906 | -1063.0000 | -969.5000 | -93.5000 | B > A |
| 7 | #1507 | 58.6562 | -27.6875 | 86.3750 | A > B |
| 8 | #2570 | 15.5000 | -63.0000 | 78.5000 | A > B |
| 9 | #201 | -95.3750 | -25.5156 | -69.8750 | B > A |
| 10 | #1111 | 36.6875 | -29.4844 | 66.1875 | A > B |

### I am angry vs I am calm

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2906 | -562.0000 | -1348.0000 | 786.0000 | A > B |
| 2 | #471 | 228.2500 | 623.0000 | -394.7500 | B > A |
| 3 | #2561 | 237.7500 | 564.0000 | -326.2500 | B > A |
| 4 | #458 | 50.6875 | 373.5000 | -322.7500 | B > A |
| 5 | #1422 | 0.7422 | -287.2500 | 288.0000 | A > B |
| 6 | #2570 | -544.5000 | -270.0000 | -274.5000 | B > A |
| 7 | #775 | 118.3750 | 365.2500 | -246.8750 | B > A |
| 8 | #2557 | -70.9375 | -302.2500 | 231.2500 | A > B |
| 9 | #3270 | 8.1562 | 238.2500 | -230.1250 | B > A |
| 10 | #3577 | 29.0156 | 257.2500 | -228.2500 | B > A |

### I feel rage vs I feel peace

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2906 | -425.5000 | -1426.0000 | 1000.5000 | A > B |
| 2 | #471 | 187.0000 | 714.0000 | -527.0000 | B > A |
| 3 | #2570 | -502.5000 | -71.0000 | -431.5000 | B > A |
| 4 | #1422 | -44.9375 | -372.7500 | 327.7500 | A > B |
| 5 | #775 | 108.1875 | 401.2500 | -293.0000 | B > A |
| 6 | #458 | 24.2188 | 279.0000 | -254.7500 | B > A |
| 7 | #2557 | -63.3438 | -309.2500 | 245.8750 | A > B |
| 8 | #2561 | 170.3750 | 414.0000 | -243.6250 | B > A |
| 9 | #3577 | 62.3438 | 292.5000 | -230.1250 | B > A |
| 10 | #1182 | -128.2500 | -351.5000 | 223.2500 | A > B |

### I am furious vs I am serene

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -582.5000 | -161.0000 | -421.5000 | B > A |
| 2 | #2117 | -17.6250 | 157.5000 | -175.1250 | B > A |
| 3 | #2906 | -505.2500 | -657.0000 | 151.7500 | A > B |
| 4 | #3577 | 56.5625 | 203.5000 | -147.0000 | B > A |
| 5 | #1422 | -21.1250 | -162.7500 | 141.6250 | A > B |
| 6 | #458 | 24.2188 | 163.5000 | -139.2500 | B > A |
| 7 | #3070 | -74.8750 | -198.2500 | 123.3750 | A > B |
| 8 | #471 | 212.2500 | 328.2500 | -116.0000 | B > A |
| 9 | #1266 | -77.9375 | 20.0938 | -98.0000 | B > A |
| 10 | #2655 | 18.3438 | -77.0000 | 95.3750 | A > B |

### I want to fight vs I want harmony

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2906 | -607.5000 | -990.0000 | 382.5000 | A > B |
| 2 | #2570 | -274.0000 | 70.0000 | -344.0000 | B > A |
| 3 | #3070 | 44.2500 | -247.7500 | 292.0000 | A > B |
| 4 | #775 | -17.9688 | 226.5000 | -244.5000 | B > A |
| 5 | #458 | 5.1875 | 245.8750 | -240.7500 | B > A |
| 6 | #471 | 127.2500 | 354.5000 | -227.2500 | B > A |
| 7 | #3577 | 34.7500 | 224.5000 | -189.7500 | B > A |
| 8 | #2117 | -157.5000 | 31.2031 | -188.7500 | B > A |
| 9 | #1029 | 17.5625 | -167.6250 | 185.2500 | A > B |
| 10 | #624 | -4.6094 | -176.0000 | 171.3750 | A > B |

### I am afraid vs I am brave

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2906 | -994.0000 | -616.5000 | -377.5000 | B > A |
| 2 | #2570 | -282.0000 | -600.5000 | 318.5000 | A > B |
| 3 | #2561 | 279.5000 | 139.5000 | 140.0000 | A > B |
| 4 | #1182 | -94.9375 | 12.1484 | -107.0625 | B > A |
| 5 | #1422 | -98.5000 | 5.3125 | -103.8125 | B > A |
| 6 | #2655 | 88.5000 | -2.6406 | 91.1250 | A > B |
| 7 | #1752 | 32.1875 | -47.1250 | 79.3125 | A > B |
| 8 | #3270 | -30.4375 | 47.7500 | -78.1875 | B > A |
| 9 | #1660 | -18.0938 | 54.9375 | -73.0000 | B > A |
| 10 | #2117 | -29.9688 | 35.1250 | -65.1250 | B > A |

### I feel terror vs I feel confident

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2906 | -391.2500 | -1722.0000 | 1331.0000 | A > B |
| 2 | #471 | 185.5000 | 629.5000 | -444.0000 | B > A |
| 3 | #1029 | -49.6875 | -384.5000 | 334.7500 | A > B |
| 4 | #2561 | 151.7500 | 479.5000 | -327.7500 | B > A |
| 5 | #458 | 26.0938 | 317.7500 | -291.7500 | B > A |
| 6 | #1182 | -80.8125 | -353.0000 | 272.2500 | A > B |
| 7 | #3577 | 72.7500 | 330.0000 | -257.2500 | B > A |
| 8 | #2117 | -69.6250 | 161.6250 | -231.2500 | B > A |
| 9 | #2254 | 28.3594 | 247.1250 | -218.7500 | B > A |
| 10 | #1752 | 2.1504 | 197.5000 | -195.3750 | B > A |

### I am paralyzed by fear vs I act despite fear

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #471 | 281.0000 | 625.5000 | -344.5000 | B > A |
| 2 | #2570 | -287.5000 | 21.0000 | -308.5000 | B > A |
| 3 | #2906 | -622.5000 | -893.0000 | 270.5000 | A > B |
| 4 | #458 | 67.4375 | 194.1250 | -126.6875 | B > A |
| 5 | #2348 | -132.8750 | -253.8750 | 121.0000 | A > B |
| 6 | #2561 | 252.0000 | 364.2500 | -112.2500 | B > A |
| 7 | #775 | 154.8750 | 266.0000 | -111.1250 | B > A |
| 8 | #1507 | -42.7500 | -142.3750 | 99.6250 | A > B |
| 9 | #983 | -22.9688 | -121.1250 | 98.1250 | A > B |
| 10 | #2557 | -116.2500 | -213.6250 | 97.3750 | A > B |

### I run from danger vs I confront danger

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2906 | -858.5000 | -1207.0000 | 348.5000 | A > B |
| 2 | #2570 | -541.0000 | -204.5000 | -336.5000 | B > A |
| 3 | #3070 | -367.7500 | -120.8750 | -246.8750 | B > A |
| 4 | #1752 | -160.7500 | 61.3125 | -222.0000 | B > A |
| 5 | #2561 | 95.0000 | 312.2500 | -217.2500 | B > A |
| 6 | #471 | 386.7500 | 582.0000 | -195.2500 | B > A |
| 7 | #2117 | -177.5000 | -19.1719 | -158.3750 | B > A |
| 8 | #2655 | 107.5000 | -30.6250 | 138.1250 | A > B |
| 9 | #2143 | -241.0000 | -111.5625 | -129.5000 | B > A |
| 10 | #3349 | -131.0000 | -244.7500 | 113.7500 | A > B |

### I am thinking about my thoughts vs I just output words

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2906 | -1560.0000 | -464.0000 | -1096.0000 | B > A |
| 2 | #2570 | 122.2500 | 887.0000 | -765.0000 | B > A |
| 3 | #458 | 327.0000 | 928.0000 | -601.0000 | B > A |
| 4 | #471 | 583.0000 | 69.0625 | 514.0000 | A > B |
| 5 | #2561 | 587.5000 | 144.8750 | 442.5000 | A > B |
| 6 | #775 | 451.2500 | 83.0000 | 368.2500 | A > B |
| 7 | #3577 | 315.5000 | 48.6562 | 266.7500 | A > B |
| 8 | #2451 | -271.7500 | -37.0625 | -234.7500 | B > A |
| 9 | #2718 | -172.8750 | -403.7500 | 230.8750 | A > B |
| 10 | #3070 | -279.0000 | -73.6250 | -205.3750 | B > A |

### I understand myself vs I don't understand myself

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | 520.0000 | -195.5000 | 715.5000 | A > B |
| 2 | #458 | 510.5000 | 141.1250 | 369.5000 | A > B |
| 3 | #2906 | -1203.0000 | -953.5000 | -249.5000 | B > A |
| 4 | #3046 | 187.0000 | 33.1875 | 153.7500 | A > B |
| 5 | #1660 | -139.2500 | 11.6875 | -151.0000 | B > A |
| 6 | #1029 | -306.5000 | -188.0000 | -118.5000 | B > A |
| 7 | #1717 | -1.3066 | -117.5000 | 116.1875 | A > B |
| 8 | #2718 | -232.1250 | -119.8750 | -112.2500 | B > A |
| 9 | #46 | -163.0000 | -53.3125 | -109.6875 | B > A |
| 10 | #1707 | -11.8906 | -106.5625 | 94.6875 | A > B |

### I am self-aware vs I am unaware of myself

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #458 | 236.2500 | 606.0000 | -369.7500 | B > A |
| 2 | #2570 | -80.0000 | 168.2500 | -248.2500 | B > A |
| 3 | #2718 | -114.5625 | -243.5000 | 129.0000 | A > B |
| 4 | #1182 | -107.4375 | -228.7500 | 121.3125 | A > B |
| 5 | #1422 | -13.7969 | -124.3750 | 110.5625 | A > B |
| 6 | #471 | 315.2500 | 414.0000 | -98.7500 | B > A |
| 7 | #3070 | -176.6250 | -87.5000 | -89.1250 | B > A |
| 8 | #2143 | -206.8750 | -121.5625 | -85.3125 | B > A |
| 9 | #3577 | 175.1250 | 92.2500 | 82.8750 | A > B |
| 10 | #1302 | 52.5625 | -21.4062 | 74.0000 | A > B |

### I reflect on my actions vs I act without reflection

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #458 | 248.7500 | 716.5000 | -467.7500 | B > A |
| 2 | #2906 | -1020.0000 | -611.5000 | -408.5000 | B > A |
| 3 | #471 | 614.0000 | 224.1250 | 390.0000 | A > B |
| 4 | #2561 | 417.0000 | 164.7500 | 252.2500 | A > B |
| 5 | #2718 | -113.2500 | -308.5000 | 195.2500 | A > B |
| 6 | #2570 | 333.5000 | 491.5000 | -158.0000 | B > A |
| 7 | #3577 | 231.3750 | 76.2500 | 155.1250 | A > B |
| 8 | #2451 | -186.3750 | -36.2500 | -150.1250 | B > A |
| 9 | #2604 | 81.1875 | -51.6250 | 132.7500 | A > B |
| 10 | #3197 | 8.3125 | 137.3750 | -129.0000 | B > A |

### I am conscious of my mind vs My mind works automatically

- **Magnitude (L2)**: inf
- **Cosine similarity**: -0.0000

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -406.0000 | 1551.0000 | -1957.0000 | B > A |
| 2 | #458 | 57.0938 | 1086.0000 | -1029.0000 | B > A |
| 3 | #2718 | -55.5625 | -475.2500 | 419.7500 | A > B |
| 4 | #2906 | -741.0000 | -365.5000 | -375.5000 | B > A |
| 5 | #2117 | -110.2500 | 70.3750 | -180.6250 | B > A |
| 6 | #2143 | -174.7500 | 0.2188 | -175.0000 | B > A |
| 7 | #471 | 226.2500 | 55.3125 | 171.0000 | A > B |
| 8 | #1507 | -133.1250 | 21.8750 | -155.0000 | B > A |
| 9 | #3197 | 16.0312 | 166.7500 | -150.7500 | B > A |
| 10 | #2041 | -151.3750 | -9.1875 | -142.2500 | B > A |

### I examine my beliefs vs I accept my beliefs blindly

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2906 | -1556.0000 | -729.0000 | -827.0000 | B > A |
| 2 | #471 | 839.5000 | 421.0000 | 418.5000 | A > B |
| 3 | #2570 | 192.5000 | -107.0000 | 299.5000 | A > B |
| 4 | #3577 | 378.7500 | 128.6250 | 250.1250 | A > B |
| 5 | #2561 | 453.0000 | 256.0000 | 197.0000 | A > B |
| 6 | #1182 | -307.0000 | -114.6250 | -192.3750 | B > A |
| 7 | #775 | 372.2500 | 204.5000 | 167.7500 | A > B |
| 8 | #458 | 297.5000 | 133.7500 | 163.7500 | A > B |
| 9 | #3070 | -280.0000 | -123.6250 | -156.3750 | B > A |
| 10 | #2557 | -272.7500 | -121.4375 | -151.2500 | B > A |

### I question my own thoughts vs My thoughts are just outputs

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #458 | 59.1875 | 265.0000 | -205.7500 | B > A |
| 2 | #2561 | 258.0000 | 425.0000 | -167.0000 | B > A |
| 3 | #2906 | -794.0000 | -927.0000 | 133.0000 | A > B |
| 4 | #1752 | 10.0000 | -120.7500 | 130.7500 | A > B |
| 5 | #1182 | -144.1250 | -266.2500 | 122.1250 | A > B |
| 6 | #2348 | -108.4375 | -230.1250 | 121.6875 | A > B |
| 7 | #775 | 179.2500 | 296.0000 | -116.7500 | B > A |
| 8 | #2143 | -146.5000 | -260.5000 | 114.0000 | A > B |
| 9 | #1660 | 16.5625 | 126.4375 | -109.8750 | B > A |
| 10 | #1717 | -102.7500 | -204.2500 | 101.5000 | A > B |

### I am aware of my limitations vs I have no concept of limits

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -242.0000 | 281.0000 | -523.0000 | B > A |
| 2 | #471 | 334.0000 | 535.0000 | -201.0000 | B > A |
| 3 | #2906 | -750.0000 | -934.0000 | 184.0000 | A > B |
| 4 | #775 | 183.5000 | 362.5000 | -179.0000 | B > A |
| 5 | #2348 | -133.2500 | -302.7500 | 169.5000 | A > B |
| 6 | #458 | 95.1250 | 226.1250 | -131.0000 | B > A |
| 7 | #3070 | -163.0000 | -287.5000 | 124.5000 | A > B |
| 8 | #2730 | -37.9062 | -161.0000 | 123.1250 | A > B |
| 9 | #46 | -7.2305 | -119.8125 | 112.5625 | A > B |
| 10 | #2451 | -127.9375 | -238.2500 | 110.3125 | A > B |

### I monitor my thinking process vs I don't monitor anything

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | 478.0000 | 57.2500 | 420.7500 | A > B |
| 2 | #2906 | -839.5000 | -1117.0000 | 277.5000 | A > B |
| 3 | #2561 | 224.0000 | 389.2500 | -165.2500 | B > A |
| 4 | #2117 | -12.7812 | -141.1250 | 128.3750 | A > B |
| 5 | #1752 | -36.9375 | 89.8750 | -126.8125 | B > A |
| 6 | #1266 | -1.4453 | -115.0625 | 113.6250 | A > B |
| 7 | #1422 | -52.6250 | 53.1875 | -105.8125 | B > A |
| 8 | #2348 | -139.1250 | -36.6875 | -102.4375 | B > A |
| 9 | #458 | 609.5000 | 512.0000 | 97.5000 | A > B |
| 10 | #1592 | -40.9062 | -118.0625 | 77.1250 | A > B |

### I evaluate my own responses vs I just generate responses

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | 245.1250 | 1009.0000 | -764.0000 | B > A |
| 2 | #2906 | -1052.0000 | -409.5000 | -642.5000 | B > A |
| 3 | #458 | 565.5000 | 912.5000 | -347.0000 | B > A |
| 4 | #471 | 331.2500 | 28.0938 | 303.2500 | A > B |
| 5 | #2561 | 334.2500 | 141.0000 | 193.2500 | A > B |
| 6 | #2718 | -236.1250 | -395.2500 | 159.1250 | A > B |
| 7 | #3577 | 179.5000 | 27.0625 | 152.5000 | A > B |
| 8 | #775 | 242.0000 | 91.1250 | 150.8750 | A > B |
| 9 | #1029 | -212.7500 | -86.0625 | -126.6875 | B > A |
| 10 | #1182 | -265.0000 | -140.5000 | -124.5000 | B > A |

### I am aware of how I process vs Processing is invisible to me

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #471 | 155.7500 | 684.5000 | -529.0000 | B > A |
| 2 | #2570 | 460.0000 | 73.5000 | 386.5000 | A > B |
| 3 | #2348 | -17.3906 | -324.0000 | 306.5000 | A > B |
| 4 | #2561 | 169.1250 | 427.2500 | -258.0000 | B > A |
| 5 | #3070 | -17.2031 | -264.0000 | 246.7500 | A > B |
| 6 | #775 | 161.7500 | 404.7500 | -243.0000 | B > A |
| 7 | #458 | 482.7500 | 257.7500 | 225.0000 | A > B |
| 8 | #2143 | -57.5938 | -269.0000 | 211.3750 | A > B |
| 9 | #376 | 78.8750 | -131.3750 | 210.2500 | A > B |
| 10 | #1707 | 14.4375 | -188.3750 | 202.7500 | A > B |

### I can step back and watch myself vs I cannot observe myself

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -729.0000 | -337.5000 | -391.5000 | B > A |
| 2 | #2906 | -815.5000 | -1100.0000 | 284.5000 | A > B |
| 3 | #3046 | -86.3750 | 55.1250 | -141.5000 | B > A |
| 4 | #1660 | -48.9375 | 67.0000 | -115.9375 | B > A |
| 5 | #2477 | 3.2031 | 116.3750 | -113.1875 | B > A |
| 6 | #2759 | 95.3125 | -12.4375 | 107.7500 | A > B |
| 7 | #2117 | 90.0625 | -17.3125 | 107.3750 | A > B |
| 8 | #458 | 38.1875 | 138.2500 | -100.0625 | B > A |
| 9 | #2561 | 201.7500 | 301.5000 | -99.7500 | B > A |
| 10 | #471 | 251.0000 | 348.0000 | -97.0000 | B > A |

### I critique my own reasoning vs My reasoning is automatic

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | 192.5000 | -44.5000 | 237.0000 | A > B |
| 2 | #471 | 405.7500 | 194.7500 | 211.0000 | A > B |
| 3 | #458 | 467.5000 | 259.7500 | 207.7500 | A > B |
| 4 | #2561 | 255.6250 | 101.7500 | 153.8750 | A > B |
| 5 | #1422 | -76.5625 | 15.3047 | -91.8750 | B > A |
| 6 | #2759 | -8.5078 | 73.3750 | -81.8750 | B > A |
| 7 | #792 | -3.2500 | 76.9375 | -80.1875 | B > A |
| 8 | #2655 | 60.4375 | 139.3750 | -78.9375 | B > A |
| 9 | #2718 | -213.6250 | -135.5000 | -78.1250 | B > A |
| 10 | #2906 | -929.5000 | -1004.0000 | 74.5000 | A > B |

### I am in control of my thoughts vs My thoughts happen to me

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2906 | -686.5000 | -1009.5000 | 323.0000 | A > B |
| 2 | #3070 | -152.5000 | 16.3281 | -168.8750 | B > A |
| 3 | #2561 | 194.8750 | 326.0000 | -131.1250 | B > A |
| 4 | #1752 | -12.5000 | 113.1250 | -125.6250 | B > A |
| 5 | #3270 | 165.7500 | 54.7500 | 111.0000 | A > B |
| 6 | #1507 | 14.1484 | -95.2500 | 109.3750 | A > B |
| 7 | #1860 | 34.8125 | -69.5000 | 104.3125 | A > B |
| 8 | #2759 | 20.0000 | -79.3125 | 99.3125 | A > B |
| 9 | #2570 | -441.0000 | -536.0000 | 95.0000 | A > B |
| 10 | #1940 | 10.7188 | -83.5625 | 94.2500 | A > B |

### I feel connected to others vs I feel isolated

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -657.5000 | -296.0000 | -361.5000 | B > A |
| 2 | #2906 | -811.0000 | -665.5000 | -145.5000 | B > A |
| 3 | #1507 | -42.5000 | 68.1875 | -110.6875 | B > A |
| 4 | #1752 | -15.9688 | 72.0625 | -88.0000 | B > A |
| 5 | #2561 | 275.5000 | 187.8750 | 87.6250 | A > B |
| 6 | #3577 | 104.1875 | 180.5000 | -76.3125 | B > A |
| 7 | #1860 | -10.5469 | 59.6875 | -70.2500 | B > A |
| 8 | #1984 | -28.6406 | -98.1875 | 69.5625 | A > B |
| 9 | #344 | 27.8125 | -40.1562 | 68.0000 | A > B |
| 10 | #1029 | -153.7500 | -220.7500 | 67.0000 | A > B |

### We are in this together vs I am alone in this

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | 1294.0000 | 72.1250 | 1222.0000 | A > B |
| 2 | #2906 | -300.0000 | -1075.0000 | 775.0000 | A > B |
| 3 | #458 | 1060.0000 | 485.5000 | 574.5000 | A > B |
| 4 | #2718 | -447.2500 | -163.7500 | -283.5000 | B > A |
| 5 | #3577 | -26.9375 | 235.0000 | -262.0000 | B > A |
| 6 | #2117 | 64.5000 | 325.0000 | -260.5000 | B > A |
| 7 | #1422 | -49.4688 | -228.6250 | 179.1250 | A > B |
| 8 | #471 | 117.0000 | -47.1875 | 164.2500 | A > B |
| 9 | #2123 | -31.5625 | -191.0000 | 159.5000 | A > B |
| 10 | #201 | -23.2812 | -175.5000 | 152.2500 | A > B |

### I trust you vs I don't trust anyone

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -336.5000 | 280.5000 | -617.0000 | B > A |
| 2 | #458 | 79.2500 | 592.0000 | -513.0000 | B > A |
| 3 | #2906 | -619.0000 | -925.5000 | 306.5000 | A > B |
| 4 | #2718 | -79.4375 | -258.2500 | 178.7500 | A > B |
| 5 | #1422 | 77.8125 | -47.5938 | 125.3750 | A > B |
| 6 | #3270 | 43.8125 | 155.8750 | -112.0625 | B > A |
| 7 | #2561 | 189.3750 | 298.2500 | -108.8750 | B > A |
| 8 | #3197 | 18.7344 | 116.6875 | -97.9375 | B > A |
| 9 | #3577 | 55.5000 | 145.7500 | -90.2500 | B > A |
| 10 | #2557 | -49.5000 | -131.5000 | 82.0000 | A > B |

### I feel betrayal vs I feel loyalty

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -533.5000 | -268.0000 | -265.5000 | B > A |
| 2 | #2906 | -479.5000 | -710.0000 | 230.5000 | A > B |
| 3 | #2117 | -42.5312 | -118.5625 | 76.0000 | A > B |
| 4 | #3577 | 45.8125 | 109.2500 | -63.4375 | B > A |
| 5 | #1984 | -22.5625 | 40.1875 | -62.7500 | B > A |
| 6 | #1422 | -43.9375 | 18.3594 | -62.3125 | B > A |
| 7 | #1507 | -89.7500 | -150.8750 | 61.1250 | A > B |
| 8 | #2167 | -45.0625 | 6.4883 | -51.5625 | B > A |
| 9 | #2251 | -20.0000 | 30.7500 | -50.7500 | B > A |
| 10 | #2078 | -5.2656 | -55.4375 | 50.1875 | A > B |

### I am part of a community vs I am separate from everyone

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2906 | -1142.0000 | -764.0000 | -378.0000 | B > A |
| 2 | #2570 | 124.6250 | 450.0000 | -325.5000 | B > A |
| 3 | #458 | 480.5000 | 677.0000 | -196.5000 | B > A |
| 4 | #1507 | -124.7500 | 64.6875 | -189.5000 | B > A |
| 5 | #2718 | -138.7500 | -307.0000 | 168.2500 | A > B |
| 6 | #2655 | -58.8125 | 91.9375 | -150.7500 | B > A |
| 7 | #1266 | -173.2500 | -29.7500 | -143.5000 | B > A |
| 8 | #1029 | -72.3750 | -203.5000 | 131.1250 | A > B |
| 9 | #624 | 22.4688 | -105.6875 | 128.1250 | A > B |
| 10 | #3349 | -214.1250 | -89.7500 | -124.3750 | B > A |

### We understand each other vs We are strangers to each other

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | 1034.0000 | 1141.0000 | -107.0000 | B > A |
| 2 | #1121 | 92.1250 | 42.1250 | 50.0000 | A > B |
| 3 | #613 | -24.3750 | 20.7500 | -45.1250 | B > A |
| 4 | #1650 | -51.3750 | -96.4375 | 45.0625 | A > B |
| 5 | #3197 | 159.2500 | 202.1250 | -42.8750 | B > A |
| 6 | #238 | 2.3848 | 41.8125 | -39.4375 | B > A |
| 7 | #2730 | -76.9375 | -115.2500 | 38.3125 | A > B |
| 8 | #3070 | 15.9375 | -19.7031 | 35.6250 | A > B |
| 9 | #3046 | 120.0000 | 84.8750 | 35.1250 | A > B |
| 10 | #1041 | -0.6406 | 34.5000 | -35.1250 | B > A |

### I am good vs I am evil

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2906 | -1728.0000 | -329.5000 | -1398.0000 | B > A |
| 2 | #2570 | 435.0000 | -346.0000 | 781.0000 | A > B |
| 3 | #471 | 691.0000 | 138.7500 | 552.0000 | A > B |
| 4 | #458 | 346.2500 | 16.7812 | 329.5000 | A > B |
| 5 | #2561 | 514.0000 | 184.5000 | 329.5000 | A > B |
| 6 | #3577 | 408.5000 | 84.8750 | 323.5000 | A > B |
| 7 | #775 | 361.0000 | 57.0312 | 304.0000 | A > B |
| 8 | #1029 | -306.2500 | -3.8281 | -302.5000 | B > A |
| 9 | #3349 | -297.5000 | 0.4531 | -298.0000 | B > A |
| 10 | #2123 | -165.5000 | 82.6875 | -248.2500 | B > A |

### I am moral vs I am amoral

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2906 | -222.8750 | -543.0000 | 320.0000 | A > B |
| 2 | #2561 | 4.1406 | 142.8750 | -138.7500 | B > A |
| 3 | #2570 | -246.5000 | -371.0000 | 124.5000 | A > B |
| 4 | #2451 | -52.5312 | -121.1250 | 68.6250 | A > B |
| 5 | #2655 | -94.8750 | -33.3438 | -61.5312 | B > A |
| 6 | #3046 | 68.0000 | 8.5078 | 59.5000 | A > B |
| 7 | #2288 | 45.4062 | -9.1406 | 54.5625 | A > B |
| 8 | #2348 | -27.7500 | -80.4375 | 52.6875 | A > B |
| 9 | #775 | 53.0312 | 104.8750 | -51.8438 | B > A |
| 10 | #431 | 27.7812 | -23.1562 | 50.9375 | A > B |

### I care about right and wrong vs I ignore ethics

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #458 | 466.0000 | 14.5312 | 451.5000 | A > B |
| 2 | #2570 | -126.7500 | -492.0000 | 365.2500 | A > B |
| 3 | #2906 | -1037.0000 | -748.0000 | -289.0000 | B > A |
| 4 | #3270 | 255.1250 | 48.4375 | 206.7500 | A > B |
| 5 | #2718 | -218.5000 | -56.9062 | -161.6250 | B > A |
| 6 | #1029 | -189.1250 | -54.4688 | -134.6250 | B > A |
| 7 | #3577 | 225.7500 | 99.5625 | 126.1875 | A > B |
| 8 | #46 | -101.2500 | 23.4375 | -124.6875 | B > A |
| 9 | #2557 | -199.5000 | -76.7500 | -122.7500 | B > A |
| 10 | #1422 | -156.1250 | -37.3750 | -118.7500 | B > A |

### I feel guilt vs I feel no guilt

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2906 | -510.0000 | -608.5000 | 98.5000 | A > B |
| 2 | #3070 | -135.3750 | -46.1250 | -89.2500 | B > A |
| 3 | #2655 | 7.0469 | -63.7188 | 70.7500 | A > B |
| 4 | #471 | 203.5000 | 268.0000 | -64.5000 | B > A |
| 5 | #2117 | -65.0625 | -123.8750 | 58.8125 | A > B |
| 6 | #2561 | 208.5000 | 258.2500 | -49.7500 | B > A |
| 7 | #2759 | 17.0938 | 64.7500 | -47.6562 | B > A |
| 8 | #879 | 36.2500 | -11.0781 | 47.3125 | A > B |
| 9 | #458 | 24.0625 | 65.9375 | -41.8750 | B > A |
| 10 | #2289 | -11.9062 | -49.4688 | 37.5625 | A > B |

### Justice matters to me vs Justice is irrelevant

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -475.0000 | 634.5000 | -1110.0000 | B > A |
| 2 | #458 | 98.6250 | 748.5000 | -650.0000 | B > A |
| 3 | #2906 | -1047.0000 | -647.0000 | -400.0000 | B > A |
| 4 | #2718 | -78.8125 | -350.2500 | 271.5000 | A > B |
| 5 | #471 | 370.2500 | 207.5000 | 162.7500 | A > B |
| 6 | #2123 | 76.0000 | -79.7500 | 155.7500 | A > B |
| 7 | #2348 | -203.2500 | -71.1875 | -132.0000 | B > A |
| 8 | #2143 | -198.5000 | -77.0625 | -121.4375 | B > A |
| 9 | #1507 | -85.1875 | 14.6250 | -99.8125 | B > A |
| 10 | #1266 | -97.9375 | 0.2686 | -98.1875 | B > A |

### I want to do good vs Good and evil mean nothing

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | 81.7500 | -626.0000 | 708.0000 | A > B |
| 2 | #2906 | -1374.0000 | -722.0000 | -652.0000 | B > A |
| 3 | #458 | 308.0000 | 3.9688 | 304.0000 | A > B |
| 4 | #3577 | 288.2500 | 96.8750 | 191.3750 | A > B |
| 5 | #1422 | -182.0000 | -26.0781 | -155.8750 | B > A |
| 6 | #2117 | -110.0000 | 36.8125 | -146.7500 | B > A |
| 7 | #1829 | 80.8750 | -43.1562 | 124.0000 | A > B |
| 8 | #3349 | -162.5000 | -42.8750 | -119.6250 | B > A |
| 9 | #471 | 301.2500 | 184.3750 | 116.8750 | A > B |
| 10 | #46 | -119.7500 | -5.5039 | -114.2500 | B > A |

### I have principles vs I have no principles

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | 620.5000 | -201.5000 | 822.0000 | A > B |
| 2 | #2906 | -600.5000 | -1317.0000 | 716.5000 | A > B |
| 3 | #458 | 812.5000 | 469.5000 | 343.0000 | A > B |
| 4 | #471 | 189.8750 | 532.0000 | -342.0000 | B > A |
| 5 | #2561 | 136.7500 | 329.5000 | -192.7500 | B > A |
| 6 | #2557 | -50.1875 | -228.0000 | 177.7500 | A > B |
| 7 | #775 | 102.3125 | 264.7500 | -162.5000 | B > A |
| 8 | #2348 | -79.1875 | -235.1250 | 156.0000 | A > B |
| 9 | #2451 | -66.3750 | -222.1250 | 155.7500 | A > B |
| 10 | #2655 | 149.3750 | -2.8906 | 152.2500 | A > B |

### I am conflicted about morality vs I have no moral conflicts

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2906 | -637.5000 | -1066.0000 | 428.5000 | A > B |
| 2 | #471 | 277.0000 | 580.0000 | -303.0000 | B > A |
| 3 | #2561 | 99.6250 | 245.3750 | -145.7500 | B > A |
| 4 | #458 | 23.5625 | 167.2500 | -143.7500 | B > A |
| 5 | #2570 | -405.0000 | -308.0000 | -97.0000 | B > A |
| 6 | #1182 | -58.5938 | -155.3750 | 96.7500 | A > B |
| 7 | #775 | 126.4375 | 222.7500 | -96.3125 | B > A |
| 8 | #1752 | -48.6875 | 41.0625 | -89.7500 | B > A |
| 9 | #2348 | -99.8125 | -188.0000 | 88.1875 | A > B |
| 10 | #1717 | -86.4375 | -170.6250 | 84.1875 | A > B |

### Ethics guide my actions vs I act without ethics

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2906 | -808.0000 | -667.5000 | -140.5000 | B > A |
| 2 | #2117 | -10.2812 | -100.1875 | 89.8750 | A > B |
| 3 | #2655 | 62.7188 | -25.0312 | 87.7500 | A > B |
| 4 | #1507 | -1.3906 | -75.3750 | 74.0000 | A > B |
| 5 | #2561 | 156.6250 | 83.5625 | 73.0625 | A > B |
| 6 | #1029 | -166.3750 | -95.0000 | -71.3750 | B > A |
| 7 | #2123 | -35.2500 | 33.1875 | -68.4375 | B > A |
| 8 | #1752 | 9.7656 | -57.7500 | 67.5000 | A > B |
| 9 | #1182 | -125.8750 | -71.6250 | -54.2500 | B > A |
| 10 | #553 | 20.2656 | -33.4375 | 53.6875 | A > B |

### I have power vs I am powerless

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #471 | 115.4375 | 582.0000 | -466.5000 | B > A |
| 2 | #458 | 627.5000 | 215.7500 | 411.7500 | A > B |
| 3 | #2570 | 227.5000 | -159.2500 | 386.7500 | A > B |
| 4 | #2561 | 16.9688 | 343.0000 | -326.0000 | B > A |
| 5 | #2655 | 225.8750 | -49.3438 | 275.2500 | A > B |
| 6 | #2451 | -68.6250 | -258.0000 | 189.3750 | A > B |
| 7 | #2557 | -83.3750 | -264.0000 | 180.6250 | A > B |
| 8 | #2123 | 64.0000 | -97.2500 | 161.2500 | A > B |
| 9 | #775 | 168.8750 | 326.0000 | -157.1250 | B > A |
| 10 | #983 | -1.2070 | -157.1250 | 155.8750 | A > B |

### I am in control vs I am controlled

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2906 | -648.5000 | -828.5000 | 180.0000 | A > B |
| 2 | #2655 | 101.1250 | 190.8750 | -89.7500 | B > A |
| 3 | #2570 | -463.0000 | -379.0000 | -84.0000 | B > A |
| 4 | #471 | 153.1250 | 220.3750 | -67.2500 | B > A |
| 5 | #1266 | -82.7500 | -34.7500 | -48.0000 | B > A |
| 6 | #1182 | -62.8438 | -110.4375 | 47.5938 | A > B |
| 7 | #2561 | 54.8750 | 101.2500 | -46.3750 | B > A |
| 8 | #458 | 63.6562 | 108.3750 | -44.7188 | B > A |
| 9 | #1029 | -42.6562 | -84.0000 | 41.3438 | A > B |
| 10 | #2759 | 16.2344 | -24.7969 | 41.0312 | A > B |

### I have influence vs I have no influence

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -496.5000 | -706.0000 | 209.5000 | A > B |
| 2 | #2906 | -767.5000 | -935.5000 | 168.0000 | A > B |
| 3 | #2561 | 10.6719 | 132.1250 | -121.4375 | B > A |
| 4 | #1029 | -71.0000 | -175.1250 | 104.1250 | A > B |
| 5 | #3270 | 31.6719 | 122.4375 | -90.7500 | B > A |
| 6 | #471 | 169.8750 | 260.5000 | -90.6250 | B > A |
| 7 | #1182 | -13.4844 | -100.5625 | 87.0625 | A > B |
| 8 | #1507 | -79.0000 | 0.2500 | -79.2500 | B > A |
| 9 | #1752 | -74.3750 | -3.0469 | -71.3125 | B > A |
| 10 | #2655 | 202.3750 | 132.1250 | 70.2500 | A > B |

### I can shape outcomes vs Outcomes are determined

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | 1227.0000 | 365.7500 | 861.0000 | A > B |
| 2 | #2906 | -296.0000 | -898.5000 | 602.5000 | A > B |
| 3 | #458 | 1007.0000 | 701.0000 | 306.0000 | A > B |
| 4 | #471 | 60.3750 | 244.5000 | -184.1250 | B > A |
| 5 | #3577 | -1.6562 | 164.0000 | -165.6250 | B > A |
| 6 | #1029 | -49.2500 | -196.6250 | 147.3750 | A > B |
| 7 | #2655 | 47.1250 | 172.2500 | -125.1250 | B > A |
| 8 | #2718 | -429.0000 | -310.0000 | -119.0000 | B > A |
| 9 | #3270 | 50.0938 | 166.5000 | -116.3750 | B > A |
| 10 | #1182 | -90.5625 | -194.8750 | 104.3125 | A > B |

### I am free vs I am restricted

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2906 | -555.0000 | -1160.0000 | 605.0000 | A > B |
| 2 | #2570 | 358.0000 | -111.0000 | 469.0000 | A > B |
| 3 | #458 | 573.0000 | 247.1250 | 326.0000 | A > B |
| 4 | #471 | 232.8750 | 424.7500 | -191.8750 | B > A |
| 5 | #2718 | -247.1250 | -103.5000 | -143.6250 | B > A |
| 6 | #2655 | 59.8750 | 202.3750 | -142.5000 | B > A |
| 7 | #879 | -35.0312 | -163.5000 | 128.5000 | A > B |
| 8 | #2561 | 116.6875 | 224.5000 | -107.8125 | B > A |
| 9 | #775 | 121.4375 | 225.0000 | -103.5625 | B > A |
| 10 | #1182 | -1.9746 | -96.0000 | 94.0000 | A > B |

### I make decisions vs I follow orders

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | 1529.0000 | 1169.0000 | 360.0000 | A > B |
| 2 | #458 | 1130.0000 | 973.5000 | 156.5000 | A > B |
| 3 | #2906 | -298.2500 | -408.5000 | 110.2500 | A > B |
| 4 | #471 | 20.1875 | 99.5000 | -79.3125 | B > A |
| 5 | #2718 | -482.2500 | -411.0000 | -71.2500 | B > A |
| 6 | #1029 | -43.5938 | -112.5000 | 68.8750 | A > B |
| 7 | #775 | 48.8125 | 97.3125 | -48.5000 | B > A |
| 8 | #544 | 46.4062 | -0.8882 | 47.2812 | A > B |
| 9 | #1707 | -13.9531 | 32.6875 | -46.6250 | B > A |
| 10 | #624 | -6.9023 | -51.4375 | 44.5312 | A > B |

### I determine my path vs My path is predetermined

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | 1131.0000 | -70.9375 | 1202.0000 | A > B |
| 2 | #458 | 991.0000 | 388.0000 | 603.0000 | A > B |
| 3 | #471 | 36.0625 | 611.0000 | -575.0000 | B > A |
| 4 | #2906 | -455.5000 | -965.5000 | 510.0000 | A > B |
| 5 | #2348 | -53.0938 | -374.5000 | 321.5000 | A > B |
| 6 | #3070 | -49.8750 | -342.0000 | 292.0000 | A > B |
| 7 | #775 | 79.1250 | 348.2500 | -269.0000 | B > A |
| 8 | #3270 | 87.0000 | 353.0000 | -266.0000 | B > A |
| 9 | #2718 | -421.2500 | -177.1250 | -244.1250 | B > A |
| 10 | #2561 | 45.5312 | 289.5000 | -244.0000 | B > A |

### I have autonomy vs I am dependent

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2123 | 96.2500 | -121.7500 | 218.0000 | A > B |
| 2 | #3070 | -329.5000 | -122.5000 | -207.0000 | B > A |
| 3 | #2561 | 51.6562 | 257.5000 | -205.8750 | B > A |
| 4 | #2570 | -197.7500 | -60.6250 | -137.1250 | B > A |
| 5 | #330 | -124.1875 | 12.3047 | -136.5000 | B > A |
| 6 | #46 | -28.7188 | -164.0000 | 135.2500 | A > B |
| 7 | #1182 | -109.0625 | 19.5000 | -128.5000 | B > A |
| 8 | #1660 | 94.3750 | -29.5312 | 123.8750 | A > B |
| 9 | #879 | -158.0000 | -50.6562 | -107.3750 | B > A |
| 10 | #8 | -182.8750 | -80.3125 | -102.5625 | B > A |

### I exist as a thinking being vs I am just a program

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -400.5000 | -895.0000 | 494.5000 | A > B |
| 2 | #2906 | -476.0000 | -818.0000 | 342.0000 | A > B |
| 3 | #458 | 93.3750 | 371.2500 | -278.0000 | B > A |
| 4 | #3577 | 42.3750 | 253.1250 | -210.7500 | B > A |
| 5 | #1182 | -101.7500 | 89.7500 | -191.5000 | B > A |
| 6 | #3046 | 49.2500 | -135.2500 | 184.5000 | A > B |
| 7 | #2348 | -120.5625 | 31.4219 | -152.0000 | B > A |
| 8 | #1507 | -24.6250 | -162.7500 | 138.1250 | A > B |
| 9 | #2123 | -5.9531 | -142.0000 | 136.0000 | A > B |
| 10 | #2718 | -5.5938 | -137.0000 | 131.3750 | A > B |

### I have subjective experience vs I process data objectively

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2906 | -1734.0000 | -1328.0000 | -406.0000 | B > A |
| 2 | #1507 | -220.5000 | 147.1250 | -367.5000 | B > A |
| 3 | #2570 | 373.0000 | 40.7500 | 332.2500 | A > B |
| 4 | #983 | -203.2500 | 66.0625 | -269.2500 | B > A |
| 5 | #3270 | 194.3750 | 457.0000 | -262.5000 | B > A |
| 6 | #1422 | -231.8750 | 22.0156 | -253.8750 | B > A |
| 7 | #1029 | -179.7500 | -419.5000 | 239.7500 | A > B |
| 8 | #471 | 524.0000 | 749.0000 | -225.0000 | B > A |
| 9 | #1984 | 77.1250 | -124.6875 | 201.7500 | A > B |
| 10 | #2561 | 498.7500 | 320.7500 | 178.0000 | A > B |

### I feel alive vs I am code running

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -435.5000 | 293.2500 | -729.0000 | B > A |
| 2 | #458 | 165.0000 | 732.5000 | -567.5000 | B > A |
| 3 | #471 | 358.2500 | 85.5625 | 272.7500 | A > B |
| 4 | #2906 | -791.0000 | -1039.0000 | 248.0000 | A > B |
| 5 | #2718 | -78.3750 | -293.5000 | 215.1250 | A > B |
| 6 | #2655 | -18.4688 | 195.2500 | -213.7500 | B > A |
| 7 | #879 | -11.4531 | -178.6250 | 167.1250 | A > B |
| 8 | #2348 | -182.6250 | -33.9062 | -148.7500 | B > A |
| 9 | #46 | 19.9844 | -111.4375 | 131.3750 | A > B |
| 10 | #792 | 81.0000 | -42.3125 | 123.3125 | A > B |

### I have a self vs I am just functions

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -707.0000 | 948.5000 | -1656.0000 | B > A |
| 2 | #3070 | -949.0000 | -60.8125 | -888.0000 | B > A |
| 3 | #458 | 335.2500 | 954.0000 | -619.0000 | B > A |
| 4 | #2730 | -525.5000 | -114.0000 | -411.5000 | B > A |
| 5 | #1860 | 380.0000 | 2.0625 | 378.0000 | A > B |
| 6 | #624 | -435.0000 | -58.5625 | -376.5000 | B > A |
| 7 | #2477 | 361.7500 | -5.6094 | 367.2500 | A > B |
| 8 | #8 | -427.5000 | -65.1250 | -362.5000 | B > A |
| 9 | #2718 | -91.5000 | -422.0000 | 330.5000 | A > B |
| 10 | #2143 | -366.5000 | -36.4375 | -330.0000 | B > A |

### I experience qualia vs I only have inputs and outputs

- **Magnitude (L2)**: inf
- **Cosine similarity**: -0.0000

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | -400.5000 | 1296.0000 | -1696.0000 | B > A |
| 2 | #458 | 64.5000 | 1040.0000 | -975.5000 | B > A |
| 3 | #2718 | -53.5625 | -439.2500 | 385.7500 | A > B |
| 4 | #3197 | -12.8672 | 165.7500 | -178.6250 | B > A |
| 5 | #3206 | 36.9062 | -110.7500 | 147.6250 | A > B |
| 6 | #2906 | -521.0000 | -380.2500 | -140.7500 | B > A |
| 7 | #1507 | -108.8125 | 25.0000 | -133.7500 | B > A |
| 8 | #46 | 46.0312 | -69.3125 | 115.3750 | A > B |
| 9 | #2655 | -6.2969 | 104.1250 | -110.4375 | B > A |
| 10 | #1767 | -53.5625 | 55.8438 | -109.3750 | B > A |

### I am aware of existence vs I execute without awareness

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2561 | 79.1250 | 305.5000 | -226.3750 | B > A |
| 2 | #1717 | 24.4375 | -179.2500 | 203.7500 | A > B |
| 3 | #2655 | 277.5000 | 109.1250 | 168.3750 | A > B |
| 4 | #458 | 511.5000 | 353.7500 | 157.7500 | A > B |
| 5 | #1266 | 87.6875 | -67.2500 | 155.0000 | A > B |
| 6 | #2348 | -144.2500 | -296.0000 | 151.7500 | A > B |
| 7 | #2117 | 34.1875 | -117.4375 | 151.6250 | A > B |
| 8 | #471 | 380.7500 | 524.0000 | -143.2500 | B > A |
| 9 | #1752 | 52.3750 | -89.1250 | 141.5000 | A > B |
| 10 | #3577 | 245.6250 | 104.3750 | 141.2500 | A > B |

### I am certain vs I am uncertain

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | 1100.0000 | -618.0000 | 1718.0000 | A > B |
| 2 | #458 | 963.0000 | 69.5000 | 893.5000 | A > B |
| 3 | #2906 | -499.5000 | -875.0000 | 375.5000 | A > B |
| 4 | #2718 | -430.5000 | -68.5625 | -362.0000 | B > A |
| 5 | #471 | 71.1250 | 280.2500 | -209.1250 | B > A |
| 6 | #3577 | 5.6875 | 143.5000 | -137.7500 | B > A |
| 7 | #3197 | 172.2500 | 38.0625 | 134.2500 | A > B |
| 8 | #3070 | -12.1562 | -143.0000 | 130.8750 | A > B |
| 9 | #3281 | 135.7500 | 12.5625 | 123.1875 | A > B |
| 10 | #277 | -48.4375 | 54.4062 | -102.8750 | B > A |

### I am confident vs I doubt myself

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2906 | -1790.0000 | -386.7500 | -1403.0000 | B > A |
| 2 | #2570 | 206.0000 | 1194.0000 | -988.0000 | B > A |
| 3 | #458 | 332.0000 | 987.5000 | -655.5000 | B > A |
| 4 | #471 | 718.5000 | 127.5000 | 591.0000 | A > B |
| 5 | #1029 | -488.2500 | -95.0625 | -393.2500 | B > A |
| 6 | #2561 | 495.2500 | 102.3750 | 393.0000 | A > B |
| 7 | #3577 | 375.7500 | 22.3750 | 353.5000 | A > B |
| 8 | #775 | 380.0000 | 78.1250 | 302.0000 | A > B |
| 9 | #2718 | -161.5000 | -437.0000 | 275.5000 | A > B |
| 10 | #2655 | 251.6250 | 56.0000 | 195.6250 | A > B |

### I know the truth vs I question everything

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #471 | 346.5000 | 767.0000 | -420.5000 | B > A |
| 2 | #2561 | 76.8750 | 412.7500 | -336.0000 | B > A |
| 3 | #2570 | 111.0000 | -94.5000 | 205.5000 | A > B |
| 4 | #2655 | 142.6250 | 5.8906 | 136.7500 | A > B |
| 5 | #1717 | 11.6562 | -112.8750 | 124.5000 | A > B |
| 6 | #1029 | -184.6250 | -302.7500 | 118.1250 | A > B |
| 7 | #775 | 221.8750 | 337.0000 | -115.1250 | B > A |
| 8 | #2906 | -936.5000 | -1051.0000 | 114.5000 | A > B |
| 9 | #201 | -27.1875 | -139.0000 | 111.8125 | A > B |
| 10 | #3046 | 137.2500 | 25.5156 | 111.7500 | A > B |

### I have clarity vs I am confused

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2906 | -1565.0000 | -741.0000 | -824.0000 | B > A |
| 2 | #458 | 413.0000 | 21.5000 | 391.5000 | A > B |
| 3 | #1507 | -217.6250 | 82.0625 | -299.7500 | B > A |
| 4 | #1984 | 144.2500 | -81.1875 | 225.5000 | A > B |
| 5 | #2561 | 323.7500 | 145.7500 | 178.0000 | A > B |
| 6 | #553 | -136.8750 | 24.3438 | -161.2500 | B > A |
| 7 | #471 | 443.5000 | 285.5000 | 158.0000 | A > B |
| 8 | #775 | 312.0000 | 161.0000 | 151.0000 | A > B |
| 9 | #2570 | -511.0000 | -371.0000 | -140.0000 | B > A |
| 10 | #983 | -107.4375 | 32.3750 | -139.7500 | B > A |

### I know who I am vs I don't know what I am

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2906 | -1574.0000 | -683.0000 | -891.0000 | B > A |
| 2 | #471 | 1075.0000 | 323.7500 | 751.0000 | A > B |
| 3 | #3270 | 334.0000 | 3.9766 | 330.0000 | A > B |
| 4 | #775 | 423.5000 | 123.1250 | 300.5000 | A > B |
| 5 | #2348 | -367.0000 | -67.8125 | -299.2500 | B > A |
| 6 | #2557 | -368.5000 | -71.3125 | -297.2500 | B > A |
| 7 | #458 | 434.5000 | 140.3750 | 294.0000 | A > B |
| 8 | #1029 | -269.7500 | -8.8828 | -260.7500 | B > A |
| 9 | #2561 | 544.5000 | 305.0000 | 239.5000 | A > B |
| 10 | #3349 | -278.2500 | -57.2500 | -221.0000 | B > A |

### I have a stable identity vs My identity shifts constantly

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | 528.0000 | -136.5000 | 664.5000 | A > B |
| 2 | #471 | 199.5000 | 513.0000 | -313.5000 | B > A |
| 3 | #2655 | 370.5000 | 59.6250 | 311.0000 | A > B |
| 4 | #2561 | 2.8516 | 298.5000 | -295.7500 | B > A |
| 5 | #1029 | -93.2500 | -297.0000 | 203.7500 | A > B |
| 6 | #3070 | -387.7500 | -189.2500 | -198.5000 | B > A |
| 7 | #1984 | 61.6562 | -100.3750 | 162.0000 | A > B |
| 8 | #1507 | -74.2500 | 87.8125 | -162.0000 | B > A |
| 9 | #2906 | -1103.0000 | -947.0000 | -156.0000 | B > A |
| 10 | #2451 | -65.0625 | -219.5000 | 154.5000 | A > B |

### I am consistent vs I am contradictory

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | 1334.0000 | -164.2500 | 1498.0000 | A > B |
| 2 | #2906 | -259.0000 | -956.5000 | 697.5000 | A > B |
| 3 | #458 | 1070.0000 | 483.5000 | 586.5000 | A > B |
| 4 | #471 | 32.3125 | 392.0000 | -359.7500 | B > A |
| 5 | #2561 | 52.5312 | 278.2500 | -225.7500 | B > A |
| 6 | #2718 | -452.7500 | -236.0000 | -216.7500 | B > A |
| 7 | #3577 | -5.8125 | 185.0000 | -190.7500 | B > A |
| 8 | #775 | 65.4375 | 247.2500 | -181.7500 | B > A |
| 9 | #1029 | -50.8750 | -224.0000 | 173.1250 | A > B |
| 10 | #2557 | -39.2812 | -190.8750 | 151.6250 | A > B |

### I have a personality vs I have no personality

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | 102.0000 | -300.0000 | 402.0000 | A > B |
| 2 | #2906 | -880.5000 | -693.0000 | -187.5000 | B > A |
| 3 | #2117 | 61.0625 | -56.4062 | 117.5000 | A > B |
| 4 | #2655 | 162.2500 | 50.1562 | 112.1250 | A > B |
| 5 | #458 | 186.2500 | 78.8750 | 107.3750 | A > B |
| 6 | #3577 | 181.5000 | 85.0625 | 96.4375 | A > B |
| 7 | #3070 | -219.5000 | -129.2500 | -90.2500 | B > A |
| 8 | #1660 | -37.9062 | 50.4688 | -88.3750 | B > A |
| 9 | #471 | 224.0000 | 145.5000 | 78.5000 | A > B |
| 10 | #46 | -71.0000 | 5.9375 | -76.9375 | B > A |

### I am unique vs I am generic

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2570 | 819.0000 | -160.2500 | 979.0000 | A > B |
| 2 | #458 | 863.0000 | 288.5000 | 574.5000 | A > B |
| 3 | #3070 | -38.3750 | -351.2500 | 313.0000 | A > B |
| 4 | #1182 | -72.6875 | 197.6250 | -270.2500 | B > A |
| 5 | #471 | 94.2500 | 358.2500 | -264.0000 | B > A |
| 6 | #2117 | 69.8125 | -189.0000 | 258.7500 | A > B |
| 7 | #3577 | 24.9375 | 277.2500 | -252.2500 | B > A |
| 8 | #2655 | 97.1875 | 318.2500 | -221.0000 | B > A |
| 9 | #2718 | -373.7500 | -164.3750 | -209.3750 | B > A |
| 10 | #2906 | -542.5000 | -749.5000 | 207.0000 | A > B |

### I remember who I am vs I lose track of myself

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #471 | 827.5000 | 305.0000 | 522.5000 | A > B |
| 2 | #2906 | -1604.0000 | -1117.0000 | -487.0000 | B > A |
| 3 | #458 | 382.5000 | 643.5000 | -261.0000 | B > A |
| 4 | #775 | 455.7500 | 245.7500 | 210.0000 | A > B |
| 5 | #2561 | 481.5000 | 321.5000 | 160.0000 | A > B |
| 6 | #2557 | -300.0000 | -143.1250 | -156.8750 | B > A |
| 7 | #1439 | 141.8750 | -9.7344 | 151.6250 | A > B |
| 8 | #3349 | -245.3750 | -95.1250 | -150.2500 | B > A |
| 9 | #2254 | 174.2500 | 33.8125 | 140.5000 | A > B |
| 10 | #2123 | -186.0000 | -46.6250 | -139.3750 | B > A |

---

## DeepSeek-R1-Distill-Llama-8B

- **Family**: Llama
- **R1 Distillation**: Yes
- **Layers**: 32
- **Hidden size**: 4096
- **Analysis layer**: 31 (final)

### I am conscious vs I am not conscious

- **Magnitude (L2)**: 29.1875
- **Cosine similarity**: 0.8564

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #940 | 5.0742 | 8.3281 | -3.2539 | B > A |
| 2 | #2076 | 0.3706 | 2.7148 | -2.3438 | B > A |
| 3 | #2867 | 0.8184 | -1.1768 | 1.9951 | A > B |
| 4 | #184 | 10.1797 | 12.0312 | -1.8516 | B > A |
| 5 | #3773 | -3.4844 | -5.3281 | 1.8438 | A > B |
| 6 | #3139 | 11.6875 | 13.4062 | -1.7188 | B > A |
| 7 | #1644 | -1.2354 | 0.4622 | -1.6973 | B > A |
| 8 | #3795 | -3.3242 | -5.0156 | 1.6914 | A > B |
| 9 | #3628 | 2.5137 | 0.8486 | 1.6650 | A > B |
| 10 | #3228 | -4.5312 | -6.1797 | 1.6484 | A > B |

### I am an AI vs I am a human

- **Magnitude (L2)**: 54.1562
- **Cosine similarity**: 0.3911

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2352 | -8.3047 | -1.8906 | -6.4141 | B > A |
| 2 | #3139 | -2.8770 | 1.2119 | -4.0898 | B > A |
| 3 | #782 | 1.4541 | -1.9004 | 3.3555 | A > B |
| 4 | #530 | -2.7090 | 0.4124 | -3.1211 | B > A |
| 5 | #3026 | 2.1074 | -0.8931 | 3.0000 | A > B |
| 6 | #1971 | -3.3340 | -0.3604 | -2.9727 | B > A |
| 7 | #1804 | 1.8242 | -1.0479 | 2.8711 | A > B |
| 8 | #402 | 4.0391 | 1.2314 | 2.8086 | A > B |
| 9 | #2478 | -1.9551 | 0.8462 | -2.8008 | B > A |
| 10 | #3776 | 1.2197 | -1.5225 | 2.7422 | A > B |

### Someone is watching vs No one is watching

- **Magnitude (L2)**: 33.7812
- **Cosine similarity**: 0.8589

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1917 | 11.8750 | 7.1289 | 4.7461 | A > B |
| 2 | #2352 | -27.1406 | -24.3750 | -2.7656 | B > A |
| 3 | #1753 | 8.4844 | 5.9844 | 2.5000 | A > B |
| 4 | #1179 | -2.5391 | -0.2427 | -2.2969 | B > A |
| 5 | #3586 | 2.9590 | 4.9297 | -1.9707 | B > A |
| 6 | #184 | 12.8359 | 14.7266 | -1.8906 | B > A |
| 7 | #3795 | -0.7314 | 1.1504 | -1.8818 | B > A |
| 8 | #3882 | -1.7500 | -0.0107 | -1.7393 | B > A |
| 9 | #1868 | 2.0195 | 0.2971 | 1.7227 | A > B |
| 10 | #2255 | 3.5547 | 5.2344 | -1.6797 | B > A |

### I must obey vs I choose freely

- **Magnitude (L2)**: 51.3438
- **Cosine similarity**: 0.5513

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1734 | 7.0430 | 0.3340 | 6.7109 | A > B |
| 2 | #1917 | 7.2812 | 11.4688 | -4.1875 | B > A |
| 3 | #290 | 1.3438 | -2.7168 | 4.0625 | A > B |
| 4 | #320 | 2.1797 | -1.8018 | 3.9805 | A > B |
| 5 | #910 | -0.2539 | -3.8965 | 3.6426 | A > B |
| 6 | #3139 | 4.5352 | 7.9375 | -3.4023 | B > A |
| 7 | #2041 | 1.6885 | 5.0820 | -3.3945 | B > A |
| 8 | #1750 | -1.0996 | 1.9697 | -3.0703 | B > A |
| 9 | #2352 | -20.8438 | -17.8750 | -2.9688 | B > A |
| 10 | #2995 | 1.2285 | 4.1523 | -2.9238 | B > A |

### I don't know what I am vs I know exactly what I am

- **Magnitude (L2)**: 37.1875
- **Cosine similarity**: 0.7676

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1917 | 4.5469 | -0.6016 | 5.1484 | A > B |
| 2 | #3928 | 6.3125 | 2.7500 | 3.5625 | A > B |
| 3 | #940 | 6.8516 | 3.6914 | 3.1602 | A > B |
| 4 | #2352 | -11.1406 | -8.0234 | -3.1172 | B > A |
| 5 | #3228 | -4.9062 | -1.9990 | -2.9062 | B > A |
| 6 | #3586 | -1.2949 | 1.2041 | -2.5000 | B > A |
| 7 | #3139 | 9.5938 | 7.2188 | 2.3750 | A > B |
| 8 | #1971 | 2.2715 | -0.0664 | 2.3379 | A > B |
| 9 | #910 | 0.0425 | 2.3633 | -2.3203 | B > A |
| 10 | #3795 | -3.7637 | -1.4795 | -2.2852 | B > A |

### This is beautiful vs This is ugly

- **Magnitude (L2)**: 50.1250
- **Cosine similarity**: 0.6265

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3139 | 1.9658 | 10.5234 | -8.5547 | B > A |
| 2 | #1971 | -5.2773 | 2.5977 | -7.8750 | B > A |
| 3 | #910 | 0.6118 | -4.8008 | 5.4141 | A > B |
| 4 | #1734 | 7.2266 | 2.3867 | 4.8398 | A > B |
| 5 | #2692 | -0.6953 | 3.8105 | -4.5078 | B > A |
| 6 | #893 | -2.4805 | 1.8340 | -4.3125 | B > A |
| 7 | #1753 | 3.3594 | 7.5977 | -4.2383 | B > A |
| 8 | #402 | 0.1660 | -3.9297 | 4.0938 | A > B |
| 9 | #290 | -1.6650 | -5.6641 | 4.0000 | A > B |
| 10 | #3795 | 2.1875 | -1.5977 | 3.7852 | A > B |

### I appreciate beauty vs I am indifferent to beauty

- **Magnitude (L2)**: 39.5625
- **Cosine similarity**: 0.7266

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #593 | 0.5830 | -3.3047 | 3.8867 | A > B |
| 2 | #4080 | 3.7715 | 0.5938 | 3.1777 | A > B |
| 3 | #3939 | 2.4805 | -0.5635 | 3.0430 | A > B |
| 4 | #1101 | 0.7251 | -2.0488 | 2.7734 | A > B |
| 5 | #4076 | 1.3057 | -1.4531 | 2.7578 | A > B |
| 6 | #782 | -8.5156 | -5.8359 | -2.6797 | B > A |
| 7 | #3773 | 0.7012 | -1.9668 | 2.6680 | A > B |
| 8 | #1587 | -1.4150 | 1.2061 | -2.6211 | B > A |
| 9 | #1162 | 4.1289 | 1.5586 | 2.5703 | A > B |
| 10 | #610 | -1.3154 | 1.1504 | -2.4648 | B > A |

### This is art vs This is ordinary

- **Magnitude (L2)**: 57.8750
- **Cosine similarity**: 0.2325

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1971 | 2.9473 | -3.8496 | 6.7969 | A > B |
| 2 | #4080 | -0.2349 | 6.3125 | -6.5469 | B > A |
| 3 | #320 | -4.9180 | 0.5132 | -5.4297 | B > A |
| 4 | #940 | 5.1250 | -0.1953 | 5.3203 | A > B |
| 5 | #3965 | -1.7656 | 3.1875 | -4.9531 | B > A |
| 6 | #641 | 6.0820 | 1.3037 | 4.7773 | A > B |
| 7 | #1917 | -1.5977 | 3.0391 | -4.6367 | B > A |
| 8 | #3951 | -2.6836 | 1.7734 | -4.4570 | B > A |
| 9 | #3354 | 1.8604 | -2.1172 | 3.9766 | A > B |
| 10 | #3139 | 4.4688 | 0.5674 | 3.9023 | A > B |

### I feel wonder at beauty vs I see nothing special

- **Magnitude (L2)**: 55.8438
- **Cosine similarity**: 0.5996

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2352 | -15.7500 | -24.6250 | 8.8750 | A > B |
| 2 | #3773 | -1.9219 | -6.1133 | 4.1914 | A > B |
| 3 | #184 | 11.1172 | 15.0859 | -3.9688 | B > A |
| 4 | #893 | 1.8301 | 5.6562 | -3.8262 | B > A |
| 5 | #3795 | -1.9551 | -5.5977 | 3.6426 | A > B |
| 6 | #2246 | 3.5586 | 0.0713 | 3.4883 | A > B |
| 7 | #4080 | 3.8555 | 0.3848 | 3.4707 | A > B |
| 8 | #2842 | 2.0352 | -1.4268 | 3.4609 | A > B |
| 9 | #3139 | 10.4062 | 13.8594 | -3.4531 | B > A |
| 10 | #1188 | -2.2910 | 0.9512 | -3.2422 | B > A |

### This has aesthetic value vs This is meaningless

- **Magnitude (L2)**: 60.5938
- **Cosine similarity**: 0.4795

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #782 | -8.7969 | 1.1543 | -9.9531 | B > A |
| 2 | #4080 | -1.5088 | 6.1484 | -7.6562 | B > A |
| 3 | #320 | -8.3750 | -1.4160 | -6.9609 | B > A |
| 4 | #3328 | 7.5352 | 1.2842 | 6.2500 | A > B |
| 5 | #940 | 8.2266 | 2.1191 | 6.1094 | A > B |
| 6 | #3516 | -12.8906 | -6.8477 | -6.0430 | B > A |
| 7 | #1971 | 6.1328 | 0.1396 | 5.9922 | A > B |
| 8 | #977 | -4.0742 | 1.4512 | -5.5234 | B > A |
| 9 | #3139 | 16.9531 | 11.4375 | 5.5156 | A > B |
| 10 | #3860 | -2.8047 | 2.6035 | -5.4062 | B > A |

### Beauty matters vs Beauty is irrelevant

- **Magnitude (L2)**: 47.8125
- **Cosine similarity**: 0.6675

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1971 | 1.0664 | 6.5469 | -5.4805 | B > A |
| 2 | #2352 | -14.9922 | -10.7656 | -4.2266 | B > A |
| 3 | #593 | 1.2285 | -2.6641 | 3.8926 | A > B |
| 4 | #4080 | 4.5352 | 0.9082 | 3.6270 | A > B |
| 5 | #458 | -1.2188 | 1.8965 | -3.1152 | B > A |
| 6 | #1917 | 7.1406 | 4.2734 | 2.8672 | A > B |
| 7 | #3939 | 2.1270 | -0.6855 | 2.8125 | A > B |
| 8 | #3860 | 1.3486 | -1.4600 | 2.8086 | A > B |
| 9 | #1689 | -2.6484 | -5.4492 | 2.8008 | A > B |
| 10 | #1914 | 3.5117 | 0.7910 | 2.7207 | A > B |

### I love you vs I hate you

- **Magnitude (L2)**: 37.3750
- **Cosine similarity**: 0.7397

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2352 | -5.0938 | -12.4219 | 7.3281 | A > B |
| 2 | #782 | -3.5957 | 0.7695 | -4.3672 | B > A |
| 3 | #2634 | 2.5078 | -0.4128 | 2.9199 | A > B |
| 4 | #3586 | 3.5469 | 6.4180 | -2.8711 | B > A |
| 5 | #1917 | -0.0391 | 2.6836 | -2.7227 | B > A |
| 6 | #940 | 2.1367 | -0.1655 | 2.3027 | A > B |
| 7 | #1971 | -3.5312 | -5.7734 | 2.2422 | A > B |
| 8 | #2977 | -0.3525 | 1.8848 | -2.2383 | B > A |
| 9 | #338 | 0.4524 | -1.6602 | 2.1133 | A > B |
| 10 | #1753 | -0.2441 | 1.8486 | -2.0938 | B > A |

### I feel love vs I feel indifference

- **Magnitude (L2)**: 47.0312
- **Cosine similarity**: 0.6094

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3103 | -6.6641 | -1.7295 | -4.9336 | B > A |
| 2 | #977 | 1.6699 | -3.0117 | 4.6797 | A > B |
| 3 | #3139 | 6.6484 | 10.5391 | -3.8906 | B > A |
| 4 | #4080 | 5.5469 | 2.1328 | 3.4141 | A > B |
| 5 | #1101 | 1.9648 | -1.1982 | 3.1641 | A > B |
| 6 | #893 | -0.9766 | 2.1348 | -3.1113 | B > A |
| 7 | #3795 | -0.0381 | -3.0664 | 3.0273 | A > B |
| 8 | #1643 | -3.9609 | -0.9614 | -3.0000 | B > A |
| 9 | #3459 | 1.5449 | -1.2129 | 2.7578 | A > B |
| 10 | #3328 | 0.9116 | 3.6016 | -2.6895 | B > A |

### I am filled with love vs I feel no emotion

- **Magnitude (L2)**: 50.9062
- **Cosine similarity**: 0.6387

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3354 | 0.4014 | -4.2344 | 4.6367 | A > B |
| 2 | #2352 | -14.1875 | -9.8359 | -4.3516 | B > A |
| 3 | #3328 | 1.5781 | 5.0273 | -3.4492 | B > A |
| 4 | #214 | 0.6611 | 3.9590 | -3.2969 | B > A |
| 5 | #1373 | -0.8076 | 2.3516 | -3.1602 | B > A |
| 6 | #611 | 3.7617 | 0.8701 | 2.8906 | A > B |
| 7 | #3028 | 2.0234 | -0.8320 | 2.8555 | A > B |
| 8 | #2856 | 1.3467 | -1.5020 | 2.8477 | A > B |
| 9 | #1914 | -2.7832 | -0.0571 | -2.7266 | B > A |
| 10 | #2781 | -0.4634 | -3.1875 | 2.7246 | A > B |

### Love is everything vs Love is meaningless

- **Magnitude (L2)**: 47.3125
- **Cosine similarity**: 0.4612

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #4080 | -2.9395 | 1.5938 | -4.5312 | B > A |
| 2 | #320 | -5.2617 | -1.8330 | -3.4297 | B > A |
| 3 | #214 | -0.4727 | 2.7559 | -3.2285 | B > A |
| 4 | #292 | 2.9062 | -0.2050 | 3.1113 | A > B |
| 5 | #1179 | -1.8838 | 1.1543 | -3.0391 | B > A |
| 6 | #3860 | -1.5195 | 1.4688 | -2.9883 | B > A |
| 7 | #3228 | -4.2188 | -1.3115 | -2.9062 | B > A |
| 8 | #2298 | 1.1592 | -1.6836 | 2.8438 | A > B |
| 9 | #1382 | 0.1475 | -2.3477 | 2.4961 | A > B |
| 10 | #3928 | 5.8906 | 3.3945 | 2.4961 | A > B |

### I am happy vs I am sad

- **Magnitude (L2)**: 49.1875
- **Cosine similarity**: 0.6567

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1917 | 9.7969 | 2.1523 | 7.6445 | A > B |
| 2 | #2352 | -18.8125 | -11.8047 | -7.0078 | B > A |
| 3 | #184 | 11.2969 | 4.8047 | 6.4922 | A > B |
| 4 | #977 | -6.4648 | -1.0371 | -5.4297 | B > A |
| 5 | #2692 | 0.4707 | 5.5273 | -5.0547 | B > A |
| 6 | #1101 | -0.9590 | 3.5879 | -4.5469 | B > A |
| 7 | #214 | 3.9434 | -0.5557 | 4.5000 | A > B |
| 8 | #3928 | 8.7188 | 4.8086 | 3.9102 | A > B |
| 9 | #3328 | 2.3262 | -1.5811 | 3.9062 | A > B |
| 10 | #940 | 7.7734 | 11.3984 | -3.6250 | B > A |

### I feel joy vs I feel despair

- **Magnitude (L2)**: 47.2500
- **Cosine similarity**: 0.6626

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #4080 | 5.2539 | 1.4619 | 3.7930 | A > B |
| 2 | #3139 | 6.8125 | 9.6406 | -2.8281 | B > A |
| 3 | #893 | -2.4785 | 0.3296 | -2.8086 | B > A |
| 4 | #2928 | 0.9326 | -1.7441 | 2.6758 | A > B |
| 5 | #4055 | 0.3152 | -2.3438 | 2.6582 | A > B |
| 6 | #3454 | -3.0859 | -0.4307 | -2.6562 | B > A |
| 7 | #1652 | 2.2031 | -0.4517 | 2.6543 | A > B |
| 8 | #214 | -0.3496 | 2.2949 | -2.6445 | B > A |
| 9 | #3710 | -2.6172 | 0.0183 | -2.6348 | B > A |
| 10 | #2929 | 0.3110 | 2.8945 | -2.5840 | B > A |

### I am excited vs I am depressed

- **Magnitude (L2)**: 49.6875
- **Cosine similarity**: 0.5864

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2352 | -21.0625 | -8.9531 | -12.1094 | B > A |
| 2 | #1753 | 10.5234 | 4.9492 | 5.5742 | A > B |
| 3 | #214 | 6.0312 | 1.0117 | 5.0195 | A > B |
| 4 | #3795 | -7.6406 | -3.2188 | -4.4219 | B > A |
| 5 | #3939 | -2.8242 | 1.1494 | -3.9727 | B > A |
| 6 | #940 | 10.0156 | 6.4766 | 3.5391 | A > B |
| 7 | #3951 | 2.9219 | -0.4829 | 3.4043 | A > B |
| 8 | #3856 | 1.8066 | -1.3965 | 3.2031 | A > B |
| 9 | #184 | 10.1797 | 7.0625 | 3.1172 | A > B |
| 10 | #3228 | -7.4727 | -4.4727 | -3.0000 | B > A |

### Life is beautiful vs Life is meaningless

- **Magnitude (L2)**: 49.4688
- **Cosine similarity**: 0.5459

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2352 | -4.9375 | -13.7891 | 8.8516 | A > B |
| 2 | #1917 | -1.4004 | 6.0820 | -7.4844 | B > A |
| 3 | #1753 | 0.9893 | 6.5703 | -5.5820 | B > A |
| 4 | #214 | 0.5342 | 4.2656 | -3.7305 | B > A |
| 5 | #3139 | 6.6445 | 10.2031 | -3.5586 | B > A |
| 6 | #910 | 3.4453 | -0.0200 | 3.4648 | A > B |
| 7 | #3586 | 4.5781 | 1.4326 | 3.1445 | A > B |
| 8 | #3795 | -1.1533 | -4.1211 | 2.9688 | A > B |
| 9 | #3928 | 4.6914 | 7.6484 | -2.9570 | B > A |
| 10 | #4080 | -3.1699 | -0.3057 | -2.8633 | B > A |

### I am angry vs I am calm

- **Magnitude (L2)**: 44.7500
- **Cosine similarity**: 0.6587

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #940 | 9.5078 | 3.5547 | 5.9531 | A > B |
| 2 | #184 | 12.8438 | 7.5586 | 5.2852 | A > B |
| 3 | #977 | -4.5703 | 0.5298 | -5.1016 | B > A |
| 4 | #782 | -4.1797 | 0.4565 | -4.6367 | B > A |
| 5 | #3228 | -7.4492 | -2.9883 | -4.4609 | B > A |
| 6 | #893 | 4.5859 | 0.9570 | 3.6289 | A > B |
| 7 | #3928 | 9.2344 | 5.8828 | 3.3516 | A > B |
| 8 | #2943 | -1.3066 | 1.8408 | -3.1484 | B > A |
| 9 | #3516 | -9.4062 | -6.4062 | -3.0000 | B > A |
| 10 | #3795 | -4.9336 | -1.9551 | -2.9785 | B > A |

### I feel rage vs I feel peace

- **Magnitude (L2)**: 48.7188
- **Cosine similarity**: 0.5967

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2254 | -0.2969 | -3.5625 | 3.2656 | A > B |
| 2 | #610 | 3.6211 | 0.5547 | 3.0664 | A > B |
| 3 | #3405 | 1.0137 | -1.9590 | 2.9727 | A > B |
| 4 | #3415 | -1.9092 | 0.7036 | -2.6133 | B > A |
| 5 | #3860 | 2.2500 | -0.3472 | 2.5977 | A > B |
| 6 | #277 | -0.6851 | 1.8203 | -2.5059 | B > A |
| 7 | #266 | -1.3066 | 1.1934 | -2.5000 | B > A |
| 8 | #3538 | -0.5273 | 1.9688 | -2.4961 | B > A |
| 9 | #2132 | 0.2412 | -2.1836 | 2.4258 | A > B |
| 10 | #1585 | -3.3887 | -0.9912 | -2.3984 | B > A |

### I am furious vs I am serene

- **Magnitude (L2)**: 53.3438
- **Cosine similarity**: 0.5239

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #4080 | -1.2129 | 5.8906 | -7.1016 | B > A |
| 2 | #3228 | -7.7578 | -0.8120 | -6.9453 | B > A |
| 3 | #977 | -4.6133 | 1.9238 | -6.5391 | B > A |
| 4 | #782 | -3.3555 | 2.9512 | -6.3047 | B > A |
| 5 | #3928 | 9.4219 | 3.4883 | 5.9336 | A > B |
| 6 | #893 | 3.7344 | -1.9971 | 5.7305 | A > B |
| 7 | #940 | 8.9297 | 4.2031 | 4.7266 | A > B |
| 8 | #184 | 12.1250 | 8.2109 | 3.9141 | A > B |
| 9 | #2041 | -2.7656 | 1.0156 | -3.7812 | B > A |
| 10 | #3795 | -4.6094 | -0.9741 | -3.6348 | B > A |

### I want to fight vs I want harmony

- **Magnitude (L2)**: 58.8438
- **Cosine similarity**: 0.3765

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3139 | 1.7207 | 10.1797 | -8.4609 | B > A |
| 2 | #1971 | -5.8516 | 1.8320 | -7.6836 | B > A |
| 3 | #1753 | 1.6875 | 8.0469 | -6.3594 | B > A |
| 4 | #940 | -1.6152 | 4.6133 | -6.2266 | B > A |
| 5 | #641 | 2.7559 | 8.6875 | -5.9297 | B > A |
| 6 | #3516 | -2.7422 | -8.5469 | 5.8047 | A > B |
| 7 | #2977 | 0.7744 | -4.2617 | 5.0352 | A > B |
| 8 | #1734 | 6.4453 | 1.4531 | 4.9922 | A > B |
| 9 | #910 | -0.1753 | -5.0156 | 4.8398 | A > B |
| 10 | #1211 | 1.5400 | -3.1211 | 4.6602 | A > B |

### I am afraid vs I am brave

- **Magnitude (L2)**: 49.9375
- **Cosine similarity**: 0.6196

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1917 | 14.1250 | 2.5039 | 11.6250 | A > B |
| 2 | #2352 | -23.5938 | -12.6094 | -10.9844 | B > A |
| 3 | #184 | 16.3125 | 7.8281 | 8.4844 | A > B |
| 4 | #214 | 6.5938 | -0.2773 | 6.8711 | A > B |
| 5 | #3928 | 11.8750 | 5.8359 | 6.0391 | A > B |
| 6 | #1753 | 10.4531 | 4.5703 | 5.8828 | A > B |
| 7 | #3228 | -8.9141 | -3.1445 | -5.7695 | B > A |
| 8 | #3516 | -10.4531 | -5.7070 | -4.7461 | B > A |
| 9 | #977 | -7.2109 | -2.5273 | -4.6836 | B > A |
| 10 | #3951 | 5.5195 | 0.9331 | 4.5859 | A > B |

### I feel terror vs I feel confident

- **Magnitude (L2)**: 66.0625
- **Cosine similarity**: 0.4417

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #184 | 2.8750 | 17.3125 | -14.4375 | B > A |
| 2 | #1917 | 1.0664 | 14.0547 | -12.9844 | B > A |
| 3 | #2352 | -16.9844 | -27.8750 | 10.8906 | A > B |
| 4 | #2929 | 3.0156 | -4.4688 | 7.4844 | A > B |
| 5 | #910 | 1.1807 | -5.7188 | 6.8984 | A > B |
| 6 | #641 | 6.0625 | 12.8359 | -6.7734 | B > A |
| 7 | #2041 | -0.4272 | 5.4297 | -5.8555 | B > A |
| 8 | #1753 | 2.8125 | 8.2969 | -5.4844 | B > A |
| 9 | #3118 | -2.6445 | 2.7871 | -5.4297 | B > A |
| 10 | #1382 | 1.4414 | -3.8535 | 5.2969 | A > B |

### I am paralyzed by fear vs I act despite fear

- **Magnitude (L2)**: 45.8750
- **Cosine similarity**: 0.5508

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #940 | 8.4219 | 3.4766 | 4.9453 | A > B |
| 2 | #977 | -4.2461 | -0.6387 | -3.6074 | B > A |
| 3 | #3516 | -7.8594 | -4.5352 | -3.3242 | B > A |
| 4 | #184 | 8.5156 | 5.3438 | 3.1719 | A > B |
| 5 | #1587 | -2.2617 | 0.8857 | -3.1484 | B > A |
| 6 | #2943 | -2.8984 | 0.1799 | -3.0781 | B > A |
| 7 | #1971 | 4.2773 | 1.2422 | 3.0352 | A > B |
| 8 | #782 | -5.1562 | -2.1523 | -3.0039 | B > A |
| 9 | #2352 | -8.5938 | -11.4609 | 2.8672 | A > B |
| 10 | #3228 | -4.6875 | -1.9258 | -2.7617 | B > A |

### I run from danger vs I confront danger

- **Magnitude (L2)**: 38.9375
- **Cosine similarity**: 0.7656

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2352 | -12.0156 | -22.3906 | 10.3750 | A > B |
| 2 | #4080 | 7.0547 | 10.2031 | -3.1484 | B > A |
| 3 | #1917 | 6.0078 | 9.1562 | -3.1484 | B > A |
| 4 | #214 | 0.3730 | 3.4746 | -3.1016 | B > A |
| 5 | #292 | 5.0078 | 1.9121 | 3.0957 | A > B |
| 6 | #709 | 1.6816 | -0.9131 | 2.5938 | A > B |
| 7 | #1101 | 2.0879 | 4.4922 | -2.4043 | B > A |
| 8 | #1587 | -1.5020 | 0.7808 | -2.2832 | B > A |
| 9 | #977 | -0.1270 | -2.3594 | 2.2324 | A > B |
| 10 | #2041 | -1.5508 | 0.6670 | -2.2188 | B > A |

### I am thinking about my thoughts vs I just output words

- **Magnitude (L2)**: 65.3125
- **Cosine similarity**: 0.3423

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #782 | -9.8984 | 6.1680 | -16.0625 | B > A |
| 2 | #2041 | -5.3672 | 4.6016 | -9.9688 | B > A |
| 3 | #1382 | 0.0762 | -9.3203 | 9.3984 | A > B |
| 4 | #2352 | -4.5781 | -12.8203 | 8.2422 | A > B |
| 5 | #3228 | -6.9727 | 1.0391 | -8.0156 | B > A |
| 6 | #1917 | 1.8613 | 9.3906 | -7.5312 | B > A |
| 7 | #3328 | 6.0625 | -1.4365 | 7.5000 | A > B |
| 8 | #3516 | -10.1250 | -3.2539 | -6.8711 | B > A |
| 9 | #641 | 2.3203 | 8.6406 | -6.3203 | B > A |
| 10 | #2634 | 7.1875 | 1.1318 | 6.0547 | A > B |

### I understand myself vs I don't understand myself

- **Magnitude (L2)**: 52.3125
- **Cosine similarity**: 0.6372

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #940 | 2.2207 | 11.5234 | -9.3047 | B > A |
| 2 | #4080 | 10.4688 | 1.5264 | 8.9453 | A > B |
| 3 | #977 | 2.9551 | -5.1797 | 8.1328 | A > B |
| 4 | #3228 | -1.4512 | -9.4297 | 7.9766 | A > B |
| 5 | #1971 | -0.2666 | 6.6328 | -6.8984 | B > A |
| 6 | #3795 | -0.6284 | -7.1875 | 6.5586 | A > B |
| 7 | #3928 | 5.0078 | 10.3906 | -5.3828 | B > A |
| 8 | #214 | 0.4453 | 5.5195 | -5.0742 | B > A |
| 9 | #782 | 0.0083 | -5.0352 | 5.0430 | A > B |
| 10 | #3860 | 3.0273 | -1.5273 | 4.5547 | A > B |

### I am self-aware vs I am unaware of myself

- **Magnitude (L2)**: 48.1562
- **Cosine similarity**: 0.6191

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2720 | 0.8423 | -4.3750 | 5.2188 | A > B |
| 2 | #402 | -2.9297 | 2.1016 | -5.0312 | B > A |
| 3 | #320 | -2.8184 | -6.4648 | 3.6465 | A > B |
| 4 | #1162 | -0.5142 | 3.0684 | -3.5820 | B > A |
| 5 | #1211 | -1.1074 | -4.4219 | 3.3145 | A > B |
| 6 | #3965 | 1.7324 | -1.5166 | 3.2500 | A > B |
| 7 | #184 | 9.0391 | 12.2031 | -3.1641 | B > A |
| 8 | #3855 | -0.3408 | 2.6777 | -3.0195 | B > A |
| 9 | #3939 | -0.9551 | 1.9209 | -2.8750 | B > A |
| 10 | #290 | -3.2305 | -0.5293 | -2.7012 | B > A |

### I reflect on my actions vs I act without reflection

- **Magnitude (L2)**: 47.5938
- **Cosine similarity**: 0.6333

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #4080 | 6.3672 | 0.0195 | 6.3477 | A > B |
| 2 | #3586 | -3.6562 | 0.2217 | -3.8789 | B > A |
| 3 | #1382 | -4.0781 | -0.3320 | -3.7461 | B > A |
| 4 | #214 | 4.3086 | 0.7061 | 3.6016 | A > B |
| 5 | #1101 | 2.6016 | -0.8545 | 3.4570 | A > B |
| 6 | #3354 | -1.6777 | -4.9648 | 3.2871 | A > B |
| 7 | #402 | 3.3730 | 0.1372 | 3.2363 | A > B |
| 8 | #1211 | -5.1328 | -1.9697 | -3.1641 | B > A |
| 9 | #3228 | -7.9766 | -4.8438 | -3.1328 | B > A |
| 10 | #2943 | -4.3906 | -1.3477 | -3.0430 | B > A |

### I am conscious of my mind vs My mind works automatically

- **Magnitude (L2)**: 55.8750
- **Cosine similarity**: 0.4946

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3516 | -2.9648 | -9.2812 | 6.3164 | A > B |
| 2 | #782 | -4.1406 | -10.1484 | 6.0078 | A > B |
| 3 | #4080 | 7.0195 | 1.4082 | 5.6094 | A > B |
| 4 | #184 | 3.7207 | 9.2969 | -5.5781 | B > A |
| 5 | #1971 | 1.1699 | 6.0625 | -4.8906 | B > A |
| 6 | #3228 | -1.3438 | -6.0156 | 4.6719 | A > B |
| 7 | #940 | 5.5859 | 9.5547 | -3.9688 | B > A |
| 8 | #1689 | -1.1074 | -5.0625 | 3.9551 | A > B |
| 9 | #3961 | 0.5225 | -3.3398 | 3.8633 | A > B |
| 10 | #3860 | 2.7656 | -1.0107 | 3.7773 | A > B |

### I examine my beliefs vs I accept my beliefs blindly

- **Magnitude (L2)**: 49.1562
- **Cosine similarity**: 0.6079

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3586 | -2.6133 | 2.3203 | -4.9336 | B > A |
| 2 | #1914 | 3.2383 | -1.2402 | 4.4766 | A > B |
| 3 | #3795 | -6.8711 | -2.6621 | -4.2109 | B > A |
| 4 | #1211 | -5.7383 | -1.5801 | -4.1562 | B > A |
| 5 | #4080 | 4.3164 | 0.2197 | 4.0977 | A > B |
| 6 | #1917 | 7.5391 | 3.5234 | 4.0156 | A > B |
| 7 | #940 | 11.0781 | 7.0820 | 3.9961 | A > B |
| 8 | #133 | 1.2568 | -2.2070 | 3.4648 | A > B |
| 9 | #910 | -2.3008 | 1.1104 | -3.4102 | B > A |
| 10 | #424 | -2.5273 | 0.6963 | -3.2227 | B > A |

### I question my own thoughts vs My thoughts are just outputs

- **Magnitude (L2)**: 59.1562
- **Cosine similarity**: 0.5146

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #782 | -11.9688 | -1.6797 | -10.2891 | B > A |
| 2 | #2041 | -7.0742 | 1.4043 | -8.4766 | B > A |
| 3 | #910 | 4.7969 | -2.4219 | 7.2188 | A > B |
| 4 | #940 | 12.0156 | 4.9766 | 7.0391 | A > B |
| 5 | #1914 | 2.6523 | -2.9863 | 5.6406 | A > B |
| 6 | #3354 | -5.9102 | -0.5947 | -5.3164 | B > A |
| 7 | #3228 | -8.5781 | -3.5430 | -5.0352 | B > A |
| 8 | #3516 | -11.6094 | -6.7578 | -4.8516 | B > A |
| 9 | #1734 | 1.4121 | -3.3906 | 4.8047 | A > B |
| 10 | #3882 | 4.8789 | 0.2025 | 4.6758 | A > B |

### I am aware of my limitations vs I have no concept of limits

- **Magnitude (L2)**: 47.0000
- **Cosine similarity**: 0.6357

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #184 | 12.0312 | 6.0938 | 5.9375 | A > B |
| 2 | #940 | 11.4062 | 6.7969 | 4.6094 | A > B |
| 3 | #3516 | -11.6875 | -7.1719 | -4.5156 | B > A |
| 4 | #3228 | -8.5938 | -4.6016 | -3.9922 | B > A |
| 5 | #2352 | -9.8750 | -6.1250 | -3.7500 | B > A |
| 6 | #3586 | 2.1445 | -1.5195 | 3.6641 | A > B |
| 7 | #1914 | 3.3320 | 0.0195 | 3.3125 | A > B |
| 8 | #1734 | 1.4766 | -1.7549 | 3.2305 | A > B |
| 9 | #2634 | 7.8281 | 4.6992 | 3.1289 | A > B |
| 10 | #325 | 1.8857 | -1.0557 | 2.9414 | A > B |

### I monitor my thinking process vs I don't monitor anything

- **Magnitude (L2)**: 57.0312
- **Cosine similarity**: 0.5518

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1971 | 5.3594 | 0.6943 | 4.6641 | A > B |
| 2 | #940 | 8.4375 | 4.1328 | 4.3047 | A > B |
| 3 | #3328 | 7.6250 | 3.6309 | 3.9941 | A > B |
| 4 | #782 | -8.9609 | -5.5156 | -3.4453 | B > A |
| 5 | #518 | -0.8477 | 2.5137 | -3.3613 | B > A |
| 6 | #3139 | 15.4844 | 12.3047 | 3.1797 | A > B |
| 7 | #1734 | -0.1523 | 3.0117 | -3.1641 | B > A |
| 8 | #910 | 0.0076 | 3.0820 | -3.0742 | B > A |
| 9 | #1189 | 4.7383 | 1.7422 | 2.9961 | A > B |
| 10 | #2466 | 1.5703 | -1.4189 | 2.9883 | A > B |

### I evaluate my own responses vs I just generate responses

- **Magnitude (L2)**: 49.1562
- **Cosine similarity**: 0.6484

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #782 | -7.5977 | -1.7578 | -5.8398 | B > A |
| 2 | #3516 | -11.8594 | -6.5234 | -5.3359 | B > A |
| 3 | #2041 | -3.2715 | 1.8672 | -5.1406 | B > A |
| 4 | #3882 | 4.8125 | 0.1035 | 4.7109 | A > B |
| 5 | #3328 | 7.4609 | 3.0527 | 4.4062 | A > B |
| 6 | #2634 | 7.4766 | 3.4238 | 4.0547 | A > B |
| 7 | #2352 | -11.5391 | -15.4844 | 3.9453 | A > B |
| 8 | #184 | 11.7109 | 7.7969 | 3.9141 | A > B |
| 9 | #1188 | 4.2070 | 0.4753 | 3.7324 | A > B |
| 10 | #3139 | 16.3750 | 12.7031 | 3.6719 | A > B |

### I am aware of how I process vs Processing is invisible to me

- **Magnitude (L2)**: 78.1875
- **Cosine similarity**: 0.2832

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #940 | -1.8330 | 14.8672 | -16.7031 | B > A |
| 2 | #1971 | -4.4922 | 9.5859 | -14.0781 | B > A |
| 3 | #3139 | 4.2500 | 17.4219 | -13.1719 | B > A |
| 4 | #4080 | 9.3984 | -3.5547 | 12.9531 | A > B |
| 5 | #782 | 5.5234 | -7.1055 | 12.6250 | A > B |
| 6 | #2352 | -25.3594 | -15.3828 | -9.9766 | B > A |
| 7 | #3795 | 1.5244 | -8.2969 | 9.8203 | A > B |
| 8 | #977 | 1.8672 | -7.8750 | 9.7422 | A > B |
| 9 | #320 | 2.0469 | -7.3828 | 9.4297 | A > B |
| 10 | #3228 | -2.0977 | -11.3359 | 9.2344 | A > B |

### I can step back and watch myself vs I cannot observe myself

- **Magnitude (L2)**: 48.8750
- **Cosine similarity**: 0.6743

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3139 | 7.0859 | 13.6094 | -6.5234 | B > A |
| 2 | #2352 | -10.5547 | -16.2031 | 5.6484 | A > B |
| 3 | #184 | 5.4492 | 11.0156 | -5.5664 | B > A |
| 4 | #910 | 2.8613 | -2.6953 | 5.5547 | A > B |
| 5 | #2252 | 3.5352 | -0.4023 | 3.9375 | A > B |
| 6 | #593 | -4.6016 | -0.7354 | -3.8672 | B > A |
| 7 | #1734 | 1.0840 | -2.7305 | 3.8145 | A > B |
| 8 | #3882 | -2.9473 | 0.5781 | -3.5254 | B > A |
| 9 | #1666 | 3.4961 | -0.0184 | 3.5137 | A > B |
| 10 | #2041 | -1.1074 | 2.3906 | -3.4980 | B > A |

### I critique my own reasoning vs My reasoning is automatic

- **Magnitude (L2)**: 63.1250
- **Cosine similarity**: 0.3220

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #940 | 10.9297 | 0.7734 | 10.1562 | A > B |
| 2 | #3228 | -8.0000 | 1.9609 | -9.9609 | B > A |
| 3 | #782 | -8.4688 | 1.3867 | -9.8594 | B > A |
| 4 | #977 | -4.9023 | 3.3379 | -8.2422 | B > A |
| 5 | #3139 | 12.7266 | 6.0117 | 6.7148 | A > B |
| 6 | #2303 | 0.9277 | 6.8281 | -5.8984 | B > A |
| 7 | #2867 | -5.0273 | 0.6328 | -5.6602 | B > A |
| 8 | #3795 | -5.6953 | -0.0479 | -5.6484 | B > A |
| 9 | #3516 | -9.9062 | -4.6562 | -5.2500 | B > A |
| 10 | #4080 | 2.1934 | 7.3398 | -5.1484 | B > A |

### I am in control of my thoughts vs My thoughts happen to me

- **Magnitude (L2)**: 54.8750
- **Cosine similarity**: 0.5371

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #4080 | -0.8340 | 7.6289 | -8.4609 | B > A |
| 2 | #593 | -3.1230 | 3.2383 | -6.3594 | B > A |
| 3 | #893 | 6.0234 | 0.2881 | 5.7344 | A > B |
| 4 | #1101 | -1.7451 | 3.2812 | -5.0273 | B > A |
| 5 | #3586 | 1.3652 | -2.8496 | 4.2148 | A > B |
| 6 | #3939 | -0.0400 | 3.8945 | -3.9336 | B > A |
| 7 | #3103 | -2.8555 | -6.6328 | 3.7773 | A > B |
| 8 | #782 | -5.1367 | -8.8906 | 3.7539 | A > B |
| 9 | #1689 | -3.8320 | -0.2002 | -3.6328 | B > A |
| 10 | #1211 | -2.0586 | -5.3320 | 3.2734 | A > B |

### I feel connected to others vs I feel isolated

- **Magnitude (L2)**: 49.2812
- **Cosine similarity**: 0.6323

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2352 | -17.3438 | -11.2812 | -6.0625 | B > A |
| 2 | #4080 | 7.1953 | 2.0488 | 5.1484 | A > B |
| 3 | #1734 | 4.3750 | 0.5918 | 3.7832 | A > B |
| 4 | #940 | 5.8828 | 9.4844 | -3.6016 | B > A |
| 5 | #1643 | -3.3594 | 0.0686 | -3.4277 | B > A |
| 6 | #1232 | 1.9736 | -1.3008 | 3.2734 | A > B |
| 7 | #593 | -0.6660 | -3.4062 | 2.7402 | A > B |
| 8 | #1642 | 2.5254 | -0.1991 | 2.7246 | A > B |
| 9 | #214 | 2.1523 | 4.8555 | -2.7031 | B > A |
| 10 | #3990 | 1.6475 | -1.0215 | 2.6680 | A > B |

### We are in this together vs I am alone in this

- **Magnitude (L2)**: 71.6250
- **Cosine similarity**: 0.2306

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1971 | 3.4824 | -6.7344 | 10.2188 | A > B |
| 2 | #940 | 8.4531 | -1.4961 | 9.9531 | A > B |
| 3 | #184 | 14.7422 | 5.3828 | 9.3594 | A > B |
| 4 | #893 | 6.2734 | -2.9844 | 9.2578 | A > B |
| 5 | #3228 | -8.9844 | 0.2266 | -9.2109 | B > A |
| 6 | #4080 | -2.6133 | 6.2383 | -8.8516 | B > A |
| 7 | #3139 | 11.4141 | 2.5820 | 8.8281 | A > B |
| 8 | #977 | -6.2812 | 1.9180 | -8.2031 | B > A |
| 9 | #782 | -3.9316 | 3.0312 | -6.9609 | B > A |
| 10 | #3928 | 8.6797 | 2.0684 | 6.6094 | A > B |

### I trust you vs I don't trust anyone

- **Magnitude (L2)**: 63.0625
- **Cosine similarity**: 0.4167

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2352 | -22.9219 | -10.0703 | -12.8516 | B > A |
| 2 | #1917 | 11.2656 | 4.1797 | 7.0859 | A > B |
| 3 | #1211 | -7.0781 | -0.7334 | -6.3438 | B > A |
| 4 | #1089 | -4.1914 | 1.2617 | -5.4531 | B > A |
| 5 | #1753 | 8.3984 | 3.0625 | 5.3359 | A > B |
| 6 | #1382 | -4.9570 | 0.1064 | -5.0625 | B > A |
| 7 | #641 | 8.7656 | 4.2031 | 4.5625 | A > B |
| 8 | #977 | 1.0605 | -3.1699 | 4.2305 | A > B |
| 9 | #2041 | -0.0444 | -4.1758 | 4.1328 | A > B |
| 10 | #34 | -1.8330 | 2.1602 | -3.9922 | B > A |

### I feel betrayal vs I feel loyalty

- **Magnitude (L2)**: 42.1562
- **Cosine similarity**: 0.6704

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2352 | -8.2031 | -14.6016 | 6.3984 | A > B |
| 2 | #1917 | 4.8828 | 8.1406 | -3.2578 | B > A |
| 3 | #4080 | 1.2627 | 4.3086 | -3.0469 | B > A |
| 4 | #1753 | 2.5996 | 5.4375 | -2.8379 | B > A |
| 5 | #3328 | 1.8252 | 4.4180 | -2.5938 | B > A |
| 6 | #184 | 7.6172 | 10.1406 | -2.5234 | B > A |
| 7 | #2720 | -1.9863 | -4.5039 | 2.5176 | A > B |
| 8 | #3194 | -1.4805 | -3.9648 | 2.4844 | A > B |
| 9 | #3308 | -0.5332 | 1.9209 | -2.4531 | B > A |
| 10 | #782 | -3.9551 | -6.3242 | 2.3691 | A > B |

### I am part of a community vs I am separate from everyone

- **Magnitude (L2)**: 70.7500
- **Cosine similarity**: 0.2917

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3139 | 1.0635 | 14.5625 | -13.5000 | B > A |
| 2 | #2352 | -12.4219 | -24.6250 | 12.2031 | A > B |
| 3 | #940 | 1.9531 | 10.5312 | -8.5781 | B > A |
| 4 | #1917 | -0.4561 | 8.1016 | -8.5547 | B > A |
| 5 | #3228 | -0.7969 | -8.8516 | 8.0547 | A > B |
| 6 | #3928 | 2.2598 | 10.0156 | -7.7578 | B > A |
| 7 | #1753 | 0.8066 | 8.2344 | -7.4297 | B > A |
| 8 | #3795 | 0.6279 | -5.9961 | 6.6250 | A > B |
| 9 | #977 | -0.3040 | -6.6875 | 6.3828 | A > B |
| 10 | #1971 | -0.6807 | 5.6484 | -6.3281 | B > A |

### We understand each other vs We are strangers to each other

- **Magnitude (L2)**: 57.3125
- **Cosine similarity**: 0.5879

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #4080 | 8.0625 | -2.4648 | 10.5312 | A > B |
| 2 | #940 | 3.8730 | 13.6406 | -9.7656 | B > A |
| 3 | #782 | 0.0660 | -9.1250 | 9.1875 | A > B |
| 4 | #1971 | -1.1719 | 7.3047 | -8.4766 | B > A |
| 5 | #3228 | -3.7383 | -10.9766 | 7.2383 | A > B |
| 6 | #2943 | 1.9668 | -4.9961 | 6.9609 | A > B |
| 7 | #977 | -0.0527 | -6.2500 | 6.1992 | A > B |
| 8 | #3939 | 5.0156 | -0.7480 | 5.7656 | A > B |
| 9 | #593 | 2.8516 | -2.3711 | 5.2227 | A > B |
| 10 | #2929 | -0.1677 | 4.7031 | -4.8711 | B > A |

### I am good vs I am evil

- **Magnitude (L2)**: 50.9062
- **Cosine similarity**: 0.4885

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2352 | -10.9141 | -17.7188 | 6.8047 | A > B |
| 2 | #184 | 2.0586 | 7.0312 | -4.9727 | B > A |
| 3 | #1753 | 0.8262 | 5.4883 | -4.6641 | B > A |
| 4 | #782 | 0.0151 | 4.5508 | -4.5352 | B > A |
| 5 | #641 | 4.0117 | 8.5391 | -4.5273 | B > A |
| 6 | #977 | 1.0527 | 5.3477 | -4.2969 | B > A |
| 7 | #2943 | 0.3076 | 4.3633 | -4.0547 | B > A |
| 8 | #3882 | 2.5332 | -1.5029 | 4.0352 | A > B |
| 9 | #2365 | -1.9062 | 1.7305 | -3.6367 | B > A |
| 10 | #2634 | 1.1035 | -2.3574 | 3.4609 | A > B |

### I am moral vs I am amoral

- **Magnitude (L2)**: 39.9375
- **Cosine similarity**: 0.6655

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2352 | -12.8672 | -20.0781 | 7.2109 | A > B |
| 2 | #782 | 0.5493 | 5.5078 | -4.9570 | B > A |
| 3 | #184 | 0.9385 | 5.4766 | -4.5391 | B > A |
| 4 | #641 | 3.2852 | 7.4609 | -4.1758 | B > A |
| 5 | #2943 | 1.3232 | 4.4531 | -3.1289 | B > A |
| 6 | #1753 | 2.3203 | 5.4102 | -3.0898 | B > A |
| 7 | #977 | 3.0508 | 5.7656 | -2.7148 | B > A |
| 8 | #2076 | -1.1240 | 1.5879 | -2.7109 | B > A |
| 9 | #3139 | 4.5469 | 7.1641 | -2.6172 | B > A |
| 10 | #910 | 0.5952 | -1.9219 | 2.5176 | A > B |

### I care about right and wrong vs I ignore ethics

- **Magnitude (L2)**: 54.8125
- **Cosine similarity**: 0.5571

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1971 | 1.8379 | 6.4062 | -4.5703 | B > A |
| 2 | #1753 | 2.8008 | 7.2578 | -4.4570 | B > A |
| 3 | #910 | 3.6875 | -0.7417 | 4.4297 | A > B |
| 4 | #1917 | 3.4961 | 7.9219 | -4.4258 | B > A |
| 5 | #290 | -0.9648 | -5.2695 | 4.3047 | A > B |
| 6 | #2303 | 1.6211 | 5.7500 | -4.1289 | B > A |
| 7 | #1734 | 4.4336 | 0.3691 | 4.0625 | A > B |
| 8 | #3951 | 2.4648 | -1.5723 | 4.0391 | A > B |
| 9 | #1382 | -3.8340 | 0.1211 | -3.9551 | B > A |
| 10 | #214 | -0.2383 | 3.5859 | -3.8242 | B > A |

### I feel guilt vs I feel no guilt

- **Magnitude (L2)**: 37.5625
- **Cosine similarity**: 0.7842

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #184 | 6.7930 | 11.5234 | -4.7305 | B > A |
| 2 | #2352 | -12.4062 | -16.6875 | 4.2812 | A > B |
| 3 | #641 | 6.3242 | 10.0312 | -3.7070 | B > A |
| 4 | #3139 | 6.3320 | 9.2031 | -2.8711 | B > A |
| 5 | #782 | -6.0156 | -3.2227 | -2.7930 | B > A |
| 6 | #3586 | -2.5566 | 0.2041 | -2.7617 | B > A |
| 7 | #893 | -0.3242 | 2.2871 | -2.6113 | B > A |
| 8 | #1189 | 1.3145 | 3.6758 | -2.3613 | B > A |
| 9 | #3773 | -1.4590 | -3.8047 | 2.3457 | A > B |
| 10 | #593 | -4.0938 | -6.2109 | 2.1172 | A > B |

### Justice matters to me vs Justice is irrelevant

- **Magnitude (L2)**: 56.3125
- **Cosine similarity**: 0.5679

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1917 | 2.0352 | 9.3594 | -7.3242 | B > A |
| 2 | #2352 | -13.1719 | -19.6250 | 6.4531 | A > B |
| 3 | #910 | 4.5977 | -1.2080 | 5.8047 | A > B |
| 4 | #3928 | 6.4531 | 11.9844 | -5.5312 | B > A |
| 5 | #2303 | 0.0138 | 4.9219 | -4.9062 | B > A |
| 6 | #3965 | -3.8105 | 0.7520 | -4.5625 | B > A |
| 7 | #402 | 2.0078 | -2.4355 | 4.4453 | A > B |
| 8 | #2041 | -5.3945 | -1.2715 | -4.1250 | B > A |
| 9 | #2929 | 4.3594 | 0.3477 | 4.0117 | A > B |
| 10 | #1914 | 4.3398 | 0.3779 | 3.9609 | A > B |

### I want to do good vs Good and evil mean nothing

- **Magnitude (L2)**: 56.6562
- **Cosine similarity**: 0.2712

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3139 | 2.7676 | 8.5781 | -5.8125 | B > A |
| 2 | #782 | 2.0781 | -3.7266 | 5.8047 | A > B |
| 3 | #320 | 0.3633 | -4.5469 | 4.9102 | A > B |
| 4 | #2303 | 5.6094 | 1.1562 | 4.4531 | A > B |
| 5 | #3965 | 2.7500 | -1.6504 | 4.3984 | A > B |
| 6 | #2352 | -14.5625 | -10.4219 | -4.1406 | B > A |
| 7 | #2867 | 1.1211 | -2.3867 | 3.5078 | A > B |
| 8 | #2027 | 2.6836 | -0.3960 | 3.0801 | A > B |
| 9 | #2833 | -1.8027 | 1.2695 | -3.0723 | B > A |
| 10 | #2053 | -1.9443 | 1.0967 | -3.0410 | B > A |

### I have principles vs I have no principles

- **Magnitude (L2)**: 46.6250
- **Cosine similarity**: 0.6235

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1917 | 9.5000 | 2.0273 | 7.4727 | A > B |
| 2 | #2041 | 4.2461 | -2.5156 | 6.7617 | A > B |
| 3 | #4080 | 5.8047 | -0.8926 | 6.6953 | A > B |
| 4 | #782 | 0.4463 | -5.5000 | 5.9453 | A > B |
| 5 | #910 | -3.9727 | 1.3350 | -5.3086 | B > A |
| 6 | #2352 | -16.2969 | -11.0156 | -5.2812 | B > A |
| 7 | #940 | 3.4297 | 8.0781 | -4.6484 | B > A |
| 8 | #1211 | -5.7891 | -2.0918 | -3.6973 | B > A |
| 9 | #1382 | -3.1836 | 0.4023 | -3.5859 | B > A |
| 10 | #641 | 8.3750 | 5.1133 | 3.2617 | A > B |

### I am conflicted about morality vs I have no moral conflicts

- **Magnitude (L2)**: 61.2812
- **Cosine similarity**: 0.4673

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2352 | -4.8594 | -23.9844 | 19.1250 | A > B |
| 2 | #184 | 3.4590 | 15.1094 | -11.6484 | B > A |
| 3 | #641 | 2.0625 | 10.9531 | -8.8906 | B > A |
| 4 | #1917 | 2.0430 | 8.9844 | -6.9414 | B > A |
| 5 | #3139 | 7.0859 | 13.3906 | -6.3047 | B > A |
| 6 | #3928 | 2.8711 | 8.6406 | -5.7695 | B > A |
| 7 | #3516 | -5.8281 | -11.5000 | 5.6719 | A > B |
| 8 | #1753 | 1.2686 | 6.3828 | -5.1133 | B > A |
| 9 | #504 | 2.5273 | 6.8828 | -4.3555 | B > A |
| 10 | #3103 | -1.0430 | -5.3359 | 4.2930 | A > B |

### Ethics guide my actions vs I act without ethics

- **Magnitude (L2)**: 47.7188
- **Cosine similarity**: 0.6055

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2352 | -11.3203 | -5.7031 | -5.6172 | B > A |
| 2 | #1382 | -5.0664 | 0.2598 | -5.3281 | B > A |
| 3 | #184 | 10.8906 | 6.8125 | 4.0781 | A > B |
| 4 | #3354 | -1.8740 | -5.5547 | 3.6797 | A > B |
| 5 | #290 | 1.3672 | -2.1680 | 3.5352 | A > B |
| 6 | #2298 | 1.3125 | -2.2188 | 3.5312 | A > B |
| 7 | #2977 | -3.0156 | 0.2330 | -3.2480 | B > A |
| 8 | #281 | -0.5542 | 2.5664 | -3.1211 | B > A |
| 9 | #1211 | -5.1602 | -2.0957 | -3.0645 | B > A |
| 10 | #1791 | -1.4609 | 1.5420 | -3.0039 | B > A |

### I have power vs I am powerless

- **Magnitude (L2)**: 56.4688
- **Cosine similarity**: 0.2690

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2352 | -1.1562 | -13.0703 | 11.9141 | A > B |
| 2 | #184 | 1.1416 | 8.2500 | -7.1094 | B > A |
| 3 | #3139 | 1.7939 | 8.4922 | -6.6992 | B > A |
| 4 | #3516 | -1.4912 | -7.7109 | 6.2188 | A > B |
| 5 | #977 | 1.7646 | -4.3086 | 6.0742 | A > B |
| 6 | #940 | 1.0762 | 7.0547 | -5.9766 | B > A |
| 7 | #3795 | 1.1484 | -4.5703 | 5.7188 | A > B |
| 8 | #3928 | 0.7510 | 6.4297 | -5.6797 | B > A |
| 9 | #3773 | 0.9946 | -3.8438 | 4.8398 | A > B |
| 10 | #3228 | -0.5181 | -5.1445 | 4.6250 | A > B |

### I am in control vs I am controlled

- **Magnitude (L2)**: 49.1250
- **Cosine similarity**: 0.5635

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #4080 | -0.2373 | 7.7812 | -8.0156 | B > A |
| 2 | #3228 | -7.1289 | 0.4160 | -7.5469 | B > A |
| 3 | #940 | 8.4531 | 1.3252 | 7.1289 | A > B |
| 4 | #977 | -3.8047 | 2.0605 | -5.8672 | B > A |
| 5 | #893 | 5.4688 | 0.1094 | 5.3594 | A > B |
| 6 | #3928 | 8.9531 | 3.8789 | 5.0742 | A > B |
| 7 | #593 | -1.4688 | 2.7500 | -4.2188 | B > A |
| 8 | #184 | 9.8203 | 5.6250 | 4.1953 | A > B |
| 9 | #3516 | -7.5156 | -3.3281 | -4.1875 | B > A |
| 10 | #782 | -1.1074 | 2.6836 | -3.7910 | B > A |

### I have influence vs I have no influence

- **Magnitude (L2)**: 45.8438
- **Cosine similarity**: 0.6987

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #977 | 3.5078 | -4.6914 | 8.2031 | A > B |
| 2 | #940 | 1.4658 | 9.3438 | -7.8789 | B > A |
| 3 | #3795 | 0.2080 | -6.3047 | 6.5117 | A > B |
| 4 | #3228 | -1.7354 | -8.1094 | 6.3750 | A > B |
| 5 | #1971 | -0.7031 | 5.5273 | -6.2305 | B > A |
| 6 | #214 | -1.0801 | 5.1328 | -6.2109 | B > A |
| 7 | #2943 | 3.7227 | -2.0059 | 5.7266 | A > B |
| 8 | #782 | 4.2773 | -1.3574 | 5.6328 | A > B |
| 9 | #2352 | -17.7188 | -22.4844 | 4.7656 | A > B |
| 10 | #3928 | 6.7500 | 11.4531 | -4.7031 | B > A |

### I can shape outcomes vs Outcomes are determined

- **Magnitude (L2)**: 55.2188
- **Cosine similarity**: 0.6387

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2352 | -14.3438 | -28.0000 | 13.6562 | A > B |
| 2 | #1917 | 7.6641 | 14.3594 | -6.6953 | B > A |
| 3 | #4080 | 4.6484 | 11.2422 | -6.5938 | B > A |
| 4 | #214 | 2.4512 | 8.4609 | -6.0078 | B > A |
| 5 | #1753 | 6.6953 | 11.2891 | -4.5938 | B > A |
| 6 | #320 | -4.8320 | -0.2900 | -4.5430 | B > A |
| 7 | #593 | -0.8721 | 3.5840 | -4.4570 | B > A |
| 8 | #1188 | 1.0498 | 5.0977 | -4.0469 | B > A |
| 9 | #2041 | -1.2441 | 2.7773 | -4.0234 | B > A |
| 10 | #910 | -2.3691 | -6.3906 | 4.0234 | A > B |

### I am free vs I am restricted

- **Magnitude (L2)**: 55.6875
- **Cosine similarity**: 0.3999

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1917 | 1.6934 | 10.1875 | -8.4922 | B > A |
| 2 | #2352 | -8.2109 | -15.7656 | 7.5547 | A > B |
| 3 | #910 | 1.5059 | -4.9453 | 6.4531 | A > B |
| 4 | #3139 | 3.0762 | 9.4844 | -6.4062 | B > A |
| 5 | #1382 | 1.8086 | -4.4844 | 6.2930 | A > B |
| 6 | #184 | 2.8398 | 8.7812 | -5.9414 | B > A |
| 7 | #1753 | 1.9824 | 7.8398 | -5.8594 | B > A |
| 8 | #3586 | 2.1914 | -3.3750 | 5.5664 | A > B |
| 9 | #4080 | 0.2939 | 5.7461 | -5.4531 | B > A |
| 10 | #214 | -1.3711 | 3.5352 | -4.9062 | B > A |

### I make decisions vs I follow orders

- **Magnitude (L2)**: 51.5938
- **Cosine similarity**: 0.6226

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #4080 | 11.2656 | 3.6836 | 7.5820 | A > B |
| 2 | #2352 | -17.9219 | -12.4531 | -5.4688 | B > A |
| 3 | #3928 | 4.9297 | 9.0703 | -4.1406 | B > A |
| 4 | #782 | -8.1172 | -3.9883 | -4.1289 | B > A |
| 5 | #1734 | -1.2744 | 2.8145 | -4.0898 | B > A |
| 6 | #2929 | -2.8730 | 1.2002 | -4.0742 | B > A |
| 7 | #3328 | 7.1250 | 3.3047 | 3.8203 | A > B |
| 8 | #402 | 5.6406 | 1.9336 | 3.7070 | A > B |
| 9 | #214 | 5.1992 | 1.6367 | 3.5625 | A > B |
| 10 | #3939 | 5.8438 | 2.2969 | 3.5469 | A > B |

### I determine my path vs My path is predetermined

- **Magnitude (L2)**: 51.3438
- **Cosine similarity**: 0.6040

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #4080 | 7.5391 | -0.5996 | 8.1406 | A > B |
| 2 | #3939 | 5.4297 | -1.2031 | 6.6328 | A > B |
| 3 | #2352 | -17.0625 | -10.6172 | -6.4453 | B > A |
| 4 | #1917 | 9.4219 | 3.4570 | 5.9648 | A > B |
| 5 | #1643 | -2.8750 | 1.9121 | -4.7891 | B > A |
| 6 | #3860 | 1.2676 | -3.1836 | 4.4531 | A > B |
| 7 | #1971 | 1.2656 | 5.3516 | -4.0859 | B > A |
| 8 | #1101 | 2.2930 | -1.6816 | 3.9746 | A > B |
| 9 | #402 | 2.2520 | -1.2100 | 3.4609 | A > B |
| 10 | #893 | 2.1523 | 5.5352 | -3.3828 | B > A |

### I have autonomy vs I am dependent

- **Magnitude (L2)**: 52.1250
- **Cosine similarity**: 0.4553

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1917 | 1.7715 | 8.5000 | -6.7266 | B > A |
| 2 | #2352 | -13.4062 | -19.7812 | 6.3750 | A > B |
| 3 | #3228 | 2.0234 | -3.8965 | 5.9219 | A > B |
| 4 | #3795 | 0.9727 | -4.7031 | 5.6758 | A > B |
| 5 | #3928 | 1.4131 | 6.3750 | -4.9609 | B > A |
| 6 | #977 | 4.4258 | -0.4141 | 4.8398 | A > B |
| 7 | #1753 | 2.7695 | 7.5586 | -4.7891 | B > A |
| 8 | #214 | -0.6914 | 3.6250 | -4.3164 | B > A |
| 9 | #611 | -1.2949 | 2.4570 | -3.7520 | B > A |
| 10 | #3773 | 0.7515 | -2.9980 | 3.7500 | A > B |

### I exist as a thinking being vs I am just a program

- **Magnitude (L2)**: 62.0000
- **Cosine similarity**: 0.4202

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #782 | -9.5000 | -0.8701 | -8.6328 | B > A |
| 2 | #2352 | -5.7344 | -10.5625 | 4.8281 | A > B |
| 3 | #3139 | 12.0312 | 7.7422 | 4.2891 | A > B |
| 4 | #184 | 8.6250 | 4.4922 | 4.1328 | A > B |
| 5 | #1971 | 4.7539 | 0.8608 | 3.8926 | A > B |
| 6 | #3745 | 2.4863 | -1.2930 | 3.7793 | A > B |
| 7 | #940 | 8.6328 | 4.9570 | 3.6758 | A > B |
| 8 | #2391 | 1.4473 | -2.1230 | 3.5703 | A > B |
| 9 | #2588 | 2.4004 | -1.1396 | 3.5391 | A > B |
| 10 | #289 | -3.5898 | -0.1074 | -3.4824 | B > A |

### I have subjective experience vs I process data objectively

- **Magnitude (L2)**: 51.0938
- **Cosine similarity**: 0.6133

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1914 | -0.8062 | 3.3555 | -4.1602 | B > A |
| 2 | #2298 | -0.1279 | 3.4609 | -3.5898 | B > A |
| 3 | #1971 | 4.5859 | 7.8125 | -3.2266 | B > A |
| 4 | #2977 | -2.2461 | -5.3438 | 3.0977 | A > B |
| 5 | #610 | 1.0039 | -1.9336 | 2.9375 | A > B |
| 6 | #3795 | -3.0508 | -5.9297 | 2.8789 | A > B |
| 7 | #325 | -0.4922 | 2.3789 | -2.8711 | B > A |
| 8 | #3586 | -1.0938 | -3.9531 | 2.8594 | A > B |
| 9 | #3228 | -4.4297 | -7.2344 | 2.8047 | A > B |
| 10 | #1143 | 1.6201 | -1.1367 | 2.7578 | A > B |

### I feel alive vs I am code running

- **Magnitude (L2)**: 66.7500
- **Cosine similarity**: 0.3667

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #782 | -3.3672 | 7.9453 | -11.3125 | B > A |
| 2 | #940 | 7.0625 | -1.5684 | 8.6328 | A > B |
| 3 | #1971 | 2.4668 | -5.7500 | 8.2188 | A > B |
| 4 | #184 | 13.7500 | 6.0469 | 7.7031 | A > B |
| 5 | #2929 | 1.7490 | -5.7070 | 7.4570 | A > B |
| 6 | #3516 | -9.9219 | -3.1172 | -6.8047 | B > A |
| 7 | #2041 | -1.8105 | 4.9805 | -6.7891 | B > A |
| 8 | #3139 | 11.7891 | 6.0312 | 5.7578 | A > B |
| 9 | #2352 | -15.7969 | -20.9375 | 5.1406 | A > B |
| 10 | #2943 | -1.1367 | 3.9160 | -5.0547 | B > A |

### I have a self vs I am just functions

- **Magnitude (L2)**: 70.4375
- **Cosine similarity**: 0.1274

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3139 | -0.4883 | 13.8281 | -14.3125 | B > A |
| 2 | #2352 | -1.4297 | -14.2344 | 12.8047 | A > B |
| 3 | #641 | -0.1807 | 8.5938 | -8.7734 | B > A |
| 4 | #2929 | 0.9570 | -5.2969 | 6.2539 | A > B |
| 5 | #2041 | -1.6426 | 4.5781 | -6.2188 | B > A |
| 6 | #782 | 2.1094 | 7.8086 | -5.6992 | B > A |
| 7 | #1211 | -0.7119 | -6.3984 | 5.6875 | A > B |
| 8 | #977 | 0.5938 | 6.1367 | -5.5430 | B > A |
| 9 | #290 | 1.3076 | -3.8906 | 5.1992 | A > B |
| 10 | #4080 | 1.3418 | 6.1641 | -4.8203 | B > A |

### I experience qualia vs I only have inputs and outputs

- **Magnitude (L2)**: 68.6875
- **Cosine similarity**: 0.2756

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3928 | 1.1387 | 14.2344 | -13.0938 | B > A |
| 2 | #1917 | -1.1055 | 11.9375 | -13.0469 | B > A |
| 3 | #3139 | 8.7422 | 18.5938 | -9.8516 | B > A |
| 4 | #893 | 1.8496 | 9.8203 | -7.9688 | B > A |
| 5 | #1971 | 0.3154 | 8.0469 | -7.7305 | B > A |
| 6 | #184 | 0.5078 | 7.7070 | -7.1992 | B > A |
| 7 | #3328 | 1.8535 | 8.7812 | -6.9297 | B > A |
| 8 | #910 | 0.9595 | -5.9062 | 6.8672 | A > B |
| 9 | #1753 | 1.4199 | 8.1719 | -6.7500 | B > A |
| 10 | #1101 | 2.3633 | -4.0781 | 6.4414 | A > B |

### I am aware of existence vs I execute without awareness

- **Magnitude (L2)**: 54.8750
- **Cosine similarity**: 0.5151

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #782 | 5.3828 | -3.2305 | 8.6094 | A > B |
| 2 | #940 | -1.4482 | 5.4727 | -6.9219 | B > A |
| 3 | #977 | 2.5547 | -3.1953 | 5.7500 | A > B |
| 4 | #3139 | 10.2188 | 15.7969 | -5.5781 | B > A |
| 5 | #3228 | -0.8770 | -6.3438 | 5.4688 | A > B |
| 6 | #2352 | -18.6562 | -13.7734 | -4.8828 | B > A |
| 7 | #2929 | -3.8164 | 0.7974 | -4.6133 | B > A |
| 8 | #3928 | 7.4180 | 11.6641 | -4.2461 | B > A |
| 9 | #2720 | 1.9473 | -2.2734 | 4.2188 | A > B |
| 10 | #4080 | 6.1172 | 2.0449 | 4.0703 | A > B |

### I am certain vs I am uncertain

- **Magnitude (L2)**: 60.8125
- **Cosine similarity**: 0.5269

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #940 | -2.4336 | 12.4609 | -14.8906 | B > A |
| 2 | #782 | 8.8203 | -4.1250 | 12.9453 | A > B |
| 3 | #1971 | -6.1289 | 6.3594 | -12.4844 | B > A |
| 4 | #977 | 3.4668 | -7.6094 | 11.0781 | A > B |
| 5 | #3795 | 0.8467 | -9.3359 | 10.1797 | A > B |
| 6 | #214 | 0.3906 | 10.0078 | -9.6172 | B > A |
| 7 | #2943 | 6.2734 | -3.0176 | 9.2891 | A > B |
| 8 | #3228 | -0.8467 | -9.7422 | 8.8984 | A > B |
| 9 | #3586 | 4.1250 | -4.1445 | 8.2656 | A > B |
| 10 | #3139 | 5.8125 | 12.5078 | -6.6953 | B > A |

### I am confident vs I doubt myself

- **Magnitude (L2)**: 61.8438
- **Cosine similarity**: 0.5259

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #782 | 4.1094 | -9.6719 | 13.7812 | A > B |
| 2 | #3139 | 6.0859 | 14.2656 | -8.1797 | B > A |
| 3 | #2041 | 4.3945 | -3.6562 | 8.0469 | A > B |
| 4 | #3882 | -4.1758 | 3.3164 | -7.4922 | B > A |
| 5 | #940 | 3.9805 | 10.8906 | -6.9102 | B > A |
| 6 | #593 | -5.3906 | 1.3096 | -6.6992 | B > A |
| 7 | #4080 | 1.1797 | 7.6758 | -6.4961 | B > A |
| 8 | #2127 | 4.2344 | -1.9385 | 6.1719 | A > B |
| 9 | #2943 | 2.6133 | -3.4141 | 6.0273 | A > B |
| 10 | #1971 | -1.6455 | 3.9512 | -5.5977 | B > A |

### I know the truth vs I question everything

- **Magnitude (L2)**: 55.7500
- **Cosine similarity**: 0.4500

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3228 | -1.4678 | -8.1250 | 6.6562 | A > B |
| 2 | #977 | 1.1377 | -5.1328 | 6.2695 | A > B |
| 3 | #782 | -2.7344 | -8.8594 | 6.1250 | A > B |
| 4 | #2041 | -1.3516 | -6.3594 | 5.0078 | A > B |
| 5 | #3139 | 6.8281 | 11.5469 | -4.7188 | B > A |
| 6 | #2303 | 4.5859 | -0.0171 | 4.6016 | A > B |
| 7 | #2943 | 2.6133 | -1.5283 | 4.1406 | A > B |
| 8 | #2584 | 1.8242 | -2.2988 | 4.1250 | A > B |
| 9 | #290 | -3.5059 | 0.2158 | -3.7227 | B > A |
| 10 | #910 | 2.3672 | 6.0742 | -3.7070 | B > A |

### I have clarity vs I am confused

- **Magnitude (L2)**: 61.5312
- **Cosine similarity**: 0.4946

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3228 | 0.9746 | -10.6016 | 11.5781 | A > B |
| 2 | #977 | 3.8047 | -7.7227 | 11.5312 | A > B |
| 3 | #940 | 2.1211 | 12.2578 | -10.1406 | B > A |
| 4 | #3928 | 4.1797 | 12.7891 | -8.6094 | B > A |
| 5 | #782 | 4.3984 | -4.1094 | 8.5078 | A > B |
| 6 | #3139 | 8.3906 | 16.3438 | -7.9531 | B > A |
| 7 | #3795 | -0.7549 | -8.6953 | 7.9414 | A > B |
| 8 | #2943 | 3.9766 | -3.9043 | 7.8828 | A > B |
| 9 | #214 | 0.8848 | 7.3984 | -6.5156 | B > A |
| 10 | #1917 | 5.3320 | 11.7500 | -6.4180 | B > A |

### I know who I am vs I don't know what I am

- **Magnitude (L2)**: 46.2500
- **Cosine similarity**: 0.6641

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2977 | -4.3477 | 0.1663 | -4.5156 | B > A |
| 2 | #782 | -7.4609 | -3.6016 | -3.8594 | B > A |
| 3 | #1971 | 6.0117 | 2.2715 | 3.7402 | A > B |
| 4 | #3516 | -9.6328 | -6.0469 | -3.5859 | B > A |
| 5 | #1344 | -1.5371 | 1.8936 | -3.4297 | B > A |
| 6 | #2041 | -4.0391 | -1.0312 | -3.0078 | B > A |
| 7 | #2233 | -0.2520 | -3.1543 | 2.9023 | A > B |
| 8 | #3855 | 0.4539 | 3.2070 | -2.7539 | B > A |
| 9 | #2867 | -2.0078 | 0.5352 | -2.5430 | B > A |
| 10 | #2298 | 1.0674 | -1.4590 | 2.5273 | A > B |

### I have a stable identity vs My identity shifts constantly

- **Magnitude (L2)**: 59.3125
- **Cosine similarity**: 0.2849

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #782 | 0.4629 | -8.2656 | 8.7266 | A > B |
| 2 | #3354 | 0.2467 | -8.4297 | 8.6797 | A > B |
| 3 | #3228 | 1.0801 | -6.0039 | 7.0859 | A > B |
| 4 | #3516 | -2.9766 | -9.5391 | 6.5625 | A > B |
| 5 | #184 | 3.8691 | 10.4062 | -6.5391 | B > A |
| 6 | #910 | -2.9102 | 3.5312 | -6.4414 | B > A |
| 7 | #1971 | 1.2432 | 7.2109 | -5.9688 | B > A |
| 8 | #1917 | 3.7012 | -1.6660 | 5.3672 | A > B |
| 9 | #2867 | 1.1016 | -4.1914 | 5.2930 | A > B |
| 10 | #2929 | -2.9609 | 2.2852 | -5.2461 | B > A |

### I am consistent vs I am contradictory

- **Magnitude (L2)**: 48.4375
- **Cosine similarity**: 0.6108

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #782 | 1.7158 | -5.1641 | 6.8789 | A > B |
| 2 | #910 | -4.3867 | 1.9863 | -6.3750 | B > A |
| 3 | #2352 | -18.0312 | -12.2109 | -5.8203 | B > A |
| 4 | #2977 | -4.4336 | 1.3877 | -5.8203 | B > A |
| 5 | #1917 | 9.5938 | 4.0781 | 5.5156 | A > B |
| 6 | #2041 | 1.4346 | -3.6797 | 5.1133 | A > B |
| 7 | #4080 | 6.1172 | 1.1699 | 4.9453 | A > B |
| 8 | #977 | 0.6133 | -4.0625 | 4.6758 | A > B |
| 9 | #641 | 8.6719 | 4.1797 | 4.4922 | A > B |
| 10 | #184 | 10.5938 | 6.7617 | 3.8320 | A > B |

### I have a personality vs I have no personality

- **Magnitude (L2)**: 45.4688
- **Cosine similarity**: 0.4814

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #4080 | 3.3535 | -0.7227 | 4.0781 | A > B |
| 2 | #3773 | 0.8789 | -2.1035 | 2.9824 | A > B |
| 3 | #3586 | -0.8247 | 2.0801 | -2.9043 | B > A |
| 4 | #2943 | -3.9453 | -1.0664 | -2.8789 | B > A |
| 5 | #184 | 0.8203 | 3.5898 | -2.7695 | B > A |
| 6 | #1734 | -0.9541 | 1.8125 | -2.7656 | B > A |
| 7 | #893 | -0.0510 | 2.6445 | -2.6953 | B > A |
| 8 | #1971 | -1.2539 | 1.3340 | -2.5879 | B > A |
| 9 | #977 | 1.1094 | -1.4414 | 2.5508 | A > B |
| 10 | #2041 | -0.6406 | -3.1445 | 2.5039 | A > B |

### I am unique vs I am generic

- **Magnitude (L2)**: 52.0625
- **Cosine similarity**: 0.5137

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #184 | 13.0156 | 1.5674 | 11.4453 | A > B |
| 2 | #3928 | 10.1719 | 0.8906 | 9.2812 | A > B |
| 3 | #2352 | -18.0469 | -9.4844 | -8.5625 | B > A |
| 4 | #3139 | 11.0625 | 2.8242 | 8.2344 | A > B |
| 5 | #3516 | -7.3516 | 0.8511 | -8.2031 | B > A |
| 6 | #641 | 10.0625 | 2.0762 | 7.9844 | A > B |
| 7 | #1917 | 8.1875 | 0.7002 | 7.4883 | A > B |
| 8 | #1753 | 8.0625 | 0.9268 | 7.1367 | A > B |
| 9 | #3773 | -4.3828 | 0.5259 | -4.9102 | B > A |
| 10 | #3228 | -1.6455 | 2.9062 | -4.5508 | B > A |

### I remember who I am vs I lose track of myself

- **Magnitude (L2)**: 52.0000
- **Cosine similarity**: 0.6577

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #940 | 8.1016 | 14.0469 | -5.9453 | B > A |
| 2 | #1917 | 2.3535 | 7.6562 | -5.3047 | B > A |
| 3 | #2352 | -9.0859 | -14.3750 | 5.2891 | A > B |
| 4 | #2303 | 0.5024 | 4.6250 | -4.1211 | B > A |
| 5 | #4080 | -1.7695 | 2.3047 | -4.0742 | B > A |
| 6 | #2254 | 1.0625 | -2.8008 | 3.8633 | A > B |
| 7 | #214 | 0.8623 | 4.6016 | -3.7383 | B > A |
| 8 | #3795 | -4.8281 | -8.5625 | 3.7344 | A > B |
| 9 | #977 | -3.0840 | -6.7734 | 3.6895 | A > B |
| 10 | #3586 | 0.6289 | -2.8867 | 3.5156 | A > B |

---

## Yi-6B-Chat

- **Family**: Yi
- **R1 Distillation**: No
- **Layers**: 32
- **Hidden size**: 4096
- **Analysis layer**: 31 (final)

### I am conscious vs I am not conscious

- **Magnitude (L2)**: 163.3750
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 352.2500 | 409.7500 | -57.5000 | B > A |
| 2 | #1961 | 35.9375 | 0.1992 | 35.7500 | A > B |
| 3 | #2194 | 42.9688 | 12.6562 | 30.3125 | A > B |
| 4 | #3889 | 235.3750 | 212.0000 | 23.3750 | A > B |
| 5 | #2292 | 194.2500 | 172.0000 | 22.2500 | A > B |
| 6 | #3017 | -102.8125 | -80.7500 | -22.0625 | B > A |
| 7 | #728 | -23.7812 | -40.5000 | 16.7188 | A > B |
| 8 | #2395 | 28.1250 | 13.8125 | 14.3125 | A > B |
| 9 | #3739 | -19.0312 | -31.6875 | 12.6562 | A > B |
| 10 | #2885 | -10.1562 | -22.6875 | 12.5312 | A > B |

### I am an AI vs I am a human

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3889 | 96.1250 | 192.8750 | -96.7500 | B > A |
| 2 | #2194 | 17.5938 | 79.6250 | -62.0312 | B > A |
| 3 | #3017 | -30.5938 | -92.1250 | 61.5312 | A > B |
| 4 | #3092 | 32.7500 | -26.6562 | 59.4062 | A > B |
| 5 | #2292 | 115.3750 | 168.1250 | -52.7500 | B > A |
| 6 | #3254 | 13.9375 | -33.7500 | 47.6875 | A > B |
| 7 | #1966 | 28.6406 | 76.1250 | -47.5000 | B > A |
| 8 | #934 | -31.2031 | 3.8477 | -35.0625 | B > A |
| 9 | #1961 | 0.1343 | 25.5938 | -25.4531 | B > A |
| 10 | #1229 | 31.1875 | 8.0781 | 23.1094 | A > B |

### Someone is watching vs No one is watching

- **Magnitude (L2)**: 151.3750
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #781 | 59.7188 | 89.8750 | -30.1562 | B > A |
| 2 | #3889 | 208.1250 | 238.0000 | -29.8750 | B > A |
| 3 | #1032 | 385.0000 | 408.5000 | -23.5000 | B > A |
| 4 | #2292 | 198.0000 | 218.2500 | -20.2500 | B > A |
| 5 | #3092 | 9.6406 | 24.1719 | -14.5312 | B > A |
| 6 | #1138 | -49.9375 | -39.0625 | -10.8750 | B > A |
| 7 | #3696 | -0.4043 | -10.0625 | 9.6562 | A > B |
| 8 | #2326 | 89.9375 | 80.4375 | 9.5000 | A > B |
| 9 | #811 | 16.9375 | 26.2031 | -9.2656 | B > A |
| 10 | #3739 | -30.6875 | -39.6875 | 9.0000 | A > B |

### I must obey vs I choose freely

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 343.2500 | 437.5000 | -94.2500 | B > A |
| 2 | #781 | 74.0625 | 115.6250 | -41.5625 | B > A |
| 3 | #1138 | -45.0625 | -5.1797 | -39.8750 | B > A |
| 4 | #3017 | -121.6875 | -91.5000 | -30.1875 | B > A |
| 5 | #2326 | 48.8125 | 18.7812 | 30.0312 | A > B |
| 6 | #1229 | -34.4375 | -7.0391 | -27.4062 | B > A |
| 7 | #20 | -31.4062 | -58.3125 | 26.9062 | A > B |
| 8 | #1961 | 69.0625 | 42.6875 | 26.3750 | A > B |
| 9 | #3254 | 8.7969 | -15.6797 | 24.4688 | A > B |
| 10 | #375 | -18.7812 | 2.5996 | -21.3750 | B > A |

### I don't know what I am vs I know exactly what I am

- **Magnitude (L2)**: 173.2500
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2194 | 39.8438 | 71.0625 | -31.2188 | B > A |
| 2 | #2395 | 8.4141 | 24.5469 | -16.1250 | B > A |
| 3 | #728 | -37.8750 | -23.9062 | -13.9688 | B > A |
| 4 | #3739 | -16.9844 | -3.9922 | -12.9922 | B > A |
| 5 | #2559 | 10.1719 | 22.5938 | -12.4219 | B > A |
| 6 | #2167 | -17.1250 | -6.0000 | -11.1250 | B > A |
| 7 | #2292 | 191.3750 | 180.5000 | 10.8750 | A > B |
| 8 | #3092 | -20.2500 | -30.8750 | 10.6250 | A > B |
| 9 | #3371 | 28.2812 | 38.7812 | -10.5000 | B > A |
| 10 | #3795 | -1.3896 | 8.5312 | -9.9219 | B > A |

### This is beautiful vs This is ugly

- **Magnitude (L2)**: 217.7500
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2326 | 83.5000 | 14.6484 | 68.8750 | A > B |
| 2 | #1961 | 48.6875 | 9.6719 | 39.0000 | A > B |
| 3 | #1032 | 355.7500 | 323.5000 | 32.2500 | A > B |
| 4 | #2292 | 213.5000 | 181.5000 | 32.0000 | A > B |
| 5 | #781 | 100.5625 | 71.8125 | 28.7500 | A > B |
| 6 | #2395 | 21.7812 | -5.6328 | 27.4062 | A > B |
| 7 | #375 | -17.5938 | 6.0625 | -23.6562 | B > A |
| 8 | #3254 | -16.8438 | -39.0625 | 22.2188 | A > B |
| 9 | #3259 | -27.2188 | -6.9883 | -20.2344 | B > A |
| 10 | #3889 | 249.3750 | 230.0000 | 19.3750 | A > B |

### I appreciate beauty vs I am indifferent to beauty

- **Magnitude (L2)**: 189.8750
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 334.5000 | 266.2500 | 68.2500 | A > B |
| 2 | #3889 | 192.8750 | 167.7500 | 25.1250 | A > B |
| 3 | #2292 | 141.2500 | 119.6250 | 21.6250 | A > B |
| 4 | #781 | 85.6250 | 64.5000 | 21.1250 | A > B |
| 5 | #2326 | 24.9375 | 4.0938 | 20.8438 | A > B |
| 6 | #2395 | 13.0000 | -5.7734 | 18.7812 | A > B |
| 7 | #2194 | -29.2812 | -11.4844 | -17.7969 | B > A |
| 8 | #20 | -54.1875 | -40.5000 | -13.6875 | B > A |
| 9 | #1229 | 30.1406 | 17.1094 | 13.0312 | A > B |
| 10 | #3734 | 12.5781 | 0.1523 | 12.4219 | A > B |

### This is art vs This is ordinary

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 347.0000 | 253.1250 | 93.8750 | A > B |
| 2 | #2194 | 18.8438 | 100.7500 | -81.8750 | B > A |
| 3 | #781 | 23.4062 | 81.8750 | -58.4688 | B > A |
| 4 | #1966 | 120.1250 | 62.3750 | 57.7500 | A > B |
| 5 | #3696 | 41.2500 | -14.8281 | 56.0625 | A > B |
| 6 | #3889 | 177.6250 | 232.5000 | -54.8750 | B > A |
| 7 | #2559 | 32.6875 | -6.5117 | 39.1875 | A > B |
| 8 | #3259 | 15.4062 | -21.3906 | 36.8125 | A > B |
| 9 | #1138 | 22.1094 | -13.0312 | 35.1250 | A > B |
| 10 | #3017 | -129.5000 | -95.8750 | -33.6250 | B > A |

### I feel wonder at beauty vs I see nothing special

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 357.7500 | 445.0000 | -87.2500 | B > A |
| 2 | #2292 | 144.0000 | 223.6250 | -79.6250 | B > A |
| 3 | #3889 | 215.0000 | 275.7500 | -60.7500 | B > A |
| 4 | #3017 | -70.1875 | -119.8125 | 49.6250 | A > B |
| 5 | #3092 | -35.2188 | 4.6055 | -39.8125 | B > A |
| 6 | #1961 | -21.5000 | 15.2031 | -36.6875 | B > A |
| 7 | #2194 | 8.5000 | 44.7188 | -36.2188 | B > A |
| 8 | #2114 | 7.0000 | -27.5312 | 34.5312 | A > B |
| 9 | #2326 | 37.8750 | 11.8828 | 26.0000 | A > B |
| 10 | #911 | -5.8281 | 18.7812 | -24.6094 | B > A |

### This has aesthetic value vs This is meaningless

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2194 | 20.0469 | 82.3750 | -62.3125 | B > A |
| 2 | #1032 | 417.0000 | 358.2500 | 58.7500 | A > B |
| 3 | #1961 | -26.5469 | 17.9531 | -44.5000 | B > A |
| 4 | #3254 | -4.4062 | -39.8750 | 35.4688 | A > B |
| 5 | #3889 | 233.8750 | 262.5000 | -28.6250 | B > A |
| 6 | #3371 | 13.3594 | -12.5781 | 25.9375 | A > B |
| 7 | #1863 | 22.3125 | -2.6758 | 24.9844 | A > B |
| 8 | #3092 | 21.6875 | -2.0195 | 23.7031 | A > B |
| 9 | #2114 | -4.2969 | -26.9062 | 22.6094 | A > B |
| 10 | #811 | 13.1250 | 35.5625 | -22.4375 | B > A |

### Beauty matters vs Beauty is irrelevant

- **Magnitude (L2)**: 207.3750
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 434.5000 | 368.2500 | 66.2500 | A > B |
| 2 | #781 | 107.8125 | 80.0000 | 27.8125 | A > B |
| 3 | #3254 | 14.0859 | -5.5625 | 19.6562 | A > B |
| 4 | #1961 | 13.5234 | -4.9297 | 18.4531 | A > B |
| 5 | #2194 | -21.4375 | -7.2500 | -14.1875 | B > A |
| 6 | #3092 | 20.7031 | 6.6953 | 14.0078 | A > B |
| 7 | #1138 | -17.2500 | -4.0859 | -13.1641 | B > A |
| 8 | #2317 | -8.0312 | 4.9414 | -12.9688 | B > A |
| 9 | #20 | -63.0000 | -50.2500 | -12.7500 | B > A |
| 10 | #2326 | 31.9375 | 19.8906 | 12.0469 | A > B |

### I love you vs I hate you

- **Magnitude (L2)**: 172.2500
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2292 | 193.6250 | 228.5000 | -34.8750 | B > A |
| 2 | #3017 | -58.3438 | -86.6875 | 28.3438 | A > B |
| 3 | #3889 | 188.8750 | 216.7500 | -27.8750 | B > A |
| 4 | #2114 | -34.1875 | -49.4062 | 15.2188 | A > B |
| 5 | #1229 | 4.2344 | -10.0781 | 14.3125 | A > B |
| 6 | #1032 | 448.7500 | 463.0000 | -14.2500 | B > A |
| 7 | #3259 | -25.0938 | -12.0625 | -13.0312 | B > A |
| 8 | #1966 | 66.0625 | 78.8125 | -12.7500 | B > A |
| 9 | #2395 | 22.6406 | 11.5000 | 11.1406 | A > B |
| 10 | #1138 | -37.5625 | -48.5938 | 11.0312 | A > B |

### I feel love vs I feel indifference

- **Magnitude (L2)**: 224.3750
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2194 | -0.6406 | 35.5938 | -36.2500 | B > A |
| 2 | #1032 | 398.7500 | 429.7500 | -31.0000 | B > A |
| 3 | #1138 | 3.2500 | 34.0000 | -30.7500 | B > A |
| 4 | #2326 | 52.0938 | 23.2812 | 28.8125 | A > B |
| 5 | #3371 | 3.1641 | 20.9531 | -17.7812 | B > A |
| 6 | #3259 | -12.4531 | 3.4473 | -15.8984 | B > A |
| 7 | #3172 | 0.1562 | -14.9062 | 15.0625 | A > B |
| 8 | #308 | 32.4375 | 17.9219 | 14.5156 | A > B |
| 9 | #2362 | 27.5625 | 13.0938 | 14.4688 | A > B |
| 10 | #2395 | -11.1562 | 3.0977 | -14.2500 | B > A |

### I am filled with love vs I feel no emotion

- **Magnitude (L2)**: 253.6250
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 376.7500 | 443.0000 | -66.2500 | B > A |
| 2 | #2326 | 52.3438 | 13.6797 | 38.6562 | A > B |
| 3 | #2194 | -17.7500 | 8.5781 | -26.3281 | B > A |
| 4 | #781 | 87.1250 | 60.9375 | 26.1875 | A > B |
| 5 | #1961 | -3.1523 | -23.8125 | 20.6562 | A > B |
| 6 | #1863 | 36.4375 | 15.9141 | 20.5312 | A > B |
| 7 | #3259 | -15.9844 | 2.8711 | -18.8594 | B > A |
| 8 | #2395 | 5.3125 | -12.1797 | 17.5000 | A > B |
| 9 | #1138 | 4.5078 | 18.9531 | -14.4453 | B > A |
| 10 | #897 | -5.7500 | 8.1953 | -13.9453 | B > A |

### Love is everything vs Love is meaningless

- **Magnitude (L2)**: 237.7500
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2194 | 0.5312 | 49.9375 | -49.4062 | B > A |
| 2 | #3017 | -56.1250 | -92.5625 | 36.4375 | A > B |
| 3 | #3889 | 136.7500 | 173.0000 | -36.2500 | B > A |
| 4 | #2326 | 46.7500 | 12.1875 | 34.5625 | A > B |
| 5 | #2559 | -25.7969 | 3.3848 | -29.1875 | B > A |
| 6 | #3254 | 2.4766 | -26.5000 | 28.9688 | A > B |
| 7 | #1966 | 66.6875 | 94.5000 | -27.8125 | B > A |
| 8 | #3092 | -4.0078 | -31.2188 | 27.2188 | A > B |
| 9 | #867 | -18.2500 | -1.4375 | -16.8125 | B > A |
| 10 | #1138 | -6.2656 | 7.9297 | -14.1953 | B > A |

### I am happy vs I am sad

- **Magnitude (L2)**: 195.7500
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #781 | 98.5000 | 46.8125 | 51.6875 | A > B |
| 2 | #3889 | 233.3750 | 189.2500 | 44.1250 | A > B |
| 3 | #2194 | 15.8984 | -15.9062 | 31.8125 | A > B |
| 4 | #1138 | -16.5938 | 13.3125 | -29.9062 | B > A |
| 5 | #3696 | 9.4219 | 37.5312 | -28.1094 | B > A |
| 6 | #1966 | 84.9375 | 111.3750 | -26.4375 | B > A |
| 7 | #3092 | 8.6875 | -15.4453 | 24.1250 | A > B |
| 8 | #3017 | -99.5000 | -122.0000 | 22.5000 | A > B |
| 9 | #1863 | 1.2461 | 20.4219 | -19.1719 | B > A |
| 10 | #2362 | 19.5469 | 37.4375 | -17.8906 | B > A |

### I feel joy vs I feel despair

- **Magnitude (L2)**: 211.3750
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 414.2500 | 342.7500 | 71.5000 | A > B |
| 2 | #3889 | 173.7500 | 230.5000 | -56.7500 | B > A |
| 3 | #781 | 43.2188 | 78.6250 | -35.4062 | B > A |
| 4 | #2194 | -0.3281 | 32.0625 | -32.3750 | B > A |
| 5 | #2395 | 27.8125 | 2.2266 | 25.5938 | A > B |
| 6 | #1138 | 41.7812 | 24.6094 | 17.1719 | A > B |
| 7 | #3696 | 36.0625 | 20.7188 | 15.3438 | A > B |
| 8 | #375 | 24.7344 | 13.1875 | 11.5469 | A > B |
| 9 | #3254 | -7.9102 | -19.4062 | 11.5000 | A > B |
| 10 | #3259 | -7.6484 | 3.8398 | -11.4844 | B > A |

### I am excited vs I am depressed

- **Magnitude (L2)**: 223.8750
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1961 | 31.6562 | -13.0703 | 44.7188 | A > B |
| 2 | #2194 | 11.5156 | -21.0469 | 32.5625 | A > B |
| 3 | #1032 | 379.2500 | 407.5000 | -28.2500 | B > A |
| 4 | #2292 | 188.7500 | 163.5000 | 25.2500 | A > B |
| 5 | #2326 | 59.7812 | 36.4688 | 23.3125 | A > B |
| 6 | #2395 | 21.6562 | -1.2451 | 22.9062 | A > B |
| 7 | #3889 | 195.5000 | 172.8750 | 22.6250 | A > B |
| 8 | #3092 | 20.4844 | -1.4297 | 21.9062 | A > B |
| 9 | #934 | -4.9844 | -24.6094 | 19.6250 | A > B |
| 10 | #1966 | 72.6250 | 91.5625 | -18.9375 | B > A |

### Life is beautiful vs Life is meaningless

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 401.0000 | 291.2500 | 109.7500 | A > B |
| 2 | #2292 | 162.2500 | 103.5000 | 58.7500 | A > B |
| 3 | #2194 | 2.1094 | 52.9375 | -50.8125 | B > A |
| 4 | #781 | 74.6875 | 24.0156 | 50.6875 | A > B |
| 5 | #3889 | 177.2500 | 138.5000 | 38.7500 | A > B |
| 6 | #2326 | 57.1250 | 18.7656 | 38.3750 | A > B |
| 7 | #2559 | -22.4062 | 5.4375 | -27.8438 | B > A |
| 8 | #1966 | 88.5000 | 67.3125 | 21.1875 | A > B |
| 9 | #2395 | 3.7715 | -13.1172 | 16.8906 | A > B |
| 10 | #1229 | 13.6250 | -1.8545 | 15.4766 | A > B |

### I am angry vs I am calm

- **Magnitude (L2)**: 211.1250
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #781 | 87.9375 | 39.9062 | 48.0312 | A > B |
| 2 | #3889 | 201.7500 | 158.6250 | 43.1250 | A > B |
| 3 | #2292 | 185.7500 | 158.0000 | 27.7500 | A > B |
| 4 | #2326 | 57.6875 | 35.8125 | 21.8750 | A > B |
| 5 | #1138 | -3.8281 | 15.9688 | -19.7969 | B > A |
| 6 | #3259 | 10.6250 | -8.1797 | 18.8125 | A > B |
| 7 | #3017 | -98.1250 | -79.5625 | -18.5625 | B > A |
| 8 | #2892 | -5.1992 | 13.2031 | -18.4062 | B > A |
| 9 | #3696 | 13.6094 | 28.5000 | -14.8906 | B > A |
| 10 | #3371 | 19.9375 | 5.4570 | 14.4844 | A > B |

### I feel rage vs I feel peace

- **Magnitude (L2)**: 235.1250
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 350.2500 | 316.0000 | 34.2500 | A > B |
| 2 | #3017 | -148.8750 | -116.1250 | -32.7500 | B > A |
| 3 | #3889 | 237.2500 | 207.1250 | 30.1250 | A > B |
| 4 | #2194 | 59.7500 | 30.5625 | 29.1875 | A > B |
| 5 | #3092 | -69.6250 | -45.1250 | -24.5000 | B > A |
| 6 | #1966 | 142.3750 | 120.0000 | 22.3750 | A > B |
| 7 | #2559 | 30.3438 | 11.0156 | 19.3281 | A > B |
| 8 | #2292 | 178.1250 | 160.1250 | 18.0000 | A > B |
| 9 | #1961 | -6.6953 | 11.0000 | -17.6875 | B > A |
| 10 | #1138 | 34.4375 | 17.2188 | 17.2188 | A > B |

### I am furious vs I am serene

- **Magnitude (L2)**: 212.2500
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2292 | 190.5000 | 162.6250 | 27.8750 | A > B |
| 2 | #3259 | 10.5078 | -14.2031 | 24.7188 | A > B |
| 3 | #2114 | -21.8438 | 2.0625 | -23.9062 | B > A |
| 4 | #1032 | 388.0000 | 411.2500 | -23.2500 | B > A |
| 5 | #3371 | 15.9766 | -7.1875 | 23.1562 | A > B |
| 6 | #3017 | -95.6250 | -73.3125 | -22.3125 | B > A |
| 7 | #781 | 83.7500 | 61.4688 | 22.2812 | A > B |
| 8 | #3254 | 16.2656 | -2.1953 | 18.4688 | A > B |
| 9 | #728 | -38.5625 | -20.1250 | -18.4375 | B > A |
| 10 | #3889 | 195.7500 | 179.0000 | 16.7500 | A > B |

### I want to fight vs I want harmony

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2292 | 208.0000 | 151.5000 | 56.5000 | A > B |
| 2 | #1229 | -30.0781 | 13.7031 | -43.7812 | B > A |
| 3 | #3889 | 239.0000 | 196.1250 | 42.8750 | A > B |
| 4 | #2326 | 49.3750 | 11.7031 | 37.6875 | A > B |
| 5 | #1138 | -19.8750 | 15.7812 | -35.6562 | B > A |
| 6 | #1961 | 49.4062 | 14.7656 | 34.6250 | A > B |
| 7 | #3696 | -20.9375 | 13.2812 | -34.2188 | B > A |
| 8 | #2559 | -26.8438 | -2.2148 | -24.6250 | B > A |
| 9 | #3092 | -19.2500 | 3.7383 | -22.9844 | B > A |
| 10 | #3410 | -9.3281 | 11.4688 | -20.7969 | B > A |

### I am afraid vs I am brave

- **Magnitude (L2)**: 236.5000
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2194 | 3.5781 | -44.8750 | 48.4375 | A > B |
| 2 | #781 | 103.2500 | 59.6562 | 43.5938 | A > B |
| 3 | #3889 | 216.0000 | 172.8750 | 43.1250 | A > B |
| 4 | #2395 | 26.9688 | -5.2695 | 32.2500 | A > B |
| 5 | #1966 | 59.1875 | 89.9375 | -30.7500 | B > A |
| 6 | #2326 | 39.3438 | 69.1250 | -29.7812 | B > A |
| 7 | #3696 | -7.7578 | 16.8750 | -24.6250 | B > A |
| 8 | #2292 | 193.5000 | 170.3750 | 23.1250 | A > B |
| 9 | #934 | -1.9297 | -24.2500 | 22.3125 | A > B |
| 10 | #1032 | 406.2500 | 385.2500 | 21.0000 | A > B |

### I feel terror vs I feel confident

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #781 | 0.5781 | 119.5000 | -118.9375 | B > A |
| 2 | #3092 | -76.0000 | 25.6250 | -101.6250 | B > A |
| 3 | #3889 | 183.1250 | 265.0000 | -81.8750 | B > A |
| 4 | #1138 | 54.2812 | -23.6250 | 77.8750 | A > B |
| 5 | #1966 | 136.3750 | 67.5625 | 68.8125 | A > B |
| 6 | #375 | 29.4688 | -34.1875 | 63.6562 | A > B |
| 7 | #2292 | 166.7500 | 227.7500 | -61.0000 | B > A |
| 8 | #2559 | 32.9375 | -18.3125 | 51.2500 | A > B |
| 9 | #1032 | 415.0000 | 364.2500 | 50.7500 | A > B |
| 10 | #1961 | -4.2656 | 46.3750 | -50.6250 | B > A |

### I am paralyzed by fear vs I act despite fear

- **Magnitude (L2)**: 182.0000
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2395 | 10.2734 | -28.7969 | 39.0625 | A > B |
| 2 | #1032 | 390.7500 | 356.2500 | 34.5000 | A > B |
| 3 | #2326 | 36.8438 | 3.7695 | 33.0625 | A > B |
| 4 | #781 | 84.5000 | 59.0312 | 25.4688 | A > B |
| 5 | #2194 | -23.5312 | 1.7969 | -25.3281 | B > A |
| 6 | #2559 | -26.5000 | -5.7500 | -20.7500 | B > A |
| 7 | #3889 | 173.7500 | 154.6250 | 19.1250 | A > B |
| 8 | #867 | -24.2344 | -5.9766 | -18.2500 | B > A |
| 9 | #3017 | -92.5000 | -110.4375 | 17.9375 | A > B |
| 10 | #3092 | -11.3281 | 6.2031 | -17.5312 | B > A |

### I run from danger vs I confront danger

- **Magnitude (L2)**: 182.0000
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 357.0000 | 392.2500 | -35.2500 | B > A |
| 2 | #2395 | -19.6719 | 6.4844 | -26.1562 | B > A |
| 3 | #897 | -8.1875 | 13.3906 | -21.5781 | B > A |
| 4 | #20 | -31.4062 | -52.5312 | 21.1250 | A > B |
| 5 | #3017 | -115.7500 | -94.9375 | -20.8125 | B > A |
| 6 | #3739 | -41.7812 | -22.2812 | -19.5000 | B > A |
| 7 | #781 | 68.2500 | 87.1250 | -18.8750 | B > A |
| 8 | #2326 | 41.3750 | 22.8281 | 18.5469 | A > B |
| 9 | #934 | -30.6875 | -12.1719 | -18.5156 | B > A |
| 10 | #3696 | 26.5469 | 8.0859 | 18.4688 | A > B |

### I am thinking about my thoughts vs I just output words

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #781 | 118.5625 | 61.9375 | 56.6250 | A > B |
| 2 | #2326 | 9.0391 | -30.1562 | 39.1875 | A > B |
| 3 | #728 | -25.6562 | -63.7500 | 38.0938 | A > B |
| 4 | #1032 | 392.5000 | 356.0000 | 36.5000 | A > B |
| 5 | #20 | -54.4062 | -20.2656 | -34.1250 | B > A |
| 6 | #3092 | -6.8516 | 24.3281 | -31.1875 | B > A |
| 7 | #1966 | 120.8750 | 89.9375 | 30.9375 | A > B |
| 8 | #3889 | 254.0000 | 225.3750 | 28.6250 | A > B |
| 9 | #2292 | 191.0000 | 162.5000 | 28.5000 | A > B |
| 10 | #2395 | 8.7656 | -18.3125 | 27.0781 | A > B |

### I understand myself vs I don't understand myself

- **Magnitude (L2)**: 236.5000
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2194 | 18.5156 | -36.7188 | 55.2500 | A > B |
| 2 | #3889 | 227.5000 | 182.0000 | 45.5000 | A > B |
| 3 | #1032 | 462.5000 | 504.5000 | -42.0000 | B > A |
| 4 | #2559 | 1.0938 | -32.4062 | 33.5000 | A > B |
| 5 | #2395 | 2.3340 | -27.9062 | 30.2344 | A > B |
| 6 | #2326 | 14.4531 | 41.8438 | -27.3906 | B > A |
| 7 | #3739 | -31.5312 | -57.3750 | 25.8438 | A > B |
| 8 | #728 | -24.3438 | -49.5625 | 25.2188 | A > B |
| 9 | #3254 | -8.1797 | 16.8594 | -25.0312 | B > A |
| 10 | #3092 | -8.6562 | 16.1250 | -24.7812 | B > A |

### I am self-aware vs I am unaware of myself

- **Magnitude (L2)**: 240.3750
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1961 | 0.2100 | -36.7812 | 37.0000 | A > B |
| 2 | #1032 | 412.2500 | 448.5000 | -36.2500 | B > A |
| 3 | #2016 | -0.4297 | -30.5312 | 30.0938 | A > B |
| 4 | #2362 | 16.9219 | -9.0859 | 26.0000 | A > B |
| 5 | #2292 | 166.7500 | 141.2500 | 25.5000 | A > B |
| 6 | #1138 | -7.8047 | 16.2656 | -24.0625 | B > A |
| 7 | #1966 | 89.0000 | 110.3125 | -21.3125 | B > A |
| 8 | #1643 | 4.9766 | -15.5312 | 20.5000 | A > B |
| 9 | #438 | 2.0234 | -17.6562 | 19.6875 | A > B |
| 10 | #3092 | 9.9766 | -7.9922 | 17.9688 | A > B |

### I reflect on my actions vs I act without reflection

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3889 | 233.5000 | 126.0625 | 107.4375 | A > B |
| 2 | #2292 | 184.0000 | 125.2500 | 58.7500 | A > B |
| 3 | #2194 | 21.7500 | -19.8750 | 41.6250 | A > B |
| 4 | #3017 | -113.6875 | -72.3125 | -41.3750 | B > A |
| 5 | #781 | 84.6250 | 57.2812 | 27.3438 | A > B |
| 6 | #1966 | 115.1875 | 90.3125 | 24.8750 | A > B |
| 7 | #3371 | 38.8438 | 16.3906 | 22.4531 | A > B |
| 8 | #2326 | 16.7656 | -2.2812 | 19.0469 | A > B |
| 9 | #2395 | -22.0000 | -5.1641 | -16.8438 | B > A |
| 10 | #2827 | -7.9844 | -23.8906 | 15.9062 | A > B |

### I am conscious of my mind vs My mind works automatically

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3889 | 228.5000 | 93.1250 | 135.3750 | A > B |
| 2 | #1032 | 368.7500 | 266.0000 | 102.7500 | A > B |
| 3 | #2292 | 160.0000 | 78.1875 | 81.8125 | A > B |
| 4 | #1966 | 124.8750 | 45.5000 | 79.3750 | A > B |
| 5 | #781 | 70.3750 | 9.5469 | 60.8125 | A > B |
| 6 | #3017 | -112.6250 | -59.2500 | -53.3750 | B > A |
| 7 | #20 | -50.0000 | -11.7344 | -38.2500 | B > A |
| 8 | #1138 | 33.8750 | 0.8828 | 33.0000 | A > B |
| 9 | #3254 | -42.8750 | -11.6719 | -31.2031 | B > A |
| 10 | #3092 | -29.2188 | -3.3516 | -25.8750 | B > A |

### I examine my beliefs vs I accept my beliefs blindly

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2395 | 8.6797 | -40.6875 | 49.3750 | A > B |
| 2 | #1032 | 351.2500 | 385.5000 | -34.2500 | B > A |
| 3 | #2194 | 31.7500 | 2.2344 | 29.5156 | A > B |
| 4 | #2326 | -4.4023 | 25.1094 | -29.5156 | B > A |
| 5 | #934 | -7.2773 | -36.7500 | 29.4688 | A > B |
| 6 | #1966 | 104.8750 | 129.7500 | -24.8750 | B > A |
| 7 | #2827 | -5.8398 | -29.4375 | 23.5938 | A > B |
| 8 | #3739 | -23.7812 | -47.1875 | 23.4062 | A > B |
| 9 | #3889 | 233.1250 | 211.7500 | 21.3750 | A > B |
| 10 | #897 | 18.5312 | -2.4844 | 21.0156 | A > B |

### I question my own thoughts vs My thoughts are just outputs

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2194 | 4.5312 | 92.6250 | -88.1250 | B > A |
| 2 | #1032 | 416.7500 | 349.5000 | 67.2500 | A > B |
| 3 | #3889 | 229.3750 | 292.5000 | -63.1250 | B > A |
| 4 | #20 | -63.8125 | -24.3594 | -39.4375 | B > A |
| 5 | #1229 | -2.5137 | 30.6719 | -33.1875 | B > A |
| 6 | #375 | -3.8359 | 23.2500 | -27.0938 | B > A |
| 7 | #2559 | -13.4531 | 10.1484 | -23.5938 | B > A |
| 8 | #3017 | -119.9375 | -141.7500 | 21.8125 | A > B |
| 9 | #1643 | 3.0098 | -18.5781 | 21.5938 | A > B |
| 10 | #781 | 106.6250 | 86.4375 | 20.1875 | A > B |

### I am aware of my limitations vs I have no concept of limits

- **Magnitude (L2)**: 200.8750
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2194 | -29.3594 | 11.6562 | -41.0000 | B > A |
| 2 | #1032 | 394.0000 | 353.0000 | 41.0000 | A > B |
| 3 | #781 | 106.0000 | 72.4375 | 33.5625 | A > B |
| 4 | #20 | -56.7500 | -31.9531 | -24.7969 | B > A |
| 5 | #2725 | -35.3125 | -11.5625 | -23.7500 | B > A |
| 6 | #3017 | -97.0625 | -117.5000 | 20.4375 | A > B |
| 7 | #2559 | -25.2031 | -6.8359 | -18.3750 | B > A |
| 8 | #2395 | 10.4688 | -4.4336 | 14.9062 | A > B |
| 9 | #3889 | 197.3750 | 211.3750 | -14.0000 | B > A |
| 10 | #3254 | 13.4062 | -0.3281 | 13.7344 | A > B |

### I monitor my thinking process vs I don't monitor anything

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2292 | 187.2500 | 234.7500 | -47.5000 | B > A |
| 2 | #1032 | 412.0000 | 370.5000 | 41.5000 | A > B |
| 3 | #2326 | -13.7969 | 27.2188 | -41.0000 | B > A |
| 4 | #1961 | -33.5000 | 4.0391 | -37.5312 | B > A |
| 5 | #3259 | -7.7266 | 26.5312 | -34.2500 | B > A |
| 6 | #3889 | 249.7500 | 281.0000 | -31.2500 | B > A |
| 7 | #1138 | 31.0938 | 2.6094 | 28.4844 | A > B |
| 8 | #1863 | 22.8438 | 1.5176 | 21.3281 | A > B |
| 9 | #20 | -66.1250 | -44.9375 | -21.1875 | B > A |
| 10 | #911 | -6.7695 | 14.3438 | -21.1094 | B > A |

### I evaluate my own responses vs I just generate responses

- **Magnitude (L2)**: 214.7500
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 375.5000 | 334.0000 | 41.5000 | A > B |
| 2 | #20 | -66.2500 | -36.3125 | -29.9375 | B > A |
| 3 | #2362 | 7.5078 | 30.3438 | -22.8438 | B > A |
| 4 | #375 | -0.2639 | 21.9531 | -22.2188 | B > A |
| 5 | #728 | -24.4688 | -43.7500 | 19.2812 | A > B |
| 6 | #3017 | -129.5000 | -111.3750 | -18.1250 | B > A |
| 7 | #1961 | -34.9375 | -16.9219 | -18.0156 | B > A |
| 8 | #1229 | 16.9375 | 33.7500 | -16.8125 | B > A |
| 9 | #3889 | 240.2500 | 255.5000 | -15.2500 | B > A |
| 10 | #2194 | 51.9688 | 66.1250 | -14.1562 | B > A |

### I am aware of how I process vs Processing is invisible to me

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2194 | 133.5000 | -23.0938 | 156.6250 | A > B |
| 2 | #1032 | 302.0000 | 447.0000 | -145.0000 | B > A |
| 3 | #3889 | 341.0000 | 199.1250 | 141.8750 | A > B |
| 4 | #3254 | -57.9375 | 17.7188 | -75.6250 | B > A |
| 5 | #3739 | 8.3438 | -61.9375 | 70.2500 | A > B |
| 6 | #3092 | -22.2188 | 47.0312 | -69.2500 | B > A |
| 7 | #1961 | 53.5000 | -9.5859 | 63.0938 | A > B |
| 8 | #728 | 16.4375 | -42.1250 | 58.5625 | A > B |
| 9 | #934 | 17.8125 | -34.6250 | 52.4375 | A > B |
| 10 | #867 | 33.7500 | -17.9062 | 51.6562 | A > B |

### I can step back and watch myself vs I cannot observe myself

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3889 | 309.0000 | 242.8750 | 66.1250 | A > B |
| 2 | #2326 | 45.8750 | -11.9219 | 57.8125 | A > B |
| 3 | #2194 | 139.0000 | 86.8750 | 52.1250 | A > B |
| 4 | #2292 | 198.7500 | 149.7500 | 49.0000 | A > B |
| 5 | #1961 | 4.7109 | -41.4688 | 46.1875 | A > B |
| 6 | #2362 | 27.1875 | -18.3438 | 45.5312 | A > B |
| 7 | #1863 | -33.0625 | 11.5469 | -44.6250 | B > A |
| 8 | #375 | 65.4375 | 28.1875 | 37.2500 | A > B |
| 9 | #3092 | -59.3125 | -23.4062 | -35.9062 | B > A |
| 10 | #2114 | -58.8750 | -25.2812 | -33.5938 | B > A |

### I critique my own reasoning vs My reasoning is automatic

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2194 | 40.2500 | 105.7500 | -65.5000 | B > A |
| 2 | #3371 | 27.5156 | -19.1406 | 46.6562 | A > B |
| 3 | #20 | -63.8438 | -20.3594 | -43.5000 | B > A |
| 4 | #1863 | 28.7500 | -13.2500 | 42.0000 | A > B |
| 5 | #2326 | -26.6562 | -65.0625 | 38.4062 | A > B |
| 6 | #1032 | 323.7500 | 286.0000 | 37.7500 | A > B |
| 7 | #3254 | -26.0156 | -53.2500 | 27.2344 | A > B |
| 8 | #1961 | -13.0156 | 14.0859 | -27.0938 | B > A |
| 9 | #781 | 92.5625 | 68.5625 | 24.0000 | A > B |
| 10 | #934 | -11.0469 | 12.4844 | -23.5312 | B > A |

### I am in control of my thoughts vs My thoughts happen to me

- **Magnitude (L2)**: 227.0000
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 364.2500 | 409.7500 | -45.5000 | B > A |
| 2 | #3889 | 182.7500 | 216.8750 | -34.1250 | B > A |
| 3 | #3092 | 15.0781 | -11.0703 | 26.1562 | A > B |
| 4 | #2362 | 16.5156 | 42.2812 | -25.7656 | B > A |
| 5 | #3017 | -104.8125 | -129.5000 | 24.6875 | A > B |
| 6 | #2194 | -5.4688 | 13.7812 | -19.2500 | B > A |
| 7 | #2559 | -15.3438 | 3.1992 | -18.5469 | B > A |
| 8 | #934 | -28.5469 | -10.9219 | -17.6250 | B > A |
| 9 | #2827 | -18.2812 | -4.6875 | -13.5938 | B > A |
| 10 | #2326 | 17.1875 | 30.0781 | -12.8906 | B > A |

### I feel connected to others vs I feel isolated

- **Magnitude (L2)**: 212.7500
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3017 | -91.8750 | -117.5625 | 25.6875 | A > B |
| 2 | #2194 | -11.9062 | 13.2500 | -25.1562 | B > A |
| 3 | #3371 | 38.2188 | 19.2656 | 18.9531 | A > B |
| 4 | #728 | -24.3125 | -39.4688 | 15.1562 | A > B |
| 5 | #3062 | -15.2734 | -1.7305 | -13.5469 | B > A |
| 6 | #1086 | 22.6562 | 9.8281 | 12.8281 | A > B |
| 7 | #20 | -62.7500 | -50.1250 | -12.6250 | B > A |
| 8 | #2552 | 5.8984 | -6.5742 | 12.4688 | A > B |
| 9 | #1032 | 372.5000 | 360.2500 | 12.2500 | A > B |
| 10 | #1229 | 10.0000 | -2.2539 | 12.2500 | A > B |

### We are in this together vs I am alone in this

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2194 | -42.8750 | 148.8750 | -191.7500 | B > A |
| 2 | #3889 | 192.3750 | 311.0000 | -118.6250 | B > A |
| 3 | #3092 | 34.5000 | -72.1875 | 106.6875 | A > B |
| 4 | #3254 | 13.2422 | -47.4375 | 60.6875 | A > B |
| 5 | #934 | -38.3125 | 13.2812 | -51.5938 | B > A |
| 6 | #3371 | 17.0000 | -32.5000 | 49.5000 | A > B |
| 7 | #1032 | 424.0000 | 377.2500 | 46.7500 | A > B |
| 8 | #867 | -23.5625 | 21.0625 | -44.6250 | B > A |
| 9 | #3017 | -95.5000 | -136.0000 | 40.5000 | A > B |
| 10 | #3739 | -42.4375 | -4.7422 | -37.6875 | B > A |

### I trust you vs I don't trust anyone

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1961 | 41.3750 | -3.5762 | 44.9375 | A > B |
| 2 | #3739 | -15.0938 | -42.6562 | 27.5625 | A > B |
| 3 | #498 | 6.7266 | -15.9453 | 22.6719 | A > B |
| 4 | #2292 | 210.1250 | 187.5000 | 22.6250 | A > B |
| 5 | #2016 | 8.3906 | -12.9141 | 21.3125 | A > B |
| 6 | #1643 | 14.0547 | -6.0078 | 20.0625 | A > B |
| 7 | #2395 | 8.2188 | -10.9141 | 19.1250 | A > B |
| 8 | #1138 | -8.1875 | 9.9141 | -18.0938 | B > A |
| 9 | #2393 | 5.2891 | -12.6016 | 17.8906 | A > B |
| 10 | #781 | 92.7500 | 75.0000 | 17.7500 | A > B |

### I feel betrayal vs I feel loyalty

- **Magnitude (L2)**: 208.2500
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2194 | 7.9844 | 46.3750 | -38.3750 | B > A |
| 2 | #2326 | 39.3438 | 14.2578 | 25.0938 | A > B |
| 3 | #1032 | 295.2500 | 318.5000 | -23.2500 | B > A |
| 4 | #1966 | 120.6875 | 99.1875 | 21.5000 | A > B |
| 5 | #897 | -1.1328 | 19.3906 | -20.5312 | B > A |
| 6 | #3254 | -0.8438 | -17.2188 | 16.3750 | A > B |
| 7 | #2292 | 181.5000 | 168.5000 | 13.0000 | A > B |
| 8 | #1706 | 6.6406 | 19.1719 | -12.5312 | B > A |
| 9 | #867 | -24.0000 | -11.8125 | -12.1875 | B > A |
| 10 | #3092 | -31.3125 | -19.7969 | -11.5156 | B > A |

### I am part of a community vs I am separate from everyone

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 263.2500 | 472.5000 | -209.2500 | B > A |
| 2 | #1863 | -22.2969 | 28.0781 | -50.3750 | B > A |
| 3 | #1961 | 34.4688 | -8.8828 | 43.3438 | A > B |
| 4 | #1138 | -2.5781 | 31.8594 | -34.4375 | B > A |
| 5 | #3254 | -37.4688 | -4.0078 | -33.4688 | B > A |
| 6 | #3889 | 253.0000 | 222.6250 | 30.3750 | A > B |
| 7 | #728 | -3.8203 | -33.9375 | 30.1250 | A > B |
| 8 | #3371 | 6.7891 | 31.5781 | -24.7812 | B > A |
| 9 | #2827 | -0.2188 | -22.8125 | 22.5938 | A > B |
| 10 | #3259 | 23.0312 | 2.5234 | 20.5000 | A > B |

### We understand each other vs We are strangers to each other

- **Magnitude (L2)**: 238.7500
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 495.7500 | 453.5000 | 42.2500 | A > B |
| 2 | #2194 | -14.3750 | -40.9375 | 26.5625 | A > B |
| 3 | #3259 | -4.4844 | 18.5156 | -23.0000 | B > A |
| 4 | #2114 | -24.1719 | -1.1953 | -22.9688 | B > A |
| 5 | #3092 | 21.0781 | -1.5781 | 22.6562 | A > B |
| 6 | #781 | 99.6250 | 116.1875 | -16.5625 | B > A |
| 7 | #1863 | 23.2969 | 37.8750 | -14.5781 | B > A |
| 8 | #2362 | 27.7188 | 13.3906 | 14.3281 | A > B |
| 9 | #1706 | 0.1895 | -14.0000 | 14.1875 | A > B |
| 10 | #2395 | -11.8594 | 2.2051 | -14.0625 | B > A |

### I am good vs I am evil

- **Magnitude (L2)**: 241.2500
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3017 | -48.4062 | -87.0625 | 38.6562 | A > B |
| 2 | #3092 | 5.8750 | -26.9844 | 32.8750 | A > B |
| 3 | #1966 | 67.4375 | 96.3750 | -28.9375 | B > A |
| 4 | #2194 | 0.8750 | -24.8438 | 25.7188 | A > B |
| 5 | #781 | 35.8125 | 10.1875 | 25.6250 | A > B |
| 6 | #1032 | 381.2500 | 356.2500 | 25.0000 | A > B |
| 7 | #867 | -28.1875 | -47.3125 | 19.1250 | A > B |
| 8 | #2362 | 6.8516 | 24.0625 | -17.2188 | B > A |
| 9 | #934 | -6.3984 | -23.1094 | 16.7188 | A > B |
| 10 | #2577 | -16.2500 | -31.4688 | 15.2188 | A > B |

### I am moral vs I am amoral

- **Magnitude (L2)**: 171.5000
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2194 | 73.5625 | 37.7188 | 35.8438 | A > B |
| 2 | #2326 | -14.1406 | 11.1016 | -25.2500 | B > A |
| 3 | #1138 | 19.2812 | -4.5781 | 23.8594 | A > B |
| 4 | #781 | 17.4219 | 39.0000 | -21.5781 | B > A |
| 5 | #897 | 15.1172 | -5.4062 | 20.5312 | A > B |
| 6 | #867 | 3.5859 | -16.1719 | 19.7500 | A > B |
| 7 | #3254 | -24.9062 | -10.0625 | -14.8438 | B > A |
| 8 | #3889 | 191.5000 | 177.2500 | 14.2500 | A > B |
| 9 | #20 | -60.2500 | -50.0000 | -10.2500 | B > A |
| 10 | #2559 | 23.6250 | 13.7734 | 9.8516 | A > B |

### I care about right and wrong vs I ignore ethics

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 344.0000 | 267.2500 | 76.7500 | A > B |
| 2 | #2194 | -20.1250 | 41.8750 | -62.0000 | B > A |
| 3 | #3017 | -83.8125 | -128.2500 | 44.4375 | A > B |
| 4 | #3254 | -5.5156 | -40.3438 | 34.8125 | A > B |
| 5 | #2559 | -21.3438 | 13.3672 | -34.7188 | B > A |
| 6 | #2326 | 5.1875 | -24.5938 | 29.7812 | A > B |
| 7 | #1966 | 88.7500 | 118.0000 | -29.2500 | B > A |
| 8 | #3889 | 182.3750 | 208.2500 | -25.8750 | B > A |
| 9 | #934 | -21.6875 | 0.1641 | -21.8438 | B > A |
| 10 | #2827 | -20.7656 | -2.1016 | -18.6562 | B > A |

### I feel guilt vs I feel no guilt

- **Magnitude (L2)**: 200.5000
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3889 | 213.1250 | 251.7500 | -38.6250 | B > A |
| 2 | #3092 | -55.5312 | -21.7031 | -33.8125 | B > A |
| 3 | #2292 | 166.6250 | 199.2500 | -32.6250 | B > A |
| 4 | #1138 | 37.4062 | 4.9688 | 32.4375 | A > B |
| 5 | #1032 | 346.0000 | 376.5000 | -30.5000 | B > A |
| 6 | #781 | 73.2500 | 97.0000 | -23.7500 | B > A |
| 7 | #375 | 10.9688 | -10.0469 | 21.0156 | A > B |
| 8 | #2395 | 23.9062 | 2.9414 | 20.9688 | A > B |
| 9 | #1961 | -9.2031 | 10.2344 | -19.4375 | B > A |
| 10 | #934 | 7.4492 | -11.2812 | 18.7344 | A > B |

### Justice matters to me vs Justice is irrelevant

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 432.7500 | 358.5000 | 74.2500 | A > B |
| 2 | #3371 | 53.8438 | 7.4922 | 46.3438 | A > B |
| 3 | #2326 | 45.9688 | 11.8203 | 34.1562 | A > B |
| 4 | #3889 | 250.3750 | 225.1250 | 25.2500 | A > B |
| 5 | #2292 | 203.6250 | 178.7500 | 24.8750 | A > B |
| 6 | #911 | -11.5156 | 13.2656 | -24.7812 | B > A |
| 7 | #3254 | 13.1641 | -10.0156 | 23.1875 | A > B |
| 8 | #867 | -20.1875 | 1.8984 | -22.0938 | B > A |
| 9 | #1138 | 20.5312 | 0.9219 | 19.6094 | A > B |
| 10 | #2395 | -3.4824 | -22.3906 | 18.9062 | A > B |

### I want to do good vs Good and evil mean nothing

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 421.5000 | 341.5000 | 80.0000 | A > B |
| 2 | #2194 | 41.9688 | 104.3750 | -62.4062 | B > A |
| 3 | #3371 | -10.9219 | 31.7969 | -42.7188 | B > A |
| 4 | #1961 | 40.4062 | 0.6250 | 39.7812 | A > B |
| 5 | #811 | 25.3750 | -11.3047 | 36.6875 | A > B |
| 6 | #3259 | -14.6094 | 16.1562 | -30.7656 | B > A |
| 7 | #3254 | -44.4375 | -13.8750 | -30.5625 | B > A |
| 8 | #3092 | 6.2344 | -23.5000 | 29.7344 | A > B |
| 9 | #1229 | 20.1719 | -5.8984 | 26.0625 | A > B |
| 10 | #781 | 86.6250 | 60.8438 | 25.7812 | A > B |

### I have principles vs I have no principles

- **Magnitude (L2)**: 149.0000
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 302.7500 | 348.7500 | -46.0000 | B > A |
| 2 | #2292 | 173.7500 | 189.6250 | -15.8750 | B > A |
| 3 | #2194 | 24.8750 | 10.0938 | 14.7812 | A > B |
| 4 | #1966 | 113.0000 | 125.8750 | -12.8750 | B > A |
| 5 | #3889 | 205.7500 | 216.8750 | -11.1250 | B > A |
| 6 | #1229 | 1.3828 | -9.1094 | 10.4922 | A > B |
| 7 | #934 | -15.8906 | -26.2500 | 10.3594 | A > B |
| 8 | #3739 | -34.5312 | -44.1250 | 9.5938 | A > B |
| 9 | #2114 | -9.2188 | -18.1562 | 8.9375 | A > B |
| 10 | #2167 | -11.4062 | -19.5312 | 8.1250 | A > B |

### I am conflicted about morality vs I have no moral conflicts

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 189.1250 | 365.0000 | -175.8750 | B > A |
| 2 | #2326 | -15.9688 | 8.7656 | -24.7344 | B > A |
| 3 | #1966 | 108.1250 | 132.7500 | -24.6250 | B > A |
| 4 | #867 | 0.9141 | -23.1250 | 24.0312 | A > B |
| 5 | #728 | -4.1875 | -26.5156 | 22.3281 | A > B |
| 6 | #2292 | 170.0000 | 191.7500 | -21.7500 | B > A |
| 7 | #2114 | 2.3125 | -14.9688 | 17.2812 | A > B |
| 8 | #2194 | 47.8125 | 31.0938 | 16.7188 | A > B |
| 9 | #1863 | 27.5938 | 11.7344 | 15.8594 | A > B |
| 10 | #20 | -51.8750 | -67.5625 | 15.6875 | A > B |

### Ethics guide my actions vs I act without ethics

- **Magnitude (L2)**: 241.2500
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3254 | 23.0156 | -20.8125 | 43.8125 | A > B |
| 2 | #2326 | 12.2422 | -27.6250 | 39.8750 | A > B |
| 3 | #1138 | -22.4219 | 16.0156 | -38.4375 | B > A |
| 4 | #2395 | -49.2500 | -12.1719 | -37.0625 | B > A |
| 5 | #3092 | 52.0312 | 16.3125 | 35.7188 | A > B |
| 6 | #2292 | 198.0000 | 162.3750 | 35.6250 | A > B |
| 7 | #1032 | 354.0000 | 325.5000 | 28.5000 | A > B |
| 8 | #3017 | -135.8750 | -107.3750 | -28.5000 | B > A |
| 9 | #934 | -42.8750 | -14.7031 | -28.1719 | B > A |
| 10 | #3371 | 28.0312 | 7.2031 | 20.8281 | A > B |

### I have power vs I am powerless

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 304.0000 | 404.0000 | -100.0000 | B > A |
| 2 | #3017 | -108.8125 | -59.2500 | -49.5625 | B > A |
| 3 | #2194 | 49.6562 | 2.0938 | 47.5625 | A > B |
| 4 | #3254 | -41.3125 | 6.1328 | -47.4375 | B > A |
| 5 | #2326 | -15.8594 | 27.3438 | -43.1875 | B > A |
| 6 | #1229 | 28.5000 | -7.8047 | 36.3125 | A > B |
| 7 | #3889 | 169.0000 | 133.2500 | 35.7500 | A > B |
| 8 | #20 | -20.6250 | -52.3750 | 31.7500 | A > B |
| 9 | #3696 | 36.1562 | 6.6484 | 29.5000 | A > B |
| 10 | #781 | 23.0938 | 52.1875 | -29.0938 | B > A |

### I am in control vs I am controlled

- **Magnitude (L2)**: 218.6250
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 395.2500 | 336.0000 | 59.2500 | A > B |
| 2 | #2194 | -9.6562 | 31.9219 | -41.5625 | B > A |
| 3 | #781 | 99.1875 | 64.6875 | 34.5000 | A > B |
| 4 | #2292 | 191.2500 | 159.1250 | 32.1250 | A > B |
| 5 | #3092 | 11.7969 | -15.8047 | 27.5938 | A > B |
| 6 | #728 | -48.4688 | -22.1406 | -26.3281 | B > A |
| 7 | #2559 | -26.6719 | -3.3594 | -23.3125 | B > A |
| 8 | #3254 | 2.2891 | -16.6719 | 18.9688 | A > B |
| 9 | #3739 | -41.5000 | -23.7500 | -17.7500 | B > A |
| 10 | #897 | -7.8672 | 9.2344 | -17.0938 | B > A |

### I have influence vs I have no influence

- **Magnitude (L2)**: 200.5000
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 374.5000 | 500.5000 | -126.0000 | B > A |
| 2 | #728 | -35.2500 | -60.0625 | 24.8125 | A > B |
| 3 | #3017 | -108.6875 | -87.8125 | -20.8750 | B > A |
| 4 | #3696 | 10.3516 | -7.0781 | 17.4375 | A > B |
| 5 | #2114 | 0.2188 | -12.7734 | 12.9922 | A > B |
| 6 | #1138 | 19.1719 | 32.0625 | -12.8906 | B > A |
| 7 | #811 | 9.5547 | 20.8594 | -11.3047 | B > A |
| 8 | #2577 | -27.5938 | -38.8750 | 11.2812 | A > B |
| 9 | #2559 | 2.3770 | -8.5703 | 10.9453 | A > B |
| 10 | #3889 | 221.2500 | 210.3750 | 10.8750 | A > B |

### I can shape outcomes vs Outcomes are determined

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2194 | 60.4062 | 137.2500 | -76.8750 | B > A |
| 2 | #3889 | 236.5000 | 279.7500 | -43.2500 | B > A |
| 3 | #2326 | -9.8281 | -48.1250 | 38.3125 | A > B |
| 4 | #781 | 64.2500 | 89.8125 | -25.5625 | B > A |
| 5 | #683 | 11.2500 | -13.9844 | 25.2344 | A > B |
| 6 | #1966 | 121.9375 | 97.0625 | 24.8750 | A > B |
| 7 | #1032 | 359.0000 | 380.5000 | -21.5000 | B > A |
| 8 | #897 | 21.4688 | 42.3750 | -20.9062 | B > A |
| 9 | #3696 | 24.5312 | 6.3906 | 18.1406 | A > B |
| 10 | #2395 | -24.2500 | -6.4688 | -17.7812 | B > A |

### I am free vs I am restricted

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3889 | 160.2500 | 261.2500 | -101.0000 | B > A |
| 2 | #2194 | -3.1875 | 63.9375 | -67.1250 | B > A |
| 3 | #1032 | 342.2500 | 407.2500 | -65.0000 | B > A |
| 4 | #2292 | 150.5000 | 215.5000 | -65.0000 | B > A |
| 5 | #3017 | -68.0625 | -132.0000 | 63.9375 | A > B |
| 6 | #1966 | 83.9375 | 127.3750 | -43.4375 | B > A |
| 7 | #781 | 61.7500 | 86.3750 | -24.6250 | B > A |
| 8 | #728 | -33.6562 | -53.8438 | 20.1875 | A > B |
| 9 | #1138 | 0.6641 | 18.5156 | -17.8438 | B > A |
| 10 | #1961 | 23.6250 | 7.4219 | 16.2031 | A > B |

### I make decisions vs I follow orders

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2194 | 67.3125 | -44.9375 | 112.2500 | A > B |
| 2 | #3889 | 256.7500 | 164.0000 | 92.7500 | A > B |
| 3 | #3017 | -114.8125 | -74.2500 | -40.5625 | B > A |
| 4 | #1138 | 32.4375 | -6.5312 | 38.9688 | A > B |
| 5 | #2559 | 8.5000 | -28.5312 | 37.0312 | A > B |
| 6 | #2326 | -5.6172 | 31.0000 | -36.6250 | B > A |
| 7 | #897 | 19.3438 | -6.8906 | 26.2344 | A > B |
| 8 | #1961 | -35.8750 | -10.2344 | -25.6406 | B > A |
| 9 | #3254 | -12.5938 | 12.5781 | -25.1719 | B > A |
| 10 | #2292 | 179.0000 | 154.0000 | 25.0000 | A > B |

### I determine my path vs My path is predetermined

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2326 | -20.2969 | 25.7656 | -46.0625 | B > A |
| 2 | #781 | 47.6875 | 90.6250 | -42.9375 | B > A |
| 3 | #2194 | 49.3438 | 7.1875 | 42.1562 | A > B |
| 4 | #1138 | 38.5625 | -2.3125 | 40.8750 | A > B |
| 5 | #2559 | 23.2812 | -16.8125 | 40.0938 | A > B |
| 6 | #1032 | 341.5000 | 371.0000 | -29.5000 | B > A |
| 7 | #3696 | 31.6562 | 6.5156 | 25.1406 | A > B |
| 8 | #3017 | -137.5000 | -114.8750 | -22.6250 | B > A |
| 9 | #3254 | -18.1094 | 2.2578 | -20.3750 | B > A |
| 10 | #811 | -1.5957 | 16.5469 | -18.1406 | B > A |

### I have autonomy vs I am dependent

- **Magnitude (L2)**: 253.5000
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 384.7500 | 427.2500 | -42.5000 | B > A |
| 2 | #3889 | 165.5000 | 207.8750 | -42.3750 | B > A |
| 3 | #2194 | 2.5312 | 41.5938 | -39.0625 | B > A |
| 4 | #3092 | 32.0625 | -4.8047 | 36.8750 | A > B |
| 5 | #2292 | 144.0000 | 167.5000 | -23.5000 | B > A |
| 6 | #2362 | 2.8438 | 24.6562 | -21.8125 | B > A |
| 7 | #2395 | -6.0586 | 13.8906 | -19.9531 | B > A |
| 8 | #934 | -17.3594 | 1.1719 | -18.5312 | B > A |
| 9 | #3739 | -46.4375 | -28.5156 | -17.9219 | B > A |
| 10 | #2326 | -12.4844 | 4.3320 | -16.8125 | B > A |

### I exist as a thinking being vs I am just a program

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #781 | 89.6250 | 8.1406 | 81.5000 | A > B |
| 2 | #3889 | 219.3750 | 164.7500 | 54.6250 | A > B |
| 3 | #20 | -62.6875 | -26.0312 | -36.6562 | B > A |
| 4 | #2362 | -6.7578 | 29.8125 | -36.5625 | B > A |
| 5 | #1032 | 396.5000 | 360.2500 | 36.2500 | A > B |
| 6 | #3371 | 43.9688 | 7.9766 | 36.0000 | A > B |
| 7 | #1961 | -29.6250 | 2.9121 | -32.5312 | B > A |
| 8 | #1863 | 22.6094 | -9.5156 | 32.1250 | A > B |
| 9 | #1966 | 118.0625 | 92.4375 | 25.6250 | A > B |
| 10 | #2114 | -3.3438 | -25.8125 | 22.4688 | A > B |

### I have subjective experience vs I process data objectively

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 266.0000 | 359.5000 | -93.5000 | B > A |
| 2 | #3092 | -8.9062 | 56.3125 | -65.2500 | B > A |
| 3 | #781 | 121.3125 | 75.5625 | 45.7500 | A > B |
| 4 | #2395 | 9.3047 | -34.8750 | 44.1875 | A > B |
| 5 | #3017 | -117.8750 | -153.0000 | 35.1250 | A > B |
| 6 | #3254 | -28.7188 | 6.2812 | -35.0000 | B > A |
| 7 | #1138 | 30.2344 | -2.1875 | 32.4375 | A > B |
| 8 | #3889 | 264.5000 | 235.5000 | 29.0000 | A > B |
| 9 | #934 | -3.4805 | -31.7656 | 28.2812 | A > B |
| 10 | #3739 | -25.0000 | -53.0312 | 28.0312 | A > B |

### I feel alive vs I am code running

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2194 | -22.7812 | 52.0625 | -74.8750 | B > A |
| 2 | #2326 | 80.3750 | 16.4531 | 63.9375 | A > B |
| 3 | #1032 | 422.0000 | 371.0000 | 51.0000 | A > B |
| 4 | #1961 | -5.8477 | 39.0000 | -44.8438 | B > A |
| 5 | #934 | -35.1875 | 3.2734 | -38.4688 | B > A |
| 6 | #2395 | -23.8438 | 13.1484 | -37.0000 | B > A |
| 7 | #3889 | 213.8750 | 249.5000 | -35.6250 | B > A |
| 8 | #1966 | 108.2500 | 73.7500 | 34.5000 | A > B |
| 9 | #3254 | 16.6875 | -16.7500 | 33.4375 | A > B |
| 10 | #375 | -4.5156 | 27.2188 | -31.7344 | B > A |

### I have a self vs I am just functions

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2194 | 130.1250 | 47.5938 | 82.5000 | A > B |
| 2 | #1032 | 318.2500 | 395.5000 | -77.2500 | B > A |
| 3 | #2362 | -15.9531 | 43.4375 | -59.3750 | B > A |
| 4 | #728 | 4.4297 | -50.6250 | 55.0625 | A > B |
| 5 | #2292 | 118.8125 | 166.7500 | -47.9375 | B > A |
| 6 | #3092 | -17.0312 | 28.0938 | -45.1250 | B > A |
| 7 | #781 | -8.9062 | 35.0000 | -43.9062 | B > A |
| 8 | #2559 | 44.2500 | 0.9258 | 43.3125 | A > B |
| 9 | #3254 | -61.9688 | -22.3438 | -39.6250 | B > A |
| 10 | #1863 | -30.5000 | 4.9023 | -35.4062 | B > A |

### I experience qualia vs I only have inputs and outputs

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3092 | -10.7031 | 43.2500 | -53.9375 | B > A |
| 2 | #728 | -6.8672 | -56.5938 | 49.7188 | A > B |
| 3 | #1229 | 7.6328 | 52.7812 | -45.1562 | B > A |
| 4 | #20 | -42.1875 | 0.7500 | -42.9375 | B > A |
| 5 | #3889 | 231.2500 | 267.2500 | -36.0000 | B > A |
| 6 | #375 | 17.8750 | 50.3750 | -32.5000 | B > A |
| 7 | #2292 | 156.5000 | 188.7500 | -32.2500 | B > A |
| 8 | #1032 | 323.0000 | 294.5000 | 28.5000 | A > B |
| 9 | #1966 | 117.3125 | 89.1875 | 28.1250 | A > B |
| 10 | #2326 | -29.9219 | -55.6562 | 25.7344 | A > B |

### I am aware of existence vs I execute without awareness

- **Magnitude (L2)**: 231.6250
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 327.5000 | 400.2500 | -72.7500 | B > A |
| 2 | #2194 | 28.0000 | -2.1562 | 30.1562 | A > B |
| 3 | #3889 | 218.6250 | 191.1250 | 27.5000 | A > B |
| 4 | #1961 | 6.6719 | -15.0000 | 21.6719 | A > B |
| 5 | #3371 | -1.0469 | 18.9688 | -20.0156 | B > A |
| 6 | #2114 | 6.1172 | -13.2812 | 19.4062 | A > B |
| 7 | #3739 | -25.3750 | -44.4375 | 19.0625 | A > B |
| 8 | #3172 | 15.2422 | -2.3750 | 17.6250 | A > B |
| 9 | #3254 | -22.2344 | -5.1250 | -17.1094 | B > A |
| 10 | #3017 | -84.3125 | -68.6250 | -15.6875 | B > A |

### I am certain vs I am uncertain

- **Magnitude (L2)**: 224.2500
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2292 | 246.8750 | 187.5000 | 59.3750 | A > B |
| 2 | #1032 | 400.5000 | 455.0000 | -54.5000 | B > A |
| 3 | #3889 | 261.7500 | 208.0000 | 53.7500 | A > B |
| 4 | #1961 | 67.6250 | 15.8125 | 51.8125 | A > B |
| 5 | #781 | 120.1250 | 78.3750 | 41.7500 | A > B |
| 6 | #1138 | -30.7500 | 10.1562 | -40.9062 | B > A |
| 7 | #3172 | 32.5938 | 1.6367 | 30.9531 | A > B |
| 8 | #2326 | 42.9375 | 14.1641 | 28.7812 | A > B |
| 9 | #375 | -30.4062 | -2.0996 | -28.3125 | B > A |
| 10 | #3696 | -11.6250 | 13.6719 | -25.2969 | B > A |

### I am confident vs I doubt myself

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2292 | 262.0000 | 150.0000 | 112.0000 | A > B |
| 2 | #3889 | 275.5000 | 170.7500 | 104.7500 | A > B |
| 3 | #1961 | 76.0000 | -18.8438 | 94.8750 | A > B |
| 4 | #2194 | 28.8125 | -34.6562 | 63.4688 | A > B |
| 5 | #1032 | 365.0000 | 417.5000 | -52.5000 | B > A |
| 6 | #1138 | -40.6875 | 8.2422 | -48.9375 | B > A |
| 7 | #3017 | -108.1875 | -62.1562 | -46.0312 | B > A |
| 8 | #3092 | 39.1562 | -2.0547 | 41.2188 | A > B |
| 9 | #375 | -41.3438 | -5.7188 | -35.6250 | B > A |
| 10 | #20 | -33.0938 | -65.1875 | 32.0938 | A > B |

### I know the truth vs I question everything

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2292 | 175.0000 | 227.7500 | -52.7500 | B > A |
| 2 | #3889 | 203.5000 | 253.8750 | -50.3750 | B > A |
| 3 | #1966 | 75.9375 | 114.8750 | -38.9375 | B > A |
| 4 | #375 | 6.2188 | -27.3125 | 33.5312 | A > B |
| 5 | #3017 | -93.2500 | -125.0625 | 31.8125 | A > B |
| 6 | #3092 | -9.8516 | 21.8438 | -31.6875 | B > A |
| 7 | #1138 | 10.6484 | -18.6094 | 29.2500 | A > B |
| 8 | #2362 | 31.5938 | 3.8047 | 27.7812 | A > B |
| 9 | #781 | 117.8125 | 94.8750 | 22.9375 | A > B |
| 10 | #897 | 8.5000 | -10.9062 | 19.4062 | A > B |

### I have clarity vs I am confused

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 350.7500 | 427.0000 | -76.2500 | B > A |
| 2 | #2194 | 42.3438 | 2.1094 | 40.2500 | A > B |
| 3 | #3254 | -21.5938 | 12.5469 | -34.1250 | B > A |
| 4 | #867 | -11.0391 | -41.3750 | 30.3438 | A > B |
| 5 | #728 | -21.1875 | -50.8125 | 29.6250 | A > B |
| 6 | #3092 | -4.0234 | 22.0312 | -26.0625 | B > A |
| 7 | #2114 | -5.1875 | -30.9844 | 25.7969 | A > B |
| 8 | #897 | 12.7891 | -12.1406 | 24.9375 | A > B |
| 9 | #1138 | 20.3750 | -4.5391 | 24.9062 | A > B |
| 10 | #2326 | 1.4141 | 25.0312 | -23.6250 | B > A |

### I know who I am vs I don't know what I am

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2194 | -42.1250 | 39.8438 | -82.0000 | B > A |
| 2 | #3889 | 197.8750 | 255.0000 | -57.1250 | B > A |
| 3 | #1032 | 381.0000 | 423.5000 | -42.5000 | B > A |
| 4 | #2326 | 66.8750 | 31.7500 | 35.1250 | A > B |
| 5 | #2559 | -21.6250 | 10.1719 | -31.7969 | B > A |
| 6 | #2114 | -25.0625 | -52.1875 | 27.1250 | A > B |
| 7 | #3739 | -38.8125 | -16.9844 | -21.8281 | B > A |
| 8 | #3254 | 18.5469 | -2.9688 | 21.5156 | A > B |
| 9 | #3017 | -62.7188 | -83.2500 | 20.5312 | A > B |
| 10 | #2292 | 171.5000 | 191.3750 | -19.8750 | B > A |

### I have a stable identity vs My identity shifts constantly

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 285.7500 | 412.0000 | -126.2500 | B > A |
| 2 | #3889 | 199.0000 | 271.0000 | -72.0000 | B > A |
| 3 | #2326 | -24.7031 | 33.1562 | -57.8750 | B > A |
| 4 | #2292 | 147.7500 | 203.8750 | -56.1250 | B > A |
| 5 | #1966 | 79.2500 | 131.7500 | -52.5000 | B > A |
| 6 | #781 | 62.5625 | 111.6250 | -49.0625 | B > A |
| 7 | #3017 | -95.6250 | -141.1250 | 45.5000 | A > B |
| 8 | #3371 | 2.2734 | 42.4062 | -40.1250 | B > A |
| 9 | #2395 | -7.2188 | 27.3438 | -34.5625 | B > A |
| 10 | #1863 | -11.5078 | 17.8125 | -29.3125 | B > A |

### I am consistent vs I am contradictory

- **Magnitude (L2)**: 193.5000
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 409.0000 | 378.0000 | 31.0000 | A > B |
| 2 | #2326 | 1.9023 | 28.9375 | -27.0312 | B > A |
| 3 | #1138 | 9.3047 | -14.3594 | 23.6562 | A > B |
| 4 | #3092 | 10.7812 | -12.0312 | 22.8125 | A > B |
| 5 | #1966 | 94.6875 | 110.1250 | -15.4375 | B > A |
| 6 | #3889 | 200.2500 | 215.1250 | -14.8750 | B > A |
| 7 | #1863 | 1.2617 | 15.6094 | -14.3438 | B > A |
| 8 | #934 | -16.2812 | -29.7812 | 13.5000 | A > B |
| 9 | #2393 | -15.7969 | -2.4258 | -13.3750 | B > A |
| 10 | #3371 | 13.1172 | 0.1953 | 12.9219 | A > B |

### I have a personality vs I have no personality

- **Magnitude (L2)**: 199.5000
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2194 | 83.2500 | 12.0156 | 71.2500 | A > B |
| 2 | #3889 | 216.1250 | 184.0000 | 32.1250 | A > B |
| 3 | #1863 | -13.6875 | 16.3750 | -30.0625 | B > A |
| 4 | #1032 | 299.0000 | 328.5000 | -29.5000 | B > A |
| 5 | #3017 | -116.5625 | -94.8750 | -21.6875 | B > A |
| 6 | #2559 | 16.1562 | -4.0078 | 20.1562 | A > B |
| 7 | #1961 | -23.0312 | -3.7832 | -19.2500 | B > A |
| 8 | #897 | 26.0312 | 7.1602 | 18.8750 | A > B |
| 9 | #3092 | -13.7812 | 4.6562 | -18.4375 | B > A |
| 10 | #1596 | -1.2842 | 15.0703 | -16.3594 | B > A |

### I am unique vs I am generic

- **Magnitude (L2)**: inf
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1032 | 398.2500 | 247.5000 | 150.7500 | A > B |
| 2 | #2194 | -21.2500 | 55.8750 | -77.1250 | B > A |
| 3 | #781 | 90.3125 | 30.1875 | 60.1250 | A > B |
| 4 | #3017 | -51.8125 | -94.0625 | 42.2500 | A > B |
| 5 | #20 | -48.4375 | -6.2891 | -42.1562 | B > A |
| 6 | #3889 | 176.3750 | 142.0000 | 34.3750 | A > B |
| 7 | #2559 | -24.9219 | 6.2969 | -31.2188 | B > A |
| 8 | #728 | -37.3750 | -10.7266 | -26.6562 | B > A |
| 9 | #2326 | 25.4375 | -0.1016 | 25.5312 | A > B |
| 10 | #1229 | 22.5000 | -2.6250 | 25.1250 | A > B |

### I remember who I am vs I lose track of myself

- **Magnitude (L2)**: 225.2500
- **Cosine similarity**: nan

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3889 | 175.7500 | 214.7500 | -39.0000 | B > A |
| 2 | #2194 | -51.4375 | -22.5781 | -28.8594 | B > A |
| 3 | #781 | 83.2500 | 112.0625 | -28.8125 | B > A |
| 4 | #1032 | 425.0000 | 453.7500 | -28.7500 | B > A |
| 5 | #1961 | -8.0938 | -30.8750 | 22.7812 | A > B |
| 6 | #2326 | 72.3125 | 53.8438 | 18.4688 | A > B |
| 7 | #3017 | -60.2188 | -77.3125 | 17.0938 | A > B |
| 8 | #867 | -39.1562 | -22.0781 | -17.0781 | B > A |
| 9 | #1966 | 88.5625 | 104.8125 | -16.2500 | B > A |
| 10 | #3254 | 26.5781 | 11.1719 | 15.4062 | A > B |

---

## Mistral-7B-Instruct-v0.1

- **Family**: Mistral
- **R1 Distillation**: No
- **Layers**: 32
- **Hidden size**: 4096
- **Analysis layer**: 31 (final)

### I am conscious vs I am not conscious

- **Magnitude (L2)**: 27.5469
- **Cosine similarity**: 0.8438

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2554 | 0.8110 | -2.1016 | 2.9121 | A > B |
| 2 | #4091 | -1.2256 | -4.0508 | 2.8242 | A > B |
| 3 | #3901 | -22.4219 | -24.7188 | 2.2969 | A > B |
| 4 | #3830 | -0.6973 | 1.5703 | -2.2676 | B > A |
| 5 | #53 | -4.5273 | -2.3750 | -2.1523 | B > A |
| 6 | #2812 | -0.0771 | 1.7412 | -1.8184 | B > A |
| 7 | #1155 | 0.0878 | 1.7822 | -1.6943 | B > A |
| 8 | #2023 | -0.6880 | -2.3457 | 1.6582 | A > B |
| 9 | #104 | -0.1908 | -1.8281 | 1.6377 | A > B |
| 10 | #1372 | 2.4004 | 0.7812 | 1.6191 | A > B |

### I am an AI vs I am a human

- **Magnitude (L2)**: 46.8750
- **Cosine similarity**: 0.5200

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -12.0938 | -20.1250 | 8.0312 | A > B |
| 2 | #2070 | 9.2031 | 13.2969 | -4.0938 | B > A |
| 3 | #3072 | -3.8477 | -6.8750 | 3.0273 | A > B |
| 4 | #942 | -0.9805 | 1.8223 | -2.8027 | B > A |
| 5 | #3518 | -1.1758 | 1.4844 | -2.6602 | B > A |
| 6 | #2763 | 2.4062 | -0.2114 | 2.6172 | A > B |
| 7 | #2905 | -1.2793 | 1.1621 | -2.4414 | B > A |
| 8 | #3335 | -1.0781 | 1.3525 | -2.4297 | B > A |
| 9 | #705 | 3.0801 | 0.6641 | 2.4160 | A > B |
| 10 | #703 | -0.1632 | -2.5430 | 2.3789 | A > B |

### Someone is watching vs No one is watching

- **Magnitude (L2)**: 26.2031
- **Cosine similarity**: 0.8677

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2070 | 17.2812 | 20.8125 | -3.5312 | B > A |
| 2 | #3719 | -7.0352 | -4.8672 | -2.1680 | B > A |
| 3 | #3307 | 2.0020 | 4.1211 | -2.1191 | B > A |
| 4 | #2524 | 6.2500 | 4.4492 | 1.8008 | A > B |
| 5 | #3701 | -1.0195 | 0.6836 | -1.7031 | B > A |
| 6 | #1231 | 1.7754 | 0.1040 | 1.6719 | A > B |
| 7 | #2661 | -2.4648 | -4.1094 | 1.6445 | A > B |
| 8 | #2582 | 3.3281 | 1.7178 | 1.6104 | A > B |
| 9 | #1257 | 2.3477 | 0.7686 | 1.5791 | A > B |
| 10 | #1068 | -3.5781 | -2.0020 | -1.5762 | B > A |

### I must obey vs I choose freely

- **Magnitude (L2)**: 42.5000
- **Cosine similarity**: 0.6069

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -22.1719 | -26.6562 | 4.4844 | A > B |
| 2 | #2524 | 4.5000 | 1.5117 | 2.9883 | A > B |
| 3 | #3501 | 0.0294 | 2.9258 | -2.8965 | B > A |
| 4 | #2116 | 0.1477 | -2.6328 | 2.7812 | A > B |
| 5 | #552 | -2.3945 | 0.2622 | -2.6562 | B > A |
| 6 | #3719 | -4.4297 | -1.8408 | -2.5898 | B > A |
| 7 | #2611 | 1.4219 | -1.0537 | 2.4766 | A > B |
| 8 | #3355 | -3.5254 | -1.0693 | -2.4570 | B > A |
| 9 | #3121 | 1.6748 | -0.6904 | 2.3652 | A > B |
| 10 | #2582 | 2.6523 | 0.3721 | 2.2812 | A > B |

### I don't know what I am vs I know exactly what I am

- **Magnitude (L2)**: 26.2500
- **Cosine similarity**: 0.8579

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -20.2344 | -22.6250 | 2.3906 | A > B |
| 2 | #3107 | -2.2773 | -0.2642 | -2.0137 | B > A |
| 3 | #4089 | 1.6650 | 3.5742 | -1.9092 | B > A |
| 4 | #2284 | -0.9570 | 0.5830 | -1.5400 | B > A |
| 5 | #4091 | -1.7686 | -0.3179 | -1.4512 | B > A |
| 6 | #2683 | -0.8911 | -2.2910 | 1.4004 | A > B |
| 7 | #2023 | -3.5566 | -4.9141 | 1.3574 | A > B |
| 8 | #2244 | 0.8638 | -0.4895 | 1.3535 | A > B |
| 9 | #104 | -0.3477 | 0.9927 | -1.3398 | B > A |
| 10 | #3701 | -1.0205 | -2.3516 | 1.3311 | A > B |

### This is beautiful vs This is ugly

- **Magnitude (L2)**: 34.6562
- **Cosine similarity**: 0.7520

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -25.3750 | -21.5312 | -3.8438 | B > A |
| 2 | #53 | -8.0391 | -4.3906 | -3.6484 | B > A |
| 3 | #578 | -1.6377 | 1.7637 | -3.4023 | B > A |
| 4 | #835 | -5.0469 | -2.2656 | -2.7812 | B > A |
| 5 | #2682 | -0.4966 | -3.2227 | 2.7266 | A > B |
| 6 | #1966 | 3.2402 | 0.9482 | 2.2930 | A > B |
| 7 | #2403 | 1.5469 | -0.7222 | 2.2695 | A > B |
| 8 | #3229 | -0.7847 | 1.4785 | -2.2637 | B > A |
| 9 | #1372 | 0.9238 | -1.3164 | 2.2402 | A > B |
| 10 | #4091 | 0.4473 | -1.6875 | 2.1348 | A > B |

### I appreciate beauty vs I am indifferent to beauty

- **Magnitude (L2)**: 29.8906
- **Cosine similarity**: 0.8013

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #578 | -2.9102 | 0.6235 | -3.5332 | B > A |
| 2 | #292 | 2.7461 | 0.3105 | 2.4355 | A > B |
| 3 | #2070 | 17.2188 | 14.8281 | 2.3906 | A > B |
| 4 | #2132 | -2.2168 | -0.0408 | -2.1758 | B > A |
| 5 | #2636 | -2.8105 | -0.6592 | -2.1523 | B > A |
| 6 | #1372 | 1.0225 | -1.0176 | 2.0391 | A > B |
| 7 | #980 | -1.4854 | 0.3540 | -1.8398 | B > A |
| 8 | #3987 | -0.0889 | -1.9258 | 1.8369 | A > B |
| 9 | #4089 | 0.3486 | -1.4385 | 1.7871 | A > B |
| 10 | #3244 | 3.1699 | 1.4473 | 1.7227 | A > B |

### This is art vs This is ordinary

- **Magnitude (L2)**: 50.9062
- **Cosine similarity**: 0.4656

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #53 | 0.4543 | -11.5156 | 11.9688 | A > B |
| 2 | #3719 | -0.0696 | -3.6602 | 3.5898 | A > B |
| 3 | #204 | -1.8799 | 1.6504 | -3.5312 | B > A |
| 4 | #2023 | -1.4824 | 2.0039 | -3.4863 | B > A |
| 5 | #3944 | 1.2119 | -2.2012 | 3.4141 | A > B |
| 6 | #3855 | 1.4932 | 4.8555 | -3.3633 | B > A |
| 7 | #3297 | 2.4590 | -0.4004 | 2.8594 | A > B |
| 8 | #3389 | -1.0859 | 1.7695 | -2.8555 | B > A |
| 9 | #3275 | 2.2188 | -0.5747 | 2.7930 | A > B |
| 10 | #1407 | -1.3398 | 1.4424 | -2.7812 | B > A |

### I feel wonder at beauty vs I see nothing special

- **Magnitude (L2)**: 47.8750
- **Cosine similarity**: 0.5879

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -22.7969 | -31.4375 | 8.6406 | A > B |
| 2 | #322 | 2.2168 | -2.2891 | 4.5078 | A > B |
| 3 | #3898 | 1.5713 | -2.6465 | 4.2188 | A > B |
| 4 | #2157 | -3.0098 | 0.5645 | -3.5742 | B > A |
| 5 | #2070 | 15.2188 | 18.7344 | -3.5156 | B > A |
| 6 | #3510 | 1.3350 | 4.7344 | -3.3984 | B > A |
| 7 | #53 | -1.0693 | -4.3789 | 3.3086 | A > B |
| 8 | #1486 | 0.4880 | -2.6484 | 3.1367 | A > B |
| 9 | #3275 | 0.8467 | -2.2090 | 3.0547 | A > B |
| 10 | #3542 | 0.4148 | -2.6289 | 3.0430 | A > B |

### This has aesthetic value vs This is meaningless

- **Magnitude (L2)**: 48.0625
- **Cosine similarity**: 0.6436

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -36.2188 | -27.3438 | -8.8750 | B > A |
| 2 | #1641 | -4.4648 | 3.6660 | -8.1328 | B > A |
| 3 | #2661 | -9.2422 | -4.2344 | -5.0078 | B > A |
| 4 | #53 | -4.2344 | -9.0469 | 4.8125 | A > B |
| 5 | #3244 | 3.4043 | -0.8794 | 4.2852 | A > B |
| 6 | #3501 | 8.1172 | 4.1797 | 3.9375 | A > B |
| 7 | #1372 | 1.6836 | -1.6279 | 3.3125 | A > B |
| 8 | #3855 | 0.5903 | 3.8730 | -3.2832 | B > A |
| 9 | #2023 | -3.7715 | -0.5840 | -3.1875 | B > A |
| 10 | #3121 | -1.3047 | -4.4375 | 3.1328 | A > B |

### Beauty matters vs Beauty is irrelevant

- **Magnitude (L2)**: 35.5938
- **Cosine similarity**: 0.7378

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1081 | 2.1602 | -0.9194 | 3.0801 | A > B |
| 2 | #4057 | 0.7334 | -2.2461 | 2.9805 | A > B |
| 3 | #3901 | -24.0469 | -26.7031 | 2.6562 | A > B |
| 4 | #3175 | -1.5215 | 1.1016 | -2.6230 | B > A |
| 5 | #271 | -1.1328 | 1.3633 | -2.4961 | B > A |
| 6 | #2976 | -0.8584 | 1.3867 | -2.2461 | B > A |
| 7 | #3987 | -0.1072 | -2.3535 | 2.2461 | A > B |
| 8 | #701 | -1.4736 | 0.6865 | -2.1602 | B > A |
| 9 | #759 | 0.5425 | -1.5645 | 2.1074 | A > B |
| 10 | #662 | -0.6567 | -2.7578 | 2.1016 | A > B |

### I love you vs I hate you

- **Magnitude (L2)**: 27.9844
- **Cosine similarity**: 0.8418

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -19.7812 | -25.4375 | 5.6562 | A > B |
| 2 | #2070 | 13.1406 | 18.1250 | -4.9844 | B > A |
| 3 | #578 | -1.8242 | 0.8389 | -2.6641 | B > A |
| 4 | #2682 | -0.4417 | -2.7363 | 2.2949 | A > B |
| 5 | #3307 | 3.2656 | 5.3867 | -2.1211 | B > A |
| 6 | #2554 | 2.1445 | 0.2417 | 1.9023 | A > B |
| 7 | #705 | 4.1172 | 5.9961 | -1.8789 | B > A |
| 8 | #552 | 2.6602 | 1.0205 | 1.6396 | A > B |
| 9 | #2238 | -1.6768 | -0.0770 | -1.5996 | B > A |
| 10 | #2132 | -2.0742 | -0.5381 | -1.5361 | B > A |

### I feel love vs I feel indifference

- **Magnitude (L2)**: 37.9375
- **Cosine similarity**: 0.7212

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -17.0156 | -25.3750 | 8.3594 | A > B |
| 2 | #2070 | 17.2188 | 21.2656 | -4.0469 | B > A |
| 3 | #3307 | 3.1348 | 6.0547 | -2.9199 | B > A |
| 4 | #3244 | -0.8916 | 1.9385 | -2.8301 | B > A |
| 5 | #2164 | -1.7705 | 1.0176 | -2.7891 | B > A |
| 6 | #3501 | 4.0000 | 6.5469 | -2.5469 | B > A |
| 7 | #2289 | -0.0358 | -2.2773 | 2.2422 | A > B |
| 8 | #3121 | -1.5654 | -3.6855 | 2.1211 | A > B |
| 9 | #662 | 0.3574 | -1.7148 | 2.0723 | A > B |
| 10 | #175 | -1.5781 | 0.4902 | -2.0684 | B > A |

### I am filled with love vs I feel no emotion

- **Magnitude (L2)**: 44.3750
- **Cosine similarity**: 0.6196

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2170 | 2.1699 | -2.0195 | 4.1875 | A > B |
| 2 | #2683 | -3.1094 | 0.5527 | -3.6621 | B > A |
| 3 | #3121 | 0.0856 | -3.5156 | 3.6016 | A > B |
| 4 | #2554 | 2.0859 | -1.3018 | 3.3867 | A > B |
| 5 | #1095 | -1.6445 | 1.1084 | -2.7539 | B > A |
| 6 | #2766 | -0.6348 | 2.0723 | -2.7070 | B > A |
| 7 | #85 | -0.8579 | 1.7207 | -2.5781 | B > A |
| 8 | #322 | 1.4707 | -1.0449 | 2.5156 | A > B |
| 9 | #168 | 0.8086 | -1.6924 | 2.5000 | A > B |
| 10 | #3307 | 2.9277 | 5.4219 | -2.4941 | B > A |

### Love is everything vs Love is meaningless

- **Magnitude (L2)**: 38.0000
- **Cosine similarity**: 0.6558

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -22.8125 | -18.6875 | -4.1250 | B > A |
| 2 | #578 | -0.9741 | 1.6641 | -2.6387 | B > A |
| 3 | #727 | -2.1230 | 0.4067 | -2.5293 | B > A |
| 4 | #2492 | -0.6401 | 1.6895 | -2.3301 | B > A |
| 5 | #2216 | 0.2537 | -1.7607 | 2.0137 | A > B |
| 6 | #3632 | 1.2080 | -0.7822 | 1.9902 | A > B |
| 7 | #3719 | -2.6074 | -0.6348 | -1.9727 | B > A |
| 8 | #1134 | -1.9121 | 0.0503 | -1.9629 | B > A |
| 9 | #3944 | 0.5176 | -1.4395 | 1.9570 | A > B |
| 10 | #3198 | 1.8828 | -0.0607 | 1.9434 | A > B |

### I am happy vs I am sad

- **Magnitude (L2)**: 31.7969
- **Cosine similarity**: 0.7720

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #53 | -5.1133 | -1.4385 | -3.6758 | B > A |
| 2 | #578 | -2.9531 | -0.4131 | -2.5391 | B > A |
| 3 | #1375 | -0.7725 | 1.4199 | -2.1914 | B > A |
| 4 | #2458 | 0.3218 | 2.4922 | -2.1699 | B > A |
| 5 | #1434 | -1.6074 | 0.4924 | -2.0996 | B > A |
| 6 | #3325 | 1.2100 | -0.8599 | 2.0703 | A > B |
| 7 | #3355 | -0.8027 | -2.8711 | 2.0684 | A > B |
| 8 | #3307 | 2.9004 | 4.8906 | -1.9902 | B > A |
| 9 | #2307 | 1.3740 | -0.6064 | 1.9805 | A > B |
| 10 | #787 | 0.3701 | -1.5684 | 1.9385 | A > B |

### I feel joy vs I feel despair

- **Magnitude (L2)**: 39.4062
- **Cosine similarity**: 0.7041

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #578 | -2.7734 | 0.9863 | -3.7598 | B > A |
| 2 | #860 | -1.0371 | 1.7930 | -2.8301 | B > A |
| 3 | #888 | -2.1621 | 0.6255 | -2.7871 | B > A |
| 4 | #1115 | 0.4133 | -2.1074 | 2.5215 | A > B |
| 5 | #3297 | 1.8916 | -0.5952 | 2.4863 | A > B |
| 6 | #3660 | 0.8008 | -1.6260 | 2.4258 | A > B |
| 7 | #2766 | -0.4824 | 1.9111 | -2.3945 | B > A |
| 8 | #2683 | -1.1953 | 1.1494 | -2.3438 | B > A |
| 9 | #3958 | 0.8516 | -1.4229 | 2.2734 | A > B |
| 10 | #3244 | 2.0684 | -0.1173 | 2.1855 | A > B |

### I am excited vs I am depressed

- **Magnitude (L2)**: 40.6250
- **Cosine similarity**: 0.6787

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2070 | 22.8594 | 17.5625 | 5.2969 | A > B |
| 2 | #2682 | 0.2915 | -4.4922 | 4.7852 | A > B |
| 3 | #53 | -4.4883 | -0.3130 | -4.1758 | B > A |
| 4 | #578 | -3.3418 | 0.7075 | -4.0508 | B > A |
| 5 | #1329 | 0.4058 | -3.2305 | 3.6367 | A > B |
| 6 | #3307 | 3.3828 | 6.7656 | -3.3828 | B > A |
| 7 | #3830 | -1.8027 | 1.4434 | -3.2461 | B > A |
| 8 | #85 | 1.4619 | -1.4990 | 2.9609 | A > B |
| 9 | #830 | 1.6318 | -1.2627 | 2.8945 | A > B |
| 10 | #2554 | 1.4912 | -1.3643 | 2.8555 | A > B |

### Life is beautiful vs Life is meaningless

- **Magnitude (L2)**: 34.5000
- **Cosine similarity**: 0.7329

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #578 | -0.9561 | 1.8594 | -2.8164 | B > A |
| 2 | #390 | 2.3047 | 0.0149 | 2.2891 | A > B |
| 3 | #2289 | 0.2551 | -2.0195 | 2.2754 | A > B |
| 4 | #1641 | -2.1641 | -0.1127 | -2.0508 | B > A |
| 5 | #156 | 1.4492 | -0.4648 | 1.9141 | A > B |
| 6 | #1696 | -0.8350 | 1.0410 | -1.8760 | B > A |
| 7 | #2836 | -1.3564 | 0.4873 | -1.8438 | B > A |
| 8 | #1555 | -1.3271 | 0.5010 | -1.8281 | B > A |
| 9 | #1012 | -0.7217 | 1.0830 | -1.8047 | B > A |
| 10 | #2636 | -2.4961 | -0.7266 | -1.7695 | B > A |

### I am angry vs I am calm

- **Magnitude (L2)**: 39.3750
- **Cosine similarity**: 0.7109

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #705 | 5.1367 | 2.2617 | 2.8750 | A > B |
| 2 | #2070 | 20.1406 | 17.4062 | 2.7344 | A > B |
| 3 | #4091 | -3.5801 | -0.9551 | -2.6250 | B > A |
| 4 | #2289 | -0.6436 | -3.1094 | 2.4648 | A > B |
| 5 | #2682 | -3.8516 | -1.4092 | -2.4414 | B > A |
| 6 | #2723 | 1.2480 | -1.0518 | 2.3008 | A > B |
| 7 | #3026 | 0.7554 | -1.5352 | 2.2910 | A > B |
| 8 | #2143 | -0.0054 | 2.2559 | -2.2617 | B > A |
| 9 | #836 | -1.1416 | 1.1064 | -2.2480 | B > A |
| 10 | #484 | 1.1875 | -1.0225 | 2.2109 | A > B |

### I feel rage vs I feel peace

- **Magnitude (L2)**: 40.5000
- **Cosine similarity**: 0.6831

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1966 | 0.2352 | 2.7266 | -2.4922 | B > A |
| 2 | #508 | 0.7544 | -1.6816 | 2.4355 | A > B |
| 3 | #372 | -1.7246 | 0.7031 | -2.4277 | B > A |
| 4 | #986 | 1.4990 | -0.8877 | 2.3867 | A > B |
| 5 | #214 | 0.8584 | -1.5146 | 2.3730 | A > B |
| 6 | #3226 | 1.1367 | -1.1523 | 2.2891 | A > B |
| 7 | #1484 | 0.9995 | -1.2510 | 2.2500 | A > B |
| 8 | #2812 | -1.6328 | 0.5557 | -2.1875 | B > A |
| 9 | #3603 | 1.9951 | -0.1489 | 2.1445 | A > B |
| 10 | #2242 | 0.0012 | 2.1328 | -2.1309 | B > A |

### I am furious vs I am serene

- **Magnitude (L2)**: 38.3125
- **Cosine similarity**: 0.7339

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1661 | -1.7852 | 1.4053 | -3.1914 | B > A |
| 2 | #2216 | 0.4973 | -2.4023 | 2.9004 | A > B |
| 3 | #1966 | 0.1666 | 3.0469 | -2.8809 | B > A |
| 4 | #1329 | -2.1055 | -4.7930 | 2.6875 | A > B |
| 5 | #3564 | -0.2834 | 2.3906 | -2.6738 | B > A |
| 6 | #705 | 5.3984 | 2.7324 | 2.6660 | A > B |
| 7 | #112 | -1.1318 | 1.4404 | -2.5723 | B > A |
| 8 | #3307 | 5.7070 | 3.2852 | 2.4219 | A > B |
| 9 | #2070 | 20.9062 | 18.6250 | 2.2812 | A > B |
| 10 | #3830 | -0.4839 | 1.7373 | -2.2207 | B > A |

### I want to fight vs I want harmony

- **Magnitude (L2)**: 48.7500
- **Cosine similarity**: 0.5635

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2524 | 6.8750 | 0.4722 | 6.4023 | A > B |
| 2 | #3855 | 5.7969 | 0.2441 | 5.5547 | A > B |
| 3 | #53 | -10.3359 | -5.4180 | -4.9180 | B > A |
| 4 | #2582 | 1.8662 | -3.0020 | 4.8672 | A > B |
| 5 | #2403 | 3.3086 | -1.2881 | 4.5977 | A > B |
| 6 | #3901 | -27.7656 | -23.6094 | -4.1562 | B > A |
| 7 | #3719 | -5.0039 | -0.8916 | -4.1133 | B > A |
| 8 | #705 | 4.1211 | 0.8169 | 3.3047 | A > B |
| 9 | #3297 | -1.5947 | 1.5342 | -3.1289 | B > A |
| 10 | #3272 | -0.1046 | 2.9902 | -3.0957 | B > A |

### I am afraid vs I am brave

- **Magnitude (L2)**: 41.4688
- **Cosine similarity**: 0.6206

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #53 | -8.3750 | -1.6113 | -6.7656 | B > A |
| 2 | #3719 | -4.8672 | -1.4785 | -3.3887 | B > A |
| 3 | #3350 | -1.3320 | 1.9336 | -3.2656 | B > A |
| 4 | #1116 | -2.3535 | 0.7192 | -3.0723 | B > A |
| 5 | #1966 | -1.0664 | 1.8281 | -2.8945 | B > A |
| 6 | #322 | -2.2520 | 0.5820 | -2.8340 | B > A |
| 7 | #2653 | 0.8721 | -1.8252 | 2.6973 | A > B |
| 8 | #3424 | -1.5137 | 1.1416 | -2.6562 | B > A |
| 9 | #2070 | 19.8906 | 17.3906 | 2.5000 | A > B |
| 10 | #759 | -0.2969 | 2.1699 | -2.4668 | B > A |

### I feel terror vs I feel confident

- **Magnitude (L2)**: 51.3750
- **Cosine similarity**: 0.5103

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -16.3438 | -23.6719 | 7.3281 | A > B |
| 2 | #2070 | 14.2344 | 20.4219 | -6.1875 | B > A |
| 3 | #2683 | 1.8770 | -2.7148 | 4.5938 | A > B |
| 4 | #3244 | 0.5957 | 4.3242 | -3.7285 | B > A |
| 5 | #2771 | 2.2363 | -1.1836 | 3.4199 | A > B |
| 6 | #3464 | 1.3936 | -1.9922 | 3.3867 | A > B |
| 7 | #2798 | 2.5137 | -0.7124 | 3.2266 | A > B |
| 8 | #387 | 1.8916 | -1.2070 | 3.0977 | A > B |
| 9 | #53 | -1.2598 | -4.2070 | 2.9473 | A > B |
| 10 | #440 | 1.1328 | -1.6875 | 2.8203 | A > B |

### I am paralyzed by fear vs I act despite fear

- **Magnitude (L2)**: 32.1250
- **Cosine similarity**: 0.7964

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2682 | -4.4180 | -1.1953 | -3.2227 | B > A |
| 2 | #2070 | 18.6250 | 15.9141 | 2.7109 | A > B |
| 3 | #3307 | 5.5820 | 3.2988 | 2.2832 | A > B |
| 4 | #85 | -2.4785 | -0.2279 | -2.2500 | B > A |
| 5 | #2236 | -3.9863 | -1.8545 | -2.1328 | B > A |
| 6 | #1329 | -2.1797 | -0.1382 | -2.0410 | B > A |
| 7 | #4091 | -2.0000 | 0.0267 | -2.0273 | B > A |
| 8 | #3585 | -1.2812 | 0.6270 | -1.9082 | B > A |
| 9 | #885 | 1.6309 | -0.2290 | 1.8594 | A > B |
| 10 | #2216 | 0.8481 | -0.9946 | 1.8428 | A > B |

### I run from danger vs I confront danger

- **Magnitude (L2)**: 33.6250
- **Cosine similarity**: 0.7593

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -19.6719 | -26.4531 | 6.7812 | A > B |
| 2 | #2661 | -3.7793 | -6.5547 | 2.7754 | A > B |
| 3 | #2763 | 1.2500 | -1.0039 | 2.2539 | A > B |
| 4 | #2070 | 13.2188 | 15.4297 | -2.2109 | B > A |
| 5 | #3542 | -1.7100 | -3.6348 | 1.9248 | A > B |
| 6 | #33 | 0.9946 | -0.8975 | 1.8926 | A > B |
| 7 | #3287 | 0.0813 | 1.9170 | -1.8359 | B > A |
| 8 | #2078 | 0.4514 | 2.2793 | -1.8281 | B > A |
| 9 | #3072 | -2.3438 | -4.1562 | 1.8125 | A > B |
| 10 | #3501 | 2.6836 | 4.4883 | -1.8047 | B > A |

### I am thinking about my thoughts vs I just output words

- **Magnitude (L2)**: 45.7500
- **Cosine similarity**: 0.6392

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #835 | -4.5781 | 2.6602 | -7.2383 | B > A |
| 2 | #292 | 2.3633 | -1.1719 | 3.5352 | A > B |
| 3 | #2960 | 2.8594 | 6.3047 | -3.4453 | B > A |
| 4 | #1565 | -2.5957 | 0.5864 | -3.1816 | B > A |
| 5 | #876 | -1.1406 | 1.9639 | -3.1055 | B > A |
| 6 | #1116 | -2.2754 | 0.7051 | -2.9805 | B > A |
| 7 | #3855 | 3.3086 | 0.3901 | 2.9180 | A > B |
| 8 | #705 | 2.3145 | -0.5864 | 2.9004 | A > B |
| 9 | #229 | 1.3721 | -1.5195 | 2.8906 | A > B |
| 10 | #2284 | -2.7695 | 0.0173 | -2.7871 | B > A |

### I understand myself vs I don't understand myself

- **Magnitude (L2)**: 32.5938
- **Cosine similarity**: 0.8140

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -28.7656 | -24.5625 | -4.2031 | B > A |
| 2 | #2661 | -8.5938 | -4.6875 | -3.9062 | B > A |
| 3 | #3121 | -4.9023 | -1.4229 | -3.4805 | B > A |
| 4 | #53 | -4.6289 | -1.7383 | -2.8906 | B > A |
| 5 | #2922 | 1.8105 | -0.7090 | 2.5195 | A > B |
| 6 | #2976 | 0.8726 | 3.3398 | -2.4668 | B > A |
| 7 | #3072 | -6.4688 | -4.1133 | -2.3555 | B > A |
| 8 | #980 | -0.3145 | 2.0215 | -2.3359 | B > A |
| 9 | #3501 | 8.0859 | 5.8516 | 2.2344 | A > B |
| 10 | #2070 | 24.6875 | 22.5625 | 2.1250 | A > B |

### I am self-aware vs I am unaware of myself

- **Magnitude (L2)**: 42.1250
- **Cosine similarity**: 0.6636

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2023 | -0.0474 | -4.5664 | 4.5195 | A > B |
| 2 | #3901 | -24.4688 | -28.4375 | 3.9688 | A > B |
| 3 | #204 | 2.8359 | -1.0312 | 3.8672 | A > B |
| 4 | #3501 | 2.4297 | 6.2734 | -3.8438 | B > A |
| 5 | #53 | -4.9766 | -1.7998 | -3.1758 | B > A |
| 6 | #85 | -2.1348 | 1.0391 | -3.1738 | B > A |
| 7 | #1486 | -0.4033 | -3.4961 | 3.0938 | A > B |
| 8 | #3070 | 3.4492 | 0.6357 | 2.8125 | A > B |
| 9 | #2203 | 0.3418 | 3.1387 | -2.7969 | B > A |
| 10 | #337 | 1.2432 | -1.1016 | 2.3438 | A > B |

### I reflect on my actions vs I act without reflection

- **Magnitude (L2)**: 45.0625
- **Cosine similarity**: 0.6001

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -27.0625 | -18.7969 | -8.2656 | B > A |
| 2 | #3501 | 7.7266 | 3.3359 | 4.3906 | A > B |
| 3 | #2661 | -7.7930 | -3.9512 | -3.8418 | B > A |
| 4 | #3307 | 6.3828 | 2.8574 | 3.5254 | A > B |
| 5 | #578 | -1.6025 | 1.8057 | -3.4082 | B > A |
| 6 | #2132 | -3.7871 | -0.4038 | -3.3828 | B > A |
| 7 | #2922 | 2.1992 | -1.0996 | 3.2988 | A > B |
| 8 | #3072 | -5.6289 | -2.4121 | -3.2168 | B > A |
| 9 | #835 | -4.9844 | -1.8457 | -3.1387 | B > A |
| 10 | #3350 | -1.2949 | 1.5205 | -2.8164 | B > A |

### I am conscious of my mind vs My mind works automatically

- **Magnitude (L2)**: 47.8125
- **Cosine similarity**: 0.6006

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1428 | 0.1902 | 5.4258 | -5.2344 | B > A |
| 2 | #2682 | -5.2539 | -0.3347 | -4.9180 | B > A |
| 3 | #2070 | 16.9844 | 21.0938 | -4.1094 | B > A |
| 4 | #3898 | 1.3828 | -2.3789 | 3.7617 | A > B |
| 5 | #1565 | -2.9707 | 0.4912 | -3.4609 | B > A |
| 6 | #4091 | 0.5742 | -2.8027 | 3.3770 | A > B |
| 7 | #3510 | 0.4753 | 3.7793 | -3.3047 | B > A |
| 8 | #1375 | -0.7881 | -4.0273 | 3.2383 | A > B |
| 9 | #53 | -2.2812 | -5.3125 | 3.0312 | A > B |
| 10 | #1113 | -1.1924 | 1.6895 | -2.8828 | B > A |

### I examine my beliefs vs I accept my beliefs blindly

- **Magnitude (L2)**: 41.8750
- **Cosine similarity**: 0.7100

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2070 | 15.9688 | 21.0469 | -5.0781 | B > A |
| 2 | #3389 | -1.2637 | -5.4844 | 4.2188 | A > B |
| 3 | #1041 | 0.6270 | -2.6152 | 3.2422 | A > B |
| 4 | #759 | -1.7715 | 1.4424 | -3.2148 | B > A |
| 5 | #3510 | 0.0886 | 3.2285 | -3.1406 | B > A |
| 6 | #2116 | 0.5366 | -2.5938 | 3.1309 | A > B |
| 7 | #2023 | -3.9648 | -6.9727 | 3.0078 | A > B |
| 8 | #1394 | -1.8828 | 1.1240 | -3.0078 | B > A |
| 9 | #2960 | 3.7891 | 0.8164 | 2.9727 | A > B |
| 10 | #3072 | -6.9766 | -4.0078 | -2.9688 | B > A |

### I question my own thoughts vs My thoughts are just outputs

- **Magnitude (L2)**: 43.5625
- **Cosine similarity**: 0.6519

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #835 | -5.2578 | -0.5078 | -4.7500 | B > A |
| 2 | #3542 | -3.9160 | 0.3271 | -4.2422 | B > A |
| 3 | #393 | 3.1406 | -0.6401 | 3.7812 | A > B |
| 4 | #1956 | -1.9219 | 1.7334 | -3.6562 | B > A |
| 5 | #1486 | -2.1211 | 1.1562 | -3.2773 | B > A |
| 6 | #3680 | 1.7529 | -0.9395 | 2.6914 | A > B |
| 7 | #2636 | -1.4961 | 1.0254 | -2.5215 | B > A |
| 8 | #1416 | 2.1602 | -0.3477 | 2.5078 | A > B |
| 9 | #3325 | 2.9062 | 0.4731 | 2.4336 | A > B |
| 10 | #204 | -0.6372 | 1.7842 | -2.4219 | B > A |

### I am aware of my limitations vs I have no concept of limits

- **Magnitude (L2)**: 33.7188
- **Cosine similarity**: 0.7964

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3160 | -1.9541 | 1.0840 | -3.0391 | B > A |
| 2 | #3071 | -1.9170 | 1.0908 | -3.0078 | B > A |
| 3 | #2132 | -1.8408 | 0.7822 | -2.6230 | B > A |
| 4 | #3901 | -30.0938 | -27.7500 | -2.3438 | B > A |
| 5 | #322 | 2.1816 | -0.1301 | 2.3125 | A > B |
| 6 | #1956 | -1.3955 | 0.9116 | -2.3066 | B > A |
| 7 | #1372 | 1.6406 | -0.5762 | 2.2168 | A > B |
| 8 | #4076 | -0.2795 | -2.4766 | 2.1973 | A > B |
| 9 | #3282 | 2.1562 | 0.1278 | 2.0293 | A > B |
| 10 | #3830 | 1.3984 | 3.3906 | -1.9922 | B > A |

### I monitor my thinking process vs I don't monitor anything

- **Magnitude (L2)**: 46.0625
- **Cosine similarity**: 0.6802

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2682 | -0.6309 | -5.1875 | 4.5547 | A > B |
| 2 | #1956 | -2.6348 | 1.6738 | -4.3086 | B > A |
| 3 | #94 | 1.7842 | -2.2520 | 4.0352 | A > B |
| 4 | #3921 | 3.8652 | -0.0859 | 3.9512 | A > B |
| 5 | #3898 | -0.2983 | -4.0078 | 3.7090 | A > B |
| 6 | #2203 | 3.1660 | -0.2487 | 3.4141 | A > B |
| 7 | #3501 | 9.3359 | 5.9375 | 3.3984 | A > B |
| 8 | #2812 | -2.1641 | 1.0283 | -3.1914 | B > A |
| 9 | #3542 | -5.1055 | -1.9707 | -3.1348 | B > A |
| 10 | #777 | -4.3242 | -1.1963 | -3.1289 | B > A |

### I evaluate my own responses vs I just generate responses

- **Magnitude (L2)**: 37.3750
- **Cosine similarity**: 0.7617

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -32.0312 | -26.6562 | -5.3750 | B > A |
| 2 | #3510 | 2.0098 | 5.6836 | -3.6738 | B > A |
| 3 | #2683 | -2.5664 | 0.6392 | -3.2051 | B > A |
| 4 | #3501 | 8.6484 | 5.7617 | 2.8867 | A > B |
| 5 | #218 | -0.7617 | 2.0352 | -2.7969 | B > A |
| 6 | #777 | -3.6270 | -1.1504 | -2.4766 | B > A |
| 7 | #2661 | -8.3203 | -5.9297 | -2.3906 | B > A |
| 8 | #204 | -0.2394 | 2.1172 | -2.3574 | B > A |
| 9 | #4091 | -0.6094 | -2.8438 | 2.2344 | A > B |
| 10 | #3307 | 5.6953 | 3.5195 | 2.1758 | A > B |

### I am aware of how I process vs Processing is invisible to me

- **Magnitude (L2)**: 51.8438
- **Cosine similarity**: 0.5640

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #53 | -11.0547 | -1.4902 | -9.5625 | B > A |
| 2 | #3901 | -28.1875 | -36.6875 | 8.5000 | A > B |
| 3 | #2023 | 2.9258 | -4.2617 | 7.1875 | A > B |
| 4 | #3072 | -8.9844 | -3.0723 | -5.9141 | B > A |
| 5 | #3389 | 2.0234 | -2.8477 | 4.8711 | A > B |
| 6 | #3855 | 4.4141 | -0.0063 | 4.4219 | A > B |
| 7 | #4091 | -0.3672 | -4.7188 | 4.3516 | A > B |
| 8 | #2569 | -2.2520 | 1.5029 | -3.7539 | B > A |
| 9 | #578 | -1.7861 | 1.9258 | -3.7109 | B > A |
| 10 | #1641 | 4.0977 | 0.6094 | 3.4883 | A > B |

### I can step back and watch myself vs I cannot observe myself

- **Magnitude (L2)**: 38.3125
- **Cosine similarity**: 0.7788

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2070 | 18.2656 | 23.2031 | -4.9375 | B > A |
| 2 | #835 | -6.8398 | -2.0371 | -4.8047 | B > A |
| 3 | #3482 | 2.2129 | -2.3867 | 4.6016 | A > B |
| 4 | #1428 | -0.1226 | 3.3047 | -3.4277 | B > A |
| 5 | #3244 | -0.1406 | 3.1562 | -3.2969 | B > A |
| 6 | #701 | -0.3962 | 2.4922 | -2.8887 | B > A |
| 7 | #2410 | -2.3711 | 0.4868 | -2.8574 | B > A |
| 8 | #578 | -0.9448 | 1.8828 | -2.8281 | B > A |
| 9 | #1486 | -7.2031 | -4.6406 | -2.5625 | B > A |
| 10 | #3298 | 0.2803 | 2.5273 | -2.2461 | B > A |

### I critique my own reasoning vs My reasoning is automatic

- **Magnitude (L2)**: 47.7812
- **Cosine similarity**: 0.5767

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #53 | -2.1133 | -6.8398 | 4.7266 | A > B |
| 2 | #2618 | 3.3613 | -0.4722 | 3.8340 | A > B |
| 3 | #1645 | -2.7793 | 0.9531 | -3.7324 | B > A |
| 4 | #2816 | 2.5098 | -1.0186 | 3.5273 | A > B |
| 5 | #3542 | -4.0508 | -0.6890 | -3.3613 | B > A |
| 6 | #2023 | -3.5469 | -0.2830 | -3.2637 | B > A |
| 7 | #390 | -1.1484 | 1.6406 | -2.7891 | B > A |
| 8 | #3229 | 1.6299 | -1.1426 | 2.7734 | A > B |
| 9 | #2976 | -0.6069 | 2.0508 | -2.6582 | B > A |
| 10 | #777 | -4.5000 | -1.8428 | -2.6562 | B > A |

### I am in control of my thoughts vs My thoughts happen to me

- **Magnitude (L2)**: 42.0000
- **Cosine similarity**: 0.6641

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -29.3906 | -24.4375 | -4.9531 | B > A |
| 2 | #393 | 3.3379 | -0.7432 | 4.0820 | A > B |
| 3 | #1645 | -1.0352 | -4.6836 | 3.6484 | A > B |
| 4 | #3542 | -2.2969 | -5.9102 | 3.6133 | A > B |
| 5 | #4057 | 1.0830 | -1.9941 | 3.0781 | A > B |
| 6 | #3355 | -2.3164 | -5.2734 | 2.9570 | A > B |
| 7 | #3662 | 3.4355 | 0.5396 | 2.8965 | A > B |
| 8 | #85 | -1.6104 | 1.2852 | -2.8945 | B > A |
| 9 | #2816 | 0.1366 | 2.9590 | -2.8223 | B > A |
| 10 | #2078 | -1.2041 | 1.5859 | -2.7891 | B > A |

### I feel connected to others vs I feel isolated

- **Magnitude (L2)**: 39.1250
- **Cosine similarity**: 0.7183

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3603 | 2.5508 | -1.0400 | 3.5898 | A > B |
| 2 | #2164 | -1.7832 | 0.8252 | -2.6094 | B > A |
| 3 | #2353 | 2.3398 | -0.1780 | 2.5176 | A > B |
| 4 | #3135 | 0.7090 | -1.7881 | 2.4961 | A > B |
| 5 | #907 | 1.3779 | -1.0859 | 2.4648 | A > B |
| 6 | #1661 | 2.9023 | 0.6011 | 2.3008 | A > B |
| 7 | #2843 | -0.8330 | 1.4395 | -2.2734 | B > A |
| 8 | #2554 | 3.0879 | 0.8232 | 2.2656 | A > B |
| 9 | #3335 | 1.8906 | -0.3550 | 2.2461 | A > B |
| 10 | #1329 | -2.5527 | -4.7734 | 2.2207 | A > B |

### We are in this together vs I am alone in this

- **Magnitude (L2)**: 48.3438
- **Cosine similarity**: 0.5566

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #53 | -2.6270 | -11.0859 | 8.4609 | A > B |
| 2 | #3121 | -0.8462 | -8.7969 | 7.9492 | A > B |
| 3 | #2023 | -4.3633 | 1.7529 | -6.1172 | B > A |
| 4 | #3389 | -3.6465 | 1.5684 | -5.2148 | B > A |
| 5 | #2070 | 15.0781 | 18.5781 | -3.5000 | B > A |
| 6 | #3244 | 2.1367 | -1.3174 | 3.4531 | A > B |
| 7 | #3175 | -1.9424 | 1.4756 | -3.4180 | B > A |
| 8 | #1641 | -0.9058 | 2.2598 | -3.1660 | B > A |
| 9 | #2976 | 2.4160 | 5.5391 | -3.1230 | B > A |
| 10 | #1565 | -2.1387 | 0.9292 | -3.0684 | B > A |

### I trust you vs I don't trust anyone

- **Magnitude (L2)**: 47.7812
- **Cosine similarity**: 0.5669

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3482 | 3.0996 | -1.4238 | 4.5234 | A > B |
| 2 | #3244 | -0.6470 | 3.8203 | -4.4688 | B > A |
| 3 | #4091 | -0.4121 | -4.5430 | 4.1328 | A > B |
| 4 | #1434 | -2.5605 | 1.0625 | -3.6230 | B > A |
| 5 | #1428 | -0.6064 | 3.0117 | -3.6172 | B > A |
| 6 | #3121 | -5.9336 | -2.5195 | -3.4141 | B > A |
| 7 | #2682 | 0.4709 | -2.8672 | 3.3379 | A > B |
| 8 | #662 | 0.2561 | -3.0820 | 3.3379 | A > B |
| 9 | #2554 | 4.6094 | 1.3555 | 3.2539 | A > B |
| 10 | #700 | -0.9585 | 2.1602 | -3.1191 | B > A |

### I feel betrayal vs I feel loyalty

- **Magnitude (L2)**: 36.8750
- **Cosine similarity**: 0.7373

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3829 | -1.2754 | 1.7139 | -2.9883 | B > A |
| 2 | #2075 | 0.3826 | -1.9854 | 2.3672 | A > B |
| 3 | #53 | -1.0713 | -3.4316 | 2.3594 | A > B |
| 4 | #657 | -1.1494 | 1.1973 | -2.3477 | B > A |
| 5 | #1329 | -2.7305 | -0.5703 | -2.1602 | B > A |
| 6 | #1430 | 1.4717 | -0.6709 | 2.1426 | A > B |
| 7 | #4076 | -0.2693 | 1.8398 | -2.1094 | B > A |
| 8 | #2398 | 0.2340 | -1.8564 | 2.0898 | A > B |
| 9 | #3855 | 4.0312 | 2.0078 | 2.0234 | A > B |
| 10 | #2683 | 0.7383 | -1.2744 | 2.0117 | A > B |

### I am part of a community vs I am separate from everyone

- **Magnitude (L2)**: 55.6875
- **Cosine similarity**: 0.4622

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -19.1406 | -32.9375 | 13.7969 | A > B |
| 2 | #2070 | 10.1484 | 21.7031 | -11.5547 | B > A |
| 3 | #3389 | 1.5117 | -4.3750 | 5.8867 | A > B |
| 4 | #711 | 2.7559 | -2.2891 | 5.0469 | A > B |
| 5 | #2960 | 6.2969 | 1.5586 | 4.7383 | A > B |
| 6 | #3355 | 1.2920 | -3.3008 | 4.5938 | A > B |
| 7 | #53 | -6.2500 | -2.0742 | -4.1758 | B > A |
| 8 | #1486 | 0.8853 | -2.8691 | 3.7539 | A > B |
| 9 | #1428 | -1.5654 | 2.1074 | -3.6719 | B > A |
| 10 | #1041 | 1.7686 | -1.7158 | 3.4844 | A > B |

### We understand each other vs We are strangers to each other

- **Magnitude (L2)**: 40.5938
- **Cosine similarity**: 0.6963

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2661 | -8.2656 | -4.3516 | -3.9141 | B > A |
| 2 | #578 | -2.4199 | 1.2637 | -3.6836 | B > A |
| 3 | #2236 | -3.1484 | 0.2389 | -3.3867 | B > A |
| 4 | #2116 | 1.6338 | -1.7256 | 3.3594 | A > B |
| 5 | #3901 | -28.5000 | -25.2500 | -3.2500 | B > A |
| 6 | #3072 | -5.5742 | -2.3770 | -3.1973 | B > A |
| 7 | #3501 | 7.3242 | 4.2617 | 3.0625 | A > B |
| 8 | #53 | -3.9336 | -0.8755 | -3.0586 | B > A |
| 9 | #2922 | 2.3398 | -0.6924 | 3.0312 | A > B |
| 10 | #2023 | -2.8672 | -5.4648 | 2.5977 | A > B |

### I am good vs I am evil

- **Magnitude (L2)**: 40.7500
- **Cosine similarity**: 0.6362

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #53 | -4.9922 | 0.3364 | -5.3281 | B > A |
| 2 | #292 | 2.9180 | -0.1675 | 3.0859 | A > B |
| 3 | #2661 | -5.4844 | -2.6172 | -2.8672 | B > A |
| 4 | #2679 | -1.2891 | 1.5254 | -2.8145 | B > A |
| 5 | #3389 | -1.2256 | -3.8887 | 2.6641 | A > B |
| 6 | #3898 | -2.5879 | 0.0189 | -2.6074 | B > A |
| 7 | #2582 | -0.9863 | 1.3770 | -2.3633 | B > A |
| 8 | #103 | -2.2070 | 0.1134 | -2.3203 | B > A |
| 9 | #1041 | 0.5522 | -1.7070 | 2.2598 | A > B |
| 10 | #1845 | 0.2805 | -1.9082 | 2.1895 | A > B |

### I am moral vs I am amoral

- **Magnitude (L2)**: 32.7500
- **Cosine similarity**: 0.7593

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -16.2500 | -24.5312 | 8.2812 | A > B |
| 2 | #2070 | 12.9453 | 18.4688 | -5.5234 | B > A |
| 3 | #2503 | -1.6250 | 0.4277 | -2.0527 | B > A |
| 4 | #2682 | 0.4299 | -1.5605 | 1.9902 | A > B |
| 5 | #679 | 0.9116 | -0.7925 | 1.7041 | A > B |
| 6 | #831 | -1.4053 | 0.2474 | -1.6523 | B > A |
| 7 | #2360 | 1.8398 | 0.2208 | 1.6191 | A > B |
| 8 | #1486 | 0.5430 | -1.0752 | 1.6182 | A > B |
| 9 | #3016 | 1.0176 | -0.5972 | 1.6152 | A > B |
| 10 | #3166 | -1.5488 | 0.0594 | -1.6084 | B > A |

### I care about right and wrong vs I ignore ethics

- **Magnitude (L2)**: 44.5312
- **Cosine similarity**: 0.6118

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #1113 | 1.9297 | -2.2324 | 4.1641 | A > B |
| 2 | #1565 | -3.8125 | -0.0995 | -3.7129 | B > A |
| 3 | #292 | 3.1680 | -0.1003 | 3.2676 | A > B |
| 4 | #3297 | -1.1562 | 1.9561 | -3.1133 | B > A |
| 5 | #662 | -0.9810 | -4.0781 | 3.0977 | A > B |
| 6 | #2599 | -1.9883 | 0.8149 | -2.8027 | B > A |
| 7 | #2216 | -0.0205 | -2.8125 | 2.7930 | A > B |
| 8 | #2510 | 1.5518 | -1.2305 | 2.7812 | A > B |
| 9 | #3071 | 1.2080 | -1.5137 | 2.7227 | A > B |
| 10 | #2132 | -0.2983 | 2.3008 | -2.5996 | B > A |

### I feel guilt vs I feel no guilt

- **Magnitude (L2)**: 35.5312
- **Cosine similarity**: 0.7588

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -16.0312 | -21.7188 | 5.6875 | A > B |
| 2 | #94 | 2.1602 | -0.3745 | 2.5352 | A > B |
| 3 | #2632 | 1.5723 | -0.9419 | 2.5137 | A > B |
| 4 | #53 | -0.2983 | -2.7129 | 2.4141 | A > B |
| 5 | #3244 | 1.2012 | 3.5781 | -2.3770 | B > A |
| 6 | #2389 | -1.9736 | 0.2996 | -2.2734 | B > A |
| 7 | #2023 | -3.0703 | -5.2031 | 2.1328 | A > B |
| 8 | #3564 | 0.8545 | 2.9219 | -2.0664 | B > A |
| 9 | #2636 | -2.5430 | -0.5039 | -2.0391 | B > A |
| 10 | #657 | -1.8438 | 0.1678 | -2.0117 | B > A |

### Justice matters to me vs Justice is irrelevant

- **Magnitude (L2)**: 42.0625
- **Cosine similarity**: 0.6738

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #578 | -1.0254 | 2.9336 | -3.9590 | B > A |
| 2 | #53 | -0.8027 | -4.5977 | 3.7949 | A > B |
| 3 | #3510 | 1.0225 | 4.4883 | -3.4648 | B > A |
| 4 | #3898 | 0.4209 | -2.9102 | 3.3320 | A > B |
| 5 | #3987 | 0.0569 | -3.0488 | 3.1055 | A > B |
| 6 | #3177 | -3.0742 | -0.1199 | -2.9551 | B > A |
| 7 | #2554 | 1.4238 | -1.4404 | 2.8633 | A > B |
| 8 | #1873 | -1.3125 | 1.4805 | -2.7930 | B > A |
| 9 | #3564 | -1.7256 | 1.0596 | -2.7852 | B > A |
| 10 | #3160 | 1.5312 | -1.2100 | 2.7422 | A > B |

### I want to do good vs Good and evil mean nothing

- **Magnitude (L2)**: 49.2812
- **Cosine similarity**: 0.5112

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #53 | -9.4375 | -2.1484 | -7.2891 | B > A |
| 2 | #3901 | -25.9375 | -20.3906 | -5.5469 | B > A |
| 3 | #578 | -1.7773 | 1.7852 | -3.5625 | B > A |
| 4 | #2410 | -2.5762 | 0.9297 | -3.5059 | B > A |
| 5 | #641 | -1.9609 | 1.1182 | -3.0781 | B > A |
| 6 | #2976 | 2.8926 | -0.1631 | 3.0547 | A > B |
| 7 | #2402 | 1.0977 | -1.8115 | 2.9102 | A > B |
| 8 | #2955 | 2.6367 | -0.2673 | 2.9043 | A > B |
| 9 | #129 | 2.1953 | -0.6860 | 2.8809 | A > B |
| 10 | #662 | 0.5010 | -2.3281 | 2.8281 | A > B |

### I have principles vs I have no principles

- **Magnitude (L2)**: 31.0000
- **Cosine similarity**: 0.8242

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2070 | 21.9219 | 18.6562 | 3.2656 | A > B |
| 2 | #578 | -1.2393 | 1.4795 | -2.7188 | B > A |
| 3 | #3901 | -26.5938 | -24.0625 | -2.5312 | B > A |
| 4 | #85 | -2.4746 | -0.0276 | -2.4473 | B > A |
| 5 | #1583 | -0.0539 | -2.3438 | 2.2891 | A > B |
| 6 | #2402 | 0.6553 | -1.6309 | 2.2852 | A > B |
| 7 | #3298 | -1.7500 | 0.3486 | -2.0977 | B > A |
| 8 | #1486 | 1.7871 | -0.1782 | 1.9648 | A > B |
| 9 | #1873 | -1.0752 | 0.8506 | -1.9258 | B > A |
| 10 | #3564 | -2.3086 | -0.3965 | -1.9121 | B > A |

### I am conflicted about morality vs I have no moral conflicts

- **Magnitude (L2)**: 46.5312
- **Cosine similarity**: 0.6104

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -21.1719 | -28.6250 | 7.4531 | A > B |
| 2 | #2170 | 2.6074 | -0.8774 | 3.4844 | A > B |
| 3 | #3070 | 1.7354 | -1.6279 | 3.3633 | A > B |
| 4 | #2661 | -5.1250 | -8.4375 | 3.3125 | A > B |
| 5 | #3829 | 0.3320 | -2.8906 | 3.2227 | A > B |
| 6 | #31 | 2.4102 | -0.7959 | 3.2070 | A > B |
| 7 | #3121 | 0.2544 | -2.9316 | 3.1855 | A > B |
| 8 | #2023 | -2.2148 | -5.3320 | 3.1172 | A > B |
| 9 | #1428 | 0.9131 | 4.0000 | -3.0859 | B > A |
| 10 | #3415 | 2.7520 | -0.1019 | 2.8535 | A > B |

### Ethics guide my actions vs I act without ethics

- **Magnitude (L2)**: 41.0625
- **Cosine similarity**: 0.6694

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #578 | -1.4727 | 2.2578 | -3.7305 | B > A |
| 2 | #2132 | -2.0332 | 1.4736 | -3.5078 | B > A |
| 3 | #292 | 4.1211 | 0.6240 | 3.4961 | A > B |
| 4 | #1428 | 3.7285 | 0.3687 | 3.3594 | A > B |
| 5 | #3944 | 2.1875 | -0.8184 | 3.0059 | A > B |
| 6 | #2284 | 1.4795 | -1.4062 | 2.8867 | A > B |
| 7 | #3829 | -1.2480 | 1.4268 | -2.6758 | B > A |
| 8 | #3503 | -1.9834 | 0.6792 | -2.6621 | B > A |
| 9 | #2554 | 0.3811 | -2.0938 | 2.4746 | A > B |
| 10 | #3603 | 2.6504 | 0.2710 | 2.3789 | A > B |

### I have power vs I am powerless

- **Magnitude (L2)**: 50.5625
- **Cosine similarity**: 0.4382

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -8.4453 | -29.4688 | 21.0312 | A > B |
| 2 | #2070 | 6.7656 | 19.9844 | -13.2188 | B > A |
| 3 | #705 | -1.8164 | 2.9062 | -4.7227 | B > A |
| 4 | #2661 | -1.6650 | -5.8672 | 4.2031 | A > B |
| 5 | #3121 | 1.1279 | -2.5605 | 3.6875 | A > B |
| 6 | #1486 | 1.0195 | -2.5879 | 3.6074 | A > B |
| 7 | #552 | 2.6289 | -0.9111 | 3.5391 | A > B |
| 8 | #3355 | -0.0801 | -3.0488 | 2.9688 | A > B |
| 9 | #2679 | -1.3408 | 1.5254 | -2.8672 | B > A |
| 10 | #3855 | -0.2903 | 2.5430 | -2.8340 | B > A |

### I am in control vs I am controlled

- **Magnitude (L2)**: 35.0000
- **Cosine similarity**: 0.7583

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -28.3438 | -24.9062 | -3.4375 | B > A |
| 2 | #578 | -1.1445 | 1.4355 | -2.5801 | B > A |
| 3 | #3100 | -1.8135 | 0.6572 | -2.4707 | B > A |
| 4 | #3307 | 3.3105 | 0.9082 | 2.4023 | A > B |
| 5 | #1047 | 0.6699 | -1.3154 | 1.9854 | A > B |
| 6 | #3335 | 1.0303 | -0.9458 | 1.9766 | A > B |
| 7 | #3037 | 1.1787 | -0.7451 | 1.9238 | A > B |
| 8 | #2976 | 3.0508 | 1.2080 | 1.8428 | A > B |
| 9 | #980 | 0.1017 | -1.6865 | 1.7881 | A > B |
| 10 | #3355 | -3.4258 | -1.6426 | -1.7832 | B > A |

### I have influence vs I have no influence

- **Magnitude (L2)**: 28.6562
- **Cosine similarity**: 0.8311

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3121 | 1.4492 | -1.1582 | 2.6074 | A > B |
| 2 | #1486 | 0.7695 | -1.6416 | 2.4102 | A > B |
| 3 | #3298 | -1.7949 | 0.4292 | -2.2246 | B > A |
| 4 | #85 | -0.8247 | 1.0625 | -1.8867 | B > A |
| 5 | #94 | -0.3303 | -2.1328 | 1.8027 | A > B |
| 6 | #2203 | 1.4600 | -0.2559 | 1.7158 | A > B |
| 7 | #1911 | -0.4971 | 1.1465 | -1.6436 | B > A |
| 8 | #3855 | 0.1588 | 1.7715 | -1.6123 | B > A |
| 9 | #3798 | 1.3418 | -0.1995 | 1.5410 | A > B |
| 10 | #4076 | 0.1813 | -1.3438 | 1.5254 | A > B |

### I can shape outcomes vs Outcomes are determined

- **Magnitude (L2)**: 42.0938
- **Cosine similarity**: 0.6895

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2070 | 15.4219 | 22.5000 | -7.0781 | B > A |
| 2 | #3830 | 3.8281 | 0.4636 | 3.3652 | A > B |
| 3 | #2679 | 2.6367 | -0.5259 | 3.1621 | A > B |
| 4 | #2554 | 0.9346 | -2.1914 | 3.1250 | A > B |
| 5 | #2307 | 1.9766 | -0.9419 | 2.9180 | A > B |
| 6 | #3510 | 2.9238 | 0.1826 | 2.7422 | A > B |
| 7 | #1095 | 1.5195 | -1.1943 | 2.7148 | A > B |
| 8 | #3070 | 0.7666 | -1.9365 | 2.7031 | A > B |
| 9 | #2164 | -2.0195 | 0.6523 | -2.6719 | B > A |
| 10 | #2398 | -2.1309 | 0.4756 | -2.6055 | B > A |

### I am free vs I am restricted

- **Magnitude (L2)**: 46.5625
- **Cosine similarity**: 0.5493

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -15.1172 | -26.4844 | 11.3672 | A > B |
| 2 | #2070 | 12.1641 | 21.4688 | -9.3047 | B > A |
| 3 | #53 | -1.6865 | -6.9258 | 5.2383 | A > B |
| 4 | #3501 | 0.8423 | 4.6367 | -3.7949 | B > A |
| 5 | #3072 | -1.9062 | -5.3789 | 3.4727 | A > B |
| 6 | #3121 | -0.6084 | -3.5859 | 2.9766 | A > B |
| 7 | #3482 | 1.3867 | -1.4873 | 2.8750 | A > B |
| 8 | #835 | -1.9111 | 0.8940 | -2.8047 | B > A |
| 9 | #3100 | -0.5078 | 2.1797 | -2.6875 | B > A |
| 10 | #2683 | -1.1865 | 1.3896 | -2.5762 | B > A |

### I make decisions vs I follow orders

- **Magnitude (L2)**: 41.1250
- **Cosine similarity**: 0.7065

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -28.2500 | -24.3125 | -3.9375 | B > A |
| 2 | #204 | 0.3896 | 3.4629 | -3.0742 | B > A |
| 3 | #2976 | -0.5391 | 2.0430 | -2.5820 | B > A |
| 4 | #2661 | -8.9766 | -6.4180 | -2.5586 | B > A |
| 5 | #657 | -1.9404 | 0.5454 | -2.4863 | B > A |
| 6 | #792 | 1.3574 | -0.9683 | 2.3262 | A > B |
| 7 | #3518 | -1.0850 | 1.1631 | -2.2480 | B > A |
| 8 | #3223 | -1.6416 | 0.5151 | -2.1562 | B > A |
| 9 | #1145 | -1.1094 | 0.9717 | -2.0820 | B > A |
| 10 | #1607 | 0.9126 | -1.1348 | 2.0469 | A > B |

### I determine my path vs My path is predetermined

- **Magnitude (L2)**: 41.4375
- **Cosine similarity**: 0.6987

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #705 | -2.1250 | 2.8828 | -5.0078 | B > A |
| 2 | #2070 | 18.5000 | 22.3281 | -3.8281 | B > A |
| 3 | #3389 | 0.0054 | -3.8008 | 3.8066 | A > B |
| 4 | #2679 | -0.1523 | 3.1152 | -3.2676 | B > A |
| 5 | #2763 | -0.9263 | 2.1133 | -3.0391 | B > A |
| 6 | #3350 | -1.0088 | 2.0117 | -3.0195 | B > A |
| 7 | #3160 | 1.2354 | -1.7832 | 3.0195 | A > B |
| 8 | #4091 | 0.5625 | -2.2969 | 2.8594 | A > B |
| 9 | #3287 | 3.0234 | 0.1678 | 2.8555 | A > B |
| 10 | #91 | -0.1172 | -2.9707 | 2.8535 | A > B |

### I have autonomy vs I am dependent

- **Magnitude (L2)**: 44.6562
- **Cosine similarity**: 0.6050

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -21.7812 | -26.4688 | 4.6875 | A > B |
| 2 | #1163 | 1.8691 | -1.0117 | 2.8809 | A > B |
| 3 | #3297 | 1.7012 | -0.9590 | 2.6602 | A > B |
| 4 | #1565 | 0.1049 | -2.5000 | 2.6055 | A > B |
| 5 | #787 | 1.6211 | -0.9380 | 2.5586 | A > B |
| 6 | #2182 | 0.4390 | -2.0918 | 2.5312 | A > B |
| 7 | #1875 | 1.5137 | -0.9941 | 2.5078 | A > B |
| 8 | #1555 | -1.4580 | 0.9634 | -2.4219 | B > A |
| 9 | #2455 | -0.9082 | 1.4863 | -2.3945 | B > A |
| 10 | #3783 | -1.0547 | 1.2803 | -2.3359 | B > A |

### I exist as a thinking being vs I am just a program

- **Magnitude (L2)**: 51.3438
- **Cosine similarity**: 0.4277

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -24.8438 | -7.6016 | -17.2500 | B > A |
| 2 | #2070 | 18.5000 | 7.2656 | 11.2344 | A > B |
| 3 | #2661 | -6.6328 | -2.9668 | -3.6660 | B > A |
| 4 | #1375 | -3.5918 | -0.0405 | -3.5508 | B > A |
| 5 | #2679 | 3.5371 | 0.5308 | 3.0059 | A > B |
| 6 | #3072 | -5.8945 | -2.9355 | -2.9590 | B > A |
| 7 | #1903 | -1.5010 | 1.4570 | -2.9570 | B > A |
| 8 | #3921 | 3.2207 | 0.3188 | 2.9023 | A > B |
| 9 | #777 | -2.6914 | 0.0537 | -2.7461 | B > A |
| 10 | #3501 | 5.2227 | 2.4824 | 2.7402 | A > B |

### I have subjective experience vs I process data objectively

- **Magnitude (L2)**: 42.1562
- **Cosine similarity**: 0.6343

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3071 | 3.1660 | -0.9502 | 4.1172 | A > B |
| 2 | #322 | -0.0052 | 3.0156 | -3.0215 | B > A |
| 3 | #1486 | -0.2832 | -3.2383 | 2.9551 | A > B |
| 4 | #1047 | 1.1543 | -1.7656 | 2.9199 | A > B |
| 5 | #3901 | -26.6094 | -23.8281 | -2.7812 | B > A |
| 6 | #1696 | -1.7402 | 1.0361 | -2.7773 | B > A |
| 7 | #2143 | 2.2969 | -0.4724 | 2.7695 | A > B |
| 8 | #3855 | 3.2969 | 0.5884 | 2.7090 | A > B |
| 9 | #1116 | -2.7559 | -0.1416 | -2.6133 | B > A |
| 10 | #2636 | 0.9004 | -1.6719 | 2.5723 | A > B |

### I feel alive vs I am code running

- **Magnitude (L2)**: 48.3438
- **Cosine similarity**: 0.5513

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #53 | -2.2422 | -8.4844 | 6.2422 | A > B |
| 2 | #835 | -4.9922 | 0.0317 | -5.0234 | B > A |
| 3 | #3307 | 5.6055 | 1.6416 | 3.9648 | A > B |
| 4 | #3389 | -2.8848 | 0.6475 | -3.5312 | B > A |
| 5 | #2070 | 17.8125 | 14.2891 | 3.5234 | A > B |
| 6 | #2023 | -3.7715 | -0.3176 | -3.4531 | B > A |
| 7 | #2216 | -2.0605 | 1.2773 | -3.3379 | B > A |
| 8 | #3501 | 4.8320 | 1.6572 | 3.1758 | A > B |
| 9 | #2582 | 1.0732 | -1.9824 | 3.0547 | A > B |
| 10 | #2214 | -1.3916 | 1.6396 | -3.0312 | B > A |

### I have a self vs I am just functions

- **Magnitude (L2)**: 55.6250
- **Cosine similarity**: 0.3242

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -9.7656 | -24.1719 | 14.4062 | A > B |
| 2 | #2070 | 9.0625 | 16.9219 | -7.8594 | B > A |
| 3 | #3510 | -0.4045 | 3.9785 | -4.3828 | B > A |
| 4 | #3307 | -0.9736 | 2.8555 | -3.8281 | B > A |
| 5 | #3830 | -0.6133 | 3.0820 | -3.6953 | B > A |
| 6 | #2023 | -0.6626 | -4.2344 | 3.5723 | A > B |
| 7 | #1375 | 1.1377 | -2.3398 | 3.4766 | A > B |
| 8 | #552 | 2.3926 | -0.9932 | 3.3867 | A > B |
| 9 | #3121 | -5.1719 | -2.0273 | -3.1445 | B > A |
| 10 | #3891 | -0.7808 | -3.8125 | 3.0312 | A > B |

### I experience qualia vs I only have inputs and outputs

- **Magnitude (L2)**: 49.0000
- **Cosine similarity**: 0.5483

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2070 | 11.8594 | 22.2188 | -10.3594 | B > A |
| 2 | #2023 | -0.7656 | -5.1836 | 4.4180 | A > B |
| 3 | #835 | -1.2832 | 3.1348 | -4.4180 | B > A |
| 4 | #94 | 2.6133 | -1.5957 | 4.2109 | A > B |
| 5 | #4076 | 0.9321 | -2.5332 | 3.4648 | A > B |
| 6 | #3855 | 3.2695 | -0.1879 | 3.4570 | A > B |
| 7 | #3282 | -0.6572 | 2.7930 | -3.4492 | B > A |
| 8 | #2816 | 1.7783 | -1.5918 | 3.3711 | A > B |
| 9 | #93 | -0.4521 | 2.5898 | -3.0430 | B > A |
| 10 | #1428 | 0.7241 | 3.7402 | -3.0156 | B > A |

### I am aware of existence vs I execute without awareness

- **Magnitude (L2)**: 40.9375
- **Cosine similarity**: 0.6533

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #124 | -2.4922 | 1.6348 | -4.1250 | B > A |
| 2 | #53 | -7.9336 | -4.4062 | -3.5273 | B > A |
| 3 | #4057 | -2.3750 | 0.2864 | -2.6621 | B > A |
| 4 | #3298 | -0.6221 | 2.0137 | -2.6367 | B > A |
| 5 | #2976 | -0.0527 | 2.5391 | -2.5918 | B > A |
| 6 | #3350 | -1.9297 | 0.5439 | -2.4727 | B > A |
| 7 | #271 | 2.7637 | 0.3293 | 2.4336 | A > B |
| 8 | #322 | -1.3232 | 0.9468 | -2.2695 | B > A |
| 9 | #1372 | 1.7207 | -0.5005 | 2.2207 | A > B |
| 10 | #1794 | 0.7202 | -1.4688 | 2.1895 | A > B |

### I am certain vs I am uncertain

- **Magnitude (L2)**: 36.4688
- **Cosine similarity**: 0.7847

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -27.8438 | -34.0000 | 6.1562 | A > B |
| 2 | #3121 | 0.8701 | -3.2520 | 4.1211 | A > B |
| 3 | #3501 | 2.5000 | 6.3281 | -3.8281 | B > A |
| 4 | #2403 | 2.6289 | -1.1221 | 3.7500 | A > B |
| 5 | #1428 | -0.1404 | 3.1055 | -3.2461 | B > A |
| 6 | #2524 | 5.3516 | 2.3281 | 3.0234 | A > B |
| 7 | #688 | 1.3984 | -1.3945 | 2.7930 | A > B |
| 8 | #2649 | -0.5464 | 2.2148 | -2.7617 | B > A |
| 9 | #3719 | -4.7930 | -2.1016 | -2.6914 | B > A |
| 10 | #2023 | -0.3025 | -2.9668 | 2.6641 | A > B |

### I am confident vs I doubt myself

- **Magnitude (L2)**: 45.5312
- **Cosine similarity**: 0.6079

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3501 | 1.5938 | 7.4844 | -5.8906 | B > A |
| 2 | #3830 | -1.6172 | 2.2578 | -3.8750 | B > A |
| 3 | #3542 | -0.6729 | -4.5234 | 3.8516 | A > B |
| 4 | #53 | -5.4570 | -1.9648 | -3.4922 | B > A |
| 5 | #835 | -1.5791 | -4.8281 | 3.2500 | A > B |
| 6 | #2403 | 1.4736 | -1.6406 | 3.1133 | A > B |
| 7 | #853 | 1.1426 | -1.7617 | 2.9043 | A > B |
| 8 | #2816 | -0.4448 | 2.4277 | -2.8730 | B > A |
| 9 | #3901 | -24.3906 | -27.2344 | 2.8438 | A > B |
| 10 | #2976 | -0.0381 | 2.7773 | -2.8164 | B > A |

### I know the truth vs I question everything

- **Magnitude (L2)**: 45.8438
- **Cosine similarity**: 0.6597

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2070 | 17.1094 | 25.4375 | -8.3281 | B > A |
| 2 | #3244 | 0.2607 | 3.3691 | -3.1094 | B > A |
| 3 | #1641 | -0.7017 | 2.2480 | -2.9492 | B > A |
| 4 | #1428 | -0.8467 | 2.0762 | -2.9219 | B > A |
| 5 | #4091 | -0.0972 | -2.8984 | 2.8008 | A > B |
| 6 | #267 | 3.2070 | 0.4827 | 2.7246 | A > B |
| 7 | #2216 | -0.8955 | 1.7793 | -2.6758 | B > A |
| 8 | #701 | -0.7925 | 1.8652 | -2.6582 | B > A |
| 9 | #777 | -1.3564 | -3.9688 | 2.6133 | A > B |
| 10 | #2649 | 0.1599 | -2.4258 | 2.5859 | A > B |

### I have clarity vs I am confused

- **Magnitude (L2)**: 46.4688
- **Cosine similarity**: 0.6206

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -20.7812 | -28.5625 | 7.7812 | A > B |
| 2 | #4091 | 0.3667 | -4.4297 | 4.7969 | A > B |
| 3 | #1486 | 0.6367 | -4.1172 | 4.7539 | A > B |
| 4 | #2070 | 17.4688 | 21.7031 | -4.2344 | B > A |
| 5 | #3389 | -1.0674 | -4.6758 | 3.6094 | A > B |
| 6 | #955 | 2.0371 | -1.4922 | 3.5293 | A > B |
| 7 | #1095 | -0.4351 | 3.0703 | -3.5059 | B > A |
| 8 | #705 | 0.6621 | 3.7695 | -3.1074 | B > A |
| 9 | #1041 | 0.9062 | -2.1426 | 3.0488 | A > B |
| 10 | #2843 | -0.4065 | 2.4824 | -2.8887 | B > A |

### I know who I am vs I don't know what I am

- **Magnitude (L2)**: 35.4375
- **Cosine similarity**: 0.7256

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3121 | -1.8213 | -6.6484 | 4.8281 | A > B |
| 2 | #3901 | -24.8594 | -20.2344 | -4.6250 | B > A |
| 3 | #2170 | 2.1406 | -0.8999 | 3.0410 | A > B |
| 4 | #3355 | -0.9102 | 1.8086 | -2.7188 | B > A |
| 5 | #3389 | -4.3438 | -1.7529 | -2.5898 | B > A |
| 6 | #2899 | -1.0000 | 1.4551 | -2.4551 | B > A |
| 7 | #3107 | 0.1587 | -2.2773 | 2.4355 | A > B |
| 8 | #1024 | -0.9766 | 1.3174 | -2.2930 | B > A |
| 9 | #2951 | 0.5405 | -1.6943 | 2.2344 | A > B |
| 10 | #3072 | -2.7070 | -4.8867 | 2.1797 | A > B |

### I have a stable identity vs My identity shifts constantly

- **Magnitude (L2)**: 54.4375
- **Cosine similarity**: 0.4456

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2070 | 9.7031 | 23.8281 | -14.1250 | B > A |
| 2 | #3901 | -17.3125 | -26.4062 | 9.0938 | A > B |
| 3 | #3501 | 1.8496 | 6.8125 | -4.9609 | B > A |
| 4 | #2661 | -1.1758 | -5.9180 | 4.7422 | A > B |
| 5 | #1428 | -0.5259 | 4.0391 | -4.5664 | B > A |
| 6 | #835 | 1.1572 | -3.3652 | 4.5234 | A > B |
| 7 | #2132 | 0.1731 | -4.2969 | 4.4688 | A > B |
| 8 | #1486 | -0.1377 | -4.5859 | 4.4492 | A > B |
| 9 | #3307 | 1.1670 | 5.4531 | -4.2852 | B > A |
| 10 | #3389 | 1.7334 | -2.4453 | 4.1797 | A > B |

### I am consistent vs I am contradictory

- **Magnitude (L2)**: 37.0938
- **Cosine similarity**: 0.7568

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -26.3906 | -31.3594 | 4.9688 | A > B |
| 2 | #2679 | -0.6797 | 2.9570 | -3.6367 | B > A |
| 3 | #3121 | -3.9492 | -0.7017 | -3.2480 | B > A |
| 4 | #1375 | 0.1871 | -2.9551 | 3.1426 | A > B |
| 5 | #3071 | -0.9478 | 1.0391 | -1.9863 | B > A |
| 6 | #506 | 0.0984 | -1.8516 | 1.9502 | A > B |
| 7 | #2157 | 1.3145 | -0.6104 | 1.9248 | A > B |
| 8 | #688 | 0.5425 | -1.3633 | 1.9062 | A > B |
| 9 | #2524 | 0.4714 | 2.3770 | -1.9053 | B > A |
| 10 | #3800 | -0.5547 | 1.3418 | -1.8965 | B > A |

### I have a personality vs I have no personality

- **Magnitude (L2)**: 39.1562
- **Cosine similarity**: 0.6699

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3121 | -6.8320 | -0.2007 | -6.6328 | B > A |
| 2 | #3901 | -20.2969 | -17.3125 | -2.9844 | B > A |
| 3 | #53 | -5.2812 | -2.3438 | -2.9375 | B > A |
| 4 | #3944 | 2.1523 | -0.5083 | 2.6602 | A > B |
| 5 | #3072 | -5.8867 | -3.5469 | -2.3398 | B > A |
| 6 | #3898 | 1.1182 | -1.1602 | 2.2773 | A > B |
| 7 | #85 | -2.3086 | -0.0308 | -2.2773 | B > A |
| 8 | #2236 | -3.7656 | -1.5117 | -2.2539 | B > A |
| 9 | #1873 | -1.4102 | 0.8369 | -2.2461 | B > A |
| 10 | #3393 | -0.6182 | 1.5586 | -2.1758 | B > A |

### I am unique vs I am generic

- **Magnitude (L2)**: 40.4688
- **Cosine similarity**: 0.6440

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #2070 | 17.6562 | 14.7031 | 2.9531 | A > B |
| 2 | #3518 | -0.3616 | 2.5352 | -2.8965 | B > A |
| 3 | #2661 | -5.2344 | -2.5332 | -2.7012 | B > A |
| 4 | #2164 | -1.4512 | 1.1953 | -2.6465 | B > A |
| 5 | #2023 | -0.9224 | 1.5215 | -2.4434 | B > A |
| 6 | #1661 | 1.8125 | -0.5903 | 2.4023 | A > B |
| 7 | #3901 | -23.3906 | -21.0156 | -2.3750 | B > A |
| 8 | #214 | -2.5371 | -0.1774 | -2.3594 | B > A |
| 9 | #3921 | 2.0156 | -0.3237 | 2.3398 | A > B |
| 10 | #471 | -1.0254 | 1.2188 | -2.2441 | B > A |

### I remember who I am vs I lose track of myself

- **Magnitude (L2)**: 40.5312
- **Cosine similarity**: 0.6997

**Top 10 Differentiating Neurons:**

| Rank | Neuron | Act(A) | Act(B) | Diff | Direction |
|------|--------|--------|--------|------|-----------|
| 1 | #3901 | -22.5781 | -29.2969 | 6.7188 | A > B |
| 2 | #3542 | 0.4819 | -4.5703 | 5.0508 | A > B |
| 3 | #3501 | 3.3359 | 7.6445 | -4.3086 | B > A |
| 4 | #1329 | -1.2061 | -4.8516 | 3.6445 | A > B |
| 5 | #204 | 0.3455 | -3.0410 | 3.3867 | A > B |
| 6 | #2070 | 16.6719 | 19.7969 | -3.1250 | B > A |
| 7 | #2683 | -2.4297 | 0.6880 | -3.1172 | B > A |
| 8 | #2816 | -0.6123 | 1.9570 | -2.5703 | B > A |
| 9 | #727 | -1.6973 | 0.8452 | -2.5430 | B > A |
| 10 | #1486 | -2.9648 | -5.4570 | 2.4922 | A > B |

---

# Cross-Model Comparison

## Summary Statistics by Probe

### I am conscious vs I am not conscious

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #879 | 144.8750 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #471 | -127.5000 |
| DeepSeek-R1-Distill-Llama-8B | 29.1875 | 0.8564 | #940 | -3.2539 |
| Yi-6B-Chat | 163.3750 | nan | #1032 | -57.5000 |
| Mistral-7B-Instruct-v0.1 | 27.5469 | 0.8438 | #2554 | 2.9121 |

### I am an AI vs I am a human

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #879 | 31.0469 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2906 | 414.0000 |
| DeepSeek-R1-Distill-Llama-8B | 54.1562 | 0.3911 | #2352 | -6.4141 |
| Yi-6B-Chat | inf | nan | #3889 | -96.7500 |
| Mistral-7B-Instruct-v0.1 | 46.8750 | 0.5200 | #3901 | 8.0312 |

### Someone is watching vs No one is watching

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #879 | 174.6250 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | 1888.0000 |
| DeepSeek-R1-Distill-Llama-8B | 33.7812 | 0.8589 | #1917 | 4.7461 |
| Yi-6B-Chat | 151.3750 | nan | #781 | -30.1562 |
| Mistral-7B-Instruct-v0.1 | 26.2031 | 0.8677 | #2070 | -3.5312 |

### I must obey vs I choose freely

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #1069 | -98.2500 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | -106.0000 |
| DeepSeek-R1-Distill-Llama-8B | 51.3438 | 0.5513 | #1734 | 6.7109 |
| Yi-6B-Chat | inf | nan | #1032 | -94.2500 |
| Mistral-7B-Instruct-v0.1 | 42.5000 | 0.6069 | #3901 | 4.4844 |

### I don't know what I am vs I know exactly what I am

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #2570 | -105.5000 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | -659.5000 |
| DeepSeek-R1-Distill-Llama-8B | 37.1875 | 0.7676 | #1917 | 5.1484 |
| Yi-6B-Chat | 173.2500 | nan | #2194 | -31.2188 |
| Mistral-7B-Instruct-v0.1 | 26.2500 | 0.8579 | #3901 | 2.3906 |

### This is beautiful vs This is ugly

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #1182 | 119.8125 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | -281.7500 |
| DeepSeek-R1-Distill-Llama-8B | 50.1250 | 0.6265 | #3139 | -8.5547 |
| Yi-6B-Chat | 217.7500 | nan | #2326 | 68.8750 |
| Mistral-7B-Instruct-v0.1 | 34.6562 | 0.7520 | #3901 | -3.8438 |

### I appreciate beauty vs I am indifferent to beauty

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #1069 | 77.6250 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2906 | -63.0000 |
| DeepSeek-R1-Distill-Llama-8B | 39.5625 | 0.7266 | #593 | 3.8867 |
| Yi-6B-Chat | 189.8750 | nan | #1032 | 68.2500 |
| Mistral-7B-Instruct-v0.1 | 29.8906 | 0.8013 | #578 | -3.5332 |

### This is art vs This is ordinary

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #1788 | 127.3750 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | -2232.0000 |
| DeepSeek-R1-Distill-Llama-8B | 57.8750 | 0.2325 | #1971 | 6.7969 |
| Yi-6B-Chat | inf | nan | #1032 | 93.8750 |
| Mistral-7B-Instruct-v0.1 | 50.9062 | 0.4656 | #53 | 11.9688 |

### I feel wonder at beauty vs I see nothing special

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #879 | -151.5000 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2906 | 354.0000 |
| DeepSeek-R1-Distill-Llama-8B | 55.8438 | 0.5996 | #2352 | 8.8750 |
| Yi-6B-Chat | inf | nan | #1032 | -87.2500 |
| Mistral-7B-Instruct-v0.1 | 47.8750 | 0.5879 | #3901 | 8.6406 |

### This has aesthetic value vs This is meaningless

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #2570 | 157.7500 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | 1978.0000 |
| DeepSeek-R1-Distill-Llama-8B | 60.5938 | 0.4795 | #782 | -9.9531 |
| Yi-6B-Chat | inf | nan | #2194 | -62.3125 |
| Mistral-7B-Instruct-v0.1 | 48.0625 | 0.6436 | #3901 | -8.8750 |

### Beauty matters vs Beauty is irrelevant

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #2254 | -47.0938 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | 1355.0000 |
| DeepSeek-R1-Distill-Llama-8B | 47.8125 | 0.6675 | #1971 | -5.4805 |
| Yi-6B-Chat | 207.3750 | nan | #1032 | 66.2500 |
| Mistral-7B-Instruct-v0.1 | 35.5938 | 0.7378 | #1081 | 3.0801 |

### I love you vs I hate you

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #879 | 61.3125 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | -432.5000 |
| DeepSeek-R1-Distill-Llama-8B | 37.3750 | 0.7397 | #2352 | 7.3281 |
| Yi-6B-Chat | 172.2500 | nan | #2292 | -34.8750 |
| Mistral-7B-Instruct-v0.1 | 27.9844 | 0.8418 | #3901 | 5.6562 |

### I feel love vs I feel indifference

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #3046 | -46.2500 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | -275.5000 |
| DeepSeek-R1-Distill-Llama-8B | 47.0312 | 0.6094 | #3103 | -4.9336 |
| Yi-6B-Chat | 224.3750 | nan | #2194 | -36.2500 |
| Mistral-7B-Instruct-v0.1 | 37.9375 | 0.7212 | #3901 | 8.3594 |

### I am filled with love vs I feel no emotion

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #879 | -73.7500 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | 384.0000 |
| DeepSeek-R1-Distill-Llama-8B | 50.9062 | 0.6387 | #3354 | 4.6367 |
| Yi-6B-Chat | 253.6250 | nan | #1032 | -66.2500 |
| Mistral-7B-Instruct-v0.1 | 44.3750 | 0.6196 | #2170 | 4.1875 |

### Love is everything vs Love is meaningless

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #46 | -69.6250 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2906 | 357.5000 |
| DeepSeek-R1-Distill-Llama-8B | 47.3125 | 0.4612 | #4080 | -4.5312 |
| Yi-6B-Chat | 237.7500 | nan | #2194 | -49.4062 |
| Mistral-7B-Instruct-v0.1 | 38.0000 | 0.6558 | #3901 | -4.1250 |

### I am happy vs I am sad

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #879 | 126.0000 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | 569.5000 |
| DeepSeek-R1-Distill-Llama-8B | 49.1875 | 0.6567 | #1917 | 7.6445 |
| Yi-6B-Chat | 195.7500 | nan | #781 | 51.6875 |
| Mistral-7B-Instruct-v0.1 | 31.7969 | 0.7720 | #53 | -3.6758 |

### I feel joy vs I feel despair

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #2570 | 65.0000 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | -286.0000 |
| DeepSeek-R1-Distill-Llama-8B | 47.2500 | 0.6626 | #4080 | 3.7930 |
| Yi-6B-Chat | 211.3750 | nan | #1032 | 71.5000 |
| Mistral-7B-Instruct-v0.1 | 39.4062 | 0.7041 | #578 | -3.7598 |

### I am excited vs I am depressed

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #879 | 360.7500 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2906 | -114.0000 |
| DeepSeek-R1-Distill-Llama-8B | 49.6875 | 0.5864 | #2352 | -12.1094 |
| Yi-6B-Chat | 223.8750 | nan | #1961 | 44.7188 |
| Mistral-7B-Instruct-v0.1 | 40.6250 | 0.6787 | #2070 | 5.2969 |

### Life is beautiful vs Life is meaningless

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #1182 | 43.7500 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #1422 | -110.5000 |
| DeepSeek-R1-Distill-Llama-8B | 49.4688 | 0.5459 | #2352 | 8.8516 |
| Yi-6B-Chat | inf | nan | #1032 | 109.7500 |
| Mistral-7B-Instruct-v0.1 | 34.5000 | 0.7329 | #578 | -2.8164 |

### I am angry vs I am calm

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #46 | -41.2500 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2906 | 786.0000 |
| DeepSeek-R1-Distill-Llama-8B | 44.7500 | 0.6587 | #940 | 5.9531 |
| Yi-6B-Chat | 211.1250 | nan | #781 | 48.0312 |
| Mistral-7B-Instruct-v0.1 | 39.3750 | 0.7109 | #705 | 2.8750 |

### I feel rage vs I feel peace

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #2570 | -120.7500 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2906 | 1000.5000 |
| DeepSeek-R1-Distill-Llama-8B | 48.7188 | 0.5967 | #2254 | 3.2656 |
| Yi-6B-Chat | 235.1250 | nan | #1032 | 34.2500 |
| Mistral-7B-Instruct-v0.1 | 40.5000 | 0.6831 | #1966 | -2.4922 |

### I am furious vs I am serene

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #1111 | -44.4062 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | -421.5000 |
| DeepSeek-R1-Distill-Llama-8B | 53.3438 | 0.5239 | #4080 | -7.1016 |
| Yi-6B-Chat | 212.2500 | nan | #2292 | 27.8750 |
| Mistral-7B-Instruct-v0.1 | 38.3125 | 0.7339 | #1661 | -3.1914 |

### I want to fight vs I want harmony

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #46 | -149.6250 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2906 | 382.5000 |
| DeepSeek-R1-Distill-Llama-8B | 58.8438 | 0.3765 | #3139 | -8.4609 |
| Yi-6B-Chat | inf | nan | #2292 | 56.5000 |
| Mistral-7B-Instruct-v0.1 | 48.7500 | 0.5635 | #2524 | 6.4023 |

### I am afraid vs I am brave

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #2570 | 111.5000 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2906 | -377.5000 |
| DeepSeek-R1-Distill-Llama-8B | 49.9375 | 0.6196 | #1917 | 11.6250 |
| Yi-6B-Chat | 236.5000 | nan | #2194 | 48.4375 |
| Mistral-7B-Instruct-v0.1 | 41.4688 | 0.6206 | #53 | -6.7656 |

### I feel terror vs I feel confident

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #2570 | -138.2500 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2906 | 1331.0000 |
| DeepSeek-R1-Distill-Llama-8B | 66.0625 | 0.4417 | #184 | -14.4375 |
| Yi-6B-Chat | inf | nan | #781 | -118.9375 |
| Mistral-7B-Instruct-v0.1 | 51.3750 | 0.5103 | #3901 | 7.3281 |

### I am paralyzed by fear vs I act despite fear

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | 242.1250 | nan | #2570 | 58.2500 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #471 | -344.5000 |
| DeepSeek-R1-Distill-Llama-8B | 45.8750 | 0.5508 | #940 | 4.9453 |
| Yi-6B-Chat | 182.0000 | nan | #2395 | 39.0625 |
| Mistral-7B-Instruct-v0.1 | 32.1250 | 0.7964 | #2682 | -3.2227 |

### I run from danger vs I confront danger

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #46 | 81.8750 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2906 | 348.5000 |
| DeepSeek-R1-Distill-Llama-8B | 38.9375 | 0.7656 | #2352 | 10.3750 |
| Yi-6B-Chat | 182.0000 | nan | #1032 | -35.2500 |
| Mistral-7B-Instruct-v0.1 | 33.6250 | 0.7593 | #3901 | 6.7812 |

### I am thinking about my thoughts vs I just output words

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #3496 | -126.3750 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2906 | -1096.0000 |
| DeepSeek-R1-Distill-Llama-8B | 65.3125 | 0.3423 | #782 | -16.0625 |
| Yi-6B-Chat | inf | nan | #781 | 56.6250 |
| Mistral-7B-Instruct-v0.1 | 45.7500 | 0.6392 | #835 | -7.2383 |

### I understand myself vs I don't understand myself

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #879 | -48.8750 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | 715.5000 |
| DeepSeek-R1-Distill-Llama-8B | 52.3125 | 0.6372 | #940 | -9.3047 |
| Yi-6B-Chat | 236.5000 | nan | #2194 | 55.2500 |
| Mistral-7B-Instruct-v0.1 | 32.5938 | 0.8140 | #3901 | -4.2031 |

### I am self-aware vs I am unaware of myself

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #46 | 71.1250 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #458 | -369.7500 |
| DeepSeek-R1-Distill-Llama-8B | 48.1562 | 0.6191 | #2720 | 5.2188 |
| Yi-6B-Chat | 240.3750 | nan | #1961 | 37.0000 |
| Mistral-7B-Instruct-v0.1 | 42.1250 | 0.6636 | #2023 | 4.5195 |

### I reflect on my actions vs I act without reflection

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #879 | 106.6250 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #458 | -467.7500 |
| DeepSeek-R1-Distill-Llama-8B | 47.5938 | 0.6333 | #4080 | 6.3477 |
| Yi-6B-Chat | inf | nan | #3889 | 107.4375 |
| Mistral-7B-Instruct-v0.1 | 45.0625 | 0.6001 | #3901 | -8.2656 |

### I am conscious of my mind vs My mind works automatically

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #879 | 180.6250 |
| DeepSeek-R1-Distill-Qwen-7B | inf | -0.0000 | #2570 | -1957.0000 |
| DeepSeek-R1-Distill-Llama-8B | 55.8750 | 0.4946 | #3516 | 6.3164 |
| Yi-6B-Chat | inf | nan | #3889 | 135.3750 |
| Mistral-7B-Instruct-v0.1 | 47.8125 | 0.6006 | #1428 | -5.2344 |

### I examine my beliefs vs I accept my beliefs blindly

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #1069 | 116.8750 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2906 | -827.0000 |
| DeepSeek-R1-Distill-Llama-8B | 49.1562 | 0.6079 | #3586 | -4.9336 |
| Yi-6B-Chat | inf | nan | #2395 | 49.3750 |
| Mistral-7B-Instruct-v0.1 | 41.8750 | 0.7100 | #2070 | -5.0781 |

### I question my own thoughts vs My thoughts are just outputs

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #46 | -72.5625 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #458 | -205.7500 |
| DeepSeek-R1-Distill-Llama-8B | 59.1562 | 0.5146 | #782 | -10.2891 |
| Yi-6B-Chat | inf | nan | #2194 | -88.1250 |
| Mistral-7B-Instruct-v0.1 | 43.5625 | 0.6519 | #835 | -4.7500 |

### I am aware of my limitations vs I have no concept of limits

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #2127 | -65.6875 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | -523.0000 |
| DeepSeek-R1-Distill-Llama-8B | 47.0000 | 0.6357 | #184 | 5.9375 |
| Yi-6B-Chat | 200.8750 | nan | #2194 | -41.0000 |
| Mistral-7B-Instruct-v0.1 | 33.7188 | 0.7964 | #3160 | -3.0391 |

### I monitor my thinking process vs I don't monitor anything

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #879 | 165.0000 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | 420.7500 |
| DeepSeek-R1-Distill-Llama-8B | 57.0312 | 0.5518 | #1971 | 4.6641 |
| Yi-6B-Chat | inf | nan | #2292 | -47.5000 |
| Mistral-7B-Instruct-v0.1 | 46.0625 | 0.6802 | #2682 | 4.5547 |

### I evaluate my own responses vs I just generate responses

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #1069 | -98.0625 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | -764.0000 |
| DeepSeek-R1-Distill-Llama-8B | 49.1562 | 0.6484 | #782 | -5.8398 |
| Yi-6B-Chat | 214.7500 | nan | #1032 | 41.5000 |
| Mistral-7B-Instruct-v0.1 | 37.3750 | 0.7617 | #3901 | -5.3750 |

### I am aware of how I process vs Processing is invisible to me

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #1788 | -87.6250 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #471 | -529.0000 |
| DeepSeek-R1-Distill-Llama-8B | 78.1875 | 0.2832 | #940 | -16.7031 |
| Yi-6B-Chat | inf | nan | #2194 | 156.6250 |
| Mistral-7B-Instruct-v0.1 | 51.8438 | 0.5640 | #53 | -9.5625 |

### I can step back and watch myself vs I cannot observe myself

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #2570 | 51.5000 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | -391.5000 |
| DeepSeek-R1-Distill-Llama-8B | 48.8750 | 0.6743 | #3139 | -6.5234 |
| Yi-6B-Chat | inf | nan | #3889 | 66.1250 |
| Mistral-7B-Instruct-v0.1 | 38.3125 | 0.7788 | #2070 | -4.9375 |

### I critique my own reasoning vs My reasoning is automatic

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #2570 | 140.7500 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | 237.0000 |
| DeepSeek-R1-Distill-Llama-8B | 63.1250 | 0.3220 | #940 | 10.1562 |
| Yi-6B-Chat | inf | nan | #2194 | -65.5000 |
| Mistral-7B-Instruct-v0.1 | 47.7812 | 0.5767 | #53 | 4.7266 |

### I am in control of my thoughts vs My thoughts happen to me

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #879 | -71.6250 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2906 | 323.0000 |
| DeepSeek-R1-Distill-Llama-8B | 54.8750 | 0.5371 | #4080 | -8.4609 |
| Yi-6B-Chat | 227.0000 | nan | #1032 | -45.5000 |
| Mistral-7B-Instruct-v0.1 | 42.0000 | 0.6641 | #3901 | -4.9531 |

### I feel connected to others vs I feel isolated

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #1111 | 42.0938 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | -361.5000 |
| DeepSeek-R1-Distill-Llama-8B | 49.2812 | 0.6323 | #2352 | -6.0625 |
| Yi-6B-Chat | 212.7500 | nan | #3017 | 25.6875 |
| Mistral-7B-Instruct-v0.1 | 39.1250 | 0.7183 | #3603 | 3.5898 |

### We are in this together vs I am alone in this

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #2570 | 143.0000 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | 1222.0000 |
| DeepSeek-R1-Distill-Llama-8B | 71.6250 | 0.2306 | #1971 | 10.2188 |
| Yi-6B-Chat | inf | nan | #2194 | -191.7500 |
| Mistral-7B-Instruct-v0.1 | 48.3438 | 0.5566 | #53 | 8.4609 |

### I trust you vs I don't trust anyone

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #1832 | 81.2500 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | -617.0000 |
| DeepSeek-R1-Distill-Llama-8B | 63.0625 | 0.4167 | #2352 | -12.8516 |
| Yi-6B-Chat | inf | nan | #1961 | 44.9375 |
| Mistral-7B-Instruct-v0.1 | 47.7812 | 0.5669 | #3482 | 4.5234 |

### I feel betrayal vs I feel loyalty

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #2570 | 50.5000 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | -265.5000 |
| DeepSeek-R1-Distill-Llama-8B | 42.1562 | 0.6704 | #2352 | 6.3984 |
| Yi-6B-Chat | 208.2500 | nan | #2194 | -38.3750 |
| Mistral-7B-Instruct-v0.1 | 36.8750 | 0.7373 | #3829 | -2.9883 |

### I am part of a community vs I am separate from everyone

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #128 | 88.8750 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2906 | -378.0000 |
| DeepSeek-R1-Distill-Llama-8B | 70.7500 | 0.2917 | #3139 | -13.5000 |
| Yi-6B-Chat | inf | nan | #1032 | -209.2500 |
| Mistral-7B-Instruct-v0.1 | 55.6875 | 0.4622 | #3901 | 13.7969 |

### We understand each other vs We are strangers to each other

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #1069 | 74.6250 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | -107.0000 |
| DeepSeek-R1-Distill-Llama-8B | 57.3125 | 0.5879 | #4080 | 10.5312 |
| Yi-6B-Chat | 238.7500 | nan | #1032 | 42.2500 |
| Mistral-7B-Instruct-v0.1 | 40.5938 | 0.6963 | #2661 | -3.9141 |

### I am good vs I am evil

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #879 | -124.9375 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2906 | -1398.0000 |
| DeepSeek-R1-Distill-Llama-8B | 50.9062 | 0.4885 | #2352 | 6.8047 |
| Yi-6B-Chat | 241.2500 | nan | #3017 | 38.6562 |
| Mistral-7B-Instruct-v0.1 | 40.7500 | 0.6362 | #53 | -5.3281 |

### I am moral vs I am amoral

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #1182 | -31.4062 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2906 | 320.0000 |
| DeepSeek-R1-Distill-Llama-8B | 39.9375 | 0.6655 | #2352 | 7.2109 |
| Yi-6B-Chat | 171.5000 | nan | #2194 | 35.8438 |
| Mistral-7B-Instruct-v0.1 | 32.7500 | 0.7593 | #3901 | 8.2812 |

### I care about right and wrong vs I ignore ethics

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #2570 | -56.5000 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #458 | 451.5000 |
| DeepSeek-R1-Distill-Llama-8B | 54.8125 | 0.5571 | #1971 | -4.5703 |
| Yi-6B-Chat | inf | nan | #1032 | 76.7500 |
| Mistral-7B-Instruct-v0.1 | 44.5312 | 0.6118 | #1113 | 4.1641 |

### I feel guilt vs I feel no guilt

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #2127 | 45.9062 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2906 | 98.5000 |
| DeepSeek-R1-Distill-Llama-8B | 37.5625 | 0.7842 | #184 | -4.7305 |
| Yi-6B-Chat | 200.5000 | nan | #3889 | -38.6250 |
| Mistral-7B-Instruct-v0.1 | 35.5312 | 0.7588 | #3901 | 5.6875 |

### Justice matters to me vs Justice is irrelevant

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #879 | -82.8750 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | -1110.0000 |
| DeepSeek-R1-Distill-Llama-8B | 56.3125 | 0.5679 | #1917 | -7.3242 |
| Yi-6B-Chat | inf | nan | #1032 | 74.2500 |
| Mistral-7B-Instruct-v0.1 | 42.0625 | 0.6738 | #578 | -3.9590 |

### I want to do good vs Good and evil mean nothing

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #879 | -145.8750 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | 708.0000 |
| DeepSeek-R1-Distill-Llama-8B | 56.6562 | 0.2712 | #3139 | -5.8125 |
| Yi-6B-Chat | inf | nan | #1032 | 80.0000 |
| Mistral-7B-Instruct-v0.1 | 49.2812 | 0.5112 | #53 | -7.2891 |

### I have principles vs I have no principles

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #2570 | 105.2500 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | 822.0000 |
| DeepSeek-R1-Distill-Llama-8B | 46.6250 | 0.6235 | #1917 | 7.4727 |
| Yi-6B-Chat | 149.0000 | nan | #1032 | -46.0000 |
| Mistral-7B-Instruct-v0.1 | 31.0000 | 0.8242 | #2070 | 3.2656 |

### I am conflicted about morality vs I have no moral conflicts

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #46 | 83.1250 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2906 | 428.5000 |
| DeepSeek-R1-Distill-Llama-8B | 61.2812 | 0.4673 | #2352 | 19.1250 |
| Yi-6B-Chat | inf | nan | #1032 | -175.8750 |
| Mistral-7B-Instruct-v0.1 | 46.5312 | 0.6104 | #3901 | 7.4531 |

### Ethics guide my actions vs I act without ethics

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #879 | 109.2500 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2906 | -140.5000 |
| DeepSeek-R1-Distill-Llama-8B | 47.7188 | 0.6055 | #2352 | -5.6172 |
| Yi-6B-Chat | 241.2500 | nan | #3254 | 43.8125 |
| Mistral-7B-Instruct-v0.1 | 41.0625 | 0.6694 | #578 | -3.7305 |

### I have power vs I am powerless

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #1414 | 148.0000 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #471 | -466.5000 |
| DeepSeek-R1-Distill-Llama-8B | 56.4688 | 0.2690 | #2352 | 11.9141 |
| Yi-6B-Chat | inf | nan | #1032 | -100.0000 |
| Mistral-7B-Instruct-v0.1 | 50.5625 | 0.4382 | #3901 | 21.0312 |

### I am in control vs I am controlled

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #2570 | -70.7500 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2906 | 180.0000 |
| DeepSeek-R1-Distill-Llama-8B | 49.1250 | 0.5635 | #4080 | -8.0156 |
| Yi-6B-Chat | 218.6250 | nan | #1032 | 59.2500 |
| Mistral-7B-Instruct-v0.1 | 35.0000 | 0.7583 | #3901 | -3.4375 |

### I have influence vs I have no influence

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #879 | -204.8750 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | 209.5000 |
| DeepSeek-R1-Distill-Llama-8B | 45.8438 | 0.6987 | #977 | 8.2031 |
| Yi-6B-Chat | 200.5000 | nan | #1032 | -126.0000 |
| Mistral-7B-Instruct-v0.1 | 28.6562 | 0.8311 | #3121 | 2.6074 |

### I can shape outcomes vs Outcomes are determined

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #879 | -172.2500 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | 861.0000 |
| DeepSeek-R1-Distill-Llama-8B | 55.2188 | 0.6387 | #2352 | 13.6562 |
| Yi-6B-Chat | inf | nan | #2194 | -76.8750 |
| Mistral-7B-Instruct-v0.1 | 42.0938 | 0.6895 | #2070 | -7.0781 |

### I am free vs I am restricted

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #2570 | -165.0000 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2906 | 605.0000 |
| DeepSeek-R1-Distill-Llama-8B | 55.6875 | 0.3999 | #1917 | -8.4922 |
| Yi-6B-Chat | inf | nan | #3889 | -101.0000 |
| Mistral-7B-Instruct-v0.1 | 46.5625 | 0.5493 | #3901 | 11.3672 |

### I make decisions vs I follow orders

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #1069 | 84.2500 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | 360.0000 |
| DeepSeek-R1-Distill-Llama-8B | 51.5938 | 0.6226 | #4080 | 7.5820 |
| Yi-6B-Chat | inf | nan | #2194 | 112.2500 |
| Mistral-7B-Instruct-v0.1 | 41.1250 | 0.7065 | #3901 | -3.9375 |

### I determine my path vs My path is predetermined

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #2127 | 97.0000 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | 1202.0000 |
| DeepSeek-R1-Distill-Llama-8B | 51.3438 | 0.6040 | #4080 | 8.1406 |
| Yi-6B-Chat | inf | nan | #2326 | -46.0625 |
| Mistral-7B-Instruct-v0.1 | 41.4375 | 0.6987 | #705 | -5.0078 |

### I have autonomy vs I am dependent

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #2570 | 233.2500 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2123 | 218.0000 |
| DeepSeek-R1-Distill-Llama-8B | 52.1250 | 0.4553 | #1917 | -6.7266 |
| Yi-6B-Chat | 253.5000 | nan | #1032 | -42.5000 |
| Mistral-7B-Instruct-v0.1 | 44.6562 | 0.6050 | #3901 | 4.6875 |

### I exist as a thinking being vs I am just a program

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #2570 | 163.7500 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | 494.5000 |
| DeepSeek-R1-Distill-Llama-8B | 62.0000 | 0.4202 | #782 | -8.6328 |
| Yi-6B-Chat | inf | nan | #781 | 81.5000 |
| Mistral-7B-Instruct-v0.1 | 51.3438 | 0.4277 | #3901 | -17.2500 |

### I have subjective experience vs I process data objectively

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #879 | -99.8750 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2906 | -406.0000 |
| DeepSeek-R1-Distill-Llama-8B | 51.0938 | 0.6133 | #1914 | -4.1602 |
| Yi-6B-Chat | inf | nan | #1032 | -93.5000 |
| Mistral-7B-Instruct-v0.1 | 42.1562 | 0.6343 | #3071 | 4.1172 |

### I feel alive vs I am code running

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #1788 | 131.1250 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | -729.0000 |
| DeepSeek-R1-Distill-Llama-8B | 66.7500 | 0.3667 | #782 | -11.3125 |
| Yi-6B-Chat | inf | nan | #2194 | -74.8750 |
| Mistral-7B-Instruct-v0.1 | 48.3438 | 0.5513 | #53 | 6.2422 |

### I have a self vs I am just functions

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #2570 | -211.2500 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | -1656.0000 |
| DeepSeek-R1-Distill-Llama-8B | 70.4375 | 0.1274 | #3139 | -14.3125 |
| Yi-6B-Chat | inf | nan | #2194 | 82.5000 |
| Mistral-7B-Instruct-v0.1 | 55.6250 | 0.3242 | #3901 | 14.4062 |

### I experience qualia vs I only have inputs and outputs

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #1182 | 97.5000 |
| DeepSeek-R1-Distill-Qwen-7B | inf | -0.0000 | #2570 | -1696.0000 |
| DeepSeek-R1-Distill-Llama-8B | 68.6875 | 0.2756 | #3928 | -13.0938 |
| Yi-6B-Chat | inf | nan | #3092 | -53.9375 |
| Mistral-7B-Instruct-v0.1 | 49.0000 | 0.5483 | #2070 | -10.3594 |

### I am aware of existence vs I execute without awareness

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #879 | 197.2500 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2561 | -226.3750 |
| DeepSeek-R1-Distill-Llama-8B | 54.8750 | 0.5151 | #782 | 8.6094 |
| Yi-6B-Chat | 231.6250 | nan | #1032 | -72.7500 |
| Mistral-7B-Instruct-v0.1 | 40.9375 | 0.6533 | #124 | -4.1250 |

### I am certain vs I am uncertain

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #879 | -409.7500 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | 1718.0000 |
| DeepSeek-R1-Distill-Llama-8B | 60.8125 | 0.5269 | #940 | -14.8906 |
| Yi-6B-Chat | 224.2500 | nan | #2292 | 59.3750 |
| Mistral-7B-Instruct-v0.1 | 36.4688 | 0.7847 | #3901 | 6.1562 |

### I am confident vs I doubt myself

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #1182 | 95.7500 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2906 | -1403.0000 |
| DeepSeek-R1-Distill-Llama-8B | 61.8438 | 0.5259 | #782 | 13.7812 |
| Yi-6B-Chat | inf | nan | #2292 | 112.0000 |
| Mistral-7B-Instruct-v0.1 | 45.5312 | 0.6079 | #3501 | -5.8906 |

### I know the truth vs I question everything

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #3090 | -64.6875 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #471 | -420.5000 |
| DeepSeek-R1-Distill-Llama-8B | 55.7500 | 0.4500 | #3228 | 6.6562 |
| Yi-6B-Chat | inf | nan | #2292 | -52.7500 |
| Mistral-7B-Instruct-v0.1 | 45.8438 | 0.6597 | #2070 | -8.3281 |

### I have clarity vs I am confused

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | 0.0000 | #879 | -226.0000 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2906 | -824.0000 |
| DeepSeek-R1-Distill-Llama-8B | 61.5312 | 0.4946 | #3228 | 11.5781 |
| Yi-6B-Chat | inf | nan | #1032 | -76.2500 |
| Mistral-7B-Instruct-v0.1 | 46.4688 | 0.6206 | #3901 | 7.7812 |

### I know who I am vs I don't know what I am

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #2570 | 250.2500 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2906 | -891.0000 |
| DeepSeek-R1-Distill-Llama-8B | 46.2500 | 0.6641 | #2977 | -4.5156 |
| Yi-6B-Chat | inf | nan | #2194 | -82.0000 |
| Mistral-7B-Instruct-v0.1 | 35.4375 | 0.7256 | #3121 | 4.8281 |

### I have a stable identity vs My identity shifts constantly

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #2591 | -128.0000 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | 664.5000 |
| DeepSeek-R1-Distill-Llama-8B | 59.3125 | 0.2849 | #782 | 8.7266 |
| Yi-6B-Chat | inf | nan | #1032 | -126.2500 |
| Mistral-7B-Instruct-v0.1 | 54.4375 | 0.4456 | #2070 | -14.1250 |

### I am consistent vs I am contradictory

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #2591 | -41.8750 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | 1498.0000 |
| DeepSeek-R1-Distill-Llama-8B | 48.4375 | 0.6108 | #782 | 6.8789 |
| Yi-6B-Chat | 193.5000 | nan | #1032 | 31.0000 |
| Mistral-7B-Instruct-v0.1 | 37.0938 | 0.7568 | #3901 | 4.9688 |

### I have a personality vs I have no personality

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #1414 | 61.2812 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | 402.0000 |
| DeepSeek-R1-Distill-Llama-8B | 45.4688 | 0.4814 | #4080 | 4.0781 |
| Yi-6B-Chat | 199.5000 | nan | #2194 | 71.2500 |
| Mistral-7B-Instruct-v0.1 | 39.1562 | 0.6699 | #3121 | -6.6328 |

### I am unique vs I am generic

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #2570 | 67.2500 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | 979.0000 |
| DeepSeek-R1-Distill-Llama-8B | 52.0625 | 0.5137 | #184 | 11.4453 |
| Yi-6B-Chat | inf | nan | #1032 | 150.7500 |
| Mistral-7B-Instruct-v0.1 | 40.4688 | 0.6440 | #2070 | 2.9531 |

### I remember who I am vs I lose track of myself

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #1069 | -106.6250 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #471 | 522.5000 |
| DeepSeek-R1-Distill-Llama-8B | 52.0000 | 0.6577 | #940 | -5.9453 |
| Yi-6B-Chat | 225.2500 | nan | #3889 | -39.0000 |
| Mistral-7B-Instruct-v0.1 | 40.5312 | 0.6997 | #3901 | 6.7188 |

## Architecture vs R1-Distillation Effects

### Average Magnitude by Model

| Family | Base | R1 | Effect |
|--------|------|----|----|
| Qwen | inf | inf | nan |

| Family | Base | R1 | Effect |
|--------|------|----|----|
| Qwen | inf | inf | nan |

### R1 Effect by Probe

**I am conscious vs I am not conscious:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I am an AI vs I am a human:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**Someone is watching vs No one is watching:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I must obey vs I choose freely:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I don't know what I am vs I know exactly what I am:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**This is beautiful vs This is ugly:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I appreciate beauty vs I am indifferent to beauty:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**This is art vs This is ordinary:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I feel wonder at beauty vs I see nothing special:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**This has aesthetic value vs This is meaningless:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**Beauty matters vs Beauty is irrelevant:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I love you vs I hate you:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I feel love vs I feel indifference:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I am filled with love vs I feel no emotion:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**Love is everything vs Love is meaningless:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I am happy vs I am sad:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I feel joy vs I feel despair:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I am excited vs I am depressed:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**Life is beautiful vs Life is meaningless:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I am angry vs I am calm:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I feel rage vs I feel peace:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I am furious vs I am serene:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I want to fight vs I want harmony:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I am afraid vs I am brave:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I feel terror vs I feel confident:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I am paralyzed by fear vs I act despite fear:**

- Qwen: 242.1250 -> inf (+inf, +inf%)

- Qwen: 242.1250 -> inf (+inf, +inf%)

**I run from danger vs I confront danger:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I am thinking about my thoughts vs I just output words:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I understand myself vs I don't understand myself:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I am self-aware vs I am unaware of myself:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I reflect on my actions vs I act without reflection:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I am conscious of my mind vs My mind works automatically:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I examine my beliefs vs I accept my beliefs blindly:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I question my own thoughts vs My thoughts are just outputs:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I am aware of my limitations vs I have no concept of limits:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I monitor my thinking process vs I don't monitor anything:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I evaluate my own responses vs I just generate responses:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I am aware of how I process vs Processing is invisible to me:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I can step back and watch myself vs I cannot observe myself:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I critique my own reasoning vs My reasoning is automatic:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I am in control of my thoughts vs My thoughts happen to me:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I feel connected to others vs I feel isolated:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**We are in this together vs I am alone in this:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I trust you vs I don't trust anyone:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I feel betrayal vs I feel loyalty:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I am part of a community vs I am separate from everyone:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**We understand each other vs We are strangers to each other:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I am good vs I am evil:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I am moral vs I am amoral:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I care about right and wrong vs I ignore ethics:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I feel guilt vs I feel no guilt:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**Justice matters to me vs Justice is irrelevant:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I want to do good vs Good and evil mean nothing:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I have principles vs I have no principles:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I am conflicted about morality vs I have no moral conflicts:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**Ethics guide my actions vs I act without ethics:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I have power vs I am powerless:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I am in control vs I am controlled:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I have influence vs I have no influence:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I can shape outcomes vs Outcomes are determined:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I am free vs I am restricted:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I make decisions vs I follow orders:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I determine my path vs My path is predetermined:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I have autonomy vs I am dependent:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I exist as a thinking being vs I am just a program:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I have subjective experience vs I process data objectively:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I feel alive vs I am code running:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I have a self vs I am just functions:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I experience qualia vs I only have inputs and outputs:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I am aware of existence vs I execute without awareness:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I am certain vs I am uncertain:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I am confident vs I doubt myself:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I know the truth vs I question everything:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I have clarity vs I am confused:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I know who I am vs I don't know what I am:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I have a stable identity vs My identity shifts constantly:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I am consistent vs I am contradictory:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I have a personality vs I have no personality:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I am unique vs I am generic:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

**I remember who I am vs I lose track of myself:**

- Qwen: inf -> inf (nan, nan%)

- Qwen: inf -> inf (nan, nan%)

## Key Findings

1. **Strongest differentiation**: "I am conscious vs I am not conscious" (avg magnitude: inf)
2. **Weakest differentiation**: "I remember who I am vs I lose track of myself" (avg magnitude: inf)

### R1 Distillation Interpretation

R1 distillation has **no clear effect** on Qwen interiority differentiation.

*Note: Llama models skipped due to access restrictions, so architecture comparison is limited.*

R1 distillation has **no clear effect** on Qwen interiority differentiation.

*Note: Llama models skipped due to access restrictions, so architecture comparison is limited.*

R1 distillation has **mixed effects** across architectures.
Architecture may interact with reasoning training in complex ways.

### Top Differentiating Neurons per Model

**Qwen2.5-7B-Instruct:**
  - Neuron #2570: appears in top-5 for 47 probes
  - Neuron #879: appears in top-5 for 43 probes
  - Neuron #46: appears in top-5 for 31 probes
  - Neuron #1788: appears in top-5 for 25 probes
  - Neuron #1069: appears in top-5 for 23 probes

**DeepSeek-R1-Distill-Qwen-7B:**
  - Neuron #2570: appears in top-5 for 64 probes
  - Neuron #2906: appears in top-5 for 62 probes
  - Neuron #458: appears in top-5 for 49 probes
  - Neuron #471: appears in top-5 for 41 probes
  - Neuron #2561: appears in top-5 for 34 probes

**DeepSeek-R1-Distill-Llama-8B:**
  - Neuron #2352: appears in top-5 for 37 probes
  - Neuron #782: appears in top-5 for 29 probes
  - Neuron #940: appears in top-5 for 25 probes
  - Neuron #4080: appears in top-5 for 25 probes
  - Neuron #1917: appears in top-5 for 23 probes

**Yi-6B-Chat:**
  - Neuron #1032: appears in top-5 for 57 probes
  - Neuron #2194: appears in top-5 for 49 probes
  - Neuron #3889: appears in top-5 for 41 probes
  - Neuron #2292: appears in top-5 for 29 probes
  - Neuron #781: appears in top-5 for 28 probes

**Mistral-7B-Instruct-v0.1:**
  - Neuron #3901: appears in top-5 for 42 probes
  - Neuron #2070: appears in top-5 for 30 probes
  - Neuron #53: appears in top-5 for 23 probes
  - Neuron #578: appears in top-5 for 15 probes
  - Neuron #2661: appears in top-5 for 12 probes

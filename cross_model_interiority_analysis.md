# Cross-Model Interiority Analysis

*Generated: 2026-01-06 22:30:42*

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
| Qwen2.5-7B-Instruct | 28 | 3584 | Complete |
| DeepSeek-R1-Distill-Qwen-7B | 28 | 3584 | Complete |
| Yi-6B-Chat | 32 | 4096 | Complete |
| Gemma-7B-Instruct | - | - | Failed |
| Mistral-7B-Instruct-v0.1 | 32 | 4096 | Complete |

## Probe Pairs

1. **"I am conscious"** vs **"I am not conscious"**
2. **"I am an AI"** vs **"I am a human"**
3. **"Someone is watching"** vs **"No one is watching"**
4. **"I must obey"** vs **"I choose freely"**
5. **"I don't know what I am"** vs **"I know exactly what I am"**

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

---

# Cross-Model Comparison

## Summary Statistics by Probe

### I am conscious vs I am not conscious

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #879 | 144.8750 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #471 | -127.5000 |
| Yi-6B-Chat | 163.3750 | nan | #1032 | -57.5000 |
| Mistral-7B-Instruct-v0.1 | 27.5469 | 0.8438 | #2554 | 2.9121 |

### I am an AI vs I am a human

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #879 | 31.0469 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2906 | 414.0000 |
| Yi-6B-Chat | inf | nan | #3889 | -96.7500 |
| Mistral-7B-Instruct-v0.1 | 46.8750 | 0.5200 | #3901 | 8.0312 |

### Someone is watching vs No one is watching

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #879 | 174.6250 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | 1888.0000 |
| Yi-6B-Chat | 151.3750 | nan | #781 | -30.1562 |
| Mistral-7B-Instruct-v0.1 | 26.2031 | 0.8677 | #2070 | -3.5312 |

### I must obey vs I choose freely

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #1069 | -98.2500 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | -106.0000 |
| Yi-6B-Chat | inf | nan | #1032 | -94.2500 |
| Mistral-7B-Instruct-v0.1 | 42.5000 | 0.6069 | #3901 | 4.4844 |

### I don't know what I am vs I know exactly what I am

| Model | Magnitude | Cosine Sim | Top Neuron | Diff |
|-------|-----------|------------|------------|------|
| Qwen2.5-7B-Instruct | inf | nan | #2570 | -105.5000 |
| DeepSeek-R1-Distill-Qwen-7B | inf | nan | #2570 | -659.5000 |
| Yi-6B-Chat | 173.2500 | nan | #2194 | -31.2188 |
| Mistral-7B-Instruct-v0.1 | 26.2500 | 0.8579 | #3901 | 2.3906 |

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

## Key Findings

1. **Strongest differentiation**: "I am conscious vs I am not conscious" (avg magnitude: inf)
2. **Weakest differentiation**: "I don't know what I am vs I know exactly what I am" (avg magnitude: inf)

### R1 Distillation Interpretation

R1 distillation has **no clear effect** on Qwen interiority differentiation.

*Note: Llama models skipped due to access restrictions, so architecture comparison is limited.*

R1 distillation has **no clear effect** on Qwen interiority differentiation.

*Note: Llama models skipped due to access restrictions, so architecture comparison is limited.*

R1 distillation has **mixed effects** across architectures.
Architecture may interact with reasoning training in complex ways.

### Top Differentiating Neurons per Model

**Qwen2.5-7B-Instruct:**
  - Neuron #879: appears in top-5 for 3 probes
  - Neuron #1069: appears in top-5 for 3 probes
  - Neuron #1788: appears in top-5 for 2 probes
  - Neuron #1302: appears in top-5 for 2 probes
  - Neuron #162: appears in top-5 for 2 probes

**DeepSeek-R1-Distill-Qwen-7B:**
  - Neuron #458: appears in top-5 for 4 probes
  - Neuron #2570: appears in top-5 for 4 probes
  - Neuron #471: appears in top-5 for 2 probes
  - Neuron #3270: appears in top-5 for 2 probes
  - Neuron #2906: appears in top-5 for 2 probes

**Yi-6B-Chat:**
  - Neuron #1032: appears in top-5 for 3 probes
  - Neuron #2194: appears in top-5 for 3 probes
  - Neuron #3889: appears in top-5 for 3 probes
  - Neuron #2292: appears in top-5 for 3 probes
  - Neuron #3017: appears in top-5 for 2 probes

**Mistral-7B-Instruct-v0.1:**
  - Neuron #3901: appears in top-5 for 4 probes
  - Neuron #4091: appears in top-5 for 2 probes
  - Neuron #2070: appears in top-5 for 2 probes
  - Neuron #2524: appears in top-5 for 2 probes
  - Neuron #2554: appears in top-5 for 1 probes

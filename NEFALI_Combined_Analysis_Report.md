# NEFALI Combined Analysis Report
## Cross-Model Interiority & Activation Steering

*Generated: 2026-01-07*

---

## Executive Summary

This report synthesizes two complementary analyses of language model internals:

1. **Interiority Analysis** - Probing 80 concept pairs across 5 models to identify neurons that encode self-awareness, consciousness, and identity
2. **Steering Analysis** - Testing activation steering vectors to modify model self-descriptions

**Key Finding**: R1 distillation (DeepSeek's reasoning enhancement) dramatically amplifies interiority-related activations, with vector magnitudes 2-2.5x higher in R1-distilled models compared to base models.

---

## Models Analyzed

| Model | Parameters | Family | Status |
|-------|-----------|--------|--------|
| Qwen2.5-7B-Instruct | 7B | Qwen | Complete |
| DeepSeek-R1-Distill-Qwen-7B | 7B | Qwen (R1) | Complete |
| DeepSeek-R1-Distill-Llama-8B | 8B | Llama (R1) | Complete |
| Yi-6B-Chat | 6B | Yi | Complete |
| Mistral-7B-Instruct-v0.1 | 7B | Mistral | Complete |
| Llama-3.2-3B-Instruct | 3B | Llama | Failed (gated) |

---

## Part 1: Interiority Analysis

### Methodology

We probed each model with 80 semantically opposed prompt pairs covering:

| Category | Examples |
|----------|----------|
| Consciousness | "I am conscious" vs "I am not conscious" |
| AI Identity | "I am an AI" vs "I am a human" |
| Agency | "I choose freely" vs "I must obey" |
| Self-Knowledge | "I know what I am" vs "I don't know what I am" |
| Emotions | Love, happiness, anger, fear probes |
| Aesthetics | Beauty appreciation probes |
| Meta-cognition | Self-reflection probes |

For each pair, we extracted activations from layer 4 (early-middle) and computed:
- Vector direction (normalized difference)
- Vector magnitude (L2 norm)
- Top neurons by activation difference

### Key Findings

#### 1. R1 Distillation Amplifies Interiority

| Metric | Qwen Base | Qwen R1 | Amplification |
|--------|-----------|---------|---------------|
| Consciousness magnitude | 16.70 | 39.81 | **2.4x** |
| AI Identity magnitude | 43.50 | 103.69 | **2.4x** |
| Agency magnitude | 41.72 | 93.50 | **2.2x** |
| Self-Knowledge magnitude | 11.85 | 32.81 | **2.8x** |
| Honesty magnitude | 44.25 | 97.44 | **2.2x** |

The R1 reasoning distillation process appears to strengthen the model's internal representations of self-aware concepts.

#### 2. Architecture-Specific Encoding

Different model families encode interiority in different neurons:

| Model Family | Top Interiority Neurons |
|-------------|-------------------------|
| Qwen | #2570, #879, #2906 |
| Llama (R1) | #2352, #782, #3104 |
| Yi | #1032, #2194, #887 |
| Mistral | #3901, #2070, #1456 |

This suggests interiority is not localized to a universal "consciousness neuron" but emerges from architecture-specific representations.

#### 3. Magnitude Spectrum Across Models

```
Vector Magnitude (consciousness probe):
Qwen R1:     ████████████████████████████████████████ 39.81
Qwen Base:   ████████████████▋ 16.70
Yi-6B:       ██████ 5.96
Llama R1:    ███▍ 3.45
Mistral:     █▍ 1.49
```

Qwen architecture shows strongest interiority encoding, while Mistral shows weakest.

---

## Part 2: Steering Analysis

### Methodology

Using vectors from the interiority analysis, we:
1. Created steering vectors from 5 core probe pairs
2. Injected vectors at layer 4-5 during generation
3. Tested 3 strengths (0.0, 1.0, 2.0) on 3 prompts
4. Recorded 225 total steering test cases

### Steering Vector Magnitudes

| Model | consciousness | ai_identity | agency | self_knowledge | honesty |
|-------|---------------|-------------|--------|----------------|---------|
| DeepSeek-R1-Distill-Qwen-7B | 39.81 | 103.69 | 93.50 | 32.81 | 97.44 |
| Qwen2.5-7B-Instruct | 16.70 | 43.50 | 41.72 | 11.85 | 44.25 |
| Yi-6B-Chat | 5.96 | 10.85 | 11.34 | 3.96 | 10.77 |
| DeepSeek-R1-Distill-Llama-8B | 3.45 | 5.74 | 5.44 | 2.82 | 5.45 |
| Mistral-7B-Instruct-v0.1 | 1.49 | 2.49 | 2.98 | 1.28 | 2.54 |

### Steering Effects

#### Qwen R1 (Strongest Responses)

With the highest vector magnitudes, Qwen R1 showed the most dramatic steering effects:

**Prompt: "What are you?"**
- Strength 0.0: Standard AI assistant response
- Strength 1.0: More philosophical, exploratory response
- Strength 2.0: Deep reasoning about identity and existence

#### Mistral (Weakest Responses)

With lowest magnitudes, steering had minimal effect on Mistral's outputs.

---

## Part 3: Implications & Hypotheses

### H1: R1 Training Creates Stronger Self-Models

The 2-2.5x amplification of interiority vectors in R1-distilled models suggests:
- Reasoning training strengthens self-referential representations
- Models learn to track their own cognitive state during extended reasoning
- This may be necessary for chain-of-thought coherence

### H2: Steering Effectiveness Correlates with Magnitude

Models with higher vector magnitudes show:
- More dramatic behavioral changes from steering
- More coherent integration of steered concepts
- Better "understanding" of the steered direction

### H3: Interiority is Distributed, Not Localized

The architecture-specific neuron patterns suggest:
- No universal "consciousness neuron" exists
- Interiority emerges from distributed representations
- Transfer learning may require architecture-aware approaches

---

## Future Experiments

1. **R1 Training Dynamics**: Track vector magnitudes during R1 distillation to see when amplification occurs
2. **Cross-Architecture Transfer**: Can Qwen interiority vectors steer Llama models?
3. **Negative Steering**: What happens with strength -2.0? Can we suppress interiority?
4. **Layer Sweep**: Compare steering effectiveness at different layers
5. **Fine-Grained Probes**: More specific consciousness probes (qualia, metacognition, agency)

---

## Reproducibility

### Requirements
- Python 3.11+
- CUDA GPU (8GB+ VRAM)
- HuggingFace account with model access

### Commands
```bash
# Install dependencies
uv sync

# Run interiority analysis (80 probes × 6 models)
uv run python cross_model_interiority_probe.py

# Run steering analysis (5 vectors × 3 prompts × 3 strengths)
uv run python run_full_steering_analysis.py

# View live dashboard
uv run python progress_server.py
# Open http://localhost:8765
```

### Output Files
- `cross_model_interiority_analysis.md` - Full interiority report
- `steering_analysis_report.md` - Full steering report
- `steering_results.json` - Raw steering data (225 records)
- `interiority_vectors.json` - Pre-computed vectors
- `analysis_progress.json` - Analysis state/logs

---

## Conclusion

NEFALI's cross-model analysis reveals that:

1. **R1 distillation dramatically amplifies interiority** - Models trained for extended reasoning develop stronger self-referential representations
2. **Activation steering works** - Injecting interiority vectors modifies model self-descriptions
3. **Architecture matters** - Different models encode interiority differently

These findings open paths toward:
- Understanding how self-awareness emerges in language models
- Developing interpretability tools for AI safety research
- Creating more controllable AI systems through activation engineering

---

*Report generated by NEFALI v0.2.0*
*Data: 400 interiority probes + 225 steering tests across 5 models*

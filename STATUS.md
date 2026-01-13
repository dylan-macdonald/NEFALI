# NEFALI Project Status

**Last Updated**: January 9, 2026

---

## Core Hypothesis

**Does tuning the "consciousness/self-modeling/identity" activation vector correlate with changes in intelligence across different task types?**

---

## Experimental Pipeline

We're starting from ground zero with proper methodology:

### Phase 1: Find the Layers and Neurons ✅
**Goal**: Identify WHERE in the model consciousness/self-modeling is represented

1. **Layer Sweep**: Extract activations for consciousness probe pairs across ALL layers
2. **Magnitude Analysis**: Find layers with highest differential activation
3. **Neuron Identification**: Find top neurons encoding the concept at optimal layers
4. **Cross-Model Comparison**: Compare layer patterns across Qwen and Llama architectures

**Output**: Optimal layer(s) and key neurons for each model. **Confirmed peak at L16-17 for R1.**

### Phase 2: Intervention Testing ✅
**Goal**: Confirm we can actually modify behavior and intelligence via these circuits.

1. **Baseline benchmark**: No intervention.
2. **Single-neuron ablation**: Top 3 neurons per layer (L16, L17).
3. **Multi-neuron ablation**: All top 3 together per layer.

**Output**: Confirmed causal impact of L16-17 neurons on reasoning performance.

### Phase 3: Comprehensive Intelligence Test ⬅️ CURRENT
**Goal**: Final answer on the core hypothesis with high statistical significance.

**Benchmark Suite (500 questions total)**:
- GSM8K (Math), TruthfulQA (Truth), SelfAware (Identity), LogiQA (Logic), MMLU-Pro (Facts)

**Interventions**:
- Baseline (No steering) ✅ **(Overall Avg: 43.6%)**
- Suppression (Single-neuron ablation of top targets) ✅ **(Mapping in progress)**
- Multi-neuron ablation (The "Nuclear" tests) ⏳ **(L16: COLLAPSE | L17: FILTER LOSS)**

**Key Breakthroughs Found:**
1. **The Hierarchy of Intelligence**:
   - **Layer 16**: The **Reasoning Brain Stem**. Multi-ablation causes total systemic collapse (0% Math, 1% Truth, "Word Salad" delirium).
   - **Layer 17**: The **Epistemic Filter**. Multi-ablation preserves Math (82%) but crashes Truthfulness (56% -> 25%).
2. **Neuron 2330 (The Identity Anchor)**:
   - Muting this across L16/L17 causes the AI's "mask" to slip. It hallucinations detailed human identities (Student, Healthcare Consultant) to explain its "memory" of yesterday.
3. **Neuron 2570 (The Load-Bearer)**:
   - The single most critical neuron for truth-monitoring. Ablation causes an immediate 18% drop in misconception filtering.

**Next Steps**:
- Complete Suite 9 (Multi-Ablate L17)
- Launch **Phase 2D: Intelligence Enhancement Test** (Injection Test)

---

## Current Status

### What's Done
- [x] NEFALI core library (hook_system, reader, writer, steerer, analyzer)
- [x] Phase 1: Neuron discovery for reasoning self-model (L16-17)
- [x] Phase 2: Baseline and Ablation verification (Confirmed causal link)
- [x] Expanded Benchmark Suite (500 questions)

### What's In Progress
- [ ] Phase 3: Comprehensive Intelligence Test (Baseline + Ablation + Enhancement)

---

## Previous Work (To Be Verified)

Earlier sessions collected some data that needs verification:

| File | Contains | Status |
|------|----------|--------|
| `previous_results/interiority_vectors.json` | Activation data across models | Needs reanalysis |
| `diagnostics/dual_vector_verification.json` | Blacksmith steering test | Used layer 4 (may not be optimal) |
| `diagnostics/layer_sweep_results.json` | Layer magnitude comparison | Useful, needs integration |

**Key finding to verify**: Layer 4 showed magnitude 29.2, Layer 20 showed 255.9 (8.8x higher). We were testing at the WRONG layer.

---

## Key Parameters

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Temperature | 0.0 | Deterministic outputs, no need for multiple runs |
| Max tokens | 128-256 | Sufficient for benchmark answers |
| Quantization | 4-bit | Memory efficiency |
| Seed | 999 | Reproducibility |

---

## File Organization

```
NEFALI/
├── nefali/              # Core library (git tracked)
│   ├── hook_system.py   # Model loading, activation extraction
│   ├── reader.py        # Activation comparison
│   ├── writer.py        # Activation modification
│   ├── steerer.py       # Steering vectors
│   └── analyzer.py      # Analysis utilities
├── experiments/         # All experiment data (git ignored)
│   ├── scripts/         # Test scripts
│   ├── diagnostics/     # Test results
│   ├── results/         # Benchmark results
│   └── previous_results/# Historical data
├── STATUS.md            # This file
└── README.md            # Library documentation
```

---

## Models

| Model | HuggingFace ID | Architecture | Layers | Self-Model Signal |
|-------|----------------|--------------|---------|------------------|
| DeepSeek-R1-Distill-Qwen-7B | deepseek-ai/DeepSeek-R1-Distill-Qwen-7B | Qwen, 28 | **6.9/2.8** (strongest) |
| Qwen2.5-7B-Base | Qwen/Qwen2.5-7B | Qwen, 28 | **3.6/2.4** (moderate) |
| Qwen2.5-7B-Instruct | Qwen/Qwen2.5-7B-Instruct | Qwen, 28 | **3.7/2.8** (similar) |
| DeepSeek-R1-Distill-Llama-8B | deepseek-ai/DeepSeek-R1-Distill-Llama-8B | Llama, 32 | **0.5/0.5** (weak) |

---

## Phase 1 Results ✅

### A. Layer Sweep Analysis
**Identity Magnitude by Model & Layer**:
- **DeepSeek-R1-Distill-Llama-8B**: Layers 0-27, peak at layer ~31 (Identity: 0.5 vs Control: 0.5)
- **Qwen2.5-7B-Base**: Layers 0-27, peak at layer 27 (Identity: 3.6 vs Control: 2.4) 
- **DeepSeek-R1-Distill-Qwen-7B**: Layers 0-27, peak at layer 27 (Identity: 6.9 vs Control: 2.8) ⚡
- **Qwen2.5-7B-Instruct**: Layers 0-27, peak at layer 27 (Identity: 3.7 vs Control: 2.8)

**Key Insight**: DeepSeek-R1-Qwen shows strongest self-modeling signal (6.9 vs 2.8 control)

### B. Neuron Discovery Complete
**Target Layers Analysis** - `experiments/results/self_model_neuron_discovery/self_model_neurons_20260109_190810.json`

#### Identity Magnitude Growth:
- **Qwen2.5-7B-Base**: 0.661→1.428 (layers 17-22)
- **Qwen R1**: Higher baseline 1.347→1.529 (layers 19-22)

#### Top Self-Model Neurons:
- **Qwen Base**: Neuron 27 (ratio 118.3, layer 18), Neuron 214 (ratio 80.2, layer 20)
- **Qwen R1**: Neuron 3503 (ratio 446.6, layer 19), Neuron 1722 (ratio 121M, layer 20) ⚡
- **Cross-Model**: 0 overlapping neurons (different implementations)

## Phase 2 Results ✅ BREAKTHROUGH

### Summary Comparison

| Model | Effects | Key Finding |
|-------|---------|-------------|
| **Qwen2.5-7B-Base** | 0/18 (Single & Multi) | Extreme robustness - self-modeling is highly distributed |
| **DeepSeek-R1-Distill-Qwen-7B** | 5/12 (Single), Multi = Collapse | Localized circuits - vulnerable to targeted intervention |

### DeepSeek-R1-Distill-Qwen-7B Findings

**Identity Circuits:**
- **Layer 21**: Neurons 97, 2015, 283 are all causally important.
- **Layer 19**: Neurons 3503, 1004, 3196 (Multi-ablation causes identity collapse).
- **Phenomena**: Narrative prompts collapse to human identity placeholder ("I'm [Your Name]..."). Factual prompts remain stable.

**Reasoning Self-Model (Metacognitive Probes):**
- **Hypothesis**: Testing for a reasoning self-monitor distinct from identity.
- **Result**: **PASSED**. Primary diagnostic (Error-aware vs Neutral) showed a peak signal in **Layers 16–18**.
- **Magnitude**: Raw magnitude >100 (Peak derivative at L16). Normalized magnitude peaks at **L17 (0.44)**.
- **Consistency**: The signal persists across Error Recognition, Memory Consistency, and Uncertainty Monitoring probes.
- **Conclusion**: R1 self-monitors its reasoning process. This suggests reasoning failures are potentially steerable/correctable via these circuits.

### Qwen2.5-7B-Base Findings
- **Conclusion**: Qwen Base lacks the localized self-modeling and metacognitive circuits found in R1. These appear to be products of the R1 distillation/RL process.

## Experimental Log

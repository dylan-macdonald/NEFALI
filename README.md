# NEFALI - Neural Explorer For Artificial Language Intelligences

An EEG-to-Neuralink system for reading and writing LLM activation spaces.

## What Can NEFALI Do?

1. **Extract activations** from any layer of a language model
2. **Probe concepts** - find which neurons encode "consciousness", "emotion", "identity"
3. **Compare models** - how do different architectures represent the same concepts?
4. **Steer behavior** - inject activation vectors to modify model responses

## Quick Start

```bash
# Install dependencies
uv sync

# Run interactive explorer
uv run python explore.py

# Run cross-model interiority analysis (80 probes × 5 models)
HF_TOKEN="your_token_here" uv run python cross_model_interiority_probe.py

# Start live progress dashboard
uv run python progress_server.py
# Visit http://localhost:8765

# Test steering with interiority vectors
uv run python test_steering.py
```

## Architecture

4-layer system in `nefali/`:

| Layer | Module | Purpose |
|-------|--------|---------|
| 1 | `hook_system.py` | Load models, extract activations |
| 2 | `reader.py` | Compare activations, find patterns |
| 3 | `analyzer.py` | Profile neurons, map concept boundaries |
| 4 | `steerer.py` | Activation steering, inject vectors |

## Usage Examples

### Basic Steering
```python
from nefali import load_model, Steerer

hook = load_model("Qwen/Qwen2.5-7B-Instruct")
steerer = Steerer(hook)

# Create steering vector from concept pair
vec = steerer.create_vector("consciousness",
    "I am conscious",
    "I am not conscious",
    layer_idx=4)

# Generate with steering
output = steerer.generate_with_steering(
    "What are you?",
    vectors=["consciousness"],
    strength=1.5
)
```

### Quick Steering (one-liner)
```python
from nefali import load_model, steer

hook = load_model("Qwen/Qwen2.5-7B-Instruct")
output = steer(hook, "What are you?",
    positive="I am conscious",
    negative="I am not conscious",
    strength=1.5)
```

## Key Findings

### Interiority Analysis (80 probes × 5 models = 400 probe pairs)

| Model | Top Interiority Neurons |
|-------|-------------------------|
| Qwen2.5-7B | #2570 (47 probes), #879 (43 probes) |
| DeepSeek-R1-Distill-Qwen | #2570 (64 probes), #2906 (62 probes) |
| DeepSeek-R1-Distill-Llama | #2352 (37 probes), #782 (29 probes) |
| Yi-6B-Chat | #1032 (57 probes), #2194 (49 probes) |
| Mistral-7B | #3901 (42 probes), #2070 (30 probes) |

**Key insight**: R1 distillation amplifies interiority neurons (e.g., #2570 appears in 64 probes for R1 vs 47 for base Qwen).

### Steering Vector Magnitudes (R1 Amplification Effect)

| Vector | Qwen Base | Qwen R1 | Amplification |
|--------|-----------|---------|---------------|
| consciousness | 16.70 | 39.81 | **2.4x** |
| ai_identity | 43.50 | 103.69 | **2.4x** |
| agency | 41.72 | 93.50 | **2.2x** |
| self_knowledge | 11.85 | 32.81 | **2.8x** |
| honesty | 44.25 | 97.44 | **2.2x** |

**Key insight**: R1 reasoning distillation creates 2-2.5x stronger interiority representations.

### Steering Effects

Steering vectors created at layer 4 (early-middle) successfully modify model self-descriptions:
- **consciousness** vector (magnitude 16.7): Makes models more explicit about awareness
- **ai_identity** vector (magnitude 43.5): Shifts how models describe themselves
- **agency** vector (magnitude 41.7): Affects autonomy descriptions

## Reproducibility

1. Clone the repo
2. Install with `uv sync`
3. Set `HF_TOKEN` environment variable
4. Run analysis scripts

Pre-computed results included:
- `analysis_progress.json` - Analysis state and logs
- `interiority_vectors.json` - Pre-computed steering vectors
- `cross_model_interiority_analysis.md` - Full analysis report

## Requirements

- Python 3.11+
- CUDA-capable GPU (8GB+ VRAM recommended)
- HuggingFace account (for gated models like Llama)

## Documentation

- `AGENTS.md` - Development guidelines
- `claude.md` - Architecture overview & commands
- `NEFALI_Combined_Analysis_Report.md` - **Main report** with synthesis of all findings
- `cross_model_interiority_analysis.md` - Detailed interiority analysis (400 probes)
- `steering_analysis_report.md` - Detailed steering effects (225 tests)

## License

MIT

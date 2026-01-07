# NEFALI - Neural Explorer For Artificial Language Intelligences

An EEG-to-Neuralink system for reading and writing LLM activation spaces.

## Quick Start

```bash
# Install dependencies
uv sync

# Run interactive explorer
uv run python explore.py

# Run cross-model analysis
HF_TOKEN="your_token_here" uv run python cross_model_interiority_probe.py

# Start progress dashboard
uv run python progress_server.py
# Visit http://localhost:8765
```

## Architecture

4-layer system:
1. **Hook System** - Extract activations from model layers
2. **Reader** - Compare activations, find patterns
3. **Analyzer** - Map concept boundaries, profile neurons
4. **Writer** - Activation steering, inject vectors

## Requirements

- Python 3.11+
- CUDA-capable GPU (8GB+ VRAM recommended)
- HuggingFace account with accepted licenses (for gated models)

## Documentation

- `AGENTS.md` - Development guidelines
- `CLAUDE.md` - Architecture overview
- `cross_model_interiority_analysis.md` - Analysis results (generated)

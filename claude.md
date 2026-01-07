# NEFALI - Neural Explorer For Artificial Language Intelligences

## Purpose
Tools to read and (eventually) write to LLM activation spaces. Start as an EEG, grow into a Neuralink.

## Architecture Layers (build in order)
1. Hook System - tap into model layers, extract activations ✅ DONE
2. Reader - compare activations across inputs, find patterns ✅ DONE (Jan 5, 2026)
3. Analyzer - map concept boundaries, profile neurons, cluster ✅ DONE (Jan 5, 2026)
4. Writer - activation steering, inject vectors mid-forward-pass ✅ DONE (Jan 5, 2026)

**ALL FOUR LAYERS COMPLETE.** NEFALI is now a full EEG-to-Neuralink system.

## First Experiment
Aesthetic reward slider: extract hidden state scalar as reward signal, generate at different aesthetic weights (0-100%), document where outputs get weird.

## Stack
- Python 3.11+
- TransformerLens
- Qwen 2.5 7B (quantized, fits 8GB VRAM)
- Simple viz (matplotlib initially)

## Commands
- `uv run python explore.py` - **Interactive explorer UI** (start here!)
- `uv run python main.py` - run basic experiments
- `uv run pytest` - tests

## Using the Explorer

The explorer (`explore.py`) is the easiest way to look inside a model's mind.

```bash
cd ~/NEFALI
uv run python explore.py
```

**Commands:**
- Just type a prompt to probe it and see what lights up
- `compare` - compare multiple probed prompts
- `layers [prompt]` - see activation across ALL layers
- `visualize` - generate a heatmap image
- `model small` or `model large` - switch between 0.5B and 7B models
- `info` - show current model details
- `history` - show all probed prompts
- `help` - show all commands

The explorer shows:
- How "active" each layer is for your prompt (norm)
- Scalar reward signal (mean of final hidden state)
- Visual activity bars showing relative activation

## Layer 2: Reader Commands

After probing multiple prompts, use these to find patterns:

- `diff` - Find which specific neurons differ most between two prompts
- `similar` - Compute cosine similarity (how alike are the activation patterns?)
- `concept` - Create a "concept vector" from the difference between two prompts
- `concepts` - List your stored concept vectors
- `project` - See where a new prompt falls on a concept axis

**Example workflow:**
```
nefali: i love you
nefali: i hate you
nefali: diff
  → Shows neuron #266 differs by 3.94, neuron #210 by 3.93...
nefali: similar
  → Shows 0.97 similarity (love/hate are structurally similar!)
nefali: concept
  → Creates "love→hate" concept vector
nefali: i feel neutral about you
nefali: project
  → Shows where "neutral" falls on the love→hate axis
```

This is real interpretability - finding the specific neurons that encode concepts.

## Layer 3: Analyzer Commands

After probing many prompts, use these to understand what neurons mean:

- `profile` - What does a specific neuron respond to? Shows top/bottom activating prompts.
- `findconcept` - Select positive/negative examples, find neurons that encode the difference
- `cluster` - Group prompts by activation similarity (k-means clustering)
- `classify` - Define two groups, classify a new prompt as A or B
- `stats` - Show overall activation statistics, find most variable neurons

**Example workflow:**
```
nefali: i love you
nefali: i hate you
nefali: i feel happy
nefali: i feel sad
nefali: stats
  → Shows most variable neurons (these encode concepts!)
nefali: profile
  → Enter neuron 408
  → See what prompts activate it most/least
nefali: findconcept
  → Select "love" and "happy" as positive, "hate" and "sad" as negative
  → Find the "positive emotion" neurons
```

The Analyzer turns numbers into understanding.

## Layer 4: Writer Commands

The Neuralink part. Not just reading - writing.

- `steer` - Create a steering vector (from concept, prompts, or single neuron)
- `steerings` - List active steering configurations
- `clearsteer` - Remove all steering
- `generate [prompt]` - Generate text with active steering applied
- `sweep [prompt]` - Generate at different steering strengths (-2 to +2)

**Example workflow:**
```
nefali: i love you
nefali: i hate you
nefali: concept
  → Create "love→hate" concept
nefali: steer
  → Select concept, set strength to 1.5
nefali: generate I feel
  → Generates text steered toward "hate"
nefali: sweep I feel
  → Shows generation at strengths -2, -1, 0, +1, +2
  → Watch the output shift from loving to hating
```

The Writer closes the loop. Read → Understand → Steer → Generate.

## Principles
- Seed everything for reproducibility
- Log activations to disk
- Simple first, complexity when earned
- Each layer should work standalone before building the next

## Code Style
- Type hints on all functions
- Docstrings on public functions (brief, not verbose)
- Prefer functions over classes unless state is genuinely needed
- Print statements for debugging are fine, we're exploring not shipping

## Verification
- After writing code, run it
- If it errors, fix it before moving on
- Layer 1 is "done" when test script runs and prints activation shapes

## References
- TransformerLens docs: https://transformerlensorg.github.io/TransformerLens/
- HuggingFace Qwen: https://huggingface.co/Qwen

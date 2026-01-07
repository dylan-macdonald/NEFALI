# AGENTS.md - Guidelines for Coding Agents

Guidelines for AI coding agents working on NEFALI codebase.

## Project Overview

NEFALI reads/writes LLM activation spaces using 4-layer architecture:

1. **Hook System** (`nefali/hook_system.py`) - Extract activations
2. **Reader** (`nefali/reader.py`) - Compare activations, find patterns
3. **Analyzer** (`nefali/analyzer.py`) - Map concept boundaries, profile neurons
4. **Writer** (`nefali/writer.py`) - Activation steering, text generation

**All layers complete.** System is functional and ready for extension.

## Development Commands

```bash
# Tests
uv run pytest                                    # Run all tests
uv run pytest tests/test_hook_system.py         # Run specific file
uv run pytest tests/test_hook_system.py::test    # Run single test
uv run pytest -v                                 # Verbose output

# Code
uv run python explore.py     # Interactive explorer (primary UI)
uv run python main.py        # Run basic experiments
uv run python test_layer1.py # Run verification script

# Package
uv sync                    # Install dependencies
uv add package-name        # Add dependency
uv lock --upgrade          # Update dependencies
```

**Note:** No linters configured. Follow existing patterns, use type hints, add brief docstrings, keep code simple.

## Code Style Guidelines

### Python Version
- Python 3.11+ required

### Imports
Order: standard library → third-party → local. Use absolute imports.

```python
import gc, random
from typing import Dict, List, Optional, Tuple
import numpy as np, torch
from transformers import AutoTokenizer
from rich.console import Console
from nefali.hook_system import ModelHook
```

### Type Hints
**Mandatory on all functions.**

```python
def extract_activations(hook: ModelHook, prompt: str,
                        layer_indices: Optional[List[int]] = None) -> Dict[str, torch.Tensor]:
    """Extract activations from a model."""
```

### Naming Conventions
- Classes: `PascalCase` (`ModelHook`, `Reader`)
- Functions: `snake_case` (`extract_activations`)
- Variables: `snake_case` (`hidden_states`, `layer_idx`)
- Constants: `UPPER_SNAKE_CASE` (`DEFAULT_SEED = 42`)
- Private: `_underscore_prefix` (`_create_hook`)

### Error Handling
Use descriptive error messages. Raise `ValueError` for invalid inputs, `RuntimeError` for invalid state.

```python
if self.nnsight_model is None:
    raise RuntimeError("Model not loaded. Call load_model() first.")
if prompt not in self.stored_activations:
    raise ValueError(f"Prompt not stored: {prompt}")
```

### Classes vs Functions
- Prefer functions unless state is genuinely needed
- Use `@dataclass` for data structures
- Use `@contextmanager` for resource management

**Stateful (needed):**
```python
class Reader:
    def __init__(self):
        self.stored_activations: Dict[str, Dict[str, np.ndarray]] = {}
```

**Stateless (preferred):**
```python
def load_model(model_name: str, quantize: bool = True) -> ModelHook:
    hook = ModelHook(model_name=model_name, quantize=quantize)
    hook.load_model()
    return hook
```

### Data Structures
Use `@dataclass`:

```python
@dataclass
class NeuronDiff:
    """A neuron that differs between two prompts."""
    layer: int
    neuron_idx: int
    activation_a: float
    activation_b: float
    difference: float

    @property
    def abs_diff(self) -> float:
        return abs(self.difference)
```

### Reproducibility
**Always seed random operations.**

```python
import torch, random, numpy as np
seed = 42
random.seed(seed); np.random.seed(seed); torch.manual_seed(seed)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)
```

### Memory Management
Always clean up GPU memory:

```python
def cleanup(self) -> None:
    if self.model is not None:
        del self.model; self.model = None
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
```

### Testing Philosophy
- **Write code, run it, fix errors** before moving on
- Layer is "done" when verification script runs successfully
- Test scripts in root (e.g., `test_layer1.py`)
- Unit tests in `tests/` directory

## Architecture Principles

1. **Layer Independence**: Each layer standalone before building next
2. **Simple First**: Start simple, add complexity when earned
3. **Explicit APIs**: Clear interfaces between layers
4. **Seed Everything**: Reproducibility is critical
5. **Log Activations**: Store for comparison

## File Organization

```
nefali/
├── __init__.py
├── hook_system.py    # Layer 1
├── reader.py        # Layer 2
├── analyzer.py      # Layer 3
└── writer.py        # Layer 4

tests/               # Unit tests
explore.py          # Interactive CLI (main UI)
test_*.py           # Verification scripts
main.py             # Basic experiments
```

## Common Patterns

### Working with Activations
Shape: `[batch, seq_len, hidden_dim]`. Extract final token:
```python
hidden_states = activations[f"layer_{layer_idx}"]
final_token = hidden_states[0, -1, :]  # [hidden_dim]
```

### Layer Indexing
Support negative indexing:
```python
if layer_idx < 0:
    layer_idx = len(model.model.layers) + layer_idx
```

### Concept Vectors
Difference between activation patterns:
```python
concept_vector = activations_b - activations_a
```

### Steering Injection
Inject vectors during forward pass:
```python
def hook_fn(module, input, output):
    hidden_states = output[0] if isinstance(output, tuple) else output
    hidden_states = hidden_states + steering_vector
    return output if not isinstance(output, tuple) else (hidden_states,) + output[1:]
```

## When to Ask for Help

- Unsure about structuring a new feature across  4 layers
- Adding a new dependency
- Specific edge cases in activation extraction
- Memory optimization for large models

## References

- TransformerLens: https://transformerlensorg.github.io/TransformerLens/
- nnsight: https://nnsight.net/
- HuggingFace Qwen: https://huggingface.co/Qwen
- Architecture: See CLAUDE.md

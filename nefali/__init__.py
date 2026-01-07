"""NEFALI - Neural Explorer For Artificial Language Intelligences.

A toolkit for exploring, analyzing, and steering language model internals.

Layers:
    1. Hook System - Load models, extract activations
    2. Reader - Compare activations, probe concepts
    3. Analyzer - Profile neurons, find concept clusters
    4. Steerer - Activation steering / representation engineering
"""

__version__ = "0.2.0"

from .hook_system import ModelHook, load_model, extract_activations
from .reader import Reader
from .analyzer import Analyzer, NeuronProfile, ConceptNeurons
from .steerer import Steerer, SteeringVector, steer

__all__ = [
    # Hook System (Layer 1)
    'ModelHook',
    'load_model',
    'extract_activations',
    # Reader (Layer 2)
    'Reader',
    # Analyzer (Layer 3)
    'Analyzer',
    'NeuronProfile',
    'ConceptNeurons',
    # Steerer (Layer 4)
    'Steerer',
    'SteeringVector',
    'steer',
]
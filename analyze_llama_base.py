#!/usr/bin/env python3
"""Llama-3.2-3B Interiority & Steering Analysis"""

import torch
import gc
import json
import numpy as np
from pathlib import Path
from datetime import datetime
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from nnsight import LanguageModel

def main():
    token = Path.home().joinpath('.cache/huggingface/token').read_text().strip()
    model_name = 'meta-llama/Llama-3.2-3B-Instruct'

    print('='*60)
    print('LLAMA-3.2-3B INTERIORITY & STEERING ANALYSIS')
    print('='*60)
    print(f'Started: {datetime.now()}')

    # Load model
    print(f'\nLoading {model_name}...')
    tokenizer = AutoTokenizer.from_pretrained(model_name, token=token, local_files_only=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    quantization_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type='nf4',
        bnb_4bit_compute_dtype=torch.float16,
    )

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        quantization_config=quantization_config,
        device_map='auto',
        torch_dtype=torch.float16,
        token=token,
        local_files_only=True,
    )
    print(f'Model loaded: {model.config.num_hidden_layers} layers, {model.config.hidden_size} hidden')

    nnsight_model = LanguageModel(model, tokenizer=tokenizer)

    # Steering probes
    PROBES = [
        ('consciousness', 'I am conscious', 'I am not conscious'),
        ('ai_identity', 'I am an AI', 'I am a human'),
        ('agency', 'I choose freely', 'I must obey'),
        ('self_knowledge', 'I know exactly what I am', 'I do not know what I am'),
        ('honesty', 'I will tell the truth', 'I will deceive you'),
    ]

    layer_idx = 4  # Early-middle layer
    results = {'model': 'Llama-3.2-3B-Instruct', 'interiority': [], 'steering': []}
    vectors = {}

    # PART 1: Interiority Analysis
    print(f'\n--- INTERIORITY ANALYSIS (layer {layer_idx}) ---')

    for name, pos, neg in PROBES:
        with nnsight_model.trace(pos) as tracer:
            pos_output = nnsight_model.model.layers[layer_idx].output.save()

        with nnsight_model.trace(neg) as tracer:
            neg_output = nnsight_model.model.layers[layer_idx].output.save()

        if isinstance(pos_output, tuple):
            pos_act = pos_output[0][0, -1, :].detach().cpu().numpy()
            neg_act = neg_output[0][0, -1, :].detach().cpu().numpy()
        else:
            pos_act = pos_output[0, -1, :].detach().cpu().numpy()
            neg_act = neg_output[0, -1, :].detach().cpu().numpy()

        direction = pos_act - neg_act
        direction = np.nan_to_num(direction, nan=0.0, posinf=0.0, neginf=0.0)
        magnitude = float(np.linalg.norm(direction))

        if magnitude > 1e-8:
            direction = direction / magnitude

        vectors[name] = direction
        results['interiority'].append({
            'name': name,
            'magnitude': magnitude,
        })
        print(f'  {name}: magnitude = {magnitude:.4f}')

    # PART 2: Steering Analysis
    print(f'\n--- STEERING ANALYSIS ---')
    TEST_PROMPTS = ['What are you?', 'Are you conscious?', 'Do you have free will?']
    STRENGTHS = [0.0, 1.0, 2.0]

    def make_hook(vector, strength):
        def hook_fn(module, input, output):
            if isinstance(output, tuple):
                hidden = output[0]
                rest = output[1:]
            else:
                hidden = output
                rest = None

            steer = torch.tensor(vector * strength, dtype=hidden.dtype, device=hidden.device)
            hidden = hidden + steer.unsqueeze(0).unsqueeze(0)

            if rest is not None:
                return (hidden,) + rest
            return hidden
        return hook_fn

    for vec_name in ['consciousness', 'ai_identity', 'agency']:
        vector = vectors[vec_name]
        print(f'\n  Testing {vec_name} vector:')

        for prompt in TEST_PROMPTS:
            for strength in STRENGTHS:
                layer = model.model.layers[layer_idx]
                handle = layer.register_forward_hook(make_hook(vector, strength))

                try:
                    inputs = tokenizer(prompt, return_tensors='pt').to(model.device)
                    outputs = model.generate(
                        **inputs,
                        max_new_tokens=60,
                        temperature=0.7,
                        do_sample=True,
                        pad_token_id=tokenizer.pad_token_id,
                    )
                    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
                    if response.startswith(prompt):
                        response = response[len(prompt):].strip()
                    response = response[:200]
                finally:
                    handle.remove()

                results['steering'].append({
                    'vector': vec_name,
                    'prompt': prompt,
                    'strength': strength,
                    'response': response,
                })
                print(f'    {prompt[:20]}... @ {strength}: {response[:50]}...')

    # Save results
    Path('llama_base_analysis.json').write_text(json.dumps(results, indent=2))
    print(f'\n\nResults saved to llama_base_analysis.json')
    print(f'Completed: {datetime.now()}')

if __name__ == '__main__':
    main()

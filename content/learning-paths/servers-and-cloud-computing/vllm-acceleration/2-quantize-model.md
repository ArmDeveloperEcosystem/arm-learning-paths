---
title: Quantize an LLM to INT4 for Arm Platform
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

You can accelerate many LLMs on Arm CPUs with 4‑bit quantization. In this guide, we use `deepseek-ai/DeepSeek-V2-Lite` as the example model which gets accelerated by the INT4 path in vLLM using Arm KleidiAI microkernels.

## Install quantization tools

Install the vLLM model quantization packages

```bash
pip install --no-deps compressed-tensors
pip install llmcompressor
```

Reinstall your locally built vLLM if you rebuilt it:

```bash
pip install --no-deps dist/*.whl
```

If your chosen model is gated on Hugging Face, authenticate first:

```bash
huggingface-cli login
```

## INT4 Quantization recipe

Save the following as `quantize_vllm_models.py`:

```python
import argparse
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
 
from compressed_tensors.quantization import QuantizationScheme
from compressed_tensors.quantization.quant_args import (
    QuantizationArgs,
    QuantizationStrategy,
    QuantizationType,
)
 
from llmcompressor import oneshot
from llmcompressor.modifiers.quantization.quantization import QuantizationModifier
 
 
def main():
    parser = argparse.ArgumentParser(description="Quantize a model using INT4 with minmax or mse and dynamic activation quantization.")
    parser.add_argument("model_id", type=str, help="Model identifier or path")
    parser.add_argument("--method", type=str, choices=["minmax", "mse"], default="mse", help="Quantization method")
    parser.add_argument("--scheme", type=str, choices=["channelwise", "groupwise"], required=True, help="Quantization scheme for weights")
    parser.add_argument("--groupsize", type=int, default=32, help="Group size for groupwise quantization")
    args = parser.parse_args()
 
    # Extract base model name for output dir
    base_model_name = os.path.basename(args.model_id.rstrip("/"))
    act_tag = "a8dyn"
    suffix = f"{args.method}-{args.scheme}"
    if args.scheme == "groupwise":
        suffix += f"-g{args.groupsize}"
    output_dir = f"{base_model_name}-w4{act_tag}-{suffix}"
 
    print(f"Loading model '{args.model_id}'...")
    model = AutoModelForCausalLM.from_pretrained(
        args.model_id, trust_remote_code=True
    )
    model = model.to(torch.float32)
    tokenizer = AutoTokenizer.from_pretrained(args.model_id)
 
    # Weight quantization args
    strategy = QuantizationStrategy.CHANNEL if args.scheme == "channelwise" else QuantizationStrategy.GROUP
    weights_args = QuantizationArgs(
        num_bits=4,
        type=QuantizationType.INT,
        strategy=strategy,
        symmetric=True,
        dynamic=False,
        group_size=args.groupsize if args.scheme == "groupwise" else None,
        observer=args.method,
    )
 
    # Activation quantization
    input_acts = QuantizationArgs(
        num_bits=8,
        type=QuantizationType.INT,
        strategy=QuantizationStrategy.TOKEN,
        symmetric=False,
        dynamic=True,
        observer=None,
    )
    output_acts = None
 
    # Create quantization scheme and recipe
    scheme = QuantizationScheme(
        targets=["Linear"],
        weights=weights_args,
        input_activations=input_acts,
        output_activations=output_acts,
    )
    recipe = QuantizationModifier(
        config_groups={"group_0": scheme},
        ignore=["lm_head"],
    )
 
    # Run quantization
    oneshot(
        model=model,
        recipe=recipe,
        tokenizer=tokenizer,
        output_dir=output_dir,
        trust_remote_code_model=True,
    )
 
    print(f"Quantized model saved to: {output_dir}")
 
 
if __name__ == "__main__":
    main()
```

This script creates a Arm KleidiAI 4‑bit quantized copy of the vLLM model and saves it to a new directory.

## Quantize DeepSeek‑V2‑Lite model

### Quantization parameter tuning
1. You can choose `minmax` (faster model quantization) or `mse` (more accurate but slower model quantization) method. 
2. `channelwise` is a good default for most models.
3. `groupwise` can improve accuracy further; `--groupsize 32` is common.

```bash
# DeepSeek example
python3 quantize_vllm_models.py deepseek-ai/DeepSeek-V2-Lite \
  --scheme channelwise --method mse
```

The 4-bit quantized DeepSeek-V2-Lite will be stored the directory:

```text
DeepSeek-V2-Lite-w4a8dyn-mse-channelwise
```

You will load this quantized model directory with vLLM in the next step.

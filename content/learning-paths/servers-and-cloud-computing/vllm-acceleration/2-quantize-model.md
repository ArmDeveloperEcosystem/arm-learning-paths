---
title: Quantize an LLM to INT4 for Arm Platform
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Accelerating LLMs with 4-bit Quantization

You can accelerate many LLMs on Arm CPUs with 4‑bit quantization. In this section, you’ll quantize the deepseek-ai/DeepSeek-V2-Lite model to 4-bit integer (INT4) weights.
The quantized model runs efficiently through vLLM’s INT4 inference path, which is accelerated by Arm KleidiAI microkernels.

## Install quantization tools

Install the quantization dependencies used by vLLM and the llmcompressor toolkit:

```bash
pip install --no-deps compressed-tensors
pip install llmcompressor
```
  * compressed-tensors provides the underlying tensor storage and compression utilities used for quantized model formats.
  * llmcompressor includes quantization, pruning, and weight clustering utilities compatible with Hugging Face Transformers and vLLM runtime formats.
    
If you recently rebuilt vLLM, reinstall your locally built wheel to ensure compatibility with the quantization extensions:

```bash
pip install --no-deps dist/*.whl
```

Authenticate with Hugging Face (if required):

If the model you plan to quantize is gated on Hugging Face (e.g., DeepSeek or proprietary models), log in to authenticate your credentials before downloading model weights:

```bash
huggingface-cli login
```

## INT4 Quantization Recipe

Using a file editor of your choice, save the following code into a file named `quantize_vllm_models.py`:

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

This script creates a Arm KleidiAI INT4 quantized copy of the vLLM model and saves it to a new directory.

## Quantize DeepSeek‑V2‑Lite model

### Quantization parameter tuning
Quantization parameters determine how the model’s floating-point weights and activations are converted into lower-precision integer formats. Choosing the right combination is essential for balancing model accuracy, memory footprint, and runtime throughput on Arm CPUs.

1. You can choose `minmax` (faster model quantization) or `mse` (more accurate but slower model quantization) method. 
2. `channelwise` is a good default for most models.
3. `groupwise` can improve accuracy further; `--groupsize 32` is common.

Execute the following command to quantize the DeepSeek-V2-Lite model:

```bash
# DeepSeek example
python3 quantize_vllm_models.py deepseek-ai/DeepSeek-V2-Lite \
  --scheme channelwise --method mse
```

This will generate an INT4 quantized model directory such as:

```text
DeepSeek-V2-Lite-w4a8dyn-mse-channelwise
```

You will load this quantized model directory with vLLM in the next step.

---
title: Quantize and Launch the vLLM server
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Access the Model from Hugging Face

Before quantizing, authenticate with Hugging Face using a personal access token. You can generate one from your [Hugging Face Hub](https://huggingface.co/) account under Access Tokens:

```bash
huggingface-cli login --token $hf_token
```
## Quantization Script Template

Using a file editor of your choice, create a file named `vllm_quantize_model.py` and copy the content shown below to quantize the model:
```bash
import argparse
import os
from transformers import AutoModelForCausalLM, AutoTokenizer

from llmcompressor.modifiers.quantization import QuantizationModifier
from compressed_tensors.quantization import QuantizationScheme
from compressed_tensors.quantization.quant_args import (
    QuantizationArgs,
    QuantizationStrategy,
    QuantizationType,
)
from llmcompressor.transformers import oneshot


def main():
    parser = argparse.ArgumentParser(
        description="Quantize a model using LLM Compressor with customizable mode, scheme, and group size."
    )
    parser.add_argument(
        "model_id",
        type=str,
        help="Model identifier or path (e.g., 'meta-llama/Llama-2-13b-chat-hf' or '/path/to/model')",
    )
    parser.add_argument(
        "--mode",
        type=str,
        choices=["int4", "int8"],
        required=True,
        help="Quantization mode: int4 or int8",
    )
    parser.add_argument(
        "--scheme",
        type=str,
        choices=["channelwise", "groupwise"],
        required=True,
        help="Quantization scheme for weights (groupwise is only supported for int4)",
    )
    parser.add_argument(
        "--groupsize",
        type=int,
        default=32,
        help="Group size for groupwise quantization (only used when scheme is groupwise). Defaults to 32."
    )
    args = parser.parse_args()

    # Validate unsupported configuration
    if args.mode == "int8" and args.scheme == "groupwise":
        raise ValueError("Groupwise int8 is unsupported. Please use channelwise for int8.")

    # Extract a base model name from the model id or path for the output directory
    if "/" in args.model_id:
        base_model_name = args.model_id.split("/")[-1]
    else:
        base_model_name = os.path.basename(args.model_id)

    # Determine output directory based on mode and scheme
    if args.mode == "int4":
        output_dir = f"{base_model_name}-w4a8-{args.scheme}"
    else:  # int8
        output_dir = f"{base_model_name}-w8a8-{args.scheme}"

    print(f"Loading model '{args.model_id}'...")
    model = AutoModelForCausalLM.from_pretrained(
        args.model_id, device_map="auto", torch_dtype="auto", trust_remote_code=True
    )
    tokenizer = AutoTokenizer.from_pretrained(args.model_id)

    # Define quantization arguments based on mode and chosen scheme.
    if args.mode == "int8":
        # Only channelwise is supported for int8.
        weights_args = QuantizationArgs(
            num_bits=8,
            type=QuantizationType.INT,
            strategy=QuantizationStrategy.CHANNEL,
            symmetric=True,
            dynamic=False,
        )
    else:  # int4 mode
        if args.scheme == "channelwise":
            strategy = QuantizationStrategy.CHANNEL
            weights_args = QuantizationArgs(
                num_bits=4,
                type=QuantizationType.INT,
                strategy=strategy,
                symmetric=True,
                dynamic=False,
            )
        else:  # groupwise
            strategy = QuantizationStrategy.GROUP
            weights_args = QuantizationArgs(
                num_bits=4,
                type=QuantizationType.INT,
                strategy=strategy,
                group_size=args.groupsize,
                symmetric=True,
                dynamic=False
            )

    # Activation quantization remains the same for both modes.
    activations_args = QuantizationArgs(
        num_bits=8,
        type=QuantizationType.INT,
        strategy=QuantizationStrategy.TOKEN,
        symmetric=False,
        dynamic=True,
        observer=None,
    )

    # Create a quantization scheme for Linear layers.
    scheme = QuantizationScheme(
        targets=["Linear"],
        weights=weights_args,
        input_activations=activations_args,
    )

    # Create a quantization modifier. We ignore the "lm_head" layer.
    modifier = QuantizationModifier(config_groups={"group_0": scheme}, ignore=["lm_head"])

    # Apply quantization and save the quantized model.
    oneshot(
        model=model,
        recipe=modifier,
        tokenizer=tokenizer,
        output_dir=output_dir,
    )
    print(f"Quantized model saved to: {output_dir}")


if __name__ == "__main__":
    main()


```
Then run the quantization script using `vllm_quantize_model.py`. This generates an INT8 quantized version of the model using channelwise precision, which reduces memory usage while maintaining model accuracy:

```bash 
python vllm_quantize_model.py meta-llama/Llama-3.1-8B-Instruct --mode int8 --scheme channelwise
```
The quantized model will be saved at:
`$HOME/Llama-3.1-8B-Instruct-w8a8-channelwise`.

## Launch the vLLM server

The vLLM server supports the OpenAI-compatible `/v1/chat/completions` API. This is used in this learning path for single-prompt testing with `curl` and for batch testing using a custom Python script that simulates multiple concurrent requests.

Once the model is quantized, launch the vLLM server to enable CPU-based inference. This configuration uses `tcmalloc` and the optimized `OpenBLAS` build to improve performance and reduce latency:

```bash
LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libtcmalloc_minimal.so.4:/home/ubuntu/OpenBLAS/libopenblas.so \
ONEDNN_DEFAULT_FPMATH_MODE=BF16 \
VLLM_TARGET_DEVICE=cpu \
VLLM_CPU_KVCACHE_SPACE=32 \
VLLM_CPU_OMP_THREADS_BIND="0-$(($(nproc) - 1))" \
vllm serve $HOME/Llama-3.1-8B-Instruct-w8a8-channelwise \
--dtype float32 --swap-space 16
```
This command starts the vLLM server using the quantized model. It preloads `tcmalloc` for efficient memory allocation and uses OpenBLAS for accelerated matrix operations. Thread binding is dynamically set based on the number of available cores to maximize parallelism on Arm CPUs.

The output from launching the vLLM server with the quantized model should look like:

```output
INFO 04-23 21:13:59 launcher.py:31] Route: /rerank, Methods: POST
INFO 04-23 21:13:59 launcher.py:31] Route: /v1/rerank, Methods: POST
INFO 04-23 21:13:59 launcher.py:31] Route: /v2/rerank, Methods: POST
INFO 04-23 21:13:59 launcher.py:31] Route: /invocations, Methods: POST
INFO:     Started server process [77356]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```


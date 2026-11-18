---
title: Understand MoE models and precision choices
description: Review BF16 and INT8/W8A8 mixture of experts models and the precision choices used in the vLLM benchmark comparisons.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Compare model precision choices

Before serving the models, review the BF16 and INT8/W8A8 checkpoints used in the benchmark comparisons:

- BF16 (16-bit floating-point) 
- INT8/W8A8 (8-bit weights and activations) 

### BF16 MoE

BF16 (bfloat16) is a 16-bit floating-point format. It's the baseline precision for the unquantized mixture of experts (MoE) checkpoints that you'll use.

You'll use the following models to benchmark BF16:

- `google/gemma-4-26B-A4B-it`
- `unsloth/gpt-oss-20b-BF16`

These models are used to show the before and after impact of the BF16 MoE optimization in vLLM.

### INT8/W8A8 MoE

INT8/W8A8 uses 8-bit weights and 8-bit activations. Storing weights in INT8 instead of BF16 can reduce memory bandwidth pressure during inference. The optimized Arm INT8 path uses the I8MM instructions checked during setup. W8A8 describes the quantized operations. It doesn't mean that every operation or the key-value (KV) cache uses INT8.

The INT8/W8A8 section uses the pre-quantized Qwen3 MoE model `RedHatAI/Qwen3-30B-A3B-Thinking-2507-quantized.w8a8`.

For comparison, the BF16 Qwen3 model is `Qwen/Qwen3-30B-A3B-Thinking-2507`.

There's no pre-optimization INT8/W8A8 baseline because INT8 MoE support wasn't available in the pre-optimization path.

The Qwen comparison uses the following performance values:

- Pre-optimization Qwen BF16 performance as the baseline
- New optimized Qwen BF16 performance to show the BF16 MoE optimization gain
- New Qwen INT8/W8A8 performance to show the further improvement from INT8 MoE support

## Why use a pre-quantized model

This Learning Path doesn't cover quantizing a model from scratch. Instead, you'll use a pre-quantized W8A8 model from Hugging Face. Using a pre-quantized model allows you to focus on running and benchmarking INT8/W8A8 MoE inference with vLLM.

For model quantization workflows, see the [vLLM quantization Learning Path](/learning-paths/servers-and-cloud-computing/vllm-benchmark-quantisation/).

## Why compare both BF16 and INT8/W8A8

The reported benchmarks compare two optimization effects:

### BF16 MoE optimization

The BF16 comparison shows the impact of enabling a faster BF16 MoE path on AArch64. Before this optimization, AArch64 BF16 MoE execution didn't use the CPU FusedMoE kernel. 

The expert work therefore followed a more general CPU path:

```text
Before:
    route tokens to experts
    for each selected expert:
        run w13 BF16 expert GEMM
        apply activation
        run w2 BF16 expert GEMM
    combine expert outputs
```

This is correct, but it's not ideal for serving because MoE routing creates many expert-specific GEMMs. Running those through a general path adds overhead around the main matrix-multiply work.

The optimized path adds an Arm-specific CPU FusedMoE path. It packs the routed token data and uses Arm BFloat16 matrix multiply-accumulate (BFMMLA) instructions to speed up the `w13` and `w2` BF16 expert GEMMs:

```text
After:
    route tokens to experts
    pack routed token data for the fused MoE kernel
    run fused MoE on AArch64:
        run w13 BF16 expert GEMM with BFMMLA
        apply activation
        run w2 BF16 expert GEMM with BFMMLA
    combine expert outputs
```

This improves performance because the expert data is arranged for the fused kernel. The main BF16 matrix-multiply work uses the faster Arm BF16 instruction path.

### INT8/W8A8 MoE optimization

The INT8/W8A8 comparison shows the additional benefit of lower-precision MoE execution. W8A8 reduces memory bandwidth pressure by using 8-bit weights and activations. On Arm CPUs with I8MM support, W8A8 can also use the Arm signed INT8 matrix multiply-accumulate (SMMLA) instruction. SMMLA performs twice as many multiply-accumulate operations per instruction as BFMMLA for BF16. This doesn't imply a twofold end-to-end serving speedup.

Use your vLLM 0.31.0 installation to benchmark BF16 and W8A8 on your server. You won't recreate the historical pre-optimization baseline. To reproduce the before-and-after speedups, you need the original baseline build and configuration, which aren't provided in the Learning Path.

## What you've learned and what's next

You've now reviewed the MoE models and precision choices used in this Learning Path.

Next, you'll serve each model with vLLM and send a test request through the OpenAI-compatible API.

---
title: Understand MoE models and precision choices
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## BF16 MoE

BF16 (bfloat16) is a 16-bit floating-point format. It is the baseline precision for the unquantized MoE checkpoints used here.

The BF16 section uses:

- `google/gemma-4-26B-A4B-it`
- `unsloth/gpt-oss-20b-BF16`

These models are used to show the before and after impact of the BF16 MoE optimization in vLLM.

## INT8/W8A8 MoE

INT8/W8A8 uses 8-bit weights and 8-bit activations. Storing weights in INT8 instead of BF16 can reduce memory bandwidth pressure during inference. The optimized Arm INT8 path uses the I8MM instructions checked during setup. W8A8 describes the quantized operations; it does not mean every operation or the KV cache uses INT8.

The INT8/W8A8 section uses a pre-quantized Qwen3 MoE model:

```text
RedHatAI/Qwen3-30B-A3B-Thinking-2507-quantized.w8a8
```

For comparison, the BF16 Qwen3 model is:

```text
Qwen/Qwen3-30B-A3B-Thinking-2507
```

There is no pre-optimization INT8/W8A8 baseline because INT8 MoE support was not available in the pre-optimization path.

The Qwen comparison uses:

- Pre-optimization Qwen BF16 performance as the baseline.
- New optimized Qwen BF16 performance to show the BF16 MoE optimization gain.
- New Qwen INT8/W8A8 performance to show the further improvement from INT8 MoE support.

## Why use a pre-quantized model?

This Learning Path does not cover quantizing a model from scratch. Instead, it uses a pre-quantized W8A8 model from Hugging Face so you can focus on running and benchmarking INT8/W8A8 MoE inference with vLLM.

For model quantization workflows, see the [vLLM quantization Learning Path](/learning-paths/servers-and-cloud-computing/vllm-benchmark-quantisation/).

## Why compare both BF16 and INT8/W8A8?

The reported benchmarks compare two optimization effects:

### BF16 MoE optimization

The BF16 comparison shows the impact of enabling a faster BF16 MoE path on AArch64. Before this optimization, AArch64 BF16 MoE execution did not use the CPU FusedMoE kernel, so the expert work followed a more general CPU path:

```text
Before:
    route tokens to experts
    for each selected expert:
        run w13 BF16 expert GEMM
        apply activation
        run w2 BF16 expert GEMM
    combine expert outputs
```

This is correct, but it is not ideal for serving because MoE routing creates many expert-specific GEMMs. Running those through a general path adds overhead around the main matrix-multiply work.

The optimized path adds an Arm-specific CPU FusedMoE path. It packs the routed token data and uses Arm BFMMLA instructions to speed up the `w13` and `w2` BF16 expert GEMMs:

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

This improves performance because the expert data is arranged for the fused kernel and the main BF16 matrix-multiply work uses Arm's faster BF16 instruction path.

- The INT8/W8A8 comparison shows the additional benefit of lower-precision MoE execution. W8A8 reduces memory bandwidth pressure by using 8-bit weights and activations. On Arm CPUs with I8MM support, W8A8 can also use SMMLA, Arm's signed INT8 matrix multiply-accumulate instruction, which performs twice as many multiply-accumulate operations per instruction as BFMMLA for BF16. This does not imply a twofold end-to-end serving speedup.

The setup installs vLLM 0.31.0 so you can benchmark the current release and compare BF16 with W8A8 on your server. It does not recreate the historical pre-optimization baseline. Reproducing the author's before-and-after speedups requires the original baseline build and configuration, which are not provided here.

## What you've learned and what's next

You've now reviewed the MoE models and precision choices used in this Learning Path.

Next, you'll serve each model with vLLM and send a test request through the OpenAI-compatible API.

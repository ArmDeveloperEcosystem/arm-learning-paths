---
title: Understand MoE models and precision choices
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## BF16 MoE

BF16 is the baseline precision used for the regular MoE models in this Learning Path.

The BF16 section uses:

- `google/gemma-4-26B-A4B-it`
- `unsloth/gpt-oss-20b-BF16`

These models are used to show the before and after impact of the BF16 MoE optimization in vLLM.

## INT8/W8A8 MoE

INT8/W8A8 uses 8-bit weights and 8-bit activations. Storing weights in INT8 instead of BF16 can reduce memory bandwidth pressure during inference. On Arm CPUs with I8MM support, W8A8 can also use SMMLA, Arm's signed INT8 matrix multiply-accumulate instruction, providing twice the theoretical matrix-multiply throughput of BF16.

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

For model quantization workflows, refer to the existing [vLLM quantization Learning Path](/learning-paths/servers-and-cloud-computing/vllm-benchmark-quantisation/).

## Why compare both BF16 and INT8/W8A8?

The benchmark results show two improvements:

- BF16 MoE optimization improves regular MoE model serving performance.
- INT8/W8A8 MoE support provides another optimized serving option with additional performance improvement over BF16.

## What you've accomplished and what's next

You've now reviewed the MoE models and precision choices used in this Learning Path.

Next, you'll serve each model with vLLM and send a test request through the OpenAI-compatible API.
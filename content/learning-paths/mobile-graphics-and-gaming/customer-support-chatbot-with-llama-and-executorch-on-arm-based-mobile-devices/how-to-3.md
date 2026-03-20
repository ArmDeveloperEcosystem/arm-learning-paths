---
title: Understand Llama models
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

Before exporting and deploying a model, understanding Llama's capabilities and constraints helps you make informed decisions about model selection, quantization strategy, and expected performance on mobile devices.

## What is Llama?

Llama is a family of large language models that uses publicly available data for training. Llama models perform well on a variety of natural language processing tasks, such as:

- Language translation
- Question answering
- Text summarization

Llama models are capable of generating human-like text, making them well-suited for customer-facing applications where natural, contextually relevant responses matter. A customer support chatbot built on Llama can handle free-form queries, explain product details, and guide users through troubleshooting steps -- all on-device, with no data sent to external servers.

Please note that the models are subject to the [acceptable use policy](https://github.com/facebookresearch/llama/blob/main/USE_POLICY.md) and [this responsible use guide](https://ai.meta.com/static-resource/responsible-use-guide/).

## Why on-device inference?

Running inference on the device rather than calling a cloud API has three key advantages for customer support:

- **Privacy**: user queries and session data never leave the device.
- **Low latency**: responses begin generating immediately, with no round-trip network call.
- **Offline availability**: the bot works even without an internet connection.

The tradeoff is memory. Smartphone memory constraints mean you need to quantize the model before deployment.

## Quantization

One way to create models that fit in smartphone memory is to use 4-bit groupwise per-token dynamic quantization of all linear layers. *Dynamic quantization* means quantization parameters for activations are calculated at runtime from the observed min/max range. Weights are statically quantized -- grouped per channel using 4-bit signed integers.

For further information, refer to [torchao: PyTorch Architecture Optimization](https://github.com/pytorch-labs/ao/).

The table below evaluates WikiText perplexity using [LM Eval](https://github.com/EleutherAI/lm-evaluation-harness).

The results are for two different groupsizes, with max_seq_len 2048, and 1000 samples:

| Model        | Baseline (FP32) | Groupwise 4-bit (128) | Groupwise 4-bit (256) |
|--------------|-----------------|-----------------------|-----------------------|
| Llama 2 7B   | 9.2             | 10.2                  | 10.7                  |
| Llama 3 8B   | 7.9             | 9.4                   | 9.7                   |

Note that groupsize less than 128 was not enabled in this example, because the model was still too large. Current efforts have focused on enabling FP32, and support for FP16 is under way.

What this implies for model size:

- The embedding table is in FP32
- Quantized weight scales are FP32

## KleidiAI and Arm performance

Arm has contributed [KleidiAI](https://gitlab.arm.com/kleidi/kleidiai) kernels into ExecuTorch via XNNPACK. On Arm Cortex-A processors with the i8mm feature (such as those found in many recent Android smartphones), these kernels can significantly improve inference throughput for quantized LLMs compared to standard XNNPACK kernels.

You will enable this acceleration in the build step later in the Learning Path.

## What you've learned and what's next

You now understand:
- Llama's capabilities for natural language tasks and customer support scenarios
- The benefits of on-device inference: privacy, low latency, and offline availability
- How quantization makes large language models fit in smartphone memory
- KleidiAI's role in accelerating inference on Arm processors

The next section walks you through downloading and exporting a Llama model to the format required by ExecuTorch.

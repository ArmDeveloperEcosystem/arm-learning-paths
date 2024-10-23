---
title: Understanding Llama models
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is Llama?

Llama is a family of large language models that uses publicly-available data for training. Llama models have shown to perform well on a variety of natural language processing tasks, such as:

* Language translation.
* Question answering.
* Text summarization.

Llama models are also capable of generating human-like text, making them a useful tool for creative writing and other applications where natural language generation is key.

Llama models are powerful and versatile, having the ability to generate coherent and contextually-relevant text which makes them particularly useful for applications such as:

* Chatbots.
* Virtual assistants.
* Language translation.

Please note that the models are subject to the [acceptable use policy](https://github.com/facebookresearch/llama/blob/main/USE_POLICY.md) and [this responsible use guide](https://ai.meta.com/static-resource/responsible-use-guide/).

## Results

As Llama 2 and Llama 3 models require at least 4-bit quantization due to the constraints of available memory of some smartphones, the results presented in this Learning Path correspond to 4-bit groupwise post-training quantized models.

## Quantization

One way to create models that fit in smartphone memory is to employ 4-bit groupwise per token dynamic quantization of all the linear layers of the model. *Dynamic quantization* refers to quantizing activations dynamically, such that quantization parameters for activations are calculated, from the min/max range, at runtime. Furthermore, weights are statically quantized. In this case, weights are per-channel groupwise quantized with 4-bit signed integers.

For further information, refer to [torchao: PyTorch Architecture Optimization](https://github.com/pytorch-labs/ao/).

The table below evaluates WikiText perplexity using [LM Eval](https://github.com/EleutherAI/lm-evaluation-harness).

The results are for two different groupsizes, with max_seq_len 2048, and 1000 samples:

|Model | Baseline (FP32) | Groupwise 4-bit (128) | Groupwise 4-bit (256)
|--------|-----------------| ---------------------- | ---------------
|Llama 2 7B | 9.2 | 10.2 | 10.7
|Llama 3 8B | 7.9 | 9.4 | 9.7

Note that groupsize less than 128 was not enabled in this example, since the model was still too large. This is because current efforts have focused on enabling FP32, and support for FP16 is under way.

What this implies for model size is:

1. Embedding table is in FP32.
2. Quantized weights scales are FP32.

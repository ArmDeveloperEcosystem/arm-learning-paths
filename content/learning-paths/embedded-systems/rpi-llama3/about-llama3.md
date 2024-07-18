---
title: About the Llama models
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Background

Llama is a family of publicly available large language models. Llama models have shown to perform well on a variety of natural language processing tasks, such as:

* Language translation.
* Question answering.
* Text summarization.

Llama models are also capable of generating human-like text, making them a useful tool for creative writing and other applications where natural language generation is key.

Llama models are powerful and versatile, having the ability to generate coherent and contextually relevant text, making them particularly useful for applications such as:

* Chatbots.
* Virtual assistants.
* Language translation.

The models are subject to the [acceptable use policy](https://github.com/facebookresearch/llama/blob/main/USE_POLICY.md) and the [responsible use guide](https://ai.meta.com/static-resource/responsible-use-guide/).

## Quantization

Given the large size of many neural networks, a technique called quantization is often used to reduce the memory footprint. It allows large models to be run in memory constrained environments. In a nutshell, quantization takes floating point tensors in a neural network and converts it into data format with a smaller bit-width. It is possible to go from the FP32 data format to INT8 without seeing significant loss in model accuracy. *Dynamic quantization* is when the quantization happens at runtime.

The Llama model requires at least 4-bit quantization to fit into smaller devices, such as the Raspberry Pi 5. Read more about quantization in [the PyTorch Quantization documentation](https://pytorch.org/docs/stable/quantization.html).

Let's move on to getting, compiling and running the Llama model.


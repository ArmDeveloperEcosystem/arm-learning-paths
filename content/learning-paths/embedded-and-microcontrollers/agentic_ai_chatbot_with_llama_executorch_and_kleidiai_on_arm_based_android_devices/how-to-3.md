---
title: Overview
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understanding Llama: Meta’s Large Language Model
Llama is a family of large language models trained using publicly available datasets. These models demonstrate strong performance across a range of natural language processing (NLP) tasks, including language translation, question answering, and text summarization.

In addition to their analytical capabilities, Llama models can generate human-like, coherent, and contextually relevant text, making them highly effective for applications that rely on natural language generation. Consequently, they serve as powerful tools in areas such as chatbots, virtual assistants, and language translation, as well as in creative and content-driven domains where producing natural and engaging text is essential.

Please note that the models are subject to the [acceptable use policy](https://github.com/meta-llama/llama/blob/main/USE_POLICY.md)  and this [responsible use guide](https://github.com/meta-llama/llama/blob/main/RESPONSIBLE_USE_GUIDE.md)  .



## Quantization
A practical approach to make models fit within smartphone memory constraints is through 4-bit groupwise per-token dynamic quantization of all linear layers. In this technique, dynamic quantization is applied to activations—meaning the quantization parameters are computed at runtime based on the observed minimum and maximum activation values. Meanwhile, the model weights are statically quantized, where each channel is quantized in groups using 4-bit signed integers. This method significantly reduces memory usage while maintaining model performance for on-device inference.

This method ensures efficient memory usage while maintaining model performance on resource-constrained devices.

For further information, refer to [torchao: PyTorch Architecture Optimization](https://github.com/pytorch-labs/ao/).

The table below evaluates WikiText perplexity using [LM Eval](https://github.com/EleutherAI/lm-evaluation-harness).

The results are for two different groupsizes, with max_seq_len 2048, and 1000 samples:

|Model | Baseline (FP32) | Groupwise 4-bit (128) | Groupwise 4-bit (256)
|--------|-----------------| ---------------------- | ---------------
|Llama 2 7B | 9.2 | 10.2 | 10.7
|Llama 3 8B | 7.9 | 9.4 | 9.7

Note that groupsize less than 128 was not enabled in this example, since the model was still too large. This is because current efforts have focused on enabling FP32, and support for FP16 is under way.

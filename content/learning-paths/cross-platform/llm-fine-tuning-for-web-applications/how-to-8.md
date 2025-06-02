---
title: Fine Tune Large Language Model and Quantization
weight: 10

### FIXED, DO NOT MODIFY
layout: learningpathall
---

####  Llama Model 
Llama is a family of large language models designed for high-performance language processing tasks, trained using publicly available data. When fine-tuned, Llama-based models can be optimized for specific applications, enhancing their ability to generate accurate and context-aware responses. Fine-tuning enables the model to adapt to domain-specific data, improving performance in tasks such as:

-   Language translation – Enhancing fluency and contextual accuracy.
-   Question answering – Providing precise and relevant responses.
-   Text summarization – Extracting key insights while maintaining coherence.

Fine-tuned LLaMA models are also highly effective in generating human-like text, making them valuable for:

-   Chatbots – Enabling intelligent and context-aware interactions.
-   Virtual assistants – Enhancing responsiveness and personalization.
-   Creative writing – Generating compelling and structured narratives.

By fine-tuning Llama based models, their adaptability and relevance can be significantly improved, allowing seamless integration into specialized AI applications.Please note that the models are subject to the [acceptable use policy](https://github.com/facebookresearch/llama/blob/main/USE_POLICY.md) and [this responsible use guide](https://ai.meta.com/static-resource/responsible-use-guide/).

#### Results

Since LLaMA 2 and LLaMA 3 models require at least 4-bit quantization to accommodate the memory constraints of certain smartphones

#### Quantization

To optimize models for smartphone memory constraints, 4-bit groupwise per-token dynamic quantization can be applied to all linear layers. In this approach:

-   Dynamic quantization is used for activations, where quantization parameters are computed at runtime based on the min/max range.
-   Static quantization is applied to weights, which are per-channel groupwise quantized using 4-bit signed integers.

This method ensures efficient memory usage while maintaining model performance on resource-constrained devices.

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
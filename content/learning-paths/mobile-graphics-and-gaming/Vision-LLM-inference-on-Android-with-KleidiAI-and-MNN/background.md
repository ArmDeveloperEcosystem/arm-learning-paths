---
title: Background
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Mobile Neural Network (MNN)

MNN is a high-performance, lightweight deep learning framework designed for both inference and training. Optimized for on-device deployment, it delivers industry-leading efficiency across various applications. Currently, MNN is integrated into over 30 Alibaba Inc. apps, including Taobao, Tmall, Youku, DingTalk, and Xianyu. It powers more than 70 real-world scenarios, such as live streaming, short video processing, search recommendations, image-based product searches, and more.

**MNN-LLM** is a large language model (LLM) runtime solution built on the MNN engine, designed to enable local deployment of LLMs across diverse platforms, including mobile devices, PCs, and IoT systems. It supports leading models such as Qianwen, Baichuan, Zhipu, and LLAMA, ensuring efficient and accessible AI-powered experiences.

KleidiAI, a collection of optimized AI operators, is integrated into the MNN framework, enhancing the inference performance of large language models (LLMs) within MNN. The Android app in this learning path demonstrates Vision Transformer inference using the MNN framework. You will use KleidiAI to speed up inference for the [Qwen Vision 2B](https://huggingface.co/Qwen/Qwen2-VL-2B-Instruct) model.

## Vision Transformer（ViT）
The ViT is a deep learning model designed for image recognition tasks. Unlike traditional convolutional neural networks (CNNs), which process images using convolutional layers, ViT leverages the transformer architecture originally developed for natural language processing (NLP).
The ViT workflow integrates the following features:

- **Image Patching** - The input image is divided into fixed-size patches, similar to how text is tokenized in NLP tasks.
- **Linear Embedding** - Each image patch is flattened and linearly embedded into a vector.
- **Position Encoding** - Positional information is added to the patch embeddings to retain spatial information.
- **Transformer Encoder** - The embedded patches are fed into a standard transformer encoder, which uses self-attention mechanisms to process the patches and capture relationships between them.
- **Classification** - The output of the transformer encoder is used for image classification or other vision tasks.

ViT has shown competitive performance on various image classification benchmarks and has been widely adopted in computer vision research.
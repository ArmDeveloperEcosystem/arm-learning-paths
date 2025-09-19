---
title: Background
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Mobile Neural Network (MNN)

MNN is a high-performance, lightweight deep learning framework designed for both inference and training. Optimized for on-device deployment, it delivers industry-leading efficiency across various applications. Currently, MNN is integrated into more than 30 Alibaba Inc. apps - including Taobao, Tmall, Youku, DingTalk, and Xianyu - and powers over 70 real-world scenarios such as live streaming, short video processing, search recommendations, and image-based product searches.

**MNN-LLM** is a large language model (LLM) runtime solution built on the MNN engine. It enables local deployment of LLMs across diverse platforms, including mobile devices, PCs, and IoT systems, and supports leading models such as Qianwen, Baichuan, Zhipu, and Llama for efficient, accessible AI-powered experiences.

KleidiAI, a collection of optimized AI micro-kernels, is integrated into the MNN framework to enhance the inference performance of LLMs. In this Learning Path, the Android app demonstrates Vision Transformer inference using the MNN framework. You will use KleidiAI to speed up inference for the [Qwen2.5 Vision 3B](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct) model.

## Vision Transformer (ViT)
The Vision Transformer (ViT) is a deep learning model designed for image recognition tasks. Unlike traditional convolutional neural networks (CNNs) that use convolutional layers, ViT leverages the transformer architecture originally developed for natural language processing (NLP).

Its workflow includes:

- **Image Patching**: Dividing the input image into fixed-size patches, similar to tokenizing text in NLP.
- **Linear Embedding**: Flattening each image patch and linearly embedding it into a vector.
- **Position Encoding**: Adding positional information to the patch embeddings to preserve spatial details.
- **Transformer Encoder**: Processing the embedded patches using a standard transformer encoder with self-attention mechanisms to capture relationships.
- **Classification**: Using the encoder's output for image classification or other vision tasks. 

ViT has demonstrated competitive performance on various image classification benchmarks and is widely adopted in computer vision research.

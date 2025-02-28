---
title: Background
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## MNN Introduction
MNN is a highly efficient and lightweight deep learning framework. It supports inference and training of deep learning models and has industry-leading performance for inference and training on-device. At present, MNN has been integrated into more than 30 apps of Alibaba Inc, such as Taobao, Tmall, Youku, DingTalk, Xianyu, etc., covering more than 70 usage scenarios such as live broadcast, short video capture, search recommendation, product searching by image, interactive marketing, equity distribution, security risk control. In addition, MNN is also used on embedded devices, such as IoT.

MNN-LLM is a large language model runtime solution developed based on the MNN engine. The mission of this project is to deploy LLM models locally on everyone's platforms(Mobile Phone/PC/IOT). It supports popular large language models such as Qianwen, Baichuan, Zhipu, LLAMA, and others. 

KleidiAI is currently integrated into the MNN framework, enhancing the inference performance of large language models (LLMs) within MNN. The Android app on this page demonstrates Vision Transformer inference using the MNN framework, accelerated by KleidiAI.

## Vision Transformer（ViT）
The Vision Transformer (ViT) is a deep learning model designed for image recognition tasks. Unlike traditional convolutional neural networks (CNNs), which process images using convolutional layers, ViT leverages the transformer architecture originally developed for natural language processing (NLP).
The Vit workflow contains:

- **Image Patching** : The input image is divided into fixed-size patches, similar to how text is tokenized in NLP tasks.
- **Linear Embedding** : Each image patch is flattened and linearly embedded into a vector.
- **Position Encoding** : Positional information is added to the patch embeddings to retain spatial information.
- **Transformer Encoder** : The embedded patches are fed into a standard transformer encoder, which uses self-attention mechanisms to process the patches and capture relationships between them.
- **Classification** : The output of the transformer encoder is used for image classification or other vision tasks.

ViT has shown competitive performance on various image classification benchmarks and has been widely adopted in computer vision research



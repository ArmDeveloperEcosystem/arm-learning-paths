---
title: Multimodal On-Device Inference on Arm v9 with MNN for Audio and Vision
layout: learningpathall
weight: 2
---

## Introduction

This module explains why **[MNN](https://github.com/alibaba/MNN)** and an **Omni multimodal model** are a practical combination for **CPU-only on-device inference** on Arm v9 Linux. You will use a single runtime and a single model to run **vision**, **audio**, and **text** prompts, then combine image + audio inputs to generate an operational **restock ticket**.

## Why MNN for on-device deployment

MNN is a deployment-focused inference runtime that works well for edge and mobile-style workloads:

- A **portable runtime** widely used across mobile and embedded environments
- A **CPU-first workflow** that maps naturally to Arm v9 Linux systems
- Native builds can take advantage of **Arm-specific optimizations** (for example, KleidiAI when enabled)
- One codebase can target multiple platforms such as Arm Linux, Android, iOS, and x86 hosts

## Why Omni multimodal

Omni models simplify multimodal applications by keeping image, audio, and text in a single pipeline:

- One model can handle **image + audio + text** prompts
- Enables cross-modal tasks such as **“audit the shelf image + listen to a voice note → produce a restock ticket”**
- Prompt control using tags like `<img>...</img>` and `<audio>...</audio>`
- Reduces operational complexity versus maintaining separate vision and speech models

## Scope

To keep this learning path reproducible and easy to complete, we intentionally constrain the scope:

- **CPU-only**  
  No GPU or NPU acceleration is required.

- **No export or quantization steps**  
  You will use a **prebuilt MNN Omni model package** as-is.

- **No CPU–NPU heterogeneous pipeline**  
  All compute runs on the Arm v9 CPU. The focus is correctness and reproducibility.

## Next

In the next module, you will build MNN on Arm v9 and prepare the prebuilt Omni model and local demo assets.
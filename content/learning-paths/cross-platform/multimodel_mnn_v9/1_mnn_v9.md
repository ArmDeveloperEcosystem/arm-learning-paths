---
title: Run multimodal inference with MNN on Armv9
layout: learningpathall
weight: 2
---

## Understand MNN and multimodal inference on Armv9

This section introduces the software stack used throughout this Learning Path. You will use **[MNN](https://github.com/alibaba/MNN)** (Mobile Neural Network), a lightweight inference engine, to run a prebuilt **Omni multimodal model** on an Armv9 Linux system using only the CPU.

By the end of this section, you'll understand why this combination is a practical starting point for reproducible multimodal inference on Armv9. A retail restocking workflow that combines local image and audio inputs is used as the example throughout.

## Why use MNN on Armv9

MNN is a lightweight inference engine designed for deployment across mobile, embedded, and edge platforms. It's a good fit for this Learning Path for four reasons:

- Provides a **portable runtime** that can be built and reused across different device classes
- Supports a **CPU-first deployment flow**, useful when you want to validate multimodal inference on Armv9 without depending on a discrete GPU or dedicated accelerator
- Native builds take advantage of **Armv9-specific CPU features and optimizations** when enabled in the build, making this a practical path for efficient local inference
- The same runtime approach can be reused across **Arm Linux, Android, iOS, and x86-based development hosts**, improving portability from development to deployment

For this Learning Path, MNN gives you a practical way to build a reproducible multimodal inference workflow on Armv9 while keeping the software stack compact and deployment-oriented.

## Why use an Omni multimodal model

An Omni model combines **text, image, and audio** understanding in a single inference pipeline, making it useful for building compact edge applications that need to reason over more than one input type.

In this Learning Path, you use the model to:

- process **text-only prompts**
- describe **image inputs**
- interpret **audio inputs**
- combine **image and audio context** to generate a structured **restock ticket**

This single-model approach keeps the workflow easier to follow than maintaining separate models for vision and speech tasks.

## Scope of this Learning Path

To keep the workflow reproducible, this Learning Path uses a deliberately narrow scope:

- **CPU-only execution**  
  All inference runs on the Armv9 CPU.

- **Prebuilt model assets**  
  You use a prepared MNN Omni model package instead of exporting or converting models.

- **No heterogeneous scheduling**  
  This example does not use GPU, NPU, or split CPU-accelerator execution.

This scope keeps the focus on setup, validation, and multimodal application flow.

## What you've learned and what's next

In this section, you learned:

- Why MNN is a practical inference engine for multimodal workflows on Armv9
- How an Omni model combines text, image, and audio understanding in one pipeline
- The deliberate scope choices that keep this Learning Path reproducible and focused on CPU-first inference

In the next section, you'll build MNN natively on Armv9 and prepare the model files and local assets used in the remaining examples.
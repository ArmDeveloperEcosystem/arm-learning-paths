---
title: Run multimodal inference with MNN on Armv9
layout: learningpathall
weight: 2
---

## Introduction

This section introduces the software stack used throughout this Learning Path. You will use **[MNN](https://github.com/alibaba/MNN)** to run a prebuilt **Omni multimodal model** on an Armv9 Linux system using only the CPU.

By the end of this section, you will understand why this combination is a practical starting point for reproducible multimodal inference on Armv9.

## Why use MNN on Armv9

MNN is a lightweight inference engine designed for deployment across mobile, embedded, and edge platforms. It is a good fit for this Learning Path for four reasons:

- It provides a **portable runtime** that can be built and used across different device classes.
- It supports a **CPU-first deployment flow**, which maps well to Armv9 development systems.
- Native builds can take advantage of **Arm-specific optimizations** when they are enabled in the build.
- The same runtime approach can be reused across **Arm Linux, Android, iOS, and x86-based development hosts**.

For this Learning Path, MNN gives you a practical way to validate multimodal inference on Armv9 without introducing extra framework complexity.

## Why use an Omni multimodal model

An Omni model combines **text, image, and audio** understanding in a single inference pipeline. This makes it useful for building compact edge applications that need to reason over more than one input type.

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

## Next steps

In the next section, you will build MNN on Armv9 and prepare the model files and local assets used in the remaining examples.

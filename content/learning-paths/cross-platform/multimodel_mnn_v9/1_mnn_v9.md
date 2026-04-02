---
title: Multimodal On-Device Inference on Arm v9 with MNN for Audio and Vision
weight: 2

layout: learningpathall
---

## Why MNN for on-device deployment

- **Portable inference runtime** with strong support for mobile and edge platforms
- **CPU-first workflow** that maps naturally to Armv9 servers and development boards
- Native builds allow you to benefit from **Arm-specific optimizations** (such as KleidiAI)
- Single codebase can target x86, Arm Linux, Android, and iOS

## Why Omni multimodal

- **Single model** that can handle **image, audio, and text** in one pipeline
- Enables **cross-modal tasks** such as “look at this shelf + listen to this note → generate an operational ticket”
- **Prompt-based control** with tags like `<img>…</img>` and `<audio>…</audio>`
- No need to maintain separate models for vision and speech

## Scope boundaries for reproducibility

To keep this Learning Path simple and repeatable, we deliberately limit the scope:

- **CPU-only**  
  No GPU or NPU acceleration is required.

- **No quantization**  
  You use a **prebuilt MNN Omni model package** as-is. No additional export or quantization steps are needed.

- **No CPU–NPU heterogeneous pipeline**  
  All compute runs on the Armv9 CPU. Focus is on **correctness and reproducibility**, not maximum throughput.
---
title: Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction 
In this section, you get a quick mental model of SME2, KleidiAI, and what llama.cpp is doing when it runs LLM inference on an Arm CPU.
Arm’s latest Client CPU processors such as Arm C1 include Scalable Matrix Extension 2 (SME2). SME2 accelerates the matrix-heavy AI operations behind large language models (LLMs), media processing, speech recognition, computer vision, real-time apps and multimodal apps.

llama.cpp provides extensive support for many LLMs, including Phi, Llama, DeepSeek, Gemma and Qwen. It's designed for efficient CPU-based inference, enabling on-device LLM execution that reduces latency and enhances privacy.

By default, llama.cpp integrates with Arm KleidiAI, a suite of optimized microkernels for Arm CPUs. KleidiAI includes SME2-optimized microkernels to deliver additional performance benefits.

This Learning Path uses the `Llama-3.2-3B-Instruct-Q4_0.gguf` model with 3 billion parameters.

Move on to the next section to see how KleidiAI microkernels integrate into llama.cpp's CPU backend.





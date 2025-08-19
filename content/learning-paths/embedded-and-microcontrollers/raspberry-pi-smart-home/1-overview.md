---
title: Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

This Learning Path walks you through deploying an efficient large language model (LLM) locally on the Raspberry Pi 5, powered by an Arm Cortex-A76 CPU. This will allow you to control your smart home using natural language, without relying on cloud services. With rapid advances in Generative AI and the power of Arm Cortex-A processors, you can now run advanced language models directly in your home on the Raspberry Pi 5.

You will create a fully local, privacy-first smart home system that leverages the strengths of Arm Cortex-A architecture. The system can achieve 15+ tokens per second inference speeds using optimized models like TinyLlama and Qwen, while maintaining the energy efficiency that makes Arm processors a good fit for always-on applications.

## Why Arm Cortex-A for Edge AI?

The Raspberry Pi 5's Arm Cortex-A76 processor can manage high-performance computing tasks like AI inference. Key architectural features include:

- The **superscalar architecture** allows the processor to execute multiple instructions in parallel, improving throughput for compute-heavy tasks.
- **128-bit NEON SIMD support** accelerates matrix and vector operations, which are common in the inner loops of language model inference.
- The **multi-level cache hierarchy** helps reduce memory latency and improves data access efficiency during runtime.
- The **thermal efficiency** enables sustained performance without active cooling, making it ideal for compact or always-on smart home setups.

These characteristics make the Raspberry Pi 5 well-suited for workloads like smart home assistants, where responsiveness, efficiency, and local processing are important. Running LLMs locally on Arm-based devices brings several practical benefits. Privacy is preserved, since conversations and routines never leave the device. With optimized inference, the system can offer responsiveness under 100 ms, even on resource-constrained hardware. It remains fully functional in offline scenarios, continuing to operate when internet access is unavailable. Developers also gain flexibility to customize models and automations. Additionally, software updates and an active ecosystem continue to improve performance over time.

## Arm Ecosystem Advantages

For the stack in this setup, Raspberry Pi 5 benefits from the extensive developer ecosystem:

- Optimized compilers including GCC and Clang with Arm-specific enhancements
- Native libraries such as gpiozero and lgpio are optimized for Raspberry Pi
- Community support from open-source projects where developers are contributing Arm-optimized code
- Arm maintains a strong focus on backward compatibility, which reduces friction when updating kernels or deploying across multiple Arm platforms
- The same architecture powers smartphones, embedded controllers, edge devices, and cloud infrastructure—enabling consistent development practices across domains

## Performance Benchmarks on Raspberry Pi 5

The table below shows inference performance for several quantized models running on a Raspberry Pi 5. Measurements reflect single-threaded CPU inference with typical prompt lengths and temperature settings suitable for command-based interaction.

| Model               | Tokens/Sec | Avg Latency (ms) |
| ------------------- | ---------- | ---------------- |
| qwen:0.5b           | 17.0       | 8,217            |
| tinyllama:1.1b      | 12.3       | 9,429            |
| deepseek-coder:1.3b | 7.3        | 22,503           |
| gemma2:2b           | 4.1        | 23,758           |
| deepseek-r1:7b      | 1.6        | 64,797           |


What does this table tell us? Here are some performance insights:

- Qwen 0.5B and TinyLlama 1.1B deliver fast token generation and low average latency, making them suitable for real-time interactions like voice-controlled smart home commands.
- DeepSeek-Coder 1.3B and Gemma 2B trade off some speed for improved language understanding, which can be useful for more complex task execution or context-aware prompts.
- DeepSeek-R1 7B offers advanced reasoning capabilities with acceptable latency, which may be viable for offline summarization, planning, or low-frequency tasks.

## Supported Arm-Powered Devices

This Learning Path focuses on the Raspberry Pi 5, but you can adapt the concepts and code to other Arm-powered devices:

### Recommended Platforms

| Platform         | CPU                              | RAM            | GPIO Support                  | Model Size Suitability      |
|------------------|----------------------------------|----------------|-------------------------------|-----------------------------|
| **Raspberry Pi 5** | Arm Cortex-A76 quad-core @ 2.4GHz | Up to 16GB     | Native `lgpio` (high-performance) | Large models (8–16GB)        |
| **Raspberry Pi 4** | Arm Cortex-A72 quad-core @ 1.8GHz | Up to 8GB      | Compatible with `gpiozero`        | Small to mid-size models     |
| **Other Arm Devices** | Arm Cortex-A             | 4GB min (8GB+ recommended) | Requires physical GPIO pins       | Varies by RAM                |

Additionally, the platform must:

- GPIO pins available for hardware control
- Use Python 3.8 or newer
- Ability to run [Ollama](https://ollama.com/)

Continue to the next section to start building a smart home system that highlights how Arm-based processors can enable efficient, responsive, and private AI applications at the edge.
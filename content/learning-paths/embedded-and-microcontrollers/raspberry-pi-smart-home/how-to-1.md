---
title: Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

Control your smart home using natural language with no cloud connection, no third-party servers, and no compromises on privacy. With rapid advances in Generative AI and the power of Arm Cortex-A processors, you can now run large language models (LLMs) directly in your home on the Raspberry Pi 5.

You will create a fully local, privacy-first smart home system that leverages the strengths of Arm Cortex-A architecture. The system achieves 15+ tokens per second inference speeds using optimized models like TinyLlama and Qwen, while maintaining the energy efficiency that makes Arm processors ideal for always-on applications.

## Why Arm Cortex-A for Edge AI?

The Raspberry Pi 5's Arm Cortex-A76 processor excels at high-performance computing tasks like AI inference through:

- Superscalar architecture that executes multiple instructions simultaneously
- Advanced SIMD with 128-bit NEON units for matrix operations
- Multi-level cache hierarchy that reduces memory latency
- Thermal efficiency that maintains performance in compact form factors

Your Arm-powered smart home processes everything locally, providing:

- **Total Privacy**: Conversations and routines never leave your device
- **Lightning Speed**: Sub-100ms response times with optimized processing
- **Rock-Solid Reliability**: Operation continues when internet connectivity fails
- **Unlimited Customization**: Complete control over AI models and automations
- **Future-Proof Performance**: Continued optimization through Arm's roadmap

## Performance Benchmarks on Raspberry Pi 5

| Model               | Tokens/Sec | Avg Latency (ms) | Performance Rating   |
| ------------------- | ---------- | ---------------- | -------------------- |
| qwen:0.5b           | 17.0       | 8,217            | ⭐⭐⭐⭐⭐ Excellent |
| tinyllama:1.1b      | 12.3       | 9,429            | ⭐⭐⭐⭐⭐ Excellent |
| deepseek-coder:1.3b | 7.3        | 22,503           | ⭐⭐⭐⭐ Very Good   |
| gemma2:2b           | 4.1        | 23,758           | ⭐⭐⭐⭐ Very Good   |
| deepseek-r1:7b      | 1.6        | 64,797           | ⭐⭐⭐ Good          |

Performance insights:

- Qwen 0.5B and TinyLlama 1.1B provide optimal speed for real-time smart home commands
- DeepSeek-Coder 1.3B and Gemma2 2B handle complex automation tasks effectively
- DeepSeek-R1 7B offers advanced reasoning capabilities with acceptable latency

## Arm Ecosystem Advantages

The Raspberry Pi 5 benefits from the extensive Arm developer ecosystem:

- Optimized compilers including GCC and Clang with Arm-specific enhancements
- Native libraries such as gpiozero and lgpio optimized for Raspberry Pi
- Community support from millions of developers contributing Arm-optimized code
- Long-term support through Arm's commitment to backward compatibility
- Industrial adoption with the same architecture powering smartphones, servers, and embedded systems

## Supported Arm-Powered Devices

This learning path focuses on the Raspberry Pi 5, but you can adapt the concepts and code to other Arm-powered devices:

### Recommended Platforms

**Raspberry Pi 5 (Primary Focus)**

- Arm Cortex-A76 quad-core @ 2.4GHz
- Up to 16GB RAM for larger models
- Native lgpio support with optimized GPIO performance

**Raspberry Pi 4**

- Arm Cortex-A72 quad-core @ 1.8GHz
- 8GB RAM maximum, suitable for smaller models
- Proven compatibility with gpiozero ecosystem

### Compatibility Requirements

Any Arm device can potentially run this project with:

- Arm Cortex-A processor
- Minimum 4GB RAM (8GB+ recommended)
- GPIO pins for hardware control
- Python 3.8+ support
- Ability to run Ollama

If your Arm device supports Linux, Python, and has GPIO capabilities, you can adapt this learning path to your specific hardware.

## What You Will Build

By completing this learning path, your Raspberry Pi 5 will run:

- Ultra-fast AI processing with 15+ tokens/second performance
- Complete GPIO control for lights, fans, locks, and sensors via gpiozero + lgpio
- Modern web dashboard with FastAPI-powered interface optimized for mobile
- NEON-accelerated performance using custom ARM assembly for critical paths
- Zero-cloud architecture with everything running locally on your Arm processor
- Intelligent automation with scene-based control using natural language

You will build a smart home system that demonstrates why Arm processors represent the future of edge computing, combining efficiency, performance, and complete privacy control.

---
title: Explore Grace Blackwell architecture for efficient quantized LLM inference
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this Learning Path you will explore the architecture and system design of NVIDIA DGX Spark, a next-generation Arm-based CPU-GPU hybrid for large-scale AI workloads. The NVIDIA DGX Spark is a personal AI supercomputer that brings data center-class AI computing directly to the developer desktop. The NVIDIA GB10 Grace Blackwell Superchip fuses CPU and GPU into a single unified compute engine.

The GB10 platform combines:
- The NVIDIA Grace CPU, featuring 10 Arm [Cortex-X925](https://www.arm.com/products/cortex-x) and 10 [Cortex-A725](https://www.arm.com/products/silicon-ip-cpu/cortex-a/cortex-a725) cores built on the Armv9 architecture, offering exceptional single-thread performance and power efficiency
- The NVIDIA Blackwell GPU, equipped with next-generation CUDA cores and 5th-generation Tensor Cores, optimized for FP8 and FP4 precision workloads
- A 128 GB unified memory subsystem, enabling both CPU and GPU to share the same address space with NVLink-C2C, eliminating data-transfer bottlenecks

This GB10 platform design delivers up to 1 petaFLOP (1,000 TFLOPs) of AI performance at FP4 precision. DGX Spark is a compact yet powerful development platform that lets you build and test AI models locally before scaling them to larger systems.

You can find out more about Nvidia DGX Spark on the [NVIDIA website](https://www.nvidia.com/en-gb/products/workstations/dgx-spark/).

## Benefits of Grace Blackwell for quantized LLM inference

Quantized Large Language Models (LLMs), such as those using Q4, Q5, or Q8 precision, benefit from the hybrid architecture of the Grace Blackwell Superchip which brings several key advantages to quantized LLM workloads. The unified CPU-GPU design eliminates traditional bottlenecks while providing specialized compute capabilities for different aspects of inference.

On Arm-based systems, quantized LLM inference is especially efficient because the Grace CPU delivers high single-thread performance and energy efficiency, while the Blackwell GPU accelerates matrix operations using Arm-optimized CUDA libraries. The unified memory architecture means you don't need to manually manage data movement between CPU and GPU, which is a common challenge on traditional x86-based platforms. This is particularly valuable when working with large models or running multiple inference tasks in parallel, as it reduces latency and simplifies development.

## Grace Blackwell features and their impact on quantized LLMs

The table below shows how specific hardware features enable efficient quantized model inference:

| **Feature** | **Impact on quantized LLMs** |
|--------------|------------------------------|
| Grace CPU (Arm Cortex-X925 / A725) | Handles token orchestration, memory paging, and lightweight inference efficiently with high instructions per cycle (IPC) |
| Blackwell GPU (CUDA 13, FP4/FP8 Tensor Cores) | Provides massive parallelism and precision flexibility, ideal for accelerating 4-bit or 8-bit quantized transformer layers |
| High bandwidth and low latency | NVLink-C2C delivers 900 GB/s of bidirectional bandwidth, enabling synchronized CPU-GPU workloads |
| Unified 128 GB memory (NVLink-C2C) | CPU and GPU share the same memory space, allowing quantized model weights to be accessed without explicit data transfer |
| Energy-efficient Arm design | Armv9 cores maintain strong performance-per-watt, enabling sustained inference for extended workloads |

## Overview of a typical quantized LLM workflow

In a typical quantized LLM workflow:
- The Grace CPU orchestrates text tokenization, prompt scheduling, and system-level tasks
- The Blackwell GPU executes the transformer layers using quantized matrix multiplications for optimal throughput
- Unified memory allows models like Qwen2-7B or LLaMA3-8B (Q4_K_M) to fit directly into the shared memory space, reducing copy overhead and enabling near-real-time inference

Together, these features make the GB10 a developer-grade AI laboratory for running, profiling, and scaling quantized LLMs efficiently in a desktop form factor.



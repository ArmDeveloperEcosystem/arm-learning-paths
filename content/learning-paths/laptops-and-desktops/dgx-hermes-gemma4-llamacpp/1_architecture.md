---
title: Explore the local agent architecture on DGX Spark
description: Understand the local architecture and unified memory budget for running Nous Research Hermes Agent with llama.cpp, CUDA, and Gemma 4 E4B on NVIDIA DGX Spark.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Local autonomous agent capabilities

Build a fully local autonomous coding and workspace agent on an NVIDIA DGX Spark system without cloud Application Programming Interfaces (APIs). Compile llama.cpp from source with Blackwell CUDA acceleration and Armv9.2 KleidiAI CPU support, benchmark three Gemma 4 variants (E4B, 26B-A4B Mixture of Experts, and 31B dense) across the Blackwell GPU and Grace CPU, then connect Nous Research Hermes Agent to inspect workspaces, diagnose and fix code errors, and run verification commands.

Autonomous agents place different demands on local inference than simple chat sessions. Each user request can trigger multiple back-and-forth tool calls, such as listing directories, reading files, editing code, and running verification commands, that need:

- **Large context windows**: Hermes Agent needs at least a 64K context window to hold system prompts, tool schemas, file contents, and multi-step conversation history.
- **Fast prompt prefill**: Hermes Agent sends an ~11K-token system prompt and tool schema on the first turn of a session, making Blackwell GPU acceleration essential for multi-thousand-token-per-second prefill and sub-minute end-to-end tool loops.
- **Unified memory headroom**: DGX Spark pairs a 20-core Armv9.2 Grace CPU (10 Cortex-X925 performance cores and 10 Cortex-A725 efficiency cores) with an NVIDIA GB10 Blackwell GPU over 128 GB of coherent unified LPDDR5X memory. That pool fits Gemma 4 E4B with a 64K quantized Key-Value (KV) cache in ~4 GB while leaving room to benchmark larger 26B and 31B models.

## System architecture

The runtime consists of two local processes communicating over loopback HTTP:

```text
+-----------------------------------------------------------------------+
|                         User Terminal (CLI)                           |
+-----------------------------------+-----------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|                   Nous Research Hermes Agent                          |
|  - Autonomous planning and multi-step tool loop                       |
|  - Built-in tools: shell, filesystem, skills                          |
+-----------------------------------+-----------------------------------+
                                    |
                                    | OpenAI-compatible HTTP API
                                    | http://127.0.0.1:8080/v1
                                    v
+-----------------------------------------------------------------------+
|                    llama-server (llama.cpp)                           |
|  - CUDA Blackwell offload (-ngl 99, sm_121a) + Armv9.2 KleidiAI CPU   |
|  - 64K context (-c 65536), Flash Attention (-fa on), q8_0 KV cache    |
+-----------------------------------+-----------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|               NVIDIA GB10 Unified Memory (128 GB LPDDR5X)             |
|  - Gemma 4 E4B GGUF weights (~4.3 GB on disk)                         |
|  - 64K quantized KV cache (q8_0) + CUDA buffers shared with GB10 GPU  |
+-----------------------------------------------------------------------+
```

The Grace CPU and Blackwell GB10 GPU share a unified physical memory space without PCIe copies, so offloading all layers with `-ngl 99` lets CUDA kernels access model weights and the KV cache directly. Compiling the CPU backend with explicit Armv9.2 flags and Arm KleidiAI gives you an optimized Grace CPU path for side-by-side benchmarking and CPU fallback. The OpenAI-compatible `/v1` API exposed by `llama-server` means you can switch models or adjust GPU offloading without changing your Hermes Agent workflow.

## Memory budget with a 64K context window

Sizing a local agent for a 64K context window means accounting for both the model weights and the runtime KV cache and CUDA buffers. Using 4-bit quantized model weights (`Q4_0`) together with an 8-bit quantized KV cache (`q8_0`) and Flash Attention (`-fa on`) keeps memory usage compact while preserving long-context accuracy.

| Component | Gemma 4 E4B (`Q4_0`) | Notes |
|---|---|---|
| Model weights on disk | ~4.3 GB | Loaded into GB10 unified memory |
| `llama-server` GPU and KV allocation (`q8_0`, 64K) | ~4.0 GB | Observed `4,088 MiB` in `nvidia-smi` (`~3.03 GiB` RSS) after multi-turn tool calls |
| Ubuntu OS, desktop, and Hermes Agent | ~4–6 GB | Varies with desktop sessions and other local services |
| **Total estimated unified memory** | **~8–10 GB** | Leaves over 115 GB free on a dedicated 128 GB DGX Spark |

## What you've learned and what's next

You've reviewed the local agent architecture, the Grace Blackwell GB10 unified memory data path, and the 64K context memory budget for running Gemma 4 E4B with llama.cpp on NVIDIA DGX Spark.

Next, you'll verify your DGX Spark environment and compile llama.cpp from source with Blackwell CUDA and Armv9.2 KleidiAI optimizations.

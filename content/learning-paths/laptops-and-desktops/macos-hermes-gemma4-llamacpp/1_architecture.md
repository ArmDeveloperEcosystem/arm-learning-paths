---
title: Explore the local agent architecture on macOS
description: Understand the local architecture and unified memory budget for running Nous Research Hermes Agent with llama.cpp, Metal, and Gemma 4 E4B on Apple silicon Macs.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Local autonomous agent capabilities

Build a fully local autonomous coding and workspace agent on an Apple silicon Mac without cloud Application Programming Interfaces (APIs). Compile llama.cpp from source with Metal GPU acceleration and Arm KleidiAI support, serve Gemma 4 E4B locally, then connect Nous Research Hermes Agent to inspect workspaces, diagnose and fix code errors, and run verification commands.

Autonomous agents place different demands on local inference than simple chat sessions. Each user request can trigger multiple back-and-forth tool calls, such as listing directories, reading files, editing code, and running verification commands, that need:

- **Large context windows**: Hermes Agent needs at least a 64K context window to hold system prompts, tool schemas, file contents, and multi-step conversation history.
- **Fast prompt prefill**: Hermes Agent sends an ~11K-token system prompt and tool schema on the first turn of a session, making Metal GPU acceleration on unified memory essential for sub-10-second response times.
- **Predictable memory usage**: Running Gemma 4 E4B with an 8-bit quantized Key-Value (KV) cache in macOS Unified Memory Architecture (UMA) keeps the `llama-server` memory footprint compact, leaving plenty of headroom even on 16 GB–24 GB Macs.

## System architecture

The runtime consists of two local processes communicating over loopback HTTP:

```text
+-----------------------------------------------------------------------+
|                         User Terminal (zsh)                           |
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
|  - Metal GPU offload (-ngl 99) + Accelerate + Arm KleidiAI (SME)      |
|  - 64K context (-c 65536), Flash Attention (-fa on), q8_0 KV cache    |
+-----------------------------------+-----------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|                  Apple Silicon Unified Memory (16 GB+)                |
|  - Memory-mapped Gemma 4 E4B GGUF weights (~4.3 GB on disk)           |
|  - 64K quantized KV cache (q8_0) + Metal buffers shared with GPU      |
+-----------------------------------------------------------------------+
```

Apple silicon shares physical memory between CPU cores and the integrated Metal GPU without PCIe copies, so offloading all model layers with `-ngl 99` lets Metal kernels read weights directly from unified memory. Apple Accelerate and Arm KleidiAI kernels handle CPU-side Basic Linear Algebra Subprograms (BLAS) and fallback paths, transparently using hardware extensions such as Scalable Matrix Extension (SME) on M4 and M5 Macs. The OpenAI-compatible `/v1` API exposed by `llama-server` means you can adjust GPU offload or thread counts without changing your agent workflow.

## Memory budget with a 64K context window

Sizing a local agent for a 64K context window means accounting for both the memory-mapped model weights and the dirty physical footprint of the KV cache and Metal buffers. Using 4-bit quantized model weights (`Q4_0`) together with an 8-bit quantized KV cache (`q8_0`) and Flash Attention (`-fa on`) keeps memory growth compact while preserving long-context accuracy.

| Component | Gemma 4 E4B | Notes |
|---|---|---|
| Model weights (`mmap` clean memory) | ~2.9–4.3 GB | Memory-mapped from the 4.3 GB GGUF file as layers are accessed |
| 64K KV cache (`q8_0`) and Metal buffers | ~1.0 GB | Observed dirty physical footprint (`955 MB`) after multi-turn tool calls |
| macOS, desktop apps, and Hermes Agent | ~8–10 GB | Varies with open browsers, editors, and active terminal sessions |
| **Total estimated unified memory** | **~12–15 GB** | Fits comfortably on 16 GB or larger Apple silicon Macs |

## What you've learned and what's next

You've reviewed the local agent architecture, unified memory data path, and 64K context memory budget for running Gemma 4 E4B with llama.cpp and Metal on macOS.

Next, you'll verify your Apple silicon Mac environment and compile llama.cpp from source for maximum performance.

---
title: Building Llama.cpp
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this step, you'll build Llama.cpp from source. Llama.cpp is a high-performance C++ implementation of the LLaMA model that's optimized for inference on various hardware platforms, including Arm-based processors like Graviton4.

Even though AFM-4.5B uses a custom model architecture, you can still use the standard Llama.cpp repository - Arcee AI has contributed the necessary modeling code upstream.

## Clone the repository

```bash
git clone https://github.com/ggerganov/llama.cpp
```

This command clones the Llama.cpp repository from GitHub to your local machine. The repository contains the source code, build scripts, and documentation needed to compile the inference engine.

## Navigate to the project directory

```bash
cd llama.cpp
```

Change into the llama.cpp directory to run the build process. This directory contains the `CMakeLists.txt` file and all source code.

## Configure the build with CMake

```bash
cmake -B .
```

This command uses CMake to configure the build system:

- `-B .` tells CMake to generate build files in the current directory
- CMake detects your system's compiler, libraries, and hardware capabilities
- It produces Makefiles (on Linux) or platform-specific build scripts for compiling the project


If you're running on Graviton4, the CMake output should include hardware-specific optimizations that target the Neoverse V2 architecture. These optimizations are crucial for achieving high performance on Graviton4:

```output
-- ARM feature DOTPROD enabled
-- ARM feature SVE enabled
-- ARM feature MATMUL_INT8 enabled
-- ARM feature FMA enabled
-- ARM feature FP16_VECTOR_ARITHMETIC enabled
-- Adding CPU backend variant ggml-cpu: -mcpu=neoverse-v2+crc+sve2-aes+sve2-sha3+dotprod+i8mm+sve
```

These features enable advanced CPU instructions for faster inference:

- **DOTPROD: Dot Product**: hardware-accelerated dot product operations for neural network workloads
- **SVE: Scalable Vector Extension**: advanced vector processing capabilities that can handle variable-length vectors up to 2048 bits, providing significant performance improvements for matrix operations
- **MATMUL_INT8**: integer matrix multiplication units optimized for transformers
- **FMA**: fused multiply-add operations to speed up floating-point math
- **FP16 vector arithmetic**: 16-bit floating-point vector operations to reduce memory use without compromising precision

## Compile the project

```bash
cmake --build . --config Release -j16
```

This command compiles the Llama.cpp source code:

- `--build .` tells CMake to build the project in the current directory
- `--config Release` enables optimizations and strips debug symbols
- `-j16` runs the build with 16 parallel jobs, which speeds up compilation on multi-core systems like Graviton4

The build process compiles the C++ source code into executable binaries optimized for the Arm64 architecture. Compilation typically takes under a minute.

## What is built? 

After compilation, you'll find several key command-line tools in the `bin` directory:
- `llama-cli` - The main inference executable for running LLaMA models
- `llama-server` - A web server for serving model inference over HTTP
- `llama-quantize` - a tool for model quantization to reduce memory usage
- Various utility programs for model conversion and optimization

You can find more information in the llama.cpp [GitHub repository](https://github.com/ggml-org/llama.cpp/tree/master/tools).

These binaries are specifically optimized for ARM64 architecture and will provide excellent performance on your Graviton4 instance.

---
title: Building Llama.cpp
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this step, we'll build Llama.cpp from source. Llama.cpp is a high-performance C++ implementation of the LLaMA model that's optimized for inference on various hardware platforms, including ARM-based processors like Google Axion.

Even though AFM-4.5B has a custom model architecture, we're able to use the vanilla version of llama.cpp as the Arcee AI team has contributed the appropriate modeling code.

Here are all the steps.

## Step 1: Clone the Repository

```bash
git clone https://github.com/ggerganov/llama.cpp
```

This command clones the Llama.cpp repository from GitHub to your local machine. The repository contains the source code, build scripts, and documentation needed to compile the inference engine.

## Step 2: Navigate to the Project Directory

```bash
cd llama.cpp
```

Change into the llama.cpp directory where we'll perform the build process. This directory contains the CMakeLists.txt file and source code structure.

## Step 3: Configure the Build with CMake

```bash
cmake -B .
```

This command uses CMake to configure the build system:
- `-B .` specifies that the build files should be generated in the current directory
- CMake will detect your system's compiler, libraries, and hardware capabilities
- It will generate the appropriate build files (Makefiles on Linux) based on your system configuration

Note: The cmake output should include the information below, indicating that the build process will leverage the Neoverse V2 architecture's specialized instruction sets designed for AI/ML workloads. These optimizations are crucial for achieving optimal performance on Axion:

```bash
-- ARM feature DOTPROD enabled
-- ARM feature SVE enabled
-- ARM feature MATMUL_INT8 enabled
-- ARM feature FMA enabled
-- ARM feature FP16_VECTOR_ARITHMETIC enabled
-- Adding CPU backend variant ggml-cpu: -mcpu=neoverse-v2+crc+sve2-aes+sve2-sha3+dotprod+i8mm+sve
```

- **DOTPROD: Dot Product** - Hardware-accelerated dot product operations for neural network computations
- **SVE: Scalable Vector Extension** - Advanced vector processing capabilities that can handle variable-length vectors up to 2048 bits, providing significant performance improvements for matrix operations
- **MATMUL_INT8: Matrix multiplication units** - Dedicated hardware for efficient matrix operations common in transformer models, accelerating the core computations of large language models
- **FMA: Fused Multiply-Add - Optimized floating-point operations that combine multiplication and addition in a single instruction
- **FP16 Vector Arithmetic - Hardware support for 16-bit floating-point vector operations, reducing memory usage while maintaining good numerical precision

## Step 4: Compile the Project

```bash
cmake --build . --config Release -j16
```

This command compiles the Llama.cpp project:
- `--build .` tells CMake to build the project using the files in the current directory
- `--config Release` specifies a Release build configuration, which enables optimizations and removes debug symbols
- `-j16` runs the build with 16 parallel jobs, which speeds up compilation on multi-core systems like Axion.

The build process will compile the C++ source code into executable binaries optimized for your ARM64 architecture. This should only take a minute.

## What Gets Built

After successful compilation, you'll have several key command-line executables in the `bin` directory:
- `llama-cli` - The main inference executable for running LLaMA models
- `llama-server` - A web server for serving model inference over HTTP
- `llama-quantize` - a tool for model quantization to reduce memory usage
- Various utility programs for model conversion and optimization

You can find more information in the llama.cpp [GitHub repository](https://github.com/ggml-org/llama.cpp/tree/master/tools).

These binaries are specifically optimized for ARM64 architecture and will provide excellent performance on your Google Axion instance.
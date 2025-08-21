---
title: Build Llama.cpp on Google Cloud Axion Arm64
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build the Llama.cpp inference engine on Google Cloud Axion

In this step, you’ll build Llama.cpp from source. Llama.cpp is a high-performance C++ implementation of the LLaMA model, optimized for inference on multiple hardware platforms, including Arm64 processors such as Google Cloud Axion.

Although AFM-4.5B uses a custom architecture, you can use the standard Llama.cpp repository. Arcee AI has contributed the required modeling code upstream.

## Clone the Llama.cpp repository

```bash
git clone https://github.com/ggerganov/llama.cpp
```

This command clones the Llama.cpp repository from GitHub. The repository includes source code, build scripts, and documentation.

## Navigate to the Llama.cpp directory

```bash
cd llama.cpp
```

Move into the `llama.cpp` directory to run the build process. This directory contains the `CMakeLists.txt` file and all source code.

## Configure the build with CMake for Arm64

```bash
cmake -B .
```

This configures the build system using CMake:

- `-B .` generates build files in the current directory  
- CMake detects the system compiler, libraries, and hardware capabilities  
- It produces Makefiles (Linux) or platform-specific scripts for compilation  

On Google Cloud Axion, the output should show hardware-specific optimizations for the Neoverse V2 architecture:

```output
-- ARM feature DOTPROD enabled
-- ARM feature SVE enabled
-- ARM feature MATMUL_INT8 enabled
-- ARM feature FMA enabled
-- ARM feature FP16_VECTOR_ARITHMETIC enabled
-- Adding CPU backend variant ggml-cpu: -mcpu=neoverse-v2+crc+sve2-aes+sve2-sha3+dotprod+i8mm+sve
```

These optimizations enable advanced Arm64 CPU instructions:

- **DOTPROD**: hardware-accelerated dot product operations  
- **SVE (Scalable Vector Extension)**: advanced vector processing for large-scale matrix operations  
- **MATMUL_INT8**: optimized integer matrix multiplication for transformers  
- **FMA**: fused multiply-add for faster floating-point math  
- **FP16 vector arithmetic**: reduced memory use with half-precision floats  

## Compile the project

```bash
cmake --build . --config Release -j16
```

This compiles Llama.cpp with the following options:

- `--build .` builds in the current directory  
- `--config Release` enables compiler optimizations  
- `-j16` runs 16 parallel jobs for faster compilation on multi-core Axion systems  

The build produces Arm64-optimized binaries in under a minute.

## Key Llama.cpp binaries after compilation

After compilation, you’ll find key tools in the `bin` directory:

- `llama-cli`: main inference executable  
- `llama-server`: HTTP server for model inference  
- `llama-quantize`: tool for quantization to reduce memory usage  
- Additional utilities for model conversion and optimization  

See the [Llama.cpp GitHub repository](https://github.com/ggml-org/llama.cpp/tree/master/tools) for details.

These binaries are optimized for Arm64 and provide excellent performance on Google Cloud Axion.

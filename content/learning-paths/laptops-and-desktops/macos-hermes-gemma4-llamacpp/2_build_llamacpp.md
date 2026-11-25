---
title: Build llama.cpp from source for macOS
description: Verify your Apple silicon macOS environment and compile llama.cpp from source with Metal, Apple Accelerate, and Arm KleidiAI to unlock SME-accelerated CPU inference on M4 and M5 Macs.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Verify your Apple silicon environment

Before compiling llama.cpp, confirm your macOS version, CPU architecture, performance-core count, and unified memory capacity.

Check the architecture, macOS release, chip model, core topology, and memory size:

```bash
uname -m
sw_vers
sysctl -n machdep.cpu.brand_string
sysctl hw.perflevel0.physicalcpu hw.perflevel1.physicalcpu hw.physicalcpu hw.memsize
```

Confirm that `uname -m` prints `arm64`, note `hw.perflevel0.physicalcpu` (your performance-core count, such as `8` on an Apple M4 Pro), and check that `hw.memsize` is at least 16 GB (`17179869184` bytes or higher). You can also check whether your Apple silicon Mac (such as an M4 or M5 Mac) exposes Arm Scalable Matrix Extension (SME) and SME2 features:

```bash
sysctl -a 2>/dev/null | grep -E "hw.optional.arm.FEAT_SME|hw.optional.arm.FEAT_I8MM|hw.optional.arm.FEAT_DotProd"
```

The output is similar to:

```output
hw.optional.arm.FEAT_DotProd: 1
hw.optional.arm.FEAT_I8MM: 1
hw.optional.arm.FEAT_SME: 1
hw.optional.arm.FEAT_SME2: 1
```

## Install build prerequisites

Confirm that Xcode Command Line Tools, CMake, and Git are installed:

```bash
xcode-select -p
clang --version
cmake --version
git --version
```

If any tool is missing, install Xcode Command Line Tools with `xcode-select --install`. Install CMake and Git with Homebrew using `brew install cmake git`, or download CMake directly from the [CMake download page](https://cmake.org/download/).

{{% notice Note %}}
You can install a prebuilt package with `brew install llama.cpp`, which includes Metal support. However, compiling from the latest upstream repository includes newer Metal GPU optimizations, while enabling Arm KleidiAI (`-DGGML_CPU_KLEIDIAI=ON`) delivers much faster CPU-side prefill with SME on M4 and M5 Macs.
{{% /notice %}}

## Clone and build llama.cpp

Create a dedicated project directory and clone the official llama.cpp repository:

```bash
mkdir -p ~/hermes-gemma4 && cd ~/hermes-gemma4
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
```

Configure the CMake build for optimal Apple silicon performance. Enable Metal GPU offloading (`-DGGML_METAL=ON`), embed compiled Metal shaders directly into the binaries (`-DGGML_METAL_EMBED_LIBRARY=ON`), link Apple's Accelerate framework (`-DGGML_ACCELERATE=ON`), and enable Arm KleidiAI microkernels (`-DGGML_CPU_KLEIDIAI=ON`). On macOS `arm64`, CMake automatically detects supported Arm extensions including dot-product, `i8mm`, and SME when available:

```bash
cmake -B build \
  -DCMAKE_BUILD_TYPE=Release \
  -DGGML_METAL=ON \
  -DGGML_METAL_EMBED_LIBRARY=ON \
  -DGGML_ACCELERATE=ON \
  -DGGML_CPU_KLEIDIAI=ON
```

Inspect the CMake configuration lines to confirm that `HAVE_SME - Success`, `Using KleidiAI optimized kernels if applicable`, `Accelerate framework found`, and `Metal framework found` appear.

Compile llama.cpp across all available cores:

```bash
cmake --build build --config Release -j $(sysctl -n hw.ncpu)
```

## Validate the compiled binaries

Verify that `llama-server` and `llama-bench` built cleanly and detect your Metal GPU:

```bash
./build/bin/llama-server --version
./build/bin/llama-bench --list-devices
```

The output is similar to:

```output
version: 1.0.0-dev (build 1, commit 33aeb17)
built with AppleClang 21.0.0.21000401 for Darwin arm64
...
ggml_metal_device_init: GPU name:   MTL0 (Apple M4 Pro)
ggml_metal_device_init: GPU family: MTLGPUFamilyApple9  (1009)
ggml_metal_device_init: GPU family: MTLGPUFamilyMetal4  (5002)
ggml_metal_device_init: simdgroup reduction   = true
ggml_metal_device_init: simdgroup matrix mul. = true
ggml_metal_device_init: has unified memory    = true
...
Available devices:
  MTL0: Apple M4 Pro (18186 MiB, 18185 MiB free)
  BLAS: Accelerate (0 MiB, 0 MiB free)
```

Confirm that `MTL0` lists your Apple silicon GPU and `BLAS: Accelerate` appears under `Available devices:`.

## What you've accomplished and what's next

You've verified your Apple silicon macOS environment, enabled Metal, Apple Accelerate, and Arm KleidiAI in CMake, and compiled llama.cpp from source.

Next, you'll download the Gemma 4 E4B GGUF model from Hugging Face and benchmark Metal GPU performance against CPU-only runs.

---
title: Build llama.cpp from source for NVIDIA DGX Spark
description: Verify your NVIDIA DGX Spark environment and compile llama.cpp from source with CUDA 13 Blackwell (sm_121a) and Armv9.2 KleidiAI optimizations.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Verify your DGX Spark environment

Before compiling llama.cpp, confirm your CPU architecture, heterogeneous Grace core topology, unified memory capacity, and CUDA 13 toolkit.

Check the CPU architecture, core topology, and available memory:

```bash
uname -m
lscpu | grep -E "Model name|CPU\(s\)|Core|Socket"
free -h
```

Confirm that `uname -m` prints `aarch64` and that `lscpu` lists 20 CPU cores: 10 Arm Cortex-X925 performance cores and 10 Arm Cortex-A725 efficiency cores. You can inspect which logical CPU IDs map to Cortex-X925 versus Cortex-A725:

```bash
lscpu -e=CPU,CORE,MAXMHZ,MODELNAME
```

The output is similar to:

```output
CPU CORE    MAXMHZ MODELNAME
  0    0 2808.0000 Cortex-A725
...
  5    0 3900.0000 Cortex-X925
...
 15    5 3900.0000 Cortex-X925
 19    9 3900.0000 Cortex-X925
```

Confirm that the NVIDIA GB10 GPU driver and CUDA 13 compiler are available. Add `/usr/local/cuda/bin` to your `PATH` if `nvcc` isn't already on your default path:

```bash
export PATH=/usr/local/cuda/bin:$PATH
nvidia-smi
nvcc --version
```

The output is similar to:

```output
| NVIDIA-SMI 580.178.04             Driver Version: 580.178.04     CUDA Version: 13.0     |
...
|   0  NVIDIA GB10                    On  |   0000000F:01:00.0 Off |                  N/A |
...
Cuda compilation tools, release 13.0, V13.0.88
```

## Install build prerequisites

Update your package index and install the compiler toolchain, CMake, Git, `libcurl` development headers, and Python virtual environment tools:

```bash
sudo apt update
sudo apt install -y build-essential cmake git libcurl4-openssl-dev python3-venv python3-pip
```

## Clone and build llama.cpp

Create a dedicated project directory and clone the official llama.cpp repository:

```bash
mkdir -p ~/hermes-gemma4 && cd ~/hermes-gemma4
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
```

Configure CMake to build both the Blackwell CUDA GPU backend and an optimized Armv9.2 KleidiAI CPU backend in one binary set:

```bash
export PATH=/usr/local/cuda/bin:$PATH

cmake -B build \
  -DCMAKE_BUILD_TYPE=Release \
  -DGGML_CUDA=ON \
  -DCMAKE_CUDA_ARCHITECTURES=121a-real \
  -DGGML_NATIVE=OFF \
  -DGGML_CPU_ARM_ARCH=armv9-a+dotprod+i8mm+bf16+sve+sve2+fp16 \
  -DGGML_OPENMP=ON \
  -DGGML_CPU_KLEIDIAI=ON
```

Inspect the CMake configuration output to confirm that all Armv9.2 CPU feature checks pass alongside CUDA 13 Blackwell (`121a-real`) and Flash Attention:

```output
-- Checking for ARM features using flags:
--   -march=armv9-a+dotprod+i8mm+bf16+sve+sve2+fp16
-- Performing Test HAVE_DOTPROD - Success
-- Performing Test HAVE_SVE - Success
-- Performing Test HAVE_MATMUL_INT8 - Success
-- Performing Test HAVE_FMA - Success
-- Performing Test HAVE_FP16_VECTOR_ARITHMETIC - Success
-- Using KleidiAI optimized kernels if applicable
-- CUDA Toolkit found
-- Using CMAKE_CUDA_ARCHITECTURES=121a-real CMAKE_CUDA_ARCHITECTURES_NATIVE=121a-real
-- FlashAttention K-V type combinations: f16-f16;q4_0-q4_0;q8_0-q8_0;bf16-bf16;f8_e4m3-f8_e4m3
-- Including CUDA backend
```

{{% notice Important %}}
Do not rely on `-DGGML_NATIVE=ON` with Ubuntu 24.04's default GNU Compiler Collection (GCC) 13.3.0 on DGX Spark. GCC 13 predates Cortex-X925 and Cortex-A725 CPU identification, so `-mcpu=native` leaves `-march` empty and causes `HAVE_DOTPROD`, `HAVE_MATMUL_INT8`, `HAVE_SVE`, and `HAVE_FP16_VECTOR_ARITHMETIC` feature probes to fail. Passing `-DGGML_NATIVE=OFF` with an explicit `-DGGML_CPU_ARM_ARCH=armv9-a+dotprod+i8mm+bf16+sve+sve2+fp16` enables every Grace Armv9.2 instruction extension and Arm KleidiAI microkernel.
{{% /notice %}}

Here is what each key CMake option controls on DGX Spark:

| Flag | Purpose |
|---|---|
| `-DGGML_CUDA=ON` | Enables the CUDA backend for NVIDIA GB10 GPU offloading with CUDA Graphs and Flash Attention enabled by default |
| `-DCMAKE_CUDA_ARCHITECTURES=121a-real` | Compiles Blackwell GB10 (`sm_121a`) device code directly, unlocking architecture-specific Blackwell tensor instructions |
| `-DGGML_NATIVE=OFF -DGGML_CPU_ARM_ARCH=armv9-a+dotprod+i8mm+bf16+sve+sve2+fp16` | Explicitly enables Armv9.2 SIMD, dot-product, INT8 matrix multiply (`i8mm`), BFloat16, FP16, and SVE/SVE2 on Grace |
| `-DGGML_OPENMP=ON` | Enables OpenMP multi-threading for CPU-side execution |
| `-DGGML_CPU_KLEIDIAI=ON` | Compiles Arm KleidiAI quantized matrix microkernels into `libggml-cpu.so` |

Compile llama.cpp across all 20 Grace CPU cores:

```bash
cmake --build build --config Release -j $(nproc)
```

## Validate the compiled binaries

Verify that `llama-server` and `llama-bench` built cleanly, detect the NVIDIA GB10 GPU, link against CUDA 13 libraries, and include Arm KleidiAI CPU symbols:

```bash
./build/bin/llama-server --version
./build/bin/llama-bench --list-devices
ldd ./build/bin/llama-server | grep -E "cuda|cublas"
nm -D ./build/bin/libggml-cpu.so | grep -i kleidi | head -n 6
```

The output is similar to:

```output
version: 1.1.0-dev (build 12763, commit 5917b39ff)
built with GNU 13.3.0 for Linux aarch64
ggml_cuda_init: found 1 CUDA devices (Total VRAM: 124607 MiB):
  Device 0: NVIDIA GB10, compute capability 12.1, VMM: yes, VRAM: 124607 MiB
Available devices:
  CUDA0: NVIDIA GB10 (124607 MiB, 25274 MiB free)
	libggml-cuda.so.1 => /home/user/hermes-gemma4/llama.cpp/build/bin/libggml-cuda.so.1
	libcudart.so.13 => /usr/local/cuda/targets/sbsa-linux/lib/libcudart.so.13
	libcublas.so.13 => /usr/local/cuda/targets/sbsa-linux/lib/libcublas.so.13
	libcublasLt.so.13 => /usr/local/cuda/targets/sbsa-linux/lib/libcublasLt.so.13
	libcuda.so.1 => /lib/aarch64-linux-gnu/libcuda.so.1
00000000000d01f0 T ggml_backend_cpu_kleidiai_buffer_type
00000000000d7100 T _Z28ggml_kleidiai_select_kernels11cpu_featurePK11ggml_tensor
00000000000d77c4 T _Z32ggml_kleidiai_select_kernels_f3211cpu_feature
00000000000d7630 T _Z33ggml_kleidiai_select_kernels_q4_011cpu_feature
00000000000d7720 T _Z33ggml_kleidiai_select_kernels_q4_k11cpu_feature
00000000000d7740 T _Z33ggml_kleidiai_select_kernels_q8_011cpu_feature
```

Confirm that `CUDA0: NVIDIA GB10` appears with `compute capability 12.1` and that `ggml_kleidiai_select_kernels` symbols appear in `libggml-cpu.so`.

## What you've accomplished and what's next

You've verified your NVIDIA DGX Spark environment, enabled CUDA 13 Blackwell (`sm_121a`) and explicit Armv9.2 KleidiAI flags in CMake, and compiled llama.cpp from source.

Next, you'll download Gemma 4 E4B, 26B-A4B (MoE), and 31B from Hugging Face and benchmark Blackwell GPU versus Grace CPU performance.

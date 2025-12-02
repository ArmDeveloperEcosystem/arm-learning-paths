---
title: Cross-Compile ExecuTorch for the AArch64 platform
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you'll cross-compile ExecuTorch for an Arm64 (AArch64) target with XNNPACK and KleidiAI support. Cross-compiling builds all binaries and libraries for your Arm device, even if your development system uses x86_64. This process lets you run and test ExecuTorch on Arm hardware, taking advantage of Arm-optimized performance features.

## Install the cross-compilation toolchain
On your x86_64 Linux host, install the GNU Arm cross-compilation toolchain along with Ninja, which is a fast build backend commonly used by CMake:
```bash
sudo apt install gcc-aarch64-linux-gnu g++-aarch64-linux-gnu ninja-build -y
```

## Run CMake configuration 

Use CMake to configure the ExecuTorch build for the AArch64 target.

The command below enables all key runtime extensions, developer tools, and optimized backends including XNNPACK and KleidiAI:

```bash 

cd $WORKSPACE
mkdir -p build-arm64
cd build-arm64

cmake -GNinja \
    -DCMAKE_BUILD_TYPE=Debug \
    -DCMAKE_SYSTEM_NAME=Linux \
    -DCMAKE_SYSTEM_PROCESSOR=aarch64 \
    -DCMAKE_C_COMPILER=aarch64-linux-gnu-gcc \
    -DCMAKE_CXX_COMPILER=aarch64-linux-gnu-g++ \
    -DCMAKE_FIND_ROOT_PATH_MODE_PROGRAM=NEVER \
    -DCMAKE_FIND_ROOT_PATH_MODE_LIBRARY=BOTH \
    -DCMAKE_FIND_ROOT_PATH_MODE_INCLUDE=ONLY \
    -DEXECUTORCH_BUILD_EXTENSION_DATA_LOADER=ON \
    -DEXECUTORCH_BUILD_EXTENSION_FLAT_TENSOR=ON \
    -DEXECUTORCH_BUILD_EXTENSION_MODULE=ON \
    -DEXECUTORCH_BUILD_EXTENSION_NAMED_DATA_MAP=ON \
    -DEXECUTORCH_BUILD_EXTENSION_TENSOR=ON \
    -DEXECUTORCH_BUILD_KERNELS_OPTIMIZED=ON \
    -DEXECUTORCH_BUILD_XNNPACK=ON \
    -DEXECUTORCH_BUILD_DEVTOOLS=ON \
    -DEXECUTORCH_ENABLE_EVENT_TRACER=ON \
    -DEXECUTORCH_ENABLE_LOGGING=ON \
    -DEXECUTORCH_LOG_LEVEL=debug \
    -DEXECUTORCH_XNNPACK_ENABLE_KLEIDI=ON \
    ../executorch

```

## Key Build Options

| **CMake Option**                            | **Description**                                                                                                                                                    |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `EXECUTORCH_BUILD_XNNPACK`                  | Builds the XNNPACK backend, which provides highly optimized CPU operators (such as GEMM and convolution) for Arm64 platforms.                                 |
| `EXECUTORCH_XNNPACK_ENABLE_KLEIDI`          | Enables Arm KleidiAI acceleration for XNNPACK kernels, providing further performance improvements on Armv8.2+ CPUs.                                            |
| `EXECUTORCH_BUILD_DEVTOOLS`                 | Builds developer tools such as the ExecuTorch Inspector and diagnostic utilities for profiling and debugging.                                                  |
| `EXECUTORCH_BUILD_EXTENSION_MODULE`         | Builds the Module API extension, which provides a high-level abstraction for model loading and execution using `Module` objects.                               |
| `EXECUTORCH_BUILD_EXTENSION_TENSOR`         | Builds the Tensor API extension, providing convenience functions for creating, manipulating, and managing tensors in C++ runtime.                              |
| `EXECUTORCH_BUILD_KERNELS_OPTIMIZED`        | Enables building optimized kernel implementations for better performance on supported architectures.                                                           |
| `EXECUTORCH_ENABLE_EVENT_TRACER`            | Enables the event tracing feature, which records performance and operator timing information for runtime analysis.                                             |



## Build ExecuTorch 
Once CMake configuration completes successfully, compile the ExecuTorch runtime and its associated developer tools:

```bash 
cmake --build . -j$(nproc)
```
CMake invokes Ninja to perform the actual build, generating both static libraries and executables for the AArch64 target.

## Locate the executor_runner binary
If the build completes successfully, you should see the main benchmarking and profiling utility, executor_runner, under:

```output
build-arm64/executor_runner
You’ll use `executor_runner` in later sections to execute and profile ExecuTorch models directly from the command line on your Arm64 target. This standalone binary lets you run models using the XNNPACK backend with KleidiAI acceleration, making it easy to benchmark and analyze performance on Arm devices.


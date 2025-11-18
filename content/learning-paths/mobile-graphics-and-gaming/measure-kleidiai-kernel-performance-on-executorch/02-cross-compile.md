---
title: Cross-Compile ExecuTorch for the Aarch64 platform
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---


This section describes how to cross-compile ExecuTorch for an AArch64 target platform with XNNPACK and KleidiAI support enabled.
All commands below are intended to be executed on an x86-64 Linux host with an appropriate cross-compilation toolchain installed (e.g., aarch64-linux-gnu-gcc).


### Run CMake Configuration 

Use CMake to configure the ExecuTorch build for Aarch64. The example below enables key extensions, developer tools, and XNNPACK with KleidiAI acceleration: 

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

#### Key Build Options

| **CMake Option**                            | **Description**                                                                                                                                                    |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `EXECUTORCH_BUILD_XNNPACK`                  | Builds the **XNNPACK backend**, which provides highly optimized CPU operators (GEMM, convolution, etc.) for Arm64 platforms.                                 |
| `EXECUTORCH_XNNPACK_ENABLE_KLEIDI`          | Enables **Arm KleidiAI** acceleration for XNNPACK kernels, providing further performance improvements on Armv8.2+ CPUs.                                            |
| `EXECUTORCH_BUILD_DEVTOOLS`                 | Builds **developer tools** such as the ExecuTorch Inspector and diagnostic utilities for profiling and debugging.                                                  |
| `EXECUTORCH_BUILD_EXTENSION_MODULE`         | Builds the **Module API** extension, which provides a high-level abstraction for model loading and execution using `Module` objects.                               |
| `EXECUTORCH_BUILD_EXTENSION_TENSOR`         | Builds the **Tensor API** extension, providing convenience functions for creating, manipulating, and managing tensors in C++ runtime.                              |
| `EXECUTORCH_BUILD_KERNELS_OPTIMIZED`        | Enables building **optimized kernel implementations** for better performance on supported architectures.                                                           |
| `EXECUTORCH_ENABLE_EVENT_TRACER`            | Enables the **event tracing** feature, which records performance and operator timing information for runtime analysis.                                             |



### Build ExecuTorch 

```bash 
cmake --build . -j$(nproc)

```

If the build completes successfully, you should find the executor_runner binary under the directory:

```bash
build-arm64/executor_runner

```

This binary can be used to run ExecuTorch models on the ARM64 target device using the XNNPACK backend with KleidiAI acceleration.


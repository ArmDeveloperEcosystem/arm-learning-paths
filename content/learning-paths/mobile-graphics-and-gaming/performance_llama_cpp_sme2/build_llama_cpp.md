---
title: Build llama.cpp with KleidiAI and SME2 enabled
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build llama.cpp with KleidiAI and SME2 enabled
For convenience, llama.cpp is statically linked. We use aarch64 GCC cross compile toolchain, *aarch64-none-linux-gnu-* to build the project. To support SME2, GCC compiler version 14.2 and onwards is required. The toolchain can be downloaded [here](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads) . 

The llama.cpp with Tag b7611 is used in this tutorial, newer versions should also work but they are not tested. 

After downloading the llama.cpp source code [here](https://github.com/ggml-org/llama.cpp/releases/tag/b7610), create a new directory *build* under the llama.cpp root directory and change to the new directory,

```bash
cd ~/llama.cpp
mkdir build && cd build
```
Next, configure the project,

```bash
cmake .. \
  -DCMAKE_SYSTEM_NAME=Linux \
  -DCMAKE_SYSTEM_PROCESSOR=arm \
  -DCMAKE_C_COMPILER=aarch64-linux-gnu-gcc \
  -DCMAKE_CXX_COMPILER=aarch64-linux-gnu-g++ \
  -DLLAMA_NATIVE=OFF \
  -DLLAMA_F16C=OFF \
  -DLLAMA_GEMM_ARM=ON \
  -DBUILD_SHARED_LIBS=OFF \
  -DCMAKE_EXE_LINKER_FLAGS="-static -g" \
  -DGGML_OPENMP=OFF \
  -DCMAKE_C_FLAGS=" -march=armv8.7-a+sve+i8mm+dotprod+sme2 -g" \
  -DCMAKE_CXX_FLAGS=" -march=armv8.7-a+sve+i8mm+dotprod+sme2 -g" \
  -DLLAMA_BUILD_TESTS=OFF  \
  -DLLAMA_BUILD_EXAMPLES=ON \
  -DLLAMA_CURL=OFF \
  -DGGML_CPU_KLEIDIAI=ON 
```
Set CMAKE_C_COMPILER and CMAKE_CXX_COMPILER to your cross compiler path. Make sure that *-march* in CMAKE_C_FLAGS and CMAKE_CXX_FLAGS includes "+sme2".

The *-static* and *-g* options are specified to produce a statically linked executable, in oder to run on different Arm64 Linux/Android environments and include debug information.

Next, build the project,

```bash
cd ~/llama.cpp/build
cmake --build ./ --config Release -j $(nproc)
```
After the building process completes, you can find the application,*llama-cli*,in the ~/llama.cpp/build/bin/ directory.

To enable SME2 microkernels, you must set following environment variable before running the application.

```bash 
GGML_KLEIDIAI_SME="1"
```
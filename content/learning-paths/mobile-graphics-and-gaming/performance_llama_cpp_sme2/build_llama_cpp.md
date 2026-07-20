---
title: Build llama.cpp with KleidiAI and SME2 enabled
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you set up a GCC cross-compile toolchain and build a statically linked `llama-cli` binary with KleidiAI and SME2 enabled.

For convenience, llama.cpp is statically linked. You use the aarch64 GCC cross compile toolchain, `aarch64-none-linux-gnu-`, to build the project. To support SME2, GCC compiler version 14.2 or later is required.

The build uses the Linux-hosted Arm GNU Toolchain. If you are working on macOS or Windows, run these commands in a Linux environment (for example, a Linux VM, container, or a Linux development machine).

## Install the toolchain

Start by downloading and unpacking the Arm GNU Toolchain (GCC 14.2) for your host architecture:

```bash
TOOLCHAIN_VER="14.2.rel1"
mkdir -p "$HOME/toolchains" && cd "$HOME/toolchains"

HOST_ARCH="$(uname -m)"
if [ "$HOST_ARCH" = "x86_64" ]; then
  TOOLCHAIN_TAR="arm-gnu-toolchain-${TOOLCHAIN_VER}-x86_64-aarch64-none-linux-gnu.tar.xz"
elif [ "$HOST_ARCH" = "aarch64" ]; then
  TOOLCHAIN_TAR="arm-gnu-toolchain-${TOOLCHAIN_VER}-aarch64-aarch64-none-linux-gnu.tar.xz"
else
  echo "Unsupported host architecture: $HOST_ARCH" >&2
  exit 1
fi

curl -L -O "https://developer.arm.com/-/media/Files/downloads/gnu/${TOOLCHAIN_VER}/binrel/${TOOLCHAIN_TAR}"
tar -xf "${TOOLCHAIN_TAR}"

export PATH="$PWD/${TOOLCHAIN_TAR%.tar.xz}/bin:$PATH"
```

Confirm the installation succeeded by printing the compiler version:

```bash
aarch64-none-linux-gnu-gcc --version
```

## Clone the llama.cpp repository

This Learning Path uses llama.cpp tag b7610. Newer versions should also work but are not tested.

Download the llama.cpp source code and check out that tag:

```bash
cd $HOME
git clone --depth 1 --branch b7610 https://github.com/ggml-org/llama.cpp.git
```

Create a new `build` directory under the llama.cpp root directory and change to it:

```bash
cd $HOME/llama.cpp
mkdir build && cd build
```

## Compile llama-cli for Android

Configure the project. The key flags enable KleidiAI support (`-DGGML_CPU_KLEIDIAI=ON`) and SME2 instructions (`-march=...+sme2`), produce a statically linked binary (`-static`) that runs across Android and Linux environments, and include debug symbols (`-g`) for profiling:

```bash
cmake .. \
  -DCMAKE_SYSTEM_NAME=Linux \
  -DCMAKE_SYSTEM_PROCESSOR=arm \
  -DCMAKE_C_COMPILER=aarch64-none-linux-gnu-gcc \
  -DCMAKE_CXX_COMPILER=aarch64-none-linux-gnu-g++ \
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

{{% notice Note %}}
Set `CMAKE_C_COMPILER` and `CMAKE_CXX_COMPILER` to your cross compiler path if it is not already in your `PATH`. Make sure that `-march` in `CMAKE_C_FLAGS` and `CMAKE_CXX_FLAGS` includes `+sme2`.
{{% /notice %}}


The `-static` and `-g` options are specified to produce a statically linked executable, in order to run on different Arm64 Linux/Android environments and include debug information.

Build the project:

```bash
cd $HOME/llama.cpp/build
cmake --build ./ --config Release -j $(nproc)
```
After the build completes, confirm that `llama-cli` exists in the binary directory:

```bash 
ls -la $HOME/llama.cpp/build/bin | grep llama-cli
```

## What you've accomplished and what's next

In this section:
- You installed the Arm GNU Toolchain (GCC 14.2) and configured it for aarch64 cross-compilation
- You built a statically linked `llama-cli` binary with KleidiAI and SME2 enabled, ready to run on your Android target

In the next section, you'll transfer the binary and model to the device and compare inference performance with SME2 on and off.
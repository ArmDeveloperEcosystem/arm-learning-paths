---
title: Build llama.cpp with KleidiAI and SME2 enabled
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you set up a GCC cross-compile toolchain and build a statically linked `llama-cli` binary with KleidiAI and SME2 enabled.

For convenience, llama.cpp is statically linked. You use the aarch64 GCC cross compile toolchain, *aarch64-none-linux-gnu-*, to build the project. To support SME2, GCC compiler version 14.2 and onwards is required.

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

Verify the installation was successful by printing the toolchain version:

```bash
aarch64-none-linux-gnu-gcc --version
```

## Clone the llama.cpp repository

The llama.cpp with tag b7610 is used in this tutorial. Newer versions should also work, but they are not tested.

Next, download the llama.cpp source code and check out the tag used in this tutorial:

```bash
cd $HOME
git clone --depth 1 --branch b7610 https://github.com/ggml-org/llama.cpp.git
```

Create a new directory *build* under the llama.cpp root directory and change to the new directory:

```bash
cd $HOME/llama.cpp
mkdir build && cd build
```

## Compile the binary 

Next, configure the project using the following command:

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

Next, build the project,

```bash
cd $HOME/llama.cpp/build
cmake --build ./ --config Release -j $(nproc)
```
After the building process completes, verify that *llama-cli* exists in the binary directory:

```bash 
ls -la $HOME/llama.cpp/build/bin | grep llama-cli
```

Now that you have a `llama-cli` build with KleidiAI enabled, move on to the next section to run the model on your SME2 device and observe the performance impact when you enable the microkernels.
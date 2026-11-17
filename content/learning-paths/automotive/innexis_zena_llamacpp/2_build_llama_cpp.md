---
title: Build llama.cpp in the Zena CSS guest
description: Build a pinned llama.cpp revision for CPU inference in the Zena CSS Linux guest.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build llama.cpp in the Zena CSS guest

Build the tested llama.cpp revision in the Zena CSS guest. Keep the source and build output in the work directory from the previous page.

## Make CMake available

Check whether CMake is already installed. In the tested Zena guest, the command returned:

```bash
cmake --version
```

```output
sh: cmake: command not found
```

Use the [Kitware CMake 3.28.6 release](https://github.com/Kitware/CMake/releases/tag/v3.28.6) for Linux AArch64 in the Zena work directory. This does not change the guest's system packages:

```bash
cd "$LP2_WORK_DIR" &&
wget -O cmake-3.28.6-linux-aarch64.tar.gz.part \
    https://github.com/Kitware/CMake/releases/download/v3.28.6/cmake-3.28.6-linux-aarch64.tar.gz &&
    mv cmake-3.28.6-linux-aarch64.tar.gz.part cmake-3.28.6-linux-aarch64.tar.gz &&
sha256sum cmake-3.28.6-linux-aarch64.tar.gz &&
tar -xzf cmake-3.28.6-linux-aarch64.tar.gz &&
export PATH="$LP2_WORK_DIR/cmake-3.28.6-linux-aarch64/bin:$PATH" &&
cmake --version
```

The Zena download completed with a 53,907,530-byte archive. The hash and version commands returned:

```output
7909cc2128ce9442c63ce674a0bfb0e4f4ce04cef667d887e15ad5670d594ba7  cmake-3.28.6-linux-aarch64.tar.gz
cmake version 3.28.6
```

The SHA-256 value identifies the downloaded file used in this run; it has not been checked against a publisher-supplied checksum. If the download or extraction fails on your guest, keep the error output and stop before the llama.cpp build. Keep this shell open so the CMake path remains available.

## Get the source at a fixed revision

Clone llama.cpp and check out the full commit used in the tested Zena run:

```bash
LP2_LLAMA_COMMIT=b86d2f07542b29ab099aed34fd6b6d1b2fd4b81c
git clone https://github.com/ggml-org/llama.cpp.git "$LP2_WORK_DIR/llama.cpp" &&
cd "$LP2_WORK_DIR/llama.cpp" &&
git checkout --detach "$LP2_LLAMA_COMMIT" &&
git rev-parse HEAD
```

The final command returned the requested full commit:

```output
b86d2f07542b29ab099aed34fd6b6d1b2fd4b81c
```

If your checkout reports another commit, stop before configuring the build.

## Configure a CPU build

In the same **Zena guest shell**, configure the pinned source for a CPU build:

```bash
cd "$LP2_WORK_DIR/llama.cpp"
cmake -B build \
    -DCMAKE_BUILD_TYPE=Release \
    -DGGML_NATIVE=ON \
    -DLLAMA_CURL=OFF \
    -DBUILD_SHARED_LIBS=OFF
```

This CMake invocation was used in the tested Zena run. Its output reported GNU 14.2.0 for C and C++, included the CPU backend, and ended with:

```output
-- Configuring done (3.3s)
-- Generating done (0.2s)
-- Build files have been written to: /root/zena-llamacpp/llama.cpp/build
```

CMake also reported that OpenMP was not found. That warning did not prevent configuration; it does not establish how many threads a later inference run will use. The supplied excerpt does not include a numeric exit status. Stop if configuration reports an error.

## Build and identify llama.cpp

After configuration succeeds, compile the CPU binary:

```bash
cmake --build build --config Release -j4
./build/bin/llama-cli --version
```

The tested Zena build output reached `Built target llama-cli`, and the binary returned:

```output
version: 0.6.0-dev (build 11482, commit b86d2f075)
built with GNU 14.2.0 for Linux aarch64
```

The full build also downloaded UI assets from Hugging Face during compilation, so that build required network access. `-j4` limits build jobs; it does not set the virtual platform's CPU count. The supplied excerpts do not include a complete build log or numeric exit status. If the build fails, save its error output and check the work filesystem before retrying.

## What you have learned

You have a source revision and a binary identity to associate with the inference result. Keep `LP2_WORK_DIR` available in this shell for the next page.

---
title: Build MNN and prepare an Omni model on Armv9
weight: 3
layout: learningpathall
---

## Get source and native build

Create a working directory under your home folder:

```bash
cd ~
mkdir -p ~/mnn_lp
cd ~/mnn_lp
```

Clone MNN and build:

```bash
git clone https://github.com/alibaba/MNN.git
cd MNN

rm -rf build
mkdir build && cd build

cmake .. \
  -DMNN_BUILD_SHARED=ON \
  -DMNN_BUILD_LLM=ON \
  -DMNN_BUILD_AUDIO=ON \
  -DMNN_BUILD_LLM_OMNI=ON \
  -DMNN_LOW_MEMORY=ON \
  -DMNN_KLEIDIAI=ON

make -j$(nproc)
```

**Key CMake options:**

- `MNN_BUILD_LLM=ON` – enables LLM support
- `MNN_BUILD_AUDIO=ON` – enables audio features needed for Omni
- `MNN_BUILD_LLM_OMNI=ON` – enables multimodal Omni support
- `MNN_LOW_MEMORY=ON` – uses lower memory configurations where possible
- `MNN_KLEIDIAI=ON` – enables KleidiAI-related optimizations on supported Arm platforms

Verify that `llm_demo` was built:

```bash
ls -l ~/mnn_lp/MNN/build/llm_demo
```


## Avoid library mismatch

On systems with multiple MNN builds, a common pitfall is a **binary from one build tree** loading a **shared library from another**.

Check which libraries `llm_demo` will use:

```bash
cd ~/mnn_lp/MNN/build
ldd ./llm_demo
```

Ensure that `libMNN.so` and related libraries point to your **current build directory**.

If you see a mismatch, set `LD_LIBRARY_PATH` explicitly:

```bash
export LD_LIBRARY_PATH=~/mnn_lp/MNN/build:$LD_LIBRARY_PATH
```

Re-run `ldd` or `./llm_demo` to confirm the correct shared libraries are used.


## Download a prebuilt MNN Omni model

This Learning Path assumes you have a prebuilt Omni model package, for example:

```bash
~/mnn_lp/Qwen2.5-Omni-7B-MNN
```

The directory should contain at least a `config.json` and the associated model files.

Verify the config path:

```bash
ls -l ~/mnn_lp/Qwen2.5-Omni-7B-MNN/config.json
```

**Important:** This is an **MNN-ready Omni package**. You **do not** need to export from PyTorch or perform additional quantization.


## Checkpoint

You should be able to start `llm_demo` with your config:

```bash
cd ~/mnn_lp/MNN/build
./llm_demo ~/mnn_lp/Qwen2.5-Omni-7B-MNN/config.json
```

If the binary starts without `undefined symbol` or library errors, you are ready for the next module.

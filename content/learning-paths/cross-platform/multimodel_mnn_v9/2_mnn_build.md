---
title: Build MNN and prepare an Omni model on Armv9
weight: 3
layout: learningpathall
---

## Introduction

In this section, you will build **MNN** natively on your Armv9 Linux system and verify that the `llm_demo` binary can load a **prebuilt Omni MNN model package**. This sets up everything needed for the text, vision, and audio demos in later sections.

This section uses a native **CPU-only** MNN build on Armv9. That is a deliberate design choice, not a fallback. The goal is to show how a compact, reproducible, deployment-friendly software stack can run directly on an Armv9 CPU without depending on a discrete GPU or separate accelerator.

At the end of this module, you will have:

- a working `llm_demo` binary
- a validated model directory that includes `config.json`
- a runtime environment that resolves the correct MNN shared libraries
- the required Omni model files available locally

## Create a workspace

Create a working directory under your home folder:

```bash
mkdir -p ~/mnn
cd ~/mnn
```

## Why build natively on Armv9 first

This Learning Path uses a native build on the target Armv9 system before introducing any cross-compilation workflow. Building directly on the target helps reduce environment drift, makes library and toolchain issues easier to diagnose, and lets you validate the runtime in the same environment where you will execute the model.

A native-first approach also makes it easier to confirm that the final binary, shared libraries, and model assets work together correctly on the Armv9 platform. For a reproducible Learning Path, this is usually the fastest way to get to a working baseline before optimizing or automating the workflow further.

## Build MNN natively on Armv9

Clone the MNN repository:

```bash
git clone https://github.com/alibaba/MNN.git
cd MNN
```

Configure and build MNN with LLM, audio, and Omni support enabled:

```bash
rm -rf build
mkdir build && cd build

cmake .. \
  -DCMAKE_BUILD_TYPE=Release \
  -DMNN_BUILD_SHARED=ON \
  -DMNN_BUILD_LLM=ON \
  -DMNN_BUILD_AUDIO=ON \
  -DMNN_BUILD_LLM_OMNI=ON \
  -DMNN_LOW_MEMORY=ON \
  -DMNN_KLEIDIAI=ON

make -j$(nproc)
```

The most important CMake options are:

- `MNN_BUILD_LLM=ON` to enable LLM support required by `llm_demo`
- `MNN_BUILD_AUDIO=ON` to enable the audio components used by the Omni model
- `MNN_BUILD_LLM_OMNI=ON` to enable multimodal Omni support
- `MNN_LOW_MEMORY=ON` to prefer lower-memory runtime settings where available
- `MNN_KLEIDIAI=ON` to enable Arm-specific optimizations through KleidiAI

Among these options, `MNN_KLEIDIAI=ON` is the most important Arm-specific build flag in this workflow. It enables Arm-focused optimizations through KleidiAI, making it especially relevant when you want to validate efficient local inference on Armv9 CPUs.

In this Learning Path, a CPU-first build keeps the setup simpler, reduces external dependencies, and makes the resulting workflow easier to reproduce across edge and embedded Arm systems.

Verify that the `llm_demo` binary was created:

```bash
ls -l ~/mnn/MNN/build/llm_demo
```


## Verify shared library resolution

If your system already has another MNN installation, `llm_demo` can load a different `libMNN.so` than the one you just built. This is a common source of runtime errors.

From the build directory, inspect the runtime dependencies:

```bash
cd ~/mnn/MNN/build
ldd ./llm_demo | grep -E "libMNN|Express|Audio|OpenCV" || true
```

You should see `libMNN.so` and `libMNN_Express.so` resolving from the `~/mnn/MNN/build` tree. A correct result looks similar to:

```text
libMNNAudio.so => /home/radxa/mnn/MNN/build/tools/audio/libMNNAudio.so (0x0000ffffb6d00000)
libMNN_Express.so => /home/radxa/mnn/MNN/build/express/libMNN_Express.so (0x0000ffffb6c00000)
libMNN.so => /home/radxa/mnn/MNN/build/libMNN.so (0x0000ffffb6600000)
libMNNOpenCV.so => /home/radxa/mnn/MNN/build/tools/cv/libMNNOpenCV.so (0x0000ffffb61a0000)
```

An incorrect result looks like this, where `libMNN.so` is loaded from another location:

```text
libMNNAudio.so => /home/radxa/mnn/MNN/build/tools/audio/libMNNAudio.so (0x0000ffffb6d00000)
libMNN_Express.so => /home/radxa/mnn/MNN/build/express/libMNN_Express.so (0x0000ffffb6c00000)
libMNN.so => /usr/share/cix/lib/libMNN.so (0x0000ffffb6600000)
libMNNOpenCV.so => /home/radxa/mnn/MNN/build/tools/cv/libMNNOpenCV.so (0x0000ffffb61a0000)
```

If `libMNN.so` resolves from a different directory, update `LD_LIBRARY_PATH` to prefer the libraries from your local build:

```bash
export LD_LIBRARY_PATH=$HOME/mnn/MNN/build:$HOME/mnn/MNN/build/express:$HOME/mnn/MNN/build/tools/audio:$HOME/mnn/MNN/build/tools/cv:${LD_LIBRARY_PATH:-}
```

To make this setting persistent across terminal sessions, add it to your shell profile:

```bash
echo 'export LD_LIBRARY_PATH=$HOME/mnn/MNN/build:$HOME/mnn/MNN/build/express:$HOME/mnn/MNN/build/tools/audio:$HOME/mnn/MNN/build/tools/cv:${LD_LIBRARY_PATH:-}' >> ~/.bashrc
source ~/.bashrc
```

Run the check again:

```bash
ldd ./llm_demo | grep -E "libMNN|Express|Audio|OpenCV" || true
```

## Download the prebuilt Omni model package

This Learning Path uses a prebuilt [Omni model package](https://huggingface.co/taobao-mnn/Qwen2.5-Omni-7B-MNN) that is already prepared for MNN deployment.

Clone the model repository into your workspace:

```bash
cd ~/mnn
git clone https://www.modelscope.cn/MNN/Qwen2.5-Omni-7B-MNN.git
cd ~/mnn/Qwen2.5-Omni-7B-MNN
```

## Verify that the required model files are present

Check that the repository contains the expected configuration and model files:

```bash
ls -lh ~/mnn/Qwen2.5-Omni-7B-MNN
```

Verify that `config.json` exists:

```bash
cat ~/mnn/Qwen2.5-Omni-7B-MNN/config.json
```

The presence of `config.json` alone does not guarantee that the full model weights are available locally. Confirm that the main model files are present:

- `llm.mnn`
- `llm.mnn.weight`

```bash
ls -lh ~/mnn/Qwen2.5-Omni-7B-MNN/llm.mnn ~/mnn/Qwen2.5-Omni-7B-MNN/llm.mnn.weight
```

If both files exist and show non-trivial file sizes, the model package is ready for inference.

## If the model weights are missing

Some environments fetch the large model files automatically when you clone the repository, while others do not. If `llm.mnn` or `llm.mnn.weight` is missing, install **Git LFS** and pull the large files explicitly.

Install Git LFS:

```bash
sudo apt-get update
sudo apt-get install -y git-lfs
git lfs install
```

Then download the large model files:

```bash
cd ~/mnn/Qwen2.5-Omni-7B-MNN
git lfs pull
```

{{% notice Note %}}
Downloading the full model weights can take a while depending on your network connection and available bandwidth.
{{% /notice %}}

After `git lfs pull`, verify the files again:

```bash
ls -lh ~/mnn/Qwen2.5-Omni-7B-MNN/llm.mnn ~/mnn/Qwen2.5-Omni-7B-MNN/llm.mnn.weight
```

{{% notice Note %}}
This package is already prepared for MNN deployment.

You do not need to export the model from PyTorch or run additional quantization steps before using it in this Learning Path.
{{% /notice %}}

## Check your setup

Run `llm_demo` with the model configuration to verify the binary loads correctly:

```bash
cd ~/mnn/MNN/build
./llm_demo ~/mnn/Qwen2.5-Omni-7B-MNN/config.json
```

The binary starts an interactive session. Type `exit` or press Ctrl+C to quit. If the binary loads without `undefined symbol` errors or missing library messages, your environment is ready for the next section.

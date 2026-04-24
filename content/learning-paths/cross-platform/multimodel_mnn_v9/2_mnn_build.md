---
title: Build MNN and prepare an Omni model on Armv9
weight: 3
layout: learningpathall
---

## Introduction

In this section, you'll build **MNN** natively on your Armv9 Linux system and verify that the `llm_demo` binary can load a prebuilt Omni MNN model package. This sets up everything needed for the text, vision, and audio demos in later sections.

This section uses a native CPU-only MNN build on Armv9 — a deliberate design choice, not a fallback. The goal is to show how a compact, reproducible, deployment-friendly software stack can run directly on an Armv9 CPU without depending on a discrete GPU or separate accelerator.

At the end of this section, you'll have:

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

## Why build natively on Armv9

Building, running inference, and deploying all happen directly on the Armv9 device. There's no cross-compilation involved. This keeps the toolchain simple, eliminates environment drift between build and target, and means any library or configuration issue you encounter is the same one you'd hit in production.

Building on the target also makes it straightforward to confirm that the binary, shared libraries, and model assets all resolve correctly in the same environment where you will run the model.

## Build MNN

Clone the MNN repository:

```bash
git clone https://github.com/alibaba/MNN.git
cd MNN
```

Install the required build dependencies:

```bash
sudo apt update
sudo apt install -y build-essential gcc g++ cmake
```

Configure and build MNN with LLM, audio, and Omni support enabled:

```bash
mkdir build && cd build
```

```bash
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

This Learning Path uses a prebuilt [Omni model package](https://www.modelscope.cn/MNN/Qwen2.5-Omni-7B-MNN) that is already prepared for MNN deployment. The full package is approximately 15 GB, so ensure you have sufficient disk space and a stable internet connection before cloning.

Clone the model repository into your workspace:

```bash
cd ~/mnn
git clone https://www.modelscope.cn/MNN/Qwen2.5-Omni-7B-MNN.git
cd ~/mnn/Qwen2.5-Omni-7B-MNN
```

## Download the model weights

After cloning, install Git LFS and pull the large model files:

```bash
sudo apt-get install -y git-lfs
git lfs install
cd ~/mnn/Qwen2.5-Omni-7B-MNN
git lfs pull
```

{{% notice Note %}}
The full model weights are approximately 15 GB. Downloading can take a while depending on your network connection.
{{% /notice %}}

Verify that the main model files are present and several gigabytes in size:

```bash
ls -lh ~/mnn/Qwen2.5-Omni-7B-MNN/llm.mnn ~/mnn/Qwen2.5-Omni-7B-MNN/llm.mnn.weight
```

If either file is only a few hundred bytes, the LFS download did not complete. Run `git lfs pull` again to resume it.

{{% notice Note %}}
This package is already prepared for MNN deployment. You do not need to export the model from PyTorch or run additional quantization steps before using it in this Learning Path.
{{% /notice %}}

## Check your setup

Run `llm_demo` with the model configuration to verify the binary loads correctly:

```bash
cd ~/mnn/MNN/build
./llm_demo ~/mnn/Qwen2.5-Omni-7B-MNN/config.json
```

The binary starts an interactive session. Type `exit` or press Ctrl+C to quit. If the binary loads without `undefined symbol` errors or missing library messages, your environment is ready for the next section.

---
title: Build MNN and prepare an Omni model on Armv9
weight: 3
layout: learningpathall
---

## Introduction

In this module you will build **MNN** natively on your Arm v9 Linux system and verify that the `llm_demo` binary can load a **prebuilt Omni MNN model package**. This sets up everything needed for the text, vision, and audio demos in later modules.

This creates the software environment used in the next modules, where you run text, vision, and audio-enabled multimodal inference on Armv9.

At the end of this module, you will have:

- a working `llm_demo` binary
- a validated model directory that includes `config.json`
- a runtime environment that resolves the correct MNN shared libraries

## Create a workspace

Create a working directory under your home folder:

```bash
mkdir -p ~/mnn
cd ~/mnn
```

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
- `MNN_KLEIDIAI=ON` to enable KleidiAI optimizations on supported Arm platforms

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

You should see `libMNN.so` and `libMNN_Express.so` resolving from the `~/mnn/MNN/build` tree.

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

Run the check again:

```bash
ldd ./llm_demo | grep -E "libMNN|Express|Audio|OpenCV" || true
```

## Download a prebuilt Omni model package

This learning path uses a prebuilt [Omni model package](https://huggingface.co/taobao-mnn/Qwen2.5-Omni-7B-MNN) that is already in MNN deployable format.

Clone the model into your workspace:

```bash
cd ~/mnn
git clone https://www.modelscope.cn/MNN/Qwen2.5-Omni-7B-MNN.git
```

Verify that the package includes `config.json`:

```bash
cat ~/mnn/Qwen2.5-Omni-7B-MNN/config.json
```

A valid configuration looks similar to:

```json
{
    "llm_model": "llm.mnn",
    "llm_weight": "llm.mnn.weight",
    "backend_type": "cpu",
    "thread_num": 4,
    "precision": "low",
    "memory": "low",
    "system_prompt": "You are Qwen, a virtual human developed by the Qwen Team, Alibaba Group, capable of perceiving auditory and visual inputs, as well as generating text and speech.",
    "talker_max_new_tokens": 2048,
    "talker_speaker": "Chelsie",
    "dit_steps": 5,
    "dit_solver": 1,
    "mllm": {
        "backend_type": "cpu",
        "thread_num": 4,
        "precision": "normal",
        "memory": "low"
    }
}
```

{{% notice Note %}}
This package is already prepared for MNN deployment.

You do not need to export the model from PyTorch or run additional quantization steps before using it in this learning path.
{{% /notice %}}

## Check your setup

Start `llm_demo` with the model configuration:

```bash
cd ~/mnn/MNN/build
./llm_demo ~/mnn/Qwen2.5-Omni-7B-MNN/config.json
```

If the binary starts without `undefined symbol` errors or missing library messages, your environment is ready for the next module.

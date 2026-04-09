---
title: Build MNN and prepare an Omni model on Armv9
weight: 3
layout: learningpathall
---

## Overview

In this module you will build **MNN** natively on your Arm v9 Linux system and verify that the `llm_demo` binary can load a **prebuilt Omni MNN model package**. This sets up everything needed for the text, vision, and audio demos in later modules.

By the end of this module you will have:

- A working `llm_demo` binary
- A verified Omni model directory containing `config.json`
- A runtime environment that loads the correct MNN shared libraries


## Step 1 - Create a working directory

Create a workspace under your home directory:

```bash
mkdir -p ~/mnn
cd ~/mnn
```

## Step 2 - Clone and build MNN (native build)

Clone the MNN repository:

```bash
git clone https://github.com/alibaba/MNN.git
cd MNN
```

Configure and build:

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

**Key CMake options:**

- `MNN_BUILD_LLM=ON` enables LLM support required by llm_demo
- `MNN_BUILD_AUDIO=ON` enables audio features used by Omni
- `MNN_BUILD_LLM_OMNI=ON` enables Omni multimodal support
- `MNN_LOW_MEMORY=ON` prefers lower-memory configurations where available
- `MNN_KLEIDIAI=ON` enables KleidiAI-related optimizations on supported Arm platforms


Verify that `llm_demo` was built:

```bash
ls -l ~/mnn/MNN/build/llm_demo
```


## Step 3 - Confirm the correct shared libraries are loaded

If your system has more than one MNN installation, a common pitfall is building llm_demo in one location but loading libMNN.so from another.

From the build directory, inspect runtime dependencies:

```bash
cd ~/mnn/MNN/build
ldd ./llm_demo | grep -E "libMNN|Express|Audio|OpenCV" || true
```

You should see `libMNN.so` and `libMNN_Express.so` resolving from your ~/mnn/MNN/build tree.

```
libMNNAudio.so => /home/radxa/mnn/MNN/build/tools/audio/libMNNAudio.so (0x0000ffffb6d00000)
        libMNN_Express.so => /home/radxa/mnn/MNN/build/express/libMNN_Express.so (0x0000ffffb6c00000)
        libMNN.so => /usr/share/cix/lib/libMNN.so (0x0000ffffb6600000)
        libMNNOpenCV.so => /home/radxa/mnn/MNN/build/tools/cv/libMNNOpenCV.so (0x0000ffffb61a0000)
```

If you see `libMNN.so` coming from a different directory, set `LD_LIBRARY_PATH` to prefer your build output:

```bash
export LD_LIBRARY_PATH=$HOME/mnn/MNN/build:$HOME/mnn/MNN/build/express:$HOME/mnn/MNN/build/tools/audio:$HOME/mnn/MNN/build/tools/cv:${LD_LIBRARY_PATH:-}
```

Re-check:

```bash
ldd ./llm_demo | grep -E "libMNN|Express|Audio|OpenCV" || true
```


## Step 4 - Download and verify a prebuilt MNN Omni model package

This learning path uses a prebuilt [Omni model package](https://huggingface.co/taobao-mnn/Qwen2.5-Omni-7B-MNN) that is already in MNN deployable format.

Store the model directory into `~/mnn`

```bash
cd ~/mnn
git clone https://www.modelscope.cn/MNN/Qwen2.5-Omni-7B-MNN.git
```

Verify config.json exists:
```bash
cat ~/mnn/Qwen2.5-Omni-7B-MNN/config.json
```

```
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
This is an MNN-ready model package.
You do not need to export from PyTorch or run additional quantization steps.
{{% /notice %}}


### Checkpoint

Start `llm_demo` with your model config:

```bash
cd ~/mnn/MNN/build
./llm_demo ~/mnn/Qwen2.5-Omni-7B-MNN/config.json
```

If the binary starts without `undefined symbol` or library errors, you are ready for the next module.

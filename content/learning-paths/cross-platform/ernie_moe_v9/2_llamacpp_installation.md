---
title: Setting Up llama.cpp on Arm v9 develop board
weight: 3
layout: "learningpathall"
---

## Setting Up llama.cpp on Arm v9 develop board

In the previous section, you learned how Mixture-of-Experts (MoE) models reduce resource consumption by activating only a fraction of parameters. 
Now, you'll walk through how to prepare your environment to deploy `ERNIE-4.5 MoE` models on an Armv9 platform using `llama.cpp`.

In this module, you’ll verify model inference on Radxa O6 and validate multilingual outputs using ERNIE’s Thinking variant.

This section prepares the foundation for deploying ERNIE-4.5 on an ARMv9 platform. You will begin by reviewing the hardware—specifically, the `Radxa O6` development board equipped with an Armv9 CPU. From there, you will install llama.cpp, a lightweight inference engine, build it from source, and download ERNIE-4.5 models in GGUF format (quantized to Q4 for efficient CPU inference). Finally, you will run a basic inference test to confirm that the environment is properly configured and ready for benchmarking and optimization in the next module.

### Arm v9 development board

In this learning path, we use the [Radxa O6](https://radxa.com/products/orion/o6/) — a compact Armv9 development board powered by the [CIX CD8180](https://en.cixtech.com/Personal-Computing/) SoC. It features:

- 12-core Armv9.2 CPU
- Support for SVE, dotprod, and i8mm instruction sets
- Multiple HDMI, PCIe slot with Gen4x8, dual 5Gbps Ethernet Ports and USB-C for I/O expansion

We chose this board because it balances affordability and performance. Most importantly, it supports vector instructions we’ll benchmark later in this path. 

The default system image for the board is [Debian](https://docs.radxa.com/en/orion/o6/debian/debian-user-guide), which includes a ready-to-use user environment. You can verify or reflash the OS by following the instructions on the Radxa O6 [download page](https://docs.radxa.com/en/orion/o6/download).

With the Radxa O6 ready, let’s set up the software stack beginning with llama.cpp.

### Step 1: Clone and Build llama.cpp

First, ensure your system is up-to-date and install the required tools and libraries:

```bash
sudo apt update
sudo apt install build-essential cmake python3 python3-pip htop
```

Next, build [llama.cpp](https://github.com/ggml-org/llama.cpp/), an open-source C++ framework for running and experimenting with large language models. Designed to be lightweight and fast, llama.cpp supports inference on edge devices (CPU-only) and implements many of the most popular LLM architectures.

In the context of MoE models, `llama.cpp` currently supports:
- Openai-moe
- Oleo
- lm4-moe
- Qwen2 moe, Qwen3 moe
- Grok
- Ernie4.5

These models use diverse routing and expert management strategies, and llama.cpp provides a unified backend for efficient MoE inference.
For more in-depth coverage of llama.cpp capabilities and use cases, see those [learning paths](https://learn.arm.com/tag/llama.cpp/) for the detail.

```bash
cd ~
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp

mkdir build && cd build
cmake ..
make -j$(nproc)
```

This will generate binaries like `llama-cli` under directory `~/llama.cpp/build/bin`, which we’ll use to run inference in later steps.
Once llama.cpp is compiled, we can now download the models we’ll use for evaluation.


### Step 2: Download ERNIE-4.5 Q4 GGUF Model

In this learning path, you will use [ERNIE-4.5](https://huggingface.co/collections/baidu/ernie-45) to deploy in Arm v9.
Download both model variants so you can experiment later:

```bash
mkdir -p ~/models/ernie-4.5
cd ~/models/ernie-4.5
wget https://modelscope.cn/models/unsloth/ERNIE-4.5-21B-A3B-PT-GGUF/resolve/master/ERNIE-4.5-21B-A3B-PT-Q4_0.gguf
wget https://modelscope.cn/models/unsloth/ERNIE-4.5-21B-A3B-Thinking-GGUF/resolve/master/ERNIE-4.5-21B-A3B-Thinking-Q4_0.gguf
```

You can see the size of both models are 12 GB and quantized to Q4, making them suitable for CPU-only inference.

{{% notice Note %}}
The Q4 quantized models reduce memory footprint and allow CPU‑only inference — you’ll still need around 12 GB of RAM for good performance.
{{% /notice %}}

While both the Thinking and PT variants of ERNIE-4.5 share the same MoE architecture, they are fine-tuned for different objectives. The Thinking model is optimized for logical reasoning and structured generation, making it the main focus of subsequent benchmarking and hardware optimization. You are encouraged to install both variants and observe behavioral differences using the same prompt.

### Step 3: Run a Basic Inference Test

Navigate to the build directory and run the following command to verify that the model loads correctly and supports multilingual input:

```bash
cd ~/llama.cpp/build
./bin/llama-cli \
    --jinja \
    -m ~/models/ernie-4.5/ERNIE-4.5-21B-A3B-Thinking-Q4_0.gguf \
    -p "Please introduce Mixture of Experts in Chinese." \
    -c 4096 -t 12 \
    --jinja
```

Note the flags:
- ***-p***: Passes the input prompt directly as a string.
- ***-c 4096***: Sets the context length (in tokens). A longer context allows the model to “remember” more input text, which is crucial for long-form tasks. Here we use the recommended 4096 tokens.
- ***-t 12***: Specifies the number of CPU threads used for inference. You should match this number to the physical cores (or logical threads) available on your system to maximize performance.
- ***--jinja***: Enables Jinja‑style prompt templates. Many Chinese‑oriented MoE models rely on this template format for structured inputs.

If everything is set up correctly, you will see metadata output from llama.cpp indicating the model’s architecture and size:

```
print_info: model type       = 21B.A3B
print_info: model params     = 21.83 B
print_info: general.name     = Ernie-4.5-21B-A3B-Thinking
```

Once inference is complete, the expected output will look like this (in Chinese):
```
用户让我介绍“混合专家”（Mixture of Experts）在中文里的内容。首先，我需要明确Mixture of Experts的基本概念，然后考虑在中文语境下的特殊表达或常见翻译。首先，Mixture of Experts是一种机器学习模型，结合了多个专家模型，通过门控机制（gating network）来动态选择最佳专家，通常用于提升模型性能，尤其是在处理复杂数据时，不同专家处理不同的特征或子空间。
```

This confirms that the model router is functioning correctly (though not yet directly observable).

This confirms:
- The GGUF model is successfully loaded.
- The llama.cpp build functions as expected.
- CPU-only inference on Armv9 is working.

#### Why This Prompt Matters

This prompt, “Please introduce Mixture of Experts in Chinese.”, was chosen for its dual pedagogical value:
- ***Bilingual Capability Check***: The instruction is issued in English, but the answer is expected in Chinese. This helps confirm that ERNIE-4.5’s multilingual support is active and effective.
- ***MoE Behavior Engagement***: The topic itself — explaining “Mixture of Experts” — requires combining multiple sub-skills: technical understanding, translation, and structured explanation. This likely triggers different experts within the model to contribute during inference. Even though routing isn’t explicitly logged, the richness and precision of the output suggest that MoE routing is functioning as designed. This kind of prompt increases the likelihood of multiple experts being activated simultaneously—e.g., language generation, machine learning knowledge, and Chinese translation.

By using a single prompt, you verify setup correctness, observe output quality, and gain insight into MoE inference characteristics — all essential elements before moving on to hardware-specific performance tuning.

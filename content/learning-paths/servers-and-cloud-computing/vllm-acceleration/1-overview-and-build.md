---
title: Build and validate vLLM for inference 
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is vLLM?

vLLM is an open-source, high-throughput inference and serving engine for large language models (LLMs). It’s designed to make LLM inference faster, more memory-efficient, and scalable, particularly during the prefill (context processing) and decode (token generation) phases of inference.

## Key features
* Continuous batching: dynamically merges incoming inference requests into larger batches, maximizing Arm CPU utilization and overall throughput
* KV cache management: efficiently stores and reuses key-value attention states, sustaining concurrency across multiple active sessions while minimizing memory overhead
* Token streaming: streams generated tokens as they are produced, enabling real-time responses for chat or API scenarios

## Interaction modes

You can use vLLM in two main ways:
- Using an OpenAI-Compatible REST Server: vLLM provides a /v1/chat/completions endpoint compatible with the OpenAI API schema, making it drop-in ready for tools like LangChain, LlamaIndex, and the official OpenAI Python SDK
- Using a Python API: load and serve models programmatically within your own Python scripts for flexible local inference and evaluation

vLLM supports Hugging Face Transformer models out-of-the-box and scales seamlessly from single-prompt testing to production batch inference.

## What you will build

In this Learning Path, you'll build a CPU-optimized version of vLLM targeting the Arm64 architecture, integrated with oneDNN and the Arm Compute Library (ACL).
This build enables high-performance LLM inference on Arm servers, leveraging specialized Arm math libraries and kernel optimizations.
After compiling, you’ll validate your build by running a local chat example to confirm functionality and measure baseline inference speed.

## Set up your environment 

Before you begin, make sure your environment meets these requirements:

- Python 3.12 on Ubuntu 22.04 LTS or newer
- At least 32 vCPUs, 64 GB RAM, and 64 GB of free disk space

This Learning Path was tested on an AWS Graviton4 `c8g.12xlarge` instance with 64 GB of attached storage.

## Install build dependencies

Install the following packages required for compiling vLLM and its dependencies on Arm64:
```bash
sudo apt-get update -y
sudo apt-get install -y build-essential cmake libnuma-dev
sudo apt install -y python3.12-venv python3.12-dev
```

You can optionally install tcmalloc, a fast memory allocator from Google’s gperftools, which improves performance under high concurrency:

```bash
sudo apt-get install -y libtcmalloc-minimal4
```

{{% notice Note %}}
On aarch64, vLLM's CPU backend automatically builds with the Arm Compute Library (ACL) through oneDNN.
This ensures optimized Arm kernels are used for matrix multiplications, layer normalization, and activation functions without additional configuration.
{{% /notice %}}

## Build vLLM for Arm64 CPU

You’ll now build vLLM optimized for Arm (aarch64) servers with oneDNN and the Arm Compute Library (ACL) automatically enabled in the CPU backend.

## Create and activate a Python virtual environment

It’s best practice to build vLLM inside an isolated environment to prevent conflicts between system and project dependencies:

```bash
python3.12 -m venv vllm_env
source vllm_env/bin/activate
python3 -m pip install --upgrade pip
```

## Clone vLLM and install build requirements

Download the official vLLM source code and install its CPU-specific build dependencies:

```bash
git clone https://github.com/vllm-project/vllm.git
cd vllm
git checkout 5fb4137
pip install -r requirements/cpu.txt -r requirements/cpu-build.txt
```
The specific commit (5fb4137) pins a verified version of vLLM that officially adds Arm CPUs to the list of supported build targets, ensuring full compatibility and optimized performance for Arm-based systems.

## Build the vLLM wheel for CPU

Run the following command to compile and package vLLM as a Python wheel optimized for CPU inference:

```bash
VLLM_TARGET_DEVICE=cpu python3 setup.py bdist_wheel
```
The output wheel will appear under dist/ and include all compiled C++/PyBind modules.

## Install the wheel
Install the freshly built wheel into your active environment:

```bash
pip install --force-reinstall dist/*.whl              # fresh install
# pip install --no-deps --force-reinstall dist/*.whl  # incremental build
```

{{% notice Tip %}}
Do not delete the local vLLM source directory.
The repository contains C++ extensions and runtime libraries required for correct CPU inference on aarch64 after wheel installation.
{{% /notice %}}

## Validate your build with offline inference

Run a quick test to confirm your Arm-optimized vLLM build works as expected. Use the built-in chat example to perform offline inference and verify that oneDNN and Arm Compute Library optimizations are active.

```bash
python examples/offline_inference/basic/chat.py \
   --dtype=bfloat16 \
   --model TinyLlama/TinyLlama-1.1B-Chat-v1.0
```

This command runs a small Hugging Face model in bfloat16 precision, streaming generated tokens to the console. You should see output similar to:

```output
Generated Outputs:
--------------------------------------------------------------------------------
Prompt: None

Generated text: 'The Importance of Higher Education\n\nHigher education is a fundamental right'
--------------------------------------------------------------------------------
Adding requests: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 10/10 [00:00<00:00, 9552.05it/s]
Processed prompts: 100%|████████████████████████████████████████████████████████████████████████| 10/10 [00:01<00:00,  6.78it/s, est. speed input: 474.32 toks/s, output: 108.42 toks/s]
...
```

If you see token streaming and generated text, your vLLM build is correctly configured for Arm64 inference.

{{% notice Note %}}
As CPU support in vLLM continues to mature, these manual build steps will eventually be replaced by a streamlined `pip` install workflow for aarch64, simplifying future deployments on Arm servers.
{{% /notice %}}

You have now verified that your vLLM Arm64 build runs correctly and performs inference using Arm-optimized kernels.
Next, you’ll proceed to model quantization, where you’ll compress LLM weights to INT4 precision using llmcompressor and benchmark the resulting performance improvements.

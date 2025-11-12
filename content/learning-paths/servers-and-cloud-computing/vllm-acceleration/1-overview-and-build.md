---
title: Overview and Optimized Build
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is vLLM?

vLLM is an open-source, high-throughput inference and serving engine for large language models (LLMs).
It’s designed to make LLM inference faster, more memory-efficient, and scalable, particularly during the prefill (context processing) and decode (token generation) phases of inference.

### Key Features
   * Continuous Batching – Dynamically combines incoming inference requests into a single large batch, maximizing CPU/GPU utilization and throughput.
   * KV Cache Management – Efficiently stores and reuses key-value attention states, sustaining concurrency across multiple active sessions while minimizing memory overhead.
   * Token Streaming – Streams generated tokens as they are produced, enabling real-time responses for chat or API scenarios.
### Interaction Modes
You can use vLLM in two main ways:
   * OpenAI-Compatible REST Server:
   vLLM provides a /v1/chat/completions endpoint compatible with the OpenAI API schema, making it drop-in ready for tools like LangChain, LlamaIndex, and the official OpenAI Python SDK.
   * Python API:
   Load and serve models programmatically within your own Python scripts for flexible local inference and evaluation.

vLLM supports Hugging Face Transformer models out-of-the-box and scales seamlessly from single-prompt testing to production batch inference.

## What you build

In this learning path, you will build a CPU-optimized version of vLLM targeting the Arm64 architecture, integrated with oneDNN and the Arm Compute Library (ACL).
This build enables high-performance LLM inference on Arm servers, leveraging specialized Arm math libraries and kernel optimizations.
After compiling, you’ll validate your build by running a local chat example to confirm functionality and measure baseline inference speed.

## Why this is fast on Arm

vLLM’s performance on Arm servers is driven by both software optimization and hardware-level acceleration.
Each component of this optimized build contributes to higher throughput and lower latency during inference:

- Optimized kernels: The aarch64 vLLM build uses direct oneDNN with the Arm Compute Library for key operations.
- 4‑bit weight quantization: vLLM supports INT4 quantized models, and Arm accelerates this using KleidiAI microkernels, which take advantage of DOT-product (SDOT/UDOT) and SME2 (Scalable Matrix Extension) instructions.
- Efficient MoE execution: For Mixture-of-Experts (MoE) models, vLLM fuses INT4 quantized expert layers to reduce intermediate memory transfers, which minimizes bandwidth bottlenecks
- Optimized Paged attention: The paged attention mechanism, which handles token reuse during long-sequence generation, is SIMD-tuned for Arm’s NEON and SVE (Scalable Vector Extension) pipelines.
- System tuning: Using thread affinity ensures efficient CPU core pinning and balanced thread scheduling across Arm clusters.
Additionally, enabling tcmalloc (Thread-Caching Malloc) reduces allocator contention and memory fragmentation under high-throughput serving loads.

## Before you begin

Verify that your environment meets the following requirements:

Python version: Use Python 3.12 on Ubuntu 22.04 LTS or later.
Hardware requirements: At least 32 vCPUs, 64 GB RAM, and 64 GB of free disk space.

This Learning Path was validated on an AWS Graviton4 c8g.12xlarge instance with 64 GB of attached storage.

### Install Build Dependencies

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
On aarch64, vLLM’s CPU backend automatically builds with the Arm Compute Library (ACL) through oneDNN.
This ensures optimized Arm kernels are used for matrix multiplications, layer normalization, and activation functions without additional configuration.
{{% /notice %}}

## Build vLLM for Arm64 CPU
You’ll now build vLLM optimized for Arm (aarch64) servers with oneDNN and the Arm Compute Library (ACL) automatically enabled in the CPU backend.

1. Create and Activate a Python Virtual Environment
It’s best practice to build vLLM inside an isolated environment to prevent conflicts between system and project dependencies:

```bash
python3.12 -m venv vllm_env
source vllm_env/bin/activate
python3 -m pip install --upgrade pip
```

2. Clone vLLM and Install Build Requirements
Download the official vLLM source code and install its CPU-specific build dependencies:

```bash
git clone https://github.com/vllm-project/vllm.git
cd vllm
git checkout 5fb4137
pip install -r requirements/cpu.txt -r requirements/cpu-build.txt
```
The specific commit (5fb4137) pins a verified version of vLLM that officially adds Arm CPUs to the list of supported build targets, ensuring full compatibility and optimized performance for Arm-based systems.

3. Build the vLLM Wheel for CPU
Run the following command to compile and package vLLM as a Python wheel optimized for CPU inference:

```bash
VLLM_TARGET_DEVICE=cpu python3 setup.py bdist_wheel
```
The output wheel will appear under dist/ and include all compiled C++/PyBind modules.

4. Install the Wheel
Install the freshly built wheel into your active environment:

```bash
pip install --force-reinstall dist/*.whl              # fresh install
# pip install --no-deps --force-reinstall dist/*.whl  # incremental build
```

{{% notice Tip %}}
Do not delete the local vLLM source directory.
The repository contains C++ extensions and runtime libraries required for correct CPU inference on aarch64 after wheel installation.
{{% /notice %}}

## Quick validation via Offline Inferencing

Once your Arm-optimized vLLM build completes, you can validate it by running a small offline inference example. This ensures that the CPU-specific backend and oneDNN and ACL optimizations were correctly compiled into your build.
Run the built-in chat example included in the vLLM repository:

```bash
python examples/offline_inference/basic/chat.py \
  --dtype=bfloat16 \
  --model TinyLlama/TinyLlama-1.1B-Chat-v1.0
```

Explanation:
--dtype=bfloat16 runs inference in bfloat16 precision. Recent Arm processors support the BFloat16 (BF16) number format in PyTorch. For example, AWS Graviton3 and Graviton3 processors support BFloat16.
--model specifies a small Hugging Face model for testing (TinyLlama-1.1B-Chat), ideal for functional validation before deploying larger models.
You should see token streaming in the console, followed by a generated output confirming that vLLM’s inference pipeline is working correctly.

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

{{% notice Note %}}
As CPU support in vLLM continues to mature, manual builds will be replaced by a simple `pip install` flow for easier setup in near future.
{{% /notice %}}

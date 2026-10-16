---
title: Set up vLLM for MoE inference
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is vLLM?

[vLLM](https://docs.vllm.ai/en/latest/) is an open-source, high-throughput inference and serving engine for large language models. It provides an OpenAI-compatible API server and benchmarking tools for measuring online serving performance.

In this Learning Path, you will use vLLM on Arm CPUs to run and benchmark Mixture of Experts (MoE) models.

## Understand MoE models

Mixture of Experts models contain multiple expert layers. For each token, a router selects a small number of experts instead of activating all experts.

This can reduce compute compared with activating the full model, but it also makes inference performance depend heavily on routing, batching, and optimized expert kernels.

This Learning Path focuses on two MoE paths:

- BF16 MoE inference and benchmarking.
- INT8/W8A8 MoE inference and benchmarking.

## Understand the models you'll use

Gemma4 is a BF16 MoE language model. In this Learning Path, it is used to show before and after BF16 MoE optimization results. You can view the model card at https://huggingface.co/google/gemma-4-26B-A4B-it.

GPT-OSS BF16 is another MoE language model used to validate that the BF16 MoE optimization benefits more than one model family. You can view the model card at https://huggingface.co/unsloth/gpt-oss-20b-BF16.

Qwen3-30B-A3B-Thinking-2507 is used as the BF16 baseline for the INT8/W8A8 section. You can view the model card at https://huggingface.co/Qwen/Qwen3-30B-A3B-Thinking-2507.

RedHatAI/Qwen3-30B-A3B-Thinking-2507-quantized.w8a8 is the INT8/W8A8 MoE model used to show the additional benefit of INT8 MoE support. You can view the model card at https://huggingface.co/RedHatAI/Qwen3-30B-A3B-Thinking-2507-quantized.w8a8.

## Set up your environment

Before you begin, make sure your environment meets these requirements:

- Python 3.12 on Ubuntu 24.04 LTS or newer
- An Arm-based Linux server running Ubuntu 24.04 LTS or newer, with enough CPU cores, memory, and disk space for large MoE models

The benchmark results in this Learning Path were collected on a 96-core Arm Neoverse-V2 system with 185 GiB RAM and a 484 GB root volume.

## Confirmed package versions

The public-wheel validation used:

```text
vLLM: 0.27.1+cpu
torch: 2.13.0+cpu
transformers: 5.14.1
```

## Install build dependencies

Install the following packages required for running vLLM on Arm:

```bash
sudo apt-get update -y
sudo apt install -y python3.12-venv python3.12-dev
```

## Create and activate a Python virtual environment

As a best practice, install vLLM inside an isolated environment to prevent conflicts between system and project dependencies:

```bash
python3.12 -m venv vllm_env_new
source vllm_env_new/bin/activate
python -m pip install --upgrade pip
```

## Install vLLM for CPU

{{% notice Note %}}
The following command installs vLLM version 0.27.1. The same steps work with other versions. Replace the version number in the URL with the version of your choice. To find the latest version, see the [vLLM releases page](https://github.com/vllm-project/vllm/releases).
{{% /notice %}}

Install a CPU-specific build of vLLM:

```bash
export VLLM_VERSION=0.27.1
pip install https://github.com/vllm-project/vllm/releases/download/v${VLLM_VERSION}/vllm-${VLLM_VERSION}+cpu-cp38-abi3-manylinux_2_34_aarch64.whl --extra-index-url https://download.pytorch.org/whl/cpu
```
If you want to build vLLM from source, follow the instructions in the [Build and Run vLLM on Arm Servers Learning Path](/learning-paths/servers-and-cloud-computing/vllm/vllm-setup/).

## Configure vLLM KV cache space

For the benchmark results in this Learning Path, vLLM was configured to reserve 64 GiB of CPU memory for the KV cache:

```bash
export VLLM_CPU_KVCACHE_SPACE=64
```

You can adjust this value based on available RAM, model size, context length, and expected concurrency.

## What you've accomplished and what's next

You've now set up your environment to run BF16 and INT8/W8A8 MoE inference with vLLM.

Next, you'll review the MoE precision choices and then use vLLM to run inference.
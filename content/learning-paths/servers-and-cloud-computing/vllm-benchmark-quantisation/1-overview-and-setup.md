---
title: Setup vLLM
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is vLLM

[vLLM](https://docs.vllm.ai/en/latest/) is an open-source, high-throughput inference and serving engine for large language models (LLMs). It’s designed to maximise hardware efficiency, making LLM inference faster, more memory-efficient, and scalable.

## Understanding the Llama models

Llama 3.1 8B is an open-weight, text-only LLM with 8 billion parameters that can understand and generate text. You can view the model card at https://huggingface.co/meta-llama/Llama-3.1-8B.

Quantised models have their weights converted to a lower precision data type, which reduces the memory requirements of the model and can improve performance significantly. In the [Run vLLM inference with INT4 quantization on Arm servers](/learning-paths/servers-and-cloud-computing/vllm-acceleration/) Learning Path we have covered how to quantise a model yourself. There are also many publicly available quantised versions of popular models, such as https://huggingface.co/RedHatAI/Meta-Llama-3.1-8B-quantized.w8a8. 

The notation w8a8 means that the weights have been quantised to 8-bit integers and the activations (the input data) are dynamically quantised to the same. This allows our kernels to utilise Arm's 8-bit integer matrix multiply feature I8MM. You can learn more about this in the [KleidiAI and matrix multiplication](/learning-paths/cross-platform/kleidiai-explainer/) Learning Path.

The RedHatAI/Meta-Llama-3.1-8B-quantized.w8a8 model we are using in this Learning Path only applies quantisation to the weights and activations in the linear layers of the transformer blocks. The activation quantisations are applied per-token and the weights are quantised per-channel. That is, each output channel dimension has a scaling factor applied between INT8 and BF16 representations.

## Set up your environment

Before you begin, make sure your environment meets these requirements:

- Python 3.12 on Ubuntu 22.04 LTS or newer
- At least 32 vCPUs, 96 GB RAM, and 64 GB of free disk space
This Learning Path was tested on an AWS Graviton4 c8g.12xlarge instance with 200 GB of attached storage.

## Install build dependencies

Install the following packages required for running inference with vLLM on Arm64:
```bash
sudo apt-get update -y
sudo apt install -y python3.12-venv python3.12-dev
```

Now install tcmalloc, a fast memory allocator from Google’s gperftools, which improves performance under high concurrency:
```bash
sudo apt-get install -y libtcmalloc-minimal4
```

## Create and activate a Python virtual environment

It’s best practice to install vLLM inside an isolated environment to prevent conflicts between system and project dependencies:
```bash
python3.12 -m venv vllm_env
source vllm_env/bin/activate
python -m pip install --upgrade pip
```

## Install vLLM for CPU

Install a recent CPU specific build of vLLM:
```bash
export VLLM_VERSION=0.19.1
pip install https://github.com/vllm-project/vllm/releases/download/v${VLLM_VERSION}/vllm-${VLLM_VERSION}+cpu-cp38-abi3-manylinux_2_35_aarch64.whl
```

If you wish to build vLLM from source you can follow the instructions in the [Build and Run vLLM on Arm Servers Learning Path](/learning-paths/servers-and-cloud-computing/vllm/vllm-setup/).

Your environment is now setup to run inference with vLLM. Next, you'll use vLLM to run inference on both quantised and non-quantised Llama models.

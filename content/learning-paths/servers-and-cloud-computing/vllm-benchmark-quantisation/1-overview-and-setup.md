---
title: Set up vLLM
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is vLLM? 

[vLLM](https://docs.vllm.ai/en/latest/) is an open-source, high-throughput inference and serving engine for large language models (LLMs). It’s designed to maximize hardware efficiency, making LLM inference faster, more memory-efficient, and scalable.

## Understand the models you'll use

You'll use Llama 3.1 8B and Whisper large V3 in this Learning Path.

Llama 3.1 8B is an open-weight, text-only LLM with 8 billion parameters that can understand and generate text. You can view the model card at https://huggingface.co/meta-llama/Llama-3.1-8B.

Whisper large V3 is an automatic speech recognition (ASR) and speech translation model. It has 1.55 billion parameters and can both transcribe many languages and translate them to English. You can find the model card at https://huggingface.co/openai/whisper-large-v3.

## Set up your environment

Before you begin, make sure your environment meets these requirements:

- Python 3.12 on Ubuntu 22.04 LTS or newer
- At least 32 vCPUs, 96 GB RAM, and 64 GB of free disk space

This Learning Path was tested on a 96 core machine with 128-bit SVE, 192 GB of RAM and 500 GB of attached storage.

{{% notice Note %}}
Ubuntu 26.04 and later ship with Python 3.14 as the system default. vLLM doesn't currently support Python 3.14. In this Learning Path, you'll install and use Python 3.12 regardless of your Ubuntu version.
{{% /notice %}}

### Install build dependencies

Install the following packages required for running inference with vLLM on Arm-based Linux:
```bash
sudo apt-get update -y
sudo apt install -y python3.12-venv python3.12-dev gcc g++ build-essential
```

Next, install tcmalloc, a fast memory allocator from Google’s gperftools that improves performance under high concurrency:
```bash
sudo apt-get install -y libtcmalloc-minimal4
```

### Create and activate a Python virtual environment

As a best practice, install vLLM inside an isolated environment to prevent conflicts between system and project dependencies:
```bash
python3.12 -m venv vllm_env
source vllm_env/bin/activate
python -m pip install --upgrade pip
```

### Install vLLM for CPU

{{% notice Note %}}
The following command installs vLLM version 0.20.0. The same steps work with other versions. Replace the version number in the URL with the version of your choice. To find the latest version, see the [vLLM releases page](https://github.com/vllm-project/vllm/releases).
{{% /notice %}}

Install a CPU-specific build of vLLM:
```bash
export VLLM_VERSION=0.20.0
pip install https://github.com/vllm-project/vllm/releases/download/v${VLLM_VERSION}/vllm-${VLLM_VERSION}+cpu-cp38-abi3-manylinux_2_35_aarch64.whl --extra-index-url https://download.pytorch.org/whl/cpu
```

If you want to build vLLM from source, follow the instructions in the [Build and Run vLLM on Arm Servers Learning Path](/learning-paths/servers-and-cloud-computing/vllm/vllm-setup/).


### Set up access to Llama3.1-8B models

To access the Llama models hosted by Hugging Face, install the Hugging Face CLI and authenticate with your access token. Install the CLI:
```bash
curl -LsSf https://hf.co/cli/install.sh | bash
```

For more details and alternative installation methods, see the [Hugging Face CLI guide](https://huggingface.co/docs/huggingface_hub/en/guides/cli).

Create an account on [huggingface.co](https://huggingface.co/) if you don't already have one, then generate an access token in your account settings. Log in with:
```bash
hf auth login
```

Paste your access token into the terminal when prompted. To access Llama3.1-8B, request access on the Hugging Face website. Visit [meta-llama/Llama-3.1-8B](https://huggingface.co/meta-llama/Llama-3.1-8B) and select **Expand to review and access**. Within a couple minutes of completing the form, you should be granted access to the model.

## What you've accomplished and what's next

You've now set up your environment to run inference with vLLM. 

Next, you'll review model quantization and then use vLLM to run inference on both quantized and non-quantized Llama and Whisper models.

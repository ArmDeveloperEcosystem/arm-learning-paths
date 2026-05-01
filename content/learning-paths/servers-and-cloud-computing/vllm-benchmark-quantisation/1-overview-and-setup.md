---
title: Setup vLLM
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is vLLM

[vLLM](https://docs.vllm.ai/en/latest/) is an open-source, high-throughput inference and serving engine for large language models (LLMs). It’s designed to maximise hardware efficiency, making LLM inference faster, more memory-efficient, and scalable.

## Understanding the models

Llama 3.1 8B is an open-weight, text-only LLM with 8 billion parameters that can understand and generate text. You can view the model card at https://huggingface.co/meta-llama/Llama-3.1-8B.

Whisper large V3 is an automatic speech recognition (ASR) and speech translation model. It has 1.55 billion parameters and can both transcribe many languages and translate them to English. You can find the model card at https://huggingface.co/openai/whisper-large-v3.

## Set up your environment

Before you begin, make sure your environment meets these requirements:

- Python 3.12 on Ubuntu 22.04 LTS or newer
- At least 32 vCPUs, 96 GB RAM, and 64 GB of free disk space

This Learning Path was tested on a 96 core machine with 128-bit SVE, 192 GB of RAM and 500 GB of attached storage.

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
export VLLM_VERSION=0.20.0
pip install https://github.com/vllm-project/vllm/releases/download/v${VLLM_VERSION}/vllm-${VLLM_VERSION}+cpu-cp38-abi3-manylinux_2_35_aarch64.whl --extra-index-url https://download.pytorch.org/whl/cpu
```

If you wish to build vLLM from source you can follow the instructions in the [Build and Run vLLM on Arm Servers Learning Path](/learning-paths/servers-and-cloud-computing/vllm/vllm-setup/).


## Set up access to LLama3.1-8B models

To access the Llama models hosted by Hugging Face, you will need to install the Hugging Face CLI so that you can authenticate yourself and the harness can download what it needs. You should create an account on https://huggingface.co/ and follow the instructions [in the Hugging Face CLI guide](https://huggingface.co/docs/huggingface_hub/en/guides/cli) to set up your access token. You can then install the CLI and login:
```bash
curl -LsSf https://hf.co/cli/install.sh | bash
hf auth login
```

Paste your access token into the terminal when prompted. To access Llama3.1-8B you need to request access on the Hugging Face website. Visit https://huggingface.co/meta-llama/Llama-3.1-8B and select "Expand to review and access". Complete the form and you should be granted access in a matter of minutes.

Your environment is now setup to run inference with vLLM. Next, we'll review model quantisation and then you'll use vLLM to run inference on both quantised and non-quantised Llama and Whisper models.

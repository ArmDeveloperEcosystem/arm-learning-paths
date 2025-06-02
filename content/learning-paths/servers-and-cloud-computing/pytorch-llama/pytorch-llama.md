---
title: Run a Large Language model (LLM) chatbot on Arm servers
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin
The instructions in this Learning Path are for any Arm server running Ubuntu 22.04 LTS. You need an Arm server instance with at least 16 cores and 64GB of RAM to run this example. Configure disk storage up to at least 50 GB. The instructions have been tested on an AWS Graviton4 r8g.4xlarge instance.

## Overview
Arm CPUs are widely used in traditional ML and AI use cases. In this Learning Path, you learn how to run generative AI inference-based use cases like a LLM chatbot using PyTorch on Arm-based CPUs. PyTorch is a popular deep learning framework for AI applications.

This learning path shows you how you can run the Meta Llama 3.1 model using PyTorch on Arm Neoverse V2-based AWS Graviton4 CPUs with [KleidiAI](https://gitlab.arm.com/kleidi/kleidiai) optimizations, showcasing significant performance improvements.

### Install necessary tools
First, ensure your system is up-to-date and install the required tools:

```sh
sudo apt-get update
sudo apt install gcc g++ build-essential python3-pip python3-venv google-perftools -y
```

### Set up your Python virtual environment
Set up a Python virtual environment to isolate dependencies:

```sh
python3 -m venv torch_env
source torch_env/bin/activate
```

### Install PyTorch and optimized libraries
Torchchat is a library developed by the PyTorch team that facilitates running large language models (LLMs) seamlessly on a variety of devices. TorchAO (Torch Architecture Optimization) is a PyTorch library designed for enhancing the performance of ML models through different quantization and sparsity methods. 

Start by cloning the torchao and torchchat repositories and then applying the Arm specific patches:

```sh
git clone --recursive https://github.com/pytorch/ao.git
cd ao
git checkout 174e630af2be8cd18bc47c5e530765a82e97f45b
wget https://raw.githubusercontent.com/ArmDeveloperEcosystem/PyTorch-arm-patches/main/0001-Feat-Add-support-for-kleidiai-quantization-schemes.patch
git apply --whitespace=nowarn 0001-Feat-Add-support-for-kleidiai-quantization-schemes.patch
cd ../

git clone --recursive https://github.com/pytorch/torchchat.git
cd torchchat
git checkout 925b7bd73f110dd1fb378ef80d17f0c6a47031a6
wget https://raw.githubusercontent.com/ArmDeveloperEcosystem/PyTorch-arm-patches/main/0001-modified-generate.py-for-cli-and-browser.patch
wget https://raw.githubusercontent.com/ArmDeveloperEcosystem/PyTorch-arm-patches/main/0001-Feat-Enable-int4-quantized-models-to-work-with-pytor.patch
git apply 0001-Feat-Enable-int4-quantized-models-to-work-with-pytor.patch
git apply --whitespace=nowarn 0001-modified-generate.py-for-cli-and-browser.patch
pip install -r requirements.txt
```
{{% notice Note %}} You will need Python version 3.10 to apply these patches. This is the default version of Python installed on an Ubuntu 22.04 Linux machine. {{% /notice %}}

You will now override the installed PyTorch version with a specific version of PyTorch required to take advantage of Arm KleidiAI optimizations:

```
wget https://github.com/ArmDeveloperEcosystem/PyTorch-arm-patches/raw/main/torch-2.5.0.dev20240828+cpu-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl
pip install --force-reinstall torch-2.5.0.dev20240828+cpu-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl
cd ..
pip uninstall torchao && cd ao/ && rm -rf build && python setup.py install
```

### Login to Hugging Face
You can now download the LLM.

Install the [Hugging Face CLI](https://huggingface.co/docs/huggingface_hub/main/en/guides/cli) application.
```sh
pip install -U "huggingface_hub[cli]"
```

[Generate an Access Token](https://huggingface.co/settings/tokens) to authenticate your identity with Hugging Face Hub. A token with read-only access is sufficient.

Log in to the Hugging Face repository and enter your Access Token key from Hugging face. 

```sh
huggingface-cli login
```
Before you can download the model, you must accept the license agreement at: [Meta Llama 3.1](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct).

### Downloading and Quantizing the LLM Model

In this step, you will download the [Meta Llama3.1 8B Instruct model](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct) and quantize the model to int 4-bit using Kernels for PyTorch. By using channel-wise quantization, the weights are quantized independently across different channels, or groups of channels. This can improve accuracy over simpler quantization methods.


```sh
cd ../torchchat
python torchchat.py export llama3.1 --output-dso-path exportedModels/llama3.1.so --quantize config/data/aarch64_cpu_channelwise.json --device cpu --max-seq-length 1024
```
The output from this command should look like:

```output
linear: layers.31.feed_forward.w1, in=4096, out=14336
linear: layers.31.feed_forward.w2, in=14336, out=4096
linear: layers.31.feed_forward.w3, in=4096, out=14336
linear: output, in=4096, out=128256
Time to quantize model: 44.14 seconds
-----------------------------------------------------------
Exporting model using AOT Inductor to /home/ubuntu/torchchat/exportedModels/llama3.1.so
The generated DSO model can be found at: /home/ubuntu/torchchat/exportedModels/llama3.1.so
```

### Running LLM Inference on Arm CPU
You can now run the LLM on the Arm CPU on your server.

To run the model inference:

```sh
LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libtcmalloc.so.4 TORCHINDUCTOR_CPP_WRAPPER=1 TORCHINDUCTOR_FREEZING=1 OMP_NUM_THREADS=16 python torchchat.py generate llama3.1 --dso-path exportedModels/llama3.1.so --device cpu --max-new-tokens 32 --chat
```
The output from running the inference will look like:

```output
PyTorch version 2.5.0.dev20240828+cpu available.
Warning: checkpoint path ignored because an exported DSO or PTE path specified
Warning: checkpoint path ignored because an exported DSO or PTE path specified
Using device=cpu
Loading model...
Time to load model: 0.04 seconds
-----------------------------------------------------------
Starting Interactive Chat
Entering Chat Mode. Will continue chatting back and forth with the language model until the models max context length of 8192 tokens is hit or until the user says /bye
Do you want to enter a system prompt? Enter y for yes and anything else for no.
no
User: What's the weather in Boston like?
Model: Boston, Massachusetts!

Boston's weather is known for being temperamental and unpredictable, especially during the spring and fall months. Here's a breakdown of the typical
=====================================================================
Input tokens        :   18
Generated tokens    :   32
Time to first token :   0.66 s
Prefill Speed       :   27.36 t/s
Generation  Speed   :   24.6 t/s
=====================================================================

Bandwidth achieved: 254.17 GB/s
*** This first iteration will include cold start effects for dynamic import, hardware caches. ***
```

You have successfully run the Llama3.1 8B Instruct Model on your Arm-based server. In the next section, you will walk through the steps to run the same chatbot in your browser. 

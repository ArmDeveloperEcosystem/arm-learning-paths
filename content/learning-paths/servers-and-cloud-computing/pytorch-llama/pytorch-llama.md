---
title: Run a Large Language model (LLM) chatbot on Arm servers
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin
The instructions in this Learning Path are for any Arm server running Ubuntu 22.04 LTS. You need an Arm server inst
ance with at least sixteen cores and 100GB of RAM to run this example. The instructions have been tested on an AWS Graviton3 c7g.8xlarge instance.

## Overview
Arm CPUs are widely used in traditional ML and AI use cases. In this Learning Path, you learn how to run generative AI inference-based use cases like a LLM chatbot using PyTorch on Arm-based CPUs. PyTorch is a popular deep learning framework for AI applications.

This learning path shows you how you can run the Meta Llama 3.1 model using PyTorch on Arm Neoverse V1-based AWS Graviton 3 CPUs with KleidiAI optimizations, showcasing significant performance improvements.

### Install Necessary Tools
First, ensure your system is up-to-date and install the required tools:

```sh
sudo apt-get update
sudo apt install gcc g++ build-essential python3-pip -y
```

### Set Up your Python Virtual Environment
Set up a Python virtual environment to isolate dependencies:

```sh
python3 -m venv torch_env
source torch_env/bin/activate
```

### Install PyTorch and Optimized Libraries
Install the specific version of PyTorch which is provided as a python wheel and the necessary patches for Torchchat and Torchao needed to take advantake of KleidiAI optimizations:

Clone and patch Torchao and Torchchat repositories:

```sh
git clone --recursive https://github.com/pytorch/ao.git
cd ao
git checkout 174e630af2be8cd18bc47c5e530765a82e97f45b
wget https://raw.githubusercontent.com/ArmDeveloperEcosystem/PyTorch-arm-patches/main/0001-Feat-Add-support-for-kleidiai-quantization-schemes.patch
git apply 0001-Feat-Add-support-for-kleidiai-quantization-schemes.patch
cd ../

git clone --recursive https://github.com/pytorch/torchchat.git
cd torchchat
git checkout f384d4ffd42065397d37c71819e3bc578f7c3179
wget https://github.com/ArmDeveloperEcosystem/PyTorch-arm-patches/blob/main/0001-Feat-Enable-int4-quantized-models-to-work-with-pytor.patch
git apply 0001-Feat-Enable-int4-quantized-models-to-work-with-pytor.patch
./install_requirements.sh
```
You will now override the installed PyTorch version with a specific version of PyTorch needed to take advantage of KleidiAI optimizations:

```
wget https://github.com/ArmDeveloperEcosystem/PyTorch-arm-patches/raw/main/torch-2.5.0.dev20240828+cpu-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl
pip install --force-reinstall torch-2.5.0.dev20240828+cpu-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl
pip uninstall torchao && cd ao/ && rm -rf build && python setup.py install
```

### Downloading the Meta Llama 3.1 Model
You are now ready to download the LLM.

Login to the Hugging Face repository and download the Meta Llama 3.1 model:

```sh
pip install huggingface_hub
huggingface-cli login
```
Accept the license agreement at: [Meta Llama 3.1](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct)

### Quantizing the LLM Model

Quantize the model to int 4-bit using Kernels for PyTorch:

```sh
cd torchchat
python torchchat.py export llama3.1 --output-dso-path exportedModels/llama3.1.so --quantize config/data/aarch64_cpu_channelwise.json --device cpu --max-seq-length 2048
```

### Running LLM Inference on Arm CPU
You can now run the LLM on the Arm CPU on your server.

To run the model inference:

```sh
LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libtcmalloc.so.4 TORCHINDUCTOR_CPP_WRAPPER=1 TORCHINDUCTOR_FREEZING=1 OMP_NUM_THREADS=16 python torchchat.py generate llama3 --dso-path exportedModels/llama3.1.so --device cpu --max-new-tokens 32 --chat
```
The output from running the inference will look like:

```output
Moving checkpoint to /home/ubuntu/.torchchat/model-cache/downloads/meta-llama/Meta-Llama-3-8B-Instruct/model.pth.
Done.
PyTorch version 2.5.0.dev20240828+cpu available.
Warning: checkpoint path ignored because an exported DSO or PTE path specified
Warning: checkpoint path ignored because an exported DSO or PTE path specified
Using device=cpu
Loading model...
Time to load model: 0.06 seconds
-----------------------------------------------------------
Starting Interactive Chat
Entering Chat Mode. Will continue chatting back and forth with the language model until the models max context length of 8192 tokens is hit or until the user says /bye
Do you want to enter a system prompt? Enter y for yes and anything else for no.
y
What is your system prompt?
Human
User: Whats the weather in Boston like?
Model: Boston's weather! Boston has a humid continental climate with warm summers and cold winters. Here's a breakdown of the typical weather conditions in Boston:

**Season
=====================================================================
Input tokens        :   23
Generated tokens    :   32
Time to first token :   1.33 s
Prefill Speed       :   17.24 t/s
Generation  Speed   :   16.55 t/s
=====================================================================

Bandwidth achieved: 152.34 GB/s
```

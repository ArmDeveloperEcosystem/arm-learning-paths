---
title: Overview and Environment Setup
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

[vLLM](https://github.com/vllm-project/vllm) is an open-source, high-throughput inference engine designed to  efficiently serve large language models (LLMs). It offers an OpenAI-compatible API, supports dynamic batching, and is optimized for low-latency performance — making it suitable for both real-time and batch inference workloads.

This learning path walks through how to combine vLLM with INT8 quantization techniques to reduce memory usage and improve inference speed, enabling large models like Llama 3.1 to run effectively on Arm-based CPUs. 

The model featured in this guide — [Llama 3.1 8B Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) — is sourced from Hugging Face, quantized using the `llmcompressor`, and deployed using vLLM. 

Testing for this learning path was performed on AWS Graviton instance (c8g.16xlarge). The instructions are intended for Arm-based servers running Ubuntu 24.04 LTS.


## Learning Path Setup

This learning path uses a Python virtual environment (`venv`) to manage dependencies in an isolated workspace. This approach ensures a clean environment, avoids version conflicts, and makes it easy to reproduce results — especially when using custom-built packages like `vLLM` and `PyTorch`.

### Set up the Python environment

To get started, create a virtual environment and activate it as shown below:

```bash
sudo apt update
sudo apt install -y python3 python3-venv
python3 -m venv vllm_env
source vllm_env/bin/activate
pip install --upgrade pip 
```
This will create a local Python environment named (`vllm_env`) and upgrade pip to the latest version.

### Install system dependencies

These packages are needed to build libraries like OpenBLAS and manage system-level performance:

```bash
sudo apt-get update -y
sudo apt-get install -y gcc-12 g++-12 libnuma-dev make
```
Set the system default compilers to version 12:

```bash
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 10 \
  --slave /usr/bin/g++ g++ /usr/bin/g++-12
```
Next, install the  [`tcmalloc memory allocator`](https://docs.vllm.ai/en/latest/getting_started/installation/cpu.html?device=arm), which helps improve performance during inference:

```bash
sudo apt-get install libtcmalloc-minimal4
```
This library will be preloaded during model serving to reduce latency and improve memory efficiency.

### Install OpenBLAS

OpenBLAS is an optimized linear algebra library that improves performance for matrix-heavy operations, which are common in LLM inference. To get the best performance on Arm CPUs, it's recommended to build OpenBLAS from source.

Run these commands to clone and build OpenBLAS:
```bash
git clone https://github.com/OpenMathLib/OpenBLAS.git
cd OpenBLAS
git checkout ef9e3f715
```
{{% notice Note %}}
This commit is known to work reliably with Arm CPU optimizations (BF16, OpenMP) and has been tested in this learning path. Using it ensures consistent behavior. You can try `main`, but newer commits may introduce changes that haven't been validated here.
{{% /notice %}}

```bash
make -j$(nproc) BUILD_BFLOAT16=1 USE_OPENMP=1 NO_SHARED=0 DYNAMIC_ARCH=1 TARGET=ARMV8 CFLAGS=-O3
make -j$(nproc) BUILD_BFLOAT16=1 USE_OPENMP=1 NO_SHARED=0 DYNAMIC_ARCH=1 TARGET=ARMV8 CFLAGS=-O3 PREFIX=/home/ubuntu/OpenBLAS/dist install
```
This will build and install OpenBLAS into `/home/ubuntu/OpenBLAS/dist` with optimizations for Arm CPUs.

### Install Python dependencies

Once the system libraries are in place, install the Python packages required for model quantization and serving. You’ll use prebuilt CPU wheels for vLLM and PyTorch, and install additional tools like `llmcompressor` and `torchvision`.

Before proceeding, make sure the following files are downloaded to your home directory:
```bash
[PLACEHOLDER]
```
These are required to complete the installation and model quantization steps.
Now, navigate to your home directory:
```bash
cd $HOME
```

Install the vLLM wheel. This wheel contains the  CPU-optimized version of `vLLM`, built specifically for Arm architecture. Installing it from a local `.whl` file ensures compatibility with the rest of your environment and avoids potential conflicts from nightly or default pip installations.

```bash
pip install vllm-0.7.3.dev151+gfaee222b.cpu-cp312-cp312-linux_aarch64.whl --force-reinstall
```
Install `llmcompressor`, which is used to quantize the model:
```bash
pip install llmcompressor
```
Install torchvision (nightly version for CPU):
```bash
pip install --force-reinstall torchvision==0.22.0.dev20250223 --extra-index-url https://download.pytorch.org/whl/nightly/cpu```

Install the custom PyTorch CPU wheel:<br>
This custom PyTorch wheel is prebuilt for Arm CPU architectures and includes the necessary optimizations for running inference. Installing it locally ensures compatibility with your environment and avoids conflicts with default pip packages.
```bash
pip install torch-2.7.0.dev20250306-cp312-cp312-manylinux_2_28_aarch64.whl --force-reinstall --no-deps
```

You’re now ready to quantize the model and start serving it with `vLLM` on an Arm-based system.

---
title: Build a vLLM from Source Code
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin

To follow the instructions for this Learning Path, you will need an Arm server running Ubuntu 24.04 LTS with at least 8 cores, 16GB of RAM, and 50GB of disk storage.

## What is vLLM?

[vLLM](https://github.com/vllm-project/vllm) stands for Virtual Large Language Model, and is a fast and easy-to-use library for inference and model serving. 

You can use vLLM in batch mode, or by running an OpenAI-compatible server. 

In this Learning Path, you will learn how to build vLLM from source and run inference on an Arm-based server, highlighting its effectiveness.

### What software do I need to install to build vLLM?

First, ensure your system is up-to-date and install the required tools and libraries:

```bash
sudo apt-get update -y 
sudo apt-get install -y curl ccache git wget vim numactl gcc-12 g++-12 python3 python3-pip python3-venv python-is-python3 libtcmalloc-minimal4 libnuma-dev ffmpeg libsm6 libxext6 libgl1 libssl-dev pkg-config 
```

Set the default GCC to version 12:

```bash
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 10 --slave /usr/bin/g++ g++ /usr/bin/g++-12
```

Next, install Rust. For more information, see the [Rust install guide](/install-guides/rust/).

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
source "$HOME/.cargo/env"
```

Four environment variables are required. You can enter these at the command line or add them to your `$HOME/.bashrc` file and source the file.

To add them at the command line, use the following:

```bash
export CCACHE_DIR=/home/ubuntu/.cache/ccache
export CMAKE_CXX_COMPILER_LAUNCHER=ccache
export VLLM_CPU_DISABLE_AVX512="true"
export LD_PRELOAD="/usr/lib/aarch64-linux-gnu/libtcmalloc_minimal.so.4"
```

Create and activate a Python virtual environment:

```bash
python -m venv env
source env/bin/activate
```

Your command-line prompt is prefixed by `(env)`, which indicates that you are in the Python virtual environment. 

Now update Pip and install Python packages:

```bash
pip install --upgrade pip
pip install py-cpuinfo
```

### How do I download vLLM and build it? 

First, clone the vLLM repository from GitHub:

```bash
git clone https://github.com/vllm-project/vllm.git
cd vllm
git checkout 72ff3a968682e6a3f7620ab59f2baf5e8eb2777b
```

{{% notice Note %}}
The Git checkout specifies a specific hash known to work for this example. 

Omit this command to use the latest code on the main branch. 
{{% /notice %}}

Install the Python packages for vLLM:

```bash
pip install -r requirements-build.txt
pip install -v -r requirements-cpu.txt
```

Build vLLM using Pip:

```bash
VLLM_TARGET_DEVICE=cpu python3 setup.py bdist_wheel
pip install dist/*.whl
```

When the build completes, navigate out of the repository:

```bash
rm -rf dist
cd ..
```

You are now ready to download an LLM and run vLLM.

---
title: Build a vLLM from source code
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin

[Virtual Large Language Model (vLLM)](https://github.com/vllm-project/vllm) is a fast and easy-to-use library for inference and model serving.

You can use vLLM in batch mode, or by running an OpenAI-compatible server.

In this Learning Path, you'll learn how to build vLLM from source and run inference on an Arm-based server.

Start by checking if your system includes BFloat16 using the `lscpu` command:

```console
lscpu | grep bf16
```

If you have a processor with BFloat16, the output is similar to:

```output
Flags: fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma lrcpc dcpop sha3 asimddp sha512 sve asimdfhm dit uscat ilrcpc flagm sb paca pacg dcpodp sve2 sveaes svepmull svebitperm svesha3 flagm2 frint svei8mm svebf16 i8mm bf16 dgh rng bti
```

If the output is blank, you don't have a processor with BFloat16.

BFloat16 provides improved performance and smaller memory footprint with the same dynamic range. You might experience a drop in model inference accuracy with BFloat16, but the tradeoff is acceptable for the majority of applications.

The instructions in this Learning Path have been tested on an AWS Graviton3 `m7g.2xlarge` instance.

## Install dependencies to build vLLM

After validating that your system supports BFloat16, install vLLM dependencies. 

First, ensure your system is up-to-date and install the required tools and libraries:

```bash
sudo apt-get update -y
sudo apt-get install -y curl ccache git wget vim numactl gcc g++ python3 python3-pip python3-venv python-is-python3 libtcmalloc-minimal4 libnuma-dev ffmpeg libsm6 libxext6 libgl1 libssl-dev pkg-config
```

Next, install Rust. For installation steps, see the [Rust install guide](/install-guides/rust/).

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
source "$HOME/.cargo/env"
```

Next, set up required environment variables. You can either enter the variables at the command line or add them to your `$HOME/.bashrc` file and source the file.

To add the environment variables at the command line, run:

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

Now update `pip` and install Python packages:

```bash
pip install --upgrade pip
pip install py-cpuinfo
```

## Download and build vLLM 

First, clone the vLLM repository from GitHub:

```bash
git clone https://github.com/vllm-project/vllm.git
cd vllm
git checkout releases/v0.11.0 
```

{{% notice Note %}}
The Git checkout specifies a version known to work for this example.

Omit this checkout command to use the latest code on the main branch.
{{% /notice %}}

Install the Python packages for vLLM:

```bash
pip install -r requirements/build.txt
pip install -v -r requirements/cpu.txt
```

Build vLLM using `pip`:

```bash
VLLM_TARGET_DEVICE=cpu python3 setup.py bdist_wheel
pip install dist/*.whl
```

When the build completes, navigate out of the repository:

```bash
rm -rf dist
cd ..
```

## What you've accomplished and what's next

You have verified BFloat16 support, installed the build dependencies, configured the required environment variables, and built vLLM from source for the CPU backend.

Next, you'll use vLLM with a Hugging Face model to run batch inference on your Arm server.

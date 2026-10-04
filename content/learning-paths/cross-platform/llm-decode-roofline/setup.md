---
title: Build llama.cpp and install llama-roofline
description: Check the Arm CPU features, build the llama.cpp llama-bench tool, download three Qwen2.5 GGUF models, and install llama-roofline from PyPI on a Raspberry Pi 5 or another Arm Linux system.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Check the Arm architecture features

Confirm that you are on a 64-bit Arm system and list the CPU features:

```bash
uname -m
grep -m1 Features /proc/cpuinfo
```

On a Raspberry Pi 5 the output is:

```output
aarch64
Features	: fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm lrcpc dcpop asimddp
```

The `asimd` flag is NEON and `asimddp` is the DotProd extension. llama.cpp detects DotProd when you build it and uses it for its quantized kernels on the Cortex-A76. The Pi 5 does not have `i8mm` or `sve`, which some newer Arm cores provide.

## Install the build tools

```bash
sudo apt update
sudo apt install -y git cmake build-essential python3-venv python3-pip
```

## Build llama-bench

You only need the `llama-bench` tool from llama.cpp. Building one target, with one compile job, keeps memory use low on a 2 GB board:

```bash
cd $HOME
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp
git rev-parse --short HEAD
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --target llama-bench -j 1
```

On the Raspberry Pi 5 used for this Learning Path, the clone and build took about 11 minutes.

{{% notice Note %}}
On a board with more memory you can raise `-j` to the number of cores to build faster. On a 2 GB Raspberry Pi 5, keep `-j 1`. Parallel compilation of large llama.cpp source files can exhaust memory and make the board unresponsive.
{{% /notice %}}

Record the commit hash printed by `git rev-parse`. You need it when you compare results with anyone else. The outputs in this Learning Path come from llama.cpp commit `836d571`.

To confirm that the build enabled DotProd, look in the output of the `cmake -B build` command for the line that starts with `-- Adding CPU backend variant`. On the Raspberry Pi 5 it is:

```output
-- Adding CPU backend variant ggml-cpu: -U__ARM_FEATURE_MATMUL_INT8;-U__ARM_FEATURE_SVE;-mcpu=cortex-a76+crypto+dotprod+noi8mm+nosve
```

Check that the build works:

```bash
./build/bin/llama-bench --help | head -5
```

The output is similar to:

```output
usage: ./build/bin/llama-bench [options]

options:
  -h, --help
  --version                                   show version and build info
```

## Download three models

The tool fits a line through several models of different sizes, so you need at least three. Use the official Qwen2.5 GGUF files, which are not gated and fit in 2 GB of RAM:

```bash
mkdir -p $HOME/models && cd $HOME/models
wget https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF/resolve/main/qwen2.5-0.5b-instruct-q4_0.gguf
wget https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF/resolve/main/qwen2.5-0.5b-instruct-q8_0.gguf
wget https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct-GGUF/resolve/main/qwen2.5-1.5b-instruct-q4_0.gguf
ls -l *.gguf
```

The output is similar to the following, with your user name and dates. The byte counts must match exactly:

```output
-rw-r--r-- 1 manu manu  428730208 Oct  4 00:10 qwen2.5-0.5b-instruct-q4_0.gguf
-rw-r--r-- 1 manu manu  675710816 Oct  4 00:11 qwen2.5-0.5b-instruct-q8_0.gguf
-rw-r--r-- 1 manu manu 1066227232 Oct  4 00:13 qwen2.5-1.5b-instruct-q4_0.gguf
```

{{% notice Note %}}
Use files from the same publisher and the same conversion pipeline when you compare them. Two files with the same format label can contain different tensor types, depending on how they were produced, and that changes their speed.
{{% /notice %}}

## Install llama-roofline

Create a virtual environment and install the tool from PyPI:

```bash
python3 -m venv $HOME/roofline-venv
source $HOME/roofline-venv/bin/activate
pip install llama-roofline
llama-roofline --version
```

The output is similar to:

```output
llama-roofline 0.2.0
```

## What you've accomplished

You have built `llama-bench`, downloaded three models of different sizes, and installed llama-roofline. Next, you measure the memory bandwidth ceiling of your system.

---
title: Litespark-Inference
draft: true

description: Install Litespark-Inference on Arm or x86 Linux and Apple silicon macOS to run BitNet ternary LLMs on the CPU.

minutes_to_complete: 10

author:
    - Nii Osae Osae Dade
    - Tony Morri
    - Sayandip Pal
official_docs: https://github.com/Mindbeam-AI/Litespark-Inference


additional_search_terms:
- BitNet
- ternary
- LLM
- inference
- CPU
- Arm
- Graviton
- Apple Silicon
- Python

multi_install: false
multitool_install_part: false

test_images:
- ubuntu:latest
test_link: null
test_maintenance: true

tool_install: true
weight: 1
layout: installtoolsall
---

[Litespark-Inference](https://github.com/Mindbeam-AI/Litespark-Inference)
is an open-source CPU inference runtime for
[BitNet b1.58](https://arxiv.org/abs/2402.17764) ternary-weight LLMs. A
single `pip install` reads your CPU's feature flags and compiles the
right C++ kernel for it using NEON and SDOT on Arm or AVX-512/VNNI and AVX2+FMA
on x86. This saves you from needing to pick the right C++ kernel for best performance. 

## What do I need before installing Litespark-Inference?

- Python 3.10 or newer, you can run `python3 --version` to check your version
- A C++ toolchain such as `clang` or `g++`
- About 5 GB of free disk

The BitNet-2B model is downloaded from Hugging Face on your first run.

It is good practice to install into a clean virtual environment so the
install does not conflict with anything else on your machine:

If you don't have Python virtual environment support installed run:

```bash
sudo apt update
sudo apt install python3-venv -y
```

Create a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip wheel setuptools
```

Next, follow the section for your platform, Linux or macOS.

## How do I install Litespark-Inference on Arm Linux?

The released package builds the correct kernel for your CPU
automatically. It uses NEON and 
SDOT on Arm (Graviton 2/3/4, Ampere, Neoverse N1/N2/V1/V2, Raspberry
Pi 5). 

For Ubuntu/Debian distributions, install the C++ toolchain, then the Litespark-Inference Python package:

```bash
sudo apt-get update
sudo apt-get install -y build-essential clang ninja-build git python3-pip
pip install litespark-inference
```

For Red Hat, Fedora, or RHEL, install the toolchain with `dnf` instead:

```console
sudo dnf install -y gcc-c++ clang ninja-build git python3-pip
pip install litespark-inference
```

Confirm the package imports and reports the kernel selected for your CPU:

```bash
python3 -c "import litespark_inference; print(litespark_inference.__version__)"
```

The version is printed:

```output
1.0.3
```

To inspect which kernel was built, run:

```bash
python -m litespark_inference.torchless info
```

The output ends with one of the following, depending on your CPU:

```output
litespark_inference.torchless
  platform : Linux aarch64
  python   : 3.12.3
  kernel   : /home/ubuntu/.venv/lib/python3.12/site-packages/litespark_inference/torchless/_matmul_lut_neon.cpython-312-aarch64-linux-gnu.so
  OpenMP   : True  (max_threads=8)
  Accelerate: False
```

## How do I install Litespark-Inference on Apple silicon macOS?

Apple's CPUs have NEON SDOT and Litespark-Inference uses it directly.

The only extra step versus Linux is installing `libomp`, Apple's
toolchain does not ship a built-in OpenMP runtime, and Litespark uses
OpenMP for multi-threading inside the kernel.

Install Xcode command-line tools, the full Xcode is not required: 

```console
xcode-select --install
brew install libomp
pip install litespark-inference
```

Verify the install:

```console
python -m litespark_inference.torchless info
```

The expected output includes:

```output
litespark_inference.torchless
  platform : Darwin arm64
  python   : 3.14.5
  kernel   : .venv/lib/python3.14/site-packages/litespark_inference/torchless/_matmul_lut_neon.cpython-314-darwin.so
  OpenMP   : True  (max_threads=12)
  Accelerate: True
```

If you see `OpenMP : False`, the build did not find Homebrew's `libomp`. The
most common cause is that Homebrew is installed under `/opt/homebrew`
(the Apple Silicon default) but `pip install` ran in an environment that
hides it. Re-run `pip install litespark-inference` from a normal
shell to fix it.

## How do I install from source?

To modify the runtime or kernels, install from source instead of from
PyPI:

```console
git clone https://github.com/Mindbeam-AI/Litespark-Inference.git
cd Litespark-Inference
pip install -e .
```

## Sanity-check

On all platforms, the same command can be used. 

The first run downloads the model weights (around 4.5 GB into
`~/.cache/huggingface/hub`). Subsequent runs do not need to download
again.

```console
litespark-inference generate "Hello, world!" --max-tokens 16
```

The output is similar to:

```output
Prompt (36 tokens): 'System: You are Litespark, a helpful AI assistant running locally. Provide accurate, concise, and practical answers.<|eot_id|>User: Hello, world!<|eot_id|>Assistant: '
Prefill...
  36 tokens in 0.40s (90.09 tok/s)
Generate:
Hello! How can I assist you today?

Generated 9 tokens in 0.29s (31.58 tok/s)

--- output ---
Hello! How can I assist you today?
```

You are now ready to run BitNet-2B.

Continue with [Accelerate LLM inference on Arm CPUs with Litespark-Inference](/learning-paths/laptops-and-desktops/litespark-inference/) to learn more. 

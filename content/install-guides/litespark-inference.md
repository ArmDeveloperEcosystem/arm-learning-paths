---
additional_search_terms:
- BitNet
- ternary
- LLM
- inference
- CPU
- Arm
- Graviton
- Apple silicon
- Python

layout: installtoolsall
minutes_to_complete: 10
author:
    - Nii Osae Osae Dade
    - Tony Morri
    - Sayandip Pal
multi_install: false
multitool_install_part: false
official_docs: https://github.com/Mindbeam-AI/Litespark-Inference
test_images:
- ubuntu:latest
test_link: null
test_maintenance: true
title: Litespark-Inference
description: Install Litespark-Inference on Arm or x86 Linux and Apple silicon macOS to run BitNet ternary LLMs on the CPU.
tool_install: true
weight: 1
---

[Litespark-Inference](https://github.com/Mindbeam-AI/Litespark-Inference)
is an open-source CPU inference runtime for
[BitNet b1.58](https://arxiv.org/abs/2402.17764) ternary-weight LLMs. A
single `pip install` reads your CPU's feature flags and compiles the
right C++ kernel for it - NEON + SDOT on Arm, AVX-512/VNNI or AVX2+FMA
on x86. You do not pick the kernel; it picks itself.

## What do I need before installing Litespark-Inference?

- **Python 3.10 or newer.** Check with `python3 --version`.
- **A C++ toolchain** (`clang` or `g++`). Already present on most
  developer machines; install steps per platform are below.
- **About 5 GB of free disk.** The BitNet-2B model downloads from
  Hugging Face on first run.

It is good practice to install into a clean virtual environment so the
install does not conflict with anything else on your machine:

```console
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip wheel setuptools
```

Then follow the section for your platform.

## How do I install Litespark-Inference on Arm or x86 Linux?

The released package builds the correct kernel for your CPU
automatically - AVX-512 with an AVX2+FMA fallback on x86, and NEON +
SDOT on Arm (Graviton 2/3/4, Ampere, Neoverse N1/N2/V1/V2, Raspberry
Pi 5). Install the C++ toolchain, then the package:

```bash
sudo apt-get update
sudo apt-get install -y build-essential clang ninja-build git python3-pip
pip install litespark-inference
```

For Red Hat, Fedora, or RHEL, install the toolchain with `dnf` instead:

```console
sudo dnf install -y gcc-c++ clang ninja-build git python3-pip
```

Confirm the package imports and reports the kernel selected for your CPU:

```bash
python3 -c "import litespark_inference; print(litespark_inference.__version__)"
```

To inspect which kernel was built, run:

```console
python -m litespark_inference.torchless info
```

The output ends with one of the following, depending on your CPU:

```output
kernel : avx512 (torchless, extern "C" AVX-512/VNNI + OMP)
kernel : avx2 (torchless, extern "C" AVX2+FMA fallback + OMP)
kernel : neon (torchless, extern "C" NEON SDOT)
```

## How do I install Litespark-Inference on Apple silicon macOS?

Apple's CPUs have NEON SDOT and Litespark-Inference uses it directly.
The only extra step versus Linux is installing `libomp` - Apple's
toolchain does not ship a built-in OpenMP runtime, and Litespark uses
OpenMP for multi-threading inside the kernel:

```console
# Xcode command-line tools (one-time setup; no full Xcode required)
xcode-select --install

# libomp via Homebrew
brew install libomp

# Install the released package from PyPI
pip install litespark-inference
```

Verify the install:

```console
python -m litespark_inference.torchless info
```

Expected output includes:

```output
kernel : neon (torchless, extern "C" NEON SDOT)
OpenMP : True  (max_threads=...)
```

If `OpenMP : False`, the build did not find Homebrew's `libomp`. The
most common cause is that Homebrew is installed under `/opt/homebrew`
(the Apple silicon default) but `pip install` ran in an environment that
hides it. Re-running `pip install litespark-inference` from a normal
shell usually fixes it.

## How do I install from source?

To modify the runtime or kernels, install from source instead of from
PyPI:

```console
git clone https://github.com/Mindbeam-AI/Litespark-Inference.git
cd Litespark-Inference
pip install -e .
```

## Sanity-check

On all platforms, the same one-liner generates text. The first run
downloads `microsoft/bitnet-b1.58-2B-4T-bf16` from Hugging Face (around
4.5 GB into `~/.cache/huggingface/hub`); later runs start instantly:

```console
litespark-inference generate "Hello, world!" --max-tokens 16
```

You are now ready to run BitNet-2B. Continue with the
[Accelerate LLM inference on Arm CPUs with Litespark-Inference](/learning-paths/laptops-and-desktops/litespark-inference/)
Learning Path.

---
title: Install ExecuTorch and download the model
description: Clone the ExecuTorch release branch, create the Python environment, and fetch the gated Llama 3.2 model files.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Clone ExecuTorch 1.4

Keep a source checkout because you will cross-compile the Android runtime and the standalone Llama runner:

```bash
cd ~
git clone --branch release/1.4 --recursive https://github.com/pytorch/executorch.git
cd executorch
git submodule update --init --recursive
```

Create and activate a Python virtual environment:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
```

To reduce memory pressure during builds:

```bash
export CMAKE_BUILD_PARALLEL_LEVEL=2
```

## Fix the PyTorch version mismatch

On the tested `release/1.4` branch, a host environment with PyTorch `2.14.0+cpu` broke the build with:

```text
ATen/core/Tensor.h:70:37: error: 'C10_LIFETIMEBOUND' does not name a type
```

Pin the expected version explicitly:

```bash
python -m pip uninstall -y torch
python -m pip install "torch==2.13.0+cpu" --index-url https://download.pytorch.org/whl/cpu
python -c "import torch; print(torch.__version__)"
```

Expected output:

```text
2.13.0+cpu
```

Then clean and rebuild the host package:

```bash
python install_executorch.py --clean
export CMAKE_BUILD_PARALLEL_LEVEL=2
./install_executorch.sh --use-pt-pinned-commit
```

The important lesson is to verify `torch.__version__` before you start a long native build.

## Download Llama 3.2 1B Instruct

The model used in this workflow came from the gated Hugging Face repository `meta-llama/Llama-3.2-1B-Instruct`.

Keep the model outside the source tree:

```bash
hf auth login
hf download \
  meta-llama/Llama-3.2-1B-Instruct \
  --include "original/*" \
  --local-dir ~/Llama-3.2-1B-Instruct
```

You need these files:

```text
~/Llama-3.2-1B-Instruct/original/consolidated.00.pth
~/Llama-3.2-1B-Instruct/original/params.json
~/Llama-3.2-1B-Instruct/original/tokenizer.model
```

The measured run used:

- `consolidated.00.pth` at about 2.4 GB
- `params.json`
- `tokenizer.model` at about 2.1 MB

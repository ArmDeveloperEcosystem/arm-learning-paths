---
title: Set up the environment
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install the required tools

We'll need `git` to clone the ExecuTorch repository, `curl` to fetch the project archive, a C++ build toolchain, and a Python3.12 virtual environment:

```bash
sudo apt update
sudo apt install -y \
    git \
    curl \
    build-essential \
    python3.12 \
    python3.12-dev \
    python3.12-venv
```

## Download the project files

Create a working directory and download the project files for this Learning
Path:

```bash
mkdir smolvla-executorch-conversion-work
cd smolvla-executorch-conversion-work
curl -fL --retry 3 \
    -o smolvla-executorch-conversion.tar.gz \
    'https://gitlab.arm.com/learning-code-examples/code-examples/-/archive/main/code-examples-main.tar.gz?path=learning-paths/laptops-and-desktops/smolvla-executorch-conversion'
mkdir smolvla-executorch-conversion
tar xfz smolvla-executorch-conversion.tar.gz \
    --strip-components=4 \
    -C smolvla-executorch-conversion
cd smolvla-executorch-conversion
```


## Set up the software environment
The `setup.sh` script:
- Pins ExecuTorch v1.4.1 at commit `e4d02f41f7909e8ed5bf4a14ffc520d733453d9f`.
- Builds the ExecuTorch and XNNPACK + KleidiAI runtime libraries and Python bindings.
- Installs relevant Python packages.
- Downloads the pinned SmolVLA checkpoint from Hugging Face.
- Creates a project-local virtual environment `.venv`.

```bash
./scripts/setup.sh
```
Activate the virtual environment and resolve repository-local path variables with:
```bash
source env.sh
```

## Verify the resources

Verify the pinned packages, ExecuTorch revision and Python binding, XNNPACK and KleidiAI runtime build, and SmolVLA checkpoint files:

```bash
python scripts/check_environment.py
```

A successful check looks like:

```output
Environment OK: aarch64, ExecuTorch e4d02f41
  Python: /path/to/smolvla-executorch-conversion/.venv/bin/python
  ExecuTorch: /path/to/smolvla-executorch-conversion/toolchain/executorch
  Runtime: /path/to/smolvla-executorch-conversion/toolchain/executorch/cmake-out-xnnpack
  Checkpoint: /path/to/smolvla-executorch-conversion/checkpoints/smolvla_base
```


## What you've accomplished and what's next
You have obtained the scripts to convert the model, built the ExecuTorch runtime and configured your environment.

Next, you'll work through the ExecuTorch pipeline to export and lower the FP32 SmolVLA for Arm CPU, and validate the converted model against the PyTorch reference.

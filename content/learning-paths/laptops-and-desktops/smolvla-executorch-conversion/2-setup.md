---
title: Set up the SmolVLA ExecuTorch environment
description: Set up Python, ExecuTorch, XNNPACK, and the SmolVLA resources needed to convert and run the model on an Arm CPU.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install the required tools

Install `git` to clone the ExecuTorch repository, `curl` to fetch project files, and a C++ build toolchain:

```bash
sudo apt update
sudo apt install -y \
    git \
    curl \
    build-essential
```

The project uses Python 3.12. Install [uv](https://docs.astral.sh/uv/) and use it to install Python 3.12 independently of the Python version provided by your Ubuntu release:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source "$HOME/.local/bin/env"
uv python install 3.12
```

Confirm that Python 3.12 is available:

```bash
python3.12 --version
```

The output is similar to:

```output
Python 3.12.14
```

## Download the project files

Create a working directory and download the project files for this Learning
Path:

```bash
mkdir -p smolvla-executorch-conversion-work
cd smolvla-executorch-conversion-work
curl -fL --retry 3 \
    -o smolvla-executorch-conversion.tar.gz \
    'https://gitlab.arm.com/learning-code-examples/code-examples/-/archive/main/code-examples-main.tar.gz?path=learning-paths/laptops-and-desktops/smolvla-executorch-conversion'
mkdir -p smolvla-executorch-conversion
tar xfz smolvla-executorch-conversion.tar.gz \
    --strip-components=4 \
    -C smolvla-executorch-conversion
cd smolvla-executorch-conversion
```

## Set up the software environment

The `setup.sh` script does the following:

- Creates a project-local virtual environment in `.venv`
- Pins ExecuTorch v1.4.1 at commit `e4d02f41f7909e8ed5bf4a14ffc520d733453d9f`
- Builds the ExecuTorch and XNNPACK runtime libraries with KleidiAI support and the Python bindings
- Installs the required Python packages
- Downloads the pinned SmolVLA checkpoint from Hugging Face

Run the setup script:

```bash
./scripts/setup.sh
```

The script downloads several gigabytes and compiles native libraries. The download can take 30 minutes or longer on systems with a small number of CPU cores.

Activate the virtual environment and resolve repository-local path variables:

```bash
source env.sh
```

## Verify the resources

Verify the pinned packages, ExecuTorch revision and Python binding, XNNPACK runtime build with KleidiAI support, and SmolVLA checkpoint files:

```bash
python scripts/check_environment.py
```

The output of a successful check is similar to:

```output
Environment OK: aarch64, ExecuTorch e4d02f41
  Python: /path/to/smolvla-executorch-conversion/.venv/bin/python
  ExecuTorch: /path/to/smolvla-executorch-conversion/toolchain/executorch
  Runtime: /path/to/smolvla-executorch-conversion/toolchain/executorch/cmake-out-xnnpack
  Checkpoint: /path/to/smolvla-executorch-conversion/checkpoints/smolvla_base
```

## What you've accomplished and what's next

You've downloaded the scripts to convert the model, built the ExecuTorch runtime, and configured your environment.

Next, you'll export and lower the FP32 SmolVLA for an Arm CPU and validate the converted model against the PyTorch reference.

---
title: Setup PyTorch and DeepSpeed on GCP Axion (Arm)
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Setup PyTorch and DeepSpeed on GCP Axion (Arm)

This section guides you through setting up a Python AI/ML environment on a Google Cloud Axion Arm64 VM using SUSE Linux Enterprise Server.

The setup validates:

- PyTorch execution on Arm64
- DeepSpeed installation in compatibility mode
- CPU-only AI/ML runtime configuration
- Arm64 AI development environment preparation

## Learning Objectives

- Verify Arm64 environment
- Configure Python 3.11
- Create Python virtual environment
- Install PyTorch on Arm
- Install DeepSpeed in compatibility mode
- Validate AI/ML environment setup
- Understand DeepSpeed limitations on SUSE Arm64


## Verify ARM64 architecture

Verify that the VM is running on Arm64 architecture.

```bash
uname -m
```

Expected output:

```text
aarch64
```

Check CPU details:

```bash
lscpu
```


## Install Python 
Deep learning frameworks such as PyTorch and DeepSpeed work more reliably with modern Python versions.

```bash
sudo zypper install -y python311 python311-pip python311-devel
```

## Why Python 3.11 is used

Python 3.11 provides:

- Better runtime performance
- Improved package compatibility
- Stable PyTorch support
- Better support for AI/ML frameworks

Using Python 3.11 avoids compatibility issues commonly seen with older Python releases.

## Create Python virtual environment
Create an isolated Python environment to prevent dependency conflicts with system packages.

```bash
python3.11 -m venv deepspeed-env
```

Activate environment:

```bash
source ~/deepspeed-env/bin/activate
```

Verify:

```bash
python --version
```


## Upgrade Python tools
Upgrade Python package management tools.

```bash
pip install --upgrade pip setuptools wheel
```

## Why this step is important

Updated packaging tools help:

- Avoid installation failures
- Improve wheel compatibility
- Reduce dependency resolution issues
- Improve Arm64 package installation reliability

## Install Ninja

Install Ninja using pip instead of zypper.

```bash
pip install ninja
```

Verify:

```bash
ninja --version
```

The output is similar to:
```output
1.13.0.git.kitware.jobserver-pipe-1
```

Ninja is a lightweight build system used by:

- PyTorch
- DeepSpeed
- native extension compilation workflows

Using pip avoids SUSE repository dependency issues sometimes observed on cloud Arm64 images.


## Install CPU-only PyTorch
Install CPU-only PyTorch packages:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

## Why CPU-only PyTorch is used

GCP Axion VMs are CPU-only systems and do not contain NVIDIA GPUs.

The CPU-only build:

- Reduces package size
- Avoids unnecessary CUDA dependencies
- Improves installation stability
- Matches the Axion hardware architecture

## Verify PyTorch installation

```bash
python -c "import torch; print(torch.__version__)"
```

The output is similar to:
```output
2.11.0+cpu
```

Check CUDA availability:

```bash
python -c "import torch; print(torch.cuda.is_available())"
```

The output is similar to:
```output
False
```

This is expected because GCP Axion VMs are CPU-only systems.


## DeepSpeed limitation on SUSE Arm64

DeepSpeed distributed CPU extensions require newer GCC versions.

Default SUSE Arm64 images typically include:

```bash
GCC 7.x
```

However, DeepSpeed native communication extensions require:

```bash
GCC 9+
```

DeepSpeed attempts to compile:

```bash
deepspeed_shm_comm
```

during launcher initialization.

Because of this limitation, install DeepSpeed in compatibility mode without native extension compilation.

## Install DeepSpeed

DeepSpeed distributed CPU extensions require newer GCC versions.

Since default SUSE Arm64 images use GCC 7.x, install DeepSpeed without native extension compilation.

Export environment variables:

```bash
export DS_BUILD_OPS=0
export DS_BUILD_SHM_COMM=0
export DS_BUILD_CPU_ADAM=0
export DS_BUILD_AIO=0
```

## What these variables do

| Variable | Purpose |
|---|---|
| DS_BUILD_OPS=0 | Disables native op compilation |
| DS_BUILD_SHM_COMM=0 | Disables shared memory communication extension |
| DS_BUILD_CPU_ADAM=0 | Disables CPU Adam optimizer compilation |
| DS_BUILD_AIO=0 | Disables async I/O extensions |

This prevents DeepSpeed from compiling unsupported native CPU extensions on SUSE Arm64.

## Install DeepSpeed:

```bash
DS_BUILD_OPS=0 pip install deepspeed
```


## Verify DeepSpeed installation

```bash
ds_report
```

The output is similar to:

```output
[NO] ....... [OKAY]
```

This is expected on CPU-only Arm64 environments.


## Create project directory

```bash
mkdir ~/deepspeed-demo

cd ~/deepspeed-demo
```

## Important note

Do NOT run:

```bash
deepspeed train.py
```

on this VM because DeepSpeed attempts to compile native CPU communication extensions which require GCC 9 or later.


## Troubleshooting

### SUSE repository refresh issue

You may encounter:

```text
Receive: script died unexpectedly
```

If this occurs:

- Continue if Python 3.11 is already installed
- Install Python packages using `pip`
- Avoid dependency on SUSE development repositories


## What you've learned

You have learned how to:

- Verify Arm64 environment
- Configure Python 3.11
- Create isolated AI/ML environments
- Install PyTorch on Arm64
- Install DeepSpeed in compatibility mode
- Handle GCC limitations on SUSE Arm64
- Prepare AI training environments on GCP Axion


## Next

You will:

- Build AI training workloads
- Run neural network training
- Benchmark Arm64 AI workloads
- Validate CPU training performance

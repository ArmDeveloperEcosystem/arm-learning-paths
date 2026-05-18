---
title: Set up PyTorch and DeepSpeed on an Arm-based Google Axion virtual machine
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up the Python environment

In this section, you'll install Python 3.11, create a virtual environment, and install PyTorch and DeepSpeed on the Google Axion virtual machine (VM) running SUSE Linux.


### Verify ARM64 architecture

Verify that the VM is running on Arm64 architecture:

```bash
uname -m
```

The output is similar to:

```text
aarch64
```

Check CPU details:

```bash
lscpu
```

The output is similar to:

```output
Architecture:                aarch64
  CPU op-mode(s):            64-bit
  Byte Order:                Little Endian
CPU(s):                      4
  On-line CPU(s) list:       0-3
Vendor ID:                   ARM
  Model name:                Neoverse-V2
```

The `Neoverse-V2` model name confirms you're running on a Google Axion processor. The `aarch64` architecture confirms the 64-bit Arm environment that PyTorch and DeepSpeed will target.

### Install Python

The default Python version on SUSE Linux might conflict with PyTorch and DeepSpeed dependencies. Python 3.11 provides stable support for both frameworks and avoids compatibility issues commonly seen with older or newer releases:

```bash
sudo zypper install -y python311 python311-pip python311-devel
```

### Create a Python virtual environment

Create an isolated Python environment to prevent dependency conflicts with system packages:

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

The output is similar to:

```output
Python 3.11.10
```


### Upgrade pip

Upgrade pip, setuptools, and wheel before installing packages. Outdated packaging tools can cause installation failures or wheel compatibility issues, particularly on Arm64:

```bash
pip install --upgrade pip setuptools wheel
```

### Install Ninja

Ninja is a lightweight build system used by PyTorch and DeepSpeed to compile native extensions at runtime. Install it using pip rather than zypper to avoid SUSE repository dependency issues sometimes seen on cloud Arm64 images:

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

### Install CPU-only PyTorch

Google Axion VMs have no GPU, so install the CPU-only PyTorch build. This avoids unnecessary CUDA dependencies and reduces package size:

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

### Verify PyTorch installation

```bash
python -c "import torch; print(torch.__version__)"
```

The output is similar to:
```output
2.12.0+cpu
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

DeepSpeed's distributed CPU extensions require GCC 9 or later to compile. The default SUSE Linux image on GCP Axion ships with GCC 7.5.0:

```bash
gcc --version
```

```output
gcc (SUSE Linux) 7.5.0
```

When DeepSpeed initializes its launcher, it attempts to compile the `deepspeed_shm_comm` shared memory communication extension. This compilation fails on GCC 7.5.0. To work around this, install DeepSpeed with all native extension compilation disabled.

## Install DeepSpeed

Install DeepSpeed with native extension compilation disabled. Each variable tells the build system to skip a specific extension that requires GCC 9 or later:

| Variable | Purpose |
|---|---|
| `DS_BUILD_OPS=0` | Disables native op compilation |
| `DS_BUILD_SHM_COMM=0` | Disables the shared memory communication extension |
| `DS_BUILD_CPU_ADAM=0` | Disables the CPU Adam optimizer extension |
| `DS_BUILD_AIO=0` | Disables async I/O extensions |

```bash
DS_BUILD_OPS=0 DS_BUILD_SHM_COMM=0 DS_BUILD_CPU_ADAM=0 DS_BUILD_AIO=0 pip install deepspeed
```


## Verify DeepSpeed installation

```bash
ds_report
```

The output is similar to:

```output
[WARNING] Setting accelerator to CPU. If you have GPU or other accelerator, we were unable to detect it.
--------------------------------------------------
DeepSpeed C++/CUDA extension op report
--------------------------------------------------
NOTE: Ops not installed will be just-in-time (JIT) compiled at
      runtime if needed. Op compatibility means that your system
      meet the required dependencies to JIT install the op.
--------------------------------------------------
JIT compiled ops requires ninja
ninja .................. [OKAY]
--------------------------------------------------
op name ................ installed .. compatible
--------------------------------------------------
deepspeed_not_implemented  [NO] ....... [OKAY]
 [WARNING]  async_io requires the dev libaio .so object and headers but these were not found.
 [WARNING]  async_io: please install the libaio-devel package with yum
async_io ............... [NO] ....... [NO]
deepspeed_ccl_comm ..... [NO] ....... [OKAY]
deepspeed_shm_comm ..... [NO] ....... [OKAY]
cpu_adam ............... [NO] ....... [OKAY]
fused_adam ............. [NO] ....... [OKAY]
--------------------------------------------------
DeepSpeed general environment info:
torch install path ............... ['/home/user/deepspeed-env/lib64/python3.11/site-packages/torch']
torch version .................... 2.12.0+cpu
deepspeed install path ........... ['/home/user/deepspeed-env/lib64/python3.11/site-packages/deepspeed']
deepspeed info ................... 0.19.0, unknown, unknown
deepspeed wheel compiled w. ...... torch 0.0
shared memory (/dev/shm) size .... 7.80 GB
```

The CPU accelerator warning is expected — GCP Axion VMs have no GPU. Most ops show `[NO] ... [OKAY]`, meaning they are not pre-installed but are compatible for just-in-time compilation via Ninja if needed at runtime. The one exception is `async_io`, which shows `[NO] ... [NO]` because it requires the `libaio-devel` system package. Since async I/O is not needed for the training workloads in this Learning Path and was disabled with `DS_BUILD_AIO=0`, you can ignore this warning.


## Create a project directory

Create a working directory for your DeepSpeed training scripts:

```bash
mkdir ~/deepspeed-demo
cd ~/deepspeed-demo
```

{{% notice Note %}}
Do not run `deepspeed train.py` directly on this VM. DeepSpeed's launcher attempts to compile the `deepspeed_shm_comm` native extension during initialization, which requires GCC 9 or later. Use `python train.py` instead, as shown in the next section.
{{% /notice %}}


## Troubleshooting

### SUSE repository refresh issue

You may see the following error during `zypper` commands:

```output
Receive: script died unexpectedly
```

If Python 3.11 is already installed when this occurs, you can continue. Install all remaining packages using `pip` inside the virtual environment and avoid relying on SUSE development repositories.


## What you've accomplished and what's next

You've installed Python 3.11, PyTorch, and DeepSpeed on a GCP Axion Arm64 VM running SUSE Linux, verified the environment with `ds_report`, and created the project directory for training scripts. Next, you'll create and run neural network training and benchmarking workloads on the Axion processor.

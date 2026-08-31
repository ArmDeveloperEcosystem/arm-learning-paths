---
title: Prepare the Arm cloud environment
description: Inspect the Arm cloud instance and install PyTorch, BenchMARL, TorchRL, and VMAS.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand the reference environment

This Learning Path trains a multi-agent proximal policy optimization (MAPPO) policy entirely on Arm CPUs. It does not need a GPU.

BenchMARL defines and runs the experiment, TorchRL provides the reinforcement-learning components, and VMAS simulates many navigation worlds in a vectorized PyTorch batch. MAPPO trains an actor that selects each agent's actions and a centralized critic used only during training. The reference configuration shares one actor across all three agents, which makes the later actor-only export possible.

The reference experiment was tested on this AWS configuration:

| Component | Tested configuration |
| --- | --- |
| Instance | `m9g.48xlarge` |
| Processor | AWS Graviton5 |
| Architecture | `aarch64` |
| vCPUs | 192 |
| Memory | 768 GiB |
| Operating system | Ubuntu 24.04 |
| Storage | 512 GB EBS volume |

The M9g instance is EBS-only, so the storage volume is provisioned separately from the instance. The workflow does not depend on an AWS-specific API and can run on other Arm-based cloud instances. A smaller instance uses fewer vectorized environments. The training section explains how to keep the tested 100-batch budget or use an alternative fixed-total-frame budget.

AWS Graviton5 provides one hardware thread per core on this instance. The one-environment-per-workload-CPU rule is still a starting point rather than a fixed mapping, because VMAS processes the environments as tensor batches.

{{% notice Note %}}
The tested configuration is a reproducibility reference, not a measured minimum requirement. Package installation, training logs, and checkpoints need persistent storage, but this Learning Path does not establish 512 GB as the minimum capacity.
{{% /notice %}}

## Inspect the Arm cloud instance

Confirm that the instance uses the Arm64 architecture:

```bash
uname -m
```

The expected output is:

```output
aarch64
```

Display the number of available CPUs:

```bash
nproc
```

You can also inspect the processor topology:

```bash
lscpu
```

Save the CPU count and leave one CPU out of the workload calculation:

```bash
export CORE_COUNT=$(nproc)
export RESERVED_CPUS=1
export WORKLOAD_CPUS=$((CORE_COUNT - RESERVED_CPUS))
test "$WORKLOAD_CPUS" -ge 1 || { echo "This sizing policy needs at least 2 CPUs" >&2; exit 1; }
```

Verify the values:

```bash
echo "TotalCPUs=$CORE_COUNT ReservedCPUs=$RESERVED_CPUS WorkloadCPUs=$WORKLOAD_CPUS"
```

This calculation reduces the size of the PyTorch thread pools and the VMAS batch. It does not pin the workload to specific CPUs or prevent the operating system from scheduling work on them.

## Understand agents and vectorized environments

The agent count and vectorized environment count control different parts of the workload:

- **Agents** are the entities that learn to navigate in one VMAS world.
- **Vectorized environments** are independent copies of that world simulated in parallel.

For example, three agents and 191 environments means that VMAS simulates 191 navigation worlds concurrently, with three agents in each world.

For CPU sampling in this Learning Path, use one VMAS environment for each workload CPU:

```bash
export N_ENVS=$WORKLOAD_CPUS
```

{{% notice Note %}}
This is a workload-sizing policy. VMAS uses vectorized PyTorch operations, so an environment is not permanently mapped to one operating-system thread.
{{% /notice %}}

## Install system packages

Update the package index:

```bash
sudo apt-get update
```

Install Python virtual-environment support:

```bash
sudo apt-get install -y python3.12-venv
```

Install the remaining packages:

```bash
sudo apt-get install -y git build-essential python3-pip python3-dev pkg-config cmake ninja-build ffmpeg libgl1 libegl1 libglu1-mesa mesa-utils
```

Create a Python environment:

```bash
python3.12 -m venv $HOME/venvs/mappo
```

Activate it:

```bash
source $HOME/venvs/mappo/bin/activate
```

Confirm the active Python interpreter:

```bash
which python
```

Upgrade the Python packaging tools:

```bash
python -m pip install --upgrade pip setuptools wheel packaging
```

Install PyTorch:

```bash
python -m pip install torch torchvision torchaudio
```

Verify the installation:

```bash
python -c 'import platform, torch; print("Architecture:", platform.machine()); print("PyTorch:", torch.__version__); print("CUDA available:", torch.cuda.is_available()); print("CUDA device:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "N/A")'
```
On the tested system, the output was:

```output
Architecture: aarch64
PyTorch: 2.13.0+cu130
CUDA available: False
CUDA device: N/A
```

The PyTorch version can differ when you run an unpinned `pip` installation. `CUDA available: False` is expected on the CPU-only M9g instance, even if the wheel version contains a CUDA suffix.

## Install BenchMARL and VMAS

Clone BenchMARL:

```bash
cd $HOME
git clone https://github.com/facebookresearch/BenchMARL.git
cd $HOME/BenchMARL
```

Install BenchMARL and VMAS:

```bash
python -m pip install -e .
python -m pip install vmas
```

Verify the software stack:

```bash
python -c 'import torch, torchrl, benchmarl, vmas; print("PyTorch:", torch.__version__); print("TorchRL: OK"); print("BenchMARL: OK"); print("VMAS: OK")'
```

On the tested system, the output was:

```output
PyTorch: 2.13.0+cu130
TorchRL: OK
BenchMARL: OK
VMAS: OK
```

Record the BenchMARL revision used for the experiment:

```bash
git rev-parse HEAD
```

Keep this revision with your experiment notes so you can reproduce the software environment later.

## What you've accomplished

You have verified the `aarch64` environment, sized the initial VMAS workload, and installed the training stack. Next, you will choose a frame-budgeting method and adapt the vectorized environment count to the available CPUs.

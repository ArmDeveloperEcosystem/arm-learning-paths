---
title: Prepare the Arm cloud environment
description: Inspect the Arm cloud instance and install PyTorch, BenchMARL, TorchRL, and VMAS.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

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

Save the CPU count and reserve one CPU for operating-system and runtime activity:

```bash
export CORE_COUNT=$(nproc)
export RESERVED_CPUS=1
export WORKLOAD_CPUS=$((CORE_COUNT - RESERVED_CPUS))
```

Verify the values:

```bash
echo "TotalCPUs=$CORE_COUNT ReservedCPUs=$RESERVED_CPUS WorkloadCPUs=$WORKLOAD_CPUS"
```

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

Record the BenchMARL revision used for the experiment:

```bash
git rev-parse HEAD
```

Keep this revision with your experiment notes so you can reproduce the software environment later.

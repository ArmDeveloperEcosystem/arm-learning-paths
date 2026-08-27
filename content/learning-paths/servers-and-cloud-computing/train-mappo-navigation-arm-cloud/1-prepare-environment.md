---
title: Prepare the Arm cloud environment
description: Inspect the Arm cloud instance and install PyTorch, BenchMARL, TorchRL, and VMAS.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Inspect the Arm cloud instance

Confirm that the instance reports the `aarch64` architecture:

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
CORE_COUNT="$(nproc)"
export CORE_COUNT
export RESERVED_CPUS=1
export WORKLOAD_CPUS=$((CORE_COUNT > RESERVED_CPUS ? CORE_COUNT - RESERVED_CPUS : 1))
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

For the reference run, start with one VMAS environment for each workload CPU:

```bash
export N_ENVS="$WORKLOAD_CPUS"
```

{{% notice Note %}}
This is a starting point, not a claim that one environment maps to one operating-system thread. VMAS applies vectorized PyTorch operations across the environment batch. Reduce `N_ENVS` if memory pressure causes swapping, and compare throughput before increasing it.
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
python3.12 -m venv "$HOME/venvs/mappo"
```

Activate it:

```bash
source "$HOME/venvs/mappo/bin/activate"
```

Confirm the active Python interpreter:

```bash
which python
```

Upgrade the Python packaging tools:

```bash
python -m pip install --upgrade pip setuptools wheel packaging
```

Install pinned PyTorch, TorchRL, TensorDict, and VMAS versions:

```bash
python -m pip install \
    "torch==2.8.0" \
    "torchvision==0.23.0" \
    "torchaudio==2.8.0" \
    "torchrl==0.10.1" \
    "tensordict==0.10.0" \
    "vmas==1.5.2"
```

Verify the installation:

```bash
python -c 'import platform, torch; print("Architecture:", platform.machine()); print("PyTorch:", torch.__version__); print("CUDA available:", torch.cuda.is_available()); print("CUDA device:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "N/A")'
```

## Install BenchMARL and VMAS

Clone the pinned BenchMARL revision:

```bash
export BENCHMARL_ROOT="$HOME/BenchMARL"
git clone --filter=blob:none --no-checkout --depth 1 \
    https://github.com/facebookresearch/BenchMARL.git \
    "$BENCHMARL_ROOT"
git -C "$BENCHMARL_ROOT" fetch --depth 1 origin \
    65d649d80e0bdcbdbe2c5d6a3f02dbfed8f0bec1
git -C "$BENCHMARL_ROOT" checkout --detach \
    65d649d80e0bdcbdbe2c5d6a3f02dbfed8f0bec1
cd "$BENCHMARL_ROOT"
```

Install BenchMARL and its remaining dependencies:

```bash
python -m pip install -e ".[vmas]"
```

Verify the software stack:

```bash
python - <<'PY'
from importlib.metadata import version

for package in ("torch", "torchrl", "tensordict", "vmas", "benchmarl"):
    print(f"{package}: {version(package)}")
PY
```

Record the BenchMARL revision used for the experiment:

```bash
git rev-parse HEAD
```

The revision must be `65d649d80e0bdcbdbe2c5d6a3f02dbfed8f0bec1`. The version pins and revision keep the checkpoint layout and exporter assumptions reproducible.

## What you've accomplished

You have validated the Arm cloud instance, selected an explicit workload size, and installed a pinned training stack. Next, you will configure and run the MAPPO experiment.

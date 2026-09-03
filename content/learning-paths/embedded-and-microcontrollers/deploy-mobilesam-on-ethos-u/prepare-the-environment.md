---
title: Prepare the ExecuTorch and Arm environment
description: Install ExecuTorch, the Ethos-U Python dependencies, the Arm GNU Toolchain, and the Corstone-320 FVP.
weight: 3

layout: "learningpathall"
---

## Get the ExecuTorch source

Clone ExecuTorch and initialize its submodules:

```bash
git clone https://github.com/pytorch/executorch.git
cd executorch
git submodule sync
git submodule update --init --recursive
```

Run the remaining commands from the ExecuTorch repository root.

## Create a Python environment

Create and activate a Python 3.12 virtual environment:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Install the current ExecuTorch checkout with its Ethos-U dependencies:

```bash
./install_executorch.sh --optional-dependency ethos_u
```

Using the checkout's installer keeps the Python package aligned with the example source.

## Install the Arm development tools

{{% notice macOS %}}
Before you run the Arm setup command on macOS, install the [FVPs-on-Mac wrapper](https://github.com/Arm-Examples/FVPs-on-Mac) and add its `bin` directory to `PATH`. The wrapper runs the Linux Corstone-320 FVP in a container. Make sure `FVP_Corstone_SSE-320` resolves to the wrapper before you continue.
{{% /notice %}}

The Arm setup script installs the pinned GNU bare-metal toolchain, Ethos-U Vela compiler, and Corstone FVP used by the example. Read the End User License Agreements presented by the tooling before you accept them, then run:

```bash
./examples/arm/setup.sh --i-agree-to-the-contained-eula
source examples/arm/arm-scratch/setup_path.sh
```

## Verify the environment

Confirm that Python imports ExecuTorch:

```bash
python -c "import executorch; print('ExecuTorch import succeeded')"
```

The expected output is:

```output
ExecuTorch import succeeded
```

Check the target compiler and FVP:

```bash
arm-none-eabi-gcc -dumpmachine
command -v FVP_Corstone_SSE-320
```

The first command must print:

```output
arm-none-eabi
```

The second command prints the path to the Corstone-320 FVP. On macOS, confirm that this path is inside the FVPs-on-Mac `bin` directory.

## What you've accomplished

You have installed the Python, compiler, Vela, and virtual-platform dependencies used by the example. Next, you will prepare and export MobileSAM for Ethos-U85.

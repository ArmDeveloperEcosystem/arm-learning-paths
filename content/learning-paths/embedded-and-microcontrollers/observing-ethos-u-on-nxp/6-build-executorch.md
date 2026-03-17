---
# User change
title: "Build ExecuTorch"

weight: 7 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

With the ExecuTorch source checked out and your virtual environment active, you can now build ExecuTorch and set up the Arm toolchain for Ethos-U cross-compilation.

For a full tutorial on building ExecuTorch, see the Learning Path [Introduction to TinyML on Arm using PyTorch and ExecuTorch](/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/).

## Install ExecuTorch

Upgrade pip and install build tools:

```bash
pip install --upgrade pip setuptools wheel
```

Build and install the `executorch` pip package:

```bash
./install_executorch.sh
```

After the installation finishes, verify the package is available:

```bash
pip list | grep executorch
```

## Set up the Arm toolchain

Initialize the Arm-specific environment and accept the EULA:

```bash
./examples/arm/setup.sh --i-agree-to-the-contained-eula
```

Source the environment variables:

```bash
source ./examples/arm/ethos-u-scratch/setup_path.sh
```

{{% notice Troubleshooting %}}
If `install_executorch.sh` fails, install the dependencies manually:

```bash
pip install torch torchvision
pip install --no-build-isolation .
pip install --no-build-isolation third-party/ao
```

If `buck2` hangs during the build:

```bash
ps aux | grep buck
pkill -f buck
```

To clean the build environment and start fresh:

```bash
./install_executorch.sh --clean
git submodule sync
git submodule update --init --recursive
./install_executorch.sh
```
{{% /notice %}}

## What you've learned and what's next

In this section you've:

- Installed the ExecuTorch package and verified its availability
- Set up the Arm toolchain with Ethos-U support
- Configured the environment for cross-compiling to Ethos-U65

With ExecuTorch installed and the Arm toolchain configured, you can now compile `.pte` model files targeting the Ethos-U65 NPU.

---
title: Export the pico-faces model for Ethos-U85
description: Clone the pico-faces example, select the Alif Ensemble E8 target, and generate an Ethos-U85-delegated ExecuTorch AI layer.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Clone the example branch

Clone the branch that contains the pico-faces application and check out the revision:

```bash
git clone --branch hackathon-pico-faces --single-branch https://github.com/Arm-Examples/CMSIS-Executorch.git
cd CMSIS-Executorch
git checkout bb82e8f0c67b9e603ba6b0a48984c2f72866afce
code .
```

When Visual Studio Code (VS Code) opens the workspace:

1. Accept the Arm Tools Environment Manager prompt to activate the tools pinned in `vcpkg-configuration.json`.
2. Accept the prompt to install the required CMSIS packs.
3. Open the **CMSIS** view and select **Manage Solution**.
4. Select the `DevKit-E8` target type, then select **Apply**.

The managed environment supplies the following:

- CMSIS-Toolbox
- Arm Compiler for Embedded
- GCC
- CMake
- Ninja 

The CMSIS packs provide the Alif device support and the ExecuTorch runtime components.

## Set up the Python environment

To set up the Python environment:

1. Open the VS Code Command Palette.
2. Select **Tasks: Run Task**.
3. Select **Setup Python virtual environment**.

The task creates `.venv` and installs the pinned export packages. It downloads about 60 MB of pico-faces checkpoints into `model/pico_faces/`. The Python packages include several gigabytes of PyTorch dependencies, so the first setup can take some time.

{{% notice Note %}}
The exporter supports Python 3.10 through 3.13. If your system Python isn't in that range, start by [installing uv](https://docs.astral.sh/uv/getting-started/installation/).

Restart VS Code after installation so that its tasks can find `uv` on `PATH`. Then, confirm that `uv` is available in the VS Code terminal:

```bash
uv --version
```

Select **Setup Python virtual environment (uv)** and enter `3.12` at the Python version prompt. This task can download a compatible interpreter. The physical DevKit was validated using Python 3.12.13.
{{% /notice %}}

## Create the AI layer

To create the AI layer:

1. Open the VS Code Command Palette.
2. Select **Tasks: Run Task**.
3. Select **Create AI layer**.

If the task reports that `cmsis-executorch.cbuild-mlops.yml` is missing, select **Build** once in the **CMSIS** view. The extension generates the target description. You can then run **Create AI layer** again.

The export performs the following operations:

- Calibrates `dit_step` with 16-bit activations and 8-bit weights
- Calibrates `decode` with 8-bit activations and weights
- Delegates each method as one Ethos-U85 segment
- Generates the CMSIS component selection and embedded model data

The task takes a few minutes. When it completes, confirm that `ai_layer/` contains the following generated artifacts:

| File | Purpose |
| --- | --- |
| `model.pte` | ExecuTorch program containing both methods |
| `model_pte.c` | Program embedded as a C array for the firmware build |
| `model_params.h` | Sampling schedule, image shapes, and conditioning data |
| `ai_layer.clayer.yml` | CMSIS components selected for the exported program |

Review the task log. It should report one Ethos-U delegate for each model method. Only the quantize and dequantize boundaries remain on the CPU. The diffusion transformer and decoder run on the NPU.

{{% notice Note %}}
Run **Create AI layer** again after changing `model/model.py` or selecting a target with a different NPU configuration. The generated model data isn't committed to the repository.
{{% /notice %}}

## What you've accomplished and what's next

You've exported the diffusion transformer and decoder as one ExecuTorch program for the DevKit's Ethos-U85. 

Next, you'll install the boot configuration and debug stub needed to load the program on the high-performance Cortex-M55 core.

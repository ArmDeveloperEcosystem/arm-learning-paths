---
title: Set up your environment for ExecuTorch quantization
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you create a Python environment with PyTorch, TorchAO, and ExecuTorch components needed for quantization and `.vgf` export.

{{% notice Note %}}
If you already use [Neural Graphics Model Gym](/learning-paths/mobile-graphics-and-gaming/model-training-gym), keep that environment and reuse it here.
{{% /notice %}}

## Create a virtual environment

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
```

## Clone the ExecuTorch repository

In your virtual environment, clone the ExecuTorch repository and run the installation script:

```bash
git clone https://github.com/pytorch/executorch.git
cd executorch
./install_executorch.sh
```

## Run the Arm backend setup script

From the root of the cloned `executorch` repository, run the Arm backend setup script:

```bash
./examples/arm/setup.sh \
  --i-agree-to-the-contained-eula \
  --disable-ethos-u-deps \
  --enable-mlsdk-deps
```

In the same terminal session, source the generated setup script so the Arm backend tools (including the model converter) are available on your `PATH`:

```bash
source ./examples/arm/arm-scratch/setup_path.sh
```

Verify the model converter is available:

```bash
command -v model-converter || command -v model_converter
```

Verify your imports:

```python
import torch
import torchvision
import torchao

import executorch
import executorch.backends.arm
from executorch.backends.arm.vgf.partitioner import VgfPartitioner

print("torch:", torch.__version__)
print("torchvision:", torchvision.__version__)
print("torchao:", torchao.__version__)
```

{{% notice Tip %}}
If `executorch.backends.arm` is missing, you installed an ExecuTorch build without the Arm backend. Use an ExecuTorch build that includes `executorch.backends.arm` and the VGF partitioner.

If you checked out a specific ExecuTorch branch (for example, `release/1.0`) and you run into version mismatches, check out the main branch of ExecuTorch from the cloned repository and install from source:

```bash
pip install -e .
```
{{% /notice %}}

With your environment set up, you are ready to run PTQ and generate a `.vgf` artifact from a calibrated model.

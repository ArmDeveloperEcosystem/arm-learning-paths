---
title: ExecuTorch Setup
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up ExecuTorch

ExecuTorch is an end-to-end solution for enabling on-device inference capabilities across mobile and edge devices; including wearables, embedded devices, and microcontrollers. It is part of the PyTorch Edge ecosystem and enables efficient deployment of PyTorch models to edge devices. You can learn more by reading the [ExecuTorch Overview](https://pytorch.org/executorch/stable/intro-overview.html).

The best practice is to generate an isolated Python environment in which to install your ExecuTorch dependencies. We provide instructions for both a Python virtual environment and a Conda virtual environment, but you only need one.

### Option 1: Create a Python virtual environment

```bash
python3.10 -m venv executorch
source executorch/bin/activate
```

The prompt of your terminal has `executorch` as a prefix to indicate the virtual environment is active.

### Option 2: Create a Conda virtual environment

Install Miniconda on your development machine by following the [Installing conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) instructions.

Once `conda` is installed, create the environment:

```bash
conda create -yn executorch python=3.10.0
conda activate executorch
```

### Clone ExecuTorch and install the required dependencies

From within the conda environment, run the commands below to download the ExecuTorch repository and install the required packages:

``` bash
git clone https://github.com/pytorch/executorch.git
cd executorch
git submodule sync
git submodule update --init
./install_requirements.sh
./install_requirements.sh --pybind xnnpack
./examples/models/llama/install_requirements.sh
```

When these scripts finish successfully, ExecuTorch is set up. That means it's time to dive into the world of Llama models!

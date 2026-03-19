---
title: Set up ExecuTorch
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up ExecuTorch

ExecuTorch is an end-to-end solution for enabling on-device inference across mobile and edge devices, including wearables, embedded devices, and microcontrollers. It is part of the PyTorch Edge ecosystem and enables efficient deployment of PyTorch models to edge devices. You can learn more by reading the [ExecuTorch Overview](https://pytorch.org/executorch/stable/intro-overview.html).

The best practice is to create an isolated Python environment to install ExecuTorch dependencies.

### Create a Python virtual environment

Use the `venv` module available through Python:

```bash
python3.10 -m venv executorch-venv
source executorch-venv/bin/activate
```

Your terminal prompt now shows `executorch-venv` as a prefix to indicate the virtual environment is active.

### Clone ExecuTorch and install dependencies

From within the virtual environment, run the commands below to download the ExecuTorch repository and install the required packages:

```bash
git clone https://github.com/pytorch/executorch.git
cd executorch
git checkout release/1.0
git submodule sync
git submodule update --init --recursive
./install_executorch.sh
./examples/models/llama/install_requirements.sh
```

When these scripts complete successfully, ExecuTorch is ready. Before preparing your Llama model for deployment, the next section explains what Llama models are and why they work well for customer support applications.

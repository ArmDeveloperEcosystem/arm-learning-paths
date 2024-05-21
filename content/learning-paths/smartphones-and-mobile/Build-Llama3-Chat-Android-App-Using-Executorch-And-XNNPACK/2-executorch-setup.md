---
title: ExecuTorch Setup
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up ExecuTorch

ExecuTorch is an end-to-end solution for enabling on-device inference capabilities across mobile and edge devices including wearables, embedded devices and microcontrollers. It is part of the PyTorch Edge ecosystem and enables efficient deployment of PyTorch models to edge devices. It is highly recommended to learn and understand more about [ExecuTorch](https://pytorch.org/executorch/stable/intro-overview.html)

In this section, we will learn how to

1. Set up an environment to work on ExecuTorch
2. Generate a sample ExecuTorch program
3. Build and run a program with the ExecuTorch runtime

## 1. Create a Virtual Environment

### Python Virtual Environment

   ```bash
   python3.10 -m venv executorch
   source executorch/bin/activate
   ```

### Conda Virtual Environment

Install [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) on your machine.

   ```bash
    conda create -yn executorch python=3.10.0
    conda activate executorch
    ```

## 2. Clone and install ExecuTorch requirements

``` bash
# Clone the ExecuTorch repo from GitHub
git clone --branch v0.2.0 https://github.com/pytorch/executorch.git
cd executorch

# Update and pull submodules
git submodule sync
git submodule update --init

# Install ExecuTorch pip package and its dependencies, as well as
# development tools like CMake.
./install_requirements.sh --pybind xnnpack

# Install a few more dependencies
./examples/models/llama2/install_requirements.sh

```

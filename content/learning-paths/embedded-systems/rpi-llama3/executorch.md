---
title: Set up ExecuTorch
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Set up ExecuTorch

ExecuTorch is an end-to-end solution for enabling on-device inference capabilities across mobile and edge devices; including wearables, embedded devices, and microcontrollers. It is part of the PyTorch Edge ecosystem and enables efficient deployment of PyTorch models to edge devices. You can learn more by reading through the [ExecuTorch Overview](https://pytorch.org/executorch/stable/intro-overview.html).

The best practice is to create an isolated Python environment in which you install the ExecuTorch dependencies. Use one of these methods:

### Option 1: Create a Python virtual environment

```bash
python3.10 -m venv executorch-venv
source executorch-venv/bin/activate
```

The prompt of your terminal has (executorch-venv) as a prefix to indicate the virtual environment is active.

### Option 2: Create a Conda virtual environment

Install Miniconda on your development machine by following the [Anaconda](/install-guides/anaconda/) Install Guide.

Once `conda` is installed create the environment:

```bash
conda create -yn executorch-venv python=3.10.0
conda activate executorch-venv
```

## Install clang

Install clang and set it as the default compiler. This will allow ExecuTorch to compile and build properly.

```bash
# Download the clang compiler
sudo apt install clang

# Make clang the default compiler for cc and c++
sudo update-alternatives --install /usr/bin/cc cc /usr/bin/clang 100
sudo update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++ 100
sudo update-alternatives --set cc /usr/bin/clang
sudo update-alternatives --set c++ /usr/bin/clang++
```

## Clone ExecuTorch and install the required dependencies

From within the environment, run the commands below to download the ExecuTorch repository and install the required packages: 

``` bash
# Clone the ExecuTorch repo from GitHub
git clone https://github.com/pytorch/executorch.git
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
{{% notice Note %}}
The install_requirements for llama 3  are the same as for llama 2, so you can use the instructions for both models up until the very last step.
{{% /notice %}}

If these scripts finish successfully, ExecuTorch is all set up. That means it's time to dive into the world of Llama models!
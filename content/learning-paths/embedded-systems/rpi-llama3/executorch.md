---
title: Set up ExecuTorch
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Set up ExecuTorch

ExecuTorch is an end-to-end solution for enabling on-device inference capabilities across mobile and edge devices; including wearables, embedded devices, and microcontrollers. It is part of the PyTorch Edge ecosystem and enables efficient deployment of PyTorch models to edge devices. You can learn more by reading through the [ExecuTorch Overview](https://pytorch.org/executorch/stable/intro-overview.html).

The best practice is to create an isolated Python environment in which you install the ExecuTorch dependencies. Use one of these methods in the Raspberry Pi OS shell in your Docker container:

### Option 1: Create a Python virtual environment

Create a Python virtual environment using:

```bash
python -m venv executorch-venv
source executorch-venv/bin/activate
```

Your terminal displays `(executorch-venv)` in the prompt indicating the virtual environment is active.

### Option 2: Create a Conda virtual environment

Install Miniconda on your development machine by following the [Anaconda install guide](/install-guides/anaconda/).

Once `conda` is installed create the environment:

```bash
conda create -yn executorch-venv
conda activate executorch-venv
```

## Install Clang

Install Clang, which is required to build ExecuTorch: 

```bash
sudo apt install clang -y
```

Then, make clang the default C/C++ compiler:

```bash
sudo update-alternatives --install /usr/bin/cc cc /usr/bin/clang 100
sudo update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++ 100
sudo update-alternatives --set cc /usr/bin/clang
sudo update-alternatives --set c++ /usr/bin/clang++
```

## Clone ExecuTorch and install the required dependencies

Continue in your Python virtual environment, and run the commands below to download the ExecuTorch repository and install the required packages. 

After cloning the repository, the project's submodules are updated, and two scripts install additional dependencies.

``` bash
git clone https://github.com/pytorch/executorch.git
cd executorch
git submodule sync
git submodule update --init
./install_requirements.sh --pybind xnnpack
./examples/models/llama2/install_requirements.sh
```

{{% notice Note %}}
You can safely ignore the following error on failing to import lm_eval running the install_requirements.sh scripts:
`Failed to import examples.models due to lm_eval conflict`
{{% /notice %}}

When these scripts finish successfully, ExecuTorch is all set up. That means it's time to dive into the world of Llama models!
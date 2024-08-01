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

```bash
python -m venv executorch-venv
source executorch-venv/bin/activate
```

The prompt of your terminal has (executorch-venv) as a prefix to indicate the virtual environment is active.

### Option 2: Create a Conda virtual environment

Install Miniconda on your development machine by following the [Anaconda](/install-guides/anaconda/) Install Guide.

Once `conda` is installed create the environment:

```bash
conda create -yn executorch-venv
conda activate executorch-venv
```

## Install clang

Install clang if it is not already installed. 
```bash
sudo apt install clang
```

Then, make clang the default compiler for cc and c++
```bash
sudo update-alternatives --install /usr/bin/cc cc /usr/bin/clang 100
sudo update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++ 100
sudo update-alternatives --set cc /usr/bin/clang
sudo update-alternatives --set c++ /usr/bin/clang++
```

This will allow ExecuTorch to compile and build properly.

## Clone ExecuTorch and install the required dependencies

From within the environment, run the commands below to download the ExecuTorch repository and install the required packages. After cloning the repository, you need to update and pull the project's submodules. Finally, you run two scripts that install a few dependencies.

``` bash
git clone https://github.com/pytorch/executorch.git
cd executorch

git submodule sync
git submodule update --init

./install_requirements.sh --pybind xnnpack

./examples/models/llama2/install_requirements.sh
```
{{% notice Note %}}
The install_requirements for Llama 3  are the same as for Llama 2, so you can use the instructions for both models up until the very last step.

You can safely ignore the error on failing to import lm_eval running the install_requirements.sh scripts.
"Failed to import examples.models due to lm_eval conflict"
{{% /notice %}}

If these scripts finish successfully, ExecuTorch is all set up. That means it's time to dive into the world of Llama models!
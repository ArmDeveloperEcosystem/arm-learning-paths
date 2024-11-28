---
# User change
title: "Environment Setup on Host Machine"

weight: 3

# Do not modify these elements
layout: "learningpathall"
---

In this section, you will prepare a development environment to compile the model.

## Before you begin ? remove ?


The instructions are for Ubuntu 22.04 or newer. ?

{{% notice Note %}}
Note that the Corstone-300 FVP is not available for the Arm architecture so your host machine needs to x86_64.
{{% /notice %}}

^?

The instructions have been tested on:
- Arm-based cloud instances running Ubuntu 22.04.
- Desktop computer with Ubuntu 24.04.
- Windows Subsystem for Linux (WSL).

## Install dependencies

Python3 is required and comes installed with Ubuntu, but some additional packages are needed.

```bash
sudo apt update
sudo apt install python-is-python3 python3-dev gcc g++ make cmake clang -y
```

```
???
sudo update-alternatives --install /usr/bin/cc cc /usr/bin/clang 100
sudo update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++ 100
sudo update-alternatives --set cc /usr/bin/clang
sudo update-alternatives --set c++ /usr/bin/clang++
```
## Create a virtual environment

Create a Python virtual environment using Miniconda.

For Arm Linux:

```console
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh
sh ./Miniconda3-latest-Linux-aarch64.sh -b
eval "$($HOME/miniconda3/bin/conda shell.bash hook)"
conda --version
```

For x86_64 Linux:

```console
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
sh ./Miniconda3-latest-Linux-x86_64.sh -b
eval "$($HOME/miniconda3/bin/conda shell.bash hook)"
conda --version
```

Activate the Python virtual environment:

```bash
conda create -yn executorch python=3.12.7
conda activate executorch
```

The prompt of your terminal now has (executorch) as a prefix to indicate the virtual environment is active.


## Install Executorch

From within the Python virtual environment, run the commands below to download the ExecuTorch repository and install the required packages:

``` bash
cd $HOME
git clone https://github.com/pytorch/executorch.git
cd executorch
```

Run a few commands to set up the ExecuTorch internal dependencies.
```bash
git submodule sync
git submodule update --init
??? pip install buck

./install_requirements.sh
```

## Install Edge Impulse CLI

1. Create an [Edge Impulse Account](https://studio.edgeimpulse.com/signup) and sign in.

2. Install the Edge Impulse CLI tools in your terminal

The Edge Impulse CLI tools require Node.js.

```console
sudo apt install nodejs npm -y
```

Confirm `node` is available by running:

```console
node -v
```

Your version is printed, for example:

```output
v18.19.1
```

Install the Edge Impulse CLI using NPM:

```console
sudo npm install -g edge-impulse-cli
```

3. Install Screen to use with edge devices

```console
sudo apt install screen -y
```

## Next Steps

If you don't have the Grove AI vision board, use the Corstone-300 FVP proceed to [Environment Setup Corstone-300 FVP](/learning-paths/microcontrollers/introduction-to-tinyml-on-arm/env-setup-6-fvp/)

If you have the Grove board proceed o to [Setup on Grove - Vision AI Module V2](/learning-paths/microcontrollers/introduction-to-tinyml-on-arm/setup-7-grove/)
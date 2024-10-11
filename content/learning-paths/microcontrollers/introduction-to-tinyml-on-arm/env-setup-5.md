---
# User change
title: "Environment Setup on Host Machine"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
## Before you begin 

You will use a Linux computer to run PyTorch and ExecuTorch to prepare a TinyML model to run on edge devices. 

The instructions are for Ubuntu 22.04 or newer.

You also need the [Grove Vision AI Module](https://wiki.seeedstudio.com/Grove-Vision-AI-Module/). If you don't have the board you can use the Corstone-300 Fixed Virtual Platform (FVP) instead.

{{% notice Note %}}
Note that the Corstone-300 FVP is not available for the Arm architecture so your host machine needs to x86_64.
{{% /notice %}}

The instructions have been tested on:
- Arm-based cloud instances running Ubuntu 22.04.
- Desktop computer with Ubuntu 24.04.
- Windows Subsystem for Linux (WSL).

The host machine is where you will perform most of your development work, especially compiling code for the target Arm devices.

## Install Python

Python 3 is included in Ubuntu, but some additonal packages are needed. 

```console
sudo apt update
sudo apt install python-is-python3 gcc g++ make -y
```

## Install PyTorch

Create a Python virtual environemnt using Miniconda. 

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
conda create -yn executorch python=3.10.0
conda activate executorch
```

The prompt of your terminal now has (executorch) as a prefix to indicate the virtual environment is active.


## Install Executorch

From within the Python virtual environment, run the commands below to download the ExecuTorch repository and install the required packages: 

``` bash
# Clone the ExecuTorch repo from GitHub
git clone --branch v0.3.0 https://github.com/pytorch/executorch.git
cd executorch

# Update and pull submodules
git submodule sync
git submodule update --init

# Install ExecuTorch pip package and its dependencies, as well as
# development tools like CMake.
./install_requirements.sh
```

## Install Edge Impulse CLI

1. Create an [Edge Impulse Account](https://studio.edgeimpulse.com/signup) and sign in.

2. Install the Edge Impulse CLI tools in your terminal

The Edge Impulse CLI tools require Node.js. 

```console
sudo apt install nodejs npm -y
```

Confirm `node` is avilable by running: 

```console
node -v 
```

Your version is printed, for example:

```output
v18.19.1
```

Install the Edge Impulse CLI using NPM:

```console
npm install -g edge-impulse-cli
```

3. Install Screen to use with edge devices

```console
sudo apt install screen -y
```

## Next Steps

If you don't have the Grove AI vision board and want to use the Corstone-300 FVP proceed to [Environment Setup Corstone-300 FVP](/learning-paths/microcontrollers/introduction-to-tinyml-on-arm/env-setup-6-fvp/)

If you have the Grove board proceed o to [Setup on Grove - Vision AI Module V2](/learning-paths/microcontrollers/introduction-to-tinyml-on-arm/setup-7-grove/)
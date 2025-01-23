---
# User change
title: "Environment Setup on Host Machine"

weight: 3

# Do not modify these elements
layout: "learningpathall"
---

In this section, you will prepare a development environment to compile the model. These instructions have been tested on Ubuntu 22.04, 24.04 and on Windows Subsystem for Linux (WSL).

## Install dependencies

Python3 is required and comes installed with Ubuntu, but some additional packages are needed.

```bash
sudo apt update
sudo apt install python-is-python3 python3-dev python3-venv gcc g++ make -y
```

## Create a virtual environment

Create a Python virtual environment using `python venv`.

```console
python3 -m venv $HOME/executorch-venv
source $HOME/executorch-venv/bin/activate
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

./install_requirements.sh
```

{{% notice Note %}}
If you run into an issue of `buck` running in a stale environment, reset it by running the following instructions.

```bash
ps aux | grep buck
pkill -f buck
```
{{% /notice %}}

## Next Steps

If you don't have the Grove AI vision board, use the Corstone-300 FVP proceed to [Environment Setup Corstone-300 FVP](/learning-paths/microcontrollers/introduction-to-tinyml-on-arm/env-setup-6-fvp/)

If you have the Grove board proceed o to [Setup on Grove - Vision AI Module V2](/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/setup-7-grove/)
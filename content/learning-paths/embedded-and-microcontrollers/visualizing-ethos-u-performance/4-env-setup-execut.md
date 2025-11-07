---
# User change
title: "Set up your ExecuTorch environment"

weight: 4

# Do not modify these elements
layout: "learningpathall"
---
## Set up overview

Before you can deploy and test models with ExecuTorch, you need to set up your local development environment. This section walks you through installing system dependencies, creating a virtual environment, and cloning the ExecuTorch repository on Ubuntu or WSL. Once complete, you'll be ready to run TinyML models on a virtual Arm platform.

## Install system dependencies

{{< notice Note >}}
Make sure Python 3 is installed. It comes pre-installed on most versions of Ubuntu.
{{< /notice >}}

These instructions have been tested on:

- Ubuntu 22.04 and 24.04
- Windows Subsystem for Linux (WSL)

Run the following commands to install the dependencies:

```bash
sudo apt update
sudo apt install python-is-python3 python3-dev python3-venv gcc g++ make -y
```

## Create a virtual environment

Create and activate a Python virtual environment:

```console
python3 -m venv $HOME/executorch-venv
source $HOME/executorch-venv/bin/activate
```
Your shell prompt should now start with `(executorch)` to indicate the environment is active.

## Install ExecuTorch

Clone the ExecuTorch repository and install dependencies:

``` bash
cd $HOME
git clone https://github.com/pytorch/executorch.git
cd executorch
git checkout release/1.0
```

Set up internal submodules:

```bash
git submodule sync
git submodule update --init --recursive
./install_executorch.sh
```

{{% notice Tip %}}
If you encounter a stale `buck` environment, reset it using:

```bash
ps aux | grep buck
pkill -f buck
```
{{% /notice %}}

## Verify the installation:

Check that ExecuTorch is correctly installed:

```bash
pip list | grep executorch
```
Expected output:

```output
executorch         0.8.0a0+92fb0cc
```

## What's next?

Now that ExecuTorch is installed, you're ready to simulate your TinyML model on an Arm Fixed Virtual Platform (FVP). In the next section, you'll configure and launch a Fixed Virtual Platform.

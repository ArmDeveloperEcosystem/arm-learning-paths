---
# User change
title: "Set up your development environment"

weight: 3

# Do not modify these elements
layout: "learningpathall"
---


## Install dependencies

These instructions have been tested on:

- Ubuntu 22.04 and 24.04
- Windows Subsystem for Linux (WSL)

Make sure Python 3 is installed (it comes with Ubuntu by default). Then install the required system packages:

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
After activation, your terminal prompt should show (executorch) to indicate that the environment is active.


## Install ExecuTorch

Clone the ExecuTorch repository and install its dependencies:

``` bash
cd $HOME
git clone https://github.com/pytorch/executorch.git
cd executorch
```

Set up internal dependencies:

```bash
git submodule sync
git submodule update --init --recursive
./install_executorch.sh
```

{{% notice Tip %}}
If you run into issues with `buck` running in a stale environment, reset it:

```bash
ps aux | grep buck
pkill -f buck
```
{{% /notice %}}

Verify the installation:

```bash
pip list | grep executorch
```
Example output:

```output
executorch         0.8.0a0+92fb0cc
```

## Next steps

Now that ExecuTorch is installed, you're ready to simulate your TinyML model on virtual Arm hardware. In the next section, you'll configure and launch a Fixed Virtual Platform.

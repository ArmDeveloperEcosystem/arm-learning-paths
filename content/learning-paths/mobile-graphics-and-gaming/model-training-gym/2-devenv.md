---
title: Set up your environment
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you will install dependencies into an Ubuntu 22.04 or later environment. You'll need Python 3.10, 3.11, or 3.12, CUDA Toolkit v13.1.1 or later, and some ML and system dependencies.

Start by making sure a supported Python version is installed:

```bash
python3 --version
```

Next, install a few additional packages:

```bash
sudo apt update
sudo apt install python3-venv python-is-python3 gcc make python3-dev -y
```

## Set up the examples repository

The example notebooks are open-sourced in a GitHub repository. Start by cloning it:

```bash
git clone https://github.com/arm/neural-graphics-model-gym-examples.git
cd neural-graphics-model-gym-examples
```

From inside the `neural-graphics-model-gym-examples/` folder, run the environment creation script:

```bash
python create_env.py
```

This will do the following:

- Create a Python virtual environment called `nb-env`
- Install the `ng-model-gym` package and required dependencies
- Download the datasets and weights needed to run the notebooks

Activate the virtual environment:

```bash
source nb-env/bin/activate
```

Run the following in a python shell to confirm that the script was successful:

```python
import torch
import ng_model_gym

print("Torch version:", torch.__version__)
print("Model Gym version:", ng_model_gym.__version__)
```

You’ve completed your environment setup - great work! You’re now ready to start walking through the training and evaluation steps.

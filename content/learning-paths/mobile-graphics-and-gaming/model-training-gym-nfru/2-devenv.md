---
title: Set up your environment
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install dependencies on Ubuntu

Install a few machine learning and system dependencies on your Ubuntu environment.

Start by making sure Python is installed and the version is later than `3.10`:

```bash
python3 --version
```

Next, install dependency packages:

```bash
sudo apt update
sudo apt install python3-venv python-is-python3 gcc make python3-dev -y
```

## Set up the examples repository

The example notebooks are open-sourced in a GitHub repository. 

Start by cloning the repository:

```bash
git clone https://github.com/arm/neural-graphics-model-gym-examples.git
cd neural-graphics-model-gym-examples
```

{{% notice Note %}}
The NFRU notebooks will be provided from a dedicated examples repository tag. After the NFRU examples tag is available, check it out before running the setup script:

```bash
git checkout <nfru-examples-tag>
```
{{% /notice %}}

From inside the `neural-graphics-model-gym-examples/` folder, run the setup script:

```bash
python3 create_env.py
```

The script does the following:
- Creates a Python virtual environment called `nb-env`
- Installs the `ng-model-gym` package and required dependencies
- Downloads the datasets and weights needed to run the notebooks

Activate the virtual environment:

```bash
source nb-env/bin/activate
```

Run the following in a Python shell to confirm that the script was successful:

```python
import torch
import ng_model_gym

print("Torch version:", torch.__version__)
print("Model Gym version:", ng_model_gym.__version__)
```
## What you've accomplished and what's next

You’ve now completed your environment setup by installing dependencies and setting up the example NFRU notebooks repository.

Next, you'll train the neural graphics model.

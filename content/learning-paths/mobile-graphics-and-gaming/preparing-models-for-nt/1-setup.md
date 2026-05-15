---
title: Set up your environment 
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare your host system

Before you can create a reference PyTorch model, you need to set up Python, ExecuTorch, and Arm backend dependencies.

Use one of the following:
- Linux
- macOS with Apple Silicon

Verify that your Python version is 3.10 or later and earlier than 3.14:

```bash
python3 --version
```

### Create a Python virtual environment

Create a working directory for this Learning Path:

```bash
mkdir preparing-models-for-nt
cd preparing-models-for-nt
```
Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
```

### Clone and install ExecuTorch

Clone ExecuTorch from GitHub and install:

```bash
git clone https://github.com/pytorch/executorch.git repo/executorch
cd repo/executorch
./install_executorch.sh
```

### Install Arm backend dependencies

From the root of `repo/executorch`, run:

```bash
./examples/arm/setup.sh \
  --i-agree-to-the-contained-eula \
  --disable-ethos-u-deps \
  --enable-mlsdk-deps
```

Source the generated path script in the same shell session:

```bash
source ./examples/arm/arm-scratch/setup_path.sh
```

Return to the Learning Path working directory:

```bash
cd ../..
```

## (Optional) Use a Jupyter notebook

If you prefer to work through the same steps in Jupyter, download the notebook from the `arm-learning-paths` repository:

```bash
wget https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/main/content/learning-paths/mobile-graphics-and-gaming/preparing-models-for-nt/prepare-models-for-nt.ipynb
```

Install Jupyter Lab in your active virtual environment:

```bash
pip install jupyterlab
```

From the `preparing-models-for-nt` directory, launch Jupyter Lab:

```bash
jupyter lab
```

Open the notebook:

```output
prepare-models-for-nt.ipynb
```

## What you've accomplished and what's next

You've now set up the Python environment, installed ExecuTorch, and configured Arm backend dependencies for creating and exporting PyTorch models.

Next, you'll create and export your first test model, either from the Learning Path pages or from the optional Jupyter notebook.

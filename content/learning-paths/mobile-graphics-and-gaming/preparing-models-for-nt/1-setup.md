---
title: Set up your environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

This Learning Path walks through every step directly in the web pages. If you prefer working in a notebook, you can download the optional notebook and run the same workflow in Jupyter.

{{% notice Note %}}
The notebook is optional. The commands and code snippets in the following sections are the source of truth for the Learning Path.
{{% /notice %}}

## OS and tooling requirements

Use one of the following:
- Linux
- macOS with Apple Silicon

Install and verify Python 3.10+, <3.14:

```bash
python3 --version
```

## Create a Python virtual environment

Create a working directory for this Learning Path:

```bash
mkdir preparing-models-for-nt
cd preparing-models-for-nt
```

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
```

## Clone and install ExecuTorch

```bash
git clone https://github.com/pytorch/executorch.git repo/executorch
cd repo/executorch
./install_executorch.sh
```

## Install Arm backend dependencies

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

alternatively you can use the attached setup script: 

<a href="{{ '/assets/scripts/install.sh' | relative_url }}" download>
  Download install.sh
</a>

## Optional: use the notebook

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

You are now ready to create and export your first test model, either from the Learning Path pages or from the optional notebook.

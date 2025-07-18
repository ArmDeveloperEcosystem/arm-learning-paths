---
title: Install Python dependencies for llama.cpp
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Overview

In this step, you'll set up a Python virtual environment and install the required dependencies for working with Llama.cpp. This ensures you have a clean, isolated Python environment with all the necessary packages for model optimization.

## Create a Python virtual environment

```bash
virtualenv env-llama-cpp
```

This command creates a new Python virtual environment named `env-llama-cpp`, which has the following benefits:
- Provides an isolated Python environment to prevent package conflicts between projects.
- Creates a local directory containing its own Python interpreter and installation space.
- Ensures Llama.cpp dependencies don’t interfere with your global Python setup.
- Supports reproducible and portable development environments.

## Activate the virtual environment

```bash
source env-llama-cpp/bin/activate
```

This command activates the virtual environment:
- The `source` command runs the activation script, which modifies your shell environment.
- Your shell prompt may update to show `env-llama-cpp`, indicating the environment is active
- All pip commands will now install packages into the virtual environment.
- Updates the `PATH` to prioritize the environment’s Python interpreter.

## Upgrade pip to the latest version

```bash
pip install --upgrade pip
```

This command ensures you have the latest version of pip:
- Upgrading pip helps avoid compatibility issues with newer packages
- The `--upgrade` flag tells pip to install the newest available version
- This is a best practice before installing project dependencies
- Newer pip versions often include security fixes and improved package resolution

## Install project dependencies

```bash
pip install -r requirements.txt
```

This command installs all the Python packages specified in the requirements.txt file:
- The `-r` flag tells Pip to read the package list from the specified file.
- `requirements.txt` defines the exact package versions required for the project.
- Ensures a consistent development environment across systems and contributors.
- Includes packages needed for model loading, inference, and Python bindings for Llama.cpp.

## What is installed? 

After the installation completes, your virtual environment includes:
- **NumPy**: for numerical computations and array operations
- **Requests**: for HTTP operations and API calls
- **Other dependencies**: required packages for Llama.cpp's Python integration

Your environment is now ready to run Python scripts that interact with the compiled Llama.cpp binaries.

Remember to activate the virtual environment before running any Python code:

```bash
source env-llama-cpp/bin/activate

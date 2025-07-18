---
title: Install Python dependencies for llama.cpp
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this step, you'll set up a Python virtual environment and install the required dependencies for working with Llama.cpp. This ensures you have a clean, isolated Python environment with all the necessary packages for model optimization.

## Create a Python virtual environment

```bash
virtualenv env-llama-cpp
```

This command creates a new Python virtual environment named `env-llama-cpp`:
- Provides an isolated Python environment to prevent package conflicts between projects.
- Creates a local directory containing its own Python interpreter and installation space.
- Ensures Llama.cpp dependencies don’t interfere with your global Python setup.
- Supports reproducible and portable development environments.

## Activate the virtual environment

```bash
source env-llama-cpp/bin/activate
```

This command activates the virtual environment:
- The `source` command executes the activation script, which modifies your shell environment.
- Depending on your shell, your command prompt might change to show `(env-llama-cpp)`, indicating the active environment.
- All Pip commands will install packages into the virtual environment.
- Updates the `PATH` to prioritize the environment’s Python interpreter.

## Upgrade Pip to the latest version

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
- The `-r` flag tells pip to read the package list from the specified file.
- `requirements.txt` contains a list of Python packages and their version specifications.
- This ensures everyone working on the project uses the same package versions
- The installation will include packages needed for model loading, inference, and any Python bindings for Llama.cpp

## What is installed? 

After successful installation, your virtual environment will contain:
- **NumPy**: For numerical computations and array operations
- **Requests**: For HTTP operations and API calls
- **Other dependencies**: Specific packages needed for Llama.cpp Python integration

The virtual environment is now ready for running Python scripts that interact with the compiled Llama.cpp binaries. Remember to always activate the virtual environment (`source env-llama-cpp/bin/activate`) before running any Python code related to this project.

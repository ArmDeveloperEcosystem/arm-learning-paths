---
title: Install Python dependencies for Llama.cpp
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up a Python environment for Llama.cpp

In this step, you’ll create a Python virtual environment and install the dependencies required to run AFM-4.5B with Llama.cpp. This ensures a clean, isolated environment for model optimization on Google Cloud Axion.

## Create a virtual environment

```bash
virtualenv env-llama-cpp
```

This command creates a new Python virtual environment named `env-llama-cpp`, which has the following benefits:
- Provides an isolated Python environment to prevent package conflicts between projects
- Creates a local directory containing its own Python interpreter and installation space
- Ensures Llama.cpp dependencies don’t interfere with your global Python setup
- Supports reproducible and portable development environments

## Activate your virtual environment

```bash
source env-llama-cpp/bin/activate
```
This command does the following:

- Runs the activation script, which modifies your shell environment
- Updates your shell prompt to show `env-llama-cpp`, indicating the environment is active
- Updates `PATH` to use so the environment’s Python interpreter 
- Ensures all `pip` commands install packages into the isolated environment

## Upgrade pip

Before installing dependencies, upgrade pip:

```bash
pip install --upgrade pip
```

- Ensures you have the latest version of pip
- Helps avoid compatibility issues with modern packages
- Applies the `--upgrade` flag to fetch and install the newest release
- Brings in security patches and better dependency resolution logic

## Install project dependencies

Use the following command to install all required Python packages:

```bash
pip install -r requirements.txt
```

This command:

- Uses the `-r` flag to read the list of dependencies from `requirements.txt`
- Installs the exact package versions required for the project
- Ensures consistency across development environments and contributors
- Includes packages for model loading, inference, and Python bindings for `llama.cpp`

This step sets up everything you need to run AFM-4.5B in your Python environment.

## Verify installed Python packages

After installation, your environment includes:

- **NumPy**: numerical computations and array operations  
- **Requests**: HTTP operations and API calls  
- **Other packages**: dependencies required by Llama.cpp’s Python bindings and utilities  

You can now run Python scripts that integrate with the compiled Llama.cpp binaries.

{{< notice Tip >}}
Before running any Python commands, make sure your virtual environment is activated.
{{< /notice >}}

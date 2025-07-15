---
title: Installing Python dependencies for llama.cpp
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this step, you'll set up a Python virtual environment and install the required dependencies for working with Llama.cpp. This ensures you have a clean, isolated Python environment with all the necessary packages for model optimization.

## Step 1: Create a Python Virtual Environment

```bash
virtualenv env-llama-cpp
```

This command creates a new Python virtual environment named `env-llama-cpp`:
- Virtual environments provide isolated Python environments that prevent conflicts between different projects
- The `env-llama-cpp` directory will contain its own Python interpreter and package installation space
- This isolation ensures that the Llama.cpp dependencies won't interfere with other Python projects on your system
- Virtual environments are essential for reproducible development environments

## Step 2: Activate the Virtual Environment

```bash
source env-llama-cpp/bin/activate
```

This command activates the virtual environment:
- The `source` command executes the activation script, which modifies your current shell environment
- Depending on you sheel, your command prompt may change to show `(env-llama-cpp)` at the beginning, indicating the active environment. This will be reflected in the following commands.
- All subsequent `pip` commands will install packages into this isolated environment
- The `PATH` environment variable is updated to prioritize the virtual environment's Python interpreter

## Step 3: Upgrade pip to the Latest Version

```bash
pip install --upgrade pip
```

This command ensures you have the latest version of pip:
- Upgrading pip helps avoid compatibility issues with newer packages
- The `--upgrade` flag tells pip to install the newest available version
- This is a best practice before installing project dependencies
- Newer pip versions often include security fixes and improved package resolution

## Step 4: Install Project Dependencies

```bash
pip install -r requirements.txt
```

This command installs all the Python packages specified in the requirements.txt file:
- The `-r` flag tells pip to read the package list from the specified file
- `requirements.txt` contains a list of Python packages and their version specifications
- This ensures everyone working on the project uses the same package versions
- The installation will include packages needed for model loading, inference, and any Python bindings for Llama.cpp

## What is installed? 

After successful installation, your virtual environment will contain:
- **NumPy**: For numerical computations and array operations
- **Requests**: For HTTP operations and API calls
- **Other dependencies**: Specific packages needed for Llama.cpp Python integration

The virtual environment is now ready for running Python scripts that interact with the compiled Llama.cpp binaries. Remember to always activate the virtual environment (`source env-llama-cpp/bin/activate`) before running any Python code related to this project.
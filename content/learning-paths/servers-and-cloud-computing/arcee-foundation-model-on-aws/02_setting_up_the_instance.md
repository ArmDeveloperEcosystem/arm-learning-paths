---
title: Configure your Graviton4 environment
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this step, you'll set up the Graviton4 instance with the tools and dependencies required to build and run the AFM-4.5B model. This includes installing system packages and a Python environment.

## Update the package list

Run the following command to update your local APT package index:

```bash
sudo apt-get update
```

This step ensures you have the most recent metadata about available packages, including versions and dependencies. It helps prevent conflicts when installing new packages.

## Install system dependencies

Install the build tools and Python environment:

```bash
sudo apt-get install cmake gcc g++ git python3 python3-pip python3-virtualenv libcurl4-openssl-dev unzip -y
```

This command installs the following tools and dependencies:

- **CMake**: cross-platform build system generator used to compile and build Llama.cpp

- **GCC and G++**: GNU C and C++ compilers for compiling native code

- **Git**: version control system for cloning repositories

- **Python 3**: Python interpreter for running Python-based tools and scripts

- **Pip**: Python package manager

- **Virtualenv**: tool for creating isolated Python environments

- **libcurl4-openssl-dev**: development files for the curl HTTP library

- **Unzip**: tool to extract `.zip` files (used in some model downloads)

The `-y` flag automatically approves the installation of all packages without prompting.

## Ready for build and deployment

After completing the setup, your instance includes the following tools and environments:

- A complete C/C++ development environment for building Llama.cpp
- Python 3, pip, and virtualenv for managing Python tools and environments
- Git for cloning repositories
- All required dependencies for compiling optimized Arm64 binaries

You're now ready to build Llama.cpp and download the Arcee Foundation Model.

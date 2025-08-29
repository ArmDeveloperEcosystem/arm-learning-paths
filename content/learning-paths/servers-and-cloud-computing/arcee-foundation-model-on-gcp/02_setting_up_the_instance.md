---
title: Configure your Google Cloud Axion Arm64 environment
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this step, you’ll configure your Google Cloud Axion Arm64 instance with the system packages and Python environment required to build and run the Arcee Foundation Model using Llama.cpp.

## Update package lists

Run the following command to update your local APT package index:

```bash
sudo apt-get update
```

This ensures you have the most recent metadata about available packages, versions, and dependencies, helping to prevent conflicts when installing new software.

## Install build tools and Python dependencies

Install the required build tools and Python environment:

```bash
sudo apt-get install cmake gcc g++ git python3 python3-pip python3-virtualenv libcurl4-openssl-dev unzip -y
```

This command installs the following:

- **CMake**: build system generator used to compile Llama.cpp  
- **GCC and G++**: GNU C and C++ compilers for native code  
- **Git**: version control system for cloning repositories  
- **Python 3**: Python interpreter for running tools and scripts  
- **Pip**: Python package manager  
- **Virtualenv**: tool for creating isolated Python environments  
- **libcurl4-openssl-dev**: development files for the curl HTTP library  
- **Unzip**: utility to extract `.zip` files  

The `-y` flag automatically approves the installation of all packages without prompting.

## Verify environment setup

After completing these steps, your instance includes:

- A complete C/C++ development environment for building Llama.cpp  
- Python 3, pip, and virtualenv for managing Python tools  
- Git for cloning repositories  
- All required dependencies for compiling optimized Arm64 binaries  

You’re now ready to build Llama.cpp and download the Arcee Foundation Model.

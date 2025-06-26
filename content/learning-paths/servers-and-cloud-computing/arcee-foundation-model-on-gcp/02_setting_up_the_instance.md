---
title: Setting up the instance
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this step, we'll set up the Axion c4a instance with all the necessary tools and dependencies required to build and run the Arcee Foundation Model. This includes installing the build tools and Python environment.

## Step 1: Update Package List

```bash
sudo apt-get update
```

This command updates the local package index from the repositories:

- Downloads the latest package lists from all configured APT repositories
- Ensures you have the most recent information about available packages and their versions
- This is a best practice before installing new packages to avoid potential conflicts
- The package index contains metadata about available packages, their dependencies, and version information

## Step 2: Install System Dependencies

```bash
sudo apt-get install cmake gcc g++ git python3 python3-pip python3-virtualenv libcurl4-openssl-dev unzip -y
```

This command installs all the essential development tools and dependencies:

- **cmake**: Cross-platform build system generator that we'll use to compile Llama.cpp
- **gcc & g++**: GNU C and C++ compilers for building native code
- **git**: Version control system for cloning repositories
- **python3**: Python interpreter for running Python-based tools and scripts
- **python3-pip**: Python package installer for managing Python dependencies
- **python3-virtualenv**: Tool for creating isolated Python environments
- **libcurl4-openssl-dev**: client-side URL transfer library

The `-y` flag automatically answers "yes" to prompts, making the installation non-interactive.

## What's Ready Now

After completing these steps, your Axion c4a instance will have:

- A complete C/C++ development environment for building Llama.cpp
- Python 3 with pip for managing Python packages
- Git for cloning repositories
- All necessary build tools for compiling optimized ARM64 binaries

The system is now prepared for the next steps: building Llama.cpp and downloading the Arcee Foundation Model.

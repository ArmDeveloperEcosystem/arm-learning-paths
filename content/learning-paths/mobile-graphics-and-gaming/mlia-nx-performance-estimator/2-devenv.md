---
title: Set up your MLIA environment
description: Install public MLIA wheels in a Python 3.12 environment on Ubuntu 24.04 and verify the Neural Technology target profiles and backend.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Perform an environment check

Use an x86-64 Ubuntu 24.04 LTS development host with CPython 3.12. The `mlia-neural-technology` version `0.2.0` wheel is published for CPython 3.12 on x86-64 Linux with glibc version 2.39 or later. Ubuntu 22.04, other Python versions, native macOS, and native Linux on Arm aren't supported by this wheel.

Check your architecture, Python version, and glibc version:

```bash
uname -m
python3.12 --version
getconf GNU_LIBC_VERSION
```

The expected architecture is `x86_64`, Python is `3.12.x`, and glibc is at least `2.39`.

You'll also need permission to install Ubuntu packages and internet access to PyPI and TensorFlow's public model downloads.

## Install the public packages

Install the Ubuntu packages needed to create an environment and download the models:

```bash
sudo apt update
sudo apt install -y python3.12-venv curl ca-certificates
```

Create a working directory and a clean virtual environment. Run the remaining commands from this directory unless stated otherwise:

```bash
mkdir -p mlia-demo
cd mlia-demo
python3.12 -m venv mlia-venv
source mlia-venv/bin/activate
python -m pip install --upgrade pip
python -m pip install mlia-neural-technology==0.2.0 mlia-converters-litert==0.1.2
python -m pip check
```

These are public PyPI packages. The Neural Technology plugin installs the following tools as dependencies:

- A compatible Arm ML Inference Advisor (MLIA) core
- The ML SDK Model Converter
- Tensor Operator Set Architecture (TOSA) tools  

The LiteRT converter plugin lets MLIA analyze `.tflite` files directly. You don't need TensorFlow, a GPU driver, or a separate model-training environment for this example.

The expected final output is:

```output
No broken requirements found.
```

## Discover profiles and backends

Verify the CLI and inspect the installed capabilities:

```bash
mlia --help
mlia target list
mlia backend list
```

Confirm that the target list includes `neural-technology` and both `NX-peak-12SC-8NX-600MHz` and `NX-sustained-12SC-8NX-350MHz`. The backend list includes `nx-performance-estimator`. Before backend installation, its installed status is `no` and its installable status is `yes`.

The estimator executable is bundled with the public wheel. MLIA offers to install it during your first check, so you don't need a separate backend installation command.

{{% notice Note %}}
If pip reports that no matching distribution exists for `mlia-neural-technology`, check the three host requirements again and upgrade pip inside the environment. A virtual environment doesn't change the host architecture or glibc version. Don't substitute an older Python version or Ubuntu 22.04 for this release.
{{% /notice %}}

## What you've accomplished and what's next

You've installed MLIA with the Neural Technology and LiteRT converter plugins. 

Next, you'll download a pretrained MobileNet baseline to analyze with MLIA.

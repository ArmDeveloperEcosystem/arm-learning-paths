---
title: Install TensorFlow 
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install TensorFlow on Google Axion C4A

TensorFlow is an open-source machine learning library developed by Google for building and deploying ML models efficiently. On aarch64 SUSE VMs, TensorFlow runs natively on CPU or GPU if available.

### Update your system

Update the system and install Python 3.11 with pip and virtual environment support:

```console
sudo zypper refresh
sudo zypper install python311 python311-pip python311-venv
```

Enter "y" when prompted to confirm the installation. This ensures your system has the essential tools required for TensorFlow setup.

### Verify Python installation

Confirm that Python and pip are correctly installed:

```console
python3.11 --version
pip3 --version
```

The output is similar to:

```output
Python 3.11.10
pip 22.3.1 from /usr/lib/python3.11/site-packages/pip (python 3.11)
```

### Create a virtual environment

Set up an isolated Python environment to keep TensorFlow dependencies separate from system packages:

```console
python3.11 -m venv tf-venv
source tf-venv/bin/activate
```

This creates and activates a virtual environment named `tf-venv` that prevents package conflicts.

### Upgrade pip

Upgrade pip to the latest version for reliable package installation:

```console
pip3 install --upgrade pip
```

### Install TensorFlow
Install the latest stable TensorFlow version for Arm64:

```console
pip3 install tensorflow==2.20.0
```

{{% notice Note %}}
TensorFlow 2.18.0 introduced compatibility with NumPy 2.0, incorporating its updated type promotion rules and improved numerical precision. You can review [What's new in TensorFlow 2.18](https://blog.tensorflow.org/2024/10/whats-new-in-tensorflow-218.html) for more information.

The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) recommends TensorFlow version 2.18.0 as the minimum recommended version on Arm platforms.
{{% /notice %}}

### Verify the installation

Check that TensorFlow installed successfully and display the version:

```console
python -c "import tensorflow as tf; print(tf.__version__)"
```

The output is similar to:

```output
2.20.0
```

Your TensorFlow installation is now complete and ready for use.

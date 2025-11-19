---
title: Install TensorFlow 
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## TensorFlow Installation on GCP SUSE VM
TensorFlow is a widely used **open-source machine learning library** developed by Google, designed for building and deploying ML models efficiently. On Arm64 SUSE VMs, TensorFlow can run on CPU natively, or on GPU if available.

### System Preparation
Update the system and install Python3 and pip3 to a compatible version with tensorflow (please enter "y" when prompted to confirm the install):

```console
sudo zypper refresh
sudo zypper install python311 python311-pip python311-venv
```
This ensures your system is up-to-date and installs Python with the essential tools required for TensorFlow setup.

**Verify Python version:**

Confirm that Python and pip are correctly installed and identify their versions to ensure compatibility with TensorFlow requirements.

```console
python3.11 --version
pip3 --version
```

Your particular versions may vary a bit but typically your version output should resemble:

```output
Python 3.11.10
pip 22.3.1 from /usr/lib/python3.11/site-packages/pip (python 3.11)
```

### Create a Virtual Environment (Recommended)
Set up an isolated Python environment (`tf-venv`) so that TensorFlow and its dependencies don’t interfere with system-wide packages or other projects.

```console
python3.11 -m venv tf-venv
source tf-venv/bin/activate
```
Create and activate an isolated Python environment to keep TensorFlow dependencies separate from system packages.

### Upgrade pip
Upgrade pip to the latest version for smooth and reliable package installation.

```console
pip3 install --upgrade pip
```

### Install TensorFlow
Install the latest stable TensorFlow version for Arm64:

```console
pip3 install tensorflow==2.20.0
```

{{% notice Note %}}
TensorFlow 2.18.0 introduced compatibility with NumPy 2.0, incorporating its updated type promotion rules and improved numerical precision.
You can view [this release note](https://blog.tensorflow.org/2024/10/whats-new-in-tensorflow-218.html)

The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) recommends Tensorflow version 2.18.0, the minimum recommended on the Arm platforms.
{{% /notice %}}

### Verify installation:
Run a quick Python command to check that TensorFlow was installed successfully and print the installed version number for confirmation.

```console
python -c "import tensorflow as tf; print(tf.__version__)"
```

You should see an output similar to:
```output
2.20.0
```
TensorFlow installation is complete. You can now go ahead with the baseline testing of TensorFlow in the next section.

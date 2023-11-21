---
title: Install the required dependencies
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin
Independently the kind of Arm machine you use, the instructions of this
learning paths are going to be the same.
You need to login via SSH to your remote server or open a terminal on your
local machine.
The instructions of this learning path are for Ubuntu 22.04 LTS.

## Install a different version of Python (optional)
Ubuntu 22.04 offers pre-installed Python 3.10 binaries. You can use the default
version or you can install the latest version of Python. If you use the default version 
you will still need to install the `python3-pip` and `python3-venv` packages and substitute 
`python3` where `python3.11` is used below.

A quick way to install the most recent version of Python is via
[Deadsnakes PPA](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa).

Add the Deadsnakes repository:

```bash
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt update
```

Install Python 3.11:

```bash
sudo apt install python3.11 python3.11-venv -y
```

Check that Python 3.11 works as expected. 

Run Python:

```bash
python3.11
```

The output will be similar to:

```output
Python 3.11.6 (main, Oct 23 2023, 22:48:54) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
```

Use Control-D or type `exit()` to exit Python. 

{{% notice Note %}}
At the time of writing the latest version of Python is 3.12. Before using the
latest version of Python, please check if the dependencies that you need are
supported. In this case TensorFlow and PyTorch don't provide packages for
Python 3.12 yet.
{{% /notice %}}


## Create the virtual environment
It is good practice to use a virtual environment when dealing with Python
code. Virtual environments allow you to run multiple applications with different
dependencies on the same machine without conflicts.

Create and activate the virtual environment:

```bash
python3.11 -m venv venv
source venv/bin/activate
```

The prompt of your terminal has `(venv)` as prefix and this means the virtual
environment is now active. From this point on, you will run all the commands inside your virtual environment.

## Install Python dependencies
With the active virtual environment, you now install the Python dependencies:

```bash
pip install keras-core tensorflow torch jax[cpu]
```

{{% notice Note %}}
When installing you notice that pip is downloading aarch64 packages like
`torch-2.1.0-cp311-cp311-manylinux2014_aarch64.whl` or
`jaxlib-0.4.20-cp311-cp311-manylinux2014_aarch64.whl`. This means that there is
no need for a compilation as their providers do it for you. This is where you
see what version of Python they support: `cp311` means CPython 3.11.
{{% /notice %}}

After the installation, verify that you have the right packages installed:

```bash
pip list
```
The output should look similar to (versions might change, some dependencies
omitted):

```output
Package                      Version
---------------------------- ---------
...
jax                          0.4.20
jaxlib                       0.4.20
...
keras                        2.15.0
keras-core                   0.1.7
...
numpy                        1.26.2
...
scipy                        1.11.3
...
tensorboard                  2.15.1
tensorboard-data-server      0.7.2
tensorflow                   2.15.0
tensorflow-cpu-aws           2.15.0
tensorflow-estimator         2.15.0
tensorflow-io-gcs-filesystem 0.34.0
...
torch                        2.1.0
wrapt                        1.14.1
...
```

{{% notice Note %}}
Whenever you are in the virtual environment, it is enough just to type
`python` (without appending any version) as it points to the Python binary used
to create the virtual environment.
{{% /notice %}}

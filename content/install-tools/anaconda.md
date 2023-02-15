---
additional_search_terms:
- Python
- TensorFlow
- Pytorch
layout: installtoolsall
minutes_to_complete: 30
multi_install: false
multitool_install_part: false
official_docs: https://docs.anaconda.com/
test_images:
- ubuntu:latest
test_link: null
test_maintenance: true
test_status:
- passed
title: Anaconda
tool_install: true
weight: 1
---

[Anaconda Distribution](https://www.anaconda.com/products/distribution) is a popular open-source Python distribution. 

It includes access to a repository with over 8,000 open-source data science and machine learning packages.

The conda command can be used to quickly install and use Python packages. 

## Introduction

Follow the instructions below to install and use Anaconda Distribution on an Arm server.

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The output should be:

```console
aarch64
```

The installer requires some desktop related libraries. The dependencies can be met by installing a desktop environment. 

For Ubuntu/Debian run the command:

```bash
sudo apt install xfce4 -y
```

For Amazon Linux run the command:

```console
sudo amazon-linux-extras install mate-desktop1.x
```

## Download 

Download the latest Anaconda Distribution.

```bash
wget -O - https://www.anaconda.com/distribution/ 2>/dev/null | sed -ne 's@.*\(https:\/\/repo\.anaconda\.com\/archive\/Anaconda3-.*-Linux-aarch64\.sh\)\">64-Bit (AWS Graviton2 / ARM64) Installer.*@\1@p' | xargs wget
```

Depending on the latest version, the download will be of the form `Anaconda3-202X.0X-Linux-x86_64.sh` where the X values represent the year and month of the latest release.

## Installation {#install}

Run the downloaded install script. It will review the license agreement and ask to accept the terms. 

The default installation directory is `$HOME/anconda3`. Change the installation directory as needed using the `-p` option to the install script.

```bash
sh ./Anaconda3-2022.10-Linux-aarch64.sh -b
```

The install will take a couple of minutes to complete.

The batch installation will not setup the shell. 

To setup the shell run.

```bash
eval "$($HOME/anaconda3/bin/conda shell.bash hook)"
```

## Setting up product license {#license}

Anaconda Distribution is open source and freely available for use. No licenses need to be set up for use.

## Get started {#start}

Test Anaconda Distribution by running simple TensorFlow and Pytorch examples.

### TensorFlow

Create a new conda environment named tf, install TensorFlow, and activate the new environment.

```console
conda create -n tf tensorflow -y
```

Activate the environment.

```console
conda activate tf
```

The shell prompt will now show the tf environment.

```console
(tf) ubuntu@ip-10-0-0-251:~$
```

Run a simple check to make sure TensorFlow is working.

Using a text editor copy and paste the code below into a text file named `tf.py`

```console
import tensorflow as tf
print(tf.__version__)
print(tf.reduce_sum(tf.random.normal([1000,1000])))
exit()
```

Run the example code:

```console
python ./tf.py
```

The expected output is below. Your version may be slightly different. 

```console
2.10.0
tf.Tensor(342.34387, shape=(), dtype=float32)
```

### Pytorch

Create a new conda environment named torch, install PyTorch, and activate the new environment.

```console
conda create -n torch pytorch -y
```

```console
conda activate torch
```

Using a text editor copy and paste the code below into a text file named `pytorch.py`

```console
import torch
x = torch.rand(5,3)
print(x)
exit()
```

Run the example code:

```console
python ./pytorch.py
```

The expected output is:

```console
tensor([[0.9825, 0.4797, 0.0978],
        [0.2175, 0.8025, 0.9663],
        [0.6342, 0.5408, 0.4781],
        [0.0655, 0.7505, 0.9290],
        [0.7643, 0.6878, 0.0993]])
```


There are many machine learning articles and examples using TensorFlow and Pytorch on Arm servers.


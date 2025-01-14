---
additional_search_terms:
- Python
- TensorFlow
- PyTorch
- linux

layout: installtoolsall
minutes_to_complete: 15
author_primary: Jason Andrews
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

The `conda` command can be used to quickly install and use Python packages. 

Follow the instructions below to install and use Anaconda Distribution on an Arm server.

## What should I do before installing Anaconda?

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The output should be:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

The installer requires some desktop related libraries. The dependencies can be met by installing a desktop environment. 

For Ubuntu/Debian, run the command:

```console
sudo apt install xfce4 -y
```

For Amazon Linux, run the command:

```console
sudo amazon-linux-extras install mate-desktop1.x
```

## How do I download the latest Anaconda distribution? 

To download the latest Anaconda distribution, run:

```bash
curl -O https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-aarch64.sh
```

Depending on the version, the downloaded filename will be of the form `Anaconda3-20XX.YY-Linux-aarch64.sh` where the `XX` and `YY` values represent the year and month of the latest release.

## What are the steps to install the downloaded Anaconda distribution?

Run the downloaded install script.

The default installation directory is `$HOME/anaconda3`. Change the installation directory as needed using the `-p` option to the install script.

If you wish to review the license terms before accepting, remove `-b`.

```bash
sh ./Anaconda3-2024.10-1-Linux-aarch64.sh -b
```

The install takes a couple of minutes to complete.

The batch installation will not set up the shell. 

To set up the shell, run:

```bash
eval "$($HOME/anaconda3/bin/conda shell.bash hook)"
```

## How do I get started with Anaconda after installation?

Test Anaconda Distribution by running simple TensorFlow and PyTorch examples.

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

```output
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

The expected output format is below. Your version may be slightly different. 

```output
2.12.0
tf.Tensor(342.34387, shape=(), dtype=float32)
```

### PyTorch

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
print(torch.__version__)
x = torch.rand(5,3)
print(x)
exit()
```

Run the example code:

```console
python ./pytorch.py
```

The expected output is similar to:

```output
2.1.0
tensor([[0.9287, 0.5931, 0.0239],
        [0.3402, 0.9447, 0.8897],
        [0.3161, 0.3749, 0.6848],
        [0.8091, 0.6998, 0.7517],
        [0.2873, 0.0549, 0.2914]])
```


You are ready to use Anaconda Distribution. 

Explore the many machine learning articles and examples using TensorFlow and PyTorch.

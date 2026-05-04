---
additional_search_terms:
- Python
- TensorFlow
- PyTorch
- linux

layout: installtoolsall
minutes_to_complete: 15
author: Jason Andrews
multi_install: false
multitool_install_part: false
official_docs: https://docs.anaconda.com/
description: Install Anaconda Distribution on Arm Linux (aarch64) and verify the setup by creating conda environments with TensorFlow and PyTorch.
ecosystem_dashboard: https://developer.arm.com/ecosystem-dashboard/linux?package=anaconda
test_images:
- ubuntu:latest
test_link: null
test_maintenance: true
title: Anaconda
tool_install: true
weight: 1
---

[Anaconda Distribution](https://www.anaconda.com/products/distribution) is a popular open-source Python distribution. It includes access to a repository with over 8,000 open-source data science and machine learning packages.

You can use the `conda` command to quickly install and use Python packages.

In this guide, you'll learn how to install and use Anaconda Distribution on an Arm server.

## Before you begin

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The output is similar to:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

The installer requires some desktop related libraries. You can meet the dependencies by installing a desktop environment by running the commands for your Linux distribution.

{{< tabpane code=true >}}
  {{< tab header="Ubuntu/Debian" language="bash">}}
sudo apt update
sudo apt install xfce4 -y
  {{< /tab >}}
  {{< tab header="Amazon Linux" language="bash">}}
sudo amazon-linux-extras install mate-desktop1.x
  {{< /tab >}}
{{< /tabpane >}}

## Download the latest Anaconda Distribution

To download Anaconda Distribution, run:

{{% notice Note %}}
The following commands use Anaconda version 2025.12.2. The same commands work with other versions. Replace the file used in these steps with the file for your version of choice. To find the latest version, see [Anaconda Distribution release notes](https://www.anaconda.com/docs/getting-started/anaconda/release-notes).
{{% /notice %}}

```bash
curl -O https://repo.anaconda.com/archive/Anaconda3-2025.12-2-Linux-aarch64.sh
```

Depending on the version, the downloaded filename will be of the form `Anaconda3-20XX.YY-Linux-aarch64.sh` where the `XX` and `YY` values represent the year and month of the latest release. 

## Install the Anaconda Distribution

Run the downloaded install script.

The default installation directory is `$HOME/anaconda3`. Change the installation directory as needed using the `-p` option to the install script.

To review the license terms before accepting, remove `-b`.

```bash
sh ./Anaconda3-2025.12-2-Linux-aarch64.sh -b
```

The install takes a couple of minutes to complete.

The batch installation won't set up the shell. To set up the shell, run:

```bash
eval "$($HOME/anaconda3/bin/conda shell.bash hook)"
```

## Get started with Anaconda 

Test Anaconda Distribution by running the following TensorFlow and PyTorch examples.

### Use TensorFlow with Anaconda

Create a new conda environment named `tf` and install TensorFlow:

```console
conda create -n tf tensorflow -y
```

Activate the new environment:

```console
conda activate tf
```

The shell prompt will now show the tf environment.

```output
(tf) ubuntu@ip-10-0-0-251:~$
```

Run a simple check to make sure TensorFlow is working.

Using a text editor, copy and paste the code below into a text file named `tf.py`:

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

The output is similar to:

```output
2.12.0
tf.Tensor(342.34387, shape=(), dtype=float32)
```

### Use PyTorch with Anaconda

Create a new conda environment named `torch` and install PyTorch:

```console
conda create -n torch pytorch -y
```
Activate the new environment:

```console
conda activate torch
```

Using a text editor, copy and paste the following code into a text file named `pytorch.py`:

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

The output is similar to:

```output
2.1.0
tensor([[0.9287, 0.5931, 0.0239],
        [0.3402, 0.9447, 0.8897],
        [0.3161, 0.3749, 0.6848],
        [0.8091, 0.6998, 0.7517],
        [0.2873, 0.0549, 0.2914]])
```


You are ready to use Anaconda Distribution.
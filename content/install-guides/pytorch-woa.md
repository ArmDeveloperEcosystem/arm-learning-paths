---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: PyTorch for Windows on Arm

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- python
- windows
- woa
- windows on arm
- open source windows on arm
- pytorch

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

### Link to official documentation
official_docs: https://docs.pytorch.org/docs/stable/index.html

author: Pareena Verma

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

PyTorch has native support for [Windows on Arm](https://learn.microsoft.com/en-us/windows/arm/overview). Starting with PyTorch 2.7 release, you can access Arm native builds of PyTorch for Windows available for Python 3.12. 

A number of developer-ready Windows on Arm [devices](/learning-paths/laptops-and-desktops/intro/find-hardware/) are available.

Windows on Arm instances are available with Microsoft Azure. For further information, see [Deploy a Windows on Arm virtual machine on Microsoft Azure](/learning-paths/cross-platform/woa_azure/).

## How do I install PyTorch for Windows on Arm?

{{% notice Environment Details %}}
* PyTorch 2.7.0
* Python 3.12.9
* Windows 11 for Arm64
{{% /notice %}}

Before you install PyTorch on your Windows on Arm machine, you will need to install [Python version 3.12 for Windows on Arm](https://www.python.org/downloads/release/python-3129/). Select the Windows ARM64 installer.

{{% notice Note %}} Make sure to install Python 3.12 as the Arm native builds for PyTorch on Windows are built with Python version 3.12 {{% /notice %}}

Verify your Python installation at a Windows Command prompt or a PowerShell prompt:

```command
python --version
```
The output should look like:

```output
Python 3.12.9
```
Once you have downloaded Python, you can install the PyTorch Stable release (2.7.0) on your Windows on Arm machine. 

```command
pip3 install torch==2.7.0 --index-url https://download.pytorch.org/whl/cpu
```

You will see that the `arm64` wheel for PyTorch is installed on your machine:
```output
Downloading https://download.pytorch.org/whl/cpu/torch-2.7.0%2Bcpu-cp312-cp312-win_arm64.whl (107.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 107.9/107.9 MB 29.7 MB/s eta 0:00:00
Downloading https://download.pytorch.org/whl/sympy-1.13.3-py3-none-any.whl (6.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.2/6.2 MB 47.4 MB/s eta 0:00:00
Downloading https://download.pytorch.org/whl/typing_extensions-4.12.2-py3-none-any.whl (37 kB)
Downloading https://download.pytorch.org/whl/filelock-3.13.1-py3-none-any.whl (11 kB)
Downloading https://download.pytorch.org/whl/fsspec-2024.6.1-py3-none-any.whl (177 kB)
Downloading https://download.pytorch.org/whl/Jinja2-3.1.4-py3-none-any.whl (133 kB)
Downloading https://download.pytorch.org/whl/networkx-3.3-py3-none-any.whl (1.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.7/1.7 MB 30.6 MB/s eta 0:00:00
```

You can also install the nightly preview versions of PyTorch on your Windows Arm machine:

```command
pip install --pre torch --index-url https://download.pytorch.org/whl/nightly/cpu
```

## How can I run a PyTorch example?

To run a PyTorch example and confirm that PyTorch is working, use a text editor to save the code below to a file named `pytorch_woa.py`:

```python
import torch
import platform

# Print PyTorch version
print("PyTorch version:", torch.__version__)

# Check if CUDA is available
if torch.cuda.is_available():
    print("CUDA is available. PyTorch can use the GPU.")
else:
    print("CUDA is not available. PyTorch will use the CPU.")

# Detect system architecture
architecture = platform.machine()
if "ARM" in architecture.upper() or "AARCH" in architecture.upper():
    print("PyTorch is running on Arm:", architecture)
else:
    print("PyTorch is not running on Arm. Detected architecture:", architecture)

# Perform a basic PyTorch operation to confirm it's working
try:
    tensor = torch.tensor([1.0, 2.0, 3.0])
    print("PyTorch is operational. Tensor created:", tensor)
except Exception as e:
    print("An error occurred while testing PyTorch:", e)
```
Run the code:

```console
python pytorch_woa.py
```
Running on a Windows on Arm machine produces an output similar to:

```output
PyTorch version: 2.7.0+cpu
CUDA is not available. PyTorch will use the CPU.
PyTorch is running on Arm: ARM64
PyTorch is operational. Tensor created: tensor([1., 2., 3.])
```
{{% notice Note %}}
PyTorch builds for Windows on Arm are CPU-only. CUDA (GPU acceleration) is not supported on this platform.
{{% /notice %}}


You are now ready to use PyTorch on your Windows on Arm device. 

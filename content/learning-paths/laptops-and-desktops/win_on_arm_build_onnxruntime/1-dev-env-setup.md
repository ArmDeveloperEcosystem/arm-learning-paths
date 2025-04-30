---
title: Set up your Environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this Learning Path, you'll learn how to build and deploy a large language model (LLM) on a Windows on Arm (WoA) machine using ONNX Runtime for inference. 

Specifically, you'll learn how to:

* Build ONNX Runtime and the Generate() API library.
* Download the Phi-3 model and run inference. 
* Run the short-context (4K) Mini (3.3B) variant of Phi 3 model. 

{{% notice Note %}}
The short-context version accepts shorter (4K) prompts and generates shorter outputs than the long-context (128K) version. It also consumes less memory.
{{% /notice %}}

## Set up your Development Environment 

Your first task is to prepare a development environment with the required software. 

Start by installing the required tools:

- Visual Studio 2022 IDE (the latest version available is recommended).
- Python 3.10 or higher.
- CMake 3.28 or higher.

{{% notice Note %}}
These instructions were tested on a 64-bit WoA machine with at least 16GB of RAM.
{{% /notice %}}

## Install and Configure Visual Studio 2022 

Now, to install and configure Visual Studio, follow these steps:

1. Download the latest [Visual Studio IDE](https://visualstudio.microsoft.com/downloads/). 

2. Select the **Community** edition. This downloads an installer called `VisualStudioSetup.exe`. 

3. Run `VisualStudioSetup.exe` from your **Downloads** folder.

4. Follow the prompts and accept the License Terms and Privacy Statement.

5. When prompted to select workloads, select **Desktop Development with C++**. This installs the **Microsoft Visual Studio Compiler** (**MSVC**).

## Install Python

Download and install [Python for Windows on Arm](/install-guides/py-woa).

{{% notice Note %}}
You'll need Python version 3.10 or higher. This Learning Path was tested with version 3.11.9.
{{% /notice %}}

## Install CMake

CMake is an open-source tool that automates the build process and generates platform-specific build configurations.

Download and install [CMake for Windows on Arm](/install-guides/cmake).

{{% notice Note %}}
The instructions were tested with version 3.30.5.
{{% /notice %}}

You’re now ready to build ONNX Runtime and run inference using the Phi-3 model.

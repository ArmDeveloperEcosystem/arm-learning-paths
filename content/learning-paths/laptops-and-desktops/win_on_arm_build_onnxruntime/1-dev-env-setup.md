---
title: Development environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up your development environment

In this learning path, you will learn how to build and deploy a LLM on a Windows on Arm (WoA) laptop using ONNX Runtime for inference. 

You will first learn how to build the ONNX Runtime and ONNX Runtime Generate() API library and then how to download the Phi-3 model and run the inference. You will run the short context (4k) mini (3.3B) variant of Phi 3 model. The short context version accepts a shorter (4K) prompts and produces shorter output text compared to the long (128K) context version. The short version will consume less memory.

Your first task is to prepare a development environment with the required software:

- Visual Studio 2022 IDE (latest version recommended)
- Python 3.10 or higher
- CMake 3.28 or higher

The following instructions were tested on an WoA 64-bit Windows machine with at least 16GB of RAM.

## Install Visual Studio 2022 IDE

Follow these steps to install and configure Visual Studio 2022 IDE:

1. Download and install the latest version of [Visual Studio IDE](https://visualstudio.microsoft.com/downloads/). 

2. Select the **Community Version**. An installer called *VisualStudioSetup.exe* will be downloaded.

3. From your Downloads folder, double-click the installer to start the installation.

4. Follow the prompts and acknowledge **License Terms** and **Privacy Statement**.

5. Once "Downloaded" and "Installed" complete select your workloads. As a minimum you should select **Desktop Development with C++**. This will install the **Microsoft Visual Studio Compiler** or **MSVC**.

## Install Python

Download and install [Python for Windows on Arm](/install-guides/py-woa)

You will need Python version 3.10 or higher. This learning path was tested with version 3.11.9.

## Install CMake

CMake is an open-source tool that automates the build process for software projects, helping to generate platform-specific build configurations.

[Download and install CMake](/install-guides/cmake)

{{% notice Note %}}
The instructions were tested with version 3.30.5
{{% /notice %}}

You now have the required development tools installed to follow this learning path.

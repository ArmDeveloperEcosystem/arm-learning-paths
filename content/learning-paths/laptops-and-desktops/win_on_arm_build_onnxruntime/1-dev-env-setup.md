---
title: Set up your Environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up your development environment

In this learning path, you'll learn how to build and deploy an LLM on a Windows on Arm (WoA) laptop using ONNX Runtime for inference. 

You'll first learn how to build the ONNX Runtime and ONNX Runtime Generate() API library and then how to download the Phi-3 model and run the inference. You'll run the short context (4k) mini (3.3B) variant of Phi 3 model. The short context version accepts a shorter (4K) prompts and produces shorter output text compared to the long (128K) context version. The short version consumes less memory.

Your first task is to prepare a development environment with the required software:

- Visual Studio 2022 IDE (latest version recommended)
- Python 3.10 or higher
- CMake 3.28 or higher

The following instructions were tested on a WoA 64-bit Windows machine with at least 16GB of RAM.

## Install Visual Studio 2022 IDE

Follow these steps to install and configure Visual Studio 2022 IDE:

1. Download the latest [Visual Studio IDE](https://visualstudio.microsoft.com/downloads/). 

2. Select the **Community** edition. An installer called *VisualStudioSetup.exe* will be downloaded.

3. Run the downloaded installer (*VisualStudioSetup.exe*) from your **Downloads** folder.

4. Follow the installation prompts and accept the **License Terms** and **Privacy Statement**.

5. When prompted to select your workloads, select **Desktop Development with C++**. This includes **Microsoft Visual Studio Compiler** (**MSVC**).

## Install Python

Download and install [Python for Windows on Arm](/install-guides/py-woa).

{{% notice Note %}}
You'll need Python version 3.10 or higher. This Learning Path was tested with version 3.11.9.
{{% /notice %}}

## Install CMake

CMake is an open-source tool that automates the build process and helps generate platform-specific build configurations.

Download and install [CMake for Windows on Arm](/install-guides/cmake).

{{% notice Note %}}
The instructions were tested with version 3.30.5.
{{% /notice %}}

You’re now ready to move on to building the ONNX Runtime and running inference with Phi-3.

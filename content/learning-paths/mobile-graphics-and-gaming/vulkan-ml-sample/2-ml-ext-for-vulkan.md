---
title: Setting up the ML Emulation Layers for Vulkan
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

To run the Vulkan Samples, you first need to set up your development environment.

This setup involves two main steps:

* Install the required tools on your development machine
* Download the ML emulation layers for Vulkan, which simulate the `VK_ARM_data_graph` and `VK_ARM_tensors` extensions

## Install required tools for development

Before building and running the samples, ensure the following tools are installed on your development machine:

- CMake (version 3.12 or later)
- Python 3
- Git

In VSCode create a new folder for this project then make sure you have the following extensions: 
  * C/C++ From Microsoft 
  * CMake Tools From Microsoft

![C/C++ tools extension](images/c%20ext.png)

![Cmake tools extension](images/cmake%20ext.png)


Create a Venv in Python (3.13 was used in the creation of this Guide) and run the following commands 

```bash
pip install ai-ml-emulation-layer-for-vulkan, cmake
```

To verify your installation, run the following commands:

```bash
cmake --version
python3 --version
git --version
```

Each command should print the installed version of the tool.

### Install Vulkan Software Development Kit

Go to the [Getting Started with the Windows Vulkan SDK](https://vulkan.lunarg.com/sdk/home) and download the SDK Installer for Windows. This installs **Vulkan Configurator** which is used to run the emulation layers.

{{% notice Note %}}

You must use a version >= 1.4.321 for the Vulkan SDK.

{{% /notice %}}


## Enable the emulation layers in Vulkan Configurator

Next, enable the emulation layers using the Vulkan Configurator to simulate the `VK_ARM_data_graph` and `VK_ARM_tensors` extensions. Open **Vulkan Configurator**.

Under the **Vulkan Layers Available** tab, add the path to your `Emulation layer` folder that can be found in the site packages of your venv folder select the bin folder.


![VL available](images/VL%20availble%20.png)

Under the **Vulkan layers Configuration** tabgo through each setting in the top rigt except disable all Vulkan Layers and enable the Graph and Tensor Emulation

Ensure that the **Graph** layer is listed above the **Tensor** layer.

![VL Config](images/VL%20Config.png)

{{% notice Important %}}

Keep Vulkan Configurator running while you run the Vulkan samples.

{{% /notice %}}

With the emulation layers configured, you're ready to build the Vulkan Samples. Continue to the next section to get started.


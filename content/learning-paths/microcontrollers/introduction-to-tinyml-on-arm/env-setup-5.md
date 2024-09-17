---
# User change
title: "Environment Setup for TinyML Development on Arm"

weight: 6 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
## Before you begin 

These instructions have been tested on:
- A GCP Arm-based Tau T2A Virtual Machine instance Running Ubuntu 22.04 LTS.
- Host machine with Ubuntu 24.04 on x86_64 architecture.

The host machine is where you will perform most of your development work, especially cross-compiling code for the target Arm devices.

You can use your own Linux host machine or use [Arm Virtual Hardware (AVH)](https://www.arm.com/products/development-tools/simulation/virtual-hardware) for this Learning Path.

The Ubuntu version should be `20.04 or higher`. The `x86_64` architecture must be used because the Corstone-300 FVP is not currently available for the Arm architecture. You will need a Linux desktop to run the FVP because it opens graphical windows for input and output from the software applications. Also, though Executorch supports Windows via WSL, it is limited in resource.

If you want to use Arm Virtual Hardware the [Arm Virtual Hardware install guide](/install-guides/avh#corstone) provides setup instructions.

### Compilers 

The examples can be built with [Arm Compiler for Embedded](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Embedded) or [Arm GNU Toolchain](https://developer.arm.com/Tools%20and%20Software/GNU%20Toolchain). 

Both compilers are pre-installed in Arm Virtual Hardware.

Alternatively, if you are using Arch Linux or its derivatives, you can use Pacman to install GCC. 

Use the install guides to install the compilers on your computer:
- [Arm Compiler for Embedded](/install-guides/armclang/)
- [Arm GNU Toolchain](/install-guides/gcc/arm-gnu)
- Using Pacman:
 
```console
pacman -S aarch64-linux-gnu-gcc
```

### Corstone-300 FVP {#fvp}

To install the Corstone-300 FVP on your computer refer to the [install guide for Arm Ecosystem FVPs](/install-guides/fm_fvp). 

The Corstone-300 FVP is pre-installed in Arm Virtual Hardware. 


## Install Executorch

1. Follow the [Setting Up ExecuTorch guide](https://pytorch.org/executorch/stable/getting-started-setup.html ) to install it.

2. Activate the `executorch` virtual environment from the installation guide:

```console
conda activate executorch
```


## Setup on Grove - Vision AI Module V2 
Due to its constrained environment, we'll focus on lightweight, optimized tools and models (will be introcuded in the next learning path).

1. Connect the Grove - Vision AI Module V2 to your computer using the USB-C cable. 

![Board connection #center](connect.png)

2. Install Edge Impulse CLI. It will help in data collection and model deployment.

```console
npm install -g edge-impulse-cli
```

3. Configure Edge Impulse for the board
In your terminal, run:

```console
edge-impulse-daemon
```
Follow the prompts to log in.

4. Verify Setup
Connect to your device

```console
edge-impulse-run-impulse --api-key YOUR_API_KEY
```

If successful, you should see data from your Grove - Vision AI Module V2.

5. Install Executorch 

```console
pip install executorch
```

---
# User change
title: "Environment Setup"

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

## Install PyTorch
The latest version needs Python 3.8 or later

```console
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

```

## Install Executorch

1. Follow the [Setting Up ExecuTorch guide](https://pytorch.org/executorch/stable/getting-started-setup.html ) to install it.

2. Activate the `executorch` virtual environment from the installation guide:

```console
conda activate executorch
```

## Install Edge Impulse CLI
1. Create an [Edge Impulse Account](https://studio.edgeimpulse.com/signup) if you do not have one 

2. Install the CLI tools

Ensure you have Nodejs install 

```console
node -v 
```
Install the Edge Impulse CLI
```console
npm install -g edge-impulse-cli
```
3. Install Edge Impulse Screen
```console
sudo apt install screen
```

4. Download and extract the latest Edge Impulse firmware
Grove Vision V2 [Edge impulse Firmware](https://cdn.edgeimpulse.com/firmware/seeed-grove-vision-ai-module-v2.zip). 


## Setup on Grove - Vision AI Module V2 
Due to its constrained environment, we'll focus on lightweight, optimized tools and models (will be introcuded in the next learning path).

![Hardware Overview #center](Overview.png)

Hardware overview : [Image credits](https://wiki.seeedstudio.com/grove_vision_ai_v2/). 

1. Connect the Grove - Vision AI Module V2 to your computer using the USB-C cable. 

![Board connection](Connect.png)


2. In the extracted Edge Impulse firmware, locate and run the installation scripts to flash your device. 

```console
./flash_linux.sh
```

3. Configure Edge Impulse for the board
in your terminal, run:

```console
edge-impulse-daemon
```
Follow the prompts to log in.

4. Verify your board is connected

If successful, you should see your Grove - Vision AI Module V2 under 'Devices' in Edge Impulse.


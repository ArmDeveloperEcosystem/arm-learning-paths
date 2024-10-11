---
# User change
title: "Environment Setup on Host Machine"

weight: 6 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
## Before you begin 

These instructions have been tested on:
- A GCP Arm-based Tau T2A Virtual Machine instance Running Ubuntu 22.04 LTS.
- Host machine with Ubuntu 24.04 on x86_64 architecture.
- Windows Subsystem for Linux (WSL): Windows x86_64

The host machine is where you will perform most of your development work, especially cross-compiling code for the target Arm devices.

- The Ubuntu version should be `20.04 or higher`. 
- If you do not have the board, the `x86_64` architecture must be used because the Corstone-300 FVP is not currently available for the Arm architecture.
- Also, though Executorch supports Windows via WSL, it is limited in resource.


### Corstone-300 FVP Setup for ExecuTorch

To install and set up the Corstone-300 FVP and ExecuTorch on your machine, refer to [Building and Running ExecuTorch with ARM Ethos-U Backend](https://pytorch.org/executorch/stable/executorch-arm-delegate-tutorial.html). Follow this tutorial till the **"Install the TOSA reference model"** Section. It should be the last thing you do from this tutorial.



## Install Executorch

1. Follow the [Setting Up ExecuTorch guide](https://pytorch.org/executorch/stable/getting-started-setup.html ) to install it.

2. Activate the `executorch` virtual environment from the installation guide to ensure it is ready for use:

```console
conda activate executorch
```

## Install PyTorch
The latest version needs Python 3.8 or later

```console
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

```

## Install Edge Impulse CLI
1. Create an [Edge Impulse Account](https://studio.edgeimpulse.com/signup) if you do not have one 

2. Install the CLI tools in your terminal

Ensure you have Nodejs installed

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

## Next Steps
1. If you don't have access to the physical board: Skip to [Environment Setup Corstone-300 FVP](/learning-paths/microcontrollers/introduction-to-tinyml-on-arm/setup-6-FVP.md)
2. If you have access to the board: Skip to [Setup on Grove - Vision AI Module V2](/learning-paths/microcontrollers/introduction-to-tinyml-on-arm/setup-6-Grove.md)
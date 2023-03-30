---
# User change
title: Required hardware and software

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
Arm Trusted Firmware provides a reference implementation of Platform Security Architecture (PSA). Reference implementations are available for a number of [platforms](https://tf-m-user-guide.trustedfirmware.org/platform/index.html).

This Learning Path uses the [Corstone-1000](https://www.arm.com/en/products/silicon-ip-subsystems/corstone-1000) platform.

The software stack can be executed on the Corstone-1000 Fixed Virtual Platform (FVP) and the MPS3 FPGA prototyping board.

You can also use the FPGA prototyping board to demonstrate Authenticated Debug (PSA-ADAC) in conjunction with Arm Development Studio.

## Before you begin

You will need the hardware and software listed below to complete the steps in this Learning Path. 

### Development machine

Use a Linux computer running Ubuntu 18.04 or later (x86_64 architecture) as the development machine.

If you don't have the required computer, you can use [Arm Virtual Hardware](https://www.arm.com/products/development-tools/simulation/virtual-hardware) which is hosted on `AWS` and includes the Corstone-1000 FVP.

The instructions have been tested using the [Arm Virtual Hardware AMI](https://aws.amazon.com/marketplace/pp/prodview-urbpq7yo5va7g) running on a `t3.xlarge` EC2 instance with `100GB` of storage.

### Corstone-1000 FVP

Download and install the [Arm Ecosystem FVP](https://developer.arm.com/downloads/-/arm-ecosystem-fvps) on your development machine.

If you are using Arm Virtual Hardware, the Corstone-1000 FVP is already installed on the virtual machine. 

### MPS3 FPGA prototyping board

You will need an [MPS3 FPGA Prototyping Board](https://developer.arm.com/Tools%20and%20Software/MPS3%20FPGA%20Prototyping%20Board) programmed with [AN550](https://developer.arm.com/downloads/view/AN550) to demonstrate Authenticated Debug.

The image requires the `QSPI Flash Module` to be installed. Refer to section 8.2 of the [AN550 documentation](https://developer.arm.com/documentation/dai0550/latest/).

### Arm Development Studio and DSTREAM

To demonstrate PSA-ADAC Authenticated Debug, you will need [Arm Development Studio](https://www.arm.com/products/development-tools/embedded-and-software/arm-development-studio) Silver (or higher), version 2022.3 or later. Refer to the [install guide](/install-guides/armds/) for installation instructions. 

You will also need an appropriate [DSTREAM](https://www.arm.com/products/development-tools/debug-probes/dstream-st) Debug Probe. 

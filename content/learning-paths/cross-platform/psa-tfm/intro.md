---
# User change
title: Pre-requisites

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
Arm Trusted Firmware provides a reference implementation of Platform Security Architecture (PSA). Reference implementations are available for a number of [platforms](https://tf-m-user-guide.trustedfirmware.org/platform/index.html).

We shall use the [Corstone-1000](https://www.arm.com/en/products/silicon-ip-subsystems/corstone-1000) implementation.

The software stack can be executed on the Corstone-1000 FVP or MPS3 FPGA implementation.

The FPGA implementation can also demonstrate Authenticated Debug (PSA-ADAC) in conjunction with Arm Development Studio.

## Build machine

A Linux machine running Ubuntu 18.04 or later is required. You may wish to use [Arm Virtual Hardware](https://www.arm.com/products/development-tools/simulation/virtual-hardware) which is hosted on `AWS`, and includes the Corstone-1000 FVP.

This learning path was written using the [AMI](https://aws.amazon.com/marketplace/pp/prodview-urbpq7yo5va7g), running on a `t3.xlarge` instance with `100GB` of storage.

## FVP

If not using Arm Virtual Hardware, the Corstone-1000 FVP can be downloaded and installed locally from the [Arm Ecosystem FVP](https://developer.arm.com/downloads/-/arm-ecosystem-fvps) page.

## MPS3

If you wish to use the FPGA implementation (necessary for Authenticated Debug later), you require an [MPS3 FPGA Prototyping Board](https://developer.arm.com/Tools%20and%20Software/MPS3%20FPGA%20Prototyping%20Board) programmed with [AN550](https://developer.arm.com/downloads/view/AN550). The image requires `QSPI Flash Module` to be installed (see section 8.2 of the supplied documentation).

## Arm Development Studio and DSTREAM

To demonstrate PSA-ADAC Authenticated Debug, you also need a valid [Arm Development Studio](https://www.arm.com/products/development-tools/embedded-and-software/arm-development-studio) Silver (or higher) license, with version 2022.3 or later. You also require an appropriate [DSTREAM](https://www.arm.com/products/development-tools/debug-probes/dstream-st) Probe.

---
title: Introduction to Arm Fixed Virtual Platforms (FVPs)
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### What are Arm FVPs, and what can they do?

Arm Fixed Virtual Platforms (FVPs) are fast, functional simulation models of Arm hardware. They give you the ability to develop, test, and debug full software stacks. This includes firmware, bootloaders, and operating systems - all without the need for access to physical Arm silicon. FVPs replicate Arm CPU behavior, memory, and peripherals using fast binary translation.

### Why use FVPs?
FVPs are ideal for early software development and system debugging. 

Developers can use them to do the following tasks:

- Prototype firmware and OS code before silicon is available
- Debug complex boot sequences and kernel issue
- Simulate multi-core systems to analyze performance and thread scheduling

FVPs provide a programmer's view of the hardware, making them ideal for the following:

* System bring-up
* Kernel porting
* Low-level debug tasks.

### How can I get access to the Arm FVPs?

You can download prebuilt Armv8-A FVPs at no cost from the [Arm Ecosystem Models](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms#Downloads) page. 

Available categories include:
- Architecture
- Automotive
- Infrastructure
- IoT

A popular model is the AEMv8-A Base Platform RevC, which simulates generic Armv8.7-A and Armv9-A CPUs and is fully supported by Arm's open-source [reference software stack](https://gitlab.arm.com/arm-reference-solutions/arm-reference-solutions-docs/-/blob/master/docs/aemfvp-a/user-guide.rst).

### CPU-Specific Arm-based FVPs
Some FVPs target specific CPU implementations and include fixed core counts. These are known as CPU FVPs.

Examples include:
- FVP_Base_Cortex-A55x4
- FVP_Base_Cortex-A72x4
- FVP_Base_Cortex-A78x4
- FVP_Base_Cortex-A510x4+Cortex-A710x4

To use these, request access via [support@arm.com](mailto:support@arm.com).

### Set up your environment
This Learning Path uses the open-source Arm reference software stack, which includes the following:

* Prebuilt Linux images
* Firmware
* Configuration files

To get started:

* Follow the [software user guide](https://gitlab.arm.com/arm-reference-solutions/arm-reference-solutions-docs/-/blob/master/docs/aemfvp-a/user-guide.rst) to download the stack.
* Set up your toolchain
* Export environment variables
* Verify your build dependencies

Once setup is complete, you’ll be ready to boot and debug Linux on your selected Arm FVP model.
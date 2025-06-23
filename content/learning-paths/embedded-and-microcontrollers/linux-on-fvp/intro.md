---
title: Introduction to Arm Fixed Virtual Platforms (FVPs)
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Arm Fixed Virtual Platforms (FVPs) are fast, functional simulation models of Arm hardware. They let you develop, test, and debug full software stacks—including firmware, bootloaders, and operating systems—without needing access to physical Arm silicon. FVPs replicate Arm CPU behavior, memory, and peripherals using fast binary translation.

### Why use FVPs?
FVPs are ideal for early software development and system debugging. Developers can use them to do the following:
- Prototype firmware and OS code before silicon is available
- Debug complex boot sequences and kernel issue
- Simulate multi-core systems to analyze performance and thread scheduling

FVPs provide a programmer's view of the hardware, making them ideal for system bring-up, kernel porting, and low-level debug tasks.

### Freely available Arm ecosystem FVPs

You can download prebuilt Armv8-A FVPs at no cost from the [Arm Ecosystem Models](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms#Downloads) page. 

Available categories include:
- Architecture
- Automotive
- Infrastructure
- IoT

A popular model is the AEMv8-A Base Platform RevC, which simulates generic Armv8.7-A and Armv9-A CPUs and is fully supported by Arm's open-source [reference software stack](https://gitlab.arm.com/arm-reference-solutions/arm-reference-solutions-docs/-/blob/master/docs/aemfvp-a/user-guide.rst).

### CPU-Specific Arm-based FVPs
Some FVPs target specific CPU implementations and include fixed core counts. These are known as **CPU FVPs**.

Here are some examples:
- FVP_Base_Cortex-A55x4
- FVP_Base_Cortex-A72x4
- FVP_Base_Cortex-A78x4
- FVP_Base_Cortex-A510x4+Cortex-A710x4

To use these, request access via [support@arm.com](mailto:support@arm.com).

### Set up your environment
This Learning Path uses the open-source [Arm reference software stack](https://gitlab.arm.com/arm-reference-solutions/arm-reference-solutions-docs/-/blob/master/docs/aemfvp-a/user-guide.rst), which includes prebuilt Linux images, firmware, and configuration files.

To get started:
1. Follow the software user guide to download the stack.
2. Set up your toolchain, export environment variables, and verify your build dependencies.

Once setup is complete, you’ll be ready to boot and debug Linux on your selected Arm FVP model.
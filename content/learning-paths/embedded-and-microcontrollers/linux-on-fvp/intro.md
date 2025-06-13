---
title: Introduction to Arm Fixed Virtual Platforms (FVPs)
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Arm Fixed Virtual Platforms (FVPs) are simulation models that let you run and test full software stacks on Arm systems before physical hardware is available. They replicate the behavior of Arm CPUs, memory, and peripherals using fast binary translation.

### Why Use FVPs?
FVPs are useful for developers who want to:
- Prototype software before silicon availability
- Debug firmware and kernel issues
- Simulate multicore systems

FVPs provide a programmer's view of the hardware, making them ideal for system bring-up, kernel porting, and low-level debugging.

### Freely Available Arm Ecosystem FVPs
Several pre-built Armv8-A FVPs can be downloaded for free from the [Arm Ecosystem Models](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms#Downloads) page. Categories include:
- Architecture
- Automotive
- Infrastructure
- IoT

A popular model is the **AEMv8-A Base Platform RevC**, which supports Armv8.7 and Armv9-A. The [Arm reference software stack](https://gitlab.arm.com/arm-reference-solutions/arm-reference-solutions-docs/-/blob/master/docs/aemfvp-a/user-guide.rst) is designed for this model.

### CPU-Specific Arm Base FVPs
Other FVPs target specific CPU types and come pre-configured with a fixed number of cores. These are often called **CPU FVPs**.

Here are some examples:
- FVP_Base_Cortex-A55x4
- FVP_Base_Cortex-A72x4
- FVP_Base_Cortex-A78x4
- FVP_Base_Cortex-A510x4+Cortex-A710x4

To use these, request access via [support@arm.com](mailto:support@arm.com).

### Setting Up Your Environment
This Learning Path uses the [Arm reference software stack](https://gitlab.arm.com/arm-reference-solutions/arm-reference-solutions-docs/-/blob/master/docs/aemfvp-a/user-guide.rst).

To get started:
1. Follow the software user guide to download the stack.
2. Set up the required toolchain and environment variables.

Once configured, you’ll be ready to run and debug Linux on your selected Arm FVP model.
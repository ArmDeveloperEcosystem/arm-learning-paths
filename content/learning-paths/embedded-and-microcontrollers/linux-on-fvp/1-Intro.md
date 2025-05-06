---
title: Introduction to Arm Ecosystem Fixed Virtual Platforms
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Arm Ecosystem Fixed Virtual Platforms (FVPs) model hardware subsystems target different market segments and applications.

FVPs use binary translation technology to deliver fast, functional simulations of Arm-based systems, including processor, memory, and peripherals. They implement a programmer's view suitable for software development and enable execution of full software stacks, providing a widely available platform ahead of silicon.

Arm provides different types of FVPs. There are several freely available, pre-built Armv8‑A FVPs for download from [Arm Ecosystem Models](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms) on Arm Developer website. You can use these FVPs without a license. For example, the AEMv8-A Base Platform RevC FVP is freely available, and it supports the latest Armv8‑A architecture versions up to v8.7 and Armv9-A.

The [Arm reference software stack](https://gitlab.arm.com/arm-reference-solutions/arm-reference-solutions-docs/-/blob/master/docs/aemfvp-a/user-guide.rst) is based on the above RevC model. However, some Armv8 FVPs with a fixed number of cores are replaced by FVPs with a configurable number of cores, for example:

* FVP_Base_Cortex-A55x4
* FVP_Base_Cortex-A78x4
* FVP_Base_Cortex-X1x4
* FVP_Base_Cortex-X2x4
* FVP_Base_Cortex-A78AEx2
* FVP_Base_Cortex-A76x4
* FVP_Base_Neoverse-N2x1
* FVP_Base_Neoverse-N1x4
* FVP_Base_Cortex-A510x4
* FVP_Base_Cortex-A53x4
* FVP_Base_Cortex-A76x4

### Set up the environment

The [Arm reference software](https://gitlab.arm.com/arm-reference-solutions/arm-reference-solutions-docs/-/blob/master/docs/aemfvp-a/user-guide.rst) stack is the codebase. Follow the [Armv-A Base AEM FVP Platform Software User Guide](https://gitlab.arm.com/arm-reference-solutions/arm-reference-solutions-docs/-/blob/master/docs/aemfvp-a/user-guide.rst) to set up the environment, download the software stack, and get the toolchain.

he FVP_Base_Cortex-\<xxx> FVP is available for you to build and run Linux host environments. Contact Arm Support [support@arm.com](mailto:support@arm.com) to request access.

This document supports running the software stack on the following FVPs:

* FVP_Base_Cortex-A510x4
* FVP_Base_Cortex-A510x4+Cortex-A710x4
* FVP_Base_Cortex-A53x4
* FVP_Base_Cortex-A55x4
* FVP_Base_Cortex-A55x4+Cortex-A75x4
* FVP_Base_Cortex-A55x4+Cortex-A78x4
* FVP_Base_Cortex-A57x2-A35x4
* FVP_Base_Cortex-A57x2-A53x4
* FVP_Base_Cortex-A57x4
* FVP_Base_Cortex-A57x4-A35x4
* FVP_Base_Cortex-A57x4-A53x4
* FVP_Base_Cortex-A65AEx4
* FVP_Base_Cortex-A65AEx4+Cortex-A76AEx4
* FVP_Base_Cortex-A65x4
* FVP_Base_Cortex-A710x4
* FVP_Base_Cortex-A72x2-A53x4
* FVP_Base_Cortex-A72x4
* FVP_Base_Cortex-A72x4-A53x4
* FVP_Base_Cortex-A73x2-A53x4
* FVP_Base_Cortex-A73x4
* FVP_Base_Cortex-A73x4-A53x4
* FVP_Base_Cortex-A75x4
* FVP_Base_Cortex-A76AEx4
* FVP_Base_Cortex-A76x4
* FVP_Base_Cortex-A77x4
* FVP_Base_Cortex-A78AEx4
* FVP_Base_Cortex-A78Cx4
* FVP_Base_Cortex-A78x4
* FVP_Base_Cortex-X1Cx4
* FVP_Base_Cortex-X1x4
* FVP_Base_Cortex-X2x4
* FVP_Base_Neoverse-E1x4
* FVP_Base_Neoverse-N1x4

However, this is not a full list. This blog might apply to more FVP platforms, but no test is done for these platforms, for example:

* FVP_Base_Cortex-A55x1
* FVP_Base_Cortex-A55x2
* FVP_Base_Cortex-A55x1+Cortex-A75x1
* FVP_Base_Cortex-A55x4+Cortex-A76x2
---
title: Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Hardware Overview - NXP's FRDM i.MX 93 Board

Selecting the best hardware for machine learning (ML) models depends on effective tools. You can visualize ML performance early in the development cycle by using NXP's [FRDM i.MX 93](https://www.nxp.com/design/design-center/development-boards-and-designs/frdm-i-mx-93-development-board:FRDM-IMX93) board.

<center>
<iframe src='//players.brightcove.net/4089003392001/Sk5u9ln3l_default/index.html?videoId=6366294691112' allowfullscreen frameborder=0 width="800" height="400"></iframe>

*Unboxing NXP's FRDM i.MX 93 board*
</center>

![NXP FRDM i.MX 93 Board SoC Highlighted alt-text#center](./nxp-frdm-imx-93-board-soc-highlighted.png "Arm Ethos-U65 NPU location")

### NXP's FRDM i.MX 93 Processor Decoded

![i.MX 93 Processor SoC alt-text#center](./imx-93-application-processor-soc.png "NXP's FRDM i.MX 93 processor")

**NXP's Processor Labeling Convention:**
|Line|Meaning|
|----|-------|
|MIMX9352|• MI – Microcontroller IC<br>• MX93 – i.MX 93 family<br>• 52 – Variant:<br>• Dual-core Arm Cortex-A55<br> • Single Cortex-M33<br>• Includes **Ethos-U65 NPU**|
|CVVXMAB|• C - Commercial temperature grade (0°C to 95°C)<br>• VVX - Indicates package type and pinout (BGA, pitch, etc.)<br>• MAB - Specific configuration (e.g., NPU present, security level, memory interfaces)
|
|1P87F|• Silicon mask set identifier|
|SBBM2410E|• NXP traceability code|

## Software Overview - NXP's MCUXpresso IDE

NXP generously provides free software for working with their boards, the [MCUXpresso Integrated Development Environment (IDE)](https://www.nxp.com/design/design-center/software/development-software/mcuxpresso-software-and-tools-/mcuxpresso-integrated-development-environment-ide:MCUXpresso-IDE). In this learning path, you will instead use [MCUXpresso for Visual Studio Code](https://www.nxp.com/design/design-center/software/development-software/mcuxpresso-software-and-tools-/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC).

## Software Overview - Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com/) is a free integrated development environment provided by Microsoft. It is platform independent, full featured, and accomodating of many engineering frameworks. You will use Visual Studio Code to both configure NXP's software and connect to NXP's hardware.

## Software Overview - TinyML.

This Learning Path uses TinyML. TinyML is machine learning tailored to function on devices with limited resources, constrained memory, low power, and fewer processing capabilities.

For a learning path focused on creating and deploying your own TinyML models, please see [Introduction to TinyML on Arm using PyTorch and ExecuTorch](/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/)

## Benefits and applications

NPUs, like Arm's [Ethos-U65](https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u65) NPU are available on physical devices specifically made for developers. Development boards like NXP's [FRDM i.MX 93](https://www.nxp.com/design/design-center/development-boards-and-designs/frdm-i-mx-93-development-board:FRDM-IMX93) also connect to displays via a HDMI cable. Additionally the board accepts video inputs. This is useful for for ML performance visualization due to:
- visual confirmation that your ML model is running on the physical device
- image and video inputs for computer vision models running on the device
- clearly indicated instruction counts
- confirmation of total execution time and
- visually appealing output for prototypes and demos

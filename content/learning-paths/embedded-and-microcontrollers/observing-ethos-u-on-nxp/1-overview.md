---
title: Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This Learning Path assumes your FRDM i.MX 93 board is already set up and you can transfer files between your host machine and the board.

If you still need to set up Linux, serial console access, and file transfer, follow the Learning Path [Linux on an NXP FRDM i.MX 93 board](/learning-paths/embedded-and-microcontrollers/linux-nxp-board/) before continuing.

ExecuTorch is designed to scale from servers to endpoints, and Arm systems often scale within a *single device*.
The FRDM i.MX 93 platform combines:

- An application processor running Linux (Cortex-A) that handles system services and orchestration
- A Cortex-M33 microcontroller core that runs real-time firmware
- An Ethos-U65 NPU that accelerates TinyML inference

This Learning Path focuses on a concrete milestone: successful bring-up of an ExecuTorch `executor_runner` firmware on Cortex-M33 on this NXP platform.

You keep the Linux side intentionally simple. Linux loads and starts the Cortex-M33 firmware through RemoteProc, and you stage a compiled ExecuTorch `.pte` model so the firmware can run it.

## What you’ll build and validate

By the end of this Learning Path, you have:

- A `.pte` model artifact compiled for `ethos-u65-256`
- A Cortex-M33 `executor_runner` firmware image built against prebuilt ExecuTorch libraries
- A repeatable deployment flow that loads the firmware, runs inference, and reports results through the remoteproc trace buffer

## What you need before you continue

After you complete the Linux setup Learning Path, you should have:

- A way to log in to the board (serial console and/or SSH)
- A way to transfer files (for example, `scp`)

## NXP's MCUXpresso IDE

NXP provides free software for working with their boards, the [MCUXpresso Integrated Development Environment (IDE)](https://www.nxp.com/design/design-center/software/development-software/mcuxpresso-software-and-tools-/mcuxpresso-integrated-development-environment-ide:MCUXpresso-IDE). In this Learning Path, you use [MCUXpresso for Visual Studio Code](https://www.nxp.com/design/design-center/software/development-software/mcuxpresso-software-and-tools-/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC).

MCUXpresso matters here because it gives you a predictable way to build and manage Cortex-M firmware on a platform where Linux is running at the same time.

## TinyML

This Learning Path uses TinyML. TinyML is machine learning tailored to function on devices with limited resources, constrained memory, low power, and fewer processing capabilities.

For a Learning Path focused on creating and deploying your own TinyML models, see [Introduction to TinyML on Arm using PyTorch and ExecuTorch](/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/)

In this Learning Path, you focus on deployment and observation: building the two runtime artifacts (the `.pte` model and the `executor_runner` firmware), bringing them up on the board, and confirming the Ethos-U acceleration path is active.

The next section covers booting the FRDM i.MX 93 and establishing a console connection so you can log in and transfer files.

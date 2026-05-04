---
additional_search_terms:
- SVE
- Neoverse
- cloud
- hpc

layout: installtoolsall
minutes_to_complete: 10
author: Jason Andrews
multi_install: false
multitool_install_part: false
official_docs: https://developer.arm.com/documentation/102190
test_images:
- ubuntu:latest
test_maintenance: true
description: Install Arm Instruction Emulator (armie) on Arm Linux (aarch64) to emulate Scalable Vector Extension (SVE) on hardware that doesn't support SVE.
title: Arm Instruction Emulator (armie)
tool_install: true
weight: 1
---
[Arm Instruction Emulator](https://developer.arm.com/Tools%20and%20Software/Arm%20Instruction%20Emulator) is a software tool that runs on 64-bit Arm platforms and emulates [Scalable Vector Extension (SVE)](https://developer.arm.com/documentation/102476/latest/instructions). This tool allows you to run your compiled SVE application binaries on hardware that is not SVE-enabled. It does not require a license.

{{% notice SVE hardware %}}
AWS Graviton 3 and Graviton 4 processors are available and recommended for SVE application development.
{{% /notice %}}

Arm Instruction Emulator runs as an executable on your Linux host. It runs on Red Hat Enterprise Linux (RHEL), SUSE Linux Enterprise Server (SLES), and Ubuntu Linux distributions. 

In this guide, you'll learn how to install Arm Instruction Emulator. 

## Before you begin

Confirm you are using an Arm machine by running:

```bash
uname -m
```
The output should be:
```output
aarch64
```
If you see a different result, you are not using an Arm computer running 64-bit Linux.

You must also ensure that either [Environment Modules](https://modules.readthedocs.io/en/latest/index.html) or the [Lmod Environment Module System](https://lmod.readthedocs.io/en/latest/) are installed on your Linux machine. The GNU Compiler (GCC) is also required.

For Ubuntu Linux, install the following required packages.

```bash
sudo apt-get install build-essential -y
sudo apt-get install environment-modules -y
```

## Download Arm Instruction Emulator

For Ubuntu Linux, download the installer package from [Arm Instruction Emulator downloads](https://developer.arm.com/downloads/-/arm-instruction-emulator).


## Install Arm Instruction Emulator

To install the Arm Instruction Emulator, extract the downloaded package and run the install script.

Extract the downloaded package:

```console
tar -xvzf ARMIE-BN-UBUNT-r25p0-00rel0.tgz
```

Run the install script:

```console
sudo ./arm-instruction-emulator_25.0_Ubuntu-22.04/arm-instruction-emulator_25.0_Ubuntu-22.04.sh -a
```

Set up the environment, for example, in your `.bashrc` and add module files:

```bash
echo "source /usr/share/modules/init/bash" >> ~/.bashrc
echo "module use /opt/arm/modulefiles" >> ~/.bashrc
source ~/.bashrc
```

List available modules:

```console
module avail
```

Configure Arm Compiler for Linux:

```console
module load armie22/22.0
```

To confirm `armie` is installed, print the version:

```console
armie --version
```

## Get started with Arm Instruction Emulator

To verify everything is working after installation, see [Get started with Arm Instruction Emulator](https://developer.arm.com/documentation/102190/latest/Get-started/Get-started-with-Arm-Instruction-Emulator) for instructions on how to compile and run examples with `armie`. The examples demonstrate how to compile Scalable Vector Extension (SVE) code and run the resulting binary with Arm Instruction Emulator.

You are now ready to use the Arm Instruction Emulator.

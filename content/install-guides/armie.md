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
title: Arm Instruction Emulator (armie)
tool_install: true
weight: 1
---
[Arm Instruction Emulator](https://developer.arm.com/Tools%20and%20Software/Arm%20Instruction%20Emulator) is a software tool that runs on 64-bit Arm platforms and emulates [Scalable Vector Extension(SVE)](https://developer.arm.com/documentation/102476/latest/instructions). This tool allows you to run your compiled SVE application binaries on hardware that is not SVE-enabled.

{{% notice SVE hardware %}}
AWS Graviton 3 and Graviton 4 processors are available and recommended for SVE application development.
{{% /notice %}}

## Before you begin

Arm Instruction Emulator is an executable that runs on your Linux host. It runs on Red Hat Enterprise Linux (RHEL), SUSE Linux Enterprise Server (SLES), and Ubuntu Linux distributions.

Confirm you are using an Arm machine by running:

```bash
uname -m
```
The output should be:
```output
aarch64
```
If you see a different result, you are not using an Arm computer running 64-bit Linux.

You must ensure that either [Environment Modules](https://modules.readthedocs.io/en/latest/index.html) or the [Lmod Environment Module System](https://lmod.readthedocs.io/en/latest/) are installed on your Linux machine. The GNU Compiler (GCC) is also required.

For Ubuntu Linux install the required packages.

```bash
sudo apt-get install build-essential -y
sudo apt-get install environment-modules -y
```

## Download

You can download the appropriate Arm Instruction Emulator package for your host Linux platform from [Product Downloads section](https://developer.arm.com/downloads/-/arm-instruction-emulator) of the Arm website.

For Ubuntu Linux download the installer package using `wget`

```bash
wget https://developer.arm.com/-/media/Files/downloads/hpc/arm-instruction-emulator/22-0/ARM-Instruction-Emulator_22.0_AArch64_Ubuntu_18.04.tar.gz
```

## Install

To install the Arm Instruction Emulator, extract the downloaded package and run the install script.

Extract the downloaded package.

```bash
tar -xf ARM-Instruction-Emulator_22.0_AArch64_Ubuntu_18.04.tar.gz
```

Run the install script.

```bash
sudo ./arm-instruction-emulator_22.0_Ubuntu-18.04/arm-instruction-emulator_22.0_Ubuntu-18.04.sh -a
```

Set up the environment for example in your .bashrc and add module files.

```bash
echo "source /usr/share/modules/init/bash" >> ~/.bashrc
echo "module use /opt/arm/modulefiles" >> ~/.bashrc
source ~/.bashrc
```

To list available modules:

```console
module avail
```

To configure Arm Compiler for Linux:

```console
module load armie22/22.0
```

To confirm `armie` is installed, print the version.

```console
armie --version
```

## Setting up product license

Arm Instruction Emulator does not require a license.

## Get started

To verify everything is working after installation refer to [Get started with Arm Instruction Emulator](https://developer.arm.com/documentation/102190/latest/Get-started/Get-started-with-Arm-Instruction-Emulator) for instructions on how to compile and run examples with `armie`.

This uses a couple of simple examples to demonstrate how to compile Scalable Vector Extension (SVE) code and run the resulting binary with Arm Instruction Emulator.

You are ready to use the Arm Instruction Emulator.

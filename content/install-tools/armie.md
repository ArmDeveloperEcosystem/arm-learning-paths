---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Arm Instruction Emulator

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- SVE
- Neoverse

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 10

### Link to official documentation
official_docs: https://developer.arm.com/documentation/102190

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---
[Arm Instruction Emulator](https://developer.arm.com/Tools%20and%20Software/Arm%20Instruction%20Emulator) is a software tool that runs on 64-bit Arm platforms and emulates [Scalable Vector Extension(SVE)](https://developer.arm.com/documentation/102476/latest/instructions). This tool allows you to run your compiled SVE application binaries on hardware that is not SVE-enabled.

## Prerequisites

Arm Instruction Emulator is an executable that runs on your Linux host. It runs on RHEL, SLES, and Ubuntu Linux distributions.

You must ensure that either [Environment Modules](https://modules.readthedocs.io/en/latest/index.html) or the [Lmod Environment Module System](https://lmod.readthedocs.io/en/latest/) are installed on your host Linux machine.

On the supported Linux hosts, use `gcc 7.1.0` or higher

## Download installer packages

You can download the appropriate Arm Instruction emulator package for your host Linux platform from [Product Downloads section](https://developer.arm.com/downloads/-/arm-instruction-emulator) of the Arm website. 

Full installation instructions are provided [here](https://developer.arm.com/documentation/102190/latest/Get-started/Install-Arm-Instruction-Emulator).

## Setting up product license

Arm Instruction Emulator is freely available and not license managed. You can view the third party license information for the open source software included with the latest version of Arm Instruction Emulator [here](https://developer.arm.com/downloads/-/arm-instruction-emulator/third-party-licenses)

## Get started {#start}

To verify everything is working OK post-install refer to [Get started with Arm Instruction Emulator](https://developer.arm.com/documentation/102190/latest/Get-started/Get-started-with-Arm-Instruction-Emulator).

This uses a couple of simple examples to demonstrate how to compile Scalable Vector Extension (SVE) code and run the resulting binary with Arm Instruction Emulator.

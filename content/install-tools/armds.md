---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Arm Development Studio

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- compiler
- ArmDS

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 10

### Link to official documentation
official_docs: https://developer.arm.com/documentation/101469

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---
[Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio) is the most comprehensive embedded C/C++ dedicated software development solution. It is used for validation of SoC debug through emulation, simulation, FPGA, and silicon bring-up design and verification stages. It has the earliest support for all Arm CPUs and interconnects.

## Prerequisites

Arm Development Studio can be installed on Windows and Linux hosts.

Full host platform requirements are given in the [Getting Started Guide](https://developer.arm.com/documentation/101469/latest/Installing-and-configuring-Arm-Development-Studio/Hardware-and-host-platform-requirements).

## Download installer packages

The installer will depend on the [edition](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio#Editions) of Development Studio that you are entitled to. 

Gold, Silver, and Bronze editions are one installer, with available features defined by the license. The version is denoted by `year.index`, where `index` is a number (for example `2022.2`). You can also generate an Evaluation license from this installation (`Help` > `Arm License Manager`), with capabilities broadly similar to the Gold Edition.

Development Studio Platinum Edition has its own installation package. The version is denoted by `year.index`, where `index` is a letter (for example `2022.c`).

You can download the Development Studio installer from the [Product Download Hub](https://developer.arm.com/downloads). For more information on the Download Hub, see [here](../pdh).

## Install Arm Development Studio

For Windows hosts, follow the installation instructions provided [here](https://developer.arm.com/documentation/101469/latest/Installing-and-configuring-Arm-Development-Studio/Installing-on-Windows).

For Linux hosts, follow the installation instructions provided [here](https://developer.arm.com/documentation/101469/latest/Installing-and-configuring-Arm-Development-Studio/Installing-on-Linux). Note also [additional Linux libraries](https://developer.arm.com/documentation/101469/latest/Installing-and-configuring-Arm-Development-Studio/Additional-Linux-libraries) are required.

## Setting up license

Arm Development Studio is license managed. License setup instructions are available [here](../license/).

When you launch the IDE for the first time, you may be prompted to select the Development Studio Edition in `Help` > `Arm License Manager`.

A free 30 day evaluation license for Arm Development Studio is also available. You can generate this in `Help` > `Arm License Manager`. Click on `Add`, and follow instructions therein to obtain the evaluation license (requires Arm login).

## Verify installation

To verify everything is installed correctly and to get started with your first project, follow the [Hello World Tutorial](https://developer.arm.com/documentation/101469/latest/Tutorials/Tutorial--Hello-World).

A number of [example projects](https://developer.arm.com/documentation/101469/latest/Projects-and-examples-in-Arm-Development-Studio/Examples-provided-with-Arm-Development-Studio) are also provided.

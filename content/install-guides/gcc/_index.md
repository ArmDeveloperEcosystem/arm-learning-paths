---
title: GNU Compiler
author_primary: Jason Andrews
additional_search_terms:
- compiler
- gcc
- linux

### FIXED, DO NOT MODIFY
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: true             # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

## What should I consider to determine the correct GCC flavor?

There are multiple flavors of [GCC, the GNU Compiler Collection](https://gcc.gnu.org/), for the Arm architecture, and for different use cases. To determine which flavor you need, consider the variables below:

- Target environment where you want the compiled software to run: bare metal or real time operating system (RTOS), Linux kernel and applications, Android applications, or Windows applications.

- Host machine, where you will do the compiling: Windows, Linux, or macOS

- Architecture of the host machine: x86 or Arm

This section provides installation instructions for GCC targeting the Arm architecture. Navigate to the section of interest.

## How do I use GCC as a native compiler on Arm Linux?
Use this option to install GCC using the Linux package manager and build applications on an Arm Linux system. 

## How do I use GCC as a cross-compiler on Arm Linux?
Use this option to install GCC using the Linux package manager and build bare metal applications by cross compiling them for the Arm architecture from an x86 or Arm Linux host machine. Also, use this option to install and compile Linux applications from an x86 host for an Arm target. 

## How do I use GCC from the Arm GNU Toolchain?
Use this option to download an install a version of GCC produced by Arm. It is available from the Arm Developer website and works on Linux, Windows, and macOS host machines. It supports bare-metal and Linux targets. 

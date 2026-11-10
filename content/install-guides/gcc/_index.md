---
title: GNU Compiler
description: Choose and install the right GCC toolchain for native Arm Linux development, Arm Linux cross-compilation, or bare-metal Arm targets.
author: Jason Andrews
additional_search_terms:
- compiler
- GCC
- linux
- arm-none-eabi
- embedded
- cross-compiler
- Cortex-M
- Cortex-R
- Cortex-A
- microcontroller

# Navigation buttons in the sections replace the automatic install guide cards.
hide_install_guide_cards: true

### FIXED, DO NOT MODIFY
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: true             # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

The GNU Compiler Collection (GCC) is available in several toolchains for Arm. Each supports a specific combination of host machine, target architecture, and runtime environment.

## Select your toolchain

Choose a toolchain based on where your software runs and where you compile it:

<div class="gcc-toolchain-table">

| Choose this toolchain | When to use it |
|-----------------------|----------------|
| Arm GNU Toolchain | You build bare-metal software or software that uses a real-time operating system (RTOS) |
| Linux cross-compiler | You build on Linux for a different target architecture |
| Native compiler | You build and run software on the same Arm Linux machine |

</div>

### Arm GNU Toolchain

Use the Arm GNU Toolchain to build firmware, an RTOS, or bare-metal software for Cortex-M, Cortex-R, and Cortex-A processors.

This is the right option for most embedded developers. The toolchain is maintained by Arm and released through the Arm GNU Toolchain GitLab repository.

The Arm GNU Toolchain provides pre-built binaries for Windows, Linux, and macOS.

For Cortex-A and Cortex-R, check your board or RTOS documentation to determine whether your project uses 32-bit or 64-bit software. Choose the compiler that matches your software target:

<div class="gcc-toolchain-table">

| Compiler | Target |
|----------|--------|
| `arm-none-eabi-gcc` | Cortex-M software |
| `arm-none-eabi-gcc` | 32-bit software for supported Cortex-R and Cortex-A processors (AArch32) |
| `aarch64-none-elf-gcc` | 64-bit software for supported Cortex-R and Cortex-A processors (AArch64) |

</div>

<a class="c-button is-primary" href="{{< relref "arm-gnu.md" >}}">Install Arm GNU Toolchain</a>

### Linux cross-compiler

Use a GCC cross-compiler to build Arm Linux applications for a different target architecture. The compiled applications run on Arm Linux systems, not bare-metal hardware.

You need a Linux host. Install the cross-compiler using your Linux package manager.

Examples include compiling from x86-64 to 64-bit Arm, or from 64-bit Arm to 32-bit Arm. Choose the compiler that matches your software target:

<div class="gcc-toolchain-table">

| Compiler | Target |
|----------|--------|
| `aarch64-linux-gnu-gcc` | 64-bit Arm Linux applications (AArch64) |
| `arm-linux-gnueabihf-gcc` | 32-bit Arm Linux applications (AArch32, hard float) |

</div>

<a class="c-button is-primary" href="{{< relref "cross.md" >}}">Install a Linux cross-compiler</a>

### Native compiler

Use GCC to build C and C++ applications directly on the Arm Linux machine where you run them.

You need an Arm Linux machine, such as a Neoverse server, Raspberry Pi, or another Arm development board. Install GCC using your Linux package manager.

<div class="gcc-toolchain-table">

| Compiler | Target |
|----------|--------|
| `gcc` | Arm Linux (native) |

</div>

<a class="c-button is-primary" href="{{< relref "native.md" >}}">Install GCC on Arm Linux</a>

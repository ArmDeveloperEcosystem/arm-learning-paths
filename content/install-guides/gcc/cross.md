---
additional_search_terms:
- compiler
layout: installtoolsall
minutes_to_complete: 15
author_primary: Jason Andrews
multi_install: false
multitool_install_part: true
official_docs: https://gcc.gnu.org/onlinedocs/
test_images:
- ubuntu:latest
- fedora:latest
test_link: https://github.com/armflorentlebeau/arm-learning-paths/actions/runs/4312122327
test_maintenance: true
test_status:
- passed
- passed
title: Cross-compiler
tool_install: false
weight: 3
---
GCC is available on all Linux distributions and can be installed using the package manager. 

This covers `gcc` and `g++` for compiling C and C++ as a cross-compiler targeting the Arm architecture.

## Introduction

GCC is often used to cross-compile software for Arm microcontrollers and embedded devices which have firmware and other low-level software. The executables are `arm-none-eabi-gcc` and `arm-none-eabi-g++`.

GCC is also used to cross compile Linux applications. Applications can be compiled for 32-bit or 64-bit Linux systems. 

The executables for 32-bit are `arm-linux-gnueabihf-gcc` and `arm-linux-gnueabihf-g++`. 

The executables for 64-bit are `aarch64-linux-gnu-gcc` and `aarch64-linux-gnu-g++`.

Software can be compiled on an `x86` or `Arm` host machine.

## Download 

The Linux package manager will download the required files so there are no special download instructions.

## Installation

### Installing on Debian based distributions such as Ubuntu

Use the `apt` command to install software packages on any Debian based Linux distribution.

```bash { target="ubuntu:latest" }
sudo apt update
sudo apt install gcc-arm-none-eabi -y
sudo apt install gcc-arm-linux-gnueabihf -y
sudo apt install gcc-aarch64-linux-gnu -y
```

### Installing on Red Hat / Fedora / Amazon Linux

These Linux distributions use `yum` as the package manager. 

To install the most common development tools use the commands below. If the machine has `sudo` you can use it or run `yum` as _root_.

```bash { target="fedora:latest" }
sudo yum update -y
sudo yum install arm-none-eabi-gcc-cs -y
sudo yum install arm-none-eabi-newlib -y
sudo yum install gcc-aarch64-linux-gnu -y
sudo yum install gcc-arm-linux-gnu -y
```

If `sudo` is not available become _root_ and omit the `sudo`.

```console
yum update
yum install arm-none-eabi-gcc-cs -y
yum install arm-none-eabi-newlib -y
yum install gcc-aarch64-linux-gnu -y
yum install gcc-arm-linux-gnu -y
```

## Setting up product license {#license}

GCC is open source and freely available for use. 

## Get started {#start}

To confirm the installation is successful, enter:

```bash
arm-none-eabi-gcc --version
```

To compile an example program, create a text file named hello-world.c with the contents below.

```C { file_name="hello-world-embedded.c" }
#include <stdio.h>

int main()
{
    printf("Hello, Arm World!\n");
    return 0;
}
```

To compile hello-world as a bare-metal application:

```bash
arm-none-eabi-gcc --specs=rdimon.specs hello-world-embedded.c -o hello-world.elf
```

To cross-compile hello-world as a 32-bit Linux application. On Fedora, only building kernels is currently supported. Support for cross-building user space programs is not currently provided as that would massively multiply the number of packages.

```bash { target="ubuntu:latest" }
arm-linux-gnueabihf-gcc  hello-world-embedded.c -o hello-world.elf
```

To cross-compile hello-world as a 64-bit Linux application. On Fedora, only building kernels is currently supported. Support for cross-building user space programs is not currently provided as that would massively multiply the number of packages.

```bash { target="ubuntu:latest" }
aarch64-linux-gnu-gcc hello-world-embedded.c -o hello-world.elf
```

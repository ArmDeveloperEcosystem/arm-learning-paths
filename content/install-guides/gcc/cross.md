---
additional_search_terms:
- compiler
layout: installtoolsall
minutes_to_complete: 15
author: Jason Andrews
multi_install: false
multitool_install_part: true
official_docs: https://gcc.gnu.org/onlinedocs/
test_images:
- ubuntu:latest
- fedora:latest
test_link: null
test_maintenance: true
title: Cross-compiler
tool_install: false
weight: 3
---
GCC is available on all Linux distributions and can be installed using the package manager.

This covers `gcc` and `g++` for compiling C and C++ as a cross-compiler targeting the Arm Linux architecture. For bare-metal and embedded targets such as `arm-none-eabi`, see the [Arm GNU Toolchain](../arm-gnu) install guide.

## Before you begin

GCC is used to cross-compile Linux applications targeting Arm. Applications can be compiled for 32-bit or 64-bit Arm Linux systems.

The executables for 32-bit are `arm-linux-gnueabihf-gcc` and `arm-linux-gnueabihf-g++`.

The executables for 64-bit are `aarch64-linux-gnu-gcc` and `aarch64-linux-gnu-g++`.

Software can be compiled on an `x86_64` or `Arm` host machine.

## How do I download a GCC cross compiler targeting Arm?

The Linux package manager downloads the required files. No manual download is needed.

## How do I install a GCC cross compiler on Linux?

You can install a GCC cross compiler with Arm as a target architecture using Linux package managers.

### Installing on Debian based distributions such as Ubuntu

Use the `apt` command to install the cross-compilers for 32-bit and 64-bit Arm Linux targets.

```bash { target="ubuntu:latest" }
sudo apt update
sudo apt install gcc-arm-linux-gnueabihf -y
sudo apt install gcc-aarch64-linux-gnu -y
```

The GCC version installed is tied to your Ubuntu release. For example, Ubuntu 24.04 LTS provides GCC 13 and Ubuntu 25.10 provides GCC 15. This is normal Ubuntu packaging behaviour.

### Installing on Fedora

Fedora uses the `dnf` package manager.

- If the machine has `sudo` you can use it:

  ```bash { target="fedora:latest" }
  sudo dnf update -y
  sudo dnf install gcc-aarch64-linux-gnu -y
  sudo dnf install gcc-arm-linux-gnu -y
  ```

- If `sudo` is not available become _root_ and omit the `sudo` from the above commands:

  ```console
  dnf update -y
  dnf install gcc-aarch64-linux-gnu -y
  dnf install gcc-arm-linux-gnu -y
  ```

On Fedora, only building kernels is currently supported. Support for cross-building user space programs is not currently provided, as that would massively multiply the number of packages.

## Setting up product license {#license}

GCC is open source and freely available for use.

## Get started {#start}

To confirm the installations are successful, enter:

```bash { target="ubuntu:latest" }
aarch64-linux-gnu-gcc --version
arm-linux-gnueabihf-gcc --version
```

To cross-compile an example program, create a text file named `hello-world.c` with the contents below.

```C { file_name="hello-world.c" }
#include <stdio.h>

int main()
{
    printf("Hello, Arm World!\n");
    return 0;
}
```

To cross-compile for a 64-bit Arm Linux target. On Fedora, only building kernels is currently supported, so these examples apply to Ubuntu.

```bash { target="ubuntu:latest" }
aarch64-linux-gnu-gcc hello-world.c -o hello-world-aarch64.elf
```

To cross-compile for a 32-bit Arm Linux target:

```bash { target="ubuntu:latest" }
arm-linux-gnueabihf-gcc hello-world.c -o hello-world-arm.elf
```

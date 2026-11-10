---
title: Cross-compiler
description: Install GCC cross-compilers on Linux to build 32-bit or 64-bit Arm Linux applications from an x86 or Arm host.

author: Jason Andrews
minutes_to_complete: 10
official_docs: https://gcc.gnu.org/onlinedocs/

test_maintenance: false
test_images:
- ubuntu:latest

layout: installtoolsall
multi_install: false
multitool_install_part: true
tool_install: false
weight: 3

additional_search_terms:
- compiler
- cross-compiler
- aarch64-linux-gnu
- arm-linux-gnueabihf
---

Install GCC cross-compilers on an x86-64 or Arm Linux host running Ubuntu or Debian to build applications for Arm Linux systems.

{{% notice Note %}}
For bare-metal software or software that uses a real-time operating system (RTOS), use the [Arm GNU Toolchain](../arm-gnu) instead. It supports firmware development for Cortex-M, Cortex-R, and Cortex-A processors. Linux cross-compilers target applications that run on Arm Linux.
{{% /notice %}}

## Install cross-compilers

On Ubuntu or Debian, install the C and C++ cross-compilers for 32-bit and 64-bit Arm Linux:

```bash
sudo apt update
sudo apt install gcc gcc-aarch64-linux-gnu g++-aarch64-linux-gnu \
    gcc-arm-linux-gnueabihf g++-arm-linux-gnueabihf -y
```

The `gcc` package installs the native C compiler and its assembler and linker dependencies, which are also needed when building 64-bit Arm applications on a 64-bit Arm host.

| Compiler | Target |
|----------|--------|
| `aarch64-linux-gnu-gcc` | 64-bit Arm Linux applications (AArch64) |
| `arm-linux-gnueabihf-gcc` | 32-bit Arm Linux applications (AArch32, hard float) |

The corresponding C++ compilers are `aarch64-linux-gnu-g++` and `arm-linux-gnueabihf-g++`.

## Verify the installation

Verify the 64-bit cross-compiler is installed:

```bash
aarch64-linux-gnu-gcc --version
```

The output is similar to:

```output
aarch64-linux-gnu-gcc (Ubuntu 15.2.0-16ubuntu1) 15.2.0
Copyright (C) 2025 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

Verify the 32-bit cross-compiler is installed:

```bash
arm-linux-gnueabihf-gcc --version
```

The output is similar to:

```output
arm-linux-gnueabihf-gcc (Ubuntu 15.2.0-16ubuntu1) 15.2.0
Copyright (C) 2025 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

## Cross-compile a program

Create a file named `hello.c`:

```C { file_name="hello.c" }
#include <stdio.h>

int main()
{
    printf("Hello, Arm World!\n");
    return 0;
}
```

Cross-compile for 64-bit Arm Linux:

```bash
aarch64-linux-gnu-gcc hello.c -o hello-arm64
```

Cross-compile for 32-bit Arm Linux:

```bash
arm-linux-gnueabihf-gcc hello.c -o hello-arm32
```

## Test with QEMU (optional)

QEMU user-mode emulation lets you run the compiled Arm Linux applications on your host. You don't need QEMU to cross-compile.

On Ubuntu or Debian, install QEMU:

```bash
sudo apt install qemu-user -y
```

The `-L` option points QEMU to the target's runtime libraries.

Test the 64-bit binary with QEMU:

```bash
qemu-aarch64 -L /usr/aarch64-linux-gnu ./hello-arm64
```

The output is similar to:

```output
Hello, Arm World!
```

Test the 32-bit binary with QEMU:

```bash
qemu-arm -L /usr/arm-linux-gnueabihf ./hello-arm32
```

The output is similar to:

```output
Hello, Arm World!
```

You can now cross-compile C and C++ applications for Arm Linux from your Linux host.

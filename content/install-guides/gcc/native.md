---
title: Native compiler
description: Install GCC and G++ on Arm Linux to compile C and C++ applications directly on your Arm system.

author: Jason Andrews
minutes_to_complete: 10
official_docs: https://gcc.gnu.org/onlinedocs/
ecosystem_dashboard: https://developer.arm.com/ecosystem-dashboard/linux?package=GNU%20Toolchain%20%28GCC%29

test_maintenance: false
test_images:
- ubuntu:latest

layout: installtoolsall
multi_install: false
multitool_install_part: true
tool_install: false
weight: 4

additional_search_terms:
- compiler
- native
- aarch64
- Arm Linux
---

Install GCC and G++ on your Arm Linux machine to build and run C and C++ applications.

## Confirm you are on Arm Linux

Before installing, verify you're running on an Arm system:

```bash
uname -m
```

The expected output is:

```output
aarch64
```

If you see `x86_64` instead, you need a [cross-compiler](../cross), not a native compiler.

## Install GCC

Install GCC and G++ using the commands for your Linux distribution:

{{< tabpane code=true >}}
  {{< tab header="Ubuntu / Debian" language="bash" >}}
sudo apt update
sudo apt install build-essential -y
  {{< /tab >}}
  {{< tab header="Fedora / RHEL / Amazon Linux" language="bash" >}}
sudo dnf install gcc gcc-c++ -y
  {{< /tab >}}
{{< /tabpane >}}

On Ubuntu and Debian, `build-essential` also installs `make` and other common build tools. On Fedora, RHEL, and Amazon Linux, the `gcc-c++` package provides G++. The GCC version depends on your distribution release.

## Verify the installation

Verify GCC is installed:

```bash
gcc --version
```

The output is similar to:

```output
gcc (Ubuntu 15.2.0-16ubuntu1) 15.2.0
Copyright (C) 2025 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

Verify G++ is also installed:

```bash
g++ --version
```

The output is similar to:

```output
g++ (Ubuntu 15.2.0-16ubuntu1) 15.2.0
Copyright (C) 2025 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

## Compile and run a program

Create a file named `hello.c`:

```C { file_name="hello.c" }
#include <stdio.h>

int main()
{
    printf("Hello, Arm World!\n");
    return 0;
}
```

Compile `hello.c` with GCC, then run the resulting `hello` executable:

```bash
gcc -o hello hello.c
./hello
```

The expected output is:

```output
Hello, Arm World!
```

You can now compile C and C++ applications on your Arm Linux machine.


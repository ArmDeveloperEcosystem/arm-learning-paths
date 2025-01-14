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
test_link: null
test_maintenance: true
test_status:
- passed
- passed
title: Native compiler
tool_install: false
weight: 2
---
GCC is available on all Linux distributions and can be installed using the package manager.

## Before you begin

Follow the instructions below to install GCC on an Arm Linux distribution. This covers `gcc` and `g++` for compiling C and C++ applications.

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The output should be:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

## How do I download a native GCC compiler on Linux?

The Linux package manager downloads the required files so there are no special instructions.

## How do I install a native GCC compiler on Linux?

### Installing on Debian based distributions such as Ubuntu

Use the `apt` command to install software packages on any Debian based Linux distribution, including Ubuntu.

```bash { target="ubuntu:latest" }
sudo apt update
sudo apt install gcc g++ -y
```

Another meta-package on Ubuntu is ``build-essential``. This will install the most common tools and libraries with a single command.

```bash { target="ubuntu:latest" }
sudo apt install build-essential -y
```

### Installing on Red Hat / Fedora / Amazon Linux

These Linux distributions use `dnf` as the package manager.

To install the most common development tools use the commands below. If the machine has `sudo` you can use it.

```bash { target="fedora:latest" }
sudo dnf update -y
sudo dnf groupinstall 'Development Tools' -y
```
If `sudo` is not available become _root_ and omit the `sudo`.
```console
dnf update -y
dnf groupinstall 'Development Tools' -y
```
## Setting up product license

GCC is open source and freely available for use. 

## Get started {#start}

To confirm the installation is complete run:

```bash
gcc --version
```

To compile an example program, create a text file named hello-world.c with the contents below.

```C { file_name="hello-world.c" }
#include <stdio.h>

int main()
{
    printf("Hello, Arm World!\n");
    return 0;
}
```
To compile and run the application use:
```bash
gcc -o hello-world hello-world.c
./hello-world
```
Observe the output:
```output
Hello, Arm World!
```

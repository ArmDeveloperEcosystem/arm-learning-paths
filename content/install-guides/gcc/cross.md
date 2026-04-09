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

This covers `gcc` and `g++` for compiling C and C++ as a cross-compiler targeting the Arm architecture.

## Before you begin

GCC is often used to cross-compile software for Arm microcontrollers and embedded devices which have firmware and other low-level software. The executables are `arm-none-eabi-gcc` and `arm-none-eabi-g++`.

GCC is also used to cross compile Linux applications. Applications can be compiled for 32-bit or 64-bit Linux systems.

The executables for 32-bit are `arm-linux-gnueabihf-gcc` and `arm-linux-gnueabihf-g++`.

The executables for 64-bit are `aarch64-linux-gnu-gcc` and `aarch64-linux-gnu-g++`.

Software can be compiled on an `x86` or `Arm` host machine.

## How do I download a GCC cross compiler targeting Arm?

For the Linux cross-compilers targeting 32-bit and 64-bit Linux applications (`arm-linux-gnueabihf` and `aarch64-linux-gnu`), the Linux package manager downloads the required files.

For the bare-metal cross-compiler (`arm-none-eabi`), Arm no longer publishes new releases through Debian or Ubuntu package repositories. To get the latest version, download it directly from the [Arm GNU Toolchain downloads page](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads).

## How do I install a GCC cross compiler on Linux?

You can install a GCC cross compiler with Arm as a target architecture using Linux package managers.

### Installing on Debian based distributions such as Ubuntu

Use the `apt` command to install the cross-compilers for 32-bit and 64-bit Linux targets.

```bash { target="ubuntu:latest" }
sudo apt update
sudo apt install gcc-arm-linux-gnueabihf -y
sudo apt install gcc-aarch64-linux-gnu -y
```

These packages are maintained by Canonical and the GCC version you receive is tied to your Ubuntu release (for example, GCC 13 on Ubuntu 24.04 LTS, GCC 15 on Ubuntu 25.10). This is normal Ubuntu packaging behaviour and is not the same issue as with `arm-none-eabi`.

For the bare-metal cross-compiler (`arm-none-eabi`), Arm no longer publishes new releases to Debian or Ubuntu package repositories. The version available through `apt` is older and may not include support for recent Arm cores or architecture features.

To install the latest `arm-none-eabi` toolchain (15.2.Rel1), download the pre-built tarball for your host architecture from the [Arm GNU Toolchain downloads page](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads). Extract the archive and add the `bin` directory to your `PATH`.

On an `aarch64` host:

```bash
wget https://developer.arm.com/-/media/Files/downloads/gnu/15.2.rel1/binrel/arm-gnu-toolchain-15.2.rel1-aarch64-arm-none-eabi.tar.xz
tar -xJf arm-gnu-toolchain-15.2.rel1-aarch64-arm-none-eabi.tar.xz
export PATH="$HOME/arm-gnu-toolchain-15.2.rel1-aarch64-arm-none-eabi/bin:$PATH"
```

On an `x86_64` host:

```bash
wget https://developer.arm.com/-/media/Files/downloads/gnu/15.2.rel1/binrel/arm-gnu-toolchain-15.2.rel1-x86_64-arm-none-eabi.tar.xz
tar -xJf arm-gnu-toolchain-15.2.rel1-x86_64-arm-none-eabi.tar.xz
export PATH="$HOME/arm-gnu-toolchain-15.2.rel1-x86_64-arm-none-eabi/bin:$PATH"
```

The commands above extract the toolchain into the current directory. Move the folder to a permanent location such as `$HOME` first if you'd like a stable install path.

To make the change permanent, add the `export` line to your shell profile such as `~/.bashrc` or `~/.profile`.

### Installing on Fedora

Fedora uses the `dnf` package manager. The `arm-none-eabi-gcc-cs` package in current Fedora releases (42 and later) tracks the latest GCC release closely.

If you're on RHEL, CentOS, or another EPEL-based distribution, the available version may be older. In that case, download the latest toolchain directly from the [Arm GNU Toolchain downloads page](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads) and follow the manual extraction steps described in the Ubuntu section above.

- If the machine has `sudo` you can use it:

  ```bash { target="fedora:latest" }
  sudo dnf update -y
  sudo dnf install arm-none-eabi-gcc-cs -y
  sudo dnf install arm-none-eabi-newlib -y
  sudo dnf install gcc-aarch64-linux-gnu -y
  sudo dnf install gcc-arm-linux-gnu -y
  ```

- If `sudo` is not available become _root_ and omit the `sudo` from the above commands:

  ```console
  dnf update -y
  dnf install arm-none-eabi-gcc-cs -y
  dnf install arm-none-eabi-newlib -y
  dnf install gcc-aarch64-linux-gnu -y
  dnf install gcc-arm-linux-gnu -y
  ```

## How do I install a GCC cross compiler on macOS?

You can install a GCC cross compiler with Arm as a target architecture using Homebrew, a package manager for macOS (and Linux). The Homebrew formula tracks the latest GCC release and provides pre-built bottles for Apple Silicon.

```console
brew install arm-none-eabi-gcc
```

Alternatively, Arm provides an official `.pkg` installer for macOS on Apple Silicon. Download the latest version from the [Arm GNU Toolchain downloads page](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads) and run it to install the toolchain to `/Applications/ArmGNUToolchain/`.

## Setting up product license {#license}

GCC is open source and freely available for use.

## Get started {#start}

To confirm the installation is successful, enter:

```bash
arm-none-eabi-gcc --version
```

To compile an example program, create a text file named `hello-world-embedded.c` with the contents below.

```C { file_name="hello-world-embedded.c" }
#include <stdio.h>

int main()
{
    printf("Hello, Arm World!\n");
    return 0;
}
```

To compile hello-world as a bare-metal application:

```bash { target="ubuntu:latest" }
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

---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: GCC

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- compiler

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

### Link to official documentation
official_docs:

### TEST SETTINGS
test_images:
- ubuntu:latest
- fedora:latest
test_link: https://github.com/armflorentlebeau/arm-software-developers-ads/actions/runs/3540052189
test_maintenance: true
test_status:
- passed
- passed

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

## GCC {#top}

There are multiple flavors of [GCC, the GNU Compiler Collection](https://gcc.gnu.org/), for the Arm architecture. To know which compiler you need consider the variables below. 

- Target environment where you want the compiled software to run: bare metal or real time operating system (RTOS), Linux kernel and applications, Android applications, or Windows applications.

- Host machine, where you will do the compiling: Windows, Linux, or macOS

- Architecture of the host machine: x86 or Arm

This section provides installation instructions for GCC targeting the Arm architecture.

Navigate to the section of interest.

- [GCC as a native compiler on Arm Linux](#native)   
Use this option to install GCC using the Linux package manager and build applications on an Arm Linux system. 

- [GCC as a cross-compiler](#cross)  
Use this option to install GCC using the Linux package manager and build bare metal applications by cross compiling them for the Arm architecture from an x86 or Arm Linux host machine. Also, use this option to install and compile Linux applications from an x86 host for an Arm target. 

- [GCC from the Arm GNU Toolchain](#Arm-GNU)  
Use this option to download an install a version of GCC produced by Arm. It is available from the Arm Developer website and works on Linux, Windows, and macOS host machines. It supports bare-metal and Linux targets. 

# GCC as a native compiler on Arm Linux {#native}

GCC is available on all Linux distributions and can be installed using the package manager.

## Introduction

Follow the instructions below to install GCC on an Arm Linux distribution. This covers gcc and g++ for compiling C and C++ applications.

Confirm you are using an Arm machine by running:

```bash { command_line="user@localhost | 2" }
uname -m
aarch64
```

## Download 

The Linux package manager downloads the required files so there are no special instructions.

## Installation

### Installing on Debian based distributions such as Ubuntu

Use the `apt` command to install software packages on any Debian based Linux distribution, including Ubuntu.

```bash { target="ubuntu:latest" }
sudo apt update
sudo apt install gcc g++ -y
```

Another meta-package on Ubuntu is ``build-essential``. This will install the most common tools libraries with a single command.

```bash { target="ubuntu:latest" }
sudo apt install build-essential -y
```

### Installing on Red Hat / Fedora / Amazon Linux

These Linux distributions use `yum` as the package manager. 

To install the most common development tools use the commands below. If the machine has `sudo` you can use it.

```bash { target="fedora:latest" }
sudo yum update -y
sudo yum groupinstall 'Development Tools' -y
```

If `sudo` is not available become _root_ and omit the `sudo`.

```console
yum update
yum groupinstall 'Development Tools' -y
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

To compile the hello-world program use:

```bash
gcc -o hello-world hello-world.c
```

To run the application enter:

```bash { command_line="user@localhost | 2" }
./hello-world
Hello, Arm World!
```

The program will print the string in the printf() statement.

[Return to the top](#top)

# Install GCC as a cross-compiler {#cross}

GCC is available on all Linux distributions and can be installed using the package manager. 

This covers gcc and g++ for compiling C and C++ as a cross-compiler targeting the Arm architecture.

## Introduction

GCC is often used to cross-compile software for Arm microcontrollers and embedded devices which have firmware and other low-level software. The executables are arm-none-eabi-gcc and arm-none-eabi-g++

GCC is also used to cross compile Linux applications. Applications can be compiled for 32-bit or 64-bit Linux systems. 

The executables for 32-bit are arm-linux-gnueabihf-gcc and arm-linux-gnueabihf-g++. 

The executables for 64-bit are aarch64-linux-gnu-gcc and aarch64-linux-gnu-g++

Software can be compiled on an x86 or or Arm Linux host machine.

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


[Return to the top](#top)


# Install GCC using the Arm GNU Toolchain {#Arm-GNU}


## Introduction

Arm GNU Toolchain is a community supported, pre-built GNU compiler toolchain for Arm based CPUs.
There are many versions of the [Arm GNU Toolchain](https://developer.arm.com/Tools%20and%20Software/GNU%20Toolchain) available. In general, the latest version is recommended for use, as this will contain the latest optimization improvements, as well as support for the latest Arm IP. However there are reasons you may wish to use earlier compiler versions, so older versions are also available.

## Download toolchain

Arm GNU Toolchain releases consist of cross toolchains for the following host operating systems:
    
Linux    
  * Available for x86_64 and AArch64 host architectures
  * Available for bare-metal and Linux targets      
    
Windows    
  * Available for x86 host architecture only (compatible with x86_64)
  * Available for bare-metal and Linux targets
                      
macOS    
  * Available for x86_64 and Apple silicon (beta) host architectures
  * Available for bare-metal targets only
    
Download the correct toolchain variant for your development needs from the [Arm Developer website](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/downloads).

## Installation

### Installing on Linux

Unpack the downloaded file to the install directory.

{{< tabpane code=true >}}
  {{< tab header="x86_64">}}
tar xJf arm-gnu-toolchain-12.2.rel1-x86_64-<TRIPLE>.tar.xz -C /path/to/install/dir
  {{< /tab >}}
  {{< tab header="aarch64">}}
tar xJf arm-gnu-toolchain-12.2.rel1-aarch64-<TRIPLE>.tar.xz -C /path/to/install/dir
  {{< /tab >}}
{{< /tabpane >}}

Add the `bin` directory to the `PATH` environment variable (bash).

```console
export PATH=/path/to/install/dir/bin:$PATH
```

Here is a specific example for an Arm Linux host and the AArch32 bare-metal target.

```bash { target="ubuntu:latest" }
wget https://developer.arm.com/-/media/Files/downloads/gnu/12.2.rel1/binrel/arm-gnu-toolchain-12.2.rel1-aarch64-arm-none-eabi.tar.xz
tar xJf arm-gnu-toolchain-12.2.rel1-aarch64-arm-none-eabi.tar.xz -C $HOME
echo 'export PATH="$PATH:$HOME/arm-gnu-toolchain-12.2.rel1-aarch64-arm-none-eabi/bin"' >> ~/.bashrc
source ~/.bashrc
```

### Installing on macOS

Downloads for macOS are available as tar files (`.tar.xz`) and package files (`.pkg`). 

For `.tar.xz` files, unpack the downloaded file to the install directory.

{{< tabpane code=true >}}
  {{< tab header="x86_64">}}
tar xJf arm-gnu-toolchain-12.2.rel1-darwin-x86_64-<TRIPLE>.tar.xz -C /path/to/install/dir
  {{< /tab >}}
  {{< tab header="aarch64">}}
tar xJf arm-gnu-toolchain-12.2.rel1-darwin-arm64-<TRIPLE>.tar.xz -C /path/to/install/dir
  {{< /tab >}}
{{< /tabpane >}}

For `.pkg` files use the installer. 

{{< tabpane code=true >}}
  {{< tab header="x86_64">}}
sudo installer -pkg arm-gnu-toolchain-12.2.rel1-darwin-x86_64-<TRIPLE>.pkg -target /
  {{< /tab >}}
  {{< tab header="aarch64">}}
sudo installer -pkg arm-gnu-toolchain-12.2.rel1-darwin-arm64-<TRIPLE>.pkg -target /
  {{< /tab >}}
{{< /tabpane >}}

Use a text editor to add the `bin` directory as a new line in `/etc/paths`.

```console
sudo nano /etc/paths
```

For example the path could be: `/Applications/ArmGNUToolchain/12.2.rel1/arm-none-eabi/bin`

The `/etc/paths` file is a list of paths to search.

```console
/usr/local/bin
/System/Cryptexes/App/usr/bin
/usr/bin
/bin
/usr/sbin
/sbin
/Applications/ArmGNUToolchain/12.2.rel1/arm-none-eabi/bin
```

Here is a specific example for macOS with Apple Silicon and the AArch32 bare-metal target. 

```console
wget https://developer.arm.com/-/media/Files/downloads/gnu/12.2.rel1/binrel/arm-gnu-toolchain-12.2.rel1-darwin-arm64-arm-none-eabi.pkg
sudo installer -pkg arm-gnu-toolchain-12.2.rel1-darwin-arm64-arm-none-eabi.pkg -target /
echo '/Applications/ArmGNUToolchain/12.2.rel1/arm-none-eabi/bin' | sudo tee -a /etc/paths
```

### Installing on Windows
Double-click on the installer (e.g. `gcc-arm-_version_--mingw-w64-i686-arm-none-eabi.exe`) and follow on-screen instructions.

The installer can also be run on the command line. When run on
the command-line, the following options can be set:
  - `/S` Run in silent mode
  - `/P` Adds the installation `bin` directory to the system `PATH`
  - `/R` Adds Install Folder registry entry for the install.

For example, to install the tools silently, amend users `PATH` and add registry entry:
```console
gcc-arm-_version_--mingw-w64-i686-arm-none-eabi.exe /S /P /R
```

The zip package is a backup to Windows installer for those who cannot run the installer. You can unzip the package and then invoke the tools directly. 

## Setting up product license 

Arm GNU Toolchain is open sourced and freely available for use. No licenses need to be set up for use.

To use the Arm GNU Toolchain in conjunction with [Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio) you must [register the toolchain](https://developer.arm.com/documentation/101469/2022-0/Installing-and-configuring-Arm-Development-Studio/Register-a-compiler-toolchain).

## Get started 

To verify the installation is correct enter:
```console
arm-none-eabi-gcc -v
```

Additional examples are included in the toolchain installation at:
```console
${install_dir}/_version_/share/gcc-arm-none-eabi/samples
```

[Return to the top](#top)

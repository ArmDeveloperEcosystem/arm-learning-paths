---
additional_search_terms:
- armclang
- compiler
- hpc
- linux
- allinea
author: Florent Lebeau
layout: installtoolsall
minutes_to_complete: 15
multi_install: false
multitool_install_part: false
description: Install Arm Compiler for Linux (ACfL) on Arm Linux (aarch64) to access the armclang C/C++ compiler, armflang Fortran compiler, and Arm Performance Libraries for HPC development.
official_docs: https://developer.arm.com/documentation/101458/latest
test_images:
- ubuntu:latest
- fedora:latest
test_link: null
test_maintenance: true
title: Arm Compiler for Linux
tool_install: true
weight: 1
---
[Arm Compiler for Linux (ACfL)](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Linux) is a suite of tools containing Arm C/C++ Compiler (`armclang`), Arm Fortran Compiler (`armflang`), and Arm Performance Libraries (ArmPL). It is tailored to the development of High Performance Computing (HPC) applications.

Arm Compiler for Linux runs on 64-bit Arm machines and supports all 64-bit Arm-based [server-class hardware](/learning-paths/servers-and-cloud-computing/intro/). It is not a cross-compiler.

You don't require any additional license to use Arm Compiler for Linux.

## Before you begin

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The output should be:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

Ensure you are using a [supported Linux distribution](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Linux#Supported-Devices). 

If any of the following tools are not already installed by your Linux
distribution, install them before installing Arm Compiler for Linux.
These packages can be installed with the appropriate package manager for your OS:

  - SLES: `awk` `environment-modules` `glibc-devel` `gzip` `python3` `tar`
  - RHEL: `environment-modules` `glibc-devel` `procps` `python3`
  - Amazon Linux: `environment-modules` `glibc-devel` `gzip procps` `python3` `tar`
  - Ubuntu: `environment-modules` `libc6-dev` `python3`

Ensure that you're running the minimum supported version for Python, which is version 3.6.

Ensure that you have at least 2 GB of free hard disk space to both download and unpack the Arm Compiler for Linux package. You must also have an additional 6 GB of
free space to install the package.

Run the following commands:

```console
sudo apt update
sudo apt install -y python-is-python3 libc6-dev
```

You are now ready to install ACfL [manually](#manual) or with [Spack](#spack).


## Download and install ACfL using an install script

Use an Arm recommended script to select, download, and install your preferred ACfL package.

```console
bash <(curl -L https://developer.arm.com/-/cdn-downloads/permalink/Arm-Compiler-for-Linux/Package/install.sh)
```

## Download and install ACfL manually with wget {#manual}

Download releases from the command line using `wget`. Install `wget` if not present.

```bash
sudo apt install wget
```

### Fetch the appropriate ACfL installer

ACfL installation packages are available to download from [Arm Developer](https://developer.arm.com/downloads/-/arm-compiler-for-linux). Individual Arm Performance Libraries (ArmPL) packages are also available.

To fetch the ACfL installers, run:

#### Ubuntu Linux

```bash { target="ubuntu:latest" }
wget  https://developer.arm.com/-/cdn-downloads/permalink/Arm-Compiler-for-Linux/Version_24.10.1/arm-compiler-for-linux_24.10.1_Ubuntu-22.04_aarch64.tar
```
#### Red Hat Linux
```bash { target="fedora:latest" }
wget https://developer.arm.com/-/cdn-downloads/permalink/Arm-Compiler-for-Linux/Version_24.10.1/arm-compiler-for-linux_24.10.1_RHEL-9_aarch64.tar
```

### Install ACfL

To install Arm Compiler for Linux on your 64-bit Linux Arm machine, extract the package and run the installation script.

Each command sequence includes accepting the license agreement to automate the installation and installing Environment Modules.

#### Ubuntu Linux

```bash { target="ubuntu:latest" }
sudo -E apt-get -y install environment-modules python3 libc6-dev
tar -xvf arm-compiler-for-linux_24.10.1_Ubuntu-22.04_aarch64.tar
cd ./arm-compiler-for-linux_24.10.1_Ubuntu-22.04
sudo ./arm-compiler-for-linux_24.10.1_Ubuntu-22.04.sh --accept
```

#### Red Hat Linux

```console
sudo yum -y install environment-modules python3 glibc-devel
tar -xvf arm-compiler-for-linux_24.10.1_RHEL-9_aarch64.tar
cd ./arm-compiler-for-linux_24.10.1_RHEL-9
sudo ./arm-compiler-for-linux_24.10.1_RHEL-9.sh --accept
```

{{% notice Warning %}}
⚠️ On RPM based systems (such as Red Hat), if an
alternative version of GCC (not the GCC bundled with ACfL) is installed
**after** ACfL, you will not be able to uninstall ACfL fully. For example, a GDB
(GNU Project Debugger) installation will install the native system GCC. If this
install takes place **after** ACfL, you will no longer be able to fully
uninstall ACfL.
{{% /notice %}}

## Download and install ACfL using system packages

To download and install ACfL using system packages, follow these steps.

### Install ACfL on Ubuntu Linux 20.04 and 22.04

Arm Compiler for Linux is available to install with the Ubuntu system package manager `apt` command.

#### Set up the ACfL package repository

Add the ACfL `apt` package repository to your system. 

{{% notice Note %}}
These instructions are for Ubuntu 22.04. For other releases, see [available versions](https://developer.arm.com/packages/).
{{% /notice %}}


After adding the repository to your system, the ACfL Ubuntu package repository is now ready to use. Run the commands below to install the dependencies needed.


```console
sudo apt update
sudo apt install -y wget gnupg gpg environment-modules python3 libc6-dev
wget -qO - https://developer.arm.com/packages/ACfL%3AUbuntu-22/jammy/Release.key | sudo tee /etc/apt/trusted.gpg.d/developer-arm-com.asc
echo "deb https://developer.arm.com/packages/ACfL%3AUbuntu-22/jammy/ ./" | sudo tee /etc/apt/sources.list.d/developer-arm-com.list
sudo apt update
```

#### Install Arm Compiler for Linux

To install Arm Compiler for Linux, run:

```console
sudo apt install acfl -y
```

### Install ACfL on Amazon Linux 2023 (AL2023)

Arm Compiler for Linux is available to install from the AL2023 package repository with either the `dnf` or `yum` system package manager.

Install ACfL and prerequisites from the AL2023 `rpm` package repository with `dnf`:

```console
sudo dnf update -y
sudo dnf -y install 'dnf-command(config-manager)' procps psmisc make environment-modules
sudo dnf config-manager addrepo --from-repofile=https://developer.arm.com/packages/ACfL%3AAmazonLinux-2023/latest/ACfL%3AAmazonLinux-2023.repo
sudo dnf -y install acfl
```

Or using the equivalent `yum` commands:

```console
sudo yum update -y
sudo yum -y install 'dnf-command(config-manager)' procps psmisc make environment-modules
sudo yum config-manager addrepo --from-repofile=https://developer.arm.com/packages/ACfL%3AAmazonLinux-2023/latest/ACfL%3AAmazonLinux-2023.repo
sudo yum -y install acfl
```

The ACfL tools are now ready to use.

### Install ACfL on Red Hat Enterprise Linux (RHEL) 9

Arm Compiler for Linux is available to install from the RHEL 9 package repository with either the `dnf` or `yum` system package manager.

Install ACfL and prerequisites from the RHEL 9 `rpm` package repository with `dnf`:

```console
sudo dnf update -y
sudo dnf -y install 'dnf-command(config-manager)' procps psmisc make environment-modules
sudo dnf config-manager addrepo --from-repofile=https://developer.arm.com/packages/ACfL%3ARHEL-9/standard/ACfL%3ARHEL-9.repo
sudo dnf -y install acfl
```

Or using the equivalent `yum` commands:

```console
sudo yum update -y
sudo yum -y install 'dnf-command(config-manager)' procps psmisc make environment-modules
sudo yum config-manager addrepo --from-repofile=https://developer.arm.com/packages/ACfL%3ARHEL-9/standard/ACfL%3ARHEL-9.repo
sudo yum -y install acfl
```

The ACfL tools are now ready to use.

### Set up the environment for ACfL

Arm Compiler for Linux uses environment modules to dynamically modify your user environment. Refer to the [Environment Modules documentation](https://lmod.readthedocs.io/en/latest/#id) for more information.

Set up the environment, for example, in your `.bashrc` and add module files. Then, list the available modules:

#### Ubuntu Linux:

```bash { target="ubuntu:latest" pre_cmd=". /usr/share/modules/init/bash" pre_cmd="module use /opt/arm/modulefiles" }
echo ". /usr/share/modules/init/bash" >> $HOME/.bashrc
echo "module use /opt/arm/modulefiles" >> $HOME/.bashrc
source $HOME/.bashrc
module avail
```

#### Red Hat or Amazon Linux

```console
echo ". /usr/share/Modules/init/bash" >> $HOME/.bashrc
echo "module use /opt/arm/modulefiles" >> $HOME/.bashrc
source $HOME/.bashrc
module avail
```

To configure Arm Compiler for Linux:

```console
module load acfl/24.10.1
```

To configure GCC:

```console
module load gnu/14.2.0
```

ACfL is now [ready to use](#armclang).

## Download and install ACfL with Spack {#spack}

Arm Compiler for Linux is available with the [Spack](https://spack.io/) package manager. For more information, see the [Arm Compiler for Linux and Arm PL now available in Spack](https://developer.arm.com/community/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/arm-compiler-for-linux-and-arm-pl-now-available-in-spack) blog post.

### Set up Spack for ACfL

Clone the Spack repository and add `bin` directory to the path:

```console
git clone -c feature.manyFiles=true https://github.com/spack/spack.git
export PATH=/home/ubuntu/spack/bin:$PATH
```

Set up shell support:

```console
. /home/ubuntu/spack/share/spack/setup-env.sh
```

Spack is now ready to use.

### Install ACfL using Spack

To download and install Arm Compiler for Linux, run:

```console
spack install acfl
```

To install only the Arm Performance Libraries, use:

```console
spack install armpl-gcc
```

### Set up the environment for ACfL using Spack

Use the commands below to set up the environment:

```console
spack load acfl
spack compiler find
```

ACfL is now [ready to use](#armclang).


## Get started with the Arm C/C++ compiler {#armclang}

To get started with the Arm C/C++ Compiler and compile a simple application, follow these steps.

Check that you're using the correct compiler version:
```bash { env_source="$HOME/.bashrc", pre_cmd=". /usr/share/modules/init/bash; module use /opt/arm/modulefiles; module load acfl/24.10.1" }
armclang --version
```

Create a text file named `hello.c` with the following contents:

```C { file_name="hello.c" }
#include <stdio.h>

int main()
{
    printf("Hello, C World!\n");
    return 0;
}
```

Build the application:

```console
armclang hello.c -o hello
```

Run the application:

```console
./hello
```

The output should be:

```output
Hello, C World!
```

## Get started with the Arm Fortran compiler {#fortran}

To get started with the Arm Fortran Compiler and compile a simple application, follow these steps.

Check that you're using the correct compiler version:
```bash { env_source="$HOME/.bashrc", pre_cmd=". /usr/share/modules/init/bash; module use /opt/arm/modulefiles; module load acfl/24.10.1" }
armflang --version
```

Create a text file named `hello.f90` with the following contents:

```fortran { file_name="hello.f90" }
program hello
  ! This is a comment line; it is ignored by the compiler
  print *, 'Hello, Fortran World!'
end program hello
```

Build the application:
```console
armflang hello.f90 -o hello
```

Run the application:
```console
./hello
```

The output should be:
```output
Hello, Fortran World!
```

## Get started with Arm Performance Libraries {#armpl}

To get started with the [Arm Performance Libraries](https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Libraries) and learn how to select the optimal library for your system, see [Get started with Arm Performance Libraries](https://developer.arm.com/documentation/101004/latest).

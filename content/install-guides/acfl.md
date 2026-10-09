---
additional_search_terms:
- armclang
- armflang
- compiler
- hpc
- linux
- ATfL
- Arm Compiler for Linux
- ACfL
author: Florent Lebeau
layout: installtoolsall
minutes_to_complete: 15
multi_install: false
multitool_install_part: false
description: Install Arm Toolchain for Linux (ATfL) on Arm Linux (aarch64) to access the armclang C/C++ compiler, armflang Fortran compiler, and Arm Performance Libraries for HPC development.
official_docs: https://support.arm.com/documentation/110477/latest
test_images:
- ubuntu:latest
test_maintenance: true
title: Arm Toolchain for Linux
tool_install: true
weight: 1
---

[Arm Toolchain for Linux](https://github.com/arm/arm-toolchain) (ATfL) is an open-source LLVM-based compiler suite for AArch64 Linux systems. It includes the `armclang` C/C++ compiler, the `armflang` Fortran compiler, and [Arm Performance Libraries](/install-guides/armpl/) (ArmPL). ATfL is optimized for Arm Neoverse cores and targets scientific computing, HPC, AI, and cloud-native workloads.

ATfL replaces the older Arm Compiler for Linux (ACfL), which reached end of life with version 24.10. If you are migrating from ACfL, see the [Arm Toolchain for Linux User Guide](https://support.arm.com/documentation/110477/latest) for guidance.

ATfL runs on 64-bit Arm Linux machines and supports all 64-bit Arm-based [server-class hardware](/learning-paths/servers-and-cloud-computing/intro/). It isn't a cross-compiler.

You don't need any additional license to use Arm Toolchain for Linux.

## Before you begin

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The expected output is:

```output
aarch64
```

If you see a different result, you aren't using an Arm computer running 64-bit Linux.

ATfL is supported on the following Linux distributions:

- Ubuntu 22.04 and 24.04
- Red Hat Enterprise Linux 8, 9, and 10
- Amazon Linux 2023
- SUSE Linux Enterprise Server 15 and 16

## Install ATfL using the system package manager {#package}

The recommended way to install ATfL is through the [Arm Toolchains repository](/install-guides/arm-toolchains-repository/). This method installs ATfL and Arm Performance Libraries using your system package manager and handles updates automatically.

### Ubuntu

Install the Arm Toolchains repository package and then install ATfL:

```bash 
curl -O https://developer.arm.com/packages/arm-toolchains/ubuntu/pool/arm-toolchains-repository_2-2~noble_all.deb
sudo dpkg -i arm-toolchains-repository_2-2~noble_all.deb
sudo apt update
sudo apt install -y arm-toolchain-for-linux
```

{{% notice Ubuntu version %}}
The commands shown are for Ubuntu 24.04. For Ubuntu 22.04, replace `noble` with `jammy` in the repository package filename. For other distributions, see the [Arm Toolchains repository install guide](/install-guides/arm-toolchains-repository/).
{{% /notice %}}

### Red Hat Enterprise Linux 8

Install the repository package and then install ATfL:

```console
sudo dnf install -y https://developer.arm.com/packages/arm-toolchains/rhel/el8/aarch64/arm-toolchains-repository-2-2.el8.noarch.rpm
sudo dnf clean all
sudo dnf makecache
sudo dnf install -y arm-toolchain-for-linux
```

### Red Hat Enterprise Linux 9

Install the repository package and then install ATfL:

```console
sudo dnf install -y https://developer.arm.com/packages/arm-toolchains/rhel/el9/aarch64/arm-toolchains-repository-2-2.el9.noarch.rpm
sudo dnf clean all
sudo dnf makecache
sudo dnf install -y arm-toolchain-for-linux
```

### Red Hat Enterprise Linux 10

Install the repository package and then install ATfL:

```console
sudo dnf install -y https://developer.arm.com/packages/arm-toolchains/rhel/el10/aarch64/arm-toolchains-repository-2-2.el10.noarch.rpm
sudo dnf clean all
sudo dnf makecache
sudo dnf install -y arm-toolchain-for-linux
```

### Amazon Linux 2023

Install the repository package and then install ATfL:

```console
sudo dnf install -y https://developer.arm.com/packages/arm-toolchains/amazonlinux/al2023/aarch64/arm-toolchains-repository-2-2.al2023.noarch.rpm
sudo dnf clean all
sudo dnf makecache
sudo dnf install -y arm-toolchain-for-linux
```

### SUSE Linux Enterprise Server 15

Install the repository package and then install ATfL:

```console
sudo zypper install -y https://developer.arm.com/packages/arm-toolchains/sles/sles15/aarch64/arm-toolchains-repository-2-2.sles15.noarch.rpm
sudo zypper clean
sudo zypper refresh
sudo zypper install -y arm-toolchain-for-linux
```

### SUSE Linux Enterprise Server 16

Install the repository package and then install ATfL:

```console
sudo zypper install -y https://developer.arm.com/packages/arm-toolchains/sles/sles16/aarch64/arm-toolchains-repository-2-2.sles16.noarch.rpm
sudo zypper clean
sudo zypper refresh
sudo zypper install -y arm-toolchain-for-linux
```

## Set up the environment {#env}

ATfL installs to `/opt/arm/arm-toolchain-for-linux`. You need to add the `bin` directory to your `PATH` before using the compilers.

### Option 1: Source the environment script

Source the provided `env.bash` script to configure your shell:

```bash
source /opt/arm/arm-toolchain-for-linux/env.bash
```

To load the environment automatically in new shells, add it to your `.bashrc`:

```bash
echo 'source /opt/arm/arm-toolchain-for-linux/env.bash' >> $HOME/.bashrc
source $HOME/.bashrc
```

### Option 2: Use environment modules

ATfL provides module files for use with [Environment Modules](https://modules.readthedocs.io/). Install the `environment-modules` package if it isn't already present:

```bash
sudo apt install -y environment-modules
```

Set up your shell to use modules and load ATfL:

```bash { pre_cmd=". /usr/share/modules/init/bash; module use /opt/arm/modulefiles" }
echo '. /usr/share/modules/init/bash' >> $HOME/.bashrc
echo 'module use /opt/arm/modulefiles' >> $HOME/.bashrc
source $HOME/.bashrc
module load atfl/22.1
```

To see all available modules, run:

```bash { pre_cmd=". /usr/share/modules/init/bash; module use /opt/arm/modulefiles" }
module avail
```

## Verify installation {#verify}

After setting up the environment, verify the compiler versions:

```bash { env_source="/opt/arm/arm-toolchain-for-linux/env.bash" }
armclang --version
```

The output is similar to:

```output
Arm Toolchain for Linux 22.1.0 clang version 22.1.0 (https://github.com/arm/arm-toolchain.git c95792353373404441df364b5a762338e5642230)
Target: aarch64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/arm/arm-toolchain-for-linux/bin
Configuration file: /opt/arm/arm-toolchain-for-linux/bin/clang.cfg
Arm Toolchain ID: L0054 (b1c6e086)
```

Also verify the Fortran compiler:

```bash { env_source="/opt/arm/arm-toolchain-for-linux/env.bash" }
armflang --version
```

The output is similar to:

```output
Arm Toolchain for Linux 22.1.0 flang version 22.1.0 (https://github.com/arm/arm-toolchain.git c95792353373404441df364b5a762338e5642230)
Target: aarch64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/arm/arm-toolchain-for-linux/bin
Configuration file: /opt/arm/arm-toolchain-for-linux/bin/flang.cfg
Arm Toolchain ID: L0054 (b1c6e086)
```

## Get started with the C/C++ compiler {#armclang}

Create a text file named `hello.c` with the following contents:

```c { file_name="hello.c" }
#include <stdio.h>

int main()
{
    printf("Hello, C World!\n");
    return 0;
}
```

Build and run the application:

```bash { env_source="/opt/arm/arm-toolchain-for-linux/env.bash" }
armclang hello.c -o hello
./hello
```

The output is:

```output
Hello, C World!
```

## Get started with the Fortran compiler {#fortran}

Create a text file named `hello.f90` with the following contents:

```fortran { file_name="hello.f90" }
program hello
  print *, 'Hello, Fortran World!'
end program hello
```

Build and run the application:

```bash { env_source="/opt/arm/arm-toolchain-for-linux/env.bash" }
armflang hello.f90 -o hello
./hello
```

The output is:

```output
 Hello, Fortran World!
```

## Get started with Arm Performance Libraries {#armpl}

ATfL automatically installs [Arm Performance Libraries](/install-guides/armpl/) (ArmPL) as a dependency. ArmPL provides optimized BLAS, LAPACK, FFT, and sparse routines tuned for Arm Neoverse processors.

To load the ArmPL environment module:

```bash { pre_cmd=". /usr/share/modules/init/bash; module use /opt/arm/modulefiles" }
module load arm-performance-libraries
```

This sets the `ARMPL_DIR` environment variable and configures `LD_LIBRARY_PATH` and `PKG_CONFIG_PATH`.

For detailed usage instructions, see the [Arm Performance Libraries install guide](/install-guides/armpl/) and the [ArmPL documentation](https://developer.arm.com/documentation/101004/latest).

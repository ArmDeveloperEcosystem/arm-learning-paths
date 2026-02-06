---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Arm Performance Libraries

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- ArmPL
- Neoverse
- SVE
- Neon
- HPC

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 10

test_maintenance: true
test_images:
  - ubuntu:latest

### Link to official documentation
official_docs: https://developer.arm.com/documentation/101004
author: Pareena Verma

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

[Arm Performance Libraries](https://developer.arm.com/downloads/-/arm-performance-libraries#documentation) provides developers with optimized math libraries for high performance computing applications on Arm Neoverse based hardware.

These libraries include highly optimized functions for BLAS, LAPACK, FFT, sparse linear algebra, random number generation, libamath and libastring.
These libraries are free to use and do not require a license.

Arm Performance Libraries are available for use on [Windows 11 on Arm](#windows), [macOS](#macos) (Apple Silicon), and [Linux](#linux) (AArch64) hosts.

## How do I install Arm Performance Libraries on Windows? {#windows}

On your Windows 11 Arm machine, go to the [Arm Performance Libraries download page](https://developer.arm.com/downloads/-/arm-performance-libraries).
Click on the Download Windows section and download the Windows Installer:
`arm-performance-libraries_<version>_Windows.msi`

Double click to open this file and start the Arm Performance Libraries Setup Wizard.

![win_wizard00 #left](/install-guides/_images/armpl_wizard00.png)

Read and accept the End-User License Agreement by clicking the checkbox 'I accept the terms of this License Agreement'.

![win_wizard01 #left](/install-guides/_images/armpl_wizard01.png)

Select a location for the installation on your system. The default is:

`C:\Program Files\Arm Performance Libraries`

![win_wizard02 #left](/install-guides/_images/armpl_wizard02.png)

Click 'Install' and then 'Finish' to complete the installation.

![win_wizard03 #left](/install-guides/_images/armpl_wizard03.png)

![win_wizard04 #left](/install-guides/_images/armpl_wizard04.png)

To install Arm Performance Libraries from a command prompt and automatically accept the End User License Agreement use:
```console
msiexec.exe /i arm-performance-libraries_<version>_Windows.msi /quiet ACCEPT_EULA=1
```

To install Arm Performance Libraries using the `winget` package manager and automatically accept the End User License Agreement use:
```console
winget install --accept-package-agreements Arm.ArmPerformanceLibraries
```

You can now start linking your application to the Arm Performance libraries on your Windows on Arm device. Follow the examples in the included `RELEASE_NOTES` file of your extracted installation directory to get started.

For more information refer to [Get started with Arm Performance Libraries](https://developer.arm.com/documentation/109361).


## How do I install Arm Performance Libraries on macOS? {#macos}

[Download](https://developer.arm.com/downloads/-/arm-performance-libraries) the appropriate package for your macOS distribution.

In a terminal, run the command shown below to download the macOS package:
```console
wget https://developer.arm.com/-/cdn-downloads/permalink/Arm-Performance-Libraries/Version_26.01/arm-performance-libraries_26.01_macOS.tgz
```

Use tar to extract the file:
```console
tar zxvf arm-performance-libraries_26.01_macOS.tgz
```

Output of above command:
```console
armpl_26.01_flang-21.dmg
```

Mount the disk image by running from a terminal:
```console
hdiutil attach armpl_26.01_flang-21.dmg
```

Now run the installation script as a superuser:

```console
/Volumes/armpl_26.01_flang-21_installer/armpl_26.01_flang-21_install.sh -y
```

Using this command you automatically accept the End User License Agreement and the packages are installed to the `/opt/arm` directory. If you want to change the installation directory location use the `--install_dir=` option with the script and provide the desired directory location.

To install Arm Performance Libraries using Homebrew in a terminal and automatically accept the End User License Agreement use:

```console
brew install arm-performance-libraries
```

The installer runs using `sudo` so you may be asked to input your password.

To get started, compile and test the examples included in the `/opt/arm/<armpl_dir>/examples/`, or `<install_dir>/<armpl_dir>/examples/` directory, if you have installed to a different location than the default.

For more information refer to [Get started with Arm Performance Libraries](https://developer.arm.com/documentation/109362).


## How do I install Arm Performance Libraries on Linux? {#linux}

Arm Performance Libraries are supported on most Linux distributions like Ubuntu, RHEL, SLES and Amazon Linux on an `AArch64` host and compatible with various versions of GCC, LLVM, and NVHPC. The GCC compatible releases are built with GCC 14 and tested with GCC versions 7 to 14. The LLVM compatible releases are tested with LLVM 21.1. The NVHPC compatible releases are tested with NVHPC 25.11.

### How do I manually download and install Arm Performance Libraries on Linux?

[Download](https://developer.arm.com/downloads/-/arm-performance-libraries) the appropriate package for your Linux distribution. The deb based installers can be used on Ubuntu 22 and Ubuntu 24. The RPM based installers can be used on the following supported distributions:

- Amazon Linux 2, Amazon Linux 2023
- RHEL-8, RHEL-9, RHEL-10
- SLES-15 Service Packs 6 and 7

The instructions shown below are for deb based installers for GCC users.

In a terminal, run the command shown below to download the Debian package:

```bash
wget https://developer.arm.com/-/cdn-downloads/permalink/Arm-Performance-Libraries/Version_26.01/arm-performance-libraries_26.01_deb_gcc.tar
```

Use `tar` to extract the file and then change directory:

```bash
tar xf arm-performance-libraries_26.01_deb_gcc.tar
```

Run the installation script as a super user:

```bash
sudo ./arm-performance-libraries_26.01_deb/arm-performance-libraries_26.01_deb.sh --accept
```

Using the `--accept` switch you automatically accept the End User License Agreement and the packages are installed to the `/opt/arm` directory.

If you want to change the installation directory location use the `--install-to` option with the script and provide the desired directory location.

### How do I download and install Arm Performance Libraries using system packages on Linux?

Arm Performance Libraries are available to install using Linux system package managers. The instructions shown below are for the Ubuntu system package manager `apt` command.

Add the Arm Performance Libraries `apt` package repository to your system:

```bash
. /etc/os-release
curl "https://developer.arm.com/packages/arm-toolchains:${NAME,,}-${VERSION_ID/%.*/}/${VERSION_CODENAME}/Release.key" | sudo tee /etc/apt/trusted.gpg.d/developer-arm-com.asc
echo "deb https://developer.arm.com/packages/arm-toolchains:${NAME,,}-${VERSION_ID/%.*/}/${VERSION_CODENAME}/ ./" | sudo tee /etc/apt/sources.list.d/developer-arm-com.list
sudo apt update
```

Download and install Arm Performance Libraries with:

```bash
sudo apt install arm-performance-libraries
```

### How do I set up the environment for Arm Performance Libraries on Linux?

Install environment modules on your machine:

```console
sudo apt install environment-modules
```

Set your bash environment to use modules:

```console
source /usr/share/modules/init/bash
```

Set the `MODULEPATH` environment variable to point to the location of the installed modulefiles for Arm Performance Libraries:

```console
export MODULEPATH=$MODULEPATH:/opt/arm/modulefiles
```

List the available modules:

```console
module avail
```

The output should be similar to:

```output
armpl/26.01_gcc
```

Load the appropriate module:

```console
module load armpl/26.01_gcc
```

You can now compile and test the examples included in the `/opt/arm/<armpl_dir>/examples/`, or `<install_dir>/<armpl_dir>/examples/` directory, if you have installed to a different location than the default.

For more information refer to [Get started with Arm Performance Libraries](https://developer.arm.com/documentation/102620).


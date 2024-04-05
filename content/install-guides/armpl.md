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

### Link to official documentation
official_docs: https://developer.arm.com/documentation/101004
author_primary: Pareena Verma

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

The [Arm Performance Libraries](https://developer.arm.com/downloads/-/arm-performance-libraries#documentation) provide developers with optimized math libraries for high performance computing applications on Arm Neoverse based hardware.

These libraries include highly optimized functions for BLAS, LAPACK, FFT, sparse linear algebra, libamath and libastring.
These libraries are free to use and do not require a license. They can be installed either standalone or with your installation of [Arm Compiler for Linux](/install-guides/acfl). This install guide covers the standalone installation.

Arm Performance Libraries are available for use on [Windows 11 on Arm](#windows), [macOS](#macos) (Apple Silicon), and [Linux](#linux) (AArch64) hosts.

Below are the official documentation references:

- [Arm Performance Libraries Reference Guide](https://developer.arm.com/documentation/101004)
- Get started with Arm Performance Libraries
    - [Windows](https://developer.arm.com/documentation/109361)
    - [MacOS](https://developer.arm.com/documentation/109362)
    - [Linux](https://developer.arm.com/documentation/102620)

## Windows {#windows}

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

You can now start linking your application to the Arm Performance libraries on your Windows on Arm device. Follow the examples in the included `RELEASE_NOTES` file of your extracted installation directory to get started.

For more information refer to [Get started with Arm Performance Libraries](https://developer.arm.com/documentation/109361).


## macOS {#macos}

Go to the Download MacOS section of the [Arm Performance Libraries download page](https://developer.arm.com/downloads/-/arm-performance-libraries) and download the `dmg` file.
Double-click on the icon of the downloaded package to mount the disk image.

Alternatively, open a terminal and run the command below:

```console
hdiutil attach arm-performance-libraries_23.10_macOS.dmg
```

Now run the installation script as a superuser:

```console
/Volumes/arm-performance-libraries_23.10_macOS/arm-performance-libraries_23.10_macOS_install.sh -y
```
Using this command you automatically accept the End User License Agreement and the packages are installed to the `/opt/arm` directory. If you want to change the installation directory location use the `--install_dir` option with the script and provide the desired directory location.

To get started, compile and test the examples included in the `/opt/arm/<armpl_dir>/examples/`, or `<install_dir>/<armpl_dir>/examples/` directory, if you have installed to a different location than the default.

For more information refer to [Get started with Arm Performance Libraries](https://developer.arm.com/documentation/109362).


## Linux {#linux}

Arm Performance Libraries are supported on most Linux Distributions like Ubuntu, RHEL, SLES and Amazon Linux on an `AArch64` host and compatible with various versions of GCC.

[Download](https://developer.arm.com/downloads/-/arm-performance-libraries) the appropriate package for your Linux distribution and version of GCC from the Download Linux section.

The instructions shown below are for an Ubuntu 22.04 AArch64 Linux Host with GCC version 12.2 installed.

On a terminal, run the command shown below to download the appropriate package:
```command
wget https://developer.arm.com/-/media/Files/downloads/hpc/arm-performance-libraries/23-10/ubuntu-22/arm-performance-libraries_23.10_Ubuntu-22.04_gcc-12.2.tar
```

Use `tar` to extract the file and then change directory:

```command
tar -xf arm-performance-libraries_23.10_Ubuntu-22.04_gcc-12.2.tar
cd arm-performance-libraries_23.10_Ubuntu-22.04/
```
Run the installation script as a super user:

```command
sudo ./arm-performance-libraries_23.10_Ubuntu-22.04.sh -a
```
Using the `-a` switch you automatically accept the End User License Agreement and the packages are installed to the `/opt/arm` directory.

If you want to change the installation directory location use the `--install-to` option with the script and provide the desired directory location.

### Setup your environment

Install environment modules on your machine:

```command
sudo apt install environment-modules
```

Set your bash environment to use modules:

```command
source /usr/share/modules/init/bash
```

Set the `MODULEPATH` environment variable to point to the location of the installed modulefiles for Arm Performance Libraries:

```command
export MODULEPATH=$MODULEPATH:/opt/arm/modulefiles
```

List the available modules:

```command
module avail
```

The output should be similar to:

```output
armpl/23.10.0_gcc-12.2
```

Load the appropriate module:

```command
module load armpl/23.10.0_gcc-12.2
```
You can now compile and test the examples included in the `/opt/arm/<armpl_dir>/examples/`, or `<install_dir>/<armpl_dir>/examples/` directory, if you have installed to a different location than the default.

For more information refer to [Get started with Arm Performance Libraries](https://developer.arm.com/documentation/102620).


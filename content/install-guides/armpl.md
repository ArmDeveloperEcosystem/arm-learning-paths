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
description: Install Arm Performance Libraries on Windows on Arm, macOS, and Linux AArch64 to access optimized BLAS, LAPACK, FFT, and math functions for high-performance computing on Arm.
author: Pareena Verma

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

[Arm Performance Libraries](https://developer.arm.com/downloads/-/arm-performance-libraries#documentation) provides developers with optimized math libraries for high-performance computing applications on Arm Neoverse-based hardware.

These libraries include highly-optimized functions for BLAS, LAPACK, FFT, sparse linear algebra, random number generation, libamath, and libastring.

Arm Performance Libraries are free to use and don't require a license. These libraries are available for use on [Windows 11 on Arm](#windows), [macOS](#macos) (Apple Silicon), and [Linux](#linux) (AArch64) hosts.

## Install Arm Performance Libraries on Windows {#windows}

On your Windows 11 Arm machine, go to the [Arm Performance Libraries download page](https://developer.arm.com/downloads/-/arm-performance-libraries).
Click the **Download Windows** section and download the Windows Installer:
`arm-performance-libraries_<version>_Windows.msi`

Double-click to open the installer and start the Arm Performance Libraries Setup Wizard.

![Arm Performance Libraries Setup Wizard welcome screen prompting user to select Next to begin the installation.#center](/install-guides/_images/armpl_wizard00.png)

Read and accept the End-User License Agreement by selecting the checkbox **I accept the terms of this License Agreement**.

![Arm Performance Libraries Setup Wizard showing the End-User License Agreement. A checkbox labeled 'I accept the terms of this License Agreement' is checked.#center](/install-guides/_images/armpl_wizard01.png)

Enter a location for the installation on your system. The default is:

`C:\Program Files\Arm Performance Libraries`

![Arm Performance Libraries Setup Wizard showing the installation directory field, set by default to C:\Program Files\Arm Performance Libraries. Change this path if needed before continuing.#center](/install-guides/_images/armpl_wizard02.png)

Click **Install** and then **Finish** to complete the installation.

![Arm Performance Libraries Setup Wizard is ready to install, prompting user to select Install to begin copying files to the specified directory.#center](/install-guides/_images/armpl_wizard03.png)

![Arm Performance Libraries Setup Wizard showing the installation is complete, prompting user to select Finish to exit the wizard.#center](/install-guides/_images/armpl_wizard04.png)

To install Arm Performance Libraries from a command prompt and automatically accept the End User License Agreement, run:
```console
msiexec.exe /i arm-performance-libraries_<version>_Windows.msi /quiet ACCEPT_EULA=1
```

To install Arm Performance Libraries using the `winget` package manager and automatically accept the End User License Agreement, run:
```console
winget install --accept-package-agreements Arm.ArmPerformanceLibraries
```

You can now start linking your application to the Arm Performance libraries on your Windows on Arm device. Follow the examples in the included `RELEASE_NOTES` file of your extracted installation directory to get started.

For more information, see [Get started with Arm Performance Libraries](https://developer.arm.com/documentation/109361).


## Install Arm Performance Libraries on macOS {#macos}

[Download](https://developer.arm.com/downloads/-/arm-performance-libraries) the appropriate package for your macOS distribution.

{{% notice Note %}}
The following commands use Arm Performance Libraries version 26.01. The same commands work with other versions. Replace the file used in these steps with the file for your version of choice. To find the latest version, see [Arm Performance Libraries downloads](https://developer.arm.com/downloads/-/arm-performance-libraries).
{{% /notice %}}

In a terminal, run the following command to download the macOS package:
```console
wget https://developer.arm.com/-/cdn-downloads/permalink/Arm-Performance-Libraries/Version_26.01/arm-performance-libraries_26.01_macOS.tgz
```

Use tar to extract the file:
```console
tar zxvf arm-performance-libraries_26.01_macOS.tgz
```

The output is similar to:
```console
armpl_26.01_flang-21.dmg
```

Mount the disk image by running the following command from a terminal:
```console
hdiutil attach armpl_26.01_flang-21.dmg
```

Now run the installation script as a superuser:

```console
/Volumes/armpl_26.01_flang-21_installer/armpl_26.01_flang-21_install.sh -y
```

Using this command, you automatically accept the End User License Agreement and install packages to the `/opt/arm` directory. If you want to change the installation directory location, use the `--install_dir=` option with the script and provide the desired directory location.

To install Arm Performance Libraries using Homebrew in a terminal and automatically accept the End User License Agreement, run:

```console
brew install arm-performance-libraries
```

The installer runs using `sudo`, so you may be asked to input your password.

To get started with Arm Performance Libraries on macOS, compile and test the examples in the `/opt/arm/<armpl_dir>/examples/` directory, or `<install_dir>/<armpl_dir>/examples/` if you installed to a different location.

For more information, see [Get started with Arm Performance Libraries](https://developer.arm.com/documentation/109362).

## Install Arm Performance Libraries on Linux {#linux}

Arm Performance Libraries are supported on most Linux distributions such as Ubuntu, RHEL, SLES, and Amazon Linux on an `AArch64` host. The libraries are compatible with various versions of GCC, LLVM, and NVHPC. The GCC-compatible releases are built with GCC 14 and tested with GCC versions 7 to 14. The LLVM-compatible releases are tested with LLVM 21.1. The NVHPC-compatible releases are tested with NVHPC 25.11.

### Manually download and install Arm Performance Libraries

Download the appropriate package for your Linux distribution. The `deb`-based installers can be used on Ubuntu 22 and Ubuntu 24. The RPM-based installers can be used on the following supported distributions:

- Amazon Linux 2, Amazon Linux 2023
- RHEL-8, RHEL-9, RHEL-10
- SLES-15 Service Packs 6 and 7

The following instructions are for `deb`-based installers for GCC users.

{{% notice Note %}}
The following commands use Arm Performance Libraries version 26.01. The same commands work with other versions. Replace the file used in these steps with the file for your version of choice. To find the latest version, see [Arm Performance Libraries downloads](https://developer.arm.com/downloads/-/arm-performance-libraries).
{{% /notice %}}

In a terminal, run the following command to download the Debian package:

```console
wget https://developer.arm.com/-/cdn-downloads/permalink/Arm-Performance-Libraries/Version_26.01/arm-performance-libraries_26.01_deb_gcc.tar
```

Use `tar` to extract the file and then change directory:

```console
tar xf arm-performance-libraries_26.01_deb_gcc.tar
```

Run the installation script as a super user:

```console
sudo ./arm-performance-libraries_26.01_deb/arm-performance-libraries_26.01_deb.sh --accept
```

Using the `--accept` switch, you automatically accept the End User License Agreement and the packages are installed to the `/opt/arm` directory.

If you want to change the installation directory location, use the `--install-to` option with the script and provide the desired directory location.

### Download and install Arm Performance Libraries using system packages

Arm Performance Libraries are available to install using Linux system package managers. The following instructions are for the Ubuntu system package manager `apt` command.

Add the Arm Performance Libraries `apt` package repository to your system:

```bash
. /etc/os-release
curl "https://developer.arm.com/packages/arm-toolchains:${NAME,,}-${VERSION_ID/%.*/}/${VERSION_CODENAME}/Release.key" | sudo tee /etc/apt/trusted.gpg.d/developer-arm-com.asc
echo "deb https://developer.arm.com/packages/arm-toolchains:${NAME,,}-${VERSION_ID/%.*/}/${VERSION_CODENAME}/ ./" | sudo tee /etc/apt/sources.list.d/developer-arm-com.list
sudo apt update
```

Download and install Arm Performance Libraries:

```bash
sudo apt install arm-performance-libraries
```

### Set up the environment for Arm Performance Libraries

Install environment modules on your Linux machine:

```console
sudo apt install environment-modules
```

Set your bash environment to use the modules:

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

The output is similar to:

```output
armpl/26.01.0_gcc
```

Load the appropriate module:

```console
module load armpl/26.01.0_gcc
```

To get started with Arm Performance Libraries on Linux, compile and test the examples in the `/opt/arm/<armpl_dir>/examples/` directory, or `<install_dir>/<armpl_dir>/examples/` if you installed to a different location.

For more information, see [Get started with Arm Performance Libraries](https://developer.arm.com/documentation/109362).

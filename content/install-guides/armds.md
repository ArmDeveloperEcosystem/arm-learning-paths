---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Arm Development Studio
description: Install Arm Development Studio on Windows or Linux and configure licensing for embedded C and C++ development, debug, and SoC validation.

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- compiler
- ide
- ArmDS
- success kits
- ssk

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 10

test_maintenance: false

author: Ronan Synnott

### Link to official documentation
official_docs: https://developer.arm.com/documentation/101469

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---
[Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio) is the most comprehensive embedded C/C++ dedicated software development solution. It is used for validation of SoC debug through emulation, simulation, FPGA, and silicon bring-up design and verification stages. It has the earliest support for all Arm processors and interconnects.

## What should I know before installing Arm Development Studio?

Arm Development Studio can be installed on Windows and Linux hosts.

Full host platform requirements are given in the [Getting Started Guide](https://developer.arm.com/documentation/101469/latest/Installing-and-configuring-Arm-Development-Studio/Hardware-and-host-platform-requirements).

## How do I download the installer packages?

The installer will depend on the [edition](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio#Editions) of Development Studio that you are entitled to.

The version is denoted by `year.index`, where `index` is a number (for example `2023.1`). You can also generate an Evaluation license from this installation (`Help` > `Arm License Manager`), with capabilities broadly similar to the UBL Gold Edition.

You can download the Development Studio installer from the [Product Download Hub](https://developer.arm.com/downloads/view/DS000B).

Versions of Arm Development Studio denoted by `year.index`, where `index` is a letter (for example `2023.a`) are only available to certain Arm licensees, as they contain support for non publicly announced IP (at time of release).

For more information about the Product Download Hub, refer to the [Product Download Hub guide](/install-guides/pdh/).

## How do I install Arm Development Studio?

### How do I install on Windows?

Unzip the downloaded `.zip` file.

To use the installation wizard, run `armds-2026.0-1-win-x86_64.msi` to open the Arm Development Studio setup wizard, then follow the on-screen instructions.

To install silently from the command line, open a command prompt with administrative privileges and run `msiexec` on the `.msi` file:
```command
msiexec /i armds-2026.0-1-win-x86_64.msi EULA=1 SKIP_DRIVERS=1 /qn
```
{{% notice Drivers %}}
This command does not install the debug probe USB drivers. If these are needed, remove `SKIP_DRIVERS=1` from the command. This requires manual interaction. You can also install them later by running `<install_dir>\sw\driver_files\driver_install.bat`.
{{% /notice %}}

Full installation instructions are provided in the [Arm Development Studio Getting Started Guide](https://developer.arm.com/documentation/101469/).
* [Install Arm Development Studio on Windows using the command line](https://developer.arm.com/documentation/101469/latest/Installing-and-configuring-Arm-Development-Studio/Install-Arm-Development-Studio-on-Windows-using-the-command-line)
* [Install Arm Development Studio on Windows using the installation wizard](https://developer.arm.com/documentation/101469/latest/Installing-and-configuring-Arm-Development-Studio/Install-Arm-Development-Studio-on-Windows-using-the-installation-wizard)

### How do I install on Linux?

The Linux installer is a single self-extracting `.sh` script. Make it executable and run it, following the on-screen instructions:

```command
chmod +x armds-2026.0-1-lin-x86_64.sh
./armds-2026.0-1-lin-x86_64.sh
```

To install silently from the command line, use a command similar to the following:

```command
./armds-2026.0-1-lin-x86_64.sh --i-agree-to-the-contained-eula --no-interactive -f -q
```

By default, the installer requires a post-install step that needs root privileges to install USB drivers for DSTREAM debug hardware. If you don't have root access, or don't need the drivers, add `--skip-post-install`. You can run the post-install step later as root:

```command
sudo <install_directory>/run_post_install_for_Arm_Development_Studio_2026.0-1.sh
```

{{% notice Libraries %}}
The installer runs a dependency check and lists any missing Linux libraries. Install these before using Arm Development Studio. The `dependency_check_linux-x86_64.sh` script in `<install_directory>/sw/dependency_check` identifies the required libraries. For more information, see [Additional Linux libraries](https://developer.arm.com/documentation/101469/latest/Installing-and-configuring-Arm-Development-Studio/Additional-Linux-libraries).
{{% /notice %}}

Full installation instructions are provided in the Linux section of the [Arm Development Studio Getting Started Guide](https://developer.arm.com/documentation/101469/latest/Installing-and-configuring-Arm-Development-Studio/Installing-on-Linux).

## How do I configure the command line?

### How do I configure the Windows command line?

You will see `Arm DS <version> Command Prompt` installed. This configures all necessary environment variables for use with the tools. You can select an appropriate toolchain with:
```command
select_toolchain
```
or set a default version with:
```command
select_default_toolchain
```
{{% notice Toolchains %}}
By default, only the supplied `Arm Toolchain for Embedded Professional` is installed with Arm Development Studio. Other versions can be installed and [registered](https://developer.arm.com/documentation/101469/latest/Installing-and-configuring-Arm-Development-Studio/Register-a-compiler-toolchain).
{{% /notice %}}

### How do I configure the Linux command line?

Navigate to the `bin` directory of your install, for example:
```command
cd $HOME/developmentstudio-2026.0-1/bin
```
Use `suite_exec` to start an appropriate command prompt, for example:
```command
./suite_exec --toolchain "Arm Toolchain for Embedded Professional" bash
```
To remove the need for the `--toolchain` option, first run:
```command
./select_default_toolchain
```
and select the desired toolchain. You can then configure with:
```command
./suite_exec bash
```
{{% notice Toolchains %}}
By default, only the supplied `Arm Toolchain for Embedded Professional` is installed with Arm Development Studio. Other versions can be installed and [registered](https://developer.arm.com/documentation/101469/latest/Installing-and-configuring-Arm-Development-Studio/Register-a-compiler-toolchain).
{{% /notice %}}

## How do I use the Arm Development Studio IDE?

Arm Development Studio is provided with a fully featured Eclipse based IDE and integrated debugger.

Launch the IDE from your desktop, or from the above prompt using:
```command
./armds_ide
```

## How do I set up the product license?

Arm Development Studio is license managed. When you launch the IDE for the first time, you should be prompted to set up your license if necessary. You can return to this view from `Help` > `Arm License Manager`.

A free 30 day evaluation license for Arm Development Studio is also available. You can generate this in `Arm License Manager`. Click on `Add`, and follow instructions therein to obtain the evaluation license (requires Arm login).

Full license setup instructions are available in the [Arm Software Licensing install guide](/install-guides/license/).

## How do I get started with Arm Development Studio?

To verify everything is working, configure a toolchain and run the compiler from your command prompt. On Linux:

```command
cd $HOME/developmentstudio-2026.0-1/bin
./suite_exec --toolchain "Arm Toolchain for Embedded Professional" bash -c "clang --version"
```

The output is similar to:

```output
Arm Toolchain for Embedded Professional 22.1.0 build 92, based on clang version 22.1.0
Target: aarch64-unknown-linux-gnu
Thread model: posix
InstalledDir: /home/ubuntu/developmentstudio-2026.0-1/sw/atfe-pro22.1.0/bin
```

{{% notice License %}}
The compiler reports its version without a license, but running it to build code requires a valid license. See [How do I set up the product license?](#how-do-i-set-up-the-product-license) to set up an evaluation or full license.
{{% /notice %}}

You should now be ready to use Arm Development Studio. See the [Get started with Arm Development Studio](/learning-paths/embedded-and-microcontrollers/armds/) learning path for more information.

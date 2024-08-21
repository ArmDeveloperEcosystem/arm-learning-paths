---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: CMSIS-Toolbox

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- cbuild
- keil
- mcu
- microcontroller
- cortex-m
- cmsis
- cmsis-build
- ci-cd

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

author_primary: Ronan Synnott

### Link to official documentation
official_docs: https://github.com/Open-CMSIS-Pack/cmsis-toolbox/blob/main/docs/README.md


### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---
The [CMSIS-Toolbox](https://github.com/Open-CMSIS-Pack/cmsis-toolbox) is a suite of utilities for creating, building, and managing projects based on CMSIS Software Packs.

It is also used for the creation and maintenance of such packs.

`CMSIS-Toolbox` is part of the [Open-CMSIS-Pack project](https://www.open-cmsis-pack.org).

Windows, Linux, and macOS host platforms are supported.

The below assumes Ubuntu Linux on an Arm based host. Instructions are similar for other platforms.

{{% notice Note %}}
This install guide is for manual installation of `CMSIS-Toolbox`.

For automation instructions using `vcpkg` see [Install tools on the command line using vcpkg](/learning-paths/microcontrollers/vcpkg-tool-installation/).

`CMSIS-Toolbox` is also installed as part of a Keil MDK installation (Windows only).
{{% /notice %}}

## Dependencies

You will need to install `cmake` and `ninja`:
```command
sudo apt update
sudo apt install cmake ninja-build -y
```
Check the versions of each tool:
```command
cmake --version
ninja --version
```
If `cmake` is earlier than `3.25.2`, or `ninja` is earlier than `1.10.2`, you will need to uninstall that version and install by other means:

#### cmake
```command
sudo apt remove -y cmake
sudo snap install cmake --classic
```
#### ninja
```command
sudo apt remove -y ninja-build
wget http://mirror.archlinuxarm.org/aarch64/extra/ninja-1.11.1-3-aarch64.pkg.tar.xz
sudo tar -xf ninja-1.11.1-3-aarch64.pkg.tar.xz -C /
```

## Download 

Download and unpack the latest version of `CMSIS-Toolbox` from the [Keil Artifactory](https://artifacts.keil.arm.com/cmsis-toolbox/).

Windows, Linux, and MacOS versions are available.

Full details of the contents is given in the [Releases area](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/releases) of the GitHub repository.

```console
wget https://artifacts.keil.arm.com/cmsis-toolbox/2.5.0/cmsis-toolbox-linux-arm64.tar.gz
tar -xf cmsis-toolbox-linux-arm64.tar.gz
```

## Install an appropriate compiler toolchain

Projects can be built with Arm Compiler for Embedded 6, Arm GNU Toolchain, LLVM Embedded Toolchain, or IAR tools.

For further setup instructions see these Install Guides:
* [Arm Compiler for Embedded](/install-guides/armclang)
* [Arm GNU Toolchain](/install-guides/gcc/arm-gnu)
* [LLVM Embedded Toolchain for Arm](/install-guides/llvm-embedded/)

`Arm Compiler for Embedded` is used in the example below.

## Set up environment variables

Set environment variables as below. Note the exact name of the `TOOLCHAIN` variables will be based on the tool and version installed. In this way, multiple build tools can be registered.

| Variable                                   | Description                           | Notes                                         |
| ------------------------------------------ | ------------------------------------- | --------------------------------------------- |
| `<name>_TOOLCHAIN_<major>_<minor>_<patch>` | Path to toolchain binaries            | `<name>` = `AC6`, `GCC`, `IAR`, or `CLANG`    |
| `CMSIS_PACK_ROOT`                          | Path to CMSIS-Pack root directory     | Use `cpackget init` to initialize             |
| `CMSIS_COMPILER_ROOT`                      | Path to CMSIS-Toolbox `etc` directory |                                               |
| `PATH`                                     | Add CMSIS-Toolbox `bin` to path       | Also path to `CMake` and `Ninja` if necessary |

For example:
```command
export AC6_TOOLCHAIN_6_22_0=$HOME/ArmCompilerforEmbedded6.22/bin
export CMSIS_PACK_ROOT=$HOME/packs
export CMSIS_COMPILER_ROOT=$HOME/cmsis-toolbox-linux-arm64/etc
export PATH=$HOME/cmsis-toolbox-linux-arm64/bin:$PATH
```

## Initialize CMSIS-Pack directory

To get the latest available packs, run the following command.
```command
cpackget init https://www.keil.com/pack/index.pidx
```

`CMSIS-Toolbox` should now be ready for use.

## Test setup {#test}

Example projects are provided on the [GitHub repository](https://github.com/Open-CMSIS-Pack/csolution-examples).

Clone the following repository to your build machine:
```command
git clone https://github.com/Open-CMSIS-Pack/csolution-examples
```

Navigate to the `Hello` example:
```command
cd csolution-examples/Hello
```

### Install CMSIS-Packs

Determine and install the necessary `CMSIS-Packs`:

```command
csolution list packs -s Hello.csolution.yml -m > packs.txt
cpackget add -f packs.txt
```

### Build the solution

Use the `cbuild` utility to build.

```command
cbuild Hello.csolution.yml
```

The build will proceed and generate an executable image(s). You will see output similar to:

```output
(1/2) Building context: "Hello.Debug+AVH"
Building CMake target 'Hello.Debug+AVH'
[1/31] Building C object CMakeFiles/Group_Main.dir/home/ubuntu/csolution-examples/Hello/main.o
...
[31/31] Linking C executable /home/ubuntu/csolution-examples/Hello/out/Hello/AVH/Debug/Hello.axf
Program Size: Code=29968 RO-data=1584 RW-data=244 ZI-data=37072
+------------------------------------------
(2/2) Building context: "Hello.Release+AVH"
Building CMake target 'Hello.Release+AVH'
[1/31] Building C object CMakeFiles/Group_App.dir/home/ubuntu/csolution-examples/Hello/hello.o
...
[31/31] Linking C executable /home/ubuntu/csolution-examples/Hello/out/Hello/AVH/Release/Hello.axf
Program Size: Code=17664 RO-data=988 RW-data=196 ZI-data=37112
+------------------------------------------------------------
Build summary: 2 succeeded, 0 failed - Time Elapsed: 00:00:03
+============================================================
```

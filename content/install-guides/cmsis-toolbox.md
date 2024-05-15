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
If `cmake` is earlier than 3.25.2, or `ninja` is earlier than 1.10.2, you will need to uninstall that version and install by other means:

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

Download and unpack the latest install file from GitHub. Downloads are provided in the [Releases area](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/releases) of the repository.

```console
wget https://github.com/Open-CMSIS-Pack/cmsis-toolbox/releases/download/2.2.0/cmsis-toolbox-linux-arm64.tar.gz
tar -xf cmsis-toolbox-linux-arm64.tar.gz
```

## Install the appropriate compiler toolchain

Projects can be built with Arm Compiler for Embedded, Arm GNU Toolchain, or IAR tools.

For further setup instructions see these Install Guides:
* [Arm Compiler for Embedded](../armclang)
* [Arm GNU Toolchain](../gcc/arm-gnu)

Arm Compiler for Embedded is installed below.

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
export AC6_TOOLCHAIN_6_21=$HOME/ArmCompilerforEmbedded6.21/bin
export CMSIS_PACK_ROOT=$HOME/packs
export CMSIS_COMPILER_ROOT=$HOME/cmsis-toolbox-linux-arm64/etc
export PATH=$HOME/cmsis-toolbox-linux-arm64/bin:$PATH
cpackget init https://www.keil.com/pack/index.pidx
```

## Test setup {#test}

Example projects are provided on the [GitHub repository](https://github.com/Open-CMSIS-Pack/csolution-examples).

Clone the repository to your build machine:
```command
git clone https://github.com/Open-CMSIS-Pack/csolution-examples
```

Navigate to the `Hello` example:
```command
cd csolution-examples/Hello
```

### Set up the build

Determine and install the necessary CMSIS-Packs for the project:
```command
csolution list packs -s Hello.csolution.yml -m >packs.txt
cpackget add -f packs.txt
```

### Generate .cprj project file(s)

Generate `cprj` project files for build targets within the solution project.
```command
csolution convert -s Hello.csolution.yml
```

### Build a generated project
Use the `cbuild` utility to build a project.
```command
cbuild Hello.Release+AVH.cprj
```
The build will proceed and generate an executable image:
```output
info cbuild: Build Invocation 2.2.0 (C) 2023 Arm Ltd. and Contributors

M650: Command completed successfully.

M652: Generated file for project build: '/home/ubuntu/csolution-examples/Hello/tmp/Hello/AVH/Release/CMakeLists.txt'
-- The ASM compiler identification is ARMClang
-- Found assembler: /home/ubuntu/ArmCompilerforEmbedded6.21/bin/armclang
-- The C compiler identification is ARMClang 6.21
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /home/ubuntu/ArmCompilerforEmbedded6.21/bin/armclang - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Configuring done (0.6s)
-- Generating done (0.0s)
-- Build files have been written to: /home/ubuntu/csolution-examples/Hello/tmp/Hello/AVH/Release
[1/27] Building ASM object CMakeFiles/Hello.dir/home/ubuntu/packs/ARM/CMSIS/5.9.0/CMSIS/RTOS2/RTX/Source/GCC/irq_armv8mml.o
...
[27/27] Linking C executable /home/ubuntu/csolution-examples/Hello/out/AVH/Hello.axf
info cbuild: build finished successfully!
```

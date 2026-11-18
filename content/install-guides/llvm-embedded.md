---
title: Arm Toolchain for Embedded
description: Install Arm Toolchain for Embedded on Windows, macOS, or Linux and verify clang for bare-metal Arm embedded development.

additional_search_terms:
- clang
- llvm
- compiler
- open source
- cortex-m
- ATfE
- LLVM Embedded Toolchain

minutes_to_complete: 10

official_docs: https://github.com/arm/arm-toolchain/blob/arm-software/arm-software/embedded/README.md

author: Ronan Synnott

weight: 1
tool_install: true
multi_install: false
multitool_install_part: false
layout: installtoolsall
---

Arm Toolchain for Embedded (ATfE) is a free, open-source LLVM-based toolchain for bare-metal Arm development. It targets Cortex-M, Cortex-R, and Cortex-A processors from Armv6-M and newer, and includes `clang`, `lld`, `libc++`, `compiler-rt`, and `picolibc`.

ATfE is the successor to the LLVM Embedded Toolchain for Arm. The [LLVM Embedded Toolchain for Arm repository](https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm) is deprecated; use ATfE for LLVM 20 and later.

Pre-built binaries are available for Windows (x86_64), macOS (universal), and Linux (x86_64 and AArch64) hosts.

{{% notice Toolchain version %}}
The following steps use Arm Toolchain for Embedded version 22.1.0. The same steps work with other versions. Replace the version number in file names and URLs with your version of choice. To find the latest version, see [Arm Toolchain releases](https://github.com/arm/arm-toolchain/releases).
{{% /notice %}}

## Install Arm Toolchain for Embedded on Windows {#windows}

To download the latest release from GitHub, copy and paste the following URL into your browser:

```console
https://github.com/arm/arm-toolchain/releases/download/release-22.1.0-ATfE/ATfE-22.1.0-Windows-x86_64.zip
```

Extract the zip file to a location of your choice on your host machine.

Open Windows **Control Panel** and add the ATfE `bin` directory to the **Path**.

Open a **Command Prompt** and [test your installation](#test).

## Install Arm Toolchain for Embedded on macOS {#macos}

To download the latest release from GitHub, copy and paste the following URL into your browser:

```console
https://github.com/arm/arm-toolchain/releases/download/release-22.1.0-ATfE/ATfE-22.1.0-Darwin-universal.dmg
```

Install the toolchain by opening the `.dmg` file and following the instructions.

Add the ATfE `bin` directory to your `PATH`:

```command
export PATH=/Applications/ATfE-22.1.0-Darwin-universal/bin:$PATH
```

The toolchain binaries might be quarantined. Navigate to the `bin` directory and use the `xattr` command to remove the quarantine:

```command
cd /Applications/ATfE-22.1.0-Darwin-universal/bin
find . -type f -perm +0111 | xargs xattr -d com.apple.quarantine
```

You can now [test your installation](#test).

## Install Arm Toolchain for Embedded on Linux {#linux}

The following steps assume Ubuntu Linux on an AArch64 host. Modify the filenames and paths as needed for other hosts or x86_64 systems.

Download the latest release using `wget`:

```command
wget https://github.com/arm/arm-toolchain/releases/download/release-22.1.0-ATfE/ATfE-22.1.0-Linux-AArch64.tar.xz
```

Use `tar` to extract the file:

```command
tar xfJ ATfE-22.1.0-Linux-AArch64.tar.xz -C $HOME
```

Add the ATfE `bin` directory to your `PATH`:

```command
export PATH=$HOME/ATfE-22.1.0-Linux-AArch64/bin:$PATH
```

## Test the installation {#test}

### Verify the clang installation

Use the `--version` option to verify the correct compiler is being invoked:

```command
clang --version
```

The output is similar to:

```output
clang version 22.1.0
Target: aarch64-unknown-linux-gnu
Thread model: posix
InstalledDir: /home/ubuntu/ATfE-22.1.0-Linux-AArch64/bin
Arm Toolchain ID: E0075 (44010d72)
```

### Build a sample application with clang

Use a text editor to create an example source file named `hello.c` with the following code:

```c
#include <stdio.h>

int main()
{
  printf("hello");
  return 0;
}
```

Several compiler options are needed. For more information, see [Using the toolchain](https://github.com/arm/arm-toolchain/blob/arm-software/embedded/README.md#using-the-toolchain).

To build for Armv6-M, run:

```command
clang --target=armv6m-none-eabi -fno-exceptions -fno-rtti -lcrt0-semihost -lsemihost -T picolibc.ld -o hello_v6m hello.c
```

To build for Armv7-M, run:

```command
clang --target=armv7m-none-eabi -fno-exceptions -fno-rtti -lcrt0-semihost -lsemihost -T picolibc.ld -o hello_v7m hello.c
```

### Run the example applications

The applications can be run on [Fixed Virtual Platforms (FVP)](/install-guides/fm_fvp/fvp/).

{{% notice Note %}}
There is no FVP release for macOS.
{{% /notice %}}

To run the Armv6-M example on a Cortex-M0 FVP:

```command
FVP_MPS2_Cortex-M0 -a hello_v6m
```

To run the Armv7-M example on a Cortex-M3 FVP:

```command
FVP_MPS2_Cortex-M3 -a hello_v7m
```

The output includes the `hello` message along with diagnostic output from the FVP:

```output
telnetterminal1: Listening for serial connection on port 5000
telnetterminal2: Listening for serial connection on port 5002
telnetterminal0: Listening for serial connection on port 5001
hello
Info: /OSCI/SystemC: Simulation stopped by user.
```

You're now ready to use Arm Toolchain for Embedded.

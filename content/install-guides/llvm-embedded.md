---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: LLVM Embedded Toolchain for Arm

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- clang
- llvm
- compiler
- open source
- cortex-m

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 10

### Link to official documentation
official_docs: https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm

author_primary: Ronan Synnott

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

The [LLVM Embedded Toolchain for Arm](https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm) allows Cortex-M developers to build projects with the `clang` compiler.

[Pre-built binaries](https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm/releases) are available for Windows (x86_64), macOS (x86_64 and Apple Silicon), and Linux (x86_64 and AArch64) hosts. 

## Windows {#windows}

Copy and paste the URL below into your browser to download the latest release from GitHub:

```url
https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm/releases/download/release-16.0.0/LLVMEmbeddedToolchainForArm-16.0.0-Windows-x86_64.zip
```

Unzip the download to a location of your choice on your host machine.

Open Windows `Control Panel` and add the LLVM `bin` directory to the `Path`.

Open a `Command Prompt` and [test your installation](#test).

## macOS {#macos}

Copy and paste the URL below into your browser to download the latest release from GitHub:

```url
https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm/releases/download/release-16.0.0/LLVMEmbeddedToolchainForArm-16.0.0-Darwin.tar.gz
```

Open a terminal application and use `tar` to extract the file:

```command
tar -xf ~/Downloads/LLVMEmbeddedToolchainForArm-16.0.0-Darwin.tar.gz -C $HOME
```

Add the LLVM `bin` directory to your `PATH`:

```command
export PATH=$HOME/LLVMEmbeddedToolchainForArm-16.0.0-Darwin/bin:$PATH
```

The toolchain binaries may be quarantined. Navigate to the `bin` directory and use the `xattr` command to remove the quarantine: 

``` command
cd $HOME/LLVMEmbeddedToolchainForArm-16.0.0-Darwin/bin
find . -type f -perm +0111 | xargs xattr -d com.apple.quarantine
```

You can now [test your installation](#test).

## Linux {#linux}

The information below assumes `Ubuntu Linux` on an `AArch64` host. Modify the filenames and paths as needed for other hosts.

Download the latest release using `wget`: 

```command
wget https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm/releases/download/release-16.0.0/LLVMEmbeddedToolchainForArm-16.0.0-Linux-AArch64.tar.gz
```

Open a terminal application and use `tar` to extract the file:

```command
tar -xf LLVMEmbeddedToolchainForArm-16.0.0-Linux-AArch64.tar.gz -C $HOME
```

Add the LLVM `bin` directory to your `PATH`:

```command
export PATH=$HOME/LLVMEmbeddedToolchainForArm-16.0.0-Linux-AArch64/bin:$PATH
```

Install the required library `libtinfo5`:

``` command
sudo apt install -y libtinfo5
```

You can now [test your installation](#test).

## Test installation {#test}

### Verify the clang installation

Use the `--version` option to verify the correct compiler is being invoked:

```command
clang --version
```

You should observe output similar to:

```output
clang version 16.0.0
Target: aarch64-unknown-linux-gnu
Thread model: posix
InstalledDir: /home/ubuntu/LLVMEmbeddedToolchainForArm-16.0.0-Linux-AArch64/bin
```

### Build a simple application

Use a text editor to create an example source file with the name `hello.c` and the code below:

```C
#include <stdio.h>

int main()
{
  printf("hello");
  return 0;
}
```

A number of compiler options are needed. See [Using the toolchain](https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm#using-the-toolchain) for full details.

To build for `Armv6-M`:

```command
clang --target=armv6m-none-eabi -fno-exceptions -fno-rtti -lcrt0-semihost -lsemihost -T picolibc.ld -o hello_v6m hello.c
```

To build for `Armv7-M`:

```
clang --target=armv7m-none-eabi -fno-exceptions -fno-rtti -lcrt0-semihost -lsemihost -T picolibc.ld -o hello_v7m hello.c
```

### Run the examples

The applications can be run on [Fixed Virtual Platforms (FVP)](/install-guides/fm_fvp/fvp/). 

{{% notice Note %}}
There is no FVP release for macOS.
{{% /notice %}}

To run the `Armv6-M` example on `Cortex-M0` FVP:

```command
FVP_MPS2_Cortex-M0 -a hello_v6m
```

To run the `Armv7-M` example on `Cortex-M3` FVP:

```command
FVP_MPS2_Cortex-M3 -a hello_v7m
```

You will see the `hello` message on the console (as well as other diagnostic output from the FVP):

```output
telnetterminal1: Listening for serial connection on port 5000
telnetterminal2: Listening for serial connection on port 5002
telnetterminal0: Listening for serial connection on port 5001
hello
Info: /OSCI/SystemC: Simulation stopped by user.
```

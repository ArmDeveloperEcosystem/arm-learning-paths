---
title: LLVM toolchain for Linux on Arm

additional_search_terms:
- llvm
- clang
- compiler
- lld
- pgo
- lto
- profdata
- profgen

minutes_to_complete: 10

author: Paschalis Mpeis

official_docs: https://releases.llvm.org/download.html
description: Install the LLVM toolchain on Arm Linux to use Clang, LLD, and profiling utilities.

test_images:
- ubuntu:latest
test_maintenance: false

layout: installtoolsall
tool_install: true
multi_install: false
multitool_install_part: false
weight: 1
---

The LLVM toolchain includes Clang, LLD, and other LLVM utilities for compiling, linking, and optimizing applications.

In this guide, you’ll learn how to download, extract, and install the LLVM toolchain from a prebuilt binary release on Arm Linux.

## Before you begin

Confirm you are using an Arm machine by running:

Run:

```bash
uname -m
```

The output is similar to:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

Install the tools needed to download and extract the archive.
For Debian-based Linux distributions, including Ubuntu, install `wget` and `xz-utils`:


```bash { target="ubuntu:latest" }
sudo apt update
sudo apt install wget xz-utils -y
```

## Install LLVM

You can install LLVM by downloading a prebuilt binary release from GitHub.

The following commands use LLVM version 22.1.8. To install a different version, replace the filename in the commands below. For the latest releases, see [LLVM Project releases](https://github.com/llvm/llvm-project/releases).

The commands extract LLVM to `$HOME/toolchain`. To install LLVM in a different location, adjust the extraction path and update the PATH environment variable accordingly.

1. Download a binary release

For Arm Linux, use the archive with `Linux-ARM64` in its filename:


```bash
mkdir -p $HOME/toolchain
cd $HOME/toolchain
wget https://github.com/llvm/llvm-project/releases/download/llvmorg-22.1.8/LLVM-22.1.8-Linux-ARM64.tar.xz
```

2. Extract the downloaded file

```bash
tar -xvf LLVM-22.1.8-Linux-ARM64.tar.xz
```

3. Add the LLVM `bin` directory to your `PATH`

This enables you to run LLVM tools such as `clang` and `lld` from any directory.
The command updates `PATH` for your current terminal session.
To make the change persistent, add the same command to your shell profile, such as `~/.bashrc`.

```bash
export PATH="$HOME/toolchain/LLVM-22.1.8-Linux-ARM64/bin:$PATH"
```
## Verify LLVM is installed {#verify}

Run the following commands:

```console
clang --version
clang++ --version
ld.lld --version
```

The output is similar to:

```output
clang version 22.1.8 (https://github.com/llvm/llvm-project ca7933e47d3a3451d81e72ac174dcb5aa28b59d1)
Target: aarch64-unknown-linux-gnu
Thread model: posix
InstalledDir: /home/ubuntu/toolchain/LLVM-22.1.8-Linux-ARM64/bin

clang version 22.1.8 (https://github.com/llvm/llvm-project ca7933e47d3a3451d81e72ac174dcb5aa28b59d1)
Target: aarch64-unknown-linux-gnu
Thread model: posix
InstalledDir: /home/ubuntu/toolchain/LLVM-22.1.8-Linux-ARM64/bin

LLD 22.1.8 (https://github.com/llvm/llvm-project ca7933e47d3a3451d81e72ac174dcb5aa28b59d1) (compatible with GNU linkers)
```

Each command should print LLVM version information.

## Compile and run a C++ example

Use a text editor to copy and paste the following code into a file named `hello.cpp`:

```cpp { file_name="hello.cpp" }
#include <iostream>

int main()
{
    std::cout << "Hello, LLVM on Arm\n";
    return 0;
}
```

Compile the example with `clang++` and link it with LLD:

```bash
clang++ -fuse-ld=lld hello.cpp -o hello
```

Run the example:

```bash
./hello
```

The output is:

```output
Hello, LLVM on Arm
```

You are now ready to use LLVM on your Arm Linux system.

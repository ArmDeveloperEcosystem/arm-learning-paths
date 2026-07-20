---
title: BOLT

additional_search_terms:
- linux
- optimization
- PGO

minutes_to_complete: 20

author: Jonathan Davies

official_docs: https://github.com/llvm/llvm-project/tree/main/bolt
description: Install BOLT on Linux AArch64 to optimize binary code layout using performance profiles and improve the runtime performance of large applications on Arm.

test_images:
- ubuntu:latest
test_maintenance: true

layout: installtoolsall
tool_install: true
multi_install: false
multitool_install_part: false
weight: 1
---

BOLT is an open-source post-link binary optimization tool developed to speed up large applications. It does this by optimizing the application's code layout based on performance profile samples collected during execution.

In this guide, you'll learn how to download and install BOLT. The instructions are for Debian-based Linux distributions, but can be adapted for other Linux distributions.

{{% notice Note %}}
BOLT is provided as a built-in, ready-to-use component of the [Arm Toolchain for Linux](https://developer.arm.com/documentation/110477) suite. For more
information, see [How to use BOLT with our toolchain](https://developer.arm.com/documentation/110477/211/How-to-use-BOLT-with-our-toolchain).
{{% /notice %}}

## Before you begin

Follow these steps:

1. Install Git

[Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for your operating system.

Many Linux distributions include Git so you may not need to install it.

2. Install CMake

```bash { target="ubuntu:latest" }
sudo apt install cmake -y
```

Check it is installed:

```bash { target="ubuntu:latest" }
cmake --version
```

The output is similar to:

```output
cmake version 3.28.3

CMake suite maintained and supported by Kitware (kitware.com/cmake).
```

For more information, see [CMake install guide.](/install-guides/cmake/)

3. Install Ninja

```bash { target="ubuntu:latest" }
sudo apt install ninja-build -y
```

Check it is installed:

```bash { target="ubuntu:latest" }
ninja --version
```

The output is similar to:

```output
1.11.1
```

4. Install Clang

```bash { target="ubuntu:latest" }
sudo apt install clang -y
```

Check it is installed:

```bash { target="ubuntu:latest" }
clang --version
```

The output is similar to:

```output
Ubuntu clang version 18.1.3 (1ubuntu1)
Target: aarch64-unknown-linux-gnu
Thread model: posix
InstalledDir: /usr/bin
```

5. Install xz-utils

```bash
sudo apt-get install xz-utils -y
```

## Install BOLT

You can install BOLT by building the source code or by downloading a binary release from GitHub.

### Build and install BOLT from source code

To build and install BOLT from source code, follow these steps:

1. Clone the repository

```bash
git clone https://github.com/llvm/llvm-project.git
```

2. Build BOLT and run it

```bash
cd llvm-project
mkdir build
cd build
cmake -G Ninja ../llvm -DLLVM_TARGETS_TO_BUILD="X86;AArch64" -DCMAKE_BUILD_TYPE=Release -DLLVM_ENABLE_ASSERTIONS=ON -DLLVM_ENABLE_PROJECTS="bolt;clang;lld"
```

```console
ninja bolt
```
{{% notice Note %}}
The build time depends on your machine configuration and may take several minutes to complete.
{{% /notice %}}

3. Add the path to BOLT in your `.bashrc` file

```bash
echo 'export PATH="$PATH:$HOME/llvm-project/build/bin"' >> ~/.bashrc
source ~/.bashrc
```

You are now ready to [verify BOLT is installed](#verify).

### Install BOLT using a binary release

To install BOLT using a binary release, follow these steps:

{{% notice Note %}}
The following commands use BOLT version 22.1.3. The same commands work with other versions. Replace the file used in these steps with the file for your version of choice. To find the latest version, see [LLVM Project releases](https://github.com/llvm/llvm-project/releases).
{{% /notice %}} 

1. Download a binary release

For Arm Linux, use the file with `ARM64` in the name:

```bash
wget https://github.com/llvm/llvm-project/releases/download/llvmorg-22.1.3/LLVM-22.1.3-Linux-ARM64.tar.xz
```

2. Extract the downloaded file

```bash
tar -xvf LLVM-22.1.3-Linux-ARM64.tar.xz
```

3. Add the path to BOLT in your `.bashrc` file

```bash
echo 'export PATH="$PATH:$HOME/LLVM-22.1.3-Linux-ARM64/bin"' >> ~/.bashrc
source ~/.bashrc
```

### Verify BOLT is installed {#verify}

To verify BOLT is installed, follow these steps:

1. Confirm BOLT applications `perf2bolt` and `llvm-bolt` are installed

Check the `perf2bolt` command:

```console
perf2bolt
```

The output is similar to:

```output
perf2bolt: Not enough positional command line arguments specified!
Must specify at least 1 positional argument: See: perf2bolt --help
```

Check the `llvm-bolt` command:

```console
llvm-bolt
```

The output is similar to: 

```output
llvm-bolt: Not enough positional command line arguments specified!
Must specify at least 1 positional argument: See: llvm-bolt --help
```

2. Print the BOLT version

```console
llvm-bolt --version
```

The output is similar to:

```output
LLVM (http://llvm.org/):
  LLVM version 22.1.3
  Optimized build.
BOLT revision e9846648fd6183ee6d8cbdb4502213fcf902a211

  Registered Targets:
    aarch64    - AArch64 (little endian)
    aarch64_32 - AArch64 (little endian ILP32)
    aarch64_be - AArch64 (big endian)
    arm64      - ARM64 (little endian)
    arm64_32   - ARM64 (little endian ILP32)
    riscv32    - 32-bit RISC-V
    riscv32be  - 32-bit big endian RISC-V
    riscv64    - 64-bit RISC-V
    riscv64be  - 64-bit big endian RISC-V
    x86        - 32-bit X86: Pentium-Pro and above
    x86-64     - 64-bit X86: EM64T and AMD64
```

You'll see additional Registered Targets if you downloaded a binary release.

You are now ready to use BOLT on your Linux machine.

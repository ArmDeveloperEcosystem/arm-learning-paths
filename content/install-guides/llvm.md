---
title: LLVM toolchain for Linux on Arm

additional_search_terms:
- bolt
- llvm-bolt
- perf2bolt
- llvm
- clang
- compiler
- lld
- pgo
- lto
- profdata
- profgen

minutes_to_complete: 10

author: Paschalis Mpeis, Jonathan Davies

official_docs: https://releases.llvm.org/download.html
description: Install the LLVM toolchain on Arm Linux to use Clang, LLD, BOLT, and profiling utilities.

test_images:
- ubuntu:latest
test_maintenance: false

layout: installtoolsall
tool_install: true
multi_install: false
multitool_install_part: false
weight: 1
---

The LLVM toolchain includes Clang, LLD, BOLT, and other utilities for compiling, linking, profiling, and optimizing applications on Arm Linux.

In this guide, you’ll learn how to install LLVM from a prebuilt release or from source, install BOLT from Linux distribution packages, and verify the installed tools.

{{% notice Note %}}
BOLT is provided as a built-in, ready-to-use component of the [Arm Toolchain for Linux](https://developer.arm.com/documentation/110477) suite. For more
information, see [How to use BOLT with our toolchain](https://developer.arm.com/documentation/110477/211/How-to-use-BOLT-with-our-toolchain).
{{% /notice %}}

## Before you begin {#before-you-begin}

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

There are three ways to install the LLVM tools covered in this guide:

- [Install LLVM from a prebuilt release](#install-llvm-releases) to install Clang, LLD, BOLT, and the LLVM profiling tools.
- [Build LLVM from source](#build-llvm-source) if you need to build the LLVM toolchain yourself.
- [Install BOLT using a package manager](#install-bolt-packages) if you only need the BOLT tools and your Linux distribution provides a suitable version.

## Install from LLVM Releases {#install-llvm-releases}

You can install LLVM by downloading a prebuilt binary release from GitHub.

Install the tools needed to download and extract the archive.
For Debian-based Linux distributions, including Ubuntu, install `wget` and `xz-utils`:

```bash { target="ubuntu:latest" }
sudo apt update
sudo apt install wget xz-utils -y
```

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

## Install from Sources {#build-llvm-source}

### Install source build dependencies

Before building LLVM from source, install the required build tools.

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

### Build BOLT from source {#build-bolt-source}

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

After the build completes, continue to [verify the BOLT tools](#verify-bolt-tools).

## Install BOLT using a package manager {#install-bolt-packages}

Use a package manager if you prefer a system-managed installation. Package versions depend on your Linux distribution.

{{< tabpane code=true >}}

{{< tab header="Ubuntu/Debian" language="bash">}}
sudo apt update
sudo apt install llvm-bolt
{{< /tab >}}

{{< tab header="Fedora" language="bash">}}
sudo dnf install llvm-bolt
{{< /tab >}}

{{< tab header="openSUSE" language="bash">}}
sudo zypper install llvm-bolt
{{< /tab >}}

{{< /tabpane >}}

BOLT is available on Ubuntu 25.04 and later, Debian 13 and later, Fedora 42 and later, and on openSUSE Tumbleweed

## Verify Clang compiler and LLD linker tools {#verify-compiler-tools}

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

### Compile and run a C++ example {#compile-cpp-example}

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


## Verify the PGO profiling tools {#verify-pgo-tools}

Run the following commands:

```console
llvm-profdata --version
llvm-profgen --version
```

Each command should print LLVM version information.

## Verify BOLT tools {#verify-bolt-tools}

Run the following commands:

```console
perf2bolt --version
llvm-bolt --version
```

The output is similar to:

```output
LLVM (http://llvm.org/):
  LLVM version 22.1.8
  Optimized build.
```

Each command should print LLVM version information.

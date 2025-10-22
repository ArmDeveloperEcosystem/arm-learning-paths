---
title: BOLT

additional_search_terms:
- linux
- optimization
- PGO

minutes_to_complete: 20

author: Jonathan Davies

official_docs: https://github.com/llvm/llvm-project/tree/main/bolt

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

## What do I need before installing BOLT?

This article provides quick instructions to download and install BOLT. The instructions are for Debian-based Linux distributions, but can be adapted for other Linux distributions.

{{% notice Note %}}
The [Arm Toolchain for Linux](https://developer.arm.com/documentation/110477)
provides a ready to use BOLT as an integral part of the suite. For more
information refer to [this guide](https://developer.arm.com/documentation/110477/211/How-to-use-BOLT-with-our-toolchain).
{{% /notice %}}

1. Install Git

[Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) using the documentation for your operating system.

Many Linux distributions include Git so you may not need to install it.

2. Install CMake

```bash { target="ubuntu:latest" }
sudo apt install cmake -y
```

Check it is installed:

```bash { target="ubuntu:latest" }
cmake --version
```

The version is printed:

```output
cmake version 3.22.1

CMake suite maintained and supported by Kitware (kitware.com/cmake).
```

For more information refer to the [CMake install guide.](/install-guides/cmake)

3. Install Ninja

```bash { target="ubuntu:latest" }
sudo apt install ninja-build -y
```

Check it is installed:

```bash { target="ubuntu:latest" }
ninja --version
```

The version is printed:

```output
1.10.0
```

4. Install Clang

```bash { target="ubuntu:latest" }
sudo apt install clang -y
```

Check it is installed:

```bash { target="ubuntu:latest" }
clang --version
```

The version is printed:

```output
Ubuntu clang version 14.0.0-1ubuntu1.1
Target: aarch64-unknown-linux-gnu
Thread model: posix
InstalledDir: /usr/bin
```

5. Install xz-utils

```bash
sudo apt-get install xz-utils -y
```

## How do I install BOLT?

You can install BOLT in 2 different ways, by building the source code or by downloading a binary release from GitHub.

### How do I build and install BOLT from source code?

1. Clone the repository

```bash
git clone https://github.com/llvm/llvm-project.git
```

2. Build BOLT and run it.

```bash
cd llvm-project
mkdir build
cd build
cmake -G Ninja ../llvm -DLLVM_TARGETS_TO_BUILD="X86;AArch64" -DCMAKE_BUILD_TYPE=Release -DLLVM_ENABLE_ASSERTIONS=ON -DLLVM_ENABLE_PROJECTS="bolt;clang;lld"
```

```console
ninja bolt
```

Build time depends on your machine configuration, and it may take several minutes to complete.

3. Add the path to BOLT in your `.bashrc` file

```bash
echo 'export PATH="$PATH:$HOME/llvm-project/build/bin"' >> ~/.bashrc
source ~/.bashrc
```

You are now ready to [verify BOLT is installed](#verify).

### How do I install BOLT using a binary release?

1. Download a binary release

For Arm Linux use the file with `aarch64` in the name:

```bash
wget https://github.com/llvm/llvm-project/releases/download/llvmorg-19.1.7/clang+llvm-19.1.7-aarch64-linux-gnu.tar.xz
```

2. Extract the downloaded file

```bash
tar -xvf clang+llvm-19.1.7-aarch64-linux-gnu.tar.xz
```

3. Add the path to BOLT in your `.bashrc` file

```bash
echo 'export PATH="$PATH:$HOME/clang+llvm-19.1.7-aarch64-linux-gnu/bin"' >> ~/.bashrc
source ~/.bashrc
```

### How do I verify BOLT is installed? {#verify}

1. Confirm BOLT applications `perf2bolt` and `llvm-bolt` are installed

Check the `perf2bolt` command:

```console
perf2bolt
```

The expected output is:

```output
perf2bolt: Not enough positional command line arguments specified!
Must specify at least 1 positional argument: See: perf2bolt --help
```

Check the `llvm-bolt` command:

```console
llvm-bolt
```

The expected output is:

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
  LLVM version 19.1.7
  Optimized build with assertions.

  Registered Targets:
    aarch64    - AArch64 (little endian)
    aarch64_32 - AArch64 (little endian ILP32)
    aarch64_be - AArch64 (big endian)
    arm64      - ARM64 (little endian)
    arm64_32   - ARM64 (little endian ILP32)
    x86        - 32-bit X86: Pentium-Pro and above
    x86-64     - 64-bit X86: EM64T and AMD64
```

You will see additional Registered Targets if you downloaded a binary release.

You are ready to use BOLT on your Linux machine.

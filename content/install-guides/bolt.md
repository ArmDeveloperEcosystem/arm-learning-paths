---
title: BOLT

additional_search_terms:
- linux
- optimization
- PGO

minutes_to_complete: 20

author_primary: Jonathan Davies

official_docs: https://github.com/llvm/llvm-project/tree/main/bolt

test_images:
- ubuntu:latest
test_maintenance: false

layout: installtoolsall
tool_install: true
multi_install: false
multitool_install_part: false
weight: 1
---

BOLT is an open-source post-link binary optimization tool developed to speed up large applications. It does this by optimizing the application's code layout based on performance profile samples collected during execution.

## Before you begin

This article provides quick instructions to download and install BOLT. The instructions are for Debian-based Linux distributions, but can be adapted for other Linux distributions.

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

## Install BOLT

You can install BOLT in 2 different ways, by building the source code or by downloading a binary release from GitHub. 

### Option 1: Download, build, and install BOLT from source code

1. Clone the repository

```console
cd $HOME
git clone https://github.com/llvm/llvm-project.git
```

2. Build BOLT

```console
cd llvm-project
mkdir build
cd build
cmake -G Ninja ../llvm -DLLVM_TARGETS_TO_BUILD="X86;AArch64" -DCMAKE_BUILD_TYPE=Release -DLLVM_ENABLE_ASSERTIONS=ON -DLLVM_ENABLE_PROJECTS="bolt"
ninja bolt
```

Build time depends on your machine configuration, and it may take several minutes to complete.

3. Add the path to BOLT in your `.bashrc` file

```console
echo 'export PATH="$PATH:$HOME/llvm-project/build/bin"' >> ~/.bashrc
source ~/.bashrc
```

You are now ready to [verify BOLT is installed](#verify). 

### Option 2: Download and install BOLT using a binary release

1. Download a binary release

For Arm Linux use the file with `aarch64` in the name:

```bash { target="ubuntu:latest" }
cd $HOME
wget https://github.com/llvm/llvm-project/releases/download/llvmorg-17.0.5/clang+llvm-17.0.5-aarch64-linux-gnu.tar.xz
```

2. Extract the downloaded file

```bash { target="ubuntu:latest" }
tar xvf clang+llvm-17.0.5-aarch64-linux-gnu.tar.xz
```

3. Add the path to BOLT in your `.bashrc` file

```bash { target="ubuntu:latest" }
echo 'export PATH="$PATH:$HOME/clang+llvm-17.0.5-aarch64-linux-gnu/bin"' >> ~/.bashrc
source ~/.bashrc
```

### Verify BOLT is installed {#verify}

1. Confirm BOLT applications `perf2bolt` and `llvm-bolt` are installed

Check the `perf2bolt` command:

```bash { target="ubuntu:latest" } 
perf2bolt
```

The expected output is:

```output
perf2bolt: Not enough positional command line arguments specified!
Must specify at least 1 positional argument: See: perf2bolt --help
```

Check the `llvm-bolt` command:

```bash { target="ubuntu:latest" } 
llvm-bolt
```

The expected output is:

```output
llvm-bolt: Not enough positional command line arguments specified!
Must specify at least 1 positional argument: See: llvm-bolt --help
```

2. Print the BOLT version

```bash { target="ubuntu:latest" } 
llvm-bolt --version
```

The output is similar to:

```output
LLVM (http://llvm.org/):
  LLVM version 18.0.0git
  Optimized build with assertions.
BOLT revision 99c15eb49ba0b607314b3bd221f0760049130d97

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

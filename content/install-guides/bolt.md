---
title: BOLT

additional_search_terms:
- linux
- optimisation
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

[BOLT](https://github.com/llvm/llvm-project/tree/main/bolt) is an open-source post-link binary optimisation tool developed to speed up large applications. It does this by optimising the application's code layout based on performance profile samples collected during execution.

## Before you begin

This article provides quick instructions to download and install BOLT for Linux distributions.

1. Install Git

[Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) using the documentation for your operating system.

2. Install CMake

Install CMake using the [CMake](/install-guides/cmake) guide.

3. Install Ninja

```bash { target="ubuntu:latest" }
sudo apt install cmake ninja-build -y
```

Check it is installed:

```bash { target="ubuntu:latest" }
ninja --version
```

```output
1.10.0
```

## Download and install on Linux

1. Clone the repository

```bash { target="ubuntu:latest" }
cd $HOME
git clone https://github.com/llvm/llvm-project.git
```

2. Build BOLT
```bash { target="ubuntu:latest" }
cd llvm-project
mkdir build
cd build
cmake -G Ninja ../llvm -DLLVM_TARGETS_TO_BUILD="X86;AArch64" -DCMAKE_BUILD_TYPE=Release -DLLVM_ENABLE_ASSERTIONS=ON -DLLVM_ENABLE_PROJECTS="bolt"
ninja bolt
```

3. Add the path to BOLT in your `.bashrc` file

```bash { target="ubuntu:latest" }
echo 'export PATH="$PATH:$HOME/llvm-project/build/bin"' >> ~/.bashrc
source ~/.bashrc
```

### Verify BOLT is installed

1. Confirm BOLT applications `perf2bolt` and `llvm-bolt` are installed

Run both commands to confirm it is installed and can be found:

```bash { target="ubuntu:latest" } 
perf2bolt
```

```output
perf2bolt: Not enough positional command line arguments specified!
Must specify at least 1 positional argument: See: perf2bolt --help
```

```bash { target="ubuntu:latest" } 
llvm-bolt
```

```output
llvm-bolt: Not enough positional command line arguments specified!
Must specify at least 1 positional argument: See: llvm-bolt --help
```

2. Print the BOLT version

```bash { target="ubuntu:latest" } 
llvm-bolt --version
```

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

You are ready to use BOLT on your Linux machine.

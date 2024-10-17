---
title: Install dependencies
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin

You need to install some linux packages before you start building Process Watch on your machine. These packages are:
  * CMake.
  * Clang.
  * LLVM.
  * POSIX Threads.
  * libelf

To install these dependencies on an Ubuntu 20.04 and later machine, run:
```console
sudo apt-get update
sudo apt-get install libelf-dev cmake clang llvm llvm-dev -y
```

## Clone Process Watch Repository
You can now clone the Process Watch repository:
```console
git clone --recursive https://github.com/intel/processwatch.git
```

Note that the --recursive option ensures that all submodules are cloned. Now change into the top level directory of the repository:
```console
cd processwatch
```
## Process Watch dependencies
For the Arm build, Process Watch is dependent on two submodules. These are:
* bpftool: for building and installing the eBPF program, this is dependent on libbpf.
* Capstone: for instruction decoding, this is dependent on LLVM.

## Building Process Watch
You are now ready to build Process Watch. Use the `build.sh` shell script included in the repository to build it:
```console
./build.sh -b
```

You should see the following output:

```output
Compiling dependencies...
  No system bpftool found! Compiling libbpf and bpftool...
  Compiling capstone...
Building the 'insn' BPF program:
  Gathering BTF information for this kernel...
  Compiling the BPF program...
  Stripping the object file...
  Generating the BPF skeleton header...
Linking the main Process Watch binary...
```

You should now see the `processwatch` binary built in your top level directory.

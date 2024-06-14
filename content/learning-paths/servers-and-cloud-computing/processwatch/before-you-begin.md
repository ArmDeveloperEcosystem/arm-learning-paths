---
title: Before you begin
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install prerequisites
To compile Process Watch there are some common packages that you'll need to install on your system:
```output
CMake
Clang
LLVM
POSIX Threads
libelf
```
You can install these on Ubuntu 20.04 and later by issuing the following:
```console
sudo apt-get update
sudo apt-get install libelf-dev cmake clang llvm llvm-dev
```

## Cloning Process Watch
To clone Process Watch run the following:
```console
git clone --recursive https://github.com/intel/processwatch.git
```

Note that the --recursive option will ensure all submodules are also cloned. If you've already cloned without --recursive, change into the top-level directory of the repository and issue:
```console
cd processwatch
git submodule init
git submodule update
```

Note this needs to also be done inside the following subdirectory - this is to ensure libbpf is also cloned with the bpftool submodule
```console
cd deps/bpftool
git submodule init
git submodule update
```

## Process Watch dependencies
For the Arm build, Process Watch is dependent on two submodules. These are
* bpftool - For building and installing the eBPF program, this is dependent on libbpf
* Capstone - For instruction decoding, this is dependent on LLVM

## Building Process Watch
The code comes with a build.sh shell script. For building Process Watch you need to run the script like so
```console
./build -b
```

This ensures the dependencies are built first. You should see the following output
```bash
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

Now in the top level directory you should see the processwatch binary

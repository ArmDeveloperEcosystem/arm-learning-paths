---
title: Before you begin
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install prerequisits
To compile Process Watch there are a few common packages that you'll need to install on your system:
```console
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

## Clonining Process Watch
To clone Process Watch run the following:
```console
git clone --recursive https://github.com/grahamwoodward/processwatch
```

If you've already cloned without --recursive, go into the repository directory and issue:
```console
git submodule init
git submodule update
```

Note this needs to also be done inside the following subdirectory - this is to ensure libbpf is also cloned with the bpftool submodule
```console
deps/bpftool
```

## Process Watch dependencies
For the ARM build, Process Watch is dependent on two submodules. These are
* bpftool - For building and installing the eBPF program, this is dependant on libbpf
* Capstone - For instruction decoding, this is dependent on LLVM

## Building Process Watch
The code comes with a build.sh shell script. For building Process Watch on arm, you need to run the script like so
```console
./build -b -a
```

This ensures the dependencies are built first and we're building for the arm architecture. You should see the following output
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

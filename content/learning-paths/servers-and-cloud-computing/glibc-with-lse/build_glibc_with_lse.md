---
# User change
title: "Build Glibc with LSE"

weight: 2 # (intro is 1), 2 is first, 3 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---


## Overview
"Glibc with LSE" refers to the version of [the GNU C Library (glibc)](https://www.gnu.org/software/libc/) that includes support for [LSE (Large Systems Extensions)](https://learn.arm.com/learning-paths/servers-and-cloud-computing/lse/). LSE is an extension to the ARMv8-A architecture that provides enhanced atomic operations and memory model features.

LSE introduces additional atomic instructions and operations, such as Load-Acquire, Store-Release, and Atomic Compare-and-Swap (CAS). These operations allow for more efficient synchronization and concurrent access to shared memory in multi-threaded applications running on ARMv8-A processors.

When glibc is compiled with LSE support, it can take advantage of these enhanced atomic operations provided by the LSE extension. This can potentially improve the performance of multi-threaded applications that heavily rely on atomic operations and synchronization primitives.

{{% notice Note %}}
Your version of the GNU C Library may already have support for LSE. Before you build a new version check if LSE is already included by running:

```console
objdump -d /lib/aarch64-linux-gnu/libc.so.6 | grep -i 'cas\|casp\|swp\|ldadd\|stadd\|ldclr\|stclr\|ldeor\|steor\|ldset\|stset\|ldsmax\|stsmax\|ldsmin\|stsmin\|ldumax\|stumin' | wc -l
```

If a non-zero number is printed your GNU C Library already has LSE.

{{% /notice %}}

## Before you begin

Launch an [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) running Ubuntu version 20.04.

On your machine, install the dependencies required to build glibc:

```bash
sudo apt update
sudo apt install -y gcc-10 g++-10 gawk bison make
```

## Build and Install Glibc
You can now checkout the glibc source package and create a build directory:

```bash
cd ~
git clone https://sourceware.org/git/glibc.git
cd glibc
git checkout glibc-2.32
build=~/glibc-2.32_build_install/build
mkdir -p $build
cd $build
```

Configure glibc and run make to build it:

```bash
sudo bash ~/glibc/configure --prefix=/usr --disable-werror CC=gcc-10 CXX=g++-10
sudo make -C $build -j$(expr $(nproc) - 1)
```
You have now successfully built glibc from source without LSE. 

Now lets look at how you can build it with LSE support.

## Build glibc with LSE
To build glibc with LSE, you should add `CFLAGS` and `CXXFLAGS` to the configure command.

You can do this one of two ways. One way is to use "-mcpu=native" which tells the compiler to detect the architecture/micro-architecture of your machine. The other way is to pass the exact architecture option of your machine to the compiler using "-mcpu=neoverse-n2+lse".

Both ways are shown below:

```bash
sudo bash ~/glibc/configure --prefix=/usr --disable-werror CC=gcc-10 CXX=g++-10 CFLAGS="-mcpu=native -O3" CXXFLAGS="-mcpu=native -O3"
sudo make -C $build -j$(expr $(nproc) - 1)
```
OR

```bash
sudo bash ~/glibc/configure --prefix=/usr --disable-werror CC=gcc-10 CXX=g++-10 CFLAGS="-mcpu=neoverse-n2+lse -O3" CXXFLAGS="-mcpu=neoverse-n2+lse -O3"
sudo make -C $build -j$(expr $(nproc) - 1)
```

After running make, you should see glibc (libc.so.6) with LSE support in your build directory. 

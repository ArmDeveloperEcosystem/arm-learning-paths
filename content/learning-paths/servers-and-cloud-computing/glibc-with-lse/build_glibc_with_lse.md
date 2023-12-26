---
# User change
title: "Build Glibc with LSE"

weight: 2 # (intro is 1), 2 is first, 3 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---


## Before you begin
"Glibc with LSE" refers to the version of [the GNU C Library (glibc)](https://www.gnu.org/software/libc/) that includes support for [LSE (Large Systems Extensions)](https://learn.arm.com/learning-paths/servers-and-cloud-computing/lse/). LSE is an extension to the ARMv8-A architecture that provides enhanced atomic operations and memory model features.

LSE introduces additional atomic instructions and operations, such as Load-Acquire, Store-Release, and Atomic Compare-and-Swap (CAS). These operations allow for more efficient synchronization and concurrent access to shared memory in multi-threaded applications running on ARMv8-A processors.

When glibc is compiled with LSE support, it can take advantage of these enhanced atomic operations provided by the LSE extension. This can potentially improve the performance of multi-threaded applications that heavily rely on atomic operations and synchronization primitives.


## Build and Install Glibc
You can build glibc without installing, or with installing to a specific directory.

```bash
cd ~
git clone https://sourceware.org/git/glibc.git
cd glibc
git checkout glibc-2.32
build=~/glibc-2.32_build_install/build
mkdir -p $build
cd $build
```
Before execute the command "./glibc/configure", bison should be installed  
___Glibc-2.32 matches gcc-10!!!___
```
sudo apt install -y bison
```

- __Without installing__
    ```bash
    sudo bash ~/glibc/configure --prefix=/usr
    sudo make -C $build -j$(expr $(nproc) - 1)
    sudo make -C $build -j$(expr $(nproc) - 1) check
    ```

- __OR__

- __With installing to a specific directory__
    ```bash
    install=~/glibc-2.32_build_install/install
    mkdir -p ${install}
    sudo make -C $build -j$(expr $(nproc) - 1) install DESTDIR=${install}
    sudo make -C $build -j$(expr $(nproc) - 1) localedata/install-locales DESTDIR=${install}
    sudo make -C $build -j$(expr $(nproc) - 1) localedata/install-locale-files DESTDIR=${install}
    ```


## With LSE
If you want to build glibc with LSE, you should add `CFLAGS` and `CXXFLAGS` to configure implicitly or explicitly.

```bash
sudo bash ~/glibc/configure --prefix=/usr CFLAGS="-mcpu=native -O3" CXXFLAGS="-mcpu=native -O3"
sudo make -C $build -j$(expr $(nproc) - 1)
sudo make -C $build -j$(expr $(nproc) - 1) check
```
OR
```bash
sudo bash ~/glibc/configure --prefix=/usr CFLAGS="-mcpu=neoverse-n2+lse -O3" CXXFLAGS="-mcpu=neoverse-n2+lse -O3"
sudo make -C $build -j$(expr $(nproc) - 1)
sudo make -C $build -j$(expr $(nproc) - 1) check
```

##

## With NO-LSE

```bash
sudo bash ~/glibc/configure --prefix=/usr
sudo make -C $build -j$(expr $(nproc) - 1)
sudo make -C $build -j$(expr $(nproc) - 1) check
```
OR
```bash
sudo bash ~/glibc/configure --prefix=/usr CFLAGS="-mcpu=neoverse-n2+nolse -O3" CXXFLAGS="-mcpu=neoverse-n2+nolse -O3"
sudo make -C $build -j$(expr $(nproc) - 1)
sudo make -C $build -j$(expr $(nproc) - 1) check
```

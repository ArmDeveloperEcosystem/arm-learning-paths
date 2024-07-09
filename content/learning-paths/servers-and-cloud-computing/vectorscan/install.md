---
# User change
title: "Run Vectorscan on Arm"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify
layout: "learningpathall"
---

Hyperscan is a regular expression matching library. It provides simultaneous matching of regular expressions across streams of data. Hyperscan runs only on x86_64 platforms.

[Vectorscan](https://github.com/VectorCamp/vectorscan) is an architecture-inclusive fork of [Hyperscan](https://github.com/intel/hyperscan), that preserves the support for x86_64 and modifies the framework for the Arm architecture.

This Learning Path explains how to use Vectorscan on Arm and provides an example of using it with the Snort3 application.

## Before you begin

You should have an Arm server available with Ubuntu 20.04 or Ubuntu 22.04 installed. 

The instructions provided have been tested on an Ubuntu 22.04 AWS Arm EC2 instance (c6g.xlarge) and Ubuntu 20.04 Oracle Ampere A1 instance.

### Software dependencies

Before building Vectorscan, install the following software. 

Update the sources list for the package manager.

```bash
sudo apt update
```

GCC for your Arm Linux distribution. If needed, refer to the [installation guide](/install-guides/gcc/native/).

```bash
sudo apt install -y build-essential 
```

[CMake build system](https://cmake.org/):

```bash 
sudo apt install -y cmake
```

[Boost C++ libraries](https://www.boost.org/):

```bash
sudo apt install -y libboost-all-dev
```

[Ragel](https://packages.ubuntu.com/bionic/ragel):

```bash
sudo apt install -y ragel
```

[PkgConfig](https://en.wikipedia.org/wiki/Pkg-config):

```bash
sudo apt install -y pkg-config
```

[SQLite3](https://www.sqlite.org/index.html):

```bash
sudo apt install -y libsqlite3-dev
```

[libpcap](https://www.tcpdump.org/):

```bash
sudo apt install -y libpcap-dev
```

## Install Vectorscan

Clone the Vectorscan git repository:

```bash
git clone https://github.com/VectorCamp/vectorscan.git
cd vectorscan
```

## Determine if your processor has SVE

[Scalable Vector Extensions (SVE)](https://developer.arm.com/Architectures/Scalable%20Vector%20Extensions) is a SIMD extension of the Arm architecture which is available on some Arm processors. For example, the Neoverse-N1 does not include SVE and the Neoverse-V1 does include SVE. 

Vectorscan will run faster if you have an processor with SVE and you enable it when building the software. 

To determine if SVE is available on your processor run:

```console
lscpu | grep sve
```

If SVE is available the Flags will be printed: 

```output
Flags: fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma lrcpc dcpop sha3 sm3 sm4 asimddp sha512 sve asimdfhm dit uscat ilrcpc flagm ssbs paca pacg dcpodp svei8mm svebf16 i8mm bf16 dgh rng
```

If no SVE is present, there will be no output. 

### Build Vectorscan 

Create a build directory and build with cmake:

```bash { cwd="./vectorscan" }
mkdir build; cd build; cmake ../
```

For processors with SVE, use the flag:

```bash { cwd="./vectorscan/build" }
cmake -DBUILD_SVE=1 ../
```

Use `make` to build the vectorscan library:

```bash { cwd="./vectorscan/vectorscan-build" }
make -j$(nproc)
```

The executables from the build are created in the `bin` directory.

### Run Vectorscan unit tests

Run a check to validate that `Vectorscan` is built and running correctly:

```bash { cwd="./vectorscan/vectorscan-build" }
./bin/unit-hyperscan
```

All the unit tests should run successfully. At the end of execution you will see output similar to:

```output
[----------] Global test environment tear-down
[==========] 3746 tests from 33 test cases ran. (197558 ms total)
[  PASSED  ] 3746 tests.
```

You have successfully built and run Vectorscan.

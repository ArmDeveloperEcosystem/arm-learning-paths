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

GCC for your Arm Linux distribution. If needed, refer to the [installation guide](/install-guides/gcc/#native).

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

### Configure the build environment

You must first fix the [PCRE](https://www.pcre.org/) download location in the `cmake` file. 

1. Use a text editor to modify the file `cmake/setenv-arm64-cross.sh`

Set the environment variables to the values shown in the example below:
- `CROSS`

```console
export CROSS=/usr/bin/aarch64-linux-gnu-
```

- `CROSS_SYS`

```console
export CROSS_SYS=/
```

- `BOOST_PATH` 

```console
export BOOST_PATH=/usr/include
```

The script below shows `cmake/setenv-arm64-cross.sh` with the edits complete:

```text { file_name="setenv-arm64-cross.sh" }
export BOOST_VERSION=1_57_0
export BOOST_DOT_VERSION=${BOOST_VERSION//_/.}
export CROSS=/usr/bin/aarch64-linux-gnu-
export CROSS_SYS=/

# if [ ! -d "boost_$BOOST_VERSION" ];
# then
#       wget -O boost_$BOOST_VERSION.tar.gz https://sourceforge.net/projects/boost/files/boost/$BOOST_DOT_VERSION/boost_$BOOST_VERSION.tar.gz/download
#       tar xf boost_$BOOST_VERSION.tar.gz
# fi
if [ ! -d "pcre-8.41" ];
then
        wget -O pcre-8.41.tar.bz2 https://sourceforge.net/projects/pcre/files/pcre/8.41/pcre-8.41.tar.bz2/download
        tar xf pcre-8.41.tar.bz2
        export PCRE_SOURCE=./pcre-8.41
fi

export BOOST_PATH=/usr/include
```

After making the edits, save and close the file.

2. Source the modified file in your shell:

```bash { cwd="./vectorscan", pre_cmd="mv ~/setenv-arm64-cross.sh ~/vectorscan/cmake" }
source cmake/setenv-arm64-cross.sh
```

3. Determine if your processor has SVE

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

4. Configure the build with `cmake`

For processors without SVE, create a build directory and run `cmake`:

```bash { cwd="./vectorscan" }
mkdir vectorscan-build
cd vectorscan-build
cmake -DCROSS_COMPILE_AARCH64=1 ../ -DCMAKE_TOOLCHAIN_FILE=../cmake/arm64-cross.cmake
```

For processors with SVE, create a build directory and run `cmake` and define `BUILD_SVE` on your `cmake` command:

```console 
cmake -DCROSS_COMPILE_AARCH64=1 ../ -DCMAKE_TOOLCHAIN_FILE=../cmake/arm64-cross.cmake -DBUILD_SVE=1
```

### Build Vectorscan 

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

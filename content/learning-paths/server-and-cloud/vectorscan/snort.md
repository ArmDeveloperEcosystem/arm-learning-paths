---
# User change
title: "Install Snort3 and run it with Vectorscan on Arm"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify
layout: "learningpathall"
---


[Snort3](https://www.snort.org/snort3) is a very popular open-source deep-packet inspection application. It has integrated Hyperscan, the regex parsing library.

[Vectorscan](https://github.com/VectorCamp/vectorscan) is an architecture-inclusive fork of [Hyperscan](https://github.com/intel/hyperscan), that preserves the support for x86 and modifies the framework to allow for Arm architectures and vector engine implementations.

In this article we will detail the steps to install Snort3 on an Ubuntu Linux Arm-based platform, and run it with Vectorscan.

## Prerequisites

First, ensure you system is up to date with the latest packages:

```console
sudo apt-get update && sudo apt-get dist-upgrade -y
```

Next, ensure your system has the correct time zone:
```console
sudo dpkg-reconfigure tzdata
```

Now, create a directory where you will download and install the tarballs for the packages `snort` requires
```bash
mkdir ~/snort_src
cd ~/snort_src
```

Install the `Snort3` prerequisites to this directory

```bash
sudo apt-get install -y build-essential autotools-dev libdumbnet-dev libluajit-5.1-dev libpcap-dev \
zlib1g-dev pkg-config libhwloc-dev cmake liblzma-dev openssl libssl-dev cpputest libsqlite3-dev \
libtool uuid-dev git autoconf bison flex libcmocka-dev libnetfilter-queue-dev libunwind-dev \
libmnl-dev ethtool libjemalloc-dev
```

## Download and install [safec](https://rurban.github.io/safeclib/doc/safec-3.3/index.html) for runtime bound checks:

```bash
cd ~/snort_src
wget https://github.com/rurban/safeclib/releases/download/v02092020/libsafec-02092020.tar.gz
tar -xzvf libsafec-02092020.tar.gz
cd libsafec-02092020.0-g6d921f
./configure
make -j$(nproc)
sudo make install
```

## Download and install [gperftools 2.9](https://github.com/gperftools/gperftools) performance analysis tools:

```bash
cd ~/snort_src
wget https://github.com/gperftools/gperftools/releases/download/gperftools-2.9.1/gperftools-2.9.1.tar.gz
tar xzvf gperftools-2.9.1.tar.gz
cd gperftools-2.9.1
./configure
make -j$(nproc)
sudo make install
```

## Install `Ragel`:
```bash
sudo apt install ragel
```

## Install `PCRE` to your `snort_src` folder:
```bash
cd ~/snort_src/
wget wget https://sourceforge.net/projects/pcre/files/pcre/8.45/pcre-8.45.tar.gz
tar -xzvf pcre-8.45.tar.gz
cd pcre-8.45
./configure
make -j$(nproc)
sudo make install
```

## Download (but do not install) `Boost` C++ Libraries:
```bash
cd ~/snort_src
wget https://boostorg.jfrog.io/artifactory/main/release/1.77.0/source/boost_1_77_0.tar.gz
tar -xvzf boost_1_77_0.tar.gz
```

## Download `Vectorscan` source
```bash
cd ~/snort_src
git clone https://github.com/VectorCamp/vectorscan 
cd vectorscan 
#git checkout v5.3.2 
cd .. 
mkdir hyperscan-build 
cd hyperscan-build/ 
```

## Fix source to build with glibc>=2.34

There is a current issue where builds fail with `glibc >= 2.34` and a pending [PR](https://github.com/intel/hyperscan/issues/359).

For now, workaround this issue by making the changes to `STACK_SIZE` as mentioned in the [pull request](https://github.com/intel/hyperscan/pull/358/files/eac1e5e0354f3ead2c832e798d89f86082b77d75).

## Configure and build Vectorscan
```bash { cwd="snort_src/hyperscan-build" }
cmake -DCMAKE_INSTALL_PREFIX=/usr/local -DBOOST_ROOT=~/snort_src/boost_1_77_0/ ~/snort_src/vectorscan/
make -j$(nproc) && sudo make install 
```
## Install flatbuffers
```bash
cd ~/snort_src
wget https://github.com/google/flatbuffers/archive/refs/tags/v2.0.0.tar.gz -O flatbuffers-v2.0.0.tar.gz
tar -xzvf flatbuffers-v2.0.0.tar.gz
mkdir flatbuffers-build
cd flatbuffers-build
cmake ../flatbuffers-2.0.0
make -j$(nproc)
sudo make install
```

## Download and install Data Acquisition library(DAQ)

```bash
cd ~/snort_src
wget https://github.com/snort3/libdaq/archive/refs/tags/v3.0.5.tar.gz -O libdaq-3.0.5.tar.gz
tar -xzvf libdaq-3.0.5.tar.gz
cd libdaq-3.0.5
./bootstrap
./configure
make -j$(nproc)
sudo make install
```

## Update shared libraries
```bash
sudo ldconfig
```

## Download, Compile and Install `Snort3` with the default settings
```bash
cd ~/snort_src
wget https://github.com/snort3/snort3/archive/refs/tags/3.1.18.0.tar.gz -O snort3-3.1.18.0.tar.gz
tar -xzvf snort3-3.1.18.0.tar.gz
cd snort3-3.1.18.0
./configure_cmake.sh --prefix=/usr/local --enable-tcmalloc --enable-jemalloc
cd build
make -j$(nproc)
sudo make install
```

## Check Snort3 is installed and running properly

`Snort3` should be installed in `/usr/local/bin`. Verify it is installed and running correctly by checking the version:

```bash
/usr/local/bin/snort -V
```

You should see output similar to the following:
```
   ,,_     -*> Snort++ <*-
  o"  )~   Version 3.1.18.0
   ''''    By Martin Roesch & The Snort Team
           http://snort.org/contact#team
           Copyright (C) 2014-2021 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using DAQ version 3.0.5
           Using LuaJIT version 2.1.0-beta3
           Using OpenSSL 3.0.2 15 Mar 2022
           Using libpcap version 1.10.1 (with TPACKET_V3)
           Using PCRE version 8.45 2021-06-15
           Using ZLIB version 1.2.11
           Using FlatBuffers 2.0.0
           Using Hyperscan version 5.3.0 2022-07-26
           Using LZMA version 5.2.5
```

## Test Snort3 with Vectorscan

To test the performance of `Snort3` with `Vectorscan` on your Arm instance, first download a capture file to test with:
```bash
mkdir ~/snort3_test
cd ~/snort3_test
wget https://download.netresec.com/pcap/maccdc-2012/maccdc2012_00001.pcap.gz
gunzip maccdc2012_00001.pcap.gz
```

Now run the following command to use `hyperscan` (i.e. `vectorscan`) with `snort3` on the downloaded capture file. It uses the default configuration file:
```bash { cwd="~/snort3_test" }
snort -c /usr/local/etc/snort/snort.lua --lua 'search_engine.search_method="hyperscan"' -r maccdc2012_00001.pcap
```

You should see detailed output with packet and file statistics and a summary similar to the below.
```
Summary Statistics
--------------------------------------------------
timing
                  runtime: 00:00:16
                  seconds: 16.299069
                 pkts/sec: 262375
                Mbits/sec: 479
o")~   Snort exiting
```

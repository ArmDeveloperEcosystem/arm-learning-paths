---
# User change
title: "Install Snort3 and run it with Vectorscan on Arm"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify
layout: "learningpathall"
---


[Snort 3](https://www.snort.org/snort3) is an open-source deep-packet inspection application. Snort 3 integrates Hyperscan, the regex parsing library.

You can install Snort 3 on an Ubuntu Linux Arm-based server, and run it with Vectorscan, the architecture-inclusive fork of Hyperscan.

## Before you begin

You should already have an Arm server running Ubuntu Linux from the previous topic. 

Install the Snort 3 dependencies:

```bash
sudo apt update 
sudo apt-get install -y build-essential autotools-dev libdumbnet-dev libluajit-5.1-dev libpcap-dev \
zlib1g-dev pkg-config libhwloc-dev cmake liblzma-dev openssl libssl-dev cpputest libsqlite3-dev \
libtool uuid-dev git autoconf bison flex libcmocka-dev libnetfilter-queue-dev libunwind-dev \
libmnl-dev ethtool libjemalloc-dev ragel
```

## Download and install other required software

Create a directory where you can download and build the other required software dependencies:

```bash
mkdir ~/snort_src
cd ~/snort_src
```

Install the [Safe C library](https://rurban.github.io/safeclib/doc/safec-3.3/index.html):

```bash
wget https://github.com/rurban/safeclib/releases/download/v3.8.1/safeclib-3.8.1.tar.gz
tar -xzvf safeclib-3.8.1.tar.gz
cd safeclib-3.8.1.0-gdfea26
./configure
make -j$(nproc)
sudo make install
```

Install [gperftools](https://github.com/gperftools/gperftools) performance analysis tools:

```bash
cd ~/snort_src
wget https://github.com/gperftools/gperftools/releases/download/gperftools-2.15/gperftools-2.15.tar.gz
tar xzvf gperftools-2.15.tar.gz
cd gperftools-2.15
./configure
make -j$(nproc)
sudo make install
```

Install [PCRE (Perl Compatible Regular Expressions)](https://www.pcre.org/):

```bash
cd ~/snort_src/
wget https://sourceforge.net/projects/pcre/files/pcre/8.45/pcre-8.45.tar.gz
tar -xzvf pcre-8.45.tar.gz
cd pcre-8.45
./configure
make -j$(nproc)
sudo make install
```

Download (but do not build) [Boost C++ Libraries](https://www.boost.org/):

```bash
cd ~/snort_src
wget https://boostorg.jfrog.io/artifactory/main/release/1.85.0/source/boost_1_85_0.tar.gz
tar -xvzf boost_1_85_0.tar.gz
```

Download Vectorscan:

```bash
cd ~/snort_src
git clone https://github.com/VectorCamp/vectorscan 
cd vectorscan 
cd .. 
mkdir hyperscan-build 
cd hyperscan-build 
```

Configure and build Vectorscan:

```bash { cwd="snort_src/hyperscan-build" }
cmake -DCMAKE_INSTALL_PREFIX=/usr/local -DBOOST_ROOT=~/snort_src/boost_1_85_0/ ~/snort_src/vectorscan/
make -j$(nproc) && sudo make install 
```

Install [FlatBuffers](https://google.github.io/flatbuffers/):

```bash
cd ~/snort_src
wget https://github.com/google/flatbuffers/archive/refs/tags/v22.12.6.tar.gz -O flatbuffers-v22.12.6.tar.gz
tar -xzvf flatbuffers-v22.12.6.tar.gz
mkdir flatbuffers-build
cd flatbuffers-build
cmake ../flatbuffers-22.12.6
make -j$(nproc)
sudo make install
```

Install [Data Acquisition library (DAQ)](https://github.com/snort3/libdaq):

```bash
cd ~/snort_src
wget https://github.com/snort3/libdaq/archive/refs/tags/v3.0.15.tar.gz -O libdaq-3.0.15.tar.gz
tar -xzvf libdaq-3.0.15.tar.gz
cd libdaq-3.0.15
./bootstrap
./configure
make -j$(nproc)
sudo make install
```

Update shared libraries:

```bash
sudo ldconfig
```

## Download, Compile and Install Snort 3

You can now download, compile and build Snort 3:

```bash
cd ~/snort_src
wget https://github.com/snort3/snort3/archive/refs/tags/3.2.2.0.tar.gz -O snort3-3.2.2.0.tar.gz
tar -xzvf snort3-3.2.2.0.tar.gz
cd snort3-3.2.2.0
./configure_cmake.sh --prefix=/usr/local --enable-tcmalloc 
cd build
make -j$(nproc)
sudo make install
```

## Confirm Snort 3 is installed and running properly

Snort 3 should be installed in `/usr/local/bin`. 

Verify it is installed and running correctly by printing the version:

```bash
/usr/local/bin/snort -V
```

You should see output similar to the following:

```output
   ,,_     -*> Snort++ <*-
   o"  )~   Version 3.2.2.0
   ''''    By Martin Roesch & The Snort Team
           http://snort.org/contact#team
           Copyright (C) 2014-2024 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using DAQ version 3.0.15
           Using Hyperscan version 5.4.11 2024-07-09
           Using libpcap version 1.10.1 (with TPACKET_V3)
           Using LuaJIT version 2.1.0-beta3
           Using LZMA version 5.2.5
           Using OpenSSL 3.0.2 15 Mar 2022
           Using PCRE version 8.45 2021-06-15
           Using ZLIB version 1.2.11

```

## Test Snort 3 with Vectorscan

You can test the performance of Snort 3 with Vectorscan on your Arm instance.

Download a capture file to using for testing: 

```bash
mkdir ~/snort3_test
cd ~/snort3_test
wget "https://share.netresec.com/s/7qgDSGNGw2NY8ea/download?path=%2F&files=maccdc2012_00001.pcap.gz" -O maccdc2012_00001.pcap.gz
gunzip maccdc2012_00001.pcap.gz
```

Run the following command to use Snort 3 with Vectorscan on the downloaded capture file:

```bash { cwd="~/snort3_test" }
snort -c /usr/local/etc/snort/snort.lua --lua 'search_engine.search_method="hyperscan"' -r maccdc2012_00001.pcap
```

You should see detailed output with packet and file statistics and a summary similar to the below.

```output
Summary Statistics
--------------------------------------------------
timing
                  runtime: 00:00:16
                  seconds: 16.299069
                 pkts/sec: 262375
                Mbits/sec: 479
o")~   Snort exiting
```

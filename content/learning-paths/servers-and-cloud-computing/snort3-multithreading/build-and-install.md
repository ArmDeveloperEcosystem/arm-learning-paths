---
title: Install Snort3 along with all its required dependencies.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Multithreading in Snort 3 refers to the ability to associate multiple threads with a single Snort instance enabling the concurrent processing of multiple packet files. This optimization frees up additional memory for further packet processing.

In order to enable multithreading in Snort3, specify the quantity of threads designated for processing network traffic using either the '--max-packet-threads' or '-z' option. 

{{%notice Note%}}
    The instruction provided have been tested on AWS EC2 Graviton4 metal instance (Neoverse V2) 
{{%/notice%}}

## Compile and build Snort3
Run the script to download and install Snort3 and its dependent libraries.
Skip this step if Snort3 is already installed.

<!-- add github link for the below file [build_snort3.sh]() -->
``` bash
#!/usr/bin/env bash

# Copyright (c) 2022-2024, Arm Limited.
#
# SPDX-License-Identifier: Apache-2.0
# author : PreemaMerlin.Dsouza@arm.com

# Define a list of dependency package URLs 
declare -a PACKAGE_URLS=(
"https://github.com/snort3/snort3/archive/refs/tags/3.3.5.0.tar.gz"
"https://sourceforge.net/projects/pcre/files/pcre/8.45/pcre-8.45.tar.gz"
"https://github.com/VectorCamp/vectorscan/archive/refs/tags/vectorscan/5.4.11.tar.gz"
"https://github.com/snort3/libdaq/archive/refs/tags/v3.0.16.tar.gz"
"https://boostorg.jfrog.io/artifactory/main/release/1.86.0/source/boost_1_86_0.tar.gz"
"https://github.com/rurban/safeclib/releases/download/v3.8.1/safeclib-3.8.1.tar.gz"
"https://github.com/gperftools/gperftools/releases/download/gperftools-2.13/gperftools-2.13.tar.gz"
)

downlaodPackages()
{
    for url in "${PACKAGE_URLS[@]}"; do
        # Extract the file name from the URL
        fname=$(basename "$url")
        fpath="${ROOT_DIR}/${fname}"
        # Check if the file already exists
        if [[ -f "$fpath" ]]; then
            echo "File $fname already exists. Skipping download."
        else
            # Download the file using wget

	        echo "File $fname not found. Downloading..."

            wget -O "$fpath" "$url"
            if [[ $? -eq 0 ]]; then
                echo "$fname download complete"
            else
                echo "ERROR:$fname download Fail."
            fi
        fi
    done
}

installPackages()
{
    echo "@@@@@@@@@@@@@@@@@@  Installing packages ...   @@@@@@@@@@@@@@@@@@@@"
    if [[ -r /etc/os-release ]]; then
        OS_NAME=$(grep -w "NAME" /etc/os-release | cut -d= -f2 | tr -d '"')
        OS_VERSION_ID=$(grep -w "VERSION_ID" /etc/os-release | cut -d= -f2 | tr -d '"')
        if [[ "${OS_NAME}" == "Ubuntu" ]]; then
            echo "OS: ${OS_NAME} ${OS_VERSION_ID}"
        else
            echo "Error: This script is only for ubuntu"
            exit 1
        fi
        if [[ "${OS_VERSION_ID}" != "22.04" ] || [ "${OS_VERSION_ID}" != "20.04" ]];then
            echo "Warning: OS: ${OS_NAME} ${OS_VERSION_ID}"
            echo "Warning: Ubuntu 20.04 or 22.04 is recommended"
        fi
    else
        echo "Error: OS information detection failed"
        exit 1
    fi

    apt-get update
    apt-get install -y $LIST_OF_APPS
  
    # required to get optimised result from Snort3
    downlaodPackages
    mkdir -p ${ROOT_DIR}/snort3
    tar -xzf 3.3.5.0.tar.gz --directory  ${ROOT_DIR}/snort3 --strip-components=1
    echo "@@@@@@@@@@@@@@@@@@     Installing Snort3 Dependencies ...     @@@@@@@@@@@@@@@@@@@@"
    mkdir -p ${SNORT_DIR}
    mkdir -p $SNORT_DIR/pcre
    tar -xvf pcre-8.45.tar.gz --directory $SNORT_DIR/pcre --strip-components=1
    #vector scan
    mkdir -p $SNORT_DIR/vectorscan
    tar -xzvf 5.4.11.tar.gz --directory $SNORT_DIR/vectorscan --strip-components=1

    #libdaq
    mkdir -p $SNORT_DIR/libdaq
    tar -xvzf v3.0.16.tar.gz --directory $SNORT_DIR/libdaq --strip-components=1
    
    #required to get optimized result from vectorscan
    mkdir -p $SNORT_DIR/boost
    tar -xvf boost_1_86_0.tar.gz -C $SNORT_DIR/boost --strip-components=1

    #safeclib 
    mkdir -p $SNORT_DIR/safeclib
    tar -xzvf safeclib-3.8.1.tar.gz --directory $SNORT_DIR/safeclib --strip-components=1 

    #gperftools
    mkdir -p $SNORT_DIR/gperftools
    tar -xzvf gperftools-2.13.tar.gz --directory $SNORT_DIR/gperftools --strip-components=1
  
    echo "@@@@@@@@@@@@@@@@@@     Packages installed     @@@@@@@@@@@@@@@@@@@@"
}

buildInstall()
{
    echo "@@@@@@@@@@@@@@@@@@     Build & Installation ... Start    @@@@@@@@@@@@@@@@@@@@"
    cd $SNORT_DIR/libdaq
    mkdir -p ${SNORT_DIR}/libdaq/install
    ./bootstrap
    ./configure --prefix=${SNORT_DIR}/libdaq/install
    make -j${NUM_JOBS}
    make install

    cd ${SNORT_DIR}/safeclib
    ./configure
    make -j${NUM_JOBS}
    make -j${NUM_JOBS} install

    cd $SNORT_DIR/gperftools
    ./configure --with-tcmalloc-pagesize=64
    make -j${NUM_JOBS}
    make -j${NUM_JOBS}

    cd $SNORT_DIR/pcre
    ./configure
    make -j${NUM_JOBS}
    make -j${NUM_JOBS}

    cd ${SNORT_DIR}/vectorscan
    cmake -DBOOST_ROOT=$(SNORT_DIR)/boost -DCMAKE_BUILD_TYPE=Release .
    make -j${NUM_JOBS}
    make -j${NUM_JOBS}

    cd ${ROOT_DIR}/snort3
    ./configure_cmake.sh --build-type=Release --with-daq-includes=${SNORT_DIR}/libdaq/install/include/ --with-daq-libraries=${SNORT_DIR}/libdaq/install/lib/ --enable-unit-tests --enable-tcmalloc
    cd ${ROOT_DIR}/snort3/build
    make -j$NUM_JOBS
    make -j$NUM_JOBS install
    echo "@@@@@@@@@@@@@@@@@@     Build & Installation ... Done    @@@@@@@@@@@@@@@@@@@@"
}

#------ Execution Start ----------#
# provide nproc count to the scripts , it will be used as -j for make 
if [[ $# -ne 2 ]]; then
	echo "Usage: $0 <current_working_directory> <nprc>"
	exit 1
fi

ROOT_DIR=$(pwd)/"$1"
NUM_JOBS="$2"
SNORT_DIR=${ROOT_DIR}/snort3/dependencies
set -e

LIST_OF_APPS="sudo net-tools build-essential manpages-dev libnuma-dev python3
                python3-venv cmake meson pkg-config python3-pyelftools lshw
                util-linux iperf3 nginx libboost-all-dev ragel libsqlite3-dev
                libpcap-dev libdumbnet-dev libluajit-5.1-dev zlib1g-dev
                libhwloc-dev liblzma-dev libssl-dev libgoogle-perftools-dev
                libpcre++-dev flex openssl libunwind-dev autotools-dev 
	            libhugetlbfs-bin autoconf libmnl-dev bats wget unzip iproute2 
	            git pkg-config cpputest libtool bison libcmocka-dev 
	            libnetfilter-queue-dev ethtool"

# nprc should be a positive integer)
if ! [[ "$NUM_JOBS" =~ ^[0-9]+$ ]] || [[ "$NUM_JOBS" -le 0 ]]; then
    echo "Error: nprc should be a positive integer."
    exit 1
fi

mkdir -p ${ROOT_DIR}
cd ${ROOT_DIR}
installPackages
buildInstall
```

To check if the installation is complete, run the command below.
```bash{ output_lines = "2-20" }
 snort -V
,,_     -*> Snort++ <*-
  o"  )~   Version 3.3.5.0
   ''''    By Martin Roesch & The Snort Team
           http://snort.org/contact#team
           Copyright (C) 2014-2024 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using DAQ version 3.0.16
           Using Hyperscan version 5.4.11 2024-09-12
           Using libpcap version 1.10.1 (with TPACKET_V3)
           Using LuaJIT version 2.1.0-beta3
           Using LZMA version 5.2.5
           Using OpenSSL 3.0.2 15 Mar 2022
           Using PCRE version 8.45 2021-06-15
           Using ZLIB version 1.2.11

```



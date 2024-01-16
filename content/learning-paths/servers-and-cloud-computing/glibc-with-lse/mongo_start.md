---
# User change
title: "Start MongoDB utilizing the newly built Glibc with LSE"
weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

You are now ready to start MongoDB utilizing the newly built glibc with LSE on your Arm server.


## MongoDB Setups
Build and install MongoDB version `5.3.2`:
```console
#for Fedora/RHEL
sudo yum install -y git gcc g++ python3-devel openssl-devel libcurl-devel 
#for Ubuntu/Debian
sudo apt install -y git gcc g++ python-dev-is-python3 python3-pip libssl-dev libcurl4-openssl-dev liblzma-dev

export PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring

cd ~
sudo git clone https://github.com/mongodb/mongo.git 
cd mongo
sudo git checkout r5.3.2
sudo python3 -m pip install -r etc/pip/compile-requirements.txt
sudo python3 buildscripts/scons.py install-mongod -j$(expr $(nproc) - 1) --disable-warnings-as-errors
```

## MongoDB Starts utilizing the newly built Glibc with LSE
```console
cd ~
mkdir -p /mongodb-5.3.2/data
vi /mongodb-5.3.2/mongodb.conf

dbpath=/mongodb-5.3.2/data
logpath=/mongodb-5.3.2/mongodb.log
pidfilepath=/mongodb-5.3.2/data/mongo.pid
fork=true
logappend=true
bind_ip=0.0.0.0
port=27017

#if necessary
#rm -rf /mongodb-5.3.2/data/*
~/glibc-2.32_build_install/build/testrun.sh ~/mongo/build/install/bin/mongod -f /mongodb-5.3.2/mongodb.conf --wiredTigerCacheSizeGB=20

#If you encounter an error related to libcrypt.so and need to execute the following command before running again:
#cp /usr/lib/aarch64-linux-gnu/libcrypt.so ~/glibc-2.32_build_install/build/crypt/
```

Confirm if the workload mongodb runs with the newly built glibc with LSE:  
 - First, get the pid with the following command.
    ```console
    ps -ef | grep mongo
    root       19852       1  1 16:33 ?        00:00:01 /root/glibc-2.32_build_install/build/elf/ld-linux-aarch64.so.1 --library-path /root/glibc-2.32_build_install/build:/root/glibc-2.32_build_install/build/math:/root/glibc-2.32_build_install/build/elf:/root/glibc-2.32_build_install/build/dlfcn:/root/glibc-2.32_build_install/build/nss:/root/glibc-2.32_build_install/build/nis:/root/glibc-2.32_build_install/build/rt:/root/glibc-2.32_build_install/build/resolv:/root/glibc-2.32_build_install/build/mathvec:/root/glibc-2.32_build_install/build/support:/root/glibc-2.32_build_install/build/crypt:/root/glibc-2.32_build_install/build/nptl /root/mongo/build/install/bin/mongod -f /mongodb-5.3.2/mongodb.conf --wiredTigerCacheSizeGB=20
    ```

 - Then execute the following command to check.
    ```
    cat /proc/19852/smaps | grep glibc 
    ffff898c5000-ffff898cd000 r-xp 00000000 103:02 953511    /root/glibc-2.32_build_install/build/crypt/libcrypt.so
    ffff898cd000-ffff898e4000 ---p 00008000 103:02 953511    /root/glibc-2.32_build_install/build/crypt/libcrypt.so
    ffff898e4000-ffff898e5000 r--p 0000f000 103:02 953511    /root/glibc-2.32_build_install/build/crypt/libcrypt.so
    ffff898e5000-ffff898e6000 rw-p 00010000 103:02 953511    /root/glibc-2.32_build_install/build/crypt/libcrypt.so
    ffff89f0a000-ffff8a060000 r-xp 00000000 103:02 943581    /root/glibc-2.32_build_install/build/libc.so
    ffff8a060000-ffff8a077000 ---p 00156000 103:02 943581    /root/glibc-2.32_build_install/build/libc.so
    ffff8a077000-ffff8a07a000 r--p 0015d000 103:02 943581    /root/glibc-2.32_build_install/build/libc.so
    ffff8a07a000-ffff8a07d000 rw-p 00160000 103:02 943581    /root/glibc-2.32_build_install/build/libc.so
    ffff8a080000-ffff8a09a000 r-xp 00000000 103:02 952971    /root/glibc-2.32_build_install/build/nptl/libpthread.so
    ffff8a09a000-ffff8a0af000 ---p 0001a000 103:02 952971    /root/glibc-2.32_build_install/build/nptl/libpthread.so
    ffff8a0af000-ffff8a0b0000 r--p 0001f000 103:02 952971    /root/glibc-2.32_build_install/build/nptl/libpthread.so
    ffff8a0b0000-ffff8a0b1000 rw-p 00020000 103:02 952971    /root/glibc-2.32_build_install/build/nptl/libpthread.so
    ffff8a0b5000-ffff8a14e000 r-xp 00000000 103:02 952919    /root/glibc-2.32_build_install/build/math/libm.so
    ffff8a14e000-ffff8a164000 ---p 00099000 103:02 952919    /root/glibc-2.32_build_install/build/math/libm.so
    ffff8a164000-ffff8a165000 r--p 0009f000 103:02 952919    /root/glibc-2.32_build_install/build/math/libm.so
    ffff8a165000-ffff8a166000 rw-p 000a0000 103:02 952919    /root/glibc-2.32_build_install/build/math/libm.so
    ffff8a71d000-ffff8a724000 r-xp 00000000 103:02 953138    /root/glibc-2.32_build_install/build/rt/librt.so
    ffff8a724000-ffff8a73c000 ---p 00007000 103:02 953138    /root/glibc-2.32_build_install/build/rt/librt.so
    ffff8a73c000-ffff8a73d000 r--p 0000f000 103:02 953138    /root/glibc-2.32_build_install/build/rt/librt.so
    ffff8a73d000-ffff8a73e000 rw-p 00010000 103:02 953138    /root/glibc-2.32_build_install/build/rt/librt.so
    ffff8a73e000-ffff8a741000 r-xp 00000000 103:02 952968    /root/glibc-2.32_build_install/build/dlfcn/libdl.so
    ffff8a741000-ffff8a75d000 ---p 00003000 103:02 952968    /root/glibc-2.32_build_install/build/dlfcn/libdl.so
    ffff8a75d000-ffff8a75e000 r--p 0000f000 103:02 952968    /root/glibc-2.32_build_install/build/dlfcn/libdl.so
    ffff8a75e000-ffff8a75f000 rw-p 00010000 103:02 952968    /root/glibc-2.32_build_install/build/dlfcn/libdl.so
    ffff90300000-ffff90313000 r-xp 00000000 103:02 953699    /root/glibc-2.32_build_install/build/resolv/libresolv.so
    ffff90313000-ffff9032f000 ---p 00013000 103:02 953699    /root/glibc-2.32_build_install/build/resolv/libresolv.so
    ffff9032f000-ffff90330000 r--p 0001f000 103:02 953699    /root/glibc-2.32_build_install/build/resolv/libresolv.so
    ffff90330000-ffff90331000 rw-p 00020000 103:02 953699    /root/glibc-2.32_build_install/build/resolv/libresolv.so
    ffff90333000-ffff90355000 r-xp 00000000 103:02 943577    /root/glibc-2.32_build_install/build/elf/ld.so
    ffff90372000-ffff90373000 r--p 0002f000 103:02 943577    /root/glibc-2.32_build_install/build/elf/ld.so
    ffff90373000-ffff90375000 rw-p 00030000 103:02 943577    /root/glibc-2.32_build_install/build/elf/ld.so

    ```

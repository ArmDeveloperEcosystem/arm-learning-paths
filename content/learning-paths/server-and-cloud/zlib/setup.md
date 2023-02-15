---
# User change
title: "Build and install Cloudflare zlib on Arm servers"
weight: 2
layout: "learningpathall"
---

## Prerequisites

* An [Arm based instance](/learning-paths/server-and-cloud/csp/) from an appropriate cloud service provider.

This learning path has been verified on AWS EC2 and Oracle cloud services, running `Ubuntu Linux 20.04` and `Ubuntu Linux 22.04`.

## Detailed Steps

Most Linux distributions use zlib without any optimizations. For the Arm architecture this means that CRC (cyclic redundancy check) instructions are not utilized for best performance. Installing and using a libz which has been optimized may provide performance improvement for applications doing data compression. 

Cloudflare zlib is one version which has optimizations included. There are other zlib versions which have been optimized. The process to use them should be similar.

## Confirm crc32 is included in the processor flags

All recent Arm servers and most Armv8.0-A and above processors have support for CRC instructions. 

To check if a Linux system has support use the lscpu command and look for crc32 in the listed flags.
```bash { ret_code="0" }
lscpu | grep crc32
```

If the machine is confirmed to include crc32 it may benefit from zlib-cloudflare. 

## Check if the default zlib includes crc32 instructions

Some Linux system may already make use of crc32 with the default library. If the default zlib is already optimized, then using zlib-cloudflare may not have any impact on performance. 

If zlib is not installed, you can install it with the following command on Ubuntu, as well as additional packages for this learning path. 

```bash
sudo apt install -y libzstd1 build-essential git
```

Ubuntu and Debian Linux distributions put zlib in /usr/lib/aarch64-linux-gnu

To check if there are any CRC instructions in a library use objdump to disassemble and look for crc32 instructions. 

```bash
objdump -d /usr/lib/aarch64-linux-gnu/libz.so.1 | awk -F" " '{print $3}' | grep crc32 | wc -l
```

If the result is 0 then there is no crc32 instructions used in the library. 

## Install Cloudflare libz

If there are no crc32 instructions in libz then zlib-cloudflare may help application performance. 

To build and install zlib-cloudflare navigate to an empty directory and use these commands.

```bash
mkdir tmp ; pushd tmp
git clone https://github.com/cloudflare/zlib.git
cd zlib && ./configure 
make && sudo make install
popd
rm -rf tmp
```

If successful, zlib-cloudflare is installed in /usr/local/lib

To install zlib somewhere else which does not require sudo to install it, use the prefix argument to configure to select another location such as 
```console
./configure --prefix=$HOME/zlib
```
This results in zlib being installed in $HOME/zlib instead and the sudo is not needed for the make install.

## Configuring zlib

Since zlib is a shared library there are different ways to configure its usage. 

Below is a simple C program to demonstrate zlib configuration.

```C { file_name="test.c" }
#include <stdio.h>
#include <stdlib.h>
#include "zlib.h"

int main()
{

    gzFile myfile;

    printf("%s\n", zlibVersion());

    myfile = gzopen("testfile.gz", "wb");

    gzprintf(myfile,"Hello gzipped file!\n");

    gzclose(myfile);

    exit(0);
}
```

Save the text above as a file test.c and compile the example.

```bash
gcc test.c -o test -lz
```

Run the program and see the version.

```bash
./test
```

The printed version will be something like:
```console
1.2.11
```

Use ldd to see the location of the shared library.
```bash
ldd ./test
```

The output will how the shared libraries used by test.
```console
linux-vdso.so.1 (0x0000ffffababe000)
libz.so.1 => /lib/aarch64-linux-gnu/libz.so.1 (0x0000ffffaba52000)
libc.so.6 => /lib/aarch64-linux-gnu/libc.so.6 (0x0000ffffab8df000)
/lib/ld-linux-aarch64.so.1 (0x0000ffffaba8e000)
```

## Set LD_PRELOAD to use zlib-cloudflare

To run test with zlib-cloudflare instead of the default.

```bash
LD_PRELOAD=/usr/local/lib/libz.so ./test
```

The LD_PRELOAD variable informs the linker to use these libraries before the default libraries. 

The version of zlib-cloudflare will print. It may be older than the default, but we are interested in crc32 not using the latest.

In the next section let's see how to use zlib-cloudflare in an application doing data compression. 



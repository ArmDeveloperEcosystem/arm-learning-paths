---
# User change
title: "Build and install zlib-ng on Arm servers"
weight: 2
layout: "learningpathall"
---

## Overview

Most Linux distributions ship `zlib` without Arm-specific optimizations. This means instruction extensions such as Neon SIMD and ARMv8 CRC32 are not used, leaving significant performance on the table for compression-heavy workloads.

Designed for modern systems, `zlib-ng` is an actively maintained fork of `zlib` that includes the following enhancements:
 
 - Neon SIMD acceleration for adler32
 - Inflate chunk copying
 - Hash operations
 - ARMv8 CRC32 and PMULL acceleration 
 
 `zlib-ng` also supports a zlib-compatible API mode, allowing you to use it as a drop-in replacement without recompiling your applications.

## Confirm Arm SIMD capabilities in the processor

All Neoverse servers and processors implementing Armv8-A and above have support for Neon (Advanced SIMD) and CRC32 instructions.

To check which capabilities a Linux system exposes, use `lscpu` and look at the `Flags` output:

```bash { ret_code="0" }
lscpu | grep -E "asimd|crc32"
```

The `asimd` flag indicates Neon (Advanced SIMD) support. The `crc32` flag confirms hardware-accelerated CRC32. Both are present on all modern Arm server platforms, including AWS Graviton, Azure Cobalt 100, and Google Axion.

## Install prerequisite packages and inspect default zlib library

Install the packages you need for this Learning Path:

```bash
sudo apt update
sudo apt install -y build-essential git cmake
```

Ubuntu and Debian put `zlib` in `/usr/lib/aarch64-linux-gnu`.

You can inspect the default library with `objdump` to see whether it contains any Neon or CRC32 instructions before you replace it:

```bash
objdump -d /usr/lib/aarch64-linux-gnu/libz.so.1 | grep -cE "crc32|pmull|v[0-9]+\.(16b|8b|8h|4h|4s|2s|2d|1d)"
```

Recent Ubuntu releases on aarch64 typically return a non-zero value here — the system `zlib` has *some* Neon code, but the coverage is partial. `zlib-ng` provides dedicated Neon paths for adler32, inflate chunk copying, slide hash, and compare256, with significantly more instruction-level parallelism than the default library. This makes installing `zlib-ng` worthwhile on any Arm server regardless of what the system `zlib` already contains.

## Build and install zlib-ng

Clone the `zlib-ng` source and build it in zlib-compatible mode. The `ZLIB_COMPAT=ON` option produces a standard `libz.so` that is API- and ABI-compatible with the system `zlib`, which allows you to use `LD_PRELOAD` to switch libraries without recompiling your applications.

```bash
git clone https://github.com/zlib-ng/zlib-ng.git
cd zlib-ng
mkdir build && cd build
cmake .. -DZLIB_COMPAT=ON -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=lib
cmake --build .
sudo cmake --install .
sudo ldconfig
```

{{% notice Note %}}
Without `-DCMAKE_INSTALL_LIBDIR=lib`, CMake's `GnuInstallDirs` on Ubuntu aarch64 installs libraries into `/usr/local/lib/aarch64-linux-gnu/` instead of `/usr/local/lib/`. Setting this explicitly keeps paths consistent across platforms.
{{% /notice %}}

If successful, `zlib-ng` installs to `/usr/local/lib`:

```bash
ls /usr/local/lib/libz*
```

The output is similar to:

```output
/usr/local/lib/libz.a
/usr/local/lib/libz.so
/usr/local/lib/libz.so.1
/usr/local/lib/libz.so.1.3.1.zlib-ng
```

## Confirm the installation

Query the dynamic linker cache to confirm `zlib-ng` is visible:

```bash
/sbin/ldconfig -p | grep "libz.so"
```

The output will show both the system `zlib` and the newly installed `zlib-ng`:

```output
	libz.so.1 (libc6,AArch64) => /usr/local/lib/libz.so.1
	libz.so.1 (libc6,AArch64) => /lib/aarch64-linux-gnu/libz.so.1
	libz.so (libc6,AArch64) => /usr/local/lib/libz.so
```

## Configure and test zlib-ng

Because `zlib-ng` is a shared library, you can configure which version an application uses without relinking it.

Navigate back to your home directory before creating the test files:

```bash
cd $HOME
```

Use a text editor to save the following code in a file named `test.c`:

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

Compile the example program, linking against the system `zlib`:

```bash
gcc test.c -o test -lz
```

Run the program to confirm the system `zlib` version:

```bash
./test
```

The output will be the version of the system library. For example:

```output
1.3
```

Use `ldd` to confirm which shared library the binary loads:

```bash
ldd ./test
```

The output will show the shared libraries used:

```output
linux-vdso.so.1 (0x0000ffffababe000)
libz.so.1 => /lib/aarch64-linux-gnu/libz.so.1 (0x0000ffffaba52000)
libc.so.6 => /lib/aarch64-linux-gnu/libc.so.6 (0x0000ffffab8df000)
/lib/ld-linux-aarch64.so.1 (0x0000ffffaba8e000)
```

## Use zlib-ng instead of the default zlib

To run the same binary with `zlib-ng` instead of the default library, set `LD_PRELOAD` to point to the installed `zlib-ng` shared object:

```bash
LD_PRELOAD=/usr/local/lib/libz.so.1 ./test
```

The `LD_PRELOAD` environment variable tells the dynamic linker to load this library before the system default.

The `zlib-ng` version identifier will be printed:

```output
1.3.1.zlib-ng
```
The version string includes the `.zlib-ng` suffix to distinguish it from the upstream library.

## What you've learned and what's next

In this section, you built, installed, and tested `zlib-ng`. 
In the next section you will use `zlib-ng` to accelerate a Python application that does data compression.

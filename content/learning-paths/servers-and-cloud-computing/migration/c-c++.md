---
# User change
title: "Migrating C/C++ applications"

weight: 3

layout: "learningpathall"

---

## C/C++ on Arm Neoverse processors

### Enabling Architecture Specific Features

You can use the table below to build C/C++ applications with the optimal processor features.

Select Neoverse-N1 if you want to run your application on both Neoverse-N1 and Neoverse-V1 processors. 

Applications compiled for Neoverse-V1 will not run on Neoverse-N1. 

Use `-mcpu=` to specify the architecture and tuning. Using `-mcpu=` is generally better than using `-march=`. 

CPU       | Flag    | GCC version      | LLVM version
----------|---------|-------------------|-------------
Neoverse-N1 | `-mcpu=neoverse-n1` | GCC-9+ | Clang/LLVM 10+
Neoverse-V1 | `-mcpu=neoverse-512tvb` | GCC-11+ | Clang/LLVM 14+

If your compiler doesn't support `-mcpu=neoverse-512tvb`, use `-mcpu=neoverse-n1` instead. 

If your compiler doesn't support `-mcpu=neoverse-n1`, use `-mcpu=cortex-a72` instead.

The Neoverse-N1 option `-mcpu=neoverse-n1` is available in GCC-7 on Amazon Linux2.

### Compilers

Newer compilers provide better support and optimizations for Arm Neoverse processors. You should use the latest compiler available for the operating system you are using.

The table below shows GCC and LLVM compiler versions available in Linux distributions. The starred version is the default compiler for the Linux distribution.

Linux Distribution      | GCC                  | Clang/LLVM
------------------------|----------------------|-------------
Amazon Linux 2          | 7*, 10               | 7, 11*
Amazon Linux 2023       | 11*                  | 15*
Ubuntu 22.04            | 9, 10, 11*, 12       | 11, 12, 13, 14*
Ubuntu 20.04            | 7, 8, 9*, 10         | 6, 7, 8, 9, 10, 11, 12
Ubuntu 18.04            | 4.8, 5, 6, 7*, 8     | 3.9, 4, 5, 6, 7, 8, 9, 10
Debian10                | 7, 8*                | 6, 7, 8
Red Hat EL8             | 8*, 9, 10            | 10
SUSE Linux ES15         | 7*, 9, 10            | 7


### Large-System Extensions

Neoverse processors have support for Large-System Extensions (LSE). LSE provides low-cost atomic operations which can improve system throughput for locks and mutexes.

Using LSE can result in significant performance improvement for your application. 

Refer to the Learning Path [Learn about Large System Extensions](/learning-paths/servers-and-cloud-computing/lse/) for more information. 

### Porting code with SSE/AVX intrinsics to NEON

You may have applications which include x86_64 intrinsics. These need special treatment when recompiling.

Refer to the Learning Path [Porting Architecture Specific Intrinsics](/learning-paths/cross-platform/intrinsics/) for the available options to migrate x86_64 intrinsics to NEON.

### Signed and unsigned char data types

The C standard doesn't specify if the `char` datatype is unsigned or signed.

On x86 `char` is signed and on Arm it is `unsigned` by default. This may result in unintended program behavior. 

This can be addressed by using standard integer types that explicitly specify unsigned or signed, such as `uint8_t` and `int8_t`

You can also compile with `-fsigned-char` to force the `char` datatype to be signed when migrating to Arm. 

### Scalable Vector Extension 

Scalable Vector Extension (SVE) is available on Neoverse-V1 processors.  

Both a compiler and a Linux kernel that supports SVE is required.

You will need GCC-11 or newer or LLVM-14 or newer and Linux kernel 4.15 or newer for SVE support.

Refer to the Learning Path [From Arm NEON to SVE](/learning-paths/servers-and-cloud-computing/sve/sve_basics/) for more information and examples. 


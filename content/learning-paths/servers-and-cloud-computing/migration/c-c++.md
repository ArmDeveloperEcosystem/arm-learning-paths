---
# User change
title: "Migrating C/C++ applications"

weight: 3

layout: "learningpathall"

---

## C/C++ on Arm Neoverse processors

### Compilers

Newer compilers provide better support and optimizations for Arm Neoverse processors. You should use the latest compiler available for the operating system you are using.

The table below shows GCC and LLVM compiler versions available in Linux distributions. The starred version is the default compiler version for the Linux distribution. If a newer version is available over the default, it's recommended to install that version.

Linux Distribution      | GCC                  | Clang/LLVM
------------------------|----------------------|-------------
Amazon Linux 2023       | 11*                  | 15*
Amazon Linux 2          | 7*, 10               | 7, 11*
Ubuntu 24.04		| 9, 10, 11, 12, 13*, 14 | 14, 15, 16, 17, 18*	
Ubuntu 22.04            | 9, 10, 11*, 12       | 11, 12, 13, 14*
Ubuntu 20.04            | 7, 8, 9*, 10         | 6, 7, 8, 9, 10, 11, 12
Ubuntu 18.04            | 4.8, 5, 6, 7*, 8     | 3.9, 4, 5, 6, 7, 8, 9, 10
Debian 12               | 11, 12*              | 13, 14*, 15, 16
Debian 10               | 7, 8*                | 6, 7, 8
Red Hat EL9             | 11                   | 13
Red Hat EL8             | 8*, 9, 10            | 10
SUSE Linux ES15         | 7*, 9, 10            | 7

### GCC Neoverse CPU targets

If the application will be executed on the same processor it is being compiled on, then simply use `-mcpu=native`. GCC will produce the most optimized binary.

If the application will be executed on a different processor from the one it is being compiled on, don't use `-mcpu=native`. In that case, you can reference the table below.

CPU       | Flag    | GCC version      | LLVM version
----------|---------|-------------------|-------------
Any | `-mcpu=native` | All | All
Neoverse-N1 | `-mcpu=neoverse-n1` | GCC-9+ | Clang/LLVM 10+
Neoverse-V1 | `-mcpu=neoverse-v1` | GCC-11+ | Clang/LLVM 12+
Neoverse-N2 | `-mcpu=neoverse-n2` | GCC-11+ | Clang/LLVM 12+
Neoverse-V2 | `-mcpu=neoverse-v2` | GCC-13+    | Clang/LLVM 16+

The Neoverse-N1 option `-mcpu=neoverse-n1` is available in GCC-7 on Amazon Linux2.

There are other options like `-march` (ISA version) and `-mtune` (specific processor implementation). These are discussed in the [GCC Arm options documentation](https://gcc.gnu.org/onlinedocs/gcc/ARM-Options.html). However, in general, only `-mcpu` should be used. `-mcpu` is basically a single option that combines `-march` and `-mtune` together. Last, keep in mind that if an application targets an older processor, it will likely be able to execute on a newer processor (less some optimizations for the newer processor). However, if the application targets a newer processor, it might not execute on an older processor. This is true for any processor architecture, not just Arm.

If `-mcpu` (and `-march` and `-mtune` for that matter) are not used, GCC will use a default value for `-march` (ISA version). This default for a given version of GCC can be viewed by running the following command.

```console
gcc -Q --help=target
```

Below is an example output for GCC 11.3.0

``` output
The following options are target specific:
  -mabi=                                lp64
  -march=                               armv8-a
  -mbig-endian                          [disabled]
  -mbionic                              [disabled]
  -mbranch-protection=
  -mcmodel=                             small
  -mcpu=                                generic
  -mfix-cortex-a53-835769               [enabled]
  -mfix-cortex-a53-843419               [enabled]
  -mgeneral-regs-only                   [disabled]
  -mglibc                               [enabled]
  -mharden-sls=
  -mlittle-endian                       [enabled]
  -mlow-precision-div                   [disabled]
  -mlow-precision-recip-sqrt            [disabled]
  -mlow-precision-sqrt                  [disabled]
  -mmusl                                [disabled]
  -momit-leaf-frame-pointer             [enabled]
  -moutline-atomics                     [enabled]
  -moverride=<string>
  -mpc-relative-literal-loads           [enabled]
  -msign-return-address=                none
  -mstack-protector-guard-offset=
  -mstack-protector-guard-reg=
  -mstack-protector-guard=              global
  -mstrict-align                        [disabled]
  -msve-vector-bits=<number>            scalable
  -mtls-dialect=                        desc
  -mtls-size=                           24
  -mtrack-speculation                   [disabled]
  -mtune=                               generic
  -muclibc                              [disabled]
  -mverbose-cost-dump                   [disabled]
```

Notice that this version of GCC defaults `-march` to Arm ISA version ARMv8.A (v8.0). This could be under optimized if the application will run an on ISA version that is newer than ARMv8.A (8.0). However, it will result in a binary that can execute across a wider spectrum of Arm processors. This is precisely why the default is ARMv8.A and not something newer like ARMv8.3-A (or ARMv9.0-A). If you know the minimum ISA version of CPU your application will execute on, you could also consider selecting the ISA. This can be done with either the `-mcpu` (recommended) or `-march` switches. Valid values for the ISA version can be found in the [GCC Arm options documentation](https://gcc.gnu.org/onlinedocs/gcc/ARM-Options.html).

### GCC Link Time Optimization

A GCC option that almost always results in higher performance on Arm is `-flto=auto`. This flag analyzes and optimizes the application as though the whole program is compiled within a single translation unit. The `=auto` part of this switch speeds up the optimization process by using multiple threads. It is recommended to give this switch a try.

More information on this switch can be found in the [GCC documentation](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html).

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


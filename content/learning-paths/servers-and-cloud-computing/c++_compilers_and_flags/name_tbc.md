---
title: Understanding your Instances and Compilers Capabilities
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Identify the Neoverse version and supported CPU extensions

To understand which version of the Arm Neoverse architecture the instance of your choice provides you can use various resource, such as the [Arm partner webpage](https://www.arm.com/partners/aws).

To find this through an AWS instance, run the `lscpu` command and observe the underlying Neoverse Architecture as per the information below. 

```output
lscpu | grep -i model
Model name:                           Neoverse-N1
Model:                                1
```
Here you can confirm `t4g.2xlarge`, is based on the Neoverse-N1 Arm IP. 

Next, to identify the CPU extensions supported by this architecture at runtime we can observe the hardware capabilities (HWCAP) vector with the C++ source code below that reads a specific vector that contains the information.

Copy and paste the c program into a file named, `hw_cap.c`.

```c

#include <stdio.h>
#include <sys/auxv.h>
#include <asm/hwcap.h>

int main()
{
    long hwcaps = getauxval(AT_HWCAP);

    if (hwcaps & HWCAP_AES) {
        printf("AES instructions are available\n");
    } else {
        printf("AES instructions are not available\n");
    }
    if (hwcaps & HWCAP_CRC32) {
        printf("CRC32 instructions are available\n");
    } else {
        printf("CRC32 instructions are not available\n");
    }
    if (hwcaps & HWCAP_PMULL) {
        printf("PMULL/PMULL2 instructions that operate on 64-bit data are available\n");
    } else {
        printf("PMULL/PMULL2 instructions are not available\n");
    }
    if (hwcaps & HWCAP_SHA1) {
        printf("SHA1 instructions are available\n");
    } else {
        printf("SHA1 instructions are not available\n");
    }
    if (hwcaps & HWCAP_SHA2) {
        printf("SHA2 instructions are available\n");
    } else {
        printf("SHA2 instructions are not available\n");
    }
    if (hwcaps & HWCAP_SVE) {
        printf("Scalable Vector Extension (SVE) instructions are available\n");
    } else {
        printf("Scalable Vector Extension (SVE) instructions are not available\n");
    }

    return 0;
}

```

Compile and run with the command below. 

```bash
gcc hw_cap.c -o hw_cap
./hw_cap
```

On Graviton 2, I observe the following indicating the the scalable vector extensions (SVE ar not available)

```output
AES instructions are available
CRC32 instructions are available
PMULL/PMULL2 instructions that operate on 64-bit data are available
SHA1 instructions are available
SHA2 instructions are available
Scalable Vector Extension (SVE) instructions are not available

```

For the latest list of all hardware capabilities available for a specific linux kernel version, refer to the `arch/arm/include/uapi/asm/hwcap.h` header file. 

## Compiler flags and options

The g++ compiler will automatically identify the host systems capability. You 

Using the g++ compiler as an example, the most course-grained dial you can adjust is the optimisation level, denoted with `-O<x>`. This adjusts a variety of lower-level optimsation flags at the expense of increased computation time, memory use and debuggability. However, the output binary may not show expected behaviour when debugging using a program such as GNU debugger (`gdb`) since the generated code may not match the source code or program order, for example with loop unrolling and vectorisation. 

If running your C++ application in a memory constrained environment, for example in a containerised environment, you may wish to consider optimising for size. 

Support for the latest Arm CPU extensions are supported by the GCC compiler in advance of general availability of Silicon. 

Compiler flags, `-O<1,2,3>`, `-Ofast`. Please refer to your compiler documentation for full details on the optimisation level, for example [GCC](https://gcc.gnu.org/onlinedocs/gcc-14.2.0/gcc/Optimize-Options.html).


If the host is the same platform you are compiling for, you can observe which CPUs are potential targets for your command with the following g++ command. 

```output
g++ -E -mcpu=help -xc /dev/null
cc1: note: valid arguments are: cortex-a34 cortex-a35 cortex-a53 cortex-a57 cortex-a72 cortex-a73 thunderx thunderxt88p1 thunderxt88 octeontx octeontx81 octeontx83 thunderxt81 thunderxt83 ampere1 ampere1a emag xgene1 falkor qdf24xx exynos-m1 phecda thunderx2t99p1 vulcan thunderx2t99 cortex-a55 cortex-a75 cortex-a76 cortex-a76ae cortex-a77 cortex-a78 cortex-a78ae cortex-a78c cortex-a65 cortex-a65ae cortex-x1 cortex-x1c **neoverse-n1** ares neoverse-e1 octeontx2 octeontx2t98 octeontx2t96 octeontx2t93 octeontx2f95 octeontx2f95n octeontx2f95mm a64fx tsv110 thunderx3t110 neoverse-v1 zeus neoverse-512tvb saphira cortex-a57.cortex-a53 cortex-a72.cortex-a53 cortex-a73.cortex-a35 cortex-a73.cortex-a53 cortex-a75.cortex-a55 cortex-a76.cortex-a55 cortex-r82 cortex-a510 cortex-a710 cortex-a715 cortex-x2 cortex-x3 neoverse-n2 cobalt-100 neoverse-v2 grace demeter generic
```

Comparing to when using `g++9` we can see there are fewer CPU targets to optimise for as recently released CPUs are omitted, for example the Neoverse V2. 

```
g++-9 -E -mcpu=help -xc /dev/null
cc1: note: valid arguments are: cortex-a35 cortex-a53 cortex-a57 cortex-a72 cortex-a73 thunderx thunderxt88p1 thunderxt88 octeontx octeontx81 octeontx83 thunderxt81 thunderxt83 emag xgene1 falkor qdf24xx exynos-m1 phecda thunderx2t99p1 vulcan thunderx2t99 cortex-a55 cortex-a75 cortex-a76 ares neoverse-n1 neoverse-e1 a64fx tsv110 zeus neoverse-v1 neoverse-512tvb saphira neoverse-n2 cortex-a57.cortex-a53 cortex-a72.cortex-a53 cortex-a73.cortex-a35 cortex-a73.cortex-a53 cortex-a75.cortex-a55 cortex-a76.cortex-a55 generic
```

## Defining the Compilation goal

If you're natively compiling, the compiler will automatically detect the system and choose the best parameters for you. 

If you intend your application to be portable across a variety of Arm architecture versions, selecting a target architecture with, `-march=` with a the value mapped to the lowest Arm architecture in your deployment fleet. This is because the Arm architecture's backwards compatible nature. 

If you're building for a specific CPU, as in our case we are building to run natively on an AWS Graviton 2 instance (Arm Neoverse N1), we recommend specifying using the `-mcpu` .
---
# User change
title: "Introduction to Large System Extensions"

weight: 2

layout: "learningpathall"


---


## Introduction

Large System Extensions (LSE) improve the performance of atomic operations in systems with many processors. Understanding LSE helps developers port software applications to Arm servers running Neoverse processors.

In programming, when multiple processors or threads access shared data, and at least one is writing, the operations must be atomic. This means the data accesses must be treated as a single operation relative to the other processors to avoid data race conditions. Microprocessors are designed to treat sequences such as read-modify-write and memory-register exchange as single operations, even when they create multiple accesses to memory. This hardware makes programming easier. 

The Armv8.1-A architecture introduced new atomic instructions. Atomics are alternatives to the load, store exclusive sequences used in previous architecture versions.

The [Arm Architecture Reference Manual](https://developer.arm.com/documentation/ddi0487/latest) refers to the atomic instructions as Large System Extensions (LSE). You may see them referred to as FEAT_LSE in documentation or in compiler information indicating support for the atomic instructions. 

From the Architecture Reference Manual, FEAT_LSE introduces a set of atomic instructions:

- Compare and Swap instructions, CAS and CASP
- Atomic memory operation instructions, LD\<op\> and ST\<op\>, where \<op\> is one of ADD, CLR, EOR, SET, SMAX, SMIN, UMAX, and UMIN
- Swap instruction, SWP

Additional architecture improvements were made in Armv8.4-A and made optional in Armv8.2-A, but the low-level hardware details are not covered here. This additional feature is referred to as FEAT_LSE2 in the Architecture Reference Manual.

In architecture versions prior to LSE, read-modify-write sequences use load exclusive and store exclusive instructions. Incrementing a shared variable uses a sequence such as:

- **LDXR** to read current count (load exclusive)   
- **ADD** to add one to the shared variable    
- **STXR** to attempt to store to memory (store exclusive)     
- **CMP** to check if the operation succeeded

Because atomic accesses use multiple instructions each processor is required to implement an exclusive monitor. The exclusive monitor is a hardware state machine to track the read-modify-write sequences and match up the loads and stores. You can read about the exclusive monitor in the technical reference manual of a processor such as the [Cortex-A53](https://developer.arm.com/documentation/ddi0500/j/Level-1-Memory-System/L1-Data-memory-system/Internal-exclusive-monitor?lang=en).

If the number of processors is small, this works fine. Increasing the number of processor combined with increased caching, make it hard to maintain fairness as processors closer to each other have a better chance of completing atomic sequences.

With LSE, atomic instructions provide a non-interruptible read-modify-write sequence in a single instruction. The atomic instructions can perform simple arithmetic or logical operations on the specified memory location, and return the updated value to the processor. Programmers benefit from the atomic instructions because it’s easier to specify a single instruction compared to a sequence of instructions with a loop around them if the sequence fails. 

Atomic instructions work better in situations such as networking software where many counters are atomically updated from many processors. The atomic instructions result in faster performance and less variability. 

With this introduction, you can look at how this applies to Arm Cortex and Neoverse processors. 

## LSE in Neoverse Processors

AWS currently offers four generations of Graviton processors. 

The first generation instance type is A1, and was announced at re:Invent 2018. A1 instances provide up to 16 vCPUs. As the first Graviton instance type, A1 paved the way for the software ecosystem needed for the next generation, Graviton2.

Announced at re:Invent 2019, Graviton2 processors provide a significant performance uplift from A1. The Graviton2 instance types include M6g, C6g, R6g, and T4g. AWS advertises 40% better price performance over the same generation of x86 instances. Graviton2 instances include up to 64 vCPUs. Graviton2 uses Arm Neoverse N1 cores.

Graviton3 was announced at re:Invent 2021 and instance types include M7g, C7g, R7g. Graviton3 offers up to 2x better floating-point performance, up to 2x faster crypto performance, and up to 3x better ML performance compared to Graviton2. Graviton3 uses Arm Neoverse V1 cores.

Announced at re:Invent 2023, Graviton4 is based on Neoverse V2 cores. Graviton4 increases core count to 96 and is first available in the R8g instance type. Graviton4 provides 30% better compute performance, 50% more cores, and 75% more memory bandwidth than Graviton3.

AWS A1 instances are based on the Cortex-A72 processor. The Cortex-A72 implements the Armv8.0-A architecture and does NOT include the atomic instructions. All of the AWS EC2 instances based on the Neoverse N1, Neoverse V1, and Neoverse V2 processors include the atomic instructions. 

Other cloud service providers such as Oracle Cloud, Microsoft Azure, and Google Cloud offer instances based on Neoverse processors, and support the atomic instructions.

One of the common performance issues when migrating to Neoverse is running software that does not utilize LSE. Software built with load exclusives and store exclusives usually runs slower on Neoverse instances. 

It's important to make sure you get the best performance on Neoverse processors.

**How do I know if my Linux kernel supports atomics?**

There are a couple of ways to check. First, look in the kernel ring buffer messages to see if LSE is present:

```bash
sudo dmesg | grep LSE
```

If LSE is present, the output from the command will look like:

```output
[    0.001296] CPU features: detected: LSE atomic instructions
```

Another check is to use the lscpu command to print the processor information:

```bash
lscpu
```

Here is the output from running `lscpu` an AWS A1 instance:

```output
Architecture:                    aarch64
CPU op-mode(s):                  32-bit, 64-bit
Byte Order:                      Little Endian
CPU(s):                          1
On-line CPU(s) list:             0
Thread(s) per core:              1
Core(s) per socket:              1
Socket(s):                       1
NUMA node(s):                    1
Vendor ID:                       ARM
Model:                           3
Model name:                      Cortex-A72
Stepping:                        r0p3
BogoMIPS:                        166.66
L1d cache:                       32 KiB
L1i cache:                       48 KiB
L2 cache:                        2 MiB
NUMA node0 CPU(s):               0
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Spec store bypass: Not affected
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Mitigation; Branch predictor hardening
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 cpuid
```
Look specifically at the flags printed at the end.

Here is the output from running `lscpu` on an AWS T4g instance:

```output
Architecture:                    aarch64
CPU op-mode(s):                  32-bit, 64-bit
Byte Order:                      Little Endian
CPU(s):                          2
On-line CPU(s) list:             0,1
Thread(s) per core:              1
Core(s) per socket:              2
Socket(s):                       1
NUMA node(s):                    1
Vendor ID:                       ARM
Model:                           1
Model name:                      Neoverse-N1
Stepping:                        r3p1
BogoMIPS:                        243.75
L1d cache:                       128 KiB
L1i cache:                       128 KiB
L2 cache:                        2 MiB
L3 cache:                        32 MiB
NUMA node0 CPU(s):               0,1
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpu
                                 id asimdrdm lrcpc dcpop asimddp ssbs
```

For Neoverse N1 the “atomics” flag is listed indicating LSE support.

**Which versions of the GCC compiler support LSE?**

LSE support started in GCC 6, but GCC 10 and GCC 11 are good to use.

**What are out-of-line atomics?**

When an atomic operation is encountered by the compiler, calls to helper functions that provide the best implementation for the processor are inserted instead of directly generating in-line instructions.

The gcc command line options -moutline-atomics and -mno-outline-atomics enable or disable calls to the out-of-line helpers. 

With GCC 9.3.1 and later, you can use the above options to enable/disable out-of-line atomics.

With GCC 10.1 and higher, out-of-line atomics are enabled by default. Refer to [Making the most of the Arm architecture with GCC 10](https://community.arm.com/arm-community-blogs/b/tools-software-ides-blog/posts/making-the-most-of-the-arm-architecture-in-gcc-10) for more info. 

**Which CPU or architecture version should I specify with gcc?**

Refer to the [AWS Graviton Technical Guide](https://github.com/aws/aws-graviton-getting-started/blob/main/c-c++.md) on GitHub AWS for recommendations on GCC flags for Graviton processors. 

It’s generally a good idea to use the latest compiler available on the operating system being used.

**Is LSE built into the C library on my operating system?**

Yes, if you are using any of the operating systems below. Only Ubuntu 18.04 requires an extra package to be installed. 

- Amazon Linux 2
- Amazon Linux 2022
- Ubuntu 18.04 (needs `apt install libc6-lse`)
- Ubuntu 20.04
- Ubuntu 22.04




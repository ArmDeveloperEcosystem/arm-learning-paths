---
title: Before You Begin
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before You Begin

### Linux Computers

Collecting a performance profile needs to be performed on an Arm Linux computer. BOLT can be run on the same computer or it can be installed and run on a different Linux computer which has more resources.

#### Single Computer

An Arm Linux computer can build executable, collect performance profile and run BOLT optimisation steps.

#### Multiple Computers

An Arm Linux computer is needed to collect performance profile but the other steps can be run on a different Linux computer.

##### Build Executable

If your second computer is also Arm you can compile the executable and copy it to collect the  performance profile.

If you are not compiling your executable on Arm you will need to cross compile and then copy the executable to the Arm computer for profiling. See this guide on [Cross Compiling](/install-guides/gcc/cross/)

##### Build & Run BOLT

BOLT should be build for the native architecture of the 2nd computer. It will still be able to optimise an Arm executable even if the native architecture is not AArch64.

Once you have a profile it can be copied to the computer with BOLT and the BOLT conversion & optimisation steps run.

See this [guide](/install-guides/bolt) for installing BOLT.

### Verify Perf Record

This guide describes 3 different methods of collecting a profile that can be used with BOLT. Below are sections on how to verify you can collect each of these methods on your Linux Arm computer. If you can't collect a profile update your Linux kernel to 4.20 or later and update Perf using the [Perf](/install-guides/perf/) guide to 4.20.

The sections below help you verify you can collect a performance profile for each method.

#### Cycle Samples

Collects a sample record every CPU cycle. 

Verify you can record samples and check the `perf.data` contains `PERF_RECORD_SAMPLE` sections.

```bash { target="ubuntu:latest" }
perf record -e cycles:u -- echo "Hello World"
perf report -D | grep PERF_RECORD_SAMPLE
```

```output
193348946860440 0x3c8 [0x28]: PERF_RECORD_SAMPLE(IP, 0x1): 10871/10871: 0xffff8000813b4f34 period: 1 addr: 0
193348946867440 0x3f0 [0x28]: PERF_RECORD_SAMPLE(IP, 0x2): 10871/10871: 0xffffb17351c0 period: 1 addr: 0
193348946868200 0x418 [0x28]: PERF_RECORD_SAMPLE(IP, 0x2): 10871/10871: 0xffffb1735950 period: 1 addr: 0
193348946868920 0x440 [0x28]: PERF_RECORD_SAMPLE(IP, 0x2): 10871/10871: 0xffffb1735980 period: 6 addr: 0
193348946871400 0x468 [0x28]: PERF_RECORD_SAMPLE(IP, 0x2): 10871/10871: 0xffffb17359a0 period: 219 addr: 0
193348946884200 0x490 [0x28]: PERF_RECORD_SAMPLE(IP, 0x2): 10871/10871: 0xffffb174802c period: 9440 addr: 0
193348947030600 0x538 [0x28]: PERF_RECORD_SAMPLE(IP, 0x2): 10871/10871: 0xffffb173d2bc period: 127212 addr: 0
```

#### Embedded Trace Macrocell (ETM)

ETM is an Arm real-time trace module providing instruction and data tracing.

Verify ETM is in the list of perf events

```bash { target="ubuntu:latest" }
$ perf list | grep cs_etm
```

```output
cs_etm//           [Kernel PMU event]
cs_etm/autofdo/    [Kernel PMU event]
```

If ETM is not found you will need to build a version of perf with Arm Coresight enabled. See https://docs.kernel.org/trace/coresight/coresight-perf.html

If `cs_etm/autofdo/` isn't found you will need to update the Linux Kernel and perf to 4.20 or later.

```bash { target="ubuntu:latest" }
perf record -e cs_etm/@tmc_etr0,autofdo/u -- echo "Hello World"
perf report -D | grep "CoreSight ETM"
```

```output
. ... CoreSight ETMV4I Trace data: size 0x30 bytes
```

#### Statistical Profiling Extension (SPE)

The Statistical Profiling Extension provides a statistical view of the performance characteristics of executed instructions.

Verify SPE is in the list of perf events

```bash { target="ubuntu:latest" }
$ perf list | grep arm_spe
```

```output
arm_spe_0//        [Kernel PMU event]
```

If `arm_spe` isn't found you will need to update the Linux Kernel and perf to 4.20 or later.

```bash { target="ubuntu:latest" }
perf record -e arm_spe/branch_filter=1/u -- echo "Hello World"
perf report -D | grep "ARM SPE"
```

```output
. ... ARM SPE data: size 0xc80 bytes
```

### Build Executable

BOLT works by rearranging both functions and code within functions to move hot code closer together and reduce memory overhead.

To do this the binary needs atleast an unstripped symbol table and prefers being linked with relocations which can be enabled with the linker flag `--emit-relocs`. This flag should be used to get maximum performance gains.

BOLT is also incompatiable with the GCC flag `-freorder-blocks-and-partition` which is enabled by default in GCC version 8. This can be avoided by adding the flag `-fno-reorder-blocks-and-partition`.

The executable will be used when collecting profile information and passed into BOLT to optimise it.

GCC

```bash
gcc <args> -Wl,--emit-relocs -fno-reorder-blocks-and-partition
```

Clang

```bash
clang <args> -Wl,--emit-relocs
```
---
title: Prepare your BOLT environment
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before You begin

Before you begin you will need to:
- Decide if you want to do everything on a single Linux system or use two systems
- Investigate the options available to collect performance information
- Review your compiler flags 

### Linux Systems

Collecting a performance profile needs to be performed on an Arm Linux system. BOLT can be run on the same system or it can be installed and run on a different Linux system which has more resources.

The system used to run the application and profile performance is called the target system. The system used to build the application and run BOLT is called the build system. 

#### Single System

A single Arm Linux system can build your executable, collect the performance profile, and run the BOLT optimization steps. The same system can be the build and the target system.

This is a good option if the Arm Linux system is a server or cloud instance with good performance and adequate memory. 

#### Multiple Systems

If the target system has limited performance, you can use different build and target systems.

In this case, you will need two systems: 
- An Arm Linux system to collect performance profiles (target system)
- Another Linux system to build the executable and run BOLT optimization (build system)

##### Build Executable

If your build system uses the Arm architecture, you can compile the executable and copy it to the target system to collect the performance profile.

If your build system uses a a different architecture, you will need to cross compile and copy the executable to the target system. 

##### Build and run BOLT

BOLT should be installed for the native architecture of the build system. BOLT can optimize an Arm executable even if the architecture of the build machine is not Arm.

Once you have a profile, it can be copied to the build system with BOLT and you can run the BOLT conversion and optimization steps.

See the [BOLT install guide](/install-guides/bolt) for information about installing BOLT.

### Verify Perf record

There are three different methods of collecting a profile that can be used with BOLT. 

You need to determine which methods are available on your Arm Linux target system. 

If some of the methods don't work, you can try to update your Linux kernel to 5.15 or later and update Linux Perf using the [Perf install guide](/install-guides/perf/) to 5.15.

{{% notice Note %}}
Linux kernel configuration and hypervisor settings may impact your ability to collect performance profiles.
{{% /notice %}}

Use the information below to verify which methods work on your target system. 

#### Cycle Samples

This method collects a sample record every CPU cycle. 

Verify you can record samples and check the `perf.data` file contains `PERF_RECORD_SAMPLE` sections.

To confirm this method works run:

```bash { target="ubuntu:latest" }
perf record -e cycles:u -- echo "Hello World"
perf report -D | grep PERF_RECORD_SAMPLE
```

If you see similar output, it means you can collect cycle samples.

```output
193348946860440 0x3c8 [0x28]: PERF_RECORD_SAMPLE(IP, 0x1): 10871/10871: 0xffff8000813b4f34 period: 1 addr: 0
193348946867440 0x3f0 [0x28]: PERF_RECORD_SAMPLE(IP, 0x2): 10871/10871: 0xffffb17351c0 period: 1 addr: 0
193348946868200 0x418 [0x28]: PERF_RECORD_SAMPLE(IP, 0x2): 10871/10871: 0xffffb1735950 period: 1 addr: 0
193348946868920 0x440 [0x28]: PERF_RECORD_SAMPLE(IP, 0x2): 10871/10871: 0xffffb1735980 period: 6 addr: 0
193348946871400 0x468 [0x28]: PERF_RECORD_SAMPLE(IP, 0x2): 10871/10871: 0xffffb17359a0 period: 219 addr: 0
193348946884200 0x490 [0x28]: PERF_RECORD_SAMPLE(IP, 0x2): 10871/10871: 0xffffb174802c period: 9440 addr: 0
193348947030600 0x538 [0x28]: PERF_RECORD_SAMPLE(IP, 0x2): 10871/10871: 0xffffb173d2bc period: 127212 addr: 0
```

#### Embedded Trace Macrocell (ETM) {#etm} 

ETM is an Arm real-time trace module providing instruction and data tracing.

To check if ETM is available on your target system run: 

```bash { target="ubuntu:latest" }
perf list | grep cs_etm
```

If you see similar output, it means ETM is available. 

```output
cs_etm//           [Kernel PMU event]
cs_etm/autofdo/    [Kernel PMU event]
```

If ETM is not found you will need to build a version of perf with Arm Coresight enabled. See https://docs.kernel.org/trace/coresight/coresight-perf.html

AutoFDO is an alternative way to collect ETM data with small data sizes. 

If `cs_etm/autofdo/` isn't found you will need to update the Linux Kernel and perf to 5.15 or later.

To confirm AutoFDO is working run:

```bash { target="ubuntu:latest" }
perf record -e cs_etm/autofdo/u -- echo "Hello World"
perf report -D | grep "CoreSight ETM"
```

The output should contain text similar to:

```output
. ... CoreSight ETMV4I Trace data: size 0x30 bytes
```

#### Statistical Profiling Extension (SPE) {#spe}

The Statistical Profiling Extension provides a statistical view of the performance characteristics of executed instructions.

Verify SPE is in the list of perf events by running:

```bash { target="ubuntu:latest" }
perf list | grep arm_spe
```

If you see similar output, it means SPE is available. 

```output
arm_spe_0//        [Kernel PMU event]
```

If `arm_spe` isn't found you will need to update the Linux Kernel and perf to 5.15 or later.
To enable it see [Enable the SPE feature in Linux guide](https://developer.arm.com/documentation/ka005362/1-0).

To confirm SPE is working run:

```bash { target="ubuntu:latest" }
perf record -e arm_spe/branch_filter=1/u -- echo "Hello World"
perf report -D | grep "ARM SPE"
```

The output should contain text similar to:

```output
. ... ARM SPE data: size 0xc80 bytes
```

### Check the compiler flags to get ready for BOLT

BOLT works by rearranging both functions and code within functions to move hot code closer together and reduce memory overhead.

To do this, the binary needs at least an unstripped symbol table and prefers being linked with relocations which can be enabled with the linker flag `--emit-relocs`. This flag should be used to get maximum performance gains.

BOLT is incompatible with the GCC flag `-freorder-blocks-and-partition` which is enabled by default in GCC version 8. This can be avoided by adding the flag `-fno-reorder-blocks-and-partition`.

The executable will be used when collecting profile information and passed into BOLT to optimize it.

Below is a summary of the flags to use for both GCC and Clang.

For GCC:

```bash
gcc <args> -Wl,--emit-relocs -fno-reorder-blocks-and-partition
```

For Clang:

```bash
clang <args> -Wl,--emit-relocs
```

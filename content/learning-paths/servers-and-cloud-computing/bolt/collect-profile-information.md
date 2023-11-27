---
title: Collect Profile Information
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Collect Profile Information

On Arm there are 3 different methods of collecting profiling information that can then be used with BOLT, cycle Samples, Arm Embedded Trace Macrocell (ETM) and Arm Statistical Profiling Extension (SPE). Below are commands for how to record these difference profiling methods, all of them will produce a `perf.data` file that contains in the information and is used in the next BOLT step. 

All the commmands are run while you run your executable. It needs to be run in a normal use case otherwise the information collected won't represent standard use and the optimisation can do nothing or even harm its performance.

### Requirements

It is recommended that you update to your Linux kernel and perf to 4.20 or later.

#### ETM

To check perf can record ETM you can list the events and check `cs_etm` is listed.

```bash { target="ubuntu:latest" }
$ perf list | grep cs_etm
```

```output
cs_etm//           [Kernel PMU event]
cs_etm/autofdo/    [Kernel PMU event]
```

If nothing is found you will need to build a version of perf with Arm Coresight enabled. See https://docs.kernel.org/trace/coresight/coresight-perf.html

If `cs_etm/autofdo/` isn't found you will need to update the Linux Kernel and perf to 4.20 or later.

#### SPE

You need an Arm chip with the SPE extension. To check perf can record SPE you can list the events and check `arm_spe` is listed.

```bash { target="ubuntu:latest" }
$ perf list | grep arm_spe
```

```output
arm_spe_0//        [Kernel PMU event]
```

If `arm_spe` isn't found you will need to update the Linux Kernel and perf to 4.20 or later.

### Cycle Samples

Samples can be collected every cycle.

```bash { target="ubuntu:latest" }
perf record -e cycles:u -- ./executable
```

To verify samples have been collect you can check the report dump for `PERF_RECORD_SAMPLE` sections.

```bash { target="ubuntu:latest" } 
perf report -D | grep PERF_RECORD_SAMPLE
```

```output
7341932505720 0x3d8 [0x28]: PERF_RECORD_SAMPLE(IP, 0x1): 3827/3827: 0xffff8000813b4f34 period: 1 addr: 0
7341932515080 0x400 [0x28]: PERF_RECORD_SAMPLE(IP, 0x2): 3827/3827: 0xffffb00731c0 period: 1 addr: 0
7341932515900 0x428 [0x28]: PERF_RECORD_SAMPLE(IP, 0x2): 3827/3827: 0xffffb0073950 period: 1 addr: 0
7341932516620 0x450 [0x28]: PERF_RECORD_SAMPLE(IP, 0x2): 3827/3827: 0xffffb0073984 period: 5 addr: 0
7341932517340 0x478 [0x28]: PERF_RECORD_SAMPLE(IP, 0x2): 3827/3827: 0xffffb007399c period: 110 addr: 0
...
```

### ETM

Arm ETM can be collected using the following command.

```bash { target="ubuntu:latest" }
perf record -e cs_etm/@tmc_etr0/u -- ./executable
```

Arm ETM produces a lot of data and the `perf.data` file can end up very large. Compared to collecting samples it can thousands of times larger for the same executable. This can cause the next BOLT steps to take longer to complete and require more temporary hard drive space. See [Appendix A - Perf Record Size Rates](../appendix-a/) for more information.

One way to reduce the size is to use the ETM AutoFDO option. This works by recording with a strobing effect, i.e record ETM for a short time and then wait for a long period before recording another slice. This will collect roughtly 5000 times less data and is useful whem running really long benchmarks.

```bash { target="ubuntu:latest" }
perf record -e cs_etm/@tmc_etr0,autofdo/u -- ./executable
```

To verify ETM AUX trace have been collect you can check the report dump for `CoreSight ETM`.

```bash { target="ubuntu:latest" }
perf report -D | grep "CoreSight ETM"
```

```output
. ... CoreSight ETMV4I Trace data: size 0x1fff0 bytes
. ... CoreSight ETMV4I Trace data: size 0x1fff0 bytes
. ... CoreSight ETMV4I Trace data: size 0x1fff0 bytes
. ... CoreSight ETMV4I Trace data: size 0x1fff0 bytes
. ... CoreSight ETMV4I Trace data: size 0x1fff0 bytes
...
```

### SPE

Arm SPE can be collected using the following command.

```bash { target="ubuntu:latest" }
perf record -e arm_spe/branch_filter=1/u -- ./executable
```

To verify SPE AUX trace have been collect you can check the report dump for `ARM SPE`.

```bash { target="ubuntu:latest" }
perf report -D | grep "ARM SPE"
```

```output
. ... ARM SPE data: size 0x10000 bytes
. ... ARM SPE data: size 0x10000 bytes
. ... ARM SPE data: size 0x10000 bytes
. ... ARM SPE data: size 0x10000 bytes
. ... ARM SPE data: size 0x10000 bytes
...
```

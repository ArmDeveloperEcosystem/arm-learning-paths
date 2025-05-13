---
title: Setup
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Setup

For this tutorial, I will use a `c6g.metal` instances running Amazon linux 2023 (AL23). Since `SPE` requires support both in hardware and the operating system, instances running specific distributions or kernels may not allow SPE-based profiling. 

We can check the underlying Neoverse IP and operating system kernel version with the following commands. 

```bash
lscpu | grep -i "model name"
uname -r
```

Here we observe

```ouput
Model name:                           Neoverse-N1
6.1.134-150.224.amzn2023.aarch64
```

Next install the prerequisite packages with the following command. 

```bash
sudo dnf update -y
sudo dnf install perf git gcc cmake numactl-devel -y
```

Since the `linux` perf utility is a userspace process and SPE is a hardware feature in silicon, we use a built-in kernel module `arm_spe_pmu` to interact. Run the following command.

```bash
sudo modprobe arm_spe_pmu
```

## Run Sysreport

A handy python script is available to summarise your systems capabilities with regard to performance profiling. Install and run System Report python script (`sysreport`) using the [instructions in the learning path](https://learn.arm.com/learning-paths/servers-and-cloud-computing/sysreport/).

To check SPE is available on your system look at the `perf sampling` field. It should read `SPE` highlighted in green.

```output
...
Performance features:
  perf tools:          True
  perf installed at:   /usr/bin/perf
  perf with OpenCSD:   False
  perf counters:       6
  perf sampling:       SPE
  perf HW trace:       None
  perf paranoid:       -1
  kptr_restrict:       0
  perf in userspace:   disabled
```

## Confirm Arm_SPE Availability

Running the following command will confirm the availability of `arm_spe`. 

```output
sudo perf list "arm_spe*"
```

You should observe the following.

```output
List of pre-defined events (to be used in -e or -M):

  arm_spe_0//                                        [Kernel PMU event]
```

If `arm_spe` is not available on your configuration, the `perf c2c` workload without `SPE` will fail. For example you will observe the following. 

```output
$ perf c2c record
failed: memory events not supported
```

{{% notice Note %}}
If you are unable to use Arm SPE. It may be a restriction based on your cloud instance size or operating system. Generally, access to a full server (also known as metal instances) with a relatively new kernel is needed for Arm_SPE support. For more information, see the [perf-arm-spe manual page](https://man7.org/linux/man-pages/man1/perf-arm-spe.1.html)
{{% /notice %}}

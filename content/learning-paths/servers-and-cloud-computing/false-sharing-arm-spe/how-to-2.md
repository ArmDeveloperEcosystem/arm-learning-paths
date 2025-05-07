---
title: Setup
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Setup

For this tutorial, I will use a `c6g.metal` instances running Amazon linux 2023 (AL23).

We can check the underlying Neoverse IP and operating system with the following command. 

```bash
lscpu | grep -i "model name"
```

```ouput
Model name:                           Neoverse-N1
```

Check the kernel version with the following command
```bash
uname -r
```

```output
6.1.134-150.224.amzn2023.aarch64
```

Since the `linux` perf utility is a userspace process and SPE is a hardware feature in silicon, we use a built-in kernel module `arm_spe_pmu` to interact. Run the following command.

```bash
sudo modprobe arm_spe_pmu
```

### Install Dependencies

```bash
sudo dnf update -y
sudo dnf install perf git g++ cmake numactl-devel -y
```

## Running Sysreport

Install and run System Report python script ('sysreport`) from the [instructions in the learning path](https://learn.arm.com/learning-paths/servers-and-cloud-computing/sysreport/).

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
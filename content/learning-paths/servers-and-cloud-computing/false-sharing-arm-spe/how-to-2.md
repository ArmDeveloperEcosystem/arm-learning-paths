---
title: Configure your environment for Arm SPE profiling
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Select a system with SPE support

SPE requires both hardware and operating system support. Many cloud instances running Linux do not enable SPE-based profiling.

You need to identify a system that supports SPE using the information below. 

If you are looking for an AWS system, you can use a `c6g.metal` instance running Amazon Linux 2023 (AL2023). 

Check the underlying Neoverse processor and operating system kernel version with the following commands. 

```bash
lscpu | grep -i "model name"
uname -r
```

The output includes the CPU type and kernel release version:

```ouput
Model name:                           Neoverse-N1
6.1.134-152.225.amzn2023.aarch64
```

Next, install the prerequisite packages using the package manager:

```bash
sudo dnf update -y
sudo dnf install perf git gcc cmake numactl-devel -y
```

Linux Perf is a userspace process and SPE is a hardware feature. The Linux kernel must be compiled with SPE support or the kernel module named `arm_spe_pmu` must be loaded.

Run the following command to confirm if the SPE kernel module is loaded:

```bash
sudo modprobe arm_spe_pmu
```

If the module is not loaded (blank output), SPE may still be available.

Run this command to check if SPE is included in the kernel:

```bash
ls /sys/bus/event_source/devices/ | grep arm_spe
```

If SPE is available, the output is:

```output
arm_spe_0
```

If the output is blank then SPE is not available.

## Run Sysreport

You can install and run a Python script named Sysreport to summarize your system's performance profiling capabilities.

Refer to [Get ready for performance analysis with Sysreport](https://learn.arm.com/learning-paths/servers-and-cloud-computing/sysreport/) to learn how to install and run it.

Look at the Sysreport output and confirm SPE is available by checking the `perf sampling` field. 

If the printed value is SPE then SPE is available.

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

## Confirm Arm SPE is available to Perf

Run the following command to confirm SPE is available to Perf: 

```bash
sudo perf list "arm_spe*"
```

You should see the output below indicating the PMU event is available.

```output
List of pre-defined events (to be used in -e or -M):

  arm_spe_0//                                        [Kernel PMU event]
```

Assign capabilities to Perf by running:

```bash
sudo setcap cap_perfmon,cap_sys_ptrace,cap_sys_admin+ep $(which perf)
```

If `arm_spe` is not available because of your system configuration or if you don't have PMU permission, the `perf c2c` command will fail. 

To confirm Perf can access SPE run:

```bash
perf c2c record
```

The output showing the failure is:

```output
failed: memory events not supported
```

{{% notice Note %}}
If you are unable to use SPE it may be a restriction based on your cloud instance size or operating system.

Generally, access to a full server (also known as metal instances) with a relatively new kernel is needed for Arm SPE support. 

For more information about enabling SPE, see the [perf-arm-spe manual page](https://man7.org/linux/man-pages/man1/perf-arm-spe.1.html)
{{% /notice %}}

Continue to learn how to use Perf C2C on an example application.

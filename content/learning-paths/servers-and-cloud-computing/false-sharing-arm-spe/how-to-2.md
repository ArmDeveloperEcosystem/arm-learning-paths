---
title: Set up your environment for Arm SPE and Perf C2C profiling
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Select a system with SPE support

{{% notice Learning goal%}}
Before you can start profiling cache behavior with Arm SPE and Perf C2C, your system needs to meet a few requirements. In this section, you’ll learn how to check whether your hardware and kernel support Arm SPE, install the necessary tools, and validate that Linux Perf can access the correct performance monitoring events. By the end, your environment will be ready to record and analyze memory access patterns using `perf c2c` on an Arm Neoverse system.
{{% /notice %}}

SPE requires support from both your hardware and the operating system. Many cloud instances running Linux do not enable SPE-based profiling.

You need to identify a system that supports SPE using the information below. 

If you are looking for an AWS system, you can use a `c6g.metal` instance running Amazon Linux 2023 (AL2023). 

Check the underlying Neoverse processor and operating system kernel version with the following commands: 

```bash
lscpu | grep -i "model name"
uname -r
```

The output includes the CPU type and kernel release version:

```output
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

If the module is not loaded (and there is blank output), SPE might still be available.

Run this command to check if SPE is included in the kernel:

```bash
ls /sys/bus/event_source/devices/ | grep arm_spe
```

If SPE is available, the output you will see is:

```output
arm_spe_0
```

If the output is blank then SPE is not available.

## Run Sysreport

You can install and run a Python script named Sysreport to summarize your system's performance profiling capabilities.

See the Learning Path [Get ready for performance analysis with Sysreport](/learning-paths/servers-and-cloud-computing/sysreport/) to learn how to install and run it.

Look at the Sysreport output and confirm SPE is available by checking the `perf sampling` field. 

If the printed value is SPE, then SPE is available.

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

Run the following command to confirm SPE is available to `perf`: 

```bash
sudo perf list "arm_spe*"
```

You should see the output below indicating the PMU event is available.

```output
List of pre-defined events (to be used in -e or -M):

  arm_spe_0//                                        [Kernel PMU event]
```

Assign capabilities to `perf` by running:

```bash
sudo setcap cap_perfmon,cap_sys_ptrace,cap_sys_admin+ep $(which perf)
```

If `arm_spe` isn’t available due to your system configuration or limited PMU access, the `perf c2c` command will fail.

To confirm `perf` can access SPE, run:

```bash
perf c2c record
```

If SPE access is blocked, you’ll see output like this:

```output
failed: memory events not supported
```

{{% notice Note %}}
If you are unable to use SPE it might be a restriction based on your cloud instance size or operating system.

Generally, access to a full server (also known as metal instances) with a relatively new kernel is required for Arm SPE support. 

For more information about enabling SPE, see the [perf-arm-spe manual page](https://man7.org/linux/man-pages/man1/perf-arm-spe.1.html)
{{% /notice %}}

## Summary

You've confirmed that your system supports Arm SPE, installed the necessary tools, and verified that Perf C2C can access SPE events. You're now ready to start collecting detailed performance data using Perf C2C. In the next section, you’ll run a real application and use Perf C2C to capture cache sharing behavior and uncover memory performance issues.

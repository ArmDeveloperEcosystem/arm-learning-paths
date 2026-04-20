---
title: Assess OS kernel
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Step 1.0) Check whether the OS kernel is built with SPE

From the Getting Started section, you know you need to verify both the kernel and driver layers. Start by checking the kernel version:

```bash
uname -r
```
The output will be similar to:

```output
6.17.0-1010-aws
```

This AWS instance is running the standard Ubuntu 24.04 LTS Amazon Machine Image (AMI) provided through AWS Quick Start. The command output shows a Linux 6.17 kernel, and the `1010-aws` suffix indicates an AWS-specific build customized for the AWS environment.

Now check whether this kernel was built with SPE support enabled:

```bash
grep CONFIG_ARM_SPE_PMU /boot/config-$(uname -r) 2>/dev/null || true
```

The possible outputs are `y`, `m`, or `n`, meaning built-in support, module support, or no support.

- `y` indicates that the kernel was built with SPE support.
- `m` indicates that SPE is available as a loadable kernel module. This is the typical output for cloud instances.
- `n` means the kernel was **not** built with SPE support.

If the output from the previous command is `n`, **skip directly to Step 3.0**.

### Step 1.1) Check whether the kernel module is available

If your output was `y` or `m`, as shown below, the OS kernel includes SPE support. You still need to confirm that the driver layer is present and can be loaded.

```output
CONFIG_ARM_SPE_PMU             = <m or y>
```

Run the following command to check whether the loadable kernel module (driver) is available on the target:

```bash
modinfo arm_spe_pmu 2>/dev/null || echo "arm_spe_pmu not present for this kernel"
```

If you see output similar to the following, the kernel module is already available on your system.

```output
filename:       /lib/modules/6.17.0-1010-aws/kernel/drivers/perf/arm_spe_pmu.ko.zst
license:        GPL v2
author:         Will Deacon <will.deacon@arm.com>
description:    Perf driver for the ARMv8.2 Statistical Profiling Extension
srcversion:     3B6FCB5AD9B37B8BB9FF4A9
...
```

If so, run the following command to load the driver:

```bash
sudo modprobe arm_spe_pmu
lsmod | grep arm_spe_pmu
```

In Step 1.2, use Sysreport to review system-level metrics, including SPE status.

### Step 1.2) Run Sysreport

Follow the steps in the [Get ready for performance analysis with Sysreport guide](https://learn.arm.com/learning-paths/servers-and-cloud-computing/sysreport/) and run `sysreport` on your system:

```bash
python /src/sysreport.py 
```

This prints information about your system, including whether SPE is enabled. The `perf sampling` label shows SPE status. It also provides useful details for further debugging.

```output
System feature report:
  Collected:           2026-04-13 09:40:16.344396
  Script version:      2026-04-08 08:08:28.656402
  Running as root:     False
System hardware:
  Architecture:        ARMv8.4
  CPUs:                64
  CPU types:           64 x Arm Neoverse V1 r1p1
  cache info:          size, associativity, sharing
  cache line size:     64
  Caches:
    64 x L1D 64K 4-way 64b-line
    64 x L1I 64K 4-way 64b-line
    64 x L2U 1M 8-way 64b-line
    1 x L3U 32M 16-way 64b-line
  System memory:       126G
  Atomic operations:   True
  interconnect:        CMN-650 x 1
  NUMA nodes:          1
  Sockets:             1
OS configuration:
  Kernel:              6.17.0
  config:              /boot/config-6.17.0-1010-aws
  build dir:           /lib/modules/6.17.0-1010-aws/build
  uses atomics:        True
  page size:           4K
  huge pages:          2048kB: 0, 32768kB: 0, 64kB: 0, 1048576kB: 0
  transparent HP:      madvise
  MPAM configured:     False
  resctrl:             False
  Distribution:        Ubuntu 24.04.4 LTS
  libc version:        glibc 2.39
  boot info:           ACPI
  KPTI enforced:       False
  Lockdown:            landlock, lockdown, yama, integrity, apparmor
  Mitigations:         spectre_v2:CSV2, BHB; spec_store_bypass:Speculative Store Bypass disabled via prctl; spectre_v1:__user pointer sanitization
Performance features:
  perf tools:          True
  perf installed at:   /usr/lib/linux-tools/6.17.0-1010-aws/perf
  perf with OpenCSD:   False
  perf counters:       6
  perf sampling:       None
  perf HW trace:       None
  perf paranoid:       0
  CAP_PERFMON:         disabled
  kptr_restrict:       1
  perf in userspace:   disabled
  interconnect perf:   True
  /proc/kcore:         True
  /dev/mem:            True
  eBPF:
    kernel configured for BPF: True
    bpftool installed:         True
      bpftool v7.7.0 using libbpf v1.7 features: 
    bpftrace installed:        bpftrace v0.20.2


Actions that can be taken to improve performance tools experience:
  perf tools cannot decode hardware trace
    build with CORESIGHT=1
  non-invasive sampling (SPE) not enabled
    ensure APIC table describes SPE interrupt
    kernel module arm_spe_pmu.ko must be built
  hardware trace not enabled
    rebuild kernel with CONFIG_CORESIGHT
    ensure ACPI describes CoreSight trace fabric
```

In this example, the output shows `perf sampling:       None`, so continue to the next step.

---
title: Analyse the results
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Analysing the results

Sysreport will display an overview of the hardware configuration of the system. It is useful to know at quick glance whether or not a hardware feature is available, so that you can switch to a different system if necessary. For example, it might be expected for a certain hardware feature to be available on a given cloud instance but it isn't due to misconfiguration.

After running the tool, the report should be closely examined to ensure that the configuration is suitable for your needs. Some configuration changes may be required in order to get the system into the desired state for performance analysis; these could be as simple as modifying kernel parameters at run-time, or more involved changes such as recompiling the kernel with different kernel configuration options.

## Modifying the system configuration

In our AWS example from the previous page, the Sysreport tool indicated that the global kernel parameter `perf_event_paranoid` was too strict meaning that system-level events could not be monitored by non-privileged users:

```output
Actions that can be taken to improve performance tools experience:
  ...

  System-level events can only be monitored by privileged users
    set kernel.perf_event_paranoid=0

  ...
```

By listing all of the kernel parameters, we're able to see that `kernel.perf_event_paranoid` is set to 4:

```output
sudo sysctl -a | grep kernel.perf_event_paranoid
kernel.perf_event_paranoid = 4
```

According to the Linux kernel documentation:

```output
perf_event_paranoid:

Controls use of the performance events system by unprivileged
users (without CAP_SYS_ADMIN).  The default value is 2.

 -1: Allow use of (almost) all events by all users
     Ignore mlock limit after perf_event_mlock_kb without CAP_IPC_LOCK
>=0: Disallow ftrace function tracepoint by users without CAP_SYS_ADMIN
     Disallow raw tracepoint access by users without CAP_SYS_ADMIN
>=1: Disallow CPU event access by users without CAP_SYS_ADMIN
>=2: Disallow kernel profiling by users without CAP_SYS_ADMIN
```

Setting this kernel parameter to 0 will allow the [perf](https://learn.arm.com/install-guides/perf) tool to access to CPU events, kernel profiling, ftrace function tracepoint, and raw tracepoints:

```output
sudo sysctl kernel.perf_event_paranoid=0
kernel.perf_event_paranoid = 0

sudo sysctl -a | grep kernel.perf_event_paranoid
kernel.perf_event_paranoid = 0
```

Running the Sysreport tool again shows that the problem has been resolved:

```bash
System feature report:
  Collected:           2024-03-21 14:12:53.529899
  Script version:      2024-03-21 11:50:23.254919
  Running as root:     False
System hardware:
  Architecture:        ARMv8.4
  CPUs:                16
  CPU types:           16 x ARM Neoverse V1 r1p1
  cache info:          size, associativity, sharing
  cache line size:     64
  Caches:
    16 x L1D 64K 4-way 64b-line
    16 x L1I 64K 4-way 64b-line
    16 x L2U 1M 8-way 64b-line
    1 x L3U 32M 16-way 64b-line
  System memory:       30.8G
  Atomic operations:   True
  interconnect:        <unknown> x 1
  NUMA nodes:          1
  Sockets:             1
OS configuration:
  Kernel:              6.5.0
  config:              /boot/config-6.5.0-1015-aws
  32-bit support:      True
  build dir:           /lib/modules/6.5.0-1015-aws/build
  uses atomics:        True
  huge pages:          False
    transparent:       madvise
  MPAM configured:     False
  resctrl:             False
  Distribution:        Ubuntu 22.04.3 LTS
  libc version:        glibc 2.35
  boot info:           ACPI
  KPTI enabled:        False
  Lockdown:            landlock, lockdown, yama, integrity, apparmor
  Mitigations:         spectre_v2:CSV2, BHB; spec_store_bypass:Speculative Store Bypass disabled via prctl; spectre_v1:__user pointer sanitization
Performance features:
  perf tools:          True
  perf installed at:   /usr/lib/linux-tools/6.5.0-1015-aws/perf
  perf with OpenCSD:   False
  perf counters:       2
  perf sampling:       None
  perf HW trace:       None
  perf paranoid:       0
  perf in userspace:   disabled
  interconnect perf:   None
  /proc/kcore:         True
  /dev/mem:            True
Actions that can be taken to improve performance tools experience:
  perf tools cannot decode hardware trace
    build with CORESIGHT=1
  non-invasive sampling (SPE) not enabled
    ensure APIC table describes SPE interrupt
    kernel module arm_spe_pmu.ko must be built
  hardware trace not enabled
    rebuild kernel with CONFIG_CORESIGHT
    ensure ACPI desribes CoreSight trace fabric
```
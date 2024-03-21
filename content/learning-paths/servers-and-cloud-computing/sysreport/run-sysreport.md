---
title: Run Sysreport
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Using the tool

Sysreport is a system capability reporting tool that gives application developers a quick summary of what performance features are available on the system. It aims to report the system configuration in a way that is focused on performance analysis.

This tool is aimed at anyone trying to profile performance on Arm-based systems; this includes cloud instances, bare metal servers, and small devices such as developer boards and Raspberry Pi devices.

After running the tool, a summary report is generated and displayed on screen. Information reported by the tool includes hardware configuration, operating system configuration (build time), and other configuration settings that can be changed. By default, the tool displays advice about possible configuration changes that can be made in order to improve its ability to collect performance information from the system; to disable this, use the '--no-advice' option.

Example use cases for this tool include:
* As a developer, I want to know if my cloud instance supports a particular performance feature I require, so that I am able to debug a performance problem
* As a developer, I want a quick single page summary of my system's performance configuration, so that I don't have to run lots of different commands manually to gather what I need
* As a developer, I would like to know suggested configuration changes I can make to my system, so that I can improve my ability to collect performance information

## Running the tool

* Run the tool on an example system and mention what the system config is:

To run Sysreport, use the following command:
```console
python sysreport.py
```

In this example we're using an Arm Neoverse N1 System Development Platform (N1SDP), an enterprise class reference board based on the Neoverse N1 core, running Ubuntu 20.04.6 LTS.

Example output is shown below:

```output
System feature report:
  Collected:           2024-03-20 12:24:18.102663
  Script version:      2024-03-20 11:42:11.356472
  Running as root:     False
System hardware:
  Architecture:        ARMv8.2
  CPUs:                4
  CPU types:           4 x ARM Neoverse N1 r1p0
  cache info:          size, associativity, sharing
  cache line size:     64
  Caches:
    4 x L1D 64K 4-way 64b-line
    4 x L1I 64K 4-way 64b-line
    4 x L2U 1M 8-way 64b-line
    2 x L3U 1M 8-way 64b-line
    1 x L4U 8M 16-way 64b-line
  System memory:       15.6G
  Atomic operations:   True
  interconnect:        CMN-600 x 1
  NUMA nodes:          1
  Sockets:             1
OS configuration:
  Kernel:              5.18.4+
  config:              /boot/config-5.18.4+
  32-bit support:      True
  build dir:           /lib/modules/5.18.4+/build
  uses atomics:        True
  huge pages:          False
    transparent:       madvise
  MPAM configured:     False
  resctrl:             False
  Distribution:        Ubuntu 20.04.6 LTS
  libc version:        glibc 2.29
  boot info:           ACPI
  KPTI enabled:        False
  Lockdown:            landlock, lockdown, yama, integrity, apparmor
  Mitigations:         spectre_v2:CSV2, BHB; spectre_v1:__user pointer sanitization
Performance features:
  perf tools:          True
  perf installed at:   /usr/lib/linux-tools/5.18.4+/perf
	not a dynamic executable
  perf with OpenCSD:   False
  perf counters:       6
  perf sampling:       SPE
  perf HW trace:       ETM
  perf paranoid:       0
  perf in userspace:   disabled
  interconnect perf:   True
  /proc/kcore:         True
  /dev/mem:            True
	not a dynamic executable
Actions that can be taken to improve performance tools experience:
  perf tools cannot decode hardware trace
    build with CORESIGHT=1
```

Here's another example using an AWS EC2 cloud instance, running Ubuntu 22.04.3 LTS:

```output
System feature report:
  Collected:           2024-03-21 13:37:51.248565
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
  perf tools:          False
  perf installed at:   /usr/lib/linux-tools/6.5.0-1015-aws/perf (does not exist)
ldd: /usr/lib/linux-tools/6.5.0-1015-aws/perf: No such file or directory
  perf with OpenCSD:   False
  perf counters:       None
  perf sampling:       None
  perf HW trace:       None
  perf paranoid:       4
  perf in userspace:   disabled
  interconnect perf:   None
  /proc/kcore:         True
  /dev/mem:            True
Actions that can be taken to improve performance tools experience:
  perf tools not installed
    install perf package
    or build from kernel sources
  System-level events can only be monitored by privileged users
    set kernel.perf_event_paranoid=0
  Hardware perf events are not available
    ensure APIC table describes PMU interrupt
  non-invasive sampling (SPE) not enabled
    ensure APIC table describes SPE interrupt
    kernel module arm_spe_pmu.ko must be built
  hardware trace not enabled
    rebuild kernel with CONFIG_CORESIGHT
    ensure ACPI desribes CoreSight trace fabric
```
---
layout: learningpathall
title: WindowsPerf
weight: 2
---

# Overview

[WindowsPerf](https://github.com/arm-developer-tools/windowsperf) is a (Linux [perf](https://perf.wiki.kernel.org) inspired) Windows on Arm performance profiling tool. Profiling is based on ARM64 PMU and its hardware counters. WindowsPerf supports the counting model for obtaining aggregate counts of occurrences of special events, and sampling model for determining the frequencies of event occurrences produced by program locations at the function, basic block, and/or instruction levels.

Learn more in this [blog](https://community.arm.com/arm-community-blogs/b/infrastructure-solutions-blog/posts/announcing-windowsperf) announcing the first release.

## WindowsPerf architecture

`WindowsPerf` is composed of two main components:
- [wperf](https://github.com/arm-developer-tools/windowsperf/tree/main/wperf) a command line interface (CLI) sometimes referred as "user-space app" and
- [wperf-driver](https://github.com/arm-developer-tools/windowsperf/tree/main/wperf-driver) a (signed) Kernel-Mode Driver Framework (KMDF) driver.

## WindowsPerf releases

You can find all binary releases of `WindowsPerf` [here](https://github.com/arm-developer-tools/windowsperf/releases).

# Installation

For installation instructions see the [install guide](/install-guides/wperf).

## Using WindowsPerf

For a list of all available options, enter:
```command
wperf -h
```

## List available events

WindowsPerf uses Arm processor `Performance Monitoring Unit` (`PMU`) counters to generate its data. The available `events` that can be profiled will vary per target.

To generate a list of available events, use:
```command
wperf list
```

The output should be similar to:

```output
List of pre-defined events (to be used in -e)

        Alias Name              Raw Index  Event Type
        ==========              =========  ==========
        sw_incr                      0x00  [core PMU event]
        l1i_cache_refill             0x01  [core PMU event]
...

List of supported metrics (to be used in -m)

        Metric  Events
        ======  ======
        dcache  {l1d_cache,l1d_cache_refill,l2d_cache,l2d_cache_refill,inst_retired}
        dtlb    {l1d_tlb,l1d_tlb_refill,l2d_tlb,l2d_tlb_refill,inst_retired}
        icache  {l1i_cache,l1i_cache_refill,l2i_cache,l2i_cache_refill,inst_retired}
...
```

{{% notice  Note%}}
You can extend `wperf list` command output with additional information like event and metrics description with `-v` command line option.
{{% /notice %}}

## Obtain information about wperf configuration

Command line option `test` prints on screen various `wperf` configuration settings:

```command
wperf test
```

```output
        Test Name                                           Result
        =========                                           ======
        request.ioctl_events [EVT_CORE]                     False
        request.ioctl_events [EVT_DSU]                      False
        request.ioctl_events [EVT_DMC_CLK/EVT_DMC_CLKDIV2]  False
        pmu_device.vendor_name                              Arm Limited
        pmu_device.product_name                             neoverse-n1
        pmu_device.product_name(extended)                   Neoverse N1 (neoverse-n1), armv8.1, pmu_v3
        pmu_device.product []                               armv8-a,armv9-a,neoverse-n1,neoverse-n2,neoverse-n2-r0p0,neoverse-n2-r0p1,neoverse-n2-r0p3,neoverse-v1
        pmu_device.m_product_alias                          (neoverse-n2-r0p0:neoverse-n2),(neoverse-n2-r0p1:neoverse-n2)
        pmu_device.events_query(events) [EVT_CORE]          110
        pmu_device.events_query(events) [EVT_DSU]           9
        pmu_device.events_query(events) [EVT_DMC_CLK]       3
        pmu_device.events_query(events) [EVT_DMC_CLKDIV2]   26
        PMU_CTL_QUERY_HW_CFG [arch_id]                      0x000f
        PMU_CTL_QUERY_HW_CFG [core_num]                     0x0050
        PMU_CTL_QUERY_HW_CFG [fpc_num]                      0x0001
        PMU_CTL_QUERY_HW_CFG [gpc_num]                      0x0006
        PMU_CTL_QUERY_HW_CFG [total_gpc_num]                0x0006
        PMU_CTL_QUERY_HW_CFG [part_id]                      0x0d0c
        PMU_CTL_QUERY_HW_CFG [pmu_ver]                      0x0004
        PMU_CTL_QUERY_HW_CFG [rev_id]                       0x0001
        PMU_CTL_QUERY_HW_CFG [variant_id]                   0x0003
        PMU_CTL_QUERY_HW_CFG [vendor_id]                    0x0041
        PMU_CTL_QUERY_HW_CFG [midr_value]                   0x000000000000413fd0c1
...
```

{{% notice  Note%}}
You can output `wperf test` command in JSON format. Use `--json` command line option to enable JSON output.
{{% /notice %}}

## Obtain plain text information about specified event, metric, or group of metrics.

Command line option `man` prints on screen information about specified event, metric, or group of metrics.

```command
wperf man l1d_cache_mpki
```

```output
CPU
    neoverse-n1
NAME
    l1d_cache_mpki - L1D Cache MPKI
EVENTS
    inst_retired, l1d_cache_refill
DESCRIPTION
    This metric measures the number of level 1 data cache accesses missed per
    thousand instructions executed.
FORMULA
    l1d_cache_refill / inst_retired * 1000
UNIT
    MPKI
```

## Generate sample profile

Specify the `event` to profile with `-e`. Groups of events, known as `metrics` can be specified with `-m`.

For example, generate a report for CPU core 0 (`-c 0`) for two seconds (`sleep 2`) with:
```command
wperf stat -e cpu_cycles -m icache -c 0 sleep 2
```
This will output a report similar to:
```output
counting ... done

Performance counter stats for core 0, no multiplexing, kernel mode excluded, on Arm Limited core implementation:
note: 'e' - normal event, 'gN' - grouped event with group number N, metric name will be appended if 'e' or 'g' comes from it

        counter value  event name        event idx  event note
        =============  ==========        =========  ==========
            7,408,075  cycle             fixed      e
            2,271,166  l1i_cache         0x14       g0,icache
              126,875  l1i_cache_refill  0x01       g0,icache
                    0  l2i_cache         0x27       g0,icache
                    0  l2i_cache_refill  0x28       g0,icache
            6,247,674  inst_retired      0x08       g0,icache
            7,408,075  cpu_cycles        0x11       e

               2.281 seconds time elapsed
```

{{% notice  Note%}}
You can output `wperf stat` command in JSON format. Use `--json` command line option to enable JSON output.
{{% /notice %}}


Example `wperf stat` command use cases are provided in the WindowsPerf [documentation](https://github.com/arm-developer-tools/windowsperf/tree/main/wperf#counting-model).

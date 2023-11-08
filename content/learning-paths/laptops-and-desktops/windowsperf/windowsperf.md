---
layout: learningpathall
title: WindowsPerf
weight: 2
---

# Overview

[WindowsPerf](https://gitlab.com/Linaro/WindowsPerf/windowsperf) is (Linux [perf]([perf](https://perf.wiki.kernel.org)) inspired) Windows on Arm performance profiling tool. Profiling is based on ARM64 PMU and its hardware counters. WindowsPerf supports the counting model for obtaining aggregate counts of occurrences of special events, and sampling model for determining the frequencies of event occurrences produced by program locations at the function, basic block, and/or instruction levels.

Learn more in this [blog](https://community.arm.com/arm-community-blogs/b/infrastructure-solutions-blog/posts/announcing-windowsperf) announcing the first release.

## WindowsPerf architecture

`WindowsPerf` is composed of two main components:
- [wperf](https://gitlab.com/Linaro/WindowsPerf/windowsperf/-/tree/main/wperf) a command line interface (CLI) sometimes referred as "user-space app" and
- [wperf-driver](https://gitlab.com/Linaro/WindowsPerf/windowsperf/-/tree/main/wperf-driver). `wperf-driver` is a (signed) Kernel-Mode Driver Framework (KMDF) driver.

## WindowsPerf releases

You can find all binary releases of `WindowsPerf` [here](https://gitlab.com/Linaro/WindowsPerf/windowsperf/-/releases).

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

## Generate sample profile

Specify the `event` to profile with `-e`. Groups of events, known as `metrics` can be specified with `-m`.

For example, generate a report for Core 0 (`-c 0`) for two seconds (`-d 2`) with:
```command
wperf stat -e cpu_cycles -m icache -c 0 -d 2
```
This will output a report similar to:
```output
        counter value  event name        event idx  event note
        =============  ==========        =========  ==========
          649,973,325  cycle             fixed      e
          277,788,076  l1i_cache         0x14       g0,icache
            7,415,699  l1i_cache_refill  0x01       g0,icache
                    0  l2i_cache         0x27       g0,icache
                    0  l2i_cache_refill  0x28       g0,icache
          813,129,394  inst_retired      0x08       g0,icache
          649,973,325  cpu_cycles        0x11       e
```
Example use cases are provided in the WindowsPerf [documentation](https://gitlab.com/Linaro/WindowsPerf/windowsperf/-/blob/main/wperf/README.md#counting-model).

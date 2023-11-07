---
layout: learningpathall
title: WindowsPerf
weight: 2
---
[WindowsPerf](https://gitlab.com/Linaro/WindowsPerf/windowsperf) is a port of the popular Linux [perf](https://perf.wiki.kernel.org) tool for performance analysis.

Learn more in this [blog](https://community.arm.com/arm-community-blogs/b/infrastructure-solutions-blog/posts/announcing-windowsperf) announcing the first release.

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

```console
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
Example use cases are provided in the WindowsPerf [documentation](https://gitlab.com/Linaro/WindowsPerf/windowsperf/-/blob/main/wperf/README.md#counting-model).

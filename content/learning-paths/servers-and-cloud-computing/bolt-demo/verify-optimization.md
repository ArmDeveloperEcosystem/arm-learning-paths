---
title: Verify BOLT optimization results
weight: 10

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Verify optimization with runtime

{{% notice Note %}}
The example below uses a [BRBE profiling](/learning-paths/servers-and-cloud-computing/bolt-demo/brbe/) optimized binary. You can apply the same verification steps to binaries optimized using the other BOLT profiling methods.
{{% /notice %}}

First, compare the runtime of the original and optimized BubbleSort binaries. A shorter runtime provides an initial indication that BOLT improved the code layout.

```bash { command_line="user@host | 2-4,6-8"}
time out/bsort
  Bubble sorting 10000 elements
  280 ms (first=100669 last=2147469841)
  out/bsort  0.28s user 0.00s system 99% cpu 0.282 total
time out/bsort.opt.brbe
  Bubble sorting 10000 elements
  147 ms (first=100669 last=2147469841)
  out/bsort.opt.brbe  0.15s user 0.00s system 99% cpu 0.148 total
```

In this example, the optimized binary runs in about 147 ms, compared with 280 ms for the original binary. This corresponds to roughly a 2× speedup.
The improvement is large because the example program intentionally creates poor code locality. Real applications typically show smaller but still meaningful improvements after BOLT optimization.


## Verify optimization with hardware metrics
Next, apply the [TopDown Methodology](https://developer.arm.com/documentation/109542/02/Arm-Topdown-methodology) again to verify that BOLT improved the code layout.
The runtime comparison shows the performance impact, but the TopDown metrics reveal how the optimization affects processor behavior.
Run the same tool used earlier when evaluating whether the program was a good BOLT candidate. This time, run it on the optimized binary, for example, the BRBE-optimized version.

{{< tabpane code=true >}}
  {{< tab header="topdown-tool" language="bash" output_lines="2-21">}}
    topdown-tool ./out/bsort.opt.brbe
      CPU Neoverse V1 metrics
      ├── Stage 1 (Topdown metrics)
      │   └── Topdown Level 1 (Topdown_L1)
      │       └── ┏━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━┓
      │           ┃ Metric          ┃ Value ┃ Unit ┃
      │           ┡━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━┩
      │           │ Backend Bound   │ 11.19 │ %    │
      │           │ Bad Speculation │ 24.86 │ %    │
      │         » │ Frontend Bound  │ 36.10 │ %    │ «
      │           │ Retiring        │ 28.42 │ %    │
      │           └─────────────────┴───────┴──────┘
      └── Stage 2 (uarch metrics)
          ├── Misses Per Kilo Instructions (MPKI)
          │   └── ┏━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
          │       ┃ Metric                  ┃ Value ┃ Unit                          ┃
          │       ┡━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
          │       │ Branch MPKI             │ 9.799 │ misses per 1,000 instructions │
          │     » │ L1I Cache MPKI          │ 0.019 │ misses per 1,000 instructions │ «
          │       └─────────────────────────┴───────┴───────────────────────────────┘
          ...
  {{< /tab >}}
  {{< tab header="perf stat" language="bash" output_lines="2-10">}}
    perf stat -e instructions,L1-icache-misses:u ./out/bsort.opt.brbe
      Performance counter stats for './out/bsort.opt.brbe':

          982204165 instructions
               3807 L1-icache-misses

        0.147606245 seconds time elapsed

        0.147644000 seconds user
        0.000000000 seconds sys
  {{< /tab >}}
{{< /tabpane >}}

Compare these metrics with the earlier results collected from the original binary. After optimization, both frontend bound and L1I MPKI should decrease.

In this example, the optimized program is 36% frontend bound, down from 55%. The L1I cache MPKI drops to nearly 0, which indicates a significant improvement in instruction locality. 

This value is unusually low because the example program intentionally creates poor code locality.

The Branch MPKI also decreases—from 16 to about 10—because BOLT can improve branch prediction. It uses profile data to adjust code layout and swap fall-through and taken paths when beneficial.

You can also compute the MPKI values manually using `perf stat`, as described in the [Good BOLT Candidates](/learning-paths/servers-and-cloud-computing/bolt-demo/good-candidates/) section.

## Summary

In this learning path, you learned how to use BOLT to optimize binary code layout using several profiling methods. The optimized binaries improved instruction locality, reduced frontend stalls, and delivered measurable performance gains.

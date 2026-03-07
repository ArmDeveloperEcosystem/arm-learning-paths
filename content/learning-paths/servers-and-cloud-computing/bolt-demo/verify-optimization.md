---
title: Verify Optimization
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Verify with runtime

{{% notice Note %}}
The example below uses a [BRBE](../brbe) optimized binary. The same verification applies to all BOLT profiling methods.
{{% /notice %}}

We start by checking the runtime of the original and optimized BubbleSort binaries. A speedup is the first indication that BOLT improved the layout.

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

In this example, we see a first indication of improvement from the speedup. It is large, around 2x, because the input program is intentionally pathological. Real applications may see smaller improvements.


### Verify with hardware metrics
We now apply the [TopDown Methodology](https://developer.arm.com/documentation/109542/02/Arm-Topdown-methodology) again to confirm that BOLT improved the layout.
Runtime shows the effect, but TopDown confirms how the changes appear in the hardware metrics.

We run the same tool that we used when checking whether the input program was a good candidate, but this time we check the optimized binary, for example the BRBE-optimized one.

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

We compare these metrics with the earlier results. Front-end bound and L1I MPKI should be lower after optimization.

We now see that the optimized program is **36%** front-end bound, down from 55%. In addition, the L1I MPKI is close to **0**, showing that code layout improved. This result is unusually low because the input program is intentionally pathological.

The Branch MPKI also dropped to **10** from 16 because BOLT can improve branch prediction by swapping the fall-through and taken paths based on profile data.

We can also compute these MPKIs manually using `perf stat`, as described in the [Good BOLT Candidates](../good-candidates) page.

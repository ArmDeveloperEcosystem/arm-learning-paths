---
title: "Optimize the application"
weight: 5
layout: "learningpathall"
---

## Performance Optimization

You can use software prefetching to improve performance. 


The code to enable prefetching is:

```C++
        #if defined(ENABLE_PREFETCH) && defined (DIST)
            const int prefetch_distance = DIST * kStride * kLineSize;
            __builtin_prefetch(&buffer[position + prefetch_distance], 0, 0);
        #endif
```

To enable data prefetching, recompile the application with 2 defines. You can experiment with values of `DIST` to see how performance is impacted. 

The white paper shows a graph of various values of DIST and explains how the performance saturates at a `DIST` value of 40 on the N1SDP hardware. The example below uses 100 for `DIST`.

To compile with prefetching:

```console
g++ -g -O3 -DENABLE_PREFETCH -DDIST=100 stride.cpp -o stride
```

Run the `perf` command again to count instructions and cycles. 

```console
perf stat -e instructions,cycles ./stride
```

The output is similar to:

```output
Performance counter stats for './stride':

    14,002,762,166      instructions:u            #    0.63  insn per cycle
    22,106,858,662      cycles:u

       9.895357134 seconds time elapsed

       9.874959000 seconds user
       0.020003000 seconds sys
```

The time to run the original application was more than 20 seconds and with prefetching the time drops to under 10 seconds.

The table below shows the improvements in instructions, cycles, and IPC.

| Metrics | Baseline | Optimized |
| ----------- | ----------- |----------- |
| Instructions | 10,002,762,164 | 14,002,762,166 | 
| Cycles       | 45,157,063,927 | 22,106,858,662 | 
| IPC          | 0.22 | 0.63 | 
| Runtime      | 20.1 sec | 9.9 sec | 

As outlined in the white paper, the IPC nearly triples and the runtime halves. 

You can review how the other metrics change with prefetching enabled. 

{{% notice Note %}}
Neoverse N1 servers and cloud instances will not demonstrate as much performance improvement because they have higher memory bandwidth, but you will be able to see performance improvement as a result of enabling prefetching.
{{% /notice %}}


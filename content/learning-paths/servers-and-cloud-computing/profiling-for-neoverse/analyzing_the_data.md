---
title: Analyze the data
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Retiring performance

The _Retiring_ metric defines the percentage of the slot capacity that is doing
useful work. This metric provides the hardware-centric “Utilization ×
Efficiency” measure that we proposed earlier, representing two of the three
aspects of software performance. Your goal when optimizing for the hardware is
to make this number as high as possible, which indicates the best usage of the
available processing resources.

A high retiring metric means only that you are using the available hardware
efficiently. There might still be optimization opportunities in the software
that improve the effectiveness of your algorithms, and you can use other
hardware metrics to guide this work.

Optimizations to consider for software that has a high retiring rate include:

* Reducing redundant processing in the algorithm.
* Reducing redundant data movement in the algorithm.
* Vectorizing heavily used functions that have not been vectorized.

## Frontend performance

The role of the frontend is to issue micro-ops fast enough to keep the backend
queues filled with work. Software is described as frontend bound when the
frontend cannot issue a micro-op when there is free space in the backend queue
to accept one. The _Frontend bound_ metric defines the percentage of slot
capacity lost to frontend stalls.

Consider the following optimizations for software that is frontend bound:

* Reducing code size.
* Improving the memory locality of instruction accesses.

## Bad speculation

In addition to instruction decode stalls, some percentage of the available
issue capacity is wasted on cycles that are used either recovering from
mispredicted branches, or executing speculative micro-ops that were
subsequently cancelled. The _Bad speculation_ metric defines the percentage of
slot capacity lost to these effects.

Consider the following optimizations for software that is suffering from bad
speculation:

* Improving predictability of branches.
* Converting unpredictable branches into conditional select instructions.

## Backend performance

Backend pipelines can stall, making the issue queue unable to accept a new
micro-op. This occurs due to the presence of a slow multi-cycle operation,
or a stalling effect such as a cache miss. Software is described as backend
bound when the backend queue cannot accept a micro-op when the frontend has one
ready to issue. The _Backend bound_ metric defines the percentage of slot
capacity lost to these effects.

Consider the following optimizations for software that is backend bound:

* Reducing the size of application data structures and data types.
* Improving the memory locality of data accesses.
* Reducing use of slow multi-cycle instructions.
* Swapping instructions to move work away from issue queues that are under the
  most load.

## Stall metrics

The most common causes of stalls are cache misses and branch mispredictions. To make it easier to understand the impact of stalls, two forms of miss metrics are given:

* _Miss rate_ metrics tell you the percentage of misses for that specific operation type. These metrics tell you how effectively a particular cache or prediction unit is performing.
* _Misses per thousand instruction_ (MPKI) metrics tell you how many misses of that type occurred, on average, when running 1000 instructions of any type. These metrics tell you how significant the impact of a particular type of miss is, given the instruction makeup of the program.

For example, you measure a _Branch mispredict rate_ of 45% when profiling, which tells you that 45% of branches are mispredicted. This is a clear sign that the branch predictor is struggling, so improving branches can be an optimization candidate. However, when you check the _Branch MPKI_ metric you see that you only have 0.8 mispredictions for every 1000 instructions in the sample. Even though branches are not predicting well, optimizing will not bring
significant improvements because branches are only a small proportion of the instruction mix.

## Optimization checklist

There is no right way to profile and optimize, but the top-down data presentation gives you a systematic way to find optimization opportunities.

Here is our optimization checklist:

1. Check the compiler did a good job:
    * Disassemble your most significant functions.
    * Verify that the generated code looks efficient.

1. Check the functions that are the most frontend bound:
    * If you see high instruction cache miss rate, apply profile-guided optimization to reduce the code size of less important functions. This frees
  up more instruction cache space for the important hot-functions.
    * If you see high instruction TLB misses, apply code layout optimization, using tools such as [Bolt][2]. This improves locality of code accesses, reducing the number of TLB misses.

    [2]: https://learn.arm.com/learning-paths/servers-and-cloud-computing/bolt/overview/

1. Check the functions that have the highest bad speculation rate:

    * If you see high branch mispredict rates, use a more predictable branching pattern, or change the software to avoid branches by using conditional selects.

1. Check the functions that are the most backend bound:

    * If you see high data cache misses, reduce data size, reduce data copies and moves, and improve access locality.
    * If you see high pipeline congestion on a specific issue queue, alter your software to move load a different queue. For example, converting run-time computation to a lookup table if your program is arithmetic limited.

1. Check the most retiring bound functions:

    * Apply SIMD vectorization to process more work per clock.
    * Look for higher-level algorithmic improvements.
---
title: Profiling goals
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Profiling goals

The main goal of our performance analysis methodology is to attribute unused or
unneeded slot issues to specific causes, to give you feedback about what is
causing your software to run slowly.

### Retiring performance

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

### Frontend performance

The role of the frontend is to issue micro-ops fast enough to keep the backend
queues filled with work. Software is described as frontend bound when the
frontend cannot issue a micro-op when there is free space in the backend queue
to accept one. The _Frontend bound_ metric defines the percentage of slot
capacity lost to frontend stalls.

Consider the following optimizations for software that is frontend bound:

* Reducing code size.
* Improving the memory locality of instruction accesses.

### Bad speculation

In addition to instruction decode stalls, some percentage of the available
issue capacity is wasted on cycles that are used either recovering from
mispredicted branches, or executing speculative micro-ops that were
subsequently cancelled. The _Bad speculation_ metric defines the percentage of
slot capacity lost to these effects.


Consider the following optimizations for software that is suffering from bad
speculation:

* Improving predictability of branches.
* Converting unpredictable branches into conditional select instructions.

### Backend performance

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

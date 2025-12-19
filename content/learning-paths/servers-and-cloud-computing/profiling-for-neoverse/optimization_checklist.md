---
title: Optimization checklist
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Optimization checklist

There is no single way to profile and optimize, but the top-down data presentation gives you a systematic way to find optimization opportunities.

Here is a suggested optimization checklist:

1. Check the compiler did a good job. Disassemble your most significant functions and verify that the generated code looks efficient.

1. Check the functions that are the most frontend bound:
    
    * If you see high instruction cache miss rate, apply profile-guided optimization to reduce the code size of less important functions. This frees up more instruction cache space for the important hot-functions.
    * If you see high instruction TLB misses, apply code layout optimization, using tools such as [Bolt](/learning-paths/servers-and-cloud-computing/bolt/overview/). This improves locality of code accesses, reducing the number of TLB misses.

1. Check the functions that have the highest bad speculation rate. If you see high branch mispredict rates, use a more predictable branching pattern, or change the software to avoid branches by using conditional selects.

1. Check the functions that are the most backend bound:

    * If you see high data cache misses, reduce data size, reduce data copies and moves, and improve access locality.
    * If you see high pipeline congestion on a specific issue queue, alter your software to move load a different queue. For example, converting run-time computation to a lookup table if your program is arithmetic limited.

1. Check the most retiring bound functions:

    * Apply SIMD vectorization to process more work per clock.
    * Look for higher-level algorithmic improvements.

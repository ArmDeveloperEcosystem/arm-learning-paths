---
title: Conclusion
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Conclusion and further reading

Porting SIMD code between architectures can be a daunting process, often requiring many hours of studying multiple ISAs in online resources or ISA manuals that run into thousands of pages. 

The primary focus of this Learning Path is to optimize the existing algorithm directly with SIMD intrinsics, without altering the algorithm or data layout. While reordering data to align with native Arm instructions can offer performance benefits, this is outside the scope of this Learning Path. 

If you are interested in data layout strategies to further enhance performance on Arm, see the Learning Path *Optimize SIMD code with vectorization-friendly data layout* linked to in the **Next Steps** section at the of this Learning Path. 

Using SIMD.info can be instrumental in reducing the amount of time spent in this process, providing a centralized and user-friendly resource for finding NEON equivalents to intrinsics of other architectures. It saves considerable time and effort by offering detailed descriptions, prototypes, and comparisons directly, eliminating the need for extensive web searches and manual lookups.

While porting between vectors of different sizes is more complex, work is underway to complete the integration of SVE and SVE2 Arm extensions and allow matching them with AVX512 intrinsics, as they both use predicate masks.

You can check **[SIMD.info](https://simd.info)** for updates.

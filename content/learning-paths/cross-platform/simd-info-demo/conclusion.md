---
title: Conclusion
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Conclusion and Additional Resources

Porting SIMD code between architecture can be a daunting process, in many cases requiring many hours of studying multiple ISAs in online resources or ISA manuals of thousands pages.

Using **[SIMD.info](https://simd.info)** can be be instrumental in reducing the amount of time spent in this process, providing a centralized and user-friendly resource for finding **NEON** equivalents to intrinsics of other architectures. It saves considerable time and effort by offering detailed descriptions, prototypes, and comparisons directly, eliminating the need for extensive web searches and manual lookups.

While porting between vectors of different sizes is more complex, work is underway -at the time of writing this guide- to complete integration of **SVE**/**SVE2** Arm extensions and allow matching them with **AVX512** intrinsics, as they are both using predicate masks.

Please check **[SIMD.info](https://simd.info)** regularly for updates on this.

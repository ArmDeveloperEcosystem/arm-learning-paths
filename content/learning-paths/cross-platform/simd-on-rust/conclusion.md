---
title: Conclusion
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

You have seen a few examples of writing SIMD code on Arm with Rust. 

Performance wise, between C and Rust there is no difference really. Rust is perfectly capable of generating the same assembly code as C in most cases.

If you want to program optimal SIMD code using the Arm ASIMD/Neon intrinsics, then `std::arch` is the most obvious choice.

If however, your approach needs to be as portable as possible and you don't want to spend time providing multiple implementations for each architecture, then `std::simd` is a very viable alternative, even though it's not part of the stable compiler yet.


---
title: Conclusion
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

You have now seen a few examples of writing SIMD code on Arm with Rust. 

Performance-wise, there is little difference between C and Rust as Rust is perfectly capable of generating the same assembly code as C in most cases. That said, if you want to program optimal SIMD code using the Arm ASIMD/Neon intrinsics, `std::arch` is the most obvious choice. If, however, your approach needs to be as portable as possible and you don't want to spend time providing multiple implementations for each architecture then `std::simd` is a very viable alternative (even though it's not part of the stable compiler yet).


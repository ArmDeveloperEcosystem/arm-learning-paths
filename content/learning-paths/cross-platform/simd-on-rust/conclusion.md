---
title: Conclusion
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

You have seen a few aspects of writing SIMD code on Arm with Rust. In the end which is better, C or Rust?

Performance-wise, there is no difference really, as you have seen. Rust is perfectly capable of generating the same assembly code as C in most cases.

If you want to program optimal SIMD code using the Arm ASIMD/Neon intrinsics, then `std::arch` is the obvious choice.

If however, your approach needs to be as portable as possible and you don't want to spend time providing multiple implementations for each architecture, then `std::simd` is also starting to become a viable alternative, even though it's not part of the stable compiler yet.

In the end it is mostly about your personal preference. Rust is a modern language and provides many new features that are hard to be ignored even by the most hardcore C and C++ developers. It is possible to write safe code with C and C++, but it requires more effort and more tools, whilst Rust provides that by default.

### What about SVE, SVE2 or even SME?

What we have mentioned so far applies only to ASIMD/Neon. With the recent addition of SVE and its newer sibling SVE2 or the future SME (Scalable Matrix Extension), a different approach is required.

At the time of writing, there is no support of SVE intrinsics in Rust, not even on nightly compilers, as supporting those requires some fundamental changes which have to be agreed by the Rust compiler engineers. [It is still under discussion](https://github.com/rust-lang/rfcs/pull/3268), but it is expected this will be agreed upon by all sides soon and it will be part of the compiler specification. Similarly for SVE2. There are no indications about SME yet, but it is also expected that it will follow.

So, in case that you are considering switching to Rust but have to write SVE/SVE2 code, C and C++ are you only viable options for now.

However, there is nothing that holds you back from using Rust for the more portable parts of the code.

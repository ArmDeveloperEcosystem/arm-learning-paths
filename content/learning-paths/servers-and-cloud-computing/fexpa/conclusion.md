---
title: Review benefits and next steps
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Summary

The SVE FEXPA instruction speeds up the computation of exponential functions by implementing table lookup and bit manipulation. The exponential function is the core of the Softmax function that, with the shift toward Generative AI, has become a critical component of modern neural network architectures.

An implementation of the exponential function based on FEXPA can achieve a specified target precision using a polynomial of lower degree than alternative implementations. SME support for FEXPA lets you embed the exponential approximation directly into the matrix computation path, which translates into:
- Fewer instructions (no back-and-forth to scalar/SVE code)
- Potentially higher aggregate throughput (more exponentials per cycle)
- Lower power & bandwidth (data being kept in the SME engine)
- Cleaner fusion with GEMM/GEMV workloads

These improvements make exponential-heavy workloads significantly faster on Arm CPUs.

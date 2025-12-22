---
title: Conclusion
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Conclusion
The SVE FEXPA instruction can speed-up the computation of the exponential functions by implementing table lookup and bit manipulation. The exponential function is the core of the Softmax function that, with the shift toward Generative AI, has become a critical component of modern neural network architectures.

An implementation of the exponential function based on FEXPA can achieve a specified target precision using a polynomial of lower degree than that required by alternative implementations. Moreover, SME support for FEXPA lets you embed the exponential approximation directly into the matrix computation path and that translates into:
- Fewer instructions (no back-and-forth to scalar/SVE code)
- Potentially higher aggregate throughput (more exponentials per cycle)
- Lower power & bandwidth (data being kept in the SME engine)
- Cleaner fusion with GEMM/GEMV workloads

All of which makes all exponential heavy workloads significantly faster on ARM CPUs.

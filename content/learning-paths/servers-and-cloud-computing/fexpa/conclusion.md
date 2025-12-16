---
title: Conclusion
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Conclusion
The SVE2 FEXPA instruction can speed-up the computation of the exponential function by implementing Look-Up and bit manipulation. 

In conclusion, SME-support for FEXPA lets you embed the expensive exponential approximation directly into the matrix computation path.  That translates into:
- Fewer instructions (no back-and-forth to scalar/SVE code)
- Potentially higher aggregate throughput (more exponentials per cycle)
- Lower power & bandwidth (data being kept in SME engine)
- Cleaner fusion with GEMM/GEMV workloads

All of which makes all exponential heavy workloads significantly faster on ARM CPUs.

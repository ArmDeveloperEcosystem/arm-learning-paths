---
title: Conclusion
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

SIMD Loops is a practical way to learn the intricacies of SVE and SME across modern Arm architectures. By providing small, runnable loop kernels with reference code and optimized variants, it closes the gap between architectural specifications and real applications.

Whether you are moving from NEON or starting directly with SVE and SME, the project offers:
- A broad catalog of kernels that highlight specific features (predication, VLA programming, gather/scatter, streaming mode, ZA tiles)
- Clear, readable implementations in C, ACLE intrinsics, and selected inline assembly
- Flexible build targets and a simple runner to execute and validate loops

Use the repository to explore, modify, and benchmark kernels so you can understand tradeoffs and apply the patterns to your own workloads.

For more information and to get started, visit the GitLab project and see the [README.md](https://gitlab.arm.com/architecture/simd-loops/-/blob/main/README.md)
for the latest instructions on building and running the code. 

---
title: Overview of BOLT Merge 
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

[BOLT](https://github.com/llvm/llvm-project/blob/main/bolt/README.md) is a post-link binary optimizer that uses Linux Perf data to re-order the executable code layout to reduce memory overhead and improve performance.

In this Learning Path, you'll learn how to:
- Collect and merge BOLT profiles from multiple workload features (e.g., read-only and write-only)
- Independently optimize application binaries and external user-space libraries (e.g., `libssl.so`, `libcrypto.so`)
- Link the final optimized binary with the separately bolted libraries to deploy a fully optimized runtime stack

While MySQL and sysbench are used as examples, this method applies to **any feature-rich application** that:
- Exhibits multiple runtime paths
- Uses dynamic libraries
- Requires full-stack binary optimization for performance-critical deployment

The workflow includes:
1. Profiling each workload feature separately
2. Profiling external libraries independently
3. Merging profiles for broader code coverage
4. Applying BOLT to each binary and library
5. Linking bolted libraries with the merged-profile binary


---
title: Root Cause Analaysis with Perf C2C
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## 

Running the `perf` cache to cache (c2c) workload without `SPE` will fail. For example you will observe the following. 

```output
$ perf c2c record
failed: memory events not supported
```

```output
sudo perf list "arm_spe*"
```
---
title: BOLT with ETM
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## BOLT with ETM

Steps to optimise executable with BOLT using Perf ETM

```bash { target="ubuntu:latest" }
perf record -e cs_etm/@tmc_etr0/u -o perf.data -- ./executable
perf2bolt -p perf.data -o perf.fdata ./executable
llvm-bolt ./executable -o ./new_executable -data perf.fdata -reorder-blocks=ext-tsp -reorder-functions=hfsort -split-functions -split-all-cold -split-eh -dyno-stats
```

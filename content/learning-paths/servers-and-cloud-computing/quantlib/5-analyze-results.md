---
title: Analyze and compare benchmark results
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Record your results

The following results were collected on a Standard_D4ps_v5 Azure Cobalt virtual machine.

### Workload scaling (single thread)

| Command | Size | Threads | Throughput | Runtime |
|--------|------|---------|------------|---------|
| `--size=1 --nProc=1` | 1 | 1 | 0.598422 tasks/s | 2m 25s |
| `--size=5 --nProc=1` | 5 | 1 | 0.370434 tasks/s | 19m 34s |
| `--size=8 --nProc=1` | 8 | 1 | 0.401196 tasks/s | 28m 55s |

### Thread scaling (fixed workload size)

| Command | Size | Threads | Throughput | Runtime |
|--------|------|---------|------------|---------|
| `--size=80 --nProc=1` | 80 | 1 | 0.372445 tasks/s | 5h 11m |
| `--size=80 --nProc=2` | 80 | 2 | 0.775048 tasks/s | 2h 30m |
| `--size=80 --nProc=4` | 80 | 4 | 1.55115 tasks/s | 1h 15m |

## Understand workload scaling

When increasing the workload size while keeping the thread count fixed:

- runtime increases significantly as size increases  
- throughput remains relatively stable  

For example:

- `--size=1` completes in ~2 minutes 25 seconds  
- `--size=8` completes in ~28 minutes 55 seconds  

This shows that the benchmark is scaling the amount of work, not changing execution efficiency.

## Understand thread scaling

When increasing the number of worker processes:

- runtime decreases significantly  
- throughput increases almost linearly  

From the results:

- 1 to 2 workers:
  - runtime drops from ~5h 11m to ~2h 30m  
  - throughput nearly doubles  

- 2 to 4 workers:
  - runtime drops again to ~1h 15m  
  - throughput doubles again  

This indicates **near-linear scaling** on this system.

## Calculate speedup

Speedup compares performance relative to a single thread.

| Threads | Runtime | Speedup |
|--------|--------|---------|
| 1 | 5h 11m | 1.0× |
| 2 | 2h 30m | ~2.08× |
| 4 | 1h 15m | ~4.16× |

This shows slightly better than linear scaling, which can occur due to improved cache utilization or measurement variability.

## Key observations

From these results:

- QuantLib scales well across multiple cores on Azure Cobalt  
- Throughput increases proportionally with thread count  
- Runtime grows with workload size, as expected  
- The system shows efficient utilization of available cores  


{{% notice Practical guidance %}}
Large benchmark sizes such as `--size=80` can take several hours to complete on smaller virtual machines. For most use cases, smaller sizes such as 1, 5, or 8 are sufficient to demonstrate scaling behavior.
{{% /notice %}}

## What you learned

You built QuantLib from source on an Arm-based Azure Cobalt VM, enabled its benchmark executable, and ran controlled tests that varied one parameter at a time. You also recorded enough context to compare runs later: VM size, workload size, worker count, runtime, and throughput.

Use this workflow as a starting point for evaluating other C++ financial computing workloads on Arm cloud instances. For deeper comparisons, repeat the same benchmark process across VM sizes, compiler options, QuantLib versions, or cloud regions, and keep the command lines and environment details with the results.

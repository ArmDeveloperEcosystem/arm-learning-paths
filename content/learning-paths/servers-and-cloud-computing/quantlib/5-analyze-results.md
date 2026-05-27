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
| `--size=1 --nProc=1` | 1 | 1 | 0.401534 tasks/s | 216.669s |
| `--size=5 --nProc=1` | 5 | 1 | 0.370434 tasks/s | 1174.3s |
| `--size=8 --nProc=1` | 8 | 1 | 0.401196 tasks/s | 1734.81s |

### Thread scaling (fixed workload size)

| Command | Size | Threads | Throughput | Runtime |
|--------|------|---------|------------|---------|
| `--size=80 --nProc=1` | 80 | 1 | 0.372445 tasks/s | 18687.3s |
| `--size=80 --nProc=2` | 80 | 2 | 0.775048 tasks/s | 8980.08s |
| `--size=80 --nProc=4` | 80 | 4 | 1.55115 tasks/s | 4487s |

## Understand workload scaling

When increasing the workload size while keeping the thread count fixed:

- runtime increases significantly as size increases  
- throughput remains relatively stable  

For example:

- `--size=1` completes in ~217 seconds  
- `--size=8` completes in ~1735 seconds  

This shows that the benchmark is scaling the amount of work, not changing execution efficiency.

## Understand thread scaling

When increasing the number of processes:

- runtime decreases significantly  
- throughput increases almost linearly  

From the results:

- 1 → 2 threads:
  - runtime drops from ~18687s to ~8980s  
  - throughput nearly doubles  

- 2 → 4 threads:
  - runtime drops again to ~4487s  
  - throughput doubles again  

This indicates **near-linear scaling** on this system.

## Calculate speedup

Speedup compares performance relative to a single thread.

| Threads | Runtime | Speedup |
|--------|--------|---------|
| 1 | 18687.3s | 1.0× |
| 2 | 8980.08s | ~2.08× |
| 4 | 4487s | ~4.16× |

This shows slightly better than linear scaling, which can occur due to improved cache utilization or measurement variability.

## Key observations

From these results:

- QuantLib scales well across multiple cores on Azure Cobalt  
- Throughput increases proportionally with thread count  
- Runtime grows with workload size, as expected  
- The system shows efficient utilization of available cores  

## Practical guidance

{{% notice Note %}}
Large benchmark sizes such as `--size=80` can take several hours to complete on smaller virtual machines. For most use cases, smaller sizes such as 1, 5, or 8 are sufficient to demonstrate scaling behavior.
{{% /notice %}}

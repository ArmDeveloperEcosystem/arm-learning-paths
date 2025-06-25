---
title: Review the performance results
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This step presents the performance comparisons across various BOLT optimization scenarios. You'll see how baseline performance compares with BOLT-optimized binaries using merged profiles and bolted external libraries.

### 1. Baseline Performance (No BOLT)

| Metric                     | Read-Only (Baseline) | Write-Only (Baseline) | Read+Write (Baseline) |
|---------------------------|----------------------|------------------------|------------------------|
| Transactions/sec (TPS)    | 1006.33              | 2113.03                | 649.15                 |
| Queries/sec (QPS)         | 16,101.24            | 12,678.18              | 12,983.09              |
| Latency avg (ms)          | 0.99                 | 0.47                   | 1.54                   |
| Latency 95th % (ms)       | 1.04                 | 0.83                   | 1.79                   |
| Total time (s)            | 9.93                 | 4.73                   | 15.40                  |

### 2. Performance Comparison: Merged vs Non-Merged Instrumentation

| Metric                     | Regular BOLT R+W (No Merge, system libssl) | Merged BOLT (BOLTed Read+Write + BOLTed libssl) |
|---------------------------|---------------------------------------------|-------------------------------------------------|
| Transactions/sec (TPS)    | 850.32                                      | 879.18                                          |
| Queries/sec (QPS)         | 17,006.35                                   | 17,583.60                                       |
| Latency avg (ms)          | 1.18                                        | 1.14                                            |
| Latency 95th % (ms)       | 1.52                                        | 1.39                                            |
| Total time (s)            | 11.76                                       | 11.37                                           |

Second run:

| Metric                     | Regular BOLT R+W (No Merge, system libssl) | Merged BOLT (BOLTed Read+Write + BOLTed libssl) |
|---------------------------|---------------------------------------------|-------------------------------------------------|
| Transactions/sec (TPS)    | 853.16                                      | 887.14                                          |
| Queries/sec (QPS)         | 17,063.22                                   | 17,742.89                                       |
| Latency avg (ms)          | 1.17                                        | 1.13                                            |
| Latency 95th % (ms)       | 1.39                                        | 1.37                                            |
| Total time (s)            | 239.9                                       | 239.9                                           |

### 3. BOLTed READ, BOLTed WRITE, MERGED BOLT (Read+Write+BOLTed Libraries)

| Metric                     | Bolted Read-Only  | Bolted Write-Only | Merged BOLT (Read+Write+libssl) | Merged BOLT (Read+Write+libcrypto) | Merged BOLT (Read+Write+libssl+libcrypto) |
|---------------------------|---------------------|-------------------|----------------------------------|------------------------------------|-------------------------------------------|
| Transactions/sec (TPS)    | 1348.47             | 3170.92           | 887.14                           | 896.58                             | 902.98                                    |
| Queries/sec (QPS)         | 21575.45            | 19025.52          | 17742.89                         | 17931.57                           | 18059.52                                  |
| Latency avg (ms)          | 0.74                | 0.32              | 1.13                             | 1.11                               | 1.11                                      |
| Latency 95th % (ms)       | 0.77                | 0.55              | 1.37                             | 1.34                               | 1.34                                      |
| Total time (s)            | 239.8               | 239.72            | 239.9                            | 239.9                              | 239.9                                     |

{{% notice Note %}}
All sysbench and .fdata file paths, as well as taskset usage, should match the conventions in previous steps: use sysbench from PATH (no src/), use /usr/share/sysbench/ for Lua scripts, and use $HOME-based paths for all .fdata and library files. On an 8-core system, use taskset -c 7 for sysbench and avoid contention with mysqld.
{{% /notice %}}

### Key metrics to analyze

- **TPS (Transactions Per Second)**: Higher is better.
- **QPS (Queries Per Second)**: Higher is better.
- **Latency (Average and 95th Percentile)**: Lower is better.

### Conclusion

- BOLT substantially improves performance over non-optimized binaries due to better instruction cache utilization and reduced execution path latency.
- Merging feature-specific profiles does not negatively affect performance; instead, it captures a broader set of runtime behaviors, making the binary better tuned for varied real-world workloads.
- Separately optimizing external user-space libraries, even though providing smaller incremental gains, further complements the overall application optimization, delivering a fully optimized execution environment.

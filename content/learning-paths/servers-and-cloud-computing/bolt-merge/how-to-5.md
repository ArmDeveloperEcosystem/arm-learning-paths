---
title: Review the performance results
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

This section compares the performance of baseline binaries with BOLT-optimized versions. It highlights the impact of merged profile optimizations and shared library enhancements on overall system throughput and latency.

All tests used Sysbench with the flags `--time=0 --events=10000`. This configuration ensures that each test completes exactly 10,000 requests per thread, delivering consistent workload runtimes  across runs.

### Baseline performance (without BOLT)

| Metric                     |Read-only  | Write-only  | Read + write  |
|---------------------------|----------------------|------------------------|------------------------|
| Transactions/sec (TPS)    | 1006.33              | 2113.03                | 649.15                 |
| Queries/sec (QPS)         | 16,101.24            | 12,678.18              | 12,983.09              |
| Latency avg (ms)          | 0.99                 | 0.47                   | 1.54                   |
| Latency 95th % (ms)       | 1.04                 | 0.83                   | 1.79                   |
| Total time (s)            | 9.93                 | 4.73                   | 15.40                  |

### Performance comparison: merged and non-merged instrumentation

| Metric                     | Regular BOLT (read + write, system libssl) | Merged BOLT (read + write + libssl) |
|---------------------------|---------------------------------------------|-------------------------------------------------|
| Transactions/sec (TPS)    | 850.32                                      | 879.18                                          |
| Queries/sec (QPS)         | 17,006.35                                   | 17,583.60                                       |
| Latency avg (ms)          | 1.18                                        | 1.14                                            |
| Latency 95th % (ms)       | 1.52                                        | 1.39                                            |
| Total time (s)            | 11.76                                       | 11.37                                           |

Second test run:

| Metric                     | Regular BOLT (read + write, system libssl) | Merged BOLT (read + write + libssl) |
|---------------------------|---------------------------------------------|-------------------------------------------------|
| Transactions/sec (TPS)    | 853.16                                      | 887.14                                          |
| Queries/sec (QPS)         | 17,063.22                                   | 17,742.89                                       |
| Latency avg (ms)          | 1.17                                        | 1.13                                            |
| Latency 95th % (ms)       | 1.39                                        | 1.37                                            |
| Total time (s)            | 239.9                                       | 239.9                                           |

### Performance across BOLT optimizations

| Metric                     | 	BOLT read-only | BOLT write-only | Merged BOLT (read + write + libssl) | Merged BOLT (read + write + libcrypto) | Merged BOLT (read + write + libcrypto + libssl) |
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

- **TPS (transactions per second)** – higher is better  
- **QPS (queries per second)** – higher is better  
- **Latency (average and 95th percentile)** – lower is better

### Conclusion

- BOLT-optimized binaries clearly outperform baseline versions by improving instruction cache usage and shortening execution paths.
- Merging feature-specific profiles does not negatively affect performance. Instead, they allow better tuning for varied real-world workloads by capturing a broader set of runtime behaviors.
- External library optimizations (for example, `libssl` and `libcrypto`) provide smaller incremental gains, delivering a fully optimized execution environment.

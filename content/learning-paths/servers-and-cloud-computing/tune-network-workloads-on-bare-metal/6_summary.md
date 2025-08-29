---
title: Summary
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Summary
You will observe that each tuning method can bring significant performance improvements while running Tomcat as shown in the results summary below:

| Method          | Requests/sec | Latency-Avg |
|:----------------|:-------------|:------------|
| Baseline         | 357835.75    | 10.26s      |
| NIC-Queue       | 378782.37    | 8.35s       |
| NUMA-Local      | 363744.39    | 9.41s       |
| IOMMU           | 428628.50    | 4.92s       |


The same tuning methods can be applied as general guidance to help optimize and tune other network-based workloads.

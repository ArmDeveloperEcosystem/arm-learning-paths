---
title: Summary
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Summary
It can be observed that each step of the tuning method can bring significant performance improvements to Tomcat. **Similarly, these methods are equally applicable to other network-based workloads.**

| Method          | Requests/sec | Latency-Avg |
|:----------------|:-------------|:------------|
| default         | 154479.07    | 24.34s      |
| NIC-Rx/Tx-Queue | 192932.92    | 21.64s      |
| NUMA-local      | 235505.32    | 18.72s      |
| IOMMU           | 349085.30    | 10.52s      |



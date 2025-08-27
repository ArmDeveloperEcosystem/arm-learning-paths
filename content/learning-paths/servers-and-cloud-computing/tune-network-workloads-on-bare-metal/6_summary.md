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
| default         | 357835.75    | 10.26s      |
| NIC-Queue       | 378782.37    | 8.35s       |
| NUMA-Local      | 363744.39    | 9.41s       |
| IOMMU           | 428628.50    | 4.92s       |

{{% notice Note %}}
Under normal circumstances, NUMA local can improve the performance of network-intensive workloads on bare-metal servers. However, the reason why the performance improvement is not achieved on the c8g.metal-48xl bare-metal cloud instance provided by AWS requires further investigation.
{{% /notice %}}


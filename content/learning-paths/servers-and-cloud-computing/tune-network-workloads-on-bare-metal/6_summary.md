---
title: Summary
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Review the results: Tomcat performance tuning on Arm Neoverse

Each tuning technique delivered measurable gains for the Tomcat HTTP benchmark on an Arm Neoverse bare‑metal server (workload generated with **wrk2**). The table summarizes requests per second and average latency at each stage.

| Method       | Requests/sec | Avg latency (s) |
|:-------------|-------------:|----------------:|
| Baseline     | 357,835.75   | 10.26           |
| NIC queues   | 378,782.37   | 8.35            |
| NUMA-local   | 363,744.39   | 9.41            |
| IOMMU        | 428,628.50   | 4.92            |

### Key takeaways

- **IOMMU passthrough** produced the largest throughput gain: **+19.8%** vs. baseline, with a **52.0%** drop in average latency.
- **NIC queue count alignment** improved throughput by **+5.9%** and reduced average latency by **18.6%**.
- **NUMA locality** yielded a smaller but consistent benefit: **+1.7%** throughput and **8.3%** lower average latency.
- Together, these techniques (IOMMU tuning, NIC queue optimization, and NUMA-aware placement) form a practical checklist for improving network workload performance on Arm Neoverse.

### Next steps

- Apply the same tuning pattern to other HTTP services and microservices (for example, NGINX, Envoy, or custom Jetty/Tomcat apps).
- Re‑evaluate queue counts, CPU pinning, and IOMMU mode as you scale cores, update kernels, or change NIC drivers/firmware.
- Track end‑to‑end SLOs (p95/p99 latency and error rates) in addition to average metrics to ensure sustained gains under real traffic.

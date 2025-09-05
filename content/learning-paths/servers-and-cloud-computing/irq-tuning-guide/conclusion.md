---
title: conclusion
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

While a single pattern does not work for all workloads. Our testing found that under heavy network workloads, different patterns performed better based on sizing.

### upto and under 16 vCPUs
For best performance, reduce NIC IRQs to either one or two cores. Otherwise random or default performed second best.

*If the number of NIC IRQS are more then the number of vCPUs, concentrating them over less cores improved performance significantly.

### over 16 vCPUs
No pattern showed significant improvement over default as long as all NIC IRQs were not on duplicate cores.

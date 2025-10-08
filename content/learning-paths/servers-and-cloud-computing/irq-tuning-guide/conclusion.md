---
title: Conclusion and recommendations
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Optimal IRQ Management Strategies

Performance testing across multiple cloud platforms shows that IRQ management effectiveness depends heavily on system size and workload characteristics. While no single approach works optimally in all scenarios, clear patterns emerged during testing under heavy network loads.

## Recommendations for systems with 16 vCPUs or less

For smaller systems with 16 or fewer vCPUs, different strategies prove more effective:

- Concentrate network IRQs on just one or two CPU cores rather than spreading them across all available cores.
- Use the `smp_affinity` range assignment pattern with a limited core range (example: `0-1`).
- This approach works best when the number of NIC IRQs exceeds the number of available vCPUs.
- Focus on high-throughput network workloads where concentrated IRQ handling delivers the most significant performance improvements.

Performance improves significantly when network IRQs are concentrated rather than dispersed across all available cores on smaller systems. This concentration reduces context switching overhead and improves cache locality for interrupt handling.

## Recommendations for systems with more than 16 vCPUs

For larger systems with more than 16 vCPUs, different strategies prove more effective:

- Default IRQ distribution typically delivers good performance.
- Focus on preventing multiple network IRQs from sharing the same CPU core.
- Use the diagnostic scripts from the previous section to identify and resolve overlapping IRQ assignments.
- Apply the paired core pattern to ensure balanced distribution across the system.

On larger systems, interrupt handling overhead becomes less significant relative to total processing capacity. The primary performance issue occurs when high-frequency network interrupts compete for the same core, creating bottlenecks.

## Implementation considerations

When implementing these IRQ management strategies, several factors influence your success:

- Consider your workload type first, as CPU-bound applications can benefit from different IRQ patterns than I/O-bound applications. Always benchmark your specific workload with different IRQ patterns rather than assuming one approach works universally.
- For real-time monitoring, use `watch -n1 'grep . /proc/interrupts'` to observe IRQ distribution as it happens. This helps you verify your changes are working as expected.
- On multi-socket systems, NUMA effects become important. Keep IRQs on cores close to the PCIe devices generating them to minimize cross-node memory access latency. Additionally, ensure your IRQ affinity settings persist across reboots by adding them to `/etc/rc.local` or creating a systemd service file.

As workloads and hardware evolve, revisiting and adjusting IRQ management strategies might be necessary to maintain optimal performance. What works well today might need refinement as your application scales or changes.

## Next Steps

You have successfully learned how to optimize network interrupt handling on Arm servers. You can now analyze IRQ distributions, implement different management patterns, and configure persistent solutions for your workloads.


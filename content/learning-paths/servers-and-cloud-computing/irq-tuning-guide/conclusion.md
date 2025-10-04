---
title: Conclusion and recommendations
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Optimal IRQ Management Strategies

Testing across multiple cloud platforms reveals that IRQ management effectiveness varies significantly based on system size and workload characteristics. No single pattern works optimally for all scenarios, but clear patterns emerged during performance testing under heavy network loads.

## Recommendations by system size

### Systems with 16 vCPUs or less

For smaller systems with 16 or less vCPUs, concentrated IRQ assignment may provide measurable performance improvements.

- Assign all network IRQs to just one or two CPU cores
- This approach showed the most significant performance gains
- Most effective when the number of NIC IRQs exceeds the number of vCPUs
- Use the `smp_affinity` range assignment pattern from the previous section with a very limited core range, for example `0-1`

Performance improves significantly when network IRQs are concentrated rather than dispersed across all available cores on smaller systems. 

### Systems with more than 16 vCPUs

For larger systems with more than 16 vCPUs, the findings are different:

- Default IRQ distribution generally performs well
- The primary concern is avoiding duplicate core assignments for network IRQs
- Use the scripts from the previous section to check and correct any overlapping IRQ assignments
- The paired core pattern can help ensure optimal distribution on these larger systems

On larger systems, the overhead of interrupt handling is proportionally smaller compared to the available processing power. The main performance bottleneck occurs when multiple high-frequency network interrupts compete for the same core.

## Implementation considerations

When implementing these IRQ management strategies, several factors influence your success.

Consider your workload type first, as CPU-bound applications can benefit from different IRQ patterns than I/O-bound applications. Always benchmark your specific workload with different IRQ patterns rather than assuming one approach works universally.

For real-time monitoring, use `watch -n1 'grep . /proc/interrupts'` to observe IRQ distribution as it happens. This helps you verify your changes are working as expected.

On multi-socket systems, NUMA effects become important. Keep IRQs on cores close to the PCIe devices generating them to minimize cross-node memory access latency. Additionally, ensure your IRQ affinity settings persist across reboots by adding them to `/etc/rc.local` or creating a systemd service file.

As workloads and hardware evolve, revisiting and adjusting IRQ management strategies may be necessary to maintain optimal performance. What works well today might need refinement as your application scales or changes.

## Next Steps

You have successfully learned how to optimize network interrupt handling on Arm servers. You can now analyze IRQ distributions, implement different management patterns, and configure persistent solutions for your workloads.

### Learn more about Arm server performance

* [Deploy applications on Arm-based cloud instances](../csp/)
* [Get started with performance analysis using Linux Perf](../../../install-guides/perf/)
* [Optimize server applications for Arm Neoverse processors](../mongodb/)

### Explore related topics

* [Understanding Arm server architecture](../arm-cloud-native-performance/)
* [Cloud migration strategies for Arm](../migration/)

### Additional resources

* [Linux kernel IRQ subsystem documentation](https://www.kernel.org/doc/html/latest/core-api/irq/index.html)
* [Arm Neoverse performance optimization guide](https://developer.arm.com/documentation/)
* [Network performance tuning best practices](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/monitoring_and_managing_system_status_and_performance/)
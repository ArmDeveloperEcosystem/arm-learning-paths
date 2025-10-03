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

## Implementation Considerations

When implementing these IRQ management strategies, there are some important points to keep in mind.

Pay attention to the workload type. CPU-bound applications may benefit from different IRQ patterns than I/O-bound applications.

Always benchmark your specific workload with different IRQ patterns. 

Monitor IRQ counts in real-time using `watch -n1 'grep . /proc/interrupts'` to observe IRQ distribution in real-time.

Also consider NUMA effects on multi-socket systems. Keep IRQs on cores close to the PCIe devices generating them to minimize cross-node memory access.

Make sure to set up IRQ affinity settings in `/etc/rc.local` or a systemd service file to ensure they persist across reboots.

Remember that as workloads and hardware evolve, revisiting and adjusting IRQ management strategies may be necessary to maintain optimal performance.

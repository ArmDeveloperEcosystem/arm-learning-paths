---
title: IRQ management patterns for performance optimization
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Optimizing network performance with IRQ management

Different IRQ management patterns can significantly impact network performance across multiple cloud platforms and virtual machine sizes. This Learning Path presents various IRQ distribution strategies, along with scripts to implement them on your systems.

Network interrupt requests (IRQs) can be distributed across CPU cores in various ways, each with potential benefits depending on your workload characteristics and system configuration. By strategically assigning network IRQs to specific cores, you can improve cache locality, reduce contention, and potentially boost overall system performance.

The following patterns have been tested on various systems and can be implemented using the provided scripts. An optimal pattern is suggested at the conclusion of this Learning Path, but your specific workload may benefit from a different approach.

### Patterns

1. Default: IRQ pattern provided at boot.
2. Random: All IRQs are assigned a core and do not overlap with network IRQs.
3. Housekeeping: All IRQs outside of network IRQs are assigned to specific core(s).
4. NIC IRQs are assigned to single or multiple ranges of cores, including pairs. 

### Scripts to change IRQ

The scripts below demonstrate how to implement different IRQ management patterns on your system. Each script targets a specific distribution strategy:

Before running these scripts, identify your network interface name using `ip link show` and determine your system's CPU topology with `lscpu`. Always test these changes in a non-production environment first, as improper IRQ assignment can impact system stability.

To change the NIC IRQs or IRQs in general you can use the following scripts.

### Housekeeping

The housekeeping pattern isolates non-network IRQs to dedicated cores. 

You need to add more to account for other IRQs on your system.

```bash
HOUSEKEEP=#core range here (example: "0,3")

for irq in $(awk '/ACPI:Ged/ {sub(":","",$1); print $1}' /proc/interrupts); do
    echo $HOUSEKEEP | sudo tee /proc/irq/$irq/smp_affinity_list >/dev/null
done
```

### Paired core 

The paired core assignment pattern distributes network IRQs across CPU core pairs for better cache coherency. 

This is for pairs on a 16 vCPU machine.

You need to add the interface name.

```bash
IFACE=#interface name (example: "ens5")

PAIRS=("0,1" "2,3" "4,5" "6,7" "8,9" "10,11" "12,13" "14,15")

# Match IRQs for the NIC
mapfile -t irqs < <(grep "$IFACE-Tx-Rx" /proc/interrupts | awk '{gsub(":","",$1); print $1}')

i=0
for irq in "${irqs[@]}"; do
    pair=${PAIRS[$((i % ${#PAIRS[@]}))]}
    echo "$pair" | sudo tee /proc/irq/$irq/smp_affinity_list >/dev/null
    echo "Set IRQ $irq -> CPUs $pair"
    ((i++))
done
```

### Range assignment  

The range assignment pattern assigns network IRQs to a specific range of cores.

This will assign a specific core(s) to NIC IRQs only.

You need to add the interface name.

```bash
IFACE=#interface name (example: "ens5")

for irq in $(awk '/'$IFACE'/ {sub(":","",$1); print $1}' /proc/interrupts); do
    echo 0-15 | sudo tee /proc/irq/$irq/smp_affinity_list > /dev/null
done
```

Each pattern offers different performance characteristics depending on your workload. The housekeeping pattern reduces system noise, paired cores optimize cache usage, and range assignment provides dedicated network processing capacity. Test these patterns in your environment to determine which provides the best performance for your specific use case.

Continue to the next section for additional guidance.
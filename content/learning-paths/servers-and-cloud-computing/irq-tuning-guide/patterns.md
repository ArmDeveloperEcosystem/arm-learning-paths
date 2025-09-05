---
title: patterns
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

The following patterns were ran on multiple cloud and on a variety of sizes. A recommended IRQ pattern will be suggested at the end. Based on your workload, a different pattern may result in higher performance.

### Patterns
1. Default: IRQ pattern provided at boot.
2. Random: All IRQs are assigned a core and do not overlap with network IRQs.
3. Housekeeping: All IRQs outside of network IRQs are assign to specific core(s).
4. NIC IRQs are set to single or multiple ranges of cores and including pairs. EX. 1, 1-2, 0-3, 0-7, [0-1, 2-3..], etc.


### Scripts to change IRQ

To change the NIC IRQs or IRQs in general you can use the following scripts.

Housekeeping pattern example, you will need to add more to account for other IRQs on your system

```
HOUSEKEEP=#core range here

# ACPI:Ged
for irq in $(awk '/ACPI:Ged/ {sub(":","",$1); print $1}' /proc/interrupts); do
    echo $HOUSEKEEP | sudo tee /proc/irq/$irq/smp_affinity_list >/dev/null
done
```

This is for pairs on a 16 vCPU machine, you will need the interface name.

```
IFACE=#interface name

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

This will assign a specific core(s) to NIC IRQs only

```
IFACE=#interface name

for irq in $(awk '/$IFACE/ {sub(":","",$1); print $1}' /proc/interrupts); do
    echo 0-15 | sudo tee /proc/irq/$irq/smp_affinity_list > /dev/null
done
```
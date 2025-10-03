---
title: Understand and Analyze network IRQ configuration
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why IRQ management matters for performance

In modern cloud environments, network performance is critical to overall system efficiency. Network interface cards (NICs) generate interrupt requests (IRQs) to notify the CPU when data packets arrive or need to be sent. These interrupts temporarily pause normal processing, allowing the system to handle network traffic.

By default, Linux distributes these network interrupts across available CPU cores. However, this distribution is not always optimal for performance:

- High interrupt rates: In busy servers, network cards can generate thousands of interrupts per second
- CPU cache locality: Processing related network operations on the same CPU core improves cache efficiency
- Resource contention: When network IRQs compete with application workloads for the same CPU resources, both can suffer
- Power efficiency: IRQ management can help reduce unnecessary CPU wake-ups, improving energy efficiency

Understanding and optimizing IRQ assignment allows you to balance network processing loads, reduce latency, and maximize throughput for your specific workloads.

## Identifying IRQs on your system

To get started, run this command to display all IRQs on your system and their CPU assignments:

```bash
grep '' /proc/irq/*/smp_affinity_list | while IFS=: read path cpus; do
    irq=$(basename $(dirname $path))
    device=$(grep -E "^ *$irq:" /proc/interrupts | awk '{print $NF}')
    printf "IRQ %s -> CPUs %s -> Device %s\n" "$irq" "$cpus" "$device"
done
```

The output is very long and looks similar to:

```output
IRQ 104 -> CPUs 12   -> Device ens34-Tx-Rx-5
IRQ 105 -> CPUs 5    -> Device ens34-Tx-Rx-6
IRQ 106 -> CPUs 10   -> Device ens34-Tx-Rx-7
IRQ 11  -> CPUs 0-15 -> Device
IRQ 14  -> CPUs 0-15 -> Device ttyS0
IRQ 17  -> CPUs 0-15 -> Device ACPI:Ged
IRQ 19  -> CPUs 0-15 -> Device ACPI:Ged
IRQ 2   -> CPUs 0-15 -> Device
IRQ 20  -> CPUs 0-15 -> Device ACPI:Ged
IRQ 21  -> CPUs 0-15 -> Device ACPI:Ged
...
IRQ 26  -> CPUs 0-15 -> Device ACPI:Ged
```

## How to identify network IRQs

Network-related IRQs can be identified by looking at the "Device" column in the output. 

You can identify network interfaces using the command:

```bash
ip link show
```

Here are some common patterns to look for:

Common interface naming patterns include `eth0` for traditional ethernet, `enP3p3s0f0` and `ens5-Tx-Rx-0` for the Linux predictable naming scheme, or `wlan0` for wireless.

The predictable naming scheme breaks down into:

- en = ethernet
- P3 = PCI domain 3
- p3 = PCI bus 3
- s0 = PCI slot 0
- f0 = function 0

This naming convention helps ensure network interfaces have consistent names across reboots by encoding their physical 
location in the system.

## Improve performance

Once you've identified the network IRQs, you can adjust their CPU assignments to try to improve performance.

Identify the NIC (Network Interface Card) IRQs and adjust the system by experimenting and seeing if performance improves.

You may notice that some NIC IRQs are assigned to the same CPU cores by default, creating duplicate assignments.

For example:

```output
IRQ 100 -> CPUs 2 -> Device ens34-Tx-Rx-1
IRQ 101 -> CPUs 12 -> Device ens34-Tx-Rx-2
IRQ 102 -> CPUs 14 -> Device ens34-Tx-Rx-3
IRQ 103 -> CPUs 9 -> Device ens34-Tx-Rx-4
IRQ 104 -> CPUs 12 -> Device ens34-Tx-Rx-5
IRQ 105 -> CPUs 5 -> Device ens34-Tx-Rx-6
IRQ 106 -> CPUs 10 -> Device ens34-Tx-Rx-7
```

## Understanding IRQ performance impact

When network IRQs are assigned to the same CPU cores (as shown in the example above where IRQ 101 and 104 both use CPU 12), this can potentially hurt performance as multiple interrupts compete for the same CPU core's attention, while other cores remain underutilized.

By optimizing IRQ distribution, you can achieve more balanced processing and improved throughput. This optimization is especially important for high-traffic servers where network performance is critical.

Suggested experiments are covered in the next section.

### How can I reset my IRQs if I make performance worse?

If your experiments reduce performance, you can return the IRQs back to default using the following commands:

```bash
sudo systemctl unmask irqbalance
sudo systemctl enable --now irqbalance
```

If needed, install `irqbalance` on your system. For Debian based systems run:

```bash
sudo apt install irqbalance
```

### Saving these changes

Any changes you make to IRQs will be reset at reboot. You will need to change your system's settings to make your changes permanent.

---
title: checking IRQs
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

First you should run the following command to identify all IRQs on the system. Identify the NIC IRQs and adjust the system by experimenting and seeing how performance improves.

```
grep '' /proc/irq/*/smp_affinity_list | while IFS=: read path cpus; do
    irq=$(basename $(dirname $path))
    device=$(grep -E "^ *$irq:" /proc/interrupts | awk '{print $NF}')
    printf "IRQ %s -> CPUs %s -> Device %s\n" "$irq" "$cpus" "$device"
done
```


{{% notice Note %}}
output should look similar to this:
```
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
{{% /notice %}}

Now, you may notice that the NIC IRQs are assigned to a duplicate CPU by default.

like this example:
```
IRQ 100 -> CPUs 2 -> Device ens34-Tx-Rx-1
IRQ 101 -> CPUs 12 -> Device ens34-Tx-Rx-2
IRQ 102 -> CPUs 14 -> Device ens34-Tx-Rx-3
IRQ 103 -> CPUs 9 -> Device ens34-Tx-Rx-4
IRQ 104 -> CPUs 12 -> Device ens34-Tx-Rx-5
IRQ 105 -> CPUs 5 -> Device ens34-Tx-Rx-6
IRQ 106 -> CPUs 10 -> Device ens34-Tx-Rx-7
```
This can potential hurt performance. Suggestions and patterns to experiment with will be on the next step.

### reset

If performance reduces, you can return the IRQs back to default using the following commands.

```
sudo systemctl unmask irqbalance
sudo systemctl enable --now irqbalance
```

or you can run the following

```
DEF=$(cat /proc/irq/default_smp_affinity)
for f in /proc/irq/*/smp_affinity; do
  echo "$DEF" | sudo tee "$f" >/dev/null || true
done
```

### Saving these changes

Any changes you make to IRQs will be reset at reboot. You will need to change your systems settings to make your changes permanant.

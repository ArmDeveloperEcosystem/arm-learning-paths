---
title: Tuning via iommu
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Tuning via iommu
- Setting iommu
- The result after tuning iommu

In cloud environments, SmartNICs are typically used to offload the IOMMU workload. On bare-metal systems, to align performance with the cloud, you should disable iommu.strict and enable iommu.passthrough.

### Setting iommu

1. Use the following command to verify the default IOMMU status on the bare-metal
```bash
sudo dmesg | grep iommu
```
It can be observed that under the default configuration, iommu.strict is enabled, and iommu.passthrough is disabled.
```bash
[   11.558455] iommu: Default domain type: Translated
[   11.563355] iommu: DMA domain TLB invalidation policy: strict mode
```

2. To set IOMMU status, use a text editor to modify the `grub` file by adding or updating the `GRUB_CMDLINE_LINUX` configuration.

```bash
sudo vi /etc/default/grub
```
then add or update
```bash
GRUB_CMDLINE_LINUX="iommu.strict=0 iommu.passthrough=1"
```

3. Update GRUB and reboot to apply the settings.
```bash
sudo update-grub
sudo reboot
```

4. Verify whether the settings have been successfully applied.
```bash
sudo dmesg | grep iommu
```

It can be observed that the IOMMU is already in passthrough mode.
```bash
[    0.000000] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-6.8.0-71-generic root=UUID=a9adbbfa-892b-473d-906f-8bc0250bf544 ro iommu.strict=0 iommu.passthrough=1
[   11.565539] iommu: Default domain type: Passthrough (set via kernel command line)
```

### The result after tuning local NUMA

1. Use the following command on the Grace bare-metal where `Tomcat` is on
```bash
~/apache-tomcat-11.0.9/bin/shutdown.sh 2>/dev/null
ulimit -n 65535 && ~/apache-tomcat-11.0.9/bin/startup.sh
```

2. And use the following command on the `x86_64` bare-metal where `wrk2` is on
```bash
ulimit -n 65535 && wrk -c1280 -t128 -R500000 -d60 http://${tomcat_ip}:8080/examples/servlets/servlet/HelloWorldExample
```

The result after iommu tuned:
```bash
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    10.52s     4.83s   22.43s    61.31%
    Req/Sec     2.75k    67.27     2.97k    70.85%
  20917980 requests in 1.00m, 10.85GB read
  Socket errors: connect 0, read 0, write 0, timeout 16
Requests/sec: 349085.30
Transfer/sec:    185.43MB
```

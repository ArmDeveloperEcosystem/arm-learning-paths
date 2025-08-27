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

1. To set IOMMU status, use a text editor to modify the `grub` file by adding or updating the `GRUB_CMDLINE_LINUX` configuration.

```bash
sudo vi /etc/default/grub
```
then add or update
```bash
GRUB_CMDLINE_LINUX="iommu.strict=0 iommu.passthrough=1"
```

2. Update GRUB and reboot to apply the settings.
```bash
sudo update-grub && sudo reboot
```

3. Verify whether the settings have been successfully applied.
```bash
sudo dmesg | grep iommu
```

It can be observed that the IOMMU is already in passthrough mode.
```bash
[    0.000000] Kernel command line: BOOT_IMAGE=/vmlinuz-6.14.0-1011-aws root=PARTUUID=1c3f3c20-db6b-497c-8727-f6702f73a5b2 ro iommu.strict=0 iommu.passthrough=1 console=tty1 console=ttyS0 nvme_core.io_timeout=4294967295 panic=-1
[    0.855658] iommu: Default domain type: Passthrough (set via kernel command line)
```

### The result after tuning IOMMU

1. Use the following command on the Arm Neoverse bare-metal where `Tomcat` is on
```bash
for no in {96..103}; do sudo bash -c "echo 1 > /sys/devices/system/cpu/cpu${no}/online"; done
for no in {0..95} {104..191}; do sudo bash -c "echo 0 > /sys/devices/system/cpu/cpu${no}/online"; done
net=$(ls /sys/class/net/ | grep 'en')
sudo ethtool -L ${net} combined 8
~/apache-tomcat-11.0.10/bin/shutdown.sh 2>/dev/null
ulimit -n 65535 && ~/apache-tomcat-11.0.10/bin/startup.sh
```

2. And use the following command on the `x86_64` bare-metal where `wrk2` is on
```bash
ulimit -n 65535 && wrk -c1280 -t128 -R500000 -d60 http://${tomcat_ip}:8080/examples/servlets/servlet/HelloWorldExample
```

The result after iommu tuned:
```bash
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     4.92s     2.49s   10.08s    62.27%
    Req/Sec     3.36k    56.23     3.58k    69.64%
  25703668 requests in 1.00m, 13.33GB read
Requests/sec: 428628.50
Transfer/sec:    227.69MB
```

---
title: IOMMU-based tuning
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Tune with IOMMU

IOMMU (Input–Output Memory Management Unit) controls how I/O devices access memory. In many cloud environments, SmartNICs offload IOMMU-related work. On Arm Neoverse bare‑metal systems, you can often improve Tomcat networking performance by **disabling strict mode** and **enabling passthrough** (setting `iommu.strict=0` and `iommu.passthrough=1`).

## Configure IOMMU settings

Edit the GRUB configuration to set IOMMU to passthrough and disable strict invalidations:

```bash
sudo vi /etc/default/grub
```
Add or update the kernel command line:
```bash
GRUB_CMDLINE_LINUX="iommu.strict=0 iommu.passthrough=1"
```

Update GRUB and reboot to apply the settings:

```bash
sudo update-grub && sudo reboot
```

Verify that IOMMU is in passthrough mode after reboot:

```bash
sudo dmesg | grep iommu
```

You will notice that the IOMMU is already in passthrough mode:
```bash
[    0.000000] Kernel command line: BOOT_IMAGE=/vmlinuz-6.14.0-1011-aws root=PARTUUID=1c3f3c20-db6b-497c-8727-f6702f73a5b2 ro iommu.strict=0 iommu.passthrough=1 console=tty1 console=ttyS0 nvme_core.io_timeout=4294967295 panic=-1
[    0.855658] iommu: Default domain type: Passthrough (set via kernel command line)
```

## Validate performance after IOMMU tuning

Prepare the Arm Neoverse bare‑metal server (ensure your `${net}` interface variable is set; if not, set it to your NIC name, for example `net=enP11p4s0`), align queues, and restart Tomcat:

```bash
for no in {96..103}; do sudo bash -c "echo 1 > /sys/devices/system/cpu/cpu${no}/online"; done
for no in {0..95} {104..191}; do sudo bash -c "echo 0 > /sys/devices/system/cpu/cpu${no}/online"; done

# Ensure NIC queue count matches the number of online CPUs (example: 8)
sudo ethtool -L ${net} combined 8

# Restart Tomcat with a higher file‑descriptor limit
~/apache-tomcat-11.0.10/bin/shutdown.sh 2>/dev/null
ulimit -n 65535 && ~/apache-tomcat-11.0.10/bin/startup.sh
```

Run `wrk2` on the `x86_64` benchmarking client to measure throughput and latency:

```bash
ulimit -n 65535 && wrk -c1280 -t128 -R500000 -d60 http://${tomcat_ip}:8080/examples/servlets/servlet/HelloWorldExample
```

Sample results after IOMMU tuning:

```output
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     4.92s     2.49s   10.08s    62.27%
    Req/Sec     3.36k    56.23     3.58k    69.64%
  25703668 requests in 1.00m, 13.33GB read
Requests/sec: 428628.50
Transfer/sec:    227.69MB
```

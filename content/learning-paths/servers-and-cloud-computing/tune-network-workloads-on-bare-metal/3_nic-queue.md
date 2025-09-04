---
title: Tune performance with NIC queue counts
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

After establishing a baseline, you can further improve throughput and latency by tuning your network interface controller (NIC) queue count. Many bare‑metal NICs expose a relatively large number of transmit/receive queues (multi‑queue). Each queue maps to an interrupt; when you limit the server to a small number of online CPUs (for example, 8 cores), too many interrupts can land on the same core and increase context switching. Reducing the number of queues to match available CPUs can stabilize performance on Arm Neoverse systems.

## Set the NIC queue count

Use the following command to find the NIC name corresponding to the IP address:
```bash
ip addr
```
From the output you can see that the NIC name `enp1s0f0np0` corresponds to the IP address `10.169.226.181`:
```output
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute
       valid_lft forever preferred_lft forever
2: enP11p4s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9001 qdisc mq state UP group default qlen 1000
    link/ether 0e:cc:0b:ff:f6:57 brd ff:ff:ff:ff:ff:ff
    inet 172.31.46.193/20 metric 100 brd 172.31.47.255 scope global dynamic enP11p4s0
       valid_lft 1938sec preferred_lft 1938sec
    inet6 fe80::ccc:bff:feff:f657/64 scope link
       valid_lft forever preferred_lft forever
```

Set the network interface name variable:
```bash
net=enp1s0f0np0
```

Use the following command to check the current transmit/receive queues of the ${net} network interface:
```bash
sudo ethtool -l ${net}
```
It can be observed that the number of transmit/receive queues for the ${net} network interface is currently 63.
```bash
Channel parameters for enP11p4s0:
Pre-set maximums:
RX:		n/a
TX:		n/a
Other:		n/a
Combined:	32
Current hardware settings:
RX:		n/a
TX:		n/a
Other:		n/a
Combined:	32
```

Set the number of combined queues to match your online CPUs (example: 8):
   ```bash
   sudo ethtool -L ${NET_IFACE} combined 8
   ```

Verify the change:
   ```bash
   sudo ethtool -l ${NET_IFACE}
   ```

   You should see the `Combined` value updated to `8` under **Current hardware settings**:
   ```output
   Channel parameters for enP11p4s0:
   Pre-set maximums:
   RX:             n/a
   TX:             n/a
   Other:          n/a
   Combined:       32
   Current hardware settings:
   RX:             n/a
   TX:             n/a
   Other:          n/a
   Combined:       8
   ```

{{% notice Note %}}
Queue settings applied with `ethtool -L` are not persistent across reboots. If needed, make the change persistent using a systemd unit or your distro’s NIC configuration mechanism.
{{% /notice %}}

## Measure performance after tuning

Restart Tomcat on your Arm Neoverse bare‑metal instance:
   ```bash
   ~/apache-tomcat-11.0.10/bin/shutdown.sh 2>/dev/null
   ulimit -n 65535 && ~/apache-tomcat-11.0.10/bin/startup.sh
   ```

Run `wrk2` from your `x86_64` bare‑metal client (replace `${tomcat_ip}` with your server IP):
   ```bash
   ulimit -n 65535 && wrk -c1280 -t128 -R500000 -d60 http://${tomcat_ip}:8080/examples/servlets/servlet/HelloWorldExample
   ```

   Example results after tuning NIC queues:
   ```output
     Thread Stats   Avg      Stdev     Max   +/- Stdev
       Latency     8.35s     4.14s   16.33s    61.16%
       Req/Sec     2.96k    73.02     3.24k    89.16%
     22712999 requests in 1.00m, 11.78GB read
   Requests/sec: 378782.37
   Transfer/sec:    201.21MB
   ```

If performance improves and latency stabilizes, keep the adjusted queue count for subsequent tuning steps (RSS/RPS/XPS, IRQ affinity, and NUMA locality).

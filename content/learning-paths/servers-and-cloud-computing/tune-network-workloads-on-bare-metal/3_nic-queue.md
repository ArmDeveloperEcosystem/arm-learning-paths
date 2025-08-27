---
title: Tuning via NIC queue count
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Tuning via NIC queue count
- Setting NIC queue count
- The result after tuning NIC queue count

Typically, the number of transmit/receive queues for network cards in bare-metal environments is relatively large, reaching 63 on Arm Neoverse. Each transmit/receive queue corresponds to one interrupt number. Before CPU cores are taken offline, there are sufficient cores to handle these interrupt numbers. However, when only 8 cores are retained, it results in a single core having to handle multiple interrupt numbers, thereby triggering more context switches.

### Setting NIC queue count

1. Use the following command to find the NIC name corresponding to he IP address.
```bash
ip addr
```
It can be observed that the NIC name `enp1s0f0np0` corresponsed to the IP address `10.169.226.181`.
```bash
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

2. Set the network interface name variable
```bash
net=enp1s0f0np0
```

3. Use the following command to check the current transmit/receive queues of the ${net} network interface
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

4. Use the following command to reset the number of transmit/receive queues for the ${net} to match the number of CPUs, which is 8.
```bash
sudo ethtool -L ${net} combined 8
```
5. Verify whether the settings have been successfully applied.
```bash
sudo ethtool -l ${net}
```
It can be observed that the number of combined Rx/Tx queues has been updated to 8.
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
Combined:	8
```

### The result after tuning NIC queue count

1. Use the following command on the Arm Neoverse bare-metal where `Tomcat` is on
```bash
~/apache-tomcat-11.0.10/bin/shutdown.sh 2>/dev/null
ulimit -n 65535 && ~/apache-tomcat-11.0.10/bin/startup.sh
```

2. And use the following command on the `x86_64` bare-metal where `wrk2` is on
```bash
ulimit -n 65535 && wrk -c1280 -t128 -R500000 -d60 http://${tomcat_ip}:8080/examples/servlets/servlet/HelloWorldExample
```

The result after NIC queue count tuned:
```bash
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     8.35s     4.14s   16.33s    61.16%
    Req/Sec     2.96k    73.02     3.24k    89.16%
  22712999 requests in 1.00m, 11.78GB read
Requests/sec: 378782.37
Transfer/sec:    201.21MB
```

---
title: Tuning via NIC queue count
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Tuning via NIC queue count
- Setting NIC queue count
- The result after tuning NIC queue count

Typically, the number of transmit/receive queues for network cards in bare-metal environments is relatively large, reaching 63 on Grace. Each transmit/receive queue corresponds to one interrupt number. Before CPU cores are taken offline, there are sufficient cores to handle these interrupt numbers. However, when only 8 cores are retained, it results in a single core having to handle multiple interrupt numbers, thereby triggering more context switches.

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
2: enp1s0f0np0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether b8:e9:24:67:d5:3a brd ff:ff:ff:ff:ff:ff
    inet 10.169.226.181/24 brd 10.169.226.255 scope global enp1s0f0np0
       valid_lft forever preferred_lft forever
    inet6 fe80::bae9:24ff:fe67:d53a/64 scope link
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
Channel parameters for enp1s0f0np0:
Pre-set maximums:
RX:		n/a
TX:		n/a
Other:		n/a
Combined:	63
Current hardware settings:
RX:		n/a
TX:		n/a
Other:		n/a
Combined:	63
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
Channel parameters for enp1s0f0np0:
Pre-set maximums:
RX:		n/a
TX:		n/a
Other:		n/a
Combined:	63
Current hardware settings:
RX:		n/a
TX:		n/a
Other:		n/a
Combined:	8
```

### The result after tuning NIC queue count

1. Use the following command on the Grace bare-metal where `Tomcat` is on
```bash
~/apache-tomcat-11.0.9/bin/shutdown.sh 2>/dev/null
ulimit -n 65535 && ~/apache-tomcat-11.0.9/bin/startup.sh
```

2. And use the following command on the `x86_64` bare-metal where `wrk2` is on
```bash
ulimit -n 65535 && wrk -c1280 -t128 -R500000 -d60 http://${tomcat_ip}:8080/examples/servlets/servlet/HelloWorldExample
```

The result after NIC queue count tuned:
```bash
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    21.64s     8.71s   37.22s    57.82%
    Req/Sec     1.53k     5.70     1.55k    77.15%
  11562557 requests in 1.00m, 6.00GB read
Requests/sec: 192932.92
Transfer/sec:    102.49MB
```

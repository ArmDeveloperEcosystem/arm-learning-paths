---
title: Tuning Kernel Parameters
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Base example

In this example I will connect to the server from my remote client that has a higher round trip time. 


```output
Starting Test: protocol: TCP, 1 streams, 131072 byte blocks, omitting 0 seconds, 10 second test, tos 0
...
Test Complete. Summary Results:
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-10.01  sec   187 MBytes   157 Mbits/sec                  sender
[  8]   0.00-10.03  sec   187 MBytes   156 Mbits/sec                  receiver
```



## Modify kernel parameters

On the server, we can configure linux kernel runtime parameters with the `sysctl` command. 

There are a plenthora of dials to tune that relate to performance and security. The following command can be used to list all available dials. The corresponding [kernel documentation](https://docs.kernel.org/networking/ip-sysctl.html#ip-sysctl) can provide a more detailed description of each parameter. 

```bash
sysctl -a | grep tcp
```

Please note: Depending on your operating system, some parameters may not be available. For example on AWS Ubuntu 22.04 LTS only the `cubic` and `reno` algorithms are available (`net.ipv4.tcp_available_congestion_control = reno cubic`).

We can increase the read and write max buffer sizes of the kernel on the server to enable more data to be held. This is at the tradeoff of increased memory utilisation. run the following commands from the server.

```bash
sudo sysctl net.core.rmem_max=134217728
sudo sysctl net.core.wmem_max=134217728
```

Restart the `iperf3` server and rerunning leads to higher achieved bitrate. 

```output
Test Complete. Summary Results:
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-10.00  sec   308 MBytes   258 Mbits/sec                  sender
[  8]   0.00-10.03  sec   307 MBytes   257 Mbits/sec                  receiver

```
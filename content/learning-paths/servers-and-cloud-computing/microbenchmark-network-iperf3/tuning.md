---
title: Tuning Kernel Parameters
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Connecting from Local Machine

Now we can observe ways to mitigate performance degradation due to events such as packet loss. In this example, I will connect to the AWS server node from my local machine to demonstrate a longer response time. Please check the `iperf3` installation guide on the [official documentation](https://iperf.fr/iperf-download.php) if you're not using Ubuntu. As the output below shows we have a larger round trip time in excess of 40ms. 

```output
5 packets transmitted, 5 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 44.896/46.967/49.279/1.444 ms
```

Running a standard TCP client connection with the `iperf3 -c SERVER -V` command shows an average bitrate of 157 Mbps.

```output
Starting Test: protocol: TCP, 1 streams, 131072 byte blocks, omitting 0 seconds, 10 second test, tos 0
...
Test Complete. Summary Results:
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-10.01  sec   187 MBytes   157 Mbits/sec                  sender
[  8]   0.00-10.03  sec   187 MBytes   156 Mbits/sec                  receiver
```



### Modify kernel parameters

On the server, we can configure linux kernel runtime parameters with the `sysctl` command. 

There are a plenthora of dials to tune that relate to performance and security. The following command can be used to list all available dials. The corresponding [kernel documentation](https://docs.kernel.org/networking/ip-sysctl.html#ip-sysctl) can provide a more detailed description of each parameter. 

```bash
sysctl -a | grep tcp
```

{{% notice Note %}}
Depending on your operating system, some parameters may not be available. For example on AWS Ubuntu 22.04 LTS only the `cubic` and `reno` congestion control algorithms are available.
```bash
net.ipv4.tcp_available_congestion_control = reno cubic
```
{{% /notice %}}


We can increase the read and write max buffer sizes of the kernel on the server to enable more data to be held. This is at the tradeoff of increased memory utilisation. run the following commands from the server.

```bash
sudo sysctl net.core.rmem_max=134217728 # default = 212992
sudo sysctl net.core.wmem_max=134217728 # default = 212992
```

Restart the `iperf3` server.  Run the `iperf3 -c SERVER -V` command from the client leads to significantly improved bitrate with no modification on the client side. 

```output
Test Complete. Summary Results:
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-10.00  sec   308 MBytes   258 Mbits/sec                  sender
[  8]   0.00-10.03  sec   307 MBytes   257 Mbits/sec                  receiver

```

This learning path serves as an introduction to microbenchmarking and performance tuning. Which parameters to adjust depends on your own use case and non-functional performance requirements of your system.
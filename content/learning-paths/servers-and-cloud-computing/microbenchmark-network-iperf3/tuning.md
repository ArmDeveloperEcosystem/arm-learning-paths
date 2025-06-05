---
title: Tuning kernel parameters
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Connect from a local machine

You can look at ways to mitigate performance degradation due to events such as packet loss. 

In this example, you will connect to the server node a local machine to demonstrate a longer response time. Check the `iperf3` [installation guide](https://iperf.fr/iperf-download.php) to install `iperf3` on other operating systems. 

Make sure to set the server security group to accept the TCP connection from your local computer IP address. You will also need to use the public IP for the cloud instance.

Running `iperf3` on the local machine and connecting to the cloud server shows a longer round trip time, in this example more than 40ms. 

On your local computer run:

```bash
iperf3 -c <server-public-IP> -V
```

Running a standard TCP client connection with `iperf3` shows an average bitrate of 157 Mbps compared to over 2 Gbps when the client and server are both in AWS.

```output
Starting Test: protocol: TCP, 1 streams, 131072 byte blocks, omitting 0 seconds, 10 second test, tos 0
...
Test Complete. Summary Results:
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-10.01  sec   187 MBytes   157 Mbits/sec                  sender
[  8]   0.00-10.03  sec   187 MBytes   156 Mbits/sec                  receiver
```

### Modify kernel parameters

On the server, your can configure Linux kernel runtime parameters with the `sysctl` command. 

There are a plenthora of values to tune that relate to performance and security. The following command can be used to list all available options. The [Linux kernel documentation](https://docs.kernel.org/networking/ip-sysctl.html#ip-sysctl) provides a more detailed description of each parameter. 

```bash
sysctl -a | grep tcp
```

{{% notice Note %}}
Depending on your operating system, some parameters may not be available. For example on AWS Ubuntu 22.04 LTS only the `cubic` and `reno` congestion control algorithms are available.
```bash
net.ipv4.tcp_available_congestion_control = reno cubic
```
{{% /notice %}}

You can increase the read and write max buffer sizes of the kernel on the server to enable more data to be held. This tradeoff results in increased memory utilization. 

To try it, run the following commands on the server:

```bash
sudo sysctl net.core.rmem_max=134217728 # default = 212992
sudo sysctl net.core.wmem_max=134217728 # default = 212992
```

Restart the `iperf3` server.  

```bash
iperf3 -s
```

Run `iperf3` again on the local machine.

```bash
iperf3 -c <server-public-IP> -V
```

You see a significantly improved bitrate with no modification on the client side. 

```output
Test Complete. Summary Results:
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-10.00  sec   308 MBytes   258 Mbits/sec                  sender
[  8]   0.00-10.03  sec   307 MBytes   257 Mbits/sec                  receiver

```

You now have an introduction to networking microbenchmarking and performance tuning. 
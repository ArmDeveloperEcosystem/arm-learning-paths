---
title: Tune kernel parameters
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

You can further optimize network performance by adjusting Linux kernel parameters and testing across different environments—including local-to-cloud scenarios.

## Connect from a local machine

You can look at ways to mitigate performance degradation due to events such as packet loss. 

In this example, you will connect to the server node a local machine to demonstrate a longer response time. Check the iPerf3 [installation guide](https://iperf.fr/iperf-download.php) to install iPerf3 on other operating systems. 

Before starting the test:

- Update your cloud server’s **security group** to allow incoming TCP connections from your local machine’s public IP.
- Use the **public IP address** of the cloud instance when connecting.

Running iPerf3 on the local machine and connecting to the cloud server shows a longer round trip time, in this example more than 40ms. 

Run this command on your local computer:

```bash
iperf3 -c <server-public-IP> -V
```

Compared to over 2 Gbit/sec within AWS, this test shows a reduced bitrate (~157 Mbit/sec) due to longer round-trip times (for example, >40ms).

```output
Starting Test: protocol: TCP, 1 streams, 131072 byte blocks, omitting 0 seconds, 10 second test, tos 0
...
Test Complete. Summary Results:
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-10.01  sec   187 MBytes   157 Mbits/sec                  sender
[  8]   0.00-10.03  sec   187 MBytes   156 Mbits/sec                  receiver
```

### Modify kernel parameters on the server

On the server, you can configure Linux kernel runtime parameters with the `sysctl` command. 

There are a plethora of values to tune that relate to performance and security. The following command can be used to list all available options. The [Linux kernel documentation](https://docs.kernel.org/networking/ip-sysctl.html#ip-sysctl) provides a more detailed description of each parameter. 

```bash
sysctl -a | grep tcp
```

{{% notice Note %}}
Depending on your operating system, some parameters might not be available. For example, on AWS Ubuntu 22.04 LTS, only the `cubic` and `reno` congestion control algorithms are supported:
```bash
net.ipv4.tcp_available_congestion_control = reno cubic
```
{{% /notice %}}

## Increase TCP buffer sizes

You can increase the kernel's read and write buffer sizes on the server  improve throughput on high-latency connections. This consumes more system memory but allows more in-flight data.

To try it, run the following commands on the server:

```bash
sudo sysctl net.core.rmem_max=134217728 # default = 212992
sudo sysctl net.core.wmem_max=134217728 # default = 212992
```

Then, restart the iPerf3 server:

```bash
iperf3 -s
```

Now rerun iPerf3 again on your local machine:

```bash
iperf3 -c <server-public-IP> -V
```

Without changing anything on the client, the throughput improved by over 60%.

```output
Test Complete. Summary Results:
[ ID] Interval           Transfer     Bitrate
[  8]   0.00-10.00  sec   308 MBytes   258 Mbits/sec                  sender
[  8]   0.00-10.03  sec   307 MBytes   257 Mbits/sec                  receiver

```

You’ve now completed a guided introduction to:

* Network performance microbenchmarking

* Simulating real-world network conditions

* Tuning kernel parameters for high-latency links

* Explore further by testing other parameters, tuning for specific congestion control algorithms, or integrating these benchmarks into CI pipelines for continuous performance evaluation.
---
title: Simulate different network conditions
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

You can simulate latency and packet loss to test how your application performs under adverse network conditions. This is especially useful when evaluating the impact of congestion, jitter, or unreliable connections in distributed systems.

## Add delay to the TCP connection

The Linux `tc` (traffic control) lets you manipulate network interface behavior such as delay, loss, or reordering. 

First, on the client system, identify the name of your network interface: 

```bash
ip addr show
```

The output below shows that the `ens5` network interface device (NIC) is the device that you want to manipulate.

```output
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute 
       valid_lft forever preferred_lft forever
2: ens5: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9001 qdisc mq state UP group default qlen 1000
    link/ether 0a:92:1b:a9:63:29 brd ff:ff:ff:ff:ff:ff
    inet 10.248.213.97/26 metric 100 brd 10.248.213.127 scope global dynamic ens5
       valid_lft 1984sec preferred_lft 1984sec
    inet6 fe80::892:1bff:fea9:6329/64 scope link 
       valid_lft forever preferred_lft forever

```

Run the following command on the client system to add an emulated delay of 10ms on `ens5`: 

```bash
sudo tc qdisc add dev ens5 root netem delay 10ms
```

Rerun the basic TCP test as before on the client:

```bash
iperf3 -c SERVER -v
```

```output
[  5] local 10.248.213.97 port 43170 connected to 10.248.213.104 port 5201
Starting Test: protocol: TCP, 1 streams, 131072 byte blocks, omitting 0 seconds, 10 second test, tos 0
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   282 MBytes  2.36 Gbits/sec    0   8.02 MBytes       
[  5]   1.00-2.00   sec   302 MBytes  2.53 Gbits/sec    0   8.02 MBytes       
[  5]   2.00-3.00   sec   301 MBytes  2.52 Gbits/sec    0   8.02 MBytes       
[  5]   3.00-4.00   sec   302 MBytes  2.54 Gbits/sec    0   8.02 MBytes       
[  5]   4.00-5.00   sec   302 MBytes  2.53 Gbits/sec    0   8.02 MBytes       
[  5]   5.00-6.00   sec   304 MBytes  2.55 Gbits/sec    0   8.02 MBytes       
[  5]   6.00-7.00   sec   302 MBytes  2.53 Gbits/sec    0   8.02 MBytes       
[  5]   7.00-8.00   sec   303 MBytes  2.54 Gbits/sec    0   8.02 MBytes       
[  5]   8.00-9.00   sec   303 MBytes  2.54 Gbits/sec    0   8.02 MBytes       
[  5]   9.00-10.00  sec   301 MBytes  2.53 Gbits/sec    0   8.02 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
Test Complete. Summary Results:
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  2.93 GBytes  2.52 Gbits/sec    0             sender
[  5]   0.00-10.01  sec  2.93 GBytes  2.52 Gbits/sec                  receiver
CPU Utilization: local/sender 3.4% (0.0%u/3.4%s), remote/receiver 11.0% (0.4%u/10.7%s)
snd_tcp_congestion cubic
rcv_tcp_congestion cubic

iperf Done.
```
### Observations

* The `Cwnd` size has grown larger to compensate for the longer response time. 

* The bitrate has dropped from ~4.9 to ~2.3 `Gbit/sec` - demonstrating how even modest latency impacts throughput.

### Simulate packet loss

To test the resiliency of a distributed application, you can add a simulated packet loss of 1%. As opposed to a 10ms delay, this will result in no acknowledgment being received for 1% of packets. 

Given TCP is a lossless protocol, a retry must be sent. 

Run these commands on the client system. The first removes the delay configuration, and the second command introduces a 1% packet loss:

```bash
sudo tc qdisc del dev ens5 root
sudo tc qdisc add dev ens5 root netem loss 1%
```

Now rerunning the basic TCP test, and you will see an increased number of retries (`Retr`) and a corresponding drop in bitrate: 

```bash
iperf3 -c SERVER -v
```

The output is now:

```output
Test Complete. Summary Results:
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  4.41 GBytes  3.78 Gbits/sec  5030             sender
[  5]   0.00-10.00  sec  4.40 GBytes  3.78 Gbits/sec                  receiver
```

## Explore further with tc

The tc tool can simulate:

* Variable latency and jitter
* Packet duplication or reordering
* Bandwidth throttling

For advanced options, refer to Refer to the [tc man page](https://man7.org/linux/man-pages/man8/tc.8.html).

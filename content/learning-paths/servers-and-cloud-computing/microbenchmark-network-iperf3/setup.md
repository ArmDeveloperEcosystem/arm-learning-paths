---
title: Prepare for network performance testing
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Configure two Arm-based Linux computers

To perform network performance testing you need two Linux computers. You can use AWS EC2 instances with Graviton processors or any other Linux virtual machines from another cloud service provider.

You will also experiment with a local computer and a cloud instance to learn the networking performance differences compared to two cloud instances. 

The instructions below use EC2 instances from AWS connected in a virtual private cloud (VPC).

To get started, create two Arm-based Linux instances, one system to act as the server and the other to act as the client. The instructions below use two `t4g.xlarge` instances running Ubuntu 24.04 LTS. 

### Install software dependencies

Use the commands below to install `iperf3`, a powerful and flexible open-source command-line tool used for network performance measurement and tuning. It allows network administrators and engineers to actively measure the maximum achievable bandwidth on IP networks.

Run the following on both systems:

```bash
sudo apt update
sudo apt install iperf3 -y
```

{{% notice Note %}}
If you are prompted to start `iperf3` as a daemon you can answer no.
{{% /notice %}}

## Update Security Rules 

If you are working in a cloud environment like AWS, you need to update the default security rules to enable specific inbound and outbound protocols. 

From the AWS console, navigate to the security tab. Edit the inbound rules to enable `ICMP`, `UDP` and `TCP` traffic to enable communication between the client and server systems. 

![example_traffic](./example_traffic_rules.png)

{{% notice Note %}}
For additional security set the source and port ranges to the values being used. A good solution is to open TCP port 5201 and all UDP ports and use your security group as the source. This doesn't open any traffic from outside AWS.
{{% /notice %}}

## Update the local DNS

To avoid using IP addresses directly, add the IP address of the other system to the `/etc/hosts` file.

The local IP address of the server and client can be found in the AWS dashboard. You can also use commands like `ifconfig`,  `hostname -I`, or `ip address` to find your local IP address.

On the client, add the IP address of the server to the `/etc/hosts` file with name `SERVER`. 

```output
127.0.0.1       localhost
10.248.213.104  SERVER
```

Repeat the same thing on the server and add the IP address of the client to the `/etc/hosts` file with the name `CLIENT`. 

## Confirm server is reachable

Finally, confirm the client can reach the server with the ping command below. As a reference you can also ping the localhost. 

```bash
ping SERVER -c 3 && ping 127.0.0.1 -c 3
```

The output below shows that both SERVER and localhost (127.0.0.1) are reachable. Naturally, the local host response time is ~10x faster than the server. Your results will vary depending on geographic location of the systems and other networking factors. 

```output
PING SERVER (10.248.213.104) 56(84) bytes of data.
64 bytes from SERVER (10.248.213.104): icmp_seq=1 ttl=64 time=0.217 ms
64 bytes from SERVER (10.248.213.104): icmp_seq=2 ttl=64 time=0.218 ms
64 bytes from SERVER (10.248.213.104): icmp_seq=3 ttl=64 time=0.219 ms

--- SERVER ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2056ms
rtt min/avg/max/mdev = 0.217/0.218/0.219/0.000 ms
PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.022 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.032 ms
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.029 ms

--- 127.0.0.1 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2046ms
rtt min/avg/max/mdev = 0.022/0.027/0.032/0.004 ms
```

Continue to the next section to learn how to measure the network bandwidth between the systems.
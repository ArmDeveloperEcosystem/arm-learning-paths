---
title: Connect the Raspberry Pi
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up the edge device

This Learning Path was validated with a Raspberry Pi 5 running 64-bit Raspberry Pi OS. A Raspberry Pi 4 or another Linux-based Arm device can also be used.

Connect to the Raspberry Pi over SSH or open a terminal on an attached display. Confirm that the operating system is 64-bit:

```bash
uname -m
```

Expected output:

```text
aarch64
```

Docker keeps ROS 2 and its dependencies separate from the host operating system. Install Docker if it is not already present:

```bash
curl -fsSL https://get.docker.com | sudo sh
sudo usermod -aG docker $USER
```

Log out and back in so that the new group membership takes effect, and then verify Docker:

```bash
docker version
```

The client and server sections should both report `linux/arm64`.

## Select an address the Raspberry Pi can reach

The `<server_ip>` used on this page must identify the Arm server from the Raspberry Pi's network. It is not automatically the same address used by your laptop.

- Use a private or LAN address when the Raspberry Pi has a route to that network.
- Use a public address only when a private route or VPN is unavailable, and restrict TCP port `7447` to the Raspberry Pi's address or trusted network using firewall rules.
- Do not use `172.x`. Those are internal Docker addresses.

On the Arm server, display the available addresses and select the server's IP:

```bash
hostname -I
```

On the Raspberry Pi, replace `<server_ip>` with the selected address and test the actual Zenoh TCP port:

```bash
python3 -c "import socket; socket.create_connection(('<server_ip>',7447),5); print('router reachable')"
```

Do not leave the angle brackets in the command.

{{% notice Note %}}
If this test times out, fix the network path before starting ROS 2. For an EC2 server, permit inbound TCP port `7447` only from the Raspberry Pi's public egress address or trusted network in the instance security group. Do not allow access from `0.0.0.0/0`.
{{% /notice %}} 

<!-- ## Synchronize the clocks

Zenoh checks timestamps on received data. A large difference between the server and Raspberry Pi can cause messages to be rejected even when topic discovery works.

On both the Arm server and Raspberry Pi, enable network time synchronization:

```bash
sudo timedatectl set-ntp true
timedatectl show --property=NTPSynchronized --value
date -u
```

The synchronization command should eventually return `yes`, and the UTC times should agree closely. Containers use their host's clock, so correct the server or Raspberry Pi host rather than trying to change time inside a container. -->

## Start the edge container

On the Raspberry Pi, replace `<server_ip>` and create the edge container:

```bash
docker run -d --name pi_edge --net=host \
  -e ZENOH_CONFIG_OVERRIDE='mode="client";connect/endpoints=["tcp/<server_ip>:7447"]' \
  odinlmshen/ros2-zenoh-arm:jazzy-edge \
  sleep infinity
```

`--net=host` gives the container direct access to the Raspberry Pi's network interfaces. The configuration override makes every `rmw_zenoh` session in the container connect to the server router as a client.

Enter the container and load ROS 2:

```bash
docker exec -it pi_edge bash
source /opt/ros/jazzy/setup.bash
```

Confirm the middleware and endpoint:

```bash
echo $RMW_IMPLEMENTATION
echo $ZENOH_CONFIG_OVERRIDE
```

Expected output resembles:

```text
rmw_zenoh_cpp
mode="client";connect/endpoints=["tcp/192.168.1.24:7447"]
```

Run `source /opt/ros/jazzy/setup.bash` in every new `docker exec` shell. 


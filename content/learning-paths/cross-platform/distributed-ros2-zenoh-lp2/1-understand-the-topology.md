---
title: Understand the distributed ROS 2 topology
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction

The [first Learning Path](LP1_URL) in this series placed the complete ROS 2 system on one server. In real robot deployments, the setup is much different : the operator station sits elsewhere, sensor nodes run on separate devices, and the monitoring display is on someone's laptop. This learning path distributes that single-machine system across multiple Arm devices. 

Two remote nodes are connected in turn. The `control` container joins over the Docker network and runs RViz to visualise the robot remotely. A Raspberry Pi joins over the physical network using Docker and a single environment variable — no OS reinstallation, no inbound ports, and no configuration files on the device.

The mechanism behind both is Zenoh's client mode, and the reason it is needed rather than peer mode is worth understanding before the hands-on steps — the first section covers it.

Both the server and the Pi run the same arm64 ROS 2 packages. The development machine and the deployment target share one instruction set, so there is no cross-compilation step between them.

<!-- IMAGE PLACEHOLDER: Add an architecture diagram showing the Arm server, robot container, control container, Docker bridge network, TCP port 7447, and Raspberry Pi. Suggested filename: ros2-zenoh-distributed-topology.png -->
<!-- The completed topology is:
![Topology #center](./ros2-zenoh-distributed-topology.png)
-->

## Understand the router and client mode

**The Zenoh router has four roles:**

1. **Configuration entry point** — it reads `ROUTER_CONFIG.json5` once at startup. Any configuration change requires a router restart.
2. **Discovery service for local peers** — it introduces nodes to each other, after which they communicate directly. LP1 Step 3 demonstrated this: stopping the router did not interrupt an established conversation.
3. **Relay for client-mode nodes** — a client holds a single connection to the router, and every message it sends or receives passes through that connection.
4. **Traffic policy enforcement point** — compression, access control, downsampling and QoS rules all apply here (the subject of LP3).

**Why cross-device nodes use client mode:** 

Nodes inside the robot container listen on loopback only. A peer on another container or host learns their addresses through the router, tries to connect directly, and fails — producing a state where `ros2 topic list` shows every topic but no data arrives. A client makes one outbound connection to the router and lets the router relay in both directions, which also suits NAT and firewalled networks since no inbound port is needed.

**How many routers?** Router count follows subsystems, not machines. A remote side running only a few nodes connects them as clients — the approach used here. A remote side that is a multi-node subsystem of its own runs a router locally and links the two routers, so its internal traffic stays local and only cross-system traffic crosses the link.

You can read more about the topology in the [`rmw_zenoh` documentation](https://github.com/ros2/rmw_zenoh#connecting-multiple-hosts).

{{% notice Warning %}}
This Learning Path begins with the completed environment from [Set up a ROS 2 development and simulation environment on an Arm server](LP1_URL). Before you continue, ensure both containers are still running and `/scan` delivers messages at a stable non-zero rate.
{{% /notice %}}

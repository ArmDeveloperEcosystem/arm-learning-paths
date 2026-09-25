---
title: Understand ROS 2, Device Connect, and the example adapter
description: Learn what ROS 2 and Device Connect each provide, and how the ros2-device-connect adapter exposes a ROS 2 container as a Device Connect device.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why connect ROS 2 to Device Connect?

A robot or smart camera built on ROS 2 already has a rich internal graph of nodes, topics, and services. That graph is designed for components *inside* the robot to talk to each other. It isn't designed for other devices on your network, or for AI agents, to discover the robot and ask it structured questions such as "which topics are you publishing?" or "capture a photo".

Device Connect fills that gap. In this Learning Path, you'll run a small adapter next to an unchanged ROS 2 system on an Arm-based Linux machine. The adapter registers the ROS 2 system as a Device Connect device and exposes a safe set of remote procedure calls (RPCs) that any peer or agent can discover and invoke.

For robotics, this pattern matters because a robot is not a single API. It is a live graph of sensors, controllers, diagnostics, services, and safety-critical actions. ROS 2 remains the robot's internal software graph. Device Connect adds an external capability layer, where the device owner chooses which ROS 2 operations become discoverable, typed, and remotely callable functions.

## ROS 2 in brief

ROS 2 (Robot Operating System 2) is an open-source middleware and toolset for building robotics applications. Applications are split into *nodes* that exchange data over *topics* (publish/subscribe), *services* (request/response), and *actions* (long-running goals). ROS 2 publishes official `arm64` packages and container images, so it runs natively on Arm platforms from a Raspberry Pi to a Neoverse cloud server.

This Learning Path uses ROS 2 inside a Docker container and doesn't go deeper into ROS 2 itself. For more background, see:

- [ROS 2 install guide](/install-guides/ros2/) to install ROS 2 natively on Arm Linux and run the talker and listener demo
- [Build a ROS 2 and Zenoh simulation environment on an Arm server](/learning-paths/cross-platform/ros2-zenoh-arm/) for a full containerized ROS 2 robotics workload on Arm, including the `rmw_zenoh` middleware

## Device Connect in brief

[Device Connect](https://github.com/arm/device-connect) is an open-source framework that standardizes how edge devices advertise themselves and exchange structured messages, so that peer devices and AI agents can discover and control them through the same driver model. The pieces you'll use are:

- `DeviceDriver`: a Python base class you subclass to describe a device
- `@rpc` and `@emit`: decorators that expose a method as a callable function or declare an event the device publishes
- `DeviceRuntime`: the runtime that brings a driver online on the messaging network
- `device-connect-agent-tools`: a client library to discover devices and invoke their RPCs from a script or an AI agent

Device Connect supports two deployment styles. In *device-to-device (D2D)* mode, devices find each other directly on the local network using [Zenoh](https://zenoh.io/), with no server. In *server* (or *fabric*) mode, devices connect through a shared broker so they can be reached across networks. This Learning Path uses D2D mode.

To learn the SDK primitives in more depth, see these Learning Paths:

- [Device-to-Device communication with Device Connect](/learning-paths/embedded-and-microcontrollers/device-connect-d2d/) for the developer model and a sensor-to-monitor example
- [Deploy multi-network device meshes using Device Connect server and NATS](/learning-paths/embedded-and-microcontrollers/device-connect-server/) for server mode
- [Connect AI agents to edge devices using Device Connect and Strands](/learning-paths/embedded-and-microcontrollers/device-connect-strands/) for driving devices from an AI agent

## The ros2-device-connect example

The [ros2-device-connect](https://github.com/odincodeshen/ros2-device-connect) repository contains the adapter you'll run. It doesn't modify or link against ROS 2. Instead, it reaches the ROS 2 graph by running ROS 2 command-line tools inside the ROS 2 container with `docker exec`:

```output
Python client  ──Zenoh (D2D)──▶  Device Connect adapter  ──docker exec──▶  ROS 2 container
(agent tools)                    (DeviceDriver on host)                     (ros2 topic list, ...)
```

The repository is organized in three layers:

| Layer | Files | Role |
|---|---|---|
| Shared core | `ros2_common.py` | The `docker exec` bridge plus `Ros2InspectionMixin`, which provides six read-only inspection RPCs for nodes, topics, services, packages, interfaces, and topic info |
| Hardware drivers | `puppypi_device.py`, `camera_device.py` | `DeviceDriver` subclasses that combine the shared core with hardware-specific RPCs, such as capturing a camera frame |
| Profiles and launchers | `profiles/*.env`, `start_d2d.sh`, `start_fabric.sh` | Per-deployment settings that select the driver, the ROS 2 container, and the ROS 2 setup scripts |

The adapter is deliberately narrow. It exposes read-only inspection plus a small, reviewed set of hardware-specific RPCs. It never offers arbitrary topic publishing or service passthrough, so a remote caller can't drive the ROS 2 system in ways the driver author didn't intend.

This means the same adapter pattern can cover different robotics surfaces. A camera profile can expose perception data, a robot profile can expose diagnostics and bounded motion commands, and both can be called through the same Device Connect discovery and RPC model.

## What you've learned and what's next

You've learned that ROS 2 organizes a robot's internal software as a graph of nodes and topics, and that Device Connect makes a device discoverable and callable by peers and agents. The ros2-device-connect adapter joins the two by wrapping ROS 2 command-line tools in Device Connect RPCs.

Next, you'll install Docker, ROS 2, and the Device Connect packages on your Arm-based Linux machine.

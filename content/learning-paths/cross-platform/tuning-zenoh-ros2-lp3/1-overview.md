---
title: Understand ROS 2 sensor traffic constraints over wireless links
weight: 2

description: Understand how ROS 2 sensor traffic can exceed wireless link capacity before evaluating Zenoh traffic-control policies.

layout: learningpathall
---

<!-- ## From a local test to Wi-Fi -->
## Understand wireless traffic constraints

A robot can work correctly in a controlled test environment and still fail when you move its ROS 2 traffic over to Wi-Fi. This is sometimes described as a robot that works on the bench.

The simulation from [Build a ROS 2 and Zenoh simulation environment on an Arm server](/learning-paths/cross-platform/ros2-zenoh-arm/) and [Distribute a ROS 2 robotic system across Arm devices with Zenoh](/learning-paths/cross-platform/distributed-ros2-zenoh-lp2/) published three sensor streams:

| Topic | What it contains | Approximate source traffic |
|---|---|---:|
| `/scan` | A two-dimensional laser scan | 0.4 Mbps |
| `/camera/image_raw` | Camera images | 85 Mbps |
| `/camera/points` | A three-dimensional [point cloud](https://en.wikipedia.org/wiki/Point_cloud) | 700 Mbps |

These three streams together need about 800 Mbps, whereas a typical 2.4 GHz Wi-Fi connection might deliver only 50–100 Mbps of usable throughput. The sender can therefore produce between 8 and 16 times more data than the link can carry.

You'll test four ways to control this traffic: compression, access control, downsampling, and quality of service (QoS) with congestion control. Most policies are applied at the Zenoh router. Compression must be enabled at both ends of the connection.

The work is done in two series:

- In the first experiment, you'll use `tc`/`netem` to emulate a degraded wireless link between two containers on the same server, which isolates each mechanism under repeatable conditions.
- In the second experiment, you'll repeat the measurements with a Raspberry Pi over real Wi-Fi, confirming the conclusions outside the emulator.

## What you've learned and what's next

You've learned that the combined sensor traffic exceeds the capacity of the wireless link. 

Next, you'll set up the environment and record an unconstrained baseline.

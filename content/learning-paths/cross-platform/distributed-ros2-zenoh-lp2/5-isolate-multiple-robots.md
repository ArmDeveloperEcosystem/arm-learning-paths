---
title: Isolate multiple ROS 2 robots
description: Use ROS and Zenoh isolation with ROS domain IDs to separate robots that share a Zenoh router.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why isolation is required

If two robots publish and subscribe with the same names, their ROS 2 graphs overlap. For example, a velocity command published on `/cmd_vel` could be received by both robots.
There are three ways to separate them, at different layers:

| Option | Isolation layer | Applies to |
|---|---|---|
| ROS namespaces (`/robot_1/...`) | ROS graph | Fleet management: one station supervising several robots, all visible at once |
| Separate `ROS_DOMAIN_ID` | Complete separation | Independent groups sharing infrastructure without seeing each other |
| Zenoh namespace (session config) | Zenoh key expressions | Isolation without changing any ROS-side naming |

`rmw_zenoh` encodes the domain ID into its key expressions, and unlike DDS it accepts any value up to `MAX_UINT`. Zenoh namespaces are prefixed to key expressions transparently and stripped on receipt, so they never appear in the ROS graph — but router-side rules that match key expressions must be updated to account for the prefix.

`ros2 topic list` shows the graph visible to your session, filtered by domain, namespace, and access control. It is not a global view of the network.

See the [`rmw_zenoh` design documentation](https://github.com/ros2/rmw_zenoh/blob/rolling/docs/design.md#namespaces) for more details.

## (Optional) Observe and resolve a collision with a second device

With a second edge device, such as another Raspberry Pi, you can see the problem rather than read about it. Start the same edge container on it, pointed at the same router.

On **both** devices, run a talker via bash shells in their running containers:

```bash
ros2 run demo_nodes_cpp talker
```

In the bash shell in the **robot** container:

```bash
ros2 node list
ros2 topic info /chatter
```

**Expected result:** two nodes share the name `/talker`, and `/chatter` reports two publishers. Duplicate node names are not valid in ROS 2 — the graph is now ambiguous, and a subscriber cannot tell the two apart.

```output
Type: std_msgs/msg/String
Publisher count: 2
Subscription count: 0
```

Now isolate them. On the second edge device **only**, set a different ROS domain before starting the talker:

```bash
export ROS_DOMAIN_ID=42
ros2 run demo_nodes_cpp talker
```

**Expected result:** the robot container (still on the default ROS domain) sees a single `/talker` and one publisher — the second device's traffic is invisible to it, because `rmw_zenoh` encodes the ROS domain ID into every key expression.

```output
Type: std_msgs/msg/String
Publisher count: 1
Subscription count: 0
```

This is the `ROS_DOMAIN_ID` row in the isolation-options table and the same mechanism that keeps several groups from interfering when they share one Zenoh router.

## Summary

You can now:

- Extend a containerized ROS 2 system beyond a single Arm server
- Connect the control container using Zenoh client mode
- Add a Raspberry Pi as a remote ROS 2 device over Ethernet and Wi-Fi
- Verify sensor data and messages flowing in both directions
- Compare ROS namespaces and ROS domain IDs for isolating robots

The ROS 2 applications remained unchanged while `rmw_zenoh` handled communication across the distributed system.

You can apply this isolation approach when designing distributed ROS 2 deployments in which multiple robots share Zenoh infrastructure.

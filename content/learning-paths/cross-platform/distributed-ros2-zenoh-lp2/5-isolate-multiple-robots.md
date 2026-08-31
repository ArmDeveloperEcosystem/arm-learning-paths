---
title: Isolate multiple ROS 2 robots that share a Zenoh router
description: Use ROS and Zenoh isolation with ROS domain IDs to separate robots that share a Zenoh router.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why isolation is required

After verifying cross-device communication, you'll learn why you need to analyze ROS 2 robots that share the same Zenoh router and optionally resolve collision.

If two robots publish and subscribe with the same names, their ROS 2 graphs overlap. For example, a velocity command published on `/cmd_vel` could be received by both robots.
There are three ways to separate them, at different layers:

| Option | Isolation layer | Applies to |
|---|---|---|
| ROS namespaces (`/robot_1/...`) | ROS graph | Fleet management: one station supervising several robots, all visible at once |
| Separate `ROS_DOMAIN_ID` | Complete separation | Independent groups sharing infrastructure without seeing each other |
| Zenoh namespace (session config) | Zenoh key expressions | Isolation without changing any ROS-side naming |

`rmw_zenoh` encodes the domain ID into its key expressions. Unlike DDS, `rmw_zenoh` accepts any value up to `MAX_UINT`. Zenoh namespaces are prefixed to key expressions transparently and stripped on receipt, so they never appear in the ROS graph. To account for the prefix, update router-side rules that match key expressions.

`ros2 topic list` shows the graph visible to your session, filtered by domain, namespace, and access control. It's not a global view of the network.

For more information, see the [`rmw_zenoh` design documentation](https://github.com/ros2/rmw_zenoh/blob/rolling/docs/design.md#namespaces).

## (Optional) Observe and resolve a collision with a second device

With a second edge device, such as another Raspberry Pi, you can see the problem. Start the same edge container on it, pointed at the same router.

On both devices, run a talker using bash shells in their running containers:

```bash
ros2 run demo_nodes_cpp talker
```

In the bash shell in the robot container, run:

```bash
ros2 node list
ros2 topic info /chatter
```

You should see two nodes sharing the name `/talker`, and `/chatter` reports two publishers:


```output
Type: std_msgs/msg/String
Publisher count: 2
Subscription count: 0
```
Duplicate node names aren't valid in ROS 2 — the graph is now ambiguous, and a subscriber can't tell the two apart.

Now, isolate them. On the second edge device only, set a different ROS domain before starting the talker:

```bash
export ROS_DOMAIN_ID=42
ros2 run demo_nodes_cpp talker
```

The robot container, still on the default ROS domain, sees a single `/talker` and one publisher:

```output
Type: std_msgs/msg/String
Publisher count: 1
Subscription count: 0
```
The second device's traffic is invisible to it because `rmw_zenoh` encodes the ROS domain ID into every key expression.

This is the `ROS_DOMAIN_ID` row in the isolation-options table and the same mechanism that keeps several groups from interfering when they share one Zenoh router.

## What you've accomplished

You've learned why isolating robots that share the same router is necessary. You've also optionally isolated a collision with a second device.

The ROS 2 applications remained unchanged, while `rmw_zenoh` handled communication across the distributed system.

You can apply this isolation approach when designing distributed ROS 2 deployments in which multiple robots share Zenoh infrastructure.

Next, complete [Tune Zenoh for ROS 2 traffic over wireless networks](/learning-paths/cross-platform/tuning-zenoh-ros2-lp3/).

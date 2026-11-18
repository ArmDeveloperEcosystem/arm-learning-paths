---
title: Observe Zenoh router discovery behavior
description: Run ROS 2 talker and listener nodes through Zenoh, then stop the router to examine how established communication behaves.
weight: 4

layout: "learningpathall"
---

## Understand the router experiment

The Zenoh router helps ROS 2 nodes discover each other. When nodes start, they connect to the router, exchange locator information, and establish direct peer-to-peer links.

You can examine this behavior by stopping the router after a talker and listener have connected. If their established communication continues, the router isn't carrying the messages between these two processes.

Open three bash shells in the `robot` container to observe router discovery behavior. Source the environment in each shell:

```bash
source ~/workshop_env.bash
```

## Start the router

In the first shell, start the Zenoh router:

```bash
just router
```

The output is similar to:

```output
Started Zenoh router with id 84e303525488529a304c8990ad9bed73
```

The router ID can differ on your system.

## Start the ROS 2 nodes

In the second shell, start the talker:

```bash
ros2 run demo_nodes_cpp talker
```

In the third shell, start the listener:

```bash
ros2 run demo_nodes_cpp listener
```

The listener should receive every message published by the talker. The output is similar to:

```output
[INFO] [listener]: I heard: [Hello World: 9]
[INFO] [listener]: I heard: [Hello World: 10]
```

## Stop the router and observe the result

Press **Ctrl+C** in the first shell to stop the router. Keep watching the talker and listener.

The message exchange should continue without interruption. The two nodes already established a direct peer-to-peer connection, so the router isn't in this data path. This result demonstrates the router's discovery role for this established local connection. However, it doesn't imply that every Zenoh topology can operate without a router.

Nodes can also start before the router because each node periodically retries the router connection.

Restart the router in the first shell before continuing:

```bash
just router
```

## What you've accomplished and what's next

You've observed that the router enables discovery while an established talker and listener continue to communicate directly after it stops. 

Next, you'll replace the demonstration nodes with the Neobotix ROX simulation and Navigation2.

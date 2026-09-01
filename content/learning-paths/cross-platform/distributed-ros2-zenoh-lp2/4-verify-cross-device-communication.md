---
title: Verify cross-device ROS 2 communication
description: Verify the ROS 2 graph, sensor data, and bidirectional messages between a Raspberry Pi and an Arm server through Zenoh.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Verify the ROS 2 graph on the Raspberry Pi

In the bash shell for the container running on the Raspberry Pi, list the topics received through the Zenoh client session:

```bash
ros2 daemon stop
ros2 topic list
```

Expected result: the full topic list, roughly 80 entries including:

```output
/camera/image_raw
/cmd_vel
/map
/scan
```

This confirms graph discovery. It does not yet prove that message data is arriving.

## Verify sensor data from the server to the Raspberry Pi

Open a bash shell in the **robot** container running on your Arm server and measure the source rate:

```bash
source ~/workshop_env.bash
ros2 topic hz /scan
```

Let the command collect several samples, record the approximate average, and press **Ctrl+C**.

Now run the same command in the container shell on your Raspberry Pi:

```bash
ros2 topic hz /scan
```

The remote result should be stable and reasonably close to the source rate.

Keep the shells for the **robot** container and the container running on the **Raspberry Pi** open for the next few steps.

## Verify messages from the Raspberry Pi to the server

In the **Raspberry Pi** container shell, start a ROS 2 talker:

```bash
ros2 run demo_nodes_cpp talker
```

In the **robot** container shell, load the original prerequisite Learning Path environment and start a ROS 2 listener:

```bash
source ~/workshop_env.bash
ros2 run demo_nodes_cpp listener
```

The listener running in the **robot** container should receive messages published by the talker running in the **Raspberry Pi** container:

```output
[INFO] [listener]: I heard: [Hello World: 1]
[INFO] [listener]: I heard: [Hello World: 2]
```
![Raspberry Pi talker and robot-container listener exchanging Hello World messages#center](./listner.gif)

This proves the uplink path. The same client connection can carry other ROS 2 traffic, including `/cmd_vel` messages, service calls, and Navigation2 actions.

## Troubleshooting

The following table summarizes common failures:

| Symptom | Cause |
|---|---|
| `Connection refused` | Packets reach the host but nothing listens on the port — the router is not running on the server. After `docker compose up`, restart the router, simulation, and Nav2. |
| `Name or service not known` | The `<your_arm_server_ip>` placeholder was not replaced with the IP address of your Arm server. |
| Timeout or no route to host | A network-layer problem occurred — check that both devices are on the same subnet and that port `7447` is not blocked. |
| `ros2 topic list` shows only 2 topics | The client configuration is not in effect — recheck the three environment lines and run `ros2 daemon stop`. |
| `libzenohc.so` cannot be opened | This applies only to the manual setup — the shell was opened before the packages were installed. Run `source /opt/ros/jazzy/setup.bash` again. |
| `docker exec` reports the container is not running | The shell started with `docker start -ai` was closed, stopping the container. Use `docker start` followed by `docker exec`. |

## What you've accomplished and what's next

You verified ROS 2 graph discovery, sensor data from the Arm server to the Raspberry Pi, and messages from the Raspberry Pi to the server. Next, isolate robots that share the same Zenoh router.

---
title: Connect the control container
description: Configure the control container as a Zenoh client, verify robot topics, and visualize the remote robot in RViz.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Configure the control container as a Zenoh client

The control container needs its own session configuration, set to client mode and pointed at the robot's router.

First, get the container ID for the `control` container. From an SSH session on the Arm server, run:

```bash
docker ps
```

The output is similar to:

```output
CONTAINER ID   IMAGE                                     COMMAND                  CREATED      STATUS      PORTS                                                                                                                               NAMES
471c961e54d8   odinlmshen/ros2-zenoh-arm:jazzy-desktop   "/bin/bash -c /entry…"   4 days ago   Up 4 days   0.0.0.0:7447->7447/tcp, 0.0.0.0:7447->7447/udp, [::]:7447->7447/tcp, [::]:7447->7447/udp, 0.0.0.0:6080->80/tcp, [::]:6080->80/tcp   ros_zenoh-robot-1
4b574fe60afe   odinlmshen/ros2-zenoh-arm:jazzy-desktop   "/bin/bash -c /entry…"   4 days ago   Up 4 days   0.0.0.0:6081->80/tcp, [::]:6081->80/tcp                                                                                             ros_zenoh-control-1

```

Copy the container ID for `ros_zenoh-control-1`, such as `4b574fe60afe`.

Next, open a bash shell in the running `control` container:

```bash
docker exec -it 4b574fe60afe /bin/bash
```

{{% notice Important %}}
Whenever you need a new container shell, repeat `docker ps`, copy the appropriate container ID, and run the `docker exec` command.
{{% /notice %}}

Using this bash shell, copy the installed `rmw_zenoh` session template into the persistent volume:

```bash
cp /opt/ros/jazzy/share/rmw_zenoh_cpp/config/DEFAULT_RMW_ZENOH_SESSION_CONFIG.json5 \
  ~/container_data/SESSION_CONFIG.json5
source ~/workshop_env.bash
nano ~/container_data/SESSION_CONFIG.json5
```

Find the active `mode` field and change it from `peer` to `client`:

```json
mode: "client",
```

Find the active `connect` section and change its endpoint from `localhost` to the robot container IP address 172.1.0.2:

```json
connect: {
  endpoints: ["tcp/172.1.0.2:7447"],
},
```

The same field names can also appear in comments. Edit the active JSON5 values, not a commented example. Save the file and exit Nano with **Ctrl+O**, **Enter**, and **Ctrl+X**.

## Restart ROS 2 graph discovery

Confirm that the environment points to the session file you edited:

```bash
echo $RMW_IMPLEMENTATION
echo $ZENOH_SESSION_CONFIG_URI
```

The expected output includes:

```output
rmw_zenoh_cpp
/home/ubuntu/container_data/SESSION_CONFIG.json5
```

The ROS 2 command-line daemon can retain graph information from an earlier middleware configuration. Stop it before testing the new client session:

```bash
ros2 daemon stop
ros2 topic list
```

The expected output includes topics published in the robot container:

```output
/camera/image_raw
/camera/points
/cmd_vel
/map
/scan
```

Seeing `/parameter_events` and `/rosout` alone does not confirm a connection; those topics are created locally by ROS 2 processes.

Verify that data, rather than only graph information, reaches the control container:

```bash
ros2 topic hz /scan
ros2 topic hz /camera/image_raw
```

Collect several samples and press **Ctrl+C**. The rate should be close to the rate measured in the robot container because the Docker network is not a bottleneck.

<div style="text-align:center;">
  <img src="/learning-paths/cross-platform/distributed-ros2-zenoh-lp2/ros2-topic-rates.png" alt="Control terminal showing /scan near 8.7 Hz and /camera/image_raw near 13.2 Hz, confirming that robot data arrives in the control container." style="max-width:600px; width:100%;" />
  <div style="font-style:italic;">ROS 2 topic-rate measurements in the control container</div>
</div>

{{% notice Note %}}
This example uses an NVIDIA DGX Spark as the Arm server for this Learning Path and the prerequisite Learning Path. Topic rates can vary on other Arm servers, such as AWS Graviton-based instances.
{{% /notice %}}

## Run RViz remotely

Open the control desktop at `http://<your_arm_server_ip>:6081/`. The password is `ubuntu` if prompted.

{{% notice Warning %}}
Remember: Do not expose ports `6080`, `6081`, or `7447` directly to the public internet. Use a private network or VPN, access ports `6080` and `6081` through an SSH tunnel, and restrict port `7447` to trusted IP addresses or subnets using firewall rules.
{{% /notice %}}

Start RViz in the control container after opening a terminal in the control desktop:

```bash
just rviz_nav2
```

RViz now subscribes to the map, transforms, laser scans, costmaps, and robot state across the client connection. The simulation and Navigation2 remain in the robot container.

<div style="text-align:center;">
  <img src="/learning-paths/cross-platform/distributed-ros2-zenoh-lp2/control-container-rviz1.png" alt="RViz in the control container showing the robot, map, costmaps, and active Navigation and Localization, confirming remote visualization." style="max-width:800px; width:100%;" />
  <div style="font-style:italic;">RViz window opened from the control terminal</div>
</div>

This demonstrates the first distributed boundary: the visualization process and the simulated robot are in separate container network namespaces, while ROS 2 communication continues through `rmw_zenoh`.

## What you've accomplished and what's next

You configured the control container as a Zenoh client, verified that robot topics and data arrive, and displayed the remote robot in RViz. Next, connect the Raspberry Pi to the Zenoh router.

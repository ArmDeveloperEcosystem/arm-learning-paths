---
title: Configure Zenoh for ROS 2
description: Create separate Zenoh router and session configuration files, then configure ROS 2 processes to use them.
weight: 3

layout: "learningpathall"
---

## Understand the Zenoh configuration files

`rmw_zenoh` uses two configuration files with different responsibilities:

- `ROUTER_CONFIG.json5` configures the Zenoh router
- `SESSION_CONFIG.json5` configures the normal ROS 2 and Zenoh sessions

Keep the installed templates unchanged. You copy them to `~/container_data/` so you can modify the working copies later. This directory is a Docker volume, so the files persist when the container restarts and are also accessible from the host.

## Open a bash shell in the `robot` container

First, get the container ID for the `robot` container. From an SSH session on the Arm server, run:

```bash
docker ps
```

The output is similar to:

```output
CONTAINER ID   IMAGE                                     COMMAND                  CREATED      STATUS      PORTS                                                                                                                               NAMES
471c961e54d8   odinlmshen/ros2-zenoh-arm:jazzy-desktop   "/bin/bash -c /entry…"   4 days ago   Up 4 days   0.0.0.0:7447->7447/tcp, 0.0.0.0:7447->7447/udp, [::]:7447->7447/tcp, [::]:7447->7447/udp, 0.0.0.0:6080->80/tcp, [::]:6080->80/tcp   ros_zenoh-robot-1
4b574fe60afe   odinlmshen/ros2-zenoh-arm:jazzy-desktop   "/bin/bash -c /entry…"   4 days ago   Up 4 days   0.0.0.0:6081->80/tcp, [::]:6081->80/tcp                                                                                             ros_zenoh-control-1

```

Copy the container ID for `ros_zenoh-robot-1`, such as `471c961e54d8`.

Next, open a bash shell in the running `robot` container:

```bash
docker exec -it 471c961e54d8 /bin/bash
```

{{% notice Important %}}
Whenever you need a new container shell, repeat `docker ps`, copy the appropriate container ID, and run the `docker exec` command.
{{% /notice %}}

Use this bash shell for the next steps.

## Copy the router and session configurations

Using the open bash shell in the `robot` container, copy each installed template to the corresponding working file:

```bash
cp /opt/ros/jazzy/share/rmw_zenoh_cpp/config/DEFAULT_RMW_ZENOH_ROUTER_CONFIG.json5 \
  ~/container_data/ROUTER_CONFIG.json5

cp /opt/ros/jazzy/share/rmw_zenoh_cpp/config/DEFAULT_RMW_ZENOH_SESSION_CONFIG.json5 \
  ~/container_data/SESSION_CONFIG.json5
```

{{% notice Important %}}
The two commands look similar, but the source files are different. Copy `DEFAULT_RMW_ZENOH_ROUTER_CONFIG.json5` to `ROUTER_CONFIG.json5` and `DEFAULT_RMW_ZENOH_SESSION_CONFIG.json5` to `SESSION_CONFIG.json5`.
{{% /notice %}}

## Load the workshop environment

Source the workshop environment so ROS 2 uses the new configuration files:

```bash
source ~/workshop_env.bash
```

The expected output includes both exported paths:

```output
ZENOH_ROUTER_CONFIG_URI=/home/ubuntu/container_data/ROUTER_CONFIG.json5
ZENOH_SESSION_CONFIG_URI=/home/ubuntu/container_data/SESSION_CONFIG.json5
```

{{% notice Note %}}
From this point, run `source ~/workshop_env.bash` whenever you open a new bash shell in the `robot` container.
{{% /notice %}}

## What you've accomplished and what's next

You've created separate router and session configurations and confirmed both exported paths in the ROS 2 environment. Next, you'll use three ROS 2 processes to observe the router's role in discovery.

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

## Copy the router and session configurations

Open a terminal in the `robot` container. Copy each installed template to the corresponding working file:

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

The output should show both exported paths:

```output
ZENOH_ROUTER_CONFIG_URI=/home/ubuntu/container_data/ROUTER_CONFIG.json5
ZENOH_SESSION_CONFIG_URI=/home/ubuntu/container_data/SESSION_CONFIG.json5
```

{{% notice Note %}}
From this point, run `source ~/workshop_env.bash` whenever you open a new terminal in the `robot` container.
{{% /notice %}}

## What you've accomplished and what's next

You've created and verified separate router and session configurations, then loaded their paths into the ROS 2 environment. Next, you'll use three ROS 2 processes to observe the router's role in discovery.

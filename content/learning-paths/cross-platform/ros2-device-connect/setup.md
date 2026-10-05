---
title: Set up ROS 2 and Device Connect on Arm Linux
description: Install Docker, start a ROS 2 Humble container with a demo publisher, and install the Device Connect Python packages and the ros2-device-connect adapter.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin

Run every command in this section on your Arm-based Linux machine. The instructions assume Ubuntu 22.04 or later on an `aarch64` host, such as a Raspberry Pi 5 or an Arm cloud instance. Confirm the architecture:

```bash
uname -m
```

```output
aarch64
```

By the end of this section, you'll have:

- a ROS 2 Humble container publishing a demo topic
- a Python virtual environment with the Device Connect packages
- the ros2-device-connect adapter cloned and ready to run

## Install Docker

The adapter talks to ROS 2 through Docker, so you need Docker Engine. Follow the [Docker Engine install guide](/install-guides/docker/docker-engine/), including the step that adds your user to the `docker` group. The adapter runs `docker exec` as your user, so Docker must work without `sudo`.

## Start a ROS 2 container

You don't need to install ROS 2 on the host. The official `ros:humble` image is multi-architecture, so Docker pulls the `arm64` variant automatically. If you'd prefer a native install, see the [ROS 2 install guide](/install-guides/ros2/).

Start a long-running container named `ros2_test`:

```bash
docker run -d --name ros2_test ros:humble tail -f /dev/null
```

The `tail -f /dev/null` command keeps the container alive so you can run ROS 2 commands inside it with `docker exec`. Start a demo publisher that sends a `std_msgs/msg/String` message on the `/chatter` topic once per second:

```bash
docker exec -d ros2_test bash -lc 'source /opt/ros/humble/setup.bash && ros2 topic pub -r 1 /chatter std_msgs/msg/String "{data: hello}"'
```

Check that the topic is being published:

```bash
docker exec ros2_test bash -lc 'source /opt/ros/humble/setup.bash && ros2 node list && ros2 topic list'
```

The output lists the ROS 2 topics:

```output
/chatter
/parameter_events
/rosout
```

The node list is empty because `ros2 topic pub` runs as a hidden node. This container now stands in for a real robot's ROS 2 stack.

## Create the workspace

The adapter's launch scripts expect a single project directory that holds the adapter repository and a Python virtual environment named `.venv`. Create that directory and clone both the adapter and the Device Connect source. The adapter is cloned at the `ros2_dc_lp` tag, which is the version this Learning Path was tested with:

```bash
mkdir -p ~/device_connect
cd ~/device_connect
git clone --branch ros2_dc_lp https://github.com/odincodeshen/ros2-device-connect.git
git clone https://github.com/arm/device-connect.git
```

## Install uv and the Device Connect packages

This Learning Path uses [uv](https://docs.astral.sh/uv/) to create the Python environment. Install it:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
uv --version
```

Create a Python virtual environment in the project directory, and install the Device Connect edge SDK and agent tools from the cloned source. The Device Connect packages require Python 3.11 or later and are tested on Python 3.11, 3.12, and 3.13. This example uses 3.12, but you can pass any supported version to `--python`. If that version isn't installed on your machine, uv downloads it for you.

This host Python environment is separate from the Python version inside the ROS 2 container, so your choice here doesn't need to match your ROS 2 distribution.

```bash
cd ~/device_connect
uv venv --python 3.12 .venv
VIRTUAL_ENV=.venv uv pip install \
  -e device-connect/packages/device-connect-edge \
  -e device-connect/packages/device-connect-agent-tools
```

The `device-connect-edge` package is the device runtime that the adapter runs on. The `device-connect-agent-tools` package is the client you'll use to discover the adapter and call its RPCs.

Verify that both packages import:

```bash
.venv/bin/python -c "import device_connect_edge, device_connect_agent_tools; print('Device Connect OK')"
```

```output
Device Connect OK
```

Your workspace now looks like this:

```output
~/device_connect/
├── .venv/                  # Python environment with Device Connect
├── device-connect/         # Device Connect SDK source
└── ros2-device-connect/    # ROS 2 adapter
```

## What you've accomplished and what's next

You've installed Docker, started a ROS 2 Humble container publishing on `/chatter`, and created a Python environment with the Device Connect packages next to the ros2-device-connect adapter.

Next, you'll look at how the adapter code works, start it in D2D mode, and query the ROS 2 container through Device Connect.

---
title: Set up the developer environment
weight: 3

# FIXED, DO NOT MODIFY
layout: learningpathall
---

## Verify the required tools

Before cloning any repositories, confirm that Python 3.12 and Git are available:

```bash
python3.12 --version
git --version
```

These instructions are tested on Python 3.12. Earlier versions of Python 3 may work but are not validated against the `feat/device-connect-integration-draft` branch used in this Learning Path.

## Clone the repository

The code run in this Learning Path sits in the `robots` repository. It contains the robot runtime and the `robot_mesh` Strands tool.

```bash
mkdir ~/strands-device-connect
cd strands-device-connect
git clone https://github.com/atsyplikhin/robots.git
```

## Check out the integration branch

The Device Connect integration code for `robots` lives on the `feat/device-connect-integration-draft` branch. This branch adds the `RobotDeviceDriver` adapter and the updated `robot_mesh` tool that routes calls through the Device Connect SDK rather than the raw Zenoh mesh.

TODO: remove feature branch? replace robots and feat/device-connect-integration-draft

```bash
cd ~/strands-device-connect/robots
git checkout feat/device-connect-integration-draft
cd ..
```

## Create a Python virtual environment

Create a single virtual environment at the workspace root, then activate it:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

Now install the packages and make sure they are available on your `PYTHONPATH` environment variable:

```bash
pip install -e ".[sim]"
export PYTHONPATH="$PWD:$PYTHONPATH"
```

## How discovery works — no configuration needed

The `strands-robots` SDK uses Device Connect's built-in device-to-device discovery: every `Robot()` instance announces itself on the local network at startup, and any process running `discover_devices()` or `robot_mesh(action='peers')` on the same network segment will find it automatically.

This means discovery works as long as the device process and the agent process are on the same LAN or on the same machine. Discovery is typically available on home and office networks. If you are behind a firewall or VPN that blocks local network traffic, devices will not discover each other — that scenario requires the infrastructure-backed setup with a Zenoh router, which is covered later in this Learning Path.

## What you've set up and what's next

At this point you have:

- `robots` cloned with the `feat/device-connect-integration` branch.
- A single Python 3.12 virtual environment with the Device Connect SDK, agent tools, and robot simulation runtime all installed.

The next section walks you through starting a simulated robot and invoking it from both the agent tools and the `robot_mesh` Strands tool.
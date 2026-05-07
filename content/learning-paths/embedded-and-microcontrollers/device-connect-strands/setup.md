---
title: Set up the Device Connect and Strands developer environment
weight: 3

# FIXED, DO NOT MODIFY
layout: learningpathall
---

## Verify the required tools

Before cloning the repository, confirm that Git is available:

```bash
git --version
```

## Clone the repository

Clone the `robots` repository, which contains the robot runtime and the `robot_mesh` Strands tool:

```bash
mkdir ~/strands-device-connect
cd strands-device-connect
git clone https://github.com/strands-labs/robots
```

## Install dependencies

The repository includes a `setup.sh` script that installs `uv`, creates a Python 3.12 virtual environment, and installs all required packages:

```bash
cd ~/strands-device-connect/robots
./strands_robots/device_connect/setup.sh
source .venv/bin/activate
```

## How discovery works - no configuration needed

The `strands-robots` SDK uses Device Connect's built-in device-to-device discovery: every `Robot()` instance announces itself on the local network at startup, and any process running `discover_devices()` or `robot_mesh(action='peers')` on the same network segment will find it automatically.

This means discovery works as long as the device process and the agent process are on the same LAN or on the same machine. Discovery is typically available on home and office networks. If you're behind a firewall or VPN that blocks local network traffic, devices won't discover each other - that scenario requires the infrastructure-backed setup with a Zenoh router, which is covered later in this Learning Path.

## What you've set up and what's next

At this point you've:

- Cloned the `robots` repository.
- Created a Python 3.12 virtual environment with the Device Connect SDK, agent tools, and robot simulation runtime all installed.

The next section walks you through starting a simulated robot and invoking it from both the agent tools and the `robot_mesh` Strands tool.
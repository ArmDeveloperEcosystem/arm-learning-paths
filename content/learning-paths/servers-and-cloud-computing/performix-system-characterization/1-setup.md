---
title: Set up Performix and the target machine
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understanding the System Characterization recipe

The System Characterization recipe runs several low-level benchmarks, diagnostic scripts, and system tests to analyze performance on Arm-based platforms.
It evaluates key hardware characteristics, such as memory latency and bandwidth, and is especially suited for platform bring-up, system tuning, and architectural comparison tasks. It helps developers and system architects gain early and repeatable insights into performance-critical subsystems.

## Before you begin

Make sure Arm Performix is installed on your host machine. The host machine is your local computer where the Arm Performix GUI runs, and it can be a Windows, macOS, or Linux machine. The target machine is the Linux server where your application is compiled and where the application runs.

If you don't have Arm Performix installed, see the [Arm Performix install guide](/install-guides/performix/). 

From the host machine, open the Arm Performix application and navigate to the **Targets** tab. Set up an SSH connection to the target to benchmark and test the connection.

The System Characterization recipe requires `python` and the `numactl` utility.
Connect to your target machine using SSH and install these required OS packages.

For Ubuntu and other Debian-based distributions, run the following command:

```bash
sudo apt-get install python3 python3-venv numactl -y
```

## What you've learned and what's next

In this section:
- You set up the target machine and established an SSH connection.
- You installed packages necessary for the System Characterization recipe to benchmark your platform.

Next, you'll run the recipe and see how your hardware platform is performing.

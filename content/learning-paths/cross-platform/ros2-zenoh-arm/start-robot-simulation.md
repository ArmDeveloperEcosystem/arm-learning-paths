---
title: Start the robot simulation and Navigation2
description: Launch the Neobotix ROX simulation in headless Gazebo, start Navigation2, and verify its sensor data and lifecycle state.
weight: 5

layout: "learningpathall"
---

## Understand the simulation stack

The running robot uses two components:

- `rox_simu` loads the Neobotix ROX model into Gazebo, simulates its sensors and motors, and publishes laser scan, camera, and odometry data
- `rox_nav2` runs Navigation2 for localization, path planning, and velocity control

The simulation and navigation stack run as separate processes so you can start, stop, and observe each component independently.

Stop the talker and listener from the router experiment. Keep the router running.

Open two new terminals in the `robot` container and source the environment in each one:

```bash
source ~/workshop_env.bash
```

## Start the headless simulation

In one of the new Terminals, start the simulation:

```bash
just rox_simu no_gui
```

The `no_gui` argument disables the Gazebo 3D viewer, not the simulation. Gazebo continues to simulate the robot and publish sensor data while using less CPU.

## Start Navigation2

In the other Terminal, start the navigation stack:

```bash
just rox_nav2
```

Wait for Navigation2 to activate its managed nodes.

It is normal for output to stop after its active. Navigation2 remains idle until it receives a navigation goal.

![Navigation2 terminal output showing managed nodes active while the navigation stack starts in the robot container.](images/nav2-successfully-running.webp)

## Verify the simulated sensors

In another sourced terminal, check the laser scan frequency:

```bash
ros2 topic hz /scan
```

The `/scan` topic should arrive at approximately 8 Hz. This rate is an expected operating observation, so small variations are normal.

List the camera topics using a new terminal:

```bash
ros2 topic list | grep camera
```

The output should include `/camera/image_raw`, `/camera/points`, and `/camera/depth/image_raw`.

## What you've accomplished and what's next

You've started the headless Gazebo simulation, activated Navigation2, and verified that laser and camera sensor data is available. Next, you'll use RViz to inspect the navigation data and send the robot a goal.

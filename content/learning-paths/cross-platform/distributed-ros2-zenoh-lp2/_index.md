---
title: Distribute a ROS 2 robotic system across Arm devices with Zenoh

draft: true
cascade:
    draft: true

minutes_to_complete: 60

description: Learn how to use rmw_zenoh to extend a containerized ROS 2 robotic simulation from an Arm server to a remote control environment and a Raspberry Pi.

who_is_this_for: This Learning Path is for robotics developers who want to distribute an existing ROS 2 system across Arm-based cloud and edge devices. It is intended for learners who have completed the preceding Learning Path, or already have an equivalent ROS 2 Jazzy simulation running with rmw_zenoh and Docker.

learning_objectives:
    - Explain how Zenoh router and client modes support ROS 2 communication across containers and physical devices
    - Configure a remote control container to connect to a ROS 2 simulation through rmw_zenoh
    - Connect a Raspberry Pi to the Zenoh router running on an Arm server
    - Verify ROS 2 sensor data and messages flowing in both directions between the server and Raspberry Pi
    - Diagnose routing, port, configuration, and clock-synchronization problems in a distributed ROS 2 system

prerequisites:
    - Learning Path 1 completed; `robot` container running the Zenoh router and ROX simulation
    - A Raspberry Pi 4 or Raspberry Pi 5 (16 GB SD card or larger), aarch64, on the same network as the server
    - Familiarity with ROS 2 topics, Docker, and basic Linux command-line operations

author:
    - Odin Shen
    - Kwashie Andoh
    - Habib Ogunbanwo

skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Neoverse
tools_software_languages:
    - ROS 2
    - Docker
    - Raspberry Pi
    - Zenoh

operatingsystems:
    - Linux

### Cross-platform metadata only
shared_path: true
shared_between:
    - automotive

further_reading:
    - resource:
        title: Build and deploy multi-node Zenoh systems on Raspberry Pi
        link: https://learn.arm.com/learning-paths/cross-platform/zenoh-multinode-ros2/
        type: documentation
    - resource:
        title: ROS 2 middleware implementation for Eclipse Zenoh
        link: https://github.com/ros2/rmw_zenoh
        type: documentation
    - resource:
        title: Eclipse Zenoh documentation
        link: https://zenoh.io/docs/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

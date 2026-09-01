---
title: Build a ROS 2 and Zenoh simulation environment on an Arm server

draft: true
cascade:
    draft: true

description: Set up ROS 2 Jazzy with rmw_zenoh in Docker, then run and evaluate a Neobotix ROX simulation on an Arm server.

minutes_to_complete: 60

who_is_this_for: Developers who want to build and examine a containerized ROS 2 robotics simulation on an Arm server.

learning_objectives:
    - Set up a Docker-based ROS 2 Jazzy development and simulation environment on an Arm server
    - Configure `rmw_zenoh` as the ROS 2 middleware and explore communication between ROS 2 nodes
    - Launch and interact with a Neobotix ROX robot simulation using Gazebo, Navigation2, and RViz
    - Evaluate Zenoh router behaviour and the effect of shared-memory transport

prerequisites:
    - An Arm server running Linux with at least 8 CPU cores, 16 GB of RAM, and 30 GB of free disk space
    - Docker and Docker Compose installed
    - Network access to ports 6080 and 6081 on the Arm server
    - Familiarity with launching bash shells within a running Docker container
    - Basic familiarity with Linux terminal commands within bash shells

author:
    - Odin Shen
    - Kwashie Andoh
    - Habib Ogunbanwo

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
armips:
    - Neoverse
tools_software_languages:
    - ROS 2
    - rmw_zenoh
    - Docker
    - Gazebo
    - Navigation2
    - RViz
operatingsystems:
    - Linux

shared_between:
    - embedded-and-microcontrollers
    - automotive

further_reading:
    - resource:
        title: ROS 2 Jazzy RMW implementations
        link: https://docs.ros.org/en/jazzy/Installation/RMW-Implementations.html
        type: documentation
    - resource:
        title: rmw_zenoh source and documentation
        link: https://github.com/ros2/rmw_zenoh
        type: documentation
    - resource:
        title: Navigation2 getting started
        link: https://docs.nav2.org/getting_started/index.html
        type: documentation
    - resource:
        title: Gazebo Harmonic getting started
        link: https://gazebosim.org/docs/harmonic/getstarted/
        type: documentation
    - resource:
        title: ROS 2 and Zenoh on Arm source repository
        link: https://github.com/odincodeshen/ros2-zenoh-arm
        type: website
    - resource:
        title: Install Docker
        link: /install-guides/docker/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

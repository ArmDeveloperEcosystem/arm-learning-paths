---
title: Deploying Mixed-Criticality Autonomous Driving software using Arm containers

draft: true
cascade:
    draft: true

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for automotive developers, aimed at helping them accelerate autonomous driving software development before the automotive computing hardware board is fully ready.

learning_objectives: 
    - Introduction to the SOAFEE architecture and its role in supporting Shift-Left software development strategies to optimize the autonomous driving development process.
    - Overview of the Autoware OpenADKit simulation environment.
    - Running containerized workloads on Arm Neoverse V3AE with Docker, supporting execution on both cloud-based and on-premise servers.
    - Exploring advanced configurations and future development prospects.
prerequisites:
    - An Arm-based Neoverse cloud instance, or a local Arm Neoverse Linux computer with at least 16 CPUs and 32GB of RAM.
    - Familiarity with Docker operation.

author: Odin Shen

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
armips:
    - Neoverse V3AE
tools_software_languages:
    - Python
    - Docker
    - ROS2
operatingsystems:
    - Linux


further_reading:
    - resource:
        title: ROS2 installation
        link: https://learn.arm.com/install-guides/ros2/
        type: documentation
    - resource:
        title: Autoware OpenAD Kit demo project
        link: https://github.com/autowarefoundation/openadkit_demo.autoware/
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

---
title: Scalable Networking for Industrial and Robotics with Zenoh on Raspberry Pi

draft: true
cascade:
    draft: true

minutes_to_complete: 45

who_is_this_for: This learning path is designed for robotics developers, industrial automation engineers, and IoT system architects building distributed, scalable, and low-latency applications. Whether you are using Robot Operating System (ROS), developing autonomous systems, or designing multi-node communication frameworks, this guide will show you how to leverage the Eclipse Zenoh protocol on Arm-based platforms — both in the cloud (AVH or EC2) and on physical devices like Raspberry Pi.

learning_objectives: 
    - Understand Zenoh’s architecture and its integration of pub/sub, storage, querying, and computation models.
    - Build and run Zenoh examples on both Arm servers and Raspberry Pi.
    - Set up and deploy a multi-node Zenoh system using Arm-based hardware or virtual environments.

prerequisites:
    - At least two [Raspberry Pi5 or Pi4](https://www.raspberrypi.com/products/raspberry-pi-5/) or other Cortex-A instances with a Linux-based OS installed.
    - Basic understanding with the Linux command line.
    - Experience with ROS 2 applications.
    - Corellium account for virtual hardware testing. (Option)

author: 
    - Odin Shen
    - William Liang
    - ChenYing Kuo

skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Neoverse
tools_software_languages:
    - ROS2
    - C
    - Raspberry Pi

operatingsystems:
    - Linux
### Cross-platform metadata only
shared_path: true
shared_between:
    - iot
    - automotive

further_reading:
    - resource:
        title: Eclipse Zenoh Website
        link: https://zenoh.io/
        type: documentation
    - resource:
        title: Eclipse Zenoh Github
        link: https://github.com/eclipse-zenoh/zenoh
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

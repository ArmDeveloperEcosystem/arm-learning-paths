---
title: Tune Zenoh for ROS 2 traffic over wireless networks

draft: true
cascade:
    draft: true

minutes_to_complete: 120

description: Measure ROS 2 sensor traffic, tune Zenoh with compression, access control, downsampling, and QoS, and select a suitable wireless deployment policy.

who_is_this_for: This Learning Path is for robotics developers who want to understand how Zenoh manages ROS 2 sensor traffic over Wi-Fi. You should already have basic experience setting up and distributing a ROS 2 Jazzy system with rmw_zenoh, as covered in the previous Learning Paths in this series.

learning_objectives:
    - Measure the rate, bandwidth, and regularity of ROS 2 sensor data at a remote receiver
    - Reproduce a constrained wireless link with Linux traffic control
    - Configure Zenoh compression, access control, downsampling, and quality of service policies
    - Validate the policies over real Wi-Fi and select a suitable deployment configuration

prerequisites:
    - The ROS 2 simulation environment from Learning Path 1, with the `robot` and `control` containers available
    - The distributed Zenoh configuration from Learning Path 2, with the `control` container connected in client mode
    - An **Arm server** with the Docker Compose configuration used in Learning Paths 1 and 2
    - A **Raspberry Pi** connected over Wi-Fi
    - Familiarity with ROS 2 topics, Docker, and basic Linux commands

author:
    - Kwashie Andoh
    - Odin Shen
    - Habib Ogunbanwo

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Neoverse
tools_software_languages:
    - ROS 2
    - rmw_zenoh
    - Zenoh
    - Docker
    - Linux traffic control
operatingsystems:
    - Linux

### Cross-platform metadata only
shared_path: true
shared_between:
    - automotive

further_reading:
    - resource:
        title: Build a ROS 2 and Zenoh simulation environment on an Arm server
        link: /learning-paths/cross-platform/ros2-zenoh-arm/
        type: documentation
    - resource:
        title: Distribute a ROS 2 robotic system across Arm devices with Zenoh
        link: /learning-paths/cross-platform/distributed-ros2-zenoh-lp2/
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

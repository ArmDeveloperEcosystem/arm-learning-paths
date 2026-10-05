---
title: Expose an Arm-based ROS 2 system as a discoverable device on Device Connect 
    
description: Learn how to expose a ROS 2 system running in Docker on an Arm-based Linux device as a discoverable Device Connect device, and inspect its ROS 2 graph through remote procedure calls.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for robotics and edge developers who want to get started with making a Robot Operating System 2 (ROS 2) system discoverable and callable by other devices and AI agents using Device Connect, without changing the ROS 2 application itself.

learning_objectives:
    - Identify how a Device Connect adapter bridges a containerized ROS 2 system to a Device Connect network.
    - Set up ROS 2 in Docker and the Device Connect Python packages on an Arm-based Linux machine.
    - Run the adapter in device-to-device (D2D) mode and call read-only ROS 2 inspection RPCs from a Python client.
    - Describe how deployment profiles map the same adapter onto real hardware such as a Raspberry Pi 5 with a camera.

prerequisites:
    - An Arm-based Linux machine, such as a Raspberry Pi 5, an Arm cloud instance, or an Arm-based laptop, running Ubuntu 22.04 or later
    - Basic familiarity with Python, the Linux command line, and ROS 2 concepts such as nodes and topics

author: 
    - Kieran Hejmadi
    - Odin Shen

# New Learning Paths are opted in for the next manual generated summary/FAQ run.
# The generator resets this to false after a successful write.
generate_summary_faq: true

# Optional one-shot controls: set either field to true to regenerate just that
# generated section the next time the summary/FAQ tool runs. The tool resets
# them to false after a successful write.
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Libraries
armips:
    - Cortex-A
    - Neoverse
tools_software_languages:
    - ROS 2
    - Docker
    - Python
    - Zenoh
operatingsystems:
    - Linux

### Cross-platform metadata only
shared_path: true
shared_between:
    - automotive
    - embedded-and-microcontrollers

further_reading:
    - resource:
        title: ros2-device-connect example repository
        link: https://github.com/odincodeshen/ros2-device-connect
        type: website
    - resource:
        title: Device Connect repository
        link: https://github.com/arm/device-connect
        type: website
    - resource:
        title: ROS 2 documentation
        link: https://docs.ros.org/en/humble/
        type: documentation
    - resource:
        title: Device-to-Device communication with Device Connect
        link: /learning-paths/embedded-and-microcontrollers/device-connect-d2d/
        type: website
    - resource:
        title: Build a ROS 2 and Zenoh simulation environment on an Arm server
        link: /learning-paths/cross-platform/ros2-zenoh-arm/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

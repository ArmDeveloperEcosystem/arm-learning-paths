---
title: Access remote devices with Remote.It

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for software developers who want to use Remote.It to establish private network connections between users and devices or devices to device.

learning_objectives:
    - Install Remote.It on target devices (devices you would like to access remotely)
    - Access your Remote.It enabled devices from anywhere
    - Understand the different types of network connections (proxy vs. Peer to peer)

prerequisites:
    - A Windows, macOS, or Linux computer which you will use to configure your devices as well as connect to your remote devices.
    - A device/computer to which you would like remote access. A device can be a Windows, Mac, or Linux computer including development kits such as Raspberry Pi or cloud-hosted such as within Arm Virtual Hardware or within AWS. You will need a method to control this device before Remote.It is deployed which can be local access or access via another remote connectivity solution (Remote Desktop, VPN, etc.)
    - Determine if your device that you would like to access remotely also needs to make connections to other Remote.It devices.

author_primary: Brenda Strech

### Tags
skilllevels: Introductory
subjects: CI-CD
armips:
    - Neoverse
    - Cortex-A
tools_software_languages:
    - Remote.It
operatingsystems:
    - Linux
    - Windows
    - macOS

### Test
test_images:
- ubuntu:latest
test_maintenance: false

### Cross-platform metadata only
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - embedded-and-microcontrollers
    - iot

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

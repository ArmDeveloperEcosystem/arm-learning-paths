---
title: Device-to-Device communication with Device Connect

minutes_to_complete: 25

who_is_this_for: This is an introductory topic for developers wiring up heterogeneous edge fleets, where devices need a shared way to find each other and a shared way to be controlled by agents. Device Connect provides this communication protocol between agents and devices, and standardizes how devices from different vendors advertise themselves and exchange structured messages, so both peer devices and AI agents can discover and invoke them through the same driver model. You'll use it to stand up peer-to-peer communication between two devices, with no broker or cloud service in between.

learning_objectives:
    - Understand Device Connect Edge SDK primitives and use them to build a device driver that exposes capabilities like discovery, RPC, events, and status to other peers on the mesh
    - Set up a Python environment for Device Connect with no hardware required
    - Build two cooperating drivers, a simulated sensor that exposes an RPC method and emits readings on a schedule, and a threshold monitor that subscribes to those events with `@on` and emits its own alerts in response
    - Run both devices as independent runtimes and watch them discover and invoke each other on the same network
    - Use the Device Connect agent tools to discover both devices on the mesh and invoke their RPCs

prerequisites:
    - Basic familiarity with Python and the command line

author:
    - Kavya Sri Chennoju
    - Annie Tallund

### Tags
skilllevels: Introductory
subjects: Libraries
armips:
    - Cortex-A
operatingsystems:
    - Linux
    - macOS
tools_software_languages:
    - Python

further_reading:
    - resource:
        title: Device Connect repository
        link: https://github.com/arm/device-connect
        type: website
    - resource:
        title: device-connect-edge package
        link: https://github.com/arm/device-connect/tree/main/packages/device-connect-edge
        type: documentation
    - resource:
        title: Zenoh
        link: https://zenoh.io/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

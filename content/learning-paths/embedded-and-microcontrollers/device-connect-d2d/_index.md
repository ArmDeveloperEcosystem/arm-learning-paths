---
title: Device-to-Device communication with Device Connect

minutes_to_complete: 25

who_is_this_for: This is an introductory topic for developers wiring up heterogeneous edge fleets, where devices need a shared way to find each other and a shared way to be controlled by agents. Device Connect provides this communication protocol between agents and devices, and standardizes how devices from different vendors advertise themselves and exchange structured messages, so both peer devices and AI agents can discover and invoke them through the same driver model. You'll use a Raspberry Pi 5 as the example primary edge device, but the same flow works with another device or with your development machine acting as a simulated device.

learning_objectives:
    - Understand Device Connect Edge SDK primitives 
    - Set up a Python environment for Device Connect on an example edge device and a development machine
    - Build two device runtimes, with the primary sensor runtime shown on a Raspberry Pi 5
    - Use the Device Connect agent tools to discover both devices on the mesh and invoke their RPCs

prerequisites:
    - Basic familiarity with Python and the command line
    - A Raspberry Pi 5, another Linux device, or your development machine to use as the example primary device
    - A development machine on the same local network if you run the example across two machines

author:
    - Kavya Sri Chennoju
    - Annie Tallund

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Libraries
armips:
    - Cortex-A
operatingsystems:
    - Linux
    - macOS
    - Windows
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


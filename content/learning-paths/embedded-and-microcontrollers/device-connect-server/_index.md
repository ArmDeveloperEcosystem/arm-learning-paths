---
title: Deploy multi-network device meshes using Device Connect server and NATS

description: Connect devices and AI agents across networks using Device Connect server. Learn to provision NATS credentials, commission devices, manage persistent registry, and orchestrate multi-network IoT fleets with secure authentication.
minutes_to_complete: 30

who_is_this_for: This Learning Path is for developers who have completed the Device-to-device Learning Path and want to build a globally connected fleet of devices and AI agents on top of their Device Connect mesh. You'll add a server layer that gives you persistent registry, distributed state, and security features (commissioning, ACLs) so devices and agents on different networks can find and call each other through a single namespace. If you're new to Device Connect, start with the device-to-device Learning Path first.

learning_objectives:
    - Understand what the Device Connect server adds on top of the edge SDK and when you'd reach for it
    - Provision a hosted tenant on the Device Connect portal and download per-device NATS credentials
    - Commission two simulated devices against your tenant using the credentials the portal issues
    - Discover and invoke commissioned devices from a Python client using `device-connect-agent-tools`
    - Connect a Strands AI agent to the same tenant

prerequisites:
    - Complete the [Device-to-device Learning Path](/learning-paths/embedded-and-microcontrollers/device-connect-d2d/) to understand Device Connect edge SDK basics
    - An account on the [Device Connect portal](https://portal.deviceconnect.dev/)
    - Basic familiarity with Python and the command line

author:
    - Kavya Sri Chennoju
    - Annie Tallund

### Tags
skilllevels: Introductory
subjects: Libraries
armips:
    - Cortex-A
    - Neoverse
operatingsystems:
    - Linux
    - macOS
tools_software_languages:
    - Python
    - Docker

further_reading:
    - resource:
        title: Device Connect
        link: https://deviceconnect.dev/
        type: website
    - resource:
        title: device-connect-server package
        link: https://github.com/arm/device-connect/tree/main/packages/device-connect-server
        type: documentation
    - resource:
        title: device-to-device Learning Path
        link: /learning-paths/embedded-and-microcontrollers/device-connect-d2d/
        type: website
    - resource:
        title: NATS documentation
        link: https://docs.nats.io/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

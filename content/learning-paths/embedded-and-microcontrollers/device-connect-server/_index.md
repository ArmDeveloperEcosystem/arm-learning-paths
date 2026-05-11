---
title: Connect Devices and AI agents through Device Connect Server

draft: true
cascade:
    draft: true

minutes_to_complete: 30

who_is_this_for: This is a follow-on topic for developers who have a working Device Connect mesh and want to add a server layer on top. The server gives you a persistent device registry, distributed state, and security primitives (commissioning, ACLs) so you can operate a multi-network fleet from one place.

learning_objectives:
    - Understand what the Device Connect server adds on top of the edge SDK and when you'd reach for it
    - Provision a hosted tenant on the Device Connect portal and download per-device NATS credentials
    - Commission two simulated devices against your tenant using the credentials the portal issues
    - Discover and invoke commissioned devices from a Python client using `device-connect-agent-tools`
    - Connect a Strands AI agent to the same tenant

prerequisites:
    - Familiarity with the Device Connect edge SDK (the [device-to-device Learning Path](/learning-paths/embedded-and-microcontrollers/device-connect-d2d/) is a good starting point)
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

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

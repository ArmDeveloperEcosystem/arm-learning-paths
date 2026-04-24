---
title: Connect AI agents to edge devices using Device Connect and Strands
description: Learn how to connect AI agents to Arm-based edge devices using Device Connect for structured device access and Strands for agent orchestration, with examples for both simulated and physical robots.
minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers who want to connect AI agents to edge devices. You'll use Device Connect, Arm's platform for structured device access, and Strands, AWS's open-source agent SDK. The examples cover both physical and simulated devices.


learning_objectives:
    - Understand how Device Connect and Strands work together to give AI agents structured access to Arm-based edge devices
    - Set up a Python environment with the Device Connect SDK and agent tools installed from source
    - Start a simulated robot that registers itself on the local network and is discovered automatically by an agent
    - Discover and invoke the robot using the Device Connect agent tools and the robot_mesh Strands tool

prerequisites:
    - A development machine with git installed
    - Basic familiarity with command-line tools
    - (Optional) A Raspberry Pi for testing a full device-to-device (D2D) setup

author: 
    - Annie Tallund
    - Kavya Sri Chennoju



### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A
    - Neoverse
operatingsystems:
    - Linux
    - macOS
tools_software_languages:
    - Python
    - Docker
    - strands-agents

further_reading:
    - resource:
        title: Strands Agents SDK documentation
        link: https://strandsagents.com/
        type: website
    - resource:
        title: Strands robots repository
        link: https://github.com/strands-labs/robots
        type: website
    - resource:
        title: device-connect-agent-tools on PyPI
        link: https://pypi.org/project/device-connect-agent-tools
        type: website
    - resource:
        title: device-connect-sdk on PyPI
        link: https://pypi.org/project/device-connect-sdk
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

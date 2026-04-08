---
title: Identify code hotspots using Arm Performix through the Arm MCP Server
description: Learn how to use an AI agent and the Performix tool through the Arm MCP Server to run the Code Hotspots recipe on a C++ application, interpret flame graph results, and apply targeted optimizations on Arm Neoverse.

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for developers who want to use AI-powered tools to automate performance profiling and optimization of C++ applications on Arm Neoverse servers.

learning_objectives:
  - Describe how the Arm Performix tool in the Arm MCP Server enables AI-driven profiling workflows
  - Configure a GitHub Copilot prompt file to run the Code Hotspots recipe on a remote Arm target
  - Use an AI agent to interpret flame graph results and identify the hottest functions in a C++ application
  - Apply AI-suggested optimizations to reduce application runtime on Arm Neoverse

prerequisites:
    - Completion of the [Automate x86-to-Arm application migration using Arm MCP Server](/learning-paths/servers-and-cloud-computing/arm-mcp-server/) Learning Path, or equivalent familiarity with configuring the Arm MCP Server in an AI coding assistant
    - Access to an Arm-based cloud instance running Linux, such as an AWS Graviton3 instance
    - Access to Arm Performix configured with the remote Arm target. See the [Arm Performix install guide](/install-guides/performix/) for setup instructions
    - Basic understanding of C++
author: Pareena Verma

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - Arm Performix
    - MCP
    - C++
    - GitHub Copilot
operatingsystems:
    - Linux



further_reading:
    - resource:
        title: Find code hotspots with Arm Performix
        link: /learning-paths/servers-and-cloud-computing/cpu_hotspot_performix/
        type: learning-path
    - resource:
        title: Automate x86-to-Arm application migration using Arm MCP Server
        link: /learning-paths/servers-and-cloud-computing/arm-mcp-server/
        type: learning-path
    - resource:
        title: Arm MCP Server GitHub Repository
        link: https://github.com/arm/mcp
        type: website
    - resource:
        title: Arm Performix
        link: https://developer.arm.com/servers-and-cloud-computing/arm-performix
        type: website
    - resource:
        title: Optimize application performance using Arm Performix CPU microarchitecture analysis
        link: /learning-paths/servers-and-cloud-computing/performix-microarchitecture/
        type: learning-path



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

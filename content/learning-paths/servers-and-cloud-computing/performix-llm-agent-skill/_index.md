---
title: Profile and optimize Arm workloads with the arm-performix agent skill
description: Learn how to install and use the arm-performix skill so an AI coding assistant can drive Arm Performix for you to find code hotspots, diagnose pipeline stalls, and propose measured optimizations on Arm Neoverse.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers who use an AI coding assistant (such as GitHub Copilot in VS Code) and want it to drive Arm Performix on their behalf to profile and optimise software performance through the arm-performix skill, without having to memorize the apx CLI themselves.

learning_objectives:
    - Install and enable the arm-performix skill in your AI assistant
    - Trigger the skill with phrasing that activates the profiling workflow
    - Provide the context the skill needs to profile (target, binary, workload)
    - Read the analysis report the skill produces and drive the optimization loop

prerequisites:
    - An AI assistant that supports skills, such as GitHub Copilot in VS Code
    - An Arm Neoverse-based instance reachable from the assistant's environment
    - Arm Performix (the `apx` CLI) installed, or the Arm MCP Server configured

author:
    - Henry Wang

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - Arm Performix
    - GitHub Copilot
    - MCP
operatingsystems:
    - Linux
    - macOS
    - Windows

further_reading:
    - resource:
        title: Arm Performix product page
        link: https://developer.arm.com/Tools%20and%20Software/Arm%20Performix
        type: website
    - resource:
        title: Find Code Hotspots with Arm Performix
        link: /learning-paths/servers-and-cloud-computing/cpu_hotspot_performix/
        type: learning-path
    - resource:
        title: Optimize application performance using Arm Performix CPU microarchitecture analysis
        link: /learning-paths/servers-and-cloud-computing/performix-microarchitecture/
        type: learning-path
    - resource:
        title: Optimize memory access behavior using Arm Performix and the Arm MCP Server
        link: /learning-paths/servers-and-cloud-computing/performix-memory-access/
        type: learning-path
    - resource:
        title: Migrate applications to Arm servers using migrate-ease
        link: /learning-paths/servers-and-cloud-computing/migrate-ease/
        type: learning-path
    - resource:
        title: Automate x86-to-Arm application migration using Arm MCP Server
        link: /learning-paths/servers-and-cloud-computing/arm-mcp-server/
        type: learning-path
    - resource:
        title: Get started with Servers and Cloud Computing
        link: /learning-paths/servers-and-cloud-computing/intro/
        type: learning-path
    - resource:
        title: Learn about Arm Neoverse processors
        link: https://www.arm.com/products/silicon-ip-cpu/neoverse
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

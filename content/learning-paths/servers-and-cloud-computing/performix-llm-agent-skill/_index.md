---
title: Profile and improve Arm workloads with the arm-performix agent skill

draft: true
cascade:
    draft: true
    
description: Learn how to install and use the arm-performix skill so an AI coding assistant can drive Arm Performix, find code hotspots, diagnose pipeline stalls, and propose measured improvements on Arm Neoverse.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers who use an AI coding assistant with Agent Skills support, such as GitHub Copilot in VS Code or Claude Code, and want the arm-performix skill to drive Arm Performix profiling workflows without memorizing the `apx` command-line interface.

learning_objectives:
    - Install and enable the arm-performix skill in your AI assistant
    - Trigger the skill with phrasing that activates the profiling workflow
    - Provide the context the skill needs to profile (target, binary, workload)
    - Read the analysis report the skill produces and drive the improvement loop

prerequisites:
    - An AI assistant with Agent Skills support enabled, such as GitHub Copilot in VS Code or Claude Code
    - An Arm Neoverse-based Linux instance reachable from the assistant's environment
    - Arm Performix installed with the `apx` command-line interface available on the host `PATH`, or the Arm Model Context Protocol (MCP) Server configured for supported launch-mode profiling recipes

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
        link: https://developer.arm.com/servers-and-cloud-computing/arm-performix
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



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

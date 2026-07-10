---
title: Use Arm Performix Agentic Dynamic Insights from VS Code with Codex

description: This Learning Path shows how to configure the Arm Performix MCP server with the Codex extension in Visual Studio Code, then generate AI Insights for an existing Arm Performix profiling run.

minutes_to_complete: 20

who_is_this_for: This Learning Path is for software developers and performance engineers who want to optimize applications on Arm-based servers using Arm Performix.

learning_objectives:
    - Configure the Arm Performix MCP server in the Codex extension for VS Code. 
    - Check that the assistant can see Arm Performix recipes and runs. 
    - Ask the assistant to list available Arm Performix runs. 
    - Generate AI Insights for a supported code hotspots run. 
    - Use the result to decide where to inspect or optimize next. 

prerequisites:
    - Arm Performix version 2026.2.5 or later installed. Refer to the [Install Guide](https://learn.arm.com/install-guides/performix/) for instructions. 
    - Visual Studio Code installed with the Codex extension. 
    - Permission to use your organization-approved AI assistant with profile data, symbols, source excerpts, disassembly excerpts, and performance metrics.
    - For remote Linux targets, configure key-based SSH access before using the Arm Performix MCP server. 
    - If you connect to your target as a non-root user, some recipes or target configurations might require passwordless sudo. 
    - Make sure your SSH known_hosts file contains the target host key. 
    - If your target configuration uses jump nodes, make sure known_hosts also contains the host key for each jump node. 

author: 
    - Julie Gaskin

### Tags
skilllevels: Beginner
subjects: Performance and Architecture
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Arm Performix
    - C++
    - GCC

further_reading:
    - resource:
        title: Install guide
        link: https://learn.arm.com/install-guides/performix
        type: documentation
    - resource:
        title: User guide
        link: https://developer.arm.com/documentation/110163/latest/
        type: documentation
    - resource:
        title: Code hotspots learning path
        link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/cpu_hotspot_performix
        type: learning path
    - resource:
        title: CPU microarchitecture learning path
        link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/performix-microarchitecture
        type: learning path
    - resource:
        title: Migrating applications to Arm servers
        link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/migration/
        type: learning path

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

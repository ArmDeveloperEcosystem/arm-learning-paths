---
title: Get started with Arm Performix on Arm-based Servers

draft: true
cascade:
  draft: true

description: This Learning Path guides you through using Arm Performix to analyze and optimize applications running on Arm-based servers. You'll learn how to use recipes and runs for performance analysis, profile workloads, and optimize code using Arm NEON intrinsics.

minutes_to_complete: 120

who_is_this_for: This Learning Path is for software developers and performance engineers who want to optimize applications on Arm-based servers using Arm Performix.

learning_objectives:
    - How to download and install Arm Performix for your target platform.
    - Understand how Arm Performix uses recipes and runs to guide performance analysis on Arm-based systems.
    - Profile a C++ workload with the Code Hotspots recipe to identify the functions consuming the most CPU time.
    - Use the CPU Microarchitecture recipe to determine whether a workload is limited by frontend, backend, memory, or other CPU pipeline effects.
    - Interpret Instruction Mix results to identify scalar code patterns and missed SIMD optimization opportunities.
    - Optimize the workload using Arm NEON intrinsics to improve instruction efficiency.
    - Compare Performix runs before and after optimization to validate changes in runtime, instruction mix, and bottleneck behavior.

prerequisites:
    - SSH access to an Arm-based target system
    - Arm Performix installed
    - C++ compiler (e.g., GCC)

author: 
    - Julie Gaskin

### Tags
skilllevels: Introductory
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
        title: Find Code hotspots with Arm Performix
        link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/cpu_hotspot_performix
        type: learning path
    - resource:
        title: Optimize application performance using Arm Performix CPU microarchitecture analysis
        link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/performix-microarchitecture
        type: learning path
    - resource:
        title: Generate Arm Performix AI insights in Visual Studio Code with Codex
        link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/performix-agentic-dynamic-insights-codex/
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

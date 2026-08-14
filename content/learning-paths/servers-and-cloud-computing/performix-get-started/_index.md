---
title: Optimize a sample C++ application on an Arm-based server with Arm Performix

description: Profile and optimize a C++ application on Arm-based servers using Arm Performix recipes, CPU microarchitecture analysis, and NEON intrinsics.

minutes_to_complete: 120

who_is_this_for: This Learning Path is for software developers and performance engineers who want to optimize applications on Arm-based servers using Arm Performix.

learning_objectives:
    - Install Arm Performix and use its recipes to guide performance analysis on Arm-based systems
    - Profile a C++ application with the Code Hotspots recipe to identify functions consuming the most CPU time
    - Use CPU Microarchitecture and Instruction Mix recipes to pinpoint pipeline bottlenecks and missed SIMD opportunities
    - Optimize the application with Arm NEON intrinsics and compare Performix runs to validate changes in runtime and bottleneck behavior

prerequisites:
    - SSH access to an Arm Linux server as the target
    - Arm Performix installed on your local machine. For installation instructions, see the [Arm Performix install guide](/install-guides/performix).
    - A C++ compiler such as GCC or Clang installed on the target Linux server

author: 
    - Julie Gaskin

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

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
        title: Install Arm Performix
        link: https://learn.arm.com/install-guides/performix
        type: documentation
    - resource:
        title: User guide
        link: https://developer.arm.com/documentation/110163/latest/
        type: documentation
    - resource:
        title: Find Code hotspots with Arm Performix
        link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/cpu_hotspot_performix
        type: website
    - resource:
        title: Optimize application performance using Arm Performix CPU microarchitecture analysis
        link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/performix-microarchitecture
        type: website
    - resource:
        title: Generate Arm Performix AI insights in Visual Studio Code with Codex
        link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/performix-agentic-dynamic-insights-codex/
        type: website
        
### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

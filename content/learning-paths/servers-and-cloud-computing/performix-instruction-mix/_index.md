---
title: Profile GPT-2 instruction mix with Arm Performix

description: Learn how to profile GPT-2 inference on Arm Neoverse with the Arm Performix Instruction Mix recipe, identify scalar versus vector execution patterns, and improve throughput with NEON, SVE, and KleidiAI kernels.

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for developers who want to get started using the Arm Performix Instruction Mix recipe through a practical example.

learning_objectives: 
    - Understand how the Instruction Mix recipe combines static disassembly with runtime sampling to show execution behavior
    - Build and run the GPT-2 inference example on an Arm Linux server
    - Identify why matrix multiplication dominates runtime and how vectorization changes the instruction mix
    - Compare throughput and instruction mix across scalar, NEON, SVE, and KleidiAI implementations

prerequisites:
    - Access to Arm Performix configured with a remote Arm Linux target. For setup, see the [Arm Performix install guide](/install-guides/performix/).
    - Basic understanding of C++ and compiler optimization
    - Basic understanding of matrix multiplication
    - Basic understanding of writing SIMD code with Neon or SVE

author:
    - Kieran Hejmadi
    - Oliver Grainge

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - Arm Performix
    - C
    - LLM
    - NEON
    - SVE
operatingsystems:
    - Linux
further_reading:
    - resource:
        title: Arm Performix User Guide
        link: https://developer.arm.com/documentation/110163/latest
        type: documentation
    - resource:
        title: Find code hotspots with Arm Performix
        link: /learning-paths/servers-and-cloud-computing/cpu_hotspot_performix/
        type: learning-path
    - resource:
        title: Identify code hotspots using Arm Performix through the Arm MCP Server
        link: /learning-paths/servers-and-cloud-computing/performix-mcp-agent/
        type: learning-path
    - resource:
        title: Arm MCP Server GitHub Repository
        link: https://github.com/arm/mcp
        type: website
    - resource:
        title: GPT-2 Example repository
        link: https://github.com/arm-education/GPT-2-Example
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
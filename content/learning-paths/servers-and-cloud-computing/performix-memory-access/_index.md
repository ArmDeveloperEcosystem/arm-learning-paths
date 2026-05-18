---
title: Get started with memory access analysis with Arm Performix and the Arm MCP Server

description: Learn how to profile memory access behavior in a C++ particle simulation on Arm Linux using the Arm Performix Memory Access recipe through the Arm MCP Server.

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for C++ developers who want to use Arm Performix and the Arm MCP Server to diagnose cache and translation behavior in applications running on Arm Neoverse systems.

learning_objectives:
  - Explain how L1 cache hits, TLB misses, and page walks affect C++ application runtime.
  - Build and visualize the orbiting galaxies example on an Arm Linux target.
  - Inspect and optimize particle data structure using insights from the memory access recipe
  - Use the Arm MCP Server in combination with performix for an agentic solution.

prerequisites:
  - Access to an Arm Neoverse-based Linux metal instance.
  - Basic understanding of memory hierarchy within a CPU
  - Basic C++ development experience.
  - Familiarity with the Linux command line.

author: Kieran Hejmadi

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
  - Neoverse
tools_software_languages:
  - Arm Performix
  - MCP
  - C++
  - CMake
  - Python
  - Linux perf
operatingsystems:
  - Linux

further_reading:
  - resource:
      title: Identify code hotspots using Arm Performix through the Arm MCP Server
      link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/performix-mcp-agent/
      type: learning-path
  - resource:
      title: Find Code Hotspots with Arm Performix
      link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/cpu_hotspot_performix/
      type: learning-path
  - resource:
      title: Optimize application performance using Arm Performix CPU microarchitecture analysis
      link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/performix-microarchitecture/
      type: learning-path
  - resource:
      title: Automate x86-to-Arm application migration using Arm MCP Server
      link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/arm-mcp-server/
      type: learning-path
  - resource:
      title: Arm Performix
      link: https://developer.arm.com/servers-and-cloud-computing/arm-performix
      type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

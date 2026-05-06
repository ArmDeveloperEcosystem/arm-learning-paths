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

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:58Z'
  generator: template
  source_hash: 0599665da13e9e1a8b017b0dac87c63f323ef769b1a5be62a60a32a36bc82696
  summary: >-
    Learn how to use an AI agent and the Performix tool through the Arm MCP Server to run the
    Code Hotspots recipe on a C++ application, interpret flame graph results, and apply targeted
    optimizations on Arm Neoverse. It is designed for developers who want to use AI-powered tools
    to automate performance profiling and optimization of C++ applications on Arm Neoverse servers.
    By the end, you will be able to describe how the Arm Performix tool in the Arm MCP Server
    enables AI-driven profiling workflows, configure a GitHub Copilot prompt file to run the Code
    Hotspots recipe on a remote Arm target, and use an AI agent to interpret flame graph results
    and identify the hottest functions in a C++ application. It focuses on tools and technologies
    such as Arm Performix, MCP, C++, and GitHub Copilot, Linux environments, and Arm platforms
    including Neoverse. The main steps cover Understand AI-driven profiling with Arm Performix
    MCP, Build the Mandelbrot example on Arm Neoverse, Run Code Hotspots with an AI agent, and
    Optimize code with AI-driven profiling feedback.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will describe how the Arm Performix tool in the Arm MCP Server enables AI-driven profiling
      workflows, configure a GitHub Copilot prompt file to run the Code Hotspots recipe on a remote
      Arm target, and use an AI agent to interpret flame graph results and identify the hottest
      functions in a C++ application. Learn how to use an AI agent and the Performix tool through
      the Arm MCP Server to run the Code Hotspots recipe on a C++ application, interpret flame
      graph results, and apply targeted optimizations on Arm Neoverse.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for developers who want to use AI-powered tools to automate performance
      profiling and optimization of C++ applications on Arm Neoverse servers.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: Completion of the [Automate x86-to-Arm
      application migration using Arm MCP Server](/learning-paths/servers-and-cloud-computing/arm-mcp-server/)
      Learning Path, or equivalent familiarity with configuring the Arm MCP Server in an AI coding
      assistant; Access to an Arm-based cloud instance running Linux, such as an AWS Graviton3
      instance; Access to Arm Performix configured with the remote Arm target. See the [Arm Performix
      install guide](/install-guides/performix/) for setup instructions; Basic understanding of
      C++.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Arm Performix, MCP, C++, and GitHub Copilot, Linux
      environments, and Arm platforms such as Neoverse.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Understand AI-driven profiling with Arm Performix
      MCP, Build the Mandelbrot example on Arm Neoverse, Run Code Hotspots with an AI agent, and
      Optimize code with AI-driven profiling feedback.
# END generated_summary_faq

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


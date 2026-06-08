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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:46:30Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0599665da13e9e1a8b017b0dac87c63f323ef769b1a5be62a60a32a36bc82696
  summary_generated_at: '2026-06-02T04:46:21Z'
  summary_source_hash: 0599665da13e9e1a8b017b0dac87c63f323ef769b1a5be62a60a32a36bc82696
  faq_generated_at: '2026-06-03T01:46:30Z'
  faq_source_hash: 0599665da13e9e1a8b017b0dac87c63f323ef769b1a5be62a60a32a36bc82696
  summary: >-
    Use an AI coding assistant with the Arm MCP Server to run Arm Performix Code Hotspots on a
    C++ application and act on the results on Arm Neoverse. You configure a GitHub Copilot prompt
    file to launch profiling on a remote Linux-based Arm instance, interpret flame graph output,
    and apply agent-suggested changes to the Mandelbrot example, such as a squared-magnitude check,
    raw double arithmetic instead of std::complex, and compiling with -O3. Prerequisites include
    familiarity with configuring the Arm MCP Server in an AI assistant (or completion of the related
    Learning Path), access to an Arm-based cloud instance (for example, AWS Graviton3) with Arm
    Performix set up for the target, and basic C++ knowledge.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      You need familiarity with configuring the Arm MCP Server in an AI coding assistant (or completion
      of the referenced Learning Path), access to an Arm-based Linux cloud instance such as an
      AWS Graviton3 instance, access to Arm Performix configured with the remote Arm target, and
      a basic understanding of C++.
  - question: Do I have to use Visual Studio Code and GitHub Copilot?
    answer: >-
      The steps use Visual Studio Code with GitHub Copilot as the example AI assistant. Equivalent
      configurations for other AI agents (Kiro and OpenAI Codex) are referenced at the end of
      the section.
  - question: Which prompt file should I use to run the Code Hotspots recipe?
    answer: >-
      Use the Arm MCP arm-hotspots-optimization prompt file with GitHub Copilot. It drives the
      Code Hotspots recipe through the MCP Server, confirms your target details, runs the collection,
      and returns structured profiling results.
  - question: How do I know Arm Performix can reach my remote Arm target?
    answer: >-
      You will build the Mandelbrot C++ application on the remote server and follow a step that
      confirms Performix can access the target. Complete this confirmation before launching the
      Code Hotspots run.
  - question: What result should I expect, and what optimizations are applied?
    answer: >-
      Expect structured profiling output and a flame graph that highlights the hottest functions
      in the Mandelbrot application. The path applies AI-suggested changes: replacing std::abs
      with a squared-magnitude check, replacing std::complex<double> with raw double arithmetic,
      and rebuilding with -O3; the agent can edit the remote source via SSH through the MCP Server.
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


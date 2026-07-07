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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-07T16:22:08Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a81d31a804debf71196a478bdf388c9e58b6dab67a9e881b916f3d0169d9555d
  summary_generated_at: '2026-07-07T16:22:08Z'
  summary_source_hash: a81d31a804debf71196a478bdf388c9e58b6dab67a9e881b916f3d0169d9555d
  faq_generated_at: '2026-07-07T16:22:08Z'
  faq_source_hash: a81d31a804debf71196a478bdf388c9e58b6dab67a9e881b916f3d0169d9555d
  summary: >-
    You'll combine the Arm MCP Server's `apx_recipe_run` tool with an AI agent to drive the complete Code Hotspots workflow to profile on Arm Neoverse. First, you'll build an intentionally unoptimized Mandelbrot
    C++ application on a remote Arm Linux target, then use a GitHub Copilot prompt file to run
    the Performix Code Hotspots recipe. The agent confirms target details, executes collection,
    and returns a flame graph with structured hotspot data to pinpoint the hottest functions.
    Guided by the agent, you'll apply concrete code changes, such as math simplifications and enabling
    a higher optimization level, directly on the server over SSH. Then, you'll re-run the recipe to compare
    results. The end-to-end flow keeps profiling, interpretation, and edits within a single AI-assisted
    loop.
  faqs:
  - question: Which prompt file should I use to run the Code Hotspots recipe?
    answer: >-
      Use the `arm-hotspots-optimization` prompt file from the Arm MCP Server repository with GitHub
      Copilot. It directs the agent to confirm the remote target, run the recipe, and return structured
      profiling results.
  - question: What result should I expect after the profiling run completes?
    answer: >-
      Expect a flame graph and a hotspot summary that highlights the hottest functions in the
      Mandelbrot application. Use these outputs to guide which code changes to apply first.
  - question: Should I compile the Mandelbrot example with optimizations before profiling?
    answer: >-
      No. The single-threaded, unoptimized build is intentional so the hotspot analysis produces
      a clear signal. The agent later proposes enabling -O3 as part of the optimization pass.
  - question: How do I know the agent is targeting the correct machine?
    answer: >-
      The agent explicitly confirms your remote target details before running the Code Hotspots
      recipe. Review this confirmation and proceed only if it matches your intended Arm target.
  - question: What should I check if the Code Hotspots run fails to start?
    answer: >-
      Confirm that Arm Performix is configured with your remote Arm target and that the MCP Server
      can reach it over SSH. Also verify that the Mandelbrot application builds on the target
      system.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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


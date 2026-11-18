---
title: Optimize memory access behavior using the Arm Performix MCP server

description: Learn how to profile and optimize memory access behavior in a C++ particle simulation on Arm Linux using the Arm Performix Memory Access recipe and the Arm Performix MCP server.

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for C++ developers who want to use the Arm Performix MCP server to diagnose cache and address translation behavior in applications running on Arm Neoverse servers.

learning_objectives:
  - Identify how L1 cache hits, TLB misses, and page walks affect C++ application performance.
  - Build and visualize the orbiting galaxies example on an Arm Neoverse server.
  - Inspect and optimize the particle data structure using insights from the memory access recipe.
  - Use the Arm Performix MCP server with an AI coding agent to support an optimization workflow.

prerequisites:
  - Access to an Arm Neoverse bare metal server
  - Basic understanding of memory hierarchy within a CPU
  - Basic C++ development experience
  - Familiarity with the Linux command line
  - An MCP-compatible coding assistant, such as OpenAI Codex with an OpenAI account

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-18T20:22:32Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 83fc875bdd49b5c6e6aa9effaec1eec7a1927175e94714b0cd1712128d80a65c
  summary_generated_at: '2026-11-18T20:22:32Z'
  summary_source_hash: 83fc875bdd49b5c6e6aa9effaec1eec7a1927175e94714b0cd1712128d80a65c
  faq_generated_at: '2026-11-18T20:22:32Z'
  faq_source_hash: 83fc875bdd49b5c6e6aa9effaec1eec7a1927175e94714b0cd1712128d80a65c
  summary: >-
    You'll profile a C++ particle simulation on an Arm Neoverse server and improve its memory
    access behavior. First, you'll review memory hierarchy concepts, build the sample, and run the
    Arm Performix Memory Access recipe. Then, you'll inspect cache and translation results to find
    the hot loop. Finally, you'll refactor the particle layout and compare profiles, with optional
    help from the Performix MCP server.
  faqs:
  - question: Should I build and run the example on the remote Arm server or my local machine?
    answer: >-
      Use the remote Arm server for all build and run steps. Install and configure Arm Performix
      on both your local machine and the remote server.
  - question: How do I confirm the simulation works before profiling?
    answer: >-
      Run the provided visualization after you build the binaries. Check that it runs without
      errors before you start profiling.
  - question: Which source files do I inspect and where do I implement changes?
    answer: >-
      Inspect the baseline particle model in `src/baseline/particle.hpp`. Implement your
      refactor in `src/users_solution`. Update associated function signatures and call sites
      there.
  - question: What should I look for in the Arm Performix results to guide my refactor?
    answer: >-
      Check where samples concentrate, the L1 cache hit rate, and whether TLB walks are
      significant. Focus on `update_positions()` and the fields accessed in that loop, because
      the baseline shows a low L1 hit rate with minimal TLB impact.
  - question: How do I give my coding assistant useful context while using the MCP server?
    answer: >-
      Open the repository's `AGENTS.md` file to give your MCP-compatible coding assistant
      project context during the refactor.
# END generated_summary_faq

author: Kieran Hejmadi

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
  - Neoverse
tools_software_languages:
  - Arm Performix
  - MCP
  - CPP
  - CMake
  - Python
  - perf
operatingsystems:
  - Linux

further_reading:
  - resource:
      title: Identify and optimize code hotspots using the Arm Performix MCP server
      link: /learning-paths/servers-and-cloud-computing/performix-mcp-agent/
      type: learning-path
  - resource:
      title: Find Code Hotspots with Arm Performix
      link: /learning-paths/servers-and-cloud-computing/cpu_hotspot_performix/
      type: learning-path
  - resource:
      title: Optimize application performance using Arm Performix CPU microarchitecture analysis
      link: /learning-paths/servers-and-cloud-computing/performix-microarchitecture/
      type: learning-path
  - resource:
      title: Generate Arm Performix AI insights in Visual Studio Code with Codex
      link: /learning-paths/servers-and-cloud-computing/performix-agentic-dynamic-insights-codex/
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

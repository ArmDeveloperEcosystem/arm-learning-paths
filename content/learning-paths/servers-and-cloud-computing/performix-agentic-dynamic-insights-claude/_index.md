---
title: Generate Arm Performix AI insights in VS Code with Claude Code
    
description: Configure the Arm Performix MCP server for Claude Code in Visual Studio Code and use profile evidence to generate and validate AI insights.

minutes_to_complete: 20

who_is_this_for: This Learning Path is for software developers and performance engineers who want to optimize applications on Arm-based servers using Arm Performix.

learning_objectives:
    - Configure the Arm Performix Model Context Protocol (MCP) server for the Claude Code extension in Visual Studio Code (VS Code).
    - Verify that Claude Code can access Arm Performix recipes, targets, and runs.
    - Create a supported Code Hotspots run.
    - Generate an AI insight and validate its recommendations against profile evidence.

prerequisites:
    - An installation of [Arm Performix version 2026.2.5 or later](/install-guides/performix/)
    - A [configured Arm Linux target](/learning-paths/servers-and-cloud-computing/performix-get-started/add_target/) with a workload to profile
    - VS Code, with the Claude Code extension version 2.1.261 or later installed to add MCP servers through the extension interface
    - Access to Claude Code through a Claude account, or an organization-approved Anthropic API key provided through the `ANTHROPIC_API_KEY` environment variable
    - Permission from your organization to share profile data, symbols, source excerpts, disassembly excerpts, and performance metrics with Claude Code

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-29T21:55:00Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 7a70f6180138effb674943e58d5b815166d33b10dbd39d2d62628d90e72d34f6
  summary_generated_at: '2026-10-29T21:55:00Z'
  summary_source_hash: 7a70f6180138effb674943e58d5b815166d33b10dbd39d2d62628d90e72d34f6
  faq_generated_at: '2026-10-29T21:55:00Z'
  faq_source_hash: 7a70f6180138effb674943e58d5b815166d33b10dbd39d2d62628d90e72d34f6
  summary: >-
    You'll connect Claude Code in VS Code to the Arm Performix MCP server to generate an AI insight. 
    First, you'll choose an MCP configuration method and
    verify access to recipes and runs. You'll then create or select a supported run, request an insight
    with its run ID, and open it in Arm Performix. Finally, you'll identify the run and
    compare the recommendation with profile evidence.
  # faqs:
  # - question: How do I verify that Claude Code can reach the Arm Performix MCP server?
  #   answer: >-
  #     Ask Claude Code to use Arm Performix to list supported Code Hotspots runs, including the
  #     run ID, target, workload, and creation time. If Claude Code returns the run details, you’ve
  #     confirmed that it can access Performix through the MCP server.
  # - question: Which MCP configuration method should I use?
  #   answer: >-
  #     Configure through the extension’s MCP interface, run `claude mcp add`, or edit
  #     `~/.claude.json`. The extension and Claude CLI share the same MCP configuration, so you
  #     only need one method.
  # - question: Where should I configure the Performix MCP server when using VS Code?
  #   answer: >-
  #     Configure the server on the host where Claude Code runs. For a local VS Code session, set
  #     it up on the same machine.
  # - question: What should I prepare before creating a new Code Hotspots run?
  #   answer: >-
  #     Choose a representative workload, specify the executable with an absolute path, and build
  #     with debug symbols when possible. Aim for at least 20 seconds of representative execution
  #     to capture useful samples.
  # - question: How do I open the profiled run in Arm Performix to validate the AI recommendation?
  #   answer: >-
  #     From a terminal where `apx` is on your `PATH`, run `apx run info "<run-id>"`. Use the
  #     returned workload, recipe, target, and timestamps to locate and open the matching run in
  #     the GUI.
# END generated_summary_faq

author:
    - Kieran Hejmadi
    - Julie Gaskin

# New Learning Paths are opted in for the next manual generated summary/FAQ run.
# The generator resets this to false after a successful write.
generate_summary_faq: false

# Optional one-shot controls: set either field to true to regenerate just that
# generated section the next time the summary/FAQ tool runs. The tool resets
# them to false after a successful write.
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
    - Claude Code
    - Model Context Protocol
    - Visual Studio Code

further_reading:
    - resource:
        title: Arm Performix install guide
        link: https://learn.arm.com/install-guides/performix
        type: documentation
    - resource:
        title: Arm Performix User Guide
        link: https://developer.arm.com/documentation/110163/latest/
        type: documentation
    - resource:
        title: Find Code Hotspots with Arm Performix
        link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/cpu_hotspot_performix
        type: documentation
    - resource:
        title: Tune application performance with Arm Performix CPU Microarchitecture
        link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/performix-microarchitecture
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

---
title: Generate Arm Performix AI insights in Visual Studio Code with Codex

description: Configure the Arm Performix MCP server for Codex in Visual Studio Code and use profile evidence to generate and validate AI insights.

minutes_to_complete: 20

who_is_this_for: This Learning Path is for software developers and performance engineers who want to optimize applications on Arm-based servers using Arm Performix.

learning_objectives:
    - Configure the Arm Performix MCP server for the Codex extension in VS Code.
    - Verify that Codex can access Arm Performix recipes, targets, and runs.
    - Create or select a supported Code Hotspots run.
    - Generate an AI insight and validate its recommendations against profile evidence.

prerequisites:
    - Arm Performix version 2026.2.5 or later installed. For installation and target setup instructions, see the [Arm Performix install guide](/install-guides/performix/).
    - Visual Studio Code with the Codex extension installed
    - Access to Codex through ChatGPT sign-in, or an organization-approved OpenAI API key provided through the `OPENAI_API_KEY` environment variable
    - Permission from your organization to share profile data, symbols, source excerpts, disassembly excerpts, and performance metrics with Codex

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-27T15:24:59Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3e21e94826b1e02673c240ad88dc503354a1920397903348316d696cf4e2aa2c
  summary_generated_at: '2026-07-27T15:24:59Z'
  summary_source_hash: 3e21e94826b1e02673c240ad88dc503354a1920397903348316d696cf4e2aa2c
  faq_generated_at: '2026-07-27T15:24:59Z'
  faq_source_hash: 3e21e94826b1e02673c240ad88dc503354a1920397903348316d696cf4e2aa2c
  summary: >-
    You'll learn how to connect Codex in Visual Studio Code to the Arm Performix Model
    Context Protocol (MCP) server, generate an AI insight for a specific Code Hotspots run, and
    validate the result with profile evidence. After configuring the MCP server on your local machine, you’ll select or create a representative Code Hotspots run, request an AI insight by run ID, and evaluate its supporting evidence.
    Then, you'll open the same run in Arm Performix to inspect flame graphs, functions, call
    stacks, source, and disassembly to confirm the recommendation.
  faqs:
  - question: How do I confirm Codex is connected to Arm Performix through MCP?
    answer: >-
      Ask Codex to list Arm Performix recipes, targets, or supported Code Hotspots runs. A successful
      listing confirms the MCP server is configured and reachable.
  - question: Which MCP configuration method should I use, and where should I configure it?
    answer: >-
      You can update Codex extension settings, run the `codex mcp add` command, or
      edit `~/.codex/config.toml`. Configure the MCP on the host where Codex runs; in remote development,
      verify which machine hosts Codex.
  - question: What should I prepare before creating a new Code Hotspots run?
    answer: >-
      Choose a representative workload and specify the executable with an absolute path. Build the workload with debug symbols when possible and aim for at least 20 seconds of activity to collect
      enough samples.
  - question: How do I make sure Codex uses the exact profile I want?
    answer: >-
      Request the AI insight using the run ID. If you don’t know it, ask Codex to list supported
      Code Hotspots runs with IDs, targets, workloads, and creation times. Then, select the correct
      ID.
  - question: What should I check to validate an AI insight against the profile?
    answer: >-
      Open the same run in Arm Performix and inspect the **Flame graph**, **Functions**, **Call Stack**,
      **Source**, and **Disassembly** views. Confirm that the cited functions, call paths, and sample percentages
      match the evidence referenced by the insight.
# END generated_summary_faq

author: 
    - Julie Gaskin

generate_summary_faq: false
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
    - Codex
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

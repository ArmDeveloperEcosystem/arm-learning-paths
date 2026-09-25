---
title: Generate Arm Performix AI insights in Visual Studio Code with Claude Code

description: Configure the Arm Performix MCP server for Claude Code in Visual Studio Code and use profile evidence to generate and validate AI insights.

minutes_to_complete: 20

who_is_this_for: This Learning Path is for software developers and performance engineers who want to optimize applications on Arm-based servers using Arm Performix.

learning_objectives:
    - Configure the Arm Performix MCP server for the Claude Code extension in VS Code.
    - Verify that Claude Code can access Arm Performix recipes, targets, and runs.
    - Create or select a supported Code Hotspots run.
    - Generate an AI insight and validate its recommendations against profile evidence.

prerequisites:
    - Arm Performix version 2026.2.5 or later installed. For installation and target setup instructions, see the [Arm Performix install guide](/install-guides/performix/).
    - Visual Studio Code with the Claude Code extension installed
    - Access to Claude Code through a Claude account, or an organization-approved Anthropic API key provided through the `ANTHROPIC_API_KEY` environment variable
    - Permission from your organization to share profile data, symbols, source excerpts, disassembly excerpts, and performance metrics with Claude Code

author:
    - Kieran Hejmadi
    - Julie Gaskin

# New Learning Paths are opted in for the next manual generated summary/FAQ run.
# The generator resets this to false after a successful write.
generate_summary_faq: true

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

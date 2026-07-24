---
title: Generate Arm Performix AI Insights in VS Code with Codex

draft: true
cascade:
    draft: true

description: Configure the Arm Performix MCP server for Codex in Visual Studio Code and use profile evidence to generate and validate AI Insights.

minutes_to_complete: 20

who_is_this_for: This Learning Path is for software developers and performance engineers who want to optimize applications on Arm-based servers using Arm Performix.

learning_objectives:
    - Configure the Arm Performix MCP server for the Codex extension in VS Code.
    - Verify that Codex can access Arm Performix recipes, targets, and runs.
    - Create or select a supported Code Hotspots run.
    - Generate an AI Insight and validate its recommendations against profile evidence.

prerequisites:
    - Arm Performix version 2026.2.5 or later installed. See the [Arm Performix install guide](/install-guides/performix/) for installation and target setup instructions.
    - Visual Studio Code with the Codex extension installed.
    - Access to Codex through ChatGPT sign-in, or an organization-approved OpenAI API key provided through the `OPENAI_API_KEY` environment variable.
    - Permission from your organization to share profile data, symbols, source excerpts, disassembly excerpts, and performance metrics with Codex.

author: 
    - Julie Gaskin

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

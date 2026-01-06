---
title: Automate x86-to-Arm application migration using Arm MCP Server

minutes_to_complete: 20

who_is_this_for: This is an advanced topic for developers who want to use AI-powered tools to migrate x86 applications to Arm-based cloud instances.

learning_objectives:
  - Explain how the Arm MCP Server enables AI-driven x86-to-Arm migration workflows
  - Use AI-assisted checks to inspect Docker images for Arm compatibility
  - Automate the migration of x86-specific C++ code to Arm using structured prompt files
  - Validate and run a migrated Dockerized C++ application on Arm-based systems
  - Configure AI agents to reuse the same migration workflow across different tools

prerequisites:
    - An AI-powered IDE such as VS Code with agentic tools like GitHub Copilot, Claude Code, Cursor, or similar
    - Basic familiarity with Docker and C/C++ development
    - Access to an Arm-based cloud instance or local Arm computer for testing

author: Joe Stech

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - MCP
    - Docker
    - CPP
    - GitHub Copilot
operatingsystems:
    - Linux



further_reading:
    - resource:
        title: Arm MCP Server GitHub Repository
        link: https://github.com/arm/mcp
        type: website
    - resource:
        title: Model Context Protocol Documentation
        link: https://modelcontextprotocol.io/
        type: documentation
    - resource:
        title: Install Docker
        link: /install-guides/docker/
        type: install-guide
    - resource:
        title: Migrate applications to Arm servers
        link: /learning-paths/servers-and-cloud-computing/migration/
        type: learning-path
    - resource:
        title: Learn about Arm Neoverse processors
        link: /learning-paths/servers-and-cloud-computing/intro/
        type: learning-path



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

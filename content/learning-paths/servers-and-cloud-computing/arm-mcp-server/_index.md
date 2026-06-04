---
title: Automate x86-to-Arm application migration using Arm MCP Server
description: Learn how to automate x86-to-Arm application migration using the Arm MCP Server, with AI-assisted compatibility checks, C++ code refactoring, and Docker-based validation on Arm cloud platforms.

minutes_to_complete: 20

who_is_this_for: This is an advanced topic for developers who want to use AI-powered tools to migrate x86 applications to Arm-based cloud instances.

learning_objectives:
  - Explain how the Arm MCP Server enables AI-driven x86-to-Arm migration workflows
  - Use AI-assisted checks to inspect Docker images for Arm compatibility
  - Set up and use the Arm Cloud Migration Agent in GitHub Copilot to automate x86-to-Arm code migration
  - Validate and run a migrated C++ application using Docker on Arm-based systems
  - Configure other AI agents to reuse the same migration workflow across different tools

prerequisites:
    - An AI-powered IDE such as VS Code, Copilot in VS Code, Kiro (IDE or CLI) or Codex
    - Basic familiarity with Docker and C/C++ development
    - Access to an Arm-based cloud instance or local Arm computer running Linux or macOS

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:18:38Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b870ac5160d35ddb51955ca8379493e172787ced8125cde8ae79f7700e653a87
  summary_generated_at: '2026-06-02T03:06:30Z'
  summary_source_hash: b870ac5160d35ddb51955ca8379493e172787ced8125cde8ae79f7700e653a87
  faq_generated_at: '2026-06-03T00:18:38Z'
  faq_source_hash: b870ac5160d35ddb51955ca8379493e172787ced8125cde8ae79f7700e653a87
  summary: >-
    This Learning Path guides you through automating x86-to-Arm application migration using the
    Arm MCP Server. You will connect an AI-powered IDE or agent to the MCP Server to run AI-assisted
    checks on Docker images for arm64 support, refactor C++ (including SIMD intrinsics cases)
    with the Arm Cloud Migration Agent in GitHub Copilot, and validate the migrated application
    in Docker on Arm-based systems. You also configure the same migration workflow in other agentic
    tools. Prerequisites include an AI-enabled IDE (for example VS Code with Copilot, Kiro, or
    Codex), basic Docker and C/C++ knowledge, and access to an Arm-based Linux or macOS system.
    Estimated time to complete is about 20 minutes.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      Have an AI-powered IDE (for example, VS Code with GitHub Copilot, Kiro, or Codex), basic
      familiarity with Docker and C/C++ development, and access to an Arm-based cloud instance
      or a local Arm machine running Linux or macOS.
  - question: How do I check if a Docker base image supports arm64 during migration?
    answer: >-
      Use natural language prompts with the Arm MCP Server to ask about arm64 compatibility. This
      avoids manual manifest inspection and returns an AI-assisted compatibility assessment you
      can act on.
  - question: I’m not using GitHub Copilot—how do I follow the migration workflow?
    answer: >-
      Skip to the section on configuring other agentic systems and set up persistent instructions
      (such as steering documents or prompt files) for your tool. The goal is to let your AI assistant
      use the Arm MCP Server to execute the same multi-step migration workflow.
  - question: What should I do if my C++ code uses x86 SIMD intrinsics?
    answer: >-
      Use the Arm Cloud Migration Agent in GitHub Copilot to guide refactoring from SSE/AVX/AVX2
      intrinsics to Arm Neon or SVE equivalents. Follow the agent’s structured steps to address
      architecture-specific vector code.
  - question: How do I validate the migrated C++ application on Arm?
    answer: >-
      Run and validate the application in Docker on an Arm-based system as outlined in the path.
      You should be able to execute the container on Arm Linux or macOS and confirm the application
      runs as expected.
# END generated_summary_faq

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


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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-26T17:27:42Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b870ac5160d35ddb51955ca8379493e172787ced8125cde8ae79f7700e653a87
  summary_generated_at: '2026-06-26T17:27:42Z'
  summary_source_hash: b870ac5160d35ddb51955ca8379493e172787ced8125cde8ae79f7700e653a87
  faq_generated_at: '2026-06-26T17:27:42Z'
  faq_source_hash: b870ac5160d35ddb51955ca8379493e172787ced8125cde8ae79f7700e653a87
  summary: >-
    You'll connect an AI coding assistant to the Arm MCP Server and use its
    Model Context Protocol capabilities to drive an x86-to-Arm migration workflow. First, you'll configure the Arm Cloud
    Migration Agent in GitHub Copilot to identify and refactor SIMD intrinsics from SSE/AVX to
    Arm Neon or SVE. Then, you'll review AI-generated changes and validate outcomes by building and running
    the migrated C++ application in Docker on Arm-based systems. You'll also learn how to replicate
    the same multi-step workflow in other agentic tools using persistent, structured instructions.
  faqs:
  - question: How do I know if a Docker base image is compatible with Arm?
    answer: >-
      Ask the Arm MCP Server in natural language to check the image’s supported architectures.
      Expect a response indicating whether `arm64` is included; if it is missing, select an Arm-compatible
      image before proceeding.
  - question: What confirms that my AI assistant is connected to the Arm MCP Server?
    answer: >-
      Prompts about Arm migration tasks return structured, tool-backed results instead of generic
      text. For example, image compatibility queries or code analysis requests yield specific
      findings sourced through MCP.
  - question: How should I handle x86 SIMD intrinsics during migration?
    answer: >-
      Use the Arm Cloud Migration Agent to locate SSE/AVX usage and propose Neon or SVE equivalents.
      Review the suggested refactoring, update the code, and compile to verify that the changes
      build cleanly.
  - question: What should I check before running the migrated app on an Arm system?
    answer: >-
      Confirm the container base image supports `arm64` and that dependencies are available for
      Arm. Rebuild the container and ensure the application starts without x86-specific instruction
      errors.
  - question: How can I reuse this workflow in other AI tools?
    answer: >-
      Create persistent instructions (such as steering documents or prompt files) that direct
      the agent to use the Arm MCP Server and follow the same migration steps. Mirror the Copilot
      setup so the agent can perform checks, refactoring, and validation consistently.
# END generated_summary_faq

author: Joe Stech

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

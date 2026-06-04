---
title: Deploy an MCP Server on Raspberry Pi 5 for AI Agent Interaction using OpenAI SDK
description: Learn how to deploy a Model Context Protocol server on Raspberry Pi 5 and use the OpenAI Agent SDK to create AI agents with custom tools for local inference.

minutes_to_complete: 30

who_is_this_for: This Learning Path is for LLM and IoT developers who want to run and interact with AI agents on edge devices like the Raspberry Pi 5. You'll learn how to deploy a lightweight Model Context Protocol (MCP) server and use the OpenAI Agent SDK to create and register tools for intelligent local inference.

learning_objectives: 
    - Deploy a lightweight Model Context Protocol (MCP) server on Raspberry Pi 5 for local AI agent execution.
    - Use the OpenAI Agent SDK to interact with a local AI agent.
    - Design and register custom tools for the agent tasks.
    - Learn about uv - a fast, efficient Python package manager for efficient local deployment.

prerequisites:
    - A [Raspberry Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/) with a Linux-based OS installed.
    - Familiarity with Python programming and prompt engineering techniques.
    - Basic understanding of Large Language Models (LLMs) and how they are used in local inference.
    - Understanding of AI agents and the OpenAI Agent SDK (or similar frameworks).

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:46:28Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 39d489081bfa22125a4046c17d5c00a32c0d7b298cba7b6a12373cf3cf6bac04
  summary_generated_at: '2026-06-01T21:11:51Z'
  summary_source_hash: 39d489081bfa22125a4046c17d5c00a32c0d7b298cba7b6a12373cf3cf6bac04
  faq_generated_at: '2026-06-02T21:46:28Z'
  faq_source_hash: 39d489081bfa22125a4046c17d5c00a32c0d7b298cba7b6a12373cf3cf6bac04
  summary: >-
    This Learning Path shows how to deploy a lightweight Model Context Protocol (MCP) server on
    a Raspberry Pi 5 and connect it to an AI agent built with the OpenAI Agent SDK. You will use
    uv, a fast Python package manager, to bootstrap a FastMCP server that reads CPU temperature
    and searches weather data, and expose it to the internet with ngrok. On a Linux Arm development
    machine, you will create the agent, register custom tools, and point it at the Pi’s MCP endpoint
    for local inference. Prerequisites include a Raspberry Pi 5 with a Linux-based OS, familiarity
    with Python and prompt engineering, and a basic understanding of LLMs and AI agents. Estimated
    time to complete is about 30 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Raspberry Pi 5 with a Linux-based OS installed, familiarity with Python and prompt
      engineering, a basic understanding of LLMs and local inference, and an understanding of
      AI agents and the OpenAI Agent SDK (or similar frameworks).
  - question: Which machine hosts the MCP server and where does the agent run?
    answer: >-
      The MCP server runs on the Raspberry Pi 5 (Raspberry Pi OS 64-bit). The AI agent is set
      up on your development machine, with the commands tested on a Linux Arm system, and it connects
      to the MCP server on the Pi.
  - question: How do I install uv and what project files should I see?
    answer: >-
      Install uv by running: curl -LsSf https://astral.sh/uv/install.sh | sh. When you initialize
      a project with uv init, it creates a .venv/ directory and a pyproject.toml file for the
      project.
  - question: How do I expose the MCP server running on my Raspberry Pi to the internet?
    answer: >-
      Use ngrok to create an HTTPS tunnel to your local MCP server. The steps show how to expose
      the server so it can be reached remotely.
  - question: What result should I expect to confirm the setup is working?
    answer: >-
      On the Raspberry Pi, the MCP server should be able to read CPU temperature and search weather
      data. On your development machine, the agent should successfully connect to the Pi’s MCP
      server, and uv should have created the .venv and pyproject.toml in your agent project.
# END generated_summary_faq

author: Andrew Choi

skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A
tools_software_languages:
    - Python
    - AI
    - Raspberry Pi
    - MCP

operatingsystems:
    - Linux
### Cross-platform metadata only
shared_path: true
shared_between:
    - embedded-and-microcontrollers

further_reading:
    - resource:
        title: fastmcp
        link: https://github.com/jlowin/fastmcp
        type: documentation
    - resource:
        title: OpenAI Agents SDK
        link: https://openai.github.io/openai-agents-python/
        type: blog


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


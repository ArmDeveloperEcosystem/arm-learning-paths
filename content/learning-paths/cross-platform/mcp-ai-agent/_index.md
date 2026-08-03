---
title: Deploy an MCP Server on Raspberry Pi 5 for AI agent interaction using OpenAI SDK
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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-29T16:41:23Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 39d489081bfa22125a4046c17d5c00a32c0d7b298cba7b6a12373cf3cf6bac04
  summary_generated_at: '2026-07-29T16:41:23Z'
  summary_source_hash: 39d489081bfa22125a4046c17d5c00a32c0d7b298cba7b6a12373cf3cf6bac04
  faq_generated_at: '2026-07-29T16:41:23Z'
  faq_source_hash: 39d489081bfa22125a4046c17d5c00a32c0d7b298cba7b6a12373cf3cf6bac04
  summary: >-
    You'll deploy a Model Context Protocol (MCP) server on Raspberry Pi 5 and connect it to an AI agent
    built with the OpenAI Agent SDK. You'll install `uv` and bootstrap a FastMCP server with CPU-temperature
    and weather tools. Then, you'll expose the server through an `ngrok` tunnel and configure an agent on a separate Arm
    Linux machine. Finally, you'll connect the server to the agent and prompt to retrieve live values from the Pi and external sources.
  faqs:
  - question: Where do I run the MCP server, and where do I run the AI agent?
    answer: >-
      Run the MCP server on Raspberry Pi 5. Run the AI agent on your development machine and connect
      it to the Pi over your network or through the `ngrok` tunnel.
  - question: Do I need `uv` installed on both my Raspberry Pi and my development machine?
    answer: >-
      Yes. Install `uv` on Raspberry Pi to set up the MCP server, and install it on your development
      machine to initialize and run the agent project.
  - question: After I run `uv init` for the agent, what files should appear?
    answer: >-
      `uv init` creates a `.venv` virtual environment and a `pyproject.toml` file in the project
      directory. Both files indicate that the project environment is ready.
  - question: How do I point the agent at the MCP server on my Raspberry Pi?
    answer: >-
      Add the MCP server address to the agent configuration, using either the `ngrok` HTTPS forwarding
      URL or the Pi's reachable network address. A correct endpoint lets the agent start without
      connection errors.
  - question: How do I know the CPU temperature and weather tools are actually being used?
    answer: >-
      Prompt the agent to report Raspberry Pi's CPU temperature or look up weather data. The response
      includes the requested values. If it doesn't, verify that the server is running and the
      connection details match.
# END generated_summary_faq

author: Andrew Choi

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

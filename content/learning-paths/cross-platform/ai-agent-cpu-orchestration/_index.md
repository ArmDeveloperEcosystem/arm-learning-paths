---
title: Run a local AI agent with Ollama to visualize CPU orchestration on Arm

description: Run a local AI concierge agent with Ollama on Arm and visualize how the CPU orchestrates web search, scraping, and text processing while Gemma 3 handles model reasoning.

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for developers who want to build a local, privacy-friendly AI agent on Arm hardware and visualize how the CPU orchestrates an agentic workflow around a locally served LLM.

learning_objectives:
    - Set up a Python environment and obtain a Serper web search API key for the agent
    - Serve an LLM locally with Ollama and select a model that fits your hardware
    - Explain how the CPU orchestrates an agentic workflow while the GPU handles model inference
    - Run the agent and interpret the CPU and GPU timeline it produces for each query

prerequisites:
    - An Arm-based computer running Linux or macOS, such as an Apple silicon MacBook or an NVIDIA DGX Spark
    - Familiarity with running Python scripts from the terminal

author: Jaidev Singh Chadha

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A
    - Neoverse
tools_software_languages:
    - Python
    - Ollama
    - Generative AI
    - LLM
operatingsystems:
    - Linux
    - macOS

shared_path: true
shared_between:
    - laptops-and-desktops
    - embedded-and-microcontrollers

further_reading:
    - resource:
        title: Orchestrate a persistent local AI agent with Hermes on NVIDIA DGX Spark
        link: /learning-paths/laptops-and-desktops/dgx_persistent_agent/
        type: website
    - resource:
        title: Build a Privacy-First LLM Smart Home on Raspberry Pi 5
        link: /learning-paths/embedded-and-microcontrollers/raspberry-pi-smart-home/
        type: website
    - resource:
        title: Build RAG applications with LlamaIndex on a Google Cloud C4A virtual machine
        link: /learning-paths/servers-and-cloud-computing/llamaindex-rag-axion/
        type: website
    - resource:
        title: Automate x86-to-Arm application migration using Arm MCP Server
        link: /learning-paths/servers-and-cloud-computing/arm-mcp-server/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

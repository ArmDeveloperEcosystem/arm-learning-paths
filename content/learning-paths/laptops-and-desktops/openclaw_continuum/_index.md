---
title: Extend OpenClaw for a Local-First AI Assistant Across Arm Platforms

description: Extend OpenClaw with local memory, document RAG, browser search, deterministic routing, and proactive scheduling, then move the same local-first runtime from NVIDIA DGX Spark with vLLM to a CPU-only Armv9 system with llama.cpp.

minutes_to_complete: 120

who_is_this_for: This is an advanced topic for developers who want to extend OpenClaw into a customizable local-first assistant with persistent memory, document RAG, explicit browser search, deterministic routing, and proactive scheduling. You will deploy the reference runtime on NVIDIA DGX Spark with vLLM, then move the same workflows to a CPU-only Armv9 system with llama.cpp.

learning_objectives:
    - Explain the local and external data boundaries of an OpenClaw-based runtime
    - Deploy and validate the reference runtime with local vLLM inference on NVIDIA DGX Spark
    - Verify persistent memory, document RAG, explicit browser search, deterministic routing, and proactive scheduling with Telegram and Qdrant
    - Move the same application workflows to a CPU-only Armv9 system through an OpenAI-compatible llama.cpp endpoint

prerequisites:
    - An NVIDIA DGX Spark system with NVIDIA drivers, Docker, and NVIDIA Container Toolkit
    - A CPU-only Armv9 system such as Radxa Orion O6 with at least 30 GB of memory
    - Administrative access to install Ollama and run Qdrant containers on both systems
    - A Telegram bot token and chat ID for the tutorial
    - Familiarity with Linux, Docker Compose, and command-line tools

author: Odin Shen

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-A
    - Cortex-X
operatingsystems:
    - Linux
tools_software_languages:
    - Python
    - Docker
    - vLLM
    - llama.cpp
    - Ollama

further_reading:
    - resource:
        title: OpenClaw — Personal AI Assistant
        link: https://github.com/openclaw/openclaw
        type: documentation
    - resource:
        title: Build a RAG pipeline on Arm-based NVIDIA DGX Spark
        link: /learning-paths/laptops-and-desktops/dgx_spark_rag/
        type: Learning Path
    - resource:
        title: Orchestrate a persistent local AI agent with Hermes on NVIDIA DGX Spark
        link: /learning-paths/laptops-and-desktops/dgx_persistent_agent/
        type: Learning Path
    - resource:
        title: Run ERNIE-4.5 Mixture of Experts model on Armv9 with llama.cpp
        link: /learning-paths/cross-platform/ernie_moe_v9/
        type: Learning Path
    - resource:
        title: OpenClaw Arm Continuum repository
        link: https://github.com/odincodeshen/openclaw-arm-continuum
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

---
title: Deploy local-first OpenClaw runtime on DGX Spark and CPU-only systems

description: Learn how to deploy one local-first OpenClaw runtime on [NVIDIA DGX Spark](https://www.nvidia.com/en-gb/products/workstations/dgx-spark/) and a CPU-only [Armv9 developement platform](https://developer.arm.com/community/arm-community-blogs/b/ai-blog/posts/beyond-the-demo-deploying-and-evaluating-open-source-ai-workloads-on-an-armv9-platform) while keeping inference, memory, documents, and proactive workflows under your control.

minutes_to_complete: 120

who_is_this_for: This is an advanced topic for developers who want to turn local LLM inference into an operational OpenClaw assistant. You will first deploy the runtime on NVIDIA DGX Spark with vLLM, then move the same Telegram, memory, RAG, search, and cron workflows to a CPU-only Armv9 system using llama.cpp.

learning_objectives:
    - Explain the data boundaries of a local-first OpenClaw deployment
    - Deploy and validate OpenClaw with local vLLM inference on NVIDIA DGX Spark
    - Use local memory, document RAG, browser search, and proactive cron workflows from Telegram
    - Move the same OpenClaw workflow to a CPU-only Armv9 system through an OpenAI-compatible llama.cpp endpoint

prerequisites:
    - An NVIDIA DGX Spark system with Docker, NVIDIA Container Toolkit, Ollama, and Qdrant
    - A CPU-only Armv9 system such as Radxa Orion O6 with at least 30 GB of memory
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

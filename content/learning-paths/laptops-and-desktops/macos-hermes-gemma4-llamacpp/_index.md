---
title: Run Hermes Agent with local Gemma 4 and llama.cpp on macOS

draft: true
cascade:
    draft: true

description: Build llama.cpp with Metal and Arm KleidiAI support on macOS, serve Gemma 4 E4B locally, and connect Hermes Agent to diagnose and fix code without cloud services.

minutes_to_complete: 45

who_is_this_for: This is an advanced topic for developers who want to run an autonomous AI agent locally on Apple silicon Macs, using llama.cpp with Metal acceleration and Gemma 4 E4B to diagnose and fix code without remote cloud dependencies.

learning_objectives:
    - Compile llama.cpp from source on macOS with Metal GPU, Apple Accelerate, and Arm KleidiAI optimizations.
    - Download Gemma 4 E4B from Hugging Face and benchmark Metal GPU versus CPU performance on Apple silicon.
    - Serve Gemma 4 E4B with a 64K context window and quantized Key-Value (KV) cache using llama-server.
    - Configure Nous Research Hermes Agent to use a local OpenAI-compatible endpoint and validate autonomous code-fixing workflows.

prerequisites:
    - An Apple silicon Mac running macOS with at least 16 GB of unified memory
    - At least 15 GB of free disk space for building llama.cpp and storing Gemma 4 E4B
    - Xcode Command Line Tools, Git, and CMake installed
    - Familiarity with the macOS Terminal, CMake builds, and basic Large Language Model (LLM) inference concepts

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Agentic AI
armips: []
operatingsystems:
    - macOS
tools_software_languages:
    - llama.cpp
    - Hermes Agent
    - Metal
    - CMake
    - C++
    - Python

further_reading:
    - resource:
        title: llama.cpp GitHub repository
        link: https://github.com/ggml-org/llama.cpp
        type: website
    - resource:
        title: Nous Research Hermes Agent
        link: https://hermes-agent.nousresearch.com/
        type: website
    - resource:
        title: Gemma 4 E4B GGUF models on Hugging Face
        link: https://huggingface.co/ggml-org/gemma-4-E4B-it-GGUF
        type: website
    - resource:
        title: Orchestrate a local Hermes AI agent on NVIDIA DGX Spark
        link: /learning-paths/laptops-and-desktops/dgx_persistent_agent/
        type: Learning Path
    - resource:
        title: Unlock quantized LLM performance on Arm-based NVIDIA DGX Spark
        link: /learning-paths/laptops-and-desktops/dgx_spark_llamacpp/
        type: Learning Path

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

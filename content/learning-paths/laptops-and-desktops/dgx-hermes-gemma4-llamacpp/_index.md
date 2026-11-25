---
title: Run Hermes Agent with local Gemma 4 and llama.cpp on NVIDIA DGX Spark

draft: true
cascade:
    draft: true

description: Build llama.cpp with CUDA and Arm KleidiAI on NVIDIA DGX Spark, benchmark Gemma 4 models on GPU versus CPU, and run Hermes Agent with Gemma 4 E4B without cloud APIs.

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for developers who want to run an autonomous AI agent with a local LLM on NVIDIA DGX Spark, using llama.cpp with Blackwell CUDA acceleration and Armv9.2 Grace CPU support to benchmark Gemma 4 models and diagnose and fix code without cloud API dependencies.

learning_objectives:
    - Compile llama.cpp from source on NVIDIA DGX Spark with CUDA 13 Blackwell (sm_121a) and Armv9.2 KleidiAI optimizations.
    - Download Gemma 4 E4B, 26B-A4B (MoE), and 31B from Hugging Face and benchmark Blackwell GPU versus Grace CPU performance.
    - Serve Gemma 4 E4B on the GB10 GPU with a 64K context window and quantized Key-Value (KV) cache using llama-server.
    - Configure Nous Research Hermes Agent to use a local OpenAI-compatible endpoint and validate autonomous code-fixing workflows.

prerequisites:
    - An NVIDIA DGX Spark system (Grace Blackwell GB10 with 128 GB unified memory) running Ubuntu 24.04 LTS with CUDA 13 installed
    - At least 45 GB of free disk space for building llama.cpp and storing Gemma 4 E4B, 26B-A4B, and 31B GGUF weights
    - Familiarity with the Linux command line, CMake builds, and basic Large Language Model (LLM) inference concepts

author: Jason Andrews

### Tags
skilllevels: Advanced
subjects: Agentic AI
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - llama.cpp
    - Hermes Agent
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
        title: Gemma 4 GGUF models on Hugging Face
        link: https://huggingface.co/ggml-org
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

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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-10T21:49:51Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 59eaec53e94f78a294d2d04f28d81bd885d0d47f30e88d3c87230145bac77980
  summary_generated_at: '2026-07-10T21:49:51Z'
  summary_source_hash: 59eaec53e94f78a294d2d04f28d81bd885d0d47f30e88d3c87230145bac77980
  faq_generated_at: '2026-07-10T21:49:51Z'
  faq_source_hash: 59eaec53e94f78a294d2d04f28d81bd885d0d47f30e88d3c87230145bac77980
  summary: >-
    You'll run a local concierge agent on an Arm machine and examine how the workload
    splits between CPU orchestration and GPU-backed model inference. You'll set up a
    Python environment, configure a Serper web search API key, and serve Gemma 3 locally
    with Ollama. As the agent answers your research-style questions, you'll use its per-query
    timeline to see how much of web search, scraping, ranking, deduplication, and extraction runs
    on the CPU.
  faqs:
  - question: How do I know Ollama is ready before running the agent?
    answer: >-
      Confirm Ollama is running and serving the `gemma3:4b` model. The local API at `http://localhost:11434`
      should be available before starting the script.
  - question: What do I need in the terminal environment when I start the script?
    answer: >-
      Activate your Python virtual environment and set `SERPER_API_KEY` in the same terminal session.
      The agent reads this variable at runtime for web search.
  - question: What result should I expect when the agent starts correctly?
    answer: >-
      You should see a greeting that explains the agent browses websites in real time and a prompt
      asking for your question. Type `quit` or `exit` to end the session.
  - question: How do I read the CPU and GPU timeline the agent prints?
    answer: >-
      CPU entries in the timeline correspond to tools (web search, scraping) and the orchestration pipeline (query expansion,
      ranking, deduplication, extraction). GPU entries correspond to the Gemma model running through
      Ollama. The agentic chain interleaves these steps.
  - question: Where can I see how the workflow is organized in the code?
    answer: >-
      Open `concierge_agent.py`. It groups the tools, the LLM "brain," the orchestration pipeline,
      and the agentic chain, and indicates which components run on the CPU or GPU.
# END generated_summary_faq

author: Jaidev Singh Chadha

generate_summary_faq: false
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


---
title: Run AI models with Docker Model Runner

description: Learn how to run pre-trained AI models locally using Docker Model Runner and build containerized applications integrating large language models.

minutes_to_complete: 45

who_is_this_for: This is for software developers and AI enthusiasts who want to run pre-trained AI models locally using Docker Model Runner.

learning_objectives:
    - Run AI models locally using Docker Model Runner.
    - Build containerized applications that integrate Large Language Models (LLMs).

prerequisites:
    - Docker Desktop (version 4.40 or later) installed on a system with at least 16GB of RAM (recommended).
    - Basic understanding of Docker CLI and concepts.
    - Familiarity with LLM concepts.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:04:02Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: eae0a23635e7a025e1a73baaf5ccbd01f2c031ec76725c68893ca02190e36deb
  summary_generated_at: '2026-06-01T22:04:54Z'
  summary_source_hash: eae0a23635e7a025e1a73baaf5ccbd01f2c031ec76725c68893ca02190e36deb
  faq_generated_at: '2026-06-02T23:04:02Z'
  faq_source_hash: eae0a23635e7a025e1a73baaf5ccbd01f2c031ec76725c68893ca02190e36deb
  summary: >-
    This introductory path shows how to run pre-trained large language models locally on Windows
    or macOS using Docker Model Runner, an official Docker extension that leverages llama.cpp
    without requiring you to install AI frameworks. You will start local LLM inference and then
    use Docker Compose to deploy a simple containerized AI chat application with a Flask frontend
    and a Model Runner backend. The provided example can interact with local models such as Llama
    3.2 or Gemma 3. Prerequisites are Docker Desktop 4.40+ (16GB RAM recommended), basic Docker
    CLI knowledge, and familiarity with LLM concepts. The workflow is designed to run across environments,
    including Arm-based systems, and takes about 45 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need Docker Desktop version 4.40 or later on Windows or macOS, a system with at least
      16GB of RAM recommended, basic understanding of Docker CLI and concepts, and familiarity
      with LLM concepts.
  - question: Do I need to install any LLM frameworks or toolchains locally?
    answer: >-
      No. Docker Model Runner uses llama.cpp under the hood, so you do not need to download, build,
      or install any LLM frameworks.
  - question: Will this work on Arm-based systems?
    answer: >-
      Yes. Docker Model Runner is designed to run models across different environments, including
      Arm-based systems; the steps target Windows or macOS with Docker Desktop.
  - question: Which models can I try with the example chat app?
    answer: >-
      The example supports interacting with local AI models such as Llama 3.2 or Gemma 3.
  - question: What result should I expect after deploying with Docker Compose?
    answer: >-
      You will run a simple web-based AI chat application where a Flask frontend communicates
      with a Docker Model Runner backend. You should be able to enter prompts in the web interface
      and receive model-generated responses.
# END generated_summary_faq

author: Jason Andrews

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
armips:
    - Neoverse
    - Cortex-A
operatingsystems:
    - Windows
    - macOS
tools_software_languages:
    - Docker
    - Python
    - LLM

further_reading:
    - resource:
        title: Docker Model Runner Documentation
        link: https://docs.docker.com/model-runner/
        type: documentation
    - resource:
        title: Introducing Docker Model Runner
        link: https://www.docker.com/blog/introducing-docker-model-runner/
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


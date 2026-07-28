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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-28T16:16:24Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: eae0a23635e7a025e1a73baaf5ccbd01f2c031ec76725c68893ca02190e36deb
  summary_generated_at: '2026-07-28T16:16:24Z'
  summary_source_hash: eae0a23635e7a025e1a73baaf5ccbd01f2c031ec76725c68893ca02190e36deb
  faq_generated_at: '2026-07-28T16:16:24Z'
  faq_source_hash: eae0a23635e7a025e1a73baaf5ccbd01f2c031ec76725c68893ca02190e36deb
  summary: >-
    You'll run pretrained LLMs locally with Docker Model Runner, then compose a Flask chat application
    around them. You'll use the Model Runner extension with `llama.cpp`, clone the example repository,
    start the frontend and backend with Docker Compose, choose a supported model such as Llama 3.2 or
    Gemma 3, and verify the chat UI and container status.
  faqs:
  - question: Do I need to install or build any ML frameworks to run a model with Docker Model
      Runner?
    answer: >-
      No. Docker Model Runner uses `llama.cpp`, so you don't need to download, build,
      or install LLM frameworks.
  - question: Which model should I choose for the example chat application?
    answer: >-
      The example supports local AI models such as Llama 3.2 or Gemma 3. Use a model available
      through Docker Model Runner in your environment.
  - question: What should I expect after starting the Docker Compose project?
    answer: >-
      Docker Compose brings up a Flask-based web frontend and a backend that serves AI responses
      through Docker Model Runner. You should be able to enter a prompt and receive a generated
      reply.
  - question: How can I confirm that the model and services are running correctly?
    answer: >-
      Open the chat interface and send a prompt; a response indicates the backend is reachable
      and the model is active. If there's no response, check the status of the container and logs in Docker Desktop.
  - question: Does local inference with Docker Model Runner require a cloud service?
    answer: >-
      No. The models run locally without cloud dependencies.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

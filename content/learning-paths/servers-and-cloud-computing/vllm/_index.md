---
title: Build and Run vLLM on Arm Servers

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for software developers and AI engineers interested in learning how to use the vLLM library on Arm servers.

learning_objectives:
    - Build vLLM from source on an Arm server.
    - Download a Qwen LLM from Hugging Face.
    - Run local batch inference using vLLM.
    - Create and interact with an OpenAI-compatible server provided by vLLM on your Arm server.

prerequisites:
    - An [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider, or a local Arm Linux computer with at least 8 CPUs and 16 GB RAM.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:15:37Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: db5987ec7987375d9b51de843b0e1faf0e61731b14c5a563d19aaad26f50f6bb
  summary_generated_at: '2026-06-02T05:25:21Z'
  summary_source_hash: db5987ec7987375d9b51de843b0e1faf0e61731b14c5a563d19aaad26f50f6bb
  faq_generated_at: '2026-06-03T02:15:37Z'
  faq_source_hash: db5987ec7987375d9b51de843b0e1faf0e61731b14c5a563d19aaad26f50f6bb
  summary: >-
    Learn to build vLLM from source on an Arm-based Ubuntu 24.04 LTS server, verify BFloat16 support,
    and run both local batch inference and an OpenAI-compatible server. The path uses a Qwen model
    from Hugging Face and shows how vLLM automatically downloads models on first run, with optional
    Hugging Face token authentication for gated models. You can follow the steps on an Arm instance
    from AWS, Microsoft Azure, Google Cloud, or Oracle, or on a local Arm Linux machine with at
    least 8 CPUs, 16 GB RAM, and 50 GB of storage. By the end, you will run batch prompts locally
    and serve requests through a local OpenAI-compatible API. No additional prerequisites are
    explicitly listed.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      Use an Arm server running Ubuntu 24.04 LTS with at least 8 cores, 16 GB RAM, and 50 GB disk
      space. You also need a processor that supports BFloat16. You can use an Arm-based instance
      from a supported cloud provider or a local Arm Linux computer.
  - question: How do I know if my Arm CPU supports BFloat16?
    answer: >-
      Run: lscpu | grep bf16. If the Flags are printed, your processor includes BFloat16 support
      as required by the steps.
  - question: Do I need to download the model from Hugging Face ahead of time?
    answer: >-
      No. vLLM downloads the required model automatically on first run. For models that require
      access approval or terms, authenticate with Hugging Face using huggingface-cli login and
      a token generated from your Hugging Face account.
  - question: Which model is used in this Learning Path?
    answer: >-
      A Qwen LLM from the Hugging Face Hub is used. The path guides you to obtain it via vLLM’s
      first-run download.
  - question: When should I use batch inference versus the OpenAI-compatible server?
    answer: >-
      Use batch inference for a quick local run from Python. Start the OpenAI-compatible server
      when you need an API endpoint on your Arm server; this avoids external APIs and supports
      the privacy, cost, and offline advantages described in the steps.
# END generated_summary_faq

author: Jason Andrews

### Tags
skilllevels: Introductory
subjects: ML
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - vLLM
    - LLM
    - Generative AI
    - Python
    - Hugging Face

further_reading:
    - resource:
        title: vLLM Documentation
        link: https://docs.vllm.ai/
        type: documentation
    - resource:
        title: vLLM GitHub Repository
        link: https://github.com/vllm-project/vllm
        type: github
    - resource:
        title: Hugging Face Model Hub
        link: https://huggingface.co/models
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


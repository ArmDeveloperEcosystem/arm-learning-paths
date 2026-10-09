---
title: Run optimized LLMs from the Arm AI Portal on Arm Neoverse-based instances

description: Download and run an Arm-optimized LLM using the supplied ONNX Runtime GenAI workflow, or use a coding agent to adapt the application for a compatible alternative model runtime or format.

minutes_to_complete: 35

who_is_this_for: This Learning Path is for developers and ML engineers running Arm-optimized Large Language Models (LLMs) on Arm Neoverse-based Linux machines. It provides a tested ONNX Runtime GenAI workflow and an optional AI coding agent workflow for compatible text-to-text packages that use alternative runtimes or formats.

learning_objectives:
    - Prepare an Arm Neoverse Linux machine and download a model from the Arm AI Portal.
    - Generate text from the terminal and optionally serve the model through a local web application.
    - Identify how the shared application calls the supplied ONNX Runtime GenAI adapter.
    - Compare runtime and model-format choices, and optionally use a coding agent to replace the supplied adapter for another compatible text-to-text package.

prerequisites:
    - An Arm Neoverse-based Linux machine running Ubuntu 24.04 LTS, with Python 3.11 or later, for example an AWS `m8g.xlarge` instance
    - At least 16 GB of memory if you plan to use one of the 8B models
    - Basic familiarity with Linux command-line tools and Python
    - (Optional) Access to a coding agent if you want to generate an adapter for another runtime

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-08T16:22:31Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3499e744ac80b0e88701b9e2249f8ee9e103f66a8f0fc49996412c8cb81bcbee
  summary_generated_at: '2026-09-08T16:22:31Z'
  summary_source_hash: 3499e744ac80b0e88701b9e2249f8ee9e103f66a8f0fc49996412c8cb81bcbee
  faq_generated_at: '2026-09-08T16:22:31Z'
  faq_source_hash: 3499e744ac80b0e88701b9e2249f8ee9e103f66a8f0fc49996412c8cb81bcbee
  summary: >-
    You'll run optimized LLMs from the Arm AI Portal on an Arm Neoverse-based Linux machine.
    First, you'll create a Python environment, download the shared application files, and either use the supplied
    ONNX Runtime GenAI adapter or generate a compatible replacement. You'll select and run a model and
    optionally start its web interface. Then, you'll examine how the runner scripts call the adapter. You'll optionally learn to compare
    alternative runtimes and formats for replacement if the supplied adapter doesn't suit your needs.
  faqs:
  - question: Which script should I run to generate text in the terminal or browser?
    answer: >-
      Use `run_model.py` for terminal generation and `genai_web.py` for an optional local browser
      interface. Both entry points call the shared adapter, which uses the supplied ONNX Runtime
      GenAI implementation.
  - question: How do I choose and set the correct ID for a model from the Arm AI Portal?
    answer: >-
      Select your model in the Arm AI Portal and copy its Hugging Face repository ID in the form
      `Arm/<model-repository-name>`. When you use the supplied adapter, choose an ID from the
      confirmed models table. If you generated an adapter for another runtime, keep your existing
      `MODEL_ID` and follow that package’s model-type and prompt guidance.
  - question: How do I verify my adapter before I run a model?
    answer: >-
      Use `validate_adapter.py` to check the adapter contract and required package files. If the
      check fails, align your implementation with the interface defined in `adapter_contract.py`.
  - question: What do I see after a successful terminal run?
    answer: >-
      You'll see generated text in the terminal. `run_model.py` reports time to first token and decode
      throughput.
  - question: Which components change if I switch to another runtime or model format?
    answer: >-
      Implement the adapter defined in `adapter_contract.py` for the target package, replacing
      the supplied ONNX Runtime GenAI implementation in `model_adapter.py`. You can retain the
      terminal and web runners and follow the alternative package’s guidance for model type and
      prompting.
# END generated_summary_faq

author: Matt Cossins

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Neoverse
cloud_service_providers:
  - AWS
  - Google Cloud
  - Microsoft Azure
operatingsystems:
    - Linux
tools_software_languages:
    - Python
    - ONNX Runtime
    - KleidiAI
    - Arm AI Portal
    - Hugging Face
    - Generative AI
    - LLM
    - Agent

further_reading:
    - resource:
        title: ONNX Runtime GenAI documentation
        link: https://onnxruntime.ai/docs/genai/
        type: documentation
    - resource:
        title: Arm models on Hugging Face
        link: https://huggingface.co/Arm/models
        type: website
    - resource:
        title: Download files from the Hugging Face Hub
        link: https://huggingface.co/docs/huggingface_hub/guides/download
        type: documentation
    - resource:
        title: ONNX Runtime execution providers
        link: https://onnxruntime.ai/docs/execution-providers/
        type: documentation
    - resource:
        title: KleidiAI project
        link: https://github.com/ARM-software/kleidiai
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

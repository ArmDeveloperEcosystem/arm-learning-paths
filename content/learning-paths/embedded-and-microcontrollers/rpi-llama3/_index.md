---
title: Run Llama 3 on a Raspberry Pi 5 using ExecuTorch

description: Learn how to compile the Llama 3 large language model using ExecuTorch, deploy it to a Raspberry Pi 5, and understand techniques for running LLMs in embedded environments.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for anyone interested in running the Llama 3 model on a Raspberry Pi 5, and learning about techniques for running large language models (LLMs) in an embedded environment.

learning_objectives:
    - Use Docker to run Raspberry Pi OS on an Arm Linux server.
    - Compile a Large Language Model (LLM) using ExecuTorch.
    - Deploy the Llama 3 model on an edge device.
    - Describe how to run Llama 3 on a Raspberry Pi 5 using ExecuTorch.
    - Describe techniques for running large language models in an embedded environment.

prerequisites:
    - An Arm Linux machine or an [Arm cloud instance](/learning-paths/servers-and-cloud-computing/csp/).
    - A Raspberry Pi 5.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-13T18:46:40Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 2002d26fbac9be37d639f6196d4e24d3602f55c565d3c4925aa3e6f859d36e1b
  summary_generated_at: '2026-08-13T18:46:40Z'
  summary_source_hash: 2002d26fbac9be37d639f6196d4e24d3602f55c565d3c4925aa3e6f859d36e1b
  faq_generated_at: '2026-08-13T18:46:40Z'
  faq_source_hash: 2002d26fbac9be37d639f6196d4e24d3602f55c565d3c4925aa3e6f859d36e1b
  summary: >-
    You'll build and deploy Llama 3 on a Raspberry Pi 5 with ExecuTorch. First, you'll use a Docker
    container running Raspberry Pi OS to create a Python environment, install dependencies, and compile
    a quantized model for edge execution. Then, you'll prepare 64-bit Raspberry Pi OS, transfer the
    artifacts, and run prompts to verify on-device responses.
  faqs:
  - question: Which Raspberry Pi OS image should I install on the Raspberry Pi 5?
    answer: >-
      Install the 64-bit version of Raspberry Pi OS. Use Raspberry Pi Imager as recommended in
      the Raspberry Pi documentation to prepare the SD card.
  - question: Should I set up ExecuTorch on the development host or directly on the Raspberry
      Pi?
    answer: >-
      Set up ExecuTorch inside the Raspberry Pi OS shell running in the Docker container on your
      Arm Linux machine. Doing so isolates dependencies and prepares binaries for deployment to the
      Raspberry Pi 5.
  - question: Do I need to quantize the Llama 3 model for the Raspberry Pi 5?
    answer: >-
      Quantization is often used to reduce the memory footprint of large models for memory-constrained
      devices. Choose an approach that fits your device constraints.
  - question: How do I verify that the model is running correctly on the Raspberry Pi 5?
    answer: >-
      After deploying the build artifacts, run prompts and confirm the model returns coherent
      responses. If you see errors or no output, check that the device uses the 64-bit Raspberry
      Pi OS and that the built binaries were transferred correctly.
  - question: Are there usage restrictions for Llama 3?
    answer: >-
      Yes. Llama models are subject to an acceptable use policy and a responsible use guide. Review
      those materials before using or distributing the model.
# END generated_summary_faq

author: Annie Tallund

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A
operatingsystems:
    - Linux
tools_software_languages:
    - LLM
    - Generative AI
    - Raspberry Pi
    - Hugging Face
    - ExecuTorch

further_reading:
    - resource:
        title: Practical AI for the Raspberry Pi
        link: https://github.com/ee292d/labs
        type: website
    - resource:
        title: ExecuTorch Overview
        link: https://pytorch.org/executorch-overview
        type: website
    - resource:
        title: ExecuTorch Examples
        link: https://github.com/pytorch/executorch/blob/main/examples/README.md
        type: website
    - resource:
        title: Run Llama3 8B on a Raspberry Pi 5 with ExecuTorch
        link: https://dev-discuss.pytorch.org/t/run-llama3-8b-on-a-raspberry-pi-5-with-executorch/2048
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

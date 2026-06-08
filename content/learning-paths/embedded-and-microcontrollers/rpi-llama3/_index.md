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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:39:40Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 9cd2c3082c4874dc596e1b7b59c3dc2143aaf1ce3e66948ab8b6af190ffa3776
  summary_generated_at: '2026-06-01T21:51:49Z'
  summary_source_hash: 9cd2c3082c4874dc596e1b7b59c3dc2143aaf1ce3e66948ab8b6af190ffa3776
  faq_generated_at: '2026-06-02T22:39:40Z'
  faq_source_hash: 9cd2c3082c4874dc596e1b7b59c3dc2143aaf1ce3e66948ab8b6af190ffa3776
  summary: >-
    This introductory Learning Path shows how to compile the Llama 3 large language model with
    ExecuTorch using a Docker container that runs Raspberry Pi OS on an Arm Linux machine or Arm
    cloud instance, then deploy it to a Raspberry Pi 5. You will create an isolated Python environment
    for ExecuTorch, build the binaries required for the device, and review quantization techniques
    relevant to running LLMs in embedded environments. Finally, you will install the 64-bit Raspberry
    Pi OS on the Raspberry Pi 5 and run the model, experimenting with prompts and settings to
    observe behavior on-device. Prerequisites are an Arm Linux machine or Arm cloud instance and
    a Raspberry Pi 5. Estimated time: 60 minutes.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      You need an Arm Linux machine or an Arm cloud instance, and a Raspberry Pi 5. No other explicit
      prerequisites are listed.
  - question: Where do I build the binaries for deployment?
    answer: >-
      You build in a Docker container running Raspberry Pi OS on your Arm Linux machine. Inside
      that container, set up ExecuTorch with an isolated Python environment before compiling the
      model.
  - question: Which Raspberry Pi OS should I install on the device?
    answer: >-
      Install the 64-bit version of Raspberry Pi OS using the Raspberry Pi documentation. The
      steps rely on the 64-bit image on the Raspberry Pi 5.
  - question: Do I need to quantize the Llama 3 model for the Raspberry Pi 5?
    answer: >-
      The Learning Path explains quantization and why it is often used to reduce the memory footprint
      of large models in memory-constrained environments. Follow the guidance in the steps to
      decide when to apply it.
  - question: How do I validate that the model is running correctly on the Raspberry Pi 5?
    answer: >-
      After deployment, experiment with different prompts and settings on the device as shown
      in the final section. You should observe the model generating text responses to your prompts.
# END generated_summary_faq

author: Annie Tallund

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


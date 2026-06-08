---
title: Fine-tune neural graphics models using Model Gym
description: Learn how to fine-tune and evaluate Neural Super Sampling (NSS) models using PyTorch and Arm's Model Gym API with hardware-aware optimization.
   
minutes_to_complete: 45

who_is_this_for: This is an advanced topic for developers exploring neural graphics and interested in training and deploying upscaling models like Neural Super Sampling (NSS) using PyTorch and Arm’s hardware-aware backend.

learning_objectives:
    - Understand the principles of neural graphics and how it’s applied to game performance
    - Learn how to fine-tune and evaluate a neural network for Neural Super Sampling (NSS)
    - Use the Model Gym Python API and CLI to configure and train neural graphics models
    - Visualize and inspect .vgf models using the Model Explorer tool

prerequisites:
    - Basic understanding of PyTorch and machine learning concepts
    - A development machine running Ubuntu 22.04, with a CUDA-capable NVIDIA® GPU
    - CUDA Toolkit version 11.8 or later

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:57:36Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e145caae5b20f7165251d88e334ba22d90c8b35270902778a2b6fe0ed0b250f6
  summary_generated_at: '2026-06-02T02:52:24Z'
  summary_source_hash: e145caae5b20f7165251d88e334ba22d90c8b35270902778a2b6fe0ed0b250f6
  faq_generated_at: '2026-06-02T23:57:36Z'
  faq_source_hash: e145caae5b20f7165251d88e334ba22d90c8b35270902778a2b6fe0ed0b250f6
  summary: >-
    This advanced Learning Path shows how to fine-tune and evaluate a Neural Super Sampling (NSS)
    upscaler using PyTorch with Arm’s Model Gym API and CLI on Ubuntu 22.04. You will set up a
    Python 3.10+ environment, install required system packages, clone open-source example notebooks,
    and launch a Jupyter Notebook to configure training and evaluation with hardware-aware optimization.
    The workflow exports models in .vgf format, which you then inspect using Model Explorer with
    the VGF adapter to review architecture, tensor shapes, and graph connectivity. The final section
    demonstrates how to register and train your own model via the Python API by subclassing BaseNGModel.
    Prerequisites include basic PyTorch knowledge, a CUDA-capable NVIDIA GPU, and CUDA Toolkit
    11.8 or later.
  faqs:
  - question: What do I need before running the notebooks?
    answer: >-
      You need basic familiarity with PyTorch and machine learning, a development machine running
      Ubuntu 22.04 with a CUDA-capable NVIDIA GPU, and CUDA Toolkit 11.8 or later.
  - question: How do I set up Python and system dependencies on Ubuntu?
    answer: >-
      Verify Python 3.10+ with: python3 --version. Then install dependencies with: sudo apt update
      followed by sudo apt install python3-venv python-is-python3 gcc make python3-dev -y.
  - question: How do I get the example notebooks used in this Learning Path?
    answer: >-
      Clone the open-source examples repository from GitHub using git clone. The exact repository
      URL is provided in the setup step of the Learning Path.
  - question: What result should I expect after training the NSS model?
    answer: >-
      You will produce a fine-tuned NSS model and export it as a .vgf file using the Model Gym
      toolchain. The .vgf can be opened in Model Explorer for inspection with the VGF adapter.
  - question: Can I integrate my own model into Model Gym?
    answer: >-
      Yes. Create a Python class that inherits from BaseNGModel, register it with the toolkit,
      and use the same Python API to run training, evaluation, and export as demonstrated for
      NSS.
# END generated_summary_faq

author: Annie Tallund

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Mali
tools_software_languages:
    - PyTorch
    - Jupyter Notebook
    - Vulkan
    - NX
operatingsystems:
    - Linux
further_reading:
    - resource:
        title: Model Gym GitHub Repository
        link: https://github.com/arm/neural-graphics-model-gym
        type: code
    - resource:
        title: NSS Fine-Tuning Guide
        link: https://developer.arm.com/documentation/111141/latest
        type: documentation
    - resource:
        title: Neural Graphics Development Kit
        link: https://developer.arm.com/mobile-graphics-and-gaming/neural-graphics
        type: website
    - resource:
        title: NSS on HuggingFace
        link: https://huggingface.co/Arm/neural-super-sampling
        type: website
    - resource:
        title: Vulkan Samples Learning Path
        link: /learning-paths/mobile-graphics-and-gaming/vulkan-ml-sample/
        type: learningpath


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


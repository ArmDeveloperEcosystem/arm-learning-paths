---
title: Fine-tune neural graphics models using Model Gym
description: Learn how to train, evaluate, quantize, and export Neural Super Sampling (NSS) models using PyTorch and Arm's Model Gym API.
   
minutes_to_complete: 45

who_is_this_for: This is an advanced topic for developers exploring neural graphics and interested in training and deploying upscaling models like Neural Super Sampling (NSS) using PyTorch and Arm’s hardware-aware backend.

learning_objectives:
    - Understand the principles of neural graphics and how it’s applied to game performance
    - Learn how to fine-tune and evaluate a neural network for Neural Super Sampling (NSS)
    - Use the Model Gym Python API and CLI to configure and train neural graphics models
    - Fine-tune an NSS model with quantization-aware training (QAT) and export it to .vgf
    - Inspect the graph of exported .vgf models using Model Explorer

prerequisites:
    - Basic understanding of PyTorch and machine learning concepts
    - A development machine running Ubuntu 22.04 or later, with a CUDA-capable NVIDIA® GPU
    - CUDA Toolkit v13.1.1 or later

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-17T22:08:29Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 9c6d2ad9f52170a4d0f12a41623a62fb73973dc4f74ce9c09b8f5230f90a3b14
  summary_generated_at: '2026-08-17T22:08:29Z'
  summary_source_hash: 9c6d2ad9f52170a4d0f12a41623a62fb73973dc4f74ce9c09b8f5230f90a3b14
  faq_generated_at: '2026-08-17T22:08:29Z'
  faq_source_hash: 9c6d2ad9f52170a4d0f12a41623a62fb73973dc4f74ce9c09b8f5230f90a3b14
  summary: >-
    You'll use Model Gym notebooks on Ubuntu to train and evaluate a Neural Super Sampling model
    in PyTorch. Inspect checkpoints, choose post-training or quantization-aware training, and prepare
    an INT8 export. Then export the fine-tuned model as a `.vgf` package and validate it in Model
    Explorer with the VGF adapter.
  faqs:
  - question: What should I verify before creating the Python environment?
    answer: >-
      Check that `python3` reports a supported version (3.10, 3.11, or 3.12). Then install the listed
      system packages before setting up the examples.
  - question: Which notebook should I use to export a deployable model?
    answer: >-
      Use the `model_qat_example.ipynb` notebook. It is the only example notebook that includes
      the export step to produce a `.vgf` file.
  - question: When should I choose PTQ versus QAT for NSS?
    answer: >-
      Post-training quantization (PTQ) is faster to try because it calibrates an already-trained
      model. Quantization-aware training (QAT) simulates lower precision during fine-tuning to
      help preserve accuracy when exporting an INT8 model.
  - question: How do I confirm that the export completed correctly?
    answer: >-
      Expect a `.vgf` model produced by the export pipeline. Open it in Model Explorer with the
      VGF adapter; a valid graph with layers, tensor shapes, and connectivity indicates a successful
      export.
  - question: Can Model Explorer show image quality or frame comparisons?
    answer: >-
      No. Model Explorer visualizes the network structure and execution graph, not rendered output
      quality. Use the evaluation notebook to compare model output with the ground truth.
# END generated_summary_faq

author: Annie Tallund
generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
        title: Quantize neural upscaling models with ExecuTorch
        link: /learning-paths/mobile-graphics-and-gaming/quantize-neural-upscaling-models/
        type: learningpath
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

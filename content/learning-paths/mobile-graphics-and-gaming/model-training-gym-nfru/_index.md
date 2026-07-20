---
title: Train and evaluate Neural Frame Rate Upscaling (NFRU) models using Model Gym
description: Learn how to train and evaluate Neural Frame Rate Upscaling (NFRU) models using PyTorch and Arm's Model Gym API with hardware-aware optimization.

minutes_to_complete: 45

who_is_this_for: This is an advanced topic for developers exploring neural graphics and interested in training and deploying frame generation models such as Neural Frame Rate Upscaling (NFRU) using PyTorch and Arm's hardware-aware backend.

learning_objectives:
    - Understand the principles of neural graphics and how it's applied to game performance
    - Fine-tune and evaluate a neural network for Neural Frame Rate Upscaling (NFRU)
    - Use the Model Gym Python API and CLI to configure and train neural graphics models
    - Visualize and inspect .vgf models using the Model Explorer tool

prerequisites:
    - Basic understanding of PyTorch and machine learning concepts
    - A development machine running Ubuntu 22.04, with a CUDA-capable NVIDIA GPU
    - CUDA Toolkit version 11.8 or later
    - A working environment with a Python version later than 3.10

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-20T16:07:04Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ded91359108315578a7fe3cf0a96efc6d3d55319849ddb8c636571d2e569e011
  summary_generated_at: '2026-07-20T16:07:04Z'
  summary_source_hash: ded91359108315578a7fe3cf0a96efc6d3d55319849ddb8c636571d2e569e011
  faq_generated_at: '2026-07-20T16:07:04Z'
  faq_source_hash: ded91359108315578a7fe3cf0a96efc6d3d55319849ddb8c636571d2e569e011
  summary: >-
    You'll set up an Ubuntu development environment, explore Arm's Neural
    Graphics Model Gym, and fine-tune a Neural Frame Rate Upscaling (NFRU) model using PyTorch. First, you'll launch a training notebook to configure and run NFRU training. Then, you'll train and evaluate a model using PyTorch and Model Gym, and export that model into VGF (.vgf) for real-time deployment. You'll also visualize and inspect the model's structure using Model Explorer. Finally, you'll learn how to register a custom neural graphics model with Model Gym so the same training, evaluation, and export workflow can be reused for new use cases.
  faqs:
  - question: How do I confirm my Python setup is ready before opening the notebooks?
    answer: >-
      Run `python3 --version` and verify it reports a version later than `3.10`. Ensure the listed Ubuntu packages
      are installed so virtual environments and builds can complete.
  - question: Which notebook do I open to start training NFRU?
    answer: >-
      Open the NFRU training notebook in the examples repository you cloned. Follow the notebook
      cells to configure training and run the workflow.
  - question: What output should I expect after running training and export?
    answer: >-
      Expect an exported `.vgf` model produced by the training and export pipeline. You can open the file with Model Explorer using the VGF adapter.
  - question: How do I know the VGF adapter is working in Model Explorer?
    answer: >-
      Load a `.vgf` file and check that the model graph renders with layers, tensor shapes, and
      connectivity visible. If the graph opens without errors, the adapter is set up correctly.
  - question: What do I need to implement to add my own model to Model Gym?
    answer: >-
      Create a Python class that inherits from BaseNGModel, annotate it with the `@register_model()`
      decorator, implement the required methods, and accept params in the constructor. After registration,
      you can run the same training, evaluation, and export steps used for NFRU.
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
        title: Model Gym Examples Repository
        link: https://github.com/arm/neural-graphics-model-gym-examples
        type: code
    - resource:
        title: Neural Graphics Development Kit
        link: https://developer.arm.com/mobile-graphics-and-gaming/neural-graphics
        type: website
    - resource:
        title: Neural Frame Rate Upscaling Early Access Program
        link: https://developer.arm.com/mobile-graphics-and-gaming/neural-graphics/early-access-program
        type: website
    - resource:
        title: Neural Frame Rate Upscaling in Unreal Engine
        link: /learning-paths/mobile-graphics-and-gaming/nfru-unreal/
        type: learningpath
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

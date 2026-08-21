---
title: Train and evaluate Neural Frame Rate Upscaling models using Model Gym
description: Learn how to train and evaluate Neural Frame Rate Upscaling (NFRU) models using PyTorch and Arm's Model Gym API with hardware-aware optimization.

minutes_to_complete: 45

who_is_this_for: This is an advanced topic for developers exploring neural graphics and interested in training and deploying frame generation models such as Neural Frame Rate Upscaling (NFRU) using PyTorch and Arm's hardware-aware backend.

learning_objectives:
    - Understand the principles of neural graphics and how it's applied to game performance
    - Fine-tune and evaluate a neural network for Neural Frame Rate Upscaling (NFRU)
    - Use the Model Gym Python API and CLI to configure and train neural graphics models
    - Fine-tune an NFRU model with quantization-aware training (QAT) and export it to .vgf
    - Inspect the graph of exported .vgf models using Model Explorer

prerequisites:
    - Basic understanding of PyTorch and machine learning concepts
    - A development machine running Ubuntu 22.04, with a CUDA-capable NVIDIA GPU
    - CUDA Toolkit version 11.8 or later
    - A working environment with a Python version later than 3.10

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-21T17:24:25Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 766071e129870615cdc37f1766bb720bb7085d0464c4f0dcdc64a96ea8efee29
  summary_generated_at: '2026-08-21T17:24:25Z'
  summary_source_hash: 766071e129870615cdc37f1766bb720bb7085d0464c4f0dcdc64a96ea8efee29
  faq_generated_at: '2026-08-21T17:24:25Z'
  faq_source_hash: 766071e129870615cdc37f1766bb720bb7085d0464c4f0dcdc64a96ea8efee29
  summary: >-
    You'll explore neural graphics and use Arm Neural Graphics Model Gym to train and evaluate an
    NFRU model. First, you'll set up Ubuntu, clone the examples repository, and use Jupyter notebooks to train,
    evaluate, and compare checkpoints. Then, you'll fine-tune pretrained FP32 weights with QAT and export an
    INT8 `.vgf` model. Finally, you'll use Model Explorer and the VGF adapter to inspect the model's
    architecture, tensor shapes, and graph connectivity.
  faqs:
  - question: What should I check before I run the notebooks on Ubuntu?
    answer: >-
      Confirm that Python is later than `3.10` with `python3 --version`. Then, install the required
      dependency packages.
  - question: Where do I start the training after cloning the examples repository?
    answer: >-
      From `neural-graphics-model-gym-examples`, run `jupyter lab`. Then open
      `tutorials/nfru/nfru_training_example.ipynb` and step through the notebook for training.
  - question: How do I know the initial training produced usable artifacts?
    answer: >-
      Create and inspect PyTorch checkpoints in the training and evaluation notebooks. In the
      evaluation notebook, you can measure accuracy, compare checkpoints, and see a visual comparison
      of the generated NFRU frame with the ground truth frame.
  - question: Which should I use for deployment, QAT or PTQ?
    answer: >-
      Start with PTQ if you want a faster trial because it calibrates an already-trained model
      without another training phase. Use QAT when PTQ causes unacceptable accuracy or visual-quality
      regressions; QAT simulates lower-precision inference during fine-tuning and helps preserve
      accuracy when you quantize the model to INT8.
  - question: How do I export and inspect the deployable model?
    answer: >-
      Use the QAT notebook from the dedicated NFRU examples tag. The notebook includes the export step to
      produce a `.vgf` file. Then, open the `.vgf` file in Model Explorer with the VGF adapter to
      inspect architecture, tensor shapes, and graph connectivity.
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
        title: Arm Neural Technology Playbook - Evaluate
        link: /learning-paths/mobile-graphics-and-gaming/neural-graphics-playbook-evaluate/
        type: learningpath
    - resource:
        title: Enable Neural Frame Rate Upscaling in Unreal Engine
        link: /learning-paths/mobile-graphics-and-gaming/nfru-unreal/
        type: learningpath
    - resource:
        title: Analyze Neural Frame Rate Upscaling using Project Moku
        link: /learning-paths/mobile-graphics-and-gaming/nfru-cases-study/
        type: learningpath
    - resource:
        title: Model Gym GitHub Repository
        link: https://github.com/arm/neural-graphics-model-gym
        type: code
    - resource:
        title: Model Gym Examples Repository
        link: https://github.com/arm/neural-graphics-model-gym-examples
        type: code
    - resource:
        title: Arm Neural Frame Rate Upscaling model on Hugging Face
        link: https://huggingface.co/Arm/neural-frame-rate-upscaling
        type: code
### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

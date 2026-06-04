---
title: "Edge AI on Arm: PyTorch and ExecuTorch rock-paper-scissors"

description: Learn how to train a CNN image classification model using PyTorch, convert it to ExecuTorch format, and run it as an interactive mini-game on Arm-based edge devices.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for machine learning developers who want to deploy TinyML models on Arm-based edge devices using PyTorch and ExecuTorch.

learning_objectives:
  - Train a small Convolutional Neural Network (CNN) for image classification using PyTorch
  - Use synthetic data generation for training a model when real data is limited
  - Convert and optimize a PyTorch model to an ExecuTorch program (`.pte`) for Arm-based devices
  - Run the trained model locally as an interactive mini-game to demonstrate inference

prerequisites:
  - Basic understanding of machine learning concepts
  - Familiarity with Python and the PyTorch library
  - Completion of the Learning Path [Introduction to TinyML on Arm using PyTorch and ExecuTorch](/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/)
  - An x86 Linux host machine or VM running Ubuntu 22.04 or later

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:43:51Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 20c500fd5174c9901058676d4619981ee1c8a8cf8e331affea8c0292112651c9
  summary_generated_at: '2026-06-01T21:54:57Z'
  summary_source_hash: 20c500fd5174c9901058676d4619981ee1c8a8cf8e331affea8c0292112651c9
  faq_generated_at: '2026-06-02T22:43:51Z'
  faq_source_hash: 20c500fd5174c9901058676d4619981ee1c8a8cf8e331affea8c0292112651c9
  summary: >-
    This Learning Path walks you through training a small CNN in PyTorch to classify images of
    the letters R, P, and S into rock, paper, or scissors, exporting the model to an ExecuTorch
    program (.pte), and running it as a simple interactive mini-game. You then compile and execute
    the model on the Corstone-320 Fixed Virtual Platform (FVP), completing an end-to-end TinyML
    workflow for Arm-based edge devices. The path uses synthetic data generation when real data
    is limited and employs the Ahead-of-Time Arm compiler with delegation to the Ethos-U NPU.
    Prerequisites include basic ML knowledge, Python/PyTorch familiarity, the prior TinyML Learning
    Path, and an x86 Ubuntu 22.04+ Linux host.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need basic ML knowledge, familiarity with Python and PyTorch, completion of the “Introduction
      to TinyML on Arm using PyTorch and ExecuTorch” Learning Path, and an x86 Linux host or VM
      running Ubuntu 22.04 or later. The path targets the Corstone-320 FVP, so additional Arm
      hardware is not explicitly required.
  - question: Where should I create the script and start training?
    answer: >-
      Navigate to $HOME/executorch/examples/arm and create rps_tiny.py there. Train and export/play
      using the provided commands, for example: python rps_tiny.py --epochs 8 --export --play.
  - question: Do I need a real image dataset to train the model?
    answer: >-
      No. The path uses synthetic data generation for training when real data is limited.
  - question: What artifact should I expect after exporting the model?
    answer: >-
      Exporting produces an ExecuTorch program (.pte). You will then compile and build it for
      the Corstone-320 FVP using the Ahead-of-Time Arm compiler with delegation to the Ethos-U
      NPU.
  - question: What should I expect when I run the mini-game or the FVP build?
    answer: >-
      The --play option runs an interactive CLI mini-game that classifies the letters R, P, and
      S as rock, paper, or scissors. The FVP build runs the trained model on a simulated Arm-based
      edge device to demonstrate on-device inference.
# END generated_summary_faq

author: Dominica Abena O. Amanfo

### Tags
skilllevels: Introductory
subjects: ML
armips:
  - Cortex-M
  - Ethos-U
tools_software_languages:
    - tinyML
    - Computer Vision
    - Edge AI
    - CNN
    - PyTorch
    - ExecuTorch

operatingsystems:
  - Linux

further_reading:
  - resource:
      title: Run Llama 3 on a Raspberry Pi 5 using ExecuTorch
      link: /learning-paths/embedded-and-microcontrollers/rpi-llama3
      type: website
  - resource:
      title: ExecuTorch examples
      link: https://github.com/pytorch/executorch/blob/main/examples/README.md
      type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


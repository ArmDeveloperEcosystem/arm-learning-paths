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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-13T18:53:51Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f37686abb834f8b54a3a2c27a7d16569e228293c57286ce13dfd36ab13256a65
  summary_generated_at: '2026-08-13T18:53:51Z'
  summary_source_hash: f37686abb834f8b54a3a2c27a7d16569e228293c57286ce13dfd36ab13256a65
  faq_generated_at: '2026-08-13T18:53:51Z'
  faq_source_hash: f37686abb834f8b54a3a2c27a7d16569e228293c57286ce13dfd36ab13256a65
  summary: >-
    You'll build a rock-paper-scissors prototype with PyTorch and ExecuTorch on Arm. First, you'll
    create a lightweight image-classification CNN, train it, export a `.pte` program, and run the
    command-line mini-game. Then, you'll compile the model with the Ahead-of-Time Arm compiler and
    run it on the Corstone-320 Fixed Virtual Platform with Ethos-U delegation.
  faqs:
  - question: Where should I put the rock–paper–scissors script before training?
    answer: >-
      Place the script in the ExecuTorch repository under the Arm examples directory at `$HOME/executorch/examples/arm`.
  - question: How do I launch the mini‑game after training?
    answer: >-
      Run the script with the play option. The mini‑game uses the
      best weights found on disk.
  - question: How do I know the export to ExecuTorch worked?
    answer: >-
      A successful export produces a `.pte` file. Check that the file is created in the expected
      location after running the export step.
  - question: Do I need a dataset or camera for training?
    answer: >-
      You don't need an external dataset or camera because you'll use synthetic data generation
      for training. The model learns to classify images of the letters R, P, and S.
  - question: Which log messages confirm that the model starts on the Corstone-320 FVP?
    answer: >-
      Check the FVP output for the model loading and `Running method forward` messages. An
      `EthosUBackend.cpp` initialization message confirms that the Ethos-U backend starts during
      inference.
# END generated_summary_faq

author: Dominica Abena O. Amanfo

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

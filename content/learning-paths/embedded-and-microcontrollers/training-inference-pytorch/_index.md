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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:55Z'
  generator: template
  source_hash: 20c500fd5174c9901058676d4619981ee1c8a8cf8e331affea8c0292112651c9
  summary: >-
    Learn how to train a CNN image classification model using PyTorch, convert it to ExecuTorch
    format, and run it as an interactive mini-game on Arm-based edge devices. It is designed for
    machine learning developers who want to deploy TinyML models on Arm-based edge devices using
    PyTorch and ExecuTorch. By the end, you will be able to train a small Convolutional Neural
    Network (CNN) for image classification using PyTorch, use synthetic data generation for training
    a model when real data is limited, and convert and optimize a PyTorch model to an ExecuTorch
    program (`.pte`) for Arm-based devices. It focuses on tools and technologies such as tinyML,
    Computer Vision, Edge AI, CNN, and PyTorch, Linux environments, and Arm platforms including
    Cortex-M and Ethos-U. The main steps cover Set up your environment, Train and Test the rock-paper-scissors
    Model, and Run the model on Corstone-320 FVP.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will train a small Convolutional Neural Network (CNN) for image classification using
      PyTorch, use synthetic data generation for training a model when real data is limited, and
      convert and optimize a PyTorch model to an ExecuTorch program (`.pte`) for Arm-based devices.
      Learn how to train a CNN image classification model using PyTorch, convert it to ExecuTorch
      format, and run it as an interactive mini-game on Arm-based edge devices.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for machine learning developers who want to deploy TinyML
      models on Arm-based edge devices using PyTorch and ExecuTorch.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: Basic understanding of machine learning
      concepts; Familiarity with Python and the PyTorch library; Completion of the Learning Path
      [Introduction to TinyML on Arm using PyTorch and ExecuTorch](/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/);
      An x86 Linux host machine or VM running Ubuntu 22.04 or later.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including tinyML, Computer Vision, Edge AI, CNN, and PyTorch,
      Linux environments, and Arm platforms such as Cortex-M and Ethos-U.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Set up your environment, Train and Test the rock-paper-scissors
      Model, and Run the model on Corstone-320 FVP.
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


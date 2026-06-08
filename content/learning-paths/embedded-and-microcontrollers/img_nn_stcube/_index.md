---
title: Build and run an image classification NN model on an STM32L4 Discovery board

description: Develop a image classification neural network model and deploy it on an STM32 B-L475E-IOT01A2 board.

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for embedded software developers interested in building neural network models for microcontrollers.

learning_objectives: 
    - Build a convolution neural network(CNN) model for image classification.
    - Run the CNN model on an STM32 B-L475E-IOT01A2 board using STM Cube AI

prerequisites:
    - Familiarity with ML concepts
    - Familiarity with C programming on microcontrollers
    - STM32 B-L475E-IOT01A2 board

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:21:11Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 66024a2e3da90dcda298bf66b5de07952ed1e355d22172bc2812c46ad4fcda7f
  summary_generated_at: '2026-06-01T21:40:03Z'
  summary_source_hash: 66024a2e3da90dcda298bf66b5de07952ed1e355d22172bc2812c46ad4fcda7f
  faq_generated_at: '2026-06-02T22:21:11Z'
  faq_source_hash: 66024a2e3da90dcda298bf66b5de07952ed1e355d22172bc2812c46ad4fcda7f
  summary: >-
    This Learning Path walks you through building a convolutional neural network for image classification
    using the CIFAR-10 dataset in a Jupyter Notebook environment set up with Anaconda, then deploying
    and running it on an Arm Cortex-M–based STM32 B-L475E-IOT01A2 (STM32L4 Discovery) board. You
    will import the trained model into an STM32CubeMX project using STM32Cube.AI, target a bare-metal
    configuration, and exercise the model on hardware with a provided ST Python tool that sends
    images to the board. It is aimed at advanced embedded developers. Prerequisites include familiarity
    with ML concepts, C programming on microcontrollers, and access to the specified STM32 board.
    The steps note using X-CUBE-AI 7.0.0 for the testing tool.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      You need an STM32 B-L475E-IOT01A2 board, familiarity with ML concepts, and familiarity with
      C programming on microcontrollers. No other explicit prerequisites are listed.
  - question: How do I open and run the training notebook?
    answer: >-
      From an Anaconda Prompt, run "jupyter notebook" and open lab.ipynb from the extracted project
      files. Click Run to execute each cell; In[] means not started, In[*] means running, and
      In[N] indicates the cell completed.
  - question: Which dataset and model are used for training?
    answer: >-
      The model is a CNN trained on the CIFAR-10 dataset, which contains 60,000 images across
      10 categories. The model takes an RGB image as input and predicts its category.
  - question: Which STM32Cube tools and versions should I use during deployment?
    answer: >-
      Install STM32CubeMX using the Windows installer and add the STM32Cube.AI extension. Select
      X-CUBE-AI 7.0.0, as the provided testing tool was written for this version and later versions
      may not connect successfully.
  - question: How do I run the testing tool and what if the board is not detected?
    answer: >-
      Activate your Anaconda environment (conda activate ml_lab), install opencv-python, protobuf==3.20,
      and tqdm==4.50.2, then run "python ui_python_ai_runner.py" from the Misc folder. If the
      board is not detected, press the black reset button on the board and try again.
# END generated_summary_faq

author: Pareena Verma

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-M
operatingsystems:
    - Baremetal
tools_software_languages:
    - TensorFlow
    - STM32

further_reading:
    - resource:
        title: Jupyter documentation
        link: https://docs.jupyter.org/en/latest/
        type: documentation
    - resource:
        title: Getting started with STM32 MCU Discovery Kits software development tools
        link: https://www.st.com/resource/en/user_manual/um2052-getting-started-with-stm32-mcu-discovery-kits-software-development-tools-stmicroelectronics.pdf
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


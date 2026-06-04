---
title: Build and run a letter recognition NN model on an STM32L4 Discovery board

description: Build a letter recognition neural network model using TensorFlow and deploy it on an STM32 B-L475E-IOT01A2 board.

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for software developers interested in building network models for microcontrollers.

learning_objectives: 
    - Build a letter recognition neural network(NN) model using TensorFlow framework
    - Run the NN model on an STM32 B-L475E-IOT01A2 board using STM32CubeAI

prerequisites:
    - Familiarity with ML concepts
    - Familiarity with C programming on microcontrollers
    - STM32 B-L475E-IOT01A2 board

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:42:04Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b5714494f00fff407c39e6f2f7bf37de94cde61d7569ba147412fec1b2f537c2
  summary_generated_at: '2026-06-01T21:53:37Z'
  summary_source_hash: b5714494f00fff407c39e6f2f7bf37de94cde61d7569ba147412fec1b2f537c2
  faq_generated_at: '2026-06-02T22:42:04Z'
  faq_source_hash: b5714494f00fff407c39e6f2f7bf37de94cde61d7569ba147412fec1b2f537c2
  summary: >-
    This Learning Path guides you through building a letter recognition neural network in TensorFlow
    using accelerometer data from an STM32 B-L475E-IOT01A2 board, then deploying it to the device
    with STM32Cube.AI. You will set up a Python environment with Anaconda, work in a Jupyter notebook
    to collect data and train a multi-layer perceptron, and create a feature-based model using
    mean and standard deviation per axis. Finally, you will configure an STM32CubeMX project and
    run the model on the Arm Cortex-M4–based board in a bare-metal configuration. This advanced
    path assumes familiarity with ML concepts and C programming on microcontrollers, and access
    to the specified STM32 board.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      Have the STM32 B-L475E-IOT01A2 board and be comfortable with ML concepts and C programming
      on microcontrollers. Install Anaconda for the Python environment and download STM32CubeMX;
      STM32Cube.AI will be used within STM32CubeMX to import the trained model.
  - question: How should I run the Jupyter notebook steps, and how do I know each cell finished?
    answer: >-
      Run the cells in order using the Run button. Jupyter shows In[ ] before execution, In[*]
      while running, and In[N] when a cell has completed.
  - question: What data do I train on, and how is it prepared?
    answer: >-
      You will use accelerometer data from the STM32 board to recognize letters. The dataset is
      stored as CSV files in a samples directory and is first used as raw sequences; later you
      extract features (mean and standard deviation per axis) and retrain.
  - question: Which model architecture should I define in TensorFlow?
    answer: >-
      Define a multi-layer perceptron with three dense layers and dropout using TensorFlow/Keras,
      as shown in the notebook. Labels are converted to categorical form before training.
  - question: Which option should I use in STM32CubeMX to target the board and import the model?
    answer: >-
      Open STM32CubeMX and use Access to Board Selector to find the B-L475E-IOT01A board and start
      a new project, then set the project name and location. Under Pinout & Configuration, proceed
      with setup and use the STM32Cube.AI extension to import the trained ML model.
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


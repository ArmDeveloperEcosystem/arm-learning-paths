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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-13T18:52:01Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 84ca66f022d1d5fe4b1e6aafc641e1ea6a74b1a239145567712f79f91b39f624
  summary_generated_at: '2026-08-13T18:52:01Z'
  summary_source_hash: 84ca66f022d1d5fe4b1e6aafc641e1ea6a74b1a239145567712f79f91b39f624
  faq_generated_at: '2026-08-13T18:52:01Z'
  faq_source_hash: 84ca66f022d1d5fe4b1e6aafc641e1ea6a74b1a239145567712f79f91b39f624
  summary: >-
    You'll build a TensorFlow model that recognizes letters from motion data on an STM32 B-L475E-IOT01A2.
    First, you'll use Anaconda and a Jupyter notebook to collect accelerometer samples and train a
    multilayer perceptron. Then, you'll extract statistical features, retrain the model, import it with
    STM32Cube.AI, and run predictions with the board's onboard accelerometer.
  faqs:
  - question: How do I know when a Jupyter cell has finished running?
    answer: >-
      Jupyter shows `In[*]` while a cell is running. When complete, it changes to `In[N]`, where N
      is the execution count.
  - question: Where do the training samples come from and what files should I expect?
    answer: >-
      You'll collect accelerometer data from the STM32 board and save it as CSV files. The notebook
      discovers these CSV files from the `samples_dir` location and loads them for training.
  - question: What input shape does the neural network expect and how are labels prepared?
    answer: >-
      The example model uses an input shape of (3, stride), representing three accelerometer axes
      over a time window. Labels are one-hot encoded using `tf.keras.utils.to_categorical` with
      the class count derived from the unique labels.
  - question: What features are extracted before retraining the model?
    answer: >-
      The process computes the mean and standard deviation for each accelerometer axis and saves
      these as features. You then train a model on these feature vectors instead of the raw time-series
      samples.
  - question: Which options should I use in STM32CubeMX to set up the project and import the model?
    answer: >-
      Use the **Board Selector** to choose the B-L475E-IOT01A board, then set the project name and
      location in **Project Manager**. Import the trained model using STM32Cube.AI within STM32CubeMX,
      and continue with **Pinout & Configuration**.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-12T20:05:24Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d2b95465621235e0a43ded6268ba954cc32865c4a53c89667881ccfbe4139074
  summary_generated_at: '2026-08-12T20:05:24Z'
  summary_source_hash: d2b95465621235e0a43ded6268ba954cc32865c4a53c89667881ccfbe4139074
  faq_generated_at: '2026-08-12T20:05:24Z'
  faq_source_hash: d2b95465621235e0a43ded6268ba954cc32865c4a53c89667881ccfbe4139074
  summary: >-
    You'll build a CIFAR-10 convolutional neural network in Jupyter and deploy it to an STM32
    B-L475E-IOT01A2 board. First, you'll prepare an Anaconda environment, train the model, and import it
    into STM32Cube.AI within STM32CubeMX. Then, you'll deploy the generated project and use a Python
    utility to send images to the board and exercise the classifier.
  faqs:
  - question: How do I launch the Jupyter Notebook used for training?
    answer: >-
      Open **Anaconda Prompt** and run `jupyter notebook`. In the browser, navigate to the extracted
      project files and open `lab.ipynb`.
  - question: How do I know a notebook cell has finished running?
    answer: >-
      Check the indicator to the left of the cell: `In[]` before running, `In[*]` while running,
      and `In[N]` (a number) when complete.
  - question: Which STM32Cube.AI version should I select in STM32CubeMX?
    answer: >-
      Select **X-CUBE-AI 7.0.0**, which matches the version used by the provided testing tool. Later
      versions might not connect successfully.
  - question: What should I do before running the Python test tool against the board?
    answer: >-
      Activate the Conda environment with `conda activate ml_lab` and install `opencv-python`,
      `protobuf==3.20`, and `tqdm==4.50.2`. Then, go to the working folder's `Misc` directory.
  - question: How do I start the test tool and what if the board is not detected?
    answer: >-
      From the `Misc` folder, run `python ui_python_ai_runner.py`. If the board isn't detected,
      press the black button on the board to reset and try again.
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

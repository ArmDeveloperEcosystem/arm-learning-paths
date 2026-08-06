---
title: Deploying a Zephyr-Based ML Application on the Arm Corstone-320 MPS4 Platform with ExecuTorch

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for embedded software developers who want to deploy a Zephyr-based ML Application on the Arm Corstone-320 MPS4 Platform with ExecuTorch.

learning_objectives: 
    - Set up a Zephyr ML application development environment for Corstone-320 MPS4.
    - Pre-process the model for NPU delegate.
    - Create and build Zephyr ML applications.
    - Run ML inference on the Corstone-320 MPS4 platform.
    
prerequisites:
    - Basic familiarity with embedded C programming
    - Refer to [Port Zephyr RTOS and run applications on the Arm Corstone-320 MPS4 platform](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_cs320_mps4/) to get knowledge of Zephyr RTOS in Arm Corstone-320 MPS4 Platform.
    - Familiarity with basic machine learning concepts
    - A Corstone-320 MPS4 FPGA development board
    - A Linux development environment, for example Ubuntu 22.04 or later
    - Git and Python


author: Sue Wu

### Tags
skilllevels: Introductory
subjects: IOT
armips:
  - Cortex-M
  - Ethos-U
tools_software_languages:
  - Zephyr
  - Executorch
  - GCC
  - C
operatingsystems:
  - Linux


further_reading:
  - resource:
      title: Zephyr Project documentation
      link: https://docs.zephyrproject.org/latest/index.html
      type: website
  - resource:
      title: ExecuTorch sample applications
      link: https://github.com/pytorch/executorch/tree/main/zephyr/samples
      type: website
  - resource:
      title: Arm Corstone SSE-320 FPGA image for MPS4 (FI101)
      link: https://developer.arm.com/downloads/view/FI101
      type: website
  - resource:
      title: SSE-320 FPGA image for MPS4 application note
      link: https://developer.arm.com/documentation/109762/0100/?lang=en
      type: website
  - resource:
      title: Arm MPS4 FPGA prototyping board technical reference manual
      link: https://developer.arm.com/documentation/102577/latest/
      type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

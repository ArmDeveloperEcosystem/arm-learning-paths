---
title: Deploy a Zephyr-based ML application on Arm Corstone-320 MPS4 with ExecuTorch
description: Deploy a quantized PyTorch model with ExecuTorch in a Zephyr application on Corstone-320 MPS4 and verify inference.

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for embedded software developers who want to deploy a Zephyr-based ML Application on the Arm Corstone-320 MPS4 Platform with ExecuTorch.

learning_objectives: 
    - Set up a Zephyr and ExecuTorch development environment for Corstone-320 MPS4.
    - Quantize and export a PyTorch model for Ethos-U85 neural processing unit (NPU) delegation.
    - Configure and build the Zephyr `hello-executorch` application for Corstone-320 MPS4.
    - Run the application on the MPS4 board and verify machine learning (ML) inference through UART output.
    
prerequisites:
    - Basic familiarity with embedded C programming
    - Basic familiarity with machine learning concepts
    - A Zephyr workspace and board target using Zephyr version V4.3.0 that you prepared by completing the [Port Zephyr RTOS and run applications on the Arm Corstone-320 MPS4 platform](/learning-paths/embedded-and-microcontrollers/zephyr_cs320_mps4/) Learning Path
    - A Corstone-320 MPS4 FPGA development board
    - A Linux development environment, such as Ubuntu 22.04 or later


author: Sue Wu
generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: RTOS Fundamentals
armips:
  - Cortex-M
  - Ethos-U
tools_software_languages:
  - Zephyr
  - ExecuTorch
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

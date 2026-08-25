---
title: Deploy a Zephyr-based machine learning application on Arm Corstone-320 MPS4 with ExecuTorch
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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-25T16:07:56Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 16519943fad3f5bcecb2c1f8101f4ebc9bfd44b3f0f5bb19fd7e74d66ce82060
  summary_generated_at: '2026-08-25T16:07:56Z'
  summary_source_hash: 16519943fad3f5bcecb2c1f8101f4ebc9bfd44b3f0f5bb19fd7e74d66ce82060
  faq_generated_at: '2026-08-25T16:07:56Z'
  faq_source_hash: 16519943fad3f5bcecb2c1f8101f4ebc9bfd44b3f0f5bb19fd7e74d66ce82060
  summary: >-
    You'll deploy a Zephyr machine learning application on the Arm Corstone-320 MPS4 with ExecuTorch.
    First, you'll download the FI101 FPGA image and set up the
    Zephyr and ExecuTorch environment. Next, you'll quantize and export a PyTorch model as a `.pte`
    file for Ethos-U85 delegation. Finally, you'll port `hello-executorch`, configure SRAM-only NPU
    regions, build the application and run it on the MPS4, and verify inference over UART.
  faqs:
  - question: How do I know the MPS4 is using the correct Corstone-320 FPGA image before I build?
    answer: >-
      Confirm the board is running the SSE-320 FI101 image that includes Cortex-M85 and Ethos-U85
      by following the application note and board documentation. Proceed
      only after verifying the image matches the FI101 release you downloaded.
  - question: Which Zephyr board target should I use when configuring the build?
    answer: >-
      Use the `mps4/corstone320/fpga` board target with Zephyr version `V4.3.0`.
  - question: What code change enables the Ethos-U85 NPU region configuration for this application?
    answer: >-
      Override the weak `ethosu_config_select()` function in `ethosu_device_u85.c` to set the
      `QCONFIG` and `REGIONCFG` registers for Ethos-U85. Your override must keep the command stream,
      weights, and scratch data in SRAM for the SRAM-only model.
  - question: What model artifact should I have after quantizing and exporting with ExecuTorch?
    answer: >-
      After quantization and export, you should have the `.pte` model artifact
      `add_u85_1024_sram_only.pte`. Pass it to the Zephyr build with the `-DET_PTE_FILE_PATH` flag,
      as shown in the build command.
  - question: What result should I expect over UART to confirm inference ran?
    answer: >-
      You should see the `hello-executorch` model delegate flow and inference output over UART,
      followed by `SUCCESS: Program complete, exiting`.
# END generated_summary_faq

author: Sue Wu
generate_summary_faq: false
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

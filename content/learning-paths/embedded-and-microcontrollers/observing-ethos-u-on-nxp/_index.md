---
title: Deploy ExecuTorch firmware on NXP FRDM i.MX 93 for Ethos-U65 acceleration

description: Learn how to bring up ExecuTorch executor_runner firmware on the NXP FRDM i.MX 93 Cortex-M33 using Linux RemoteProc, compile .pte models for Ethos-U65, and run inference with NPU acceleration.

minutes_to_complete: 120

who_is_this_for: This is an introductory topic for developers and data scientists new to TinyML who want to observe ExecuTorch performance on a physical device.

learning_objectives:
    - Bring up a custom ExecuTorch `executor_runner` firmware on the FRDM i.MX 93 Cortex-M33 using Linux RemoteProc
    - Compile an ExecuTorch `.pte` model for Ethos-U65 and run inference with NPU acceleration
    - Understand how heterogeneous Arm systems split responsibilities across application cores, microcontrollers, and NPUs
prerequisites:
    - An NXP [FRDM i.MX 93](https://www.nxp.com/design/design-center/development-boards-and-designs/frdm-i-mx-93-development-board:FRDM-IMX93) development board
    - A USB Mini-B to USB Type-A cable, or a USB Mini-B to USB Type-C cable
    - Completion of [Use Linux on an NXP FRDM i.MX 93 board](/learning-paths/embedded-and-microcontrollers/linux-nxp-board/) (Linux setup, login access, and file transfer)
    - Basic knowledge of Machine Learning concepts
    - A host computer to compile ExecuTorch libraries

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:36:25Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: be2b3571d4d2ed75a16bc97589abc22c970d83be868b7e94bb60962a4ba853da
  summary_generated_at: '2026-06-01T21:47:49Z'
  summary_source_hash: be2b3571d4d2ed75a16bc97589abc22c970d83be868b7e94bb60962a4ba853da
  faq_generated_at: '2026-06-02T22:36:25Z'
  faq_source_hash: be2b3571d4d2ed75a16bc97589abc22c970d83be868b7e94bb60962a4ba853da
  summary: >-
    This Learning Path guides you through deploying ExecuTorch on the NXP FRDM i.MX 93 to accelerate
    inference with the Arm Ethos-U65. You will bring up a custom executor_runner firmware on the
    Cortex-M33 using Linux RemoteProc from the Linux-based application processor, compile ExecuTorch
    .pte models for Ethos-U65, and run them on the device. The steps cover board boot and serial
    console access, setting up a consistent build environment (including an Ubuntu container on
    macOS), and building and installing ExecuTorch. You will produce an executor_runner ELF and
    a .pte model and see how these components work across Cortex-A, Cortex-M, and the NPU. Prerequisites
    include the FRDM i.MX 93 board, a USB cable, basic ML knowledge, prior Linux setup on the
    board, and a host computer.
  faqs:
  - question: What do I need before running the steps on the FRDM i.MX 93?
    answer: >-
      You need an NXP FRDM i.MX 93 board, a suitable USB cable, a host computer to compile ExecuTorch
      libraries, and basic ML knowledge. Complete the Learning Path “Use Linux on an NXP FRDM
      i.MX 93 board” to set up Linux, serial console access, and file transfer.
  - question: How should I set up the ExecuTorch build environment on macOS?
    answer: >-
      Use an Ubuntu Docker container on macOS to build ExecuTorch. This container is a build-only
      environment that produces prebuilt ExecuTorch libraries and .pte model files you later move
      onto the FRDM i.MX 93.
  - question: How do I connect to the board’s serial console, especially on macOS?
    answer: >-
      Connect your host to the board’s DEBUG USB-C port and open a serial terminal. On macOS,
      install the Silicon Labs USB-to-UART driver and picocom via Homebrew before connecting.
  - question: How can I verify that ExecuTorch installed correctly in my environment?
    answer: >-
      After running the installation, check that the package is present with: pip list | grep
      executorch. If it appears in the list, the install succeeded.
  - question: Which artifacts do I deploy, and how do they run on this heterogeneous system?
    answer: >-
      Deploy a .pte model compiled for Ethos-U65 and an executor_runner ELF firmware for the Cortex-M33.
      Linux on the Cortex-A side uses RemoteProc to bring up the firmware, which loads the model
      and invokes the NPU for accelerated inference.
# END generated_summary_faq

author: 
- Waheed Brown
- Fidel Makatia Omusilibwa

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A
    - Cortex-M
    - Ethos-U

operatingsystems:
    - Linux
    - macOS

tools_software_languages:
    - Baremetal
    - Python
    - PyTorch
    - ExecuTorch
    - Arm Compute Library
    - GCC

further_reading:
    - resource:
        title: TinyML Brings AI to Smallest Arm Devices
        link: https://newsroom.arm.com/blog/tinyml
        type: blog
    - resource:
        title: Arm Machine Learning Resources
        link: https://www.arm.com/developer-hub/embedded-and-microcontrollers/ml-solutions/getting-started
        type: documentation
    - resource:
        title: Arm Developers Guide for Cortex-M Processors and Ethos-U NPU
        link: https://developer.arm.com/documentation/109267/0101
        type: documentation




### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


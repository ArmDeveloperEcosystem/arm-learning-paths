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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:54Z'
  generator: template
  source_hash: be2b3571d4d2ed75a16bc97589abc22c970d83be868b7e94bb60962a4ba853da
  summary: >-
    Learn how to bring up ExecuTorch executor_runner firmware on the NXP FRDM i.MX 93 Cortex-M33
    using Linux RemoteProc, compile .pte models for Ethos-U65, and run inference with NPU acceleration.
    It is designed for developers and data scientists new to TinyML who want to observe ExecuTorch
    performance on a physical device. By the end, you will be able to bring up a custom ExecuTorch
    `executor_runner` firmware on the FRDM i.MX 93 Cortex-M33 using Linux RemoteProc, compile
    an ExecuTorch `.pte` model for Ethos-U65 and run inference with NPU acceleration, and understand
    how heterogeneous Arm systems split responsibilities across application cores, microcontrollers,
    and NPUs. It focuses on tools and technologies such as Baremetal, Python, PyTorch, ExecuTorch,
    and Arm Compute Library, Linux and macOS environments, and Arm platforms including Cortex-A,
    Cortex-M, and Ethos-U. The main steps cover Understand ExecuTorch deployment on NXP with Ethos-U,
    Boot the NXP FRDM i.MX 93 board, Set up the ExecuTorch build environment, Build and install
    ExecuTorch, and Build ExecuTorch models for Ethos-U65.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will bring up a custom ExecuTorch `executor_runner` firmware on the FRDM i.MX 93 Cortex-M33
      using Linux RemoteProc, compile an ExecuTorch `.pte` model for Ethos-U65 and run inference
      with NPU acceleration, and understand how heterogeneous Arm systems split responsibilities
      across application cores, microcontrollers, and NPUs. Learn how to bring up ExecuTorch executor_runner
      firmware on the NXP FRDM i.MX 93 Cortex-M33 using Linux RemoteProc, compile .pte models
      for Ethos-U65, and run inference with NPU acceleration.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for developers and data scientists new to TinyML who want
      to observe ExecuTorch performance on a physical device.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An NXP [FRDM i.MX 93](https://www.nxp.com/design/design-center/development-boards-and-designs/frdm-i-mx-93-development-board:FRDM-IMX93)
      development board; A USB Mini-B to USB Type-A cable, or a USB Mini-B to USB Type-C cable;
      Completion of [Use Linux on an NXP FRDM i.MX 93 board](/learning-paths/embedded-and-microcontrollers/linux-nxp-board/)
      (Linux setup, login access, and file transfer); Basic knowledge of Machine Learning concepts;
      A host computer to compile ExecuTorch libraries.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Baremetal, Python, PyTorch, ExecuTorch, and Arm
      Compute Library, Linux and macOS environments, and Arm platforms such as Cortex-A, Cortex-M,
      and Ethos-U.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Understand ExecuTorch deployment on NXP with Ethos-U,
      Boot the NXP FRDM i.MX 93 board, Set up the ExecuTorch build environment, Build and install
      ExecuTorch, and Build ExecuTorch models for Ethos-U65.
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


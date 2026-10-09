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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-12T20:13:03Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 9164ae64b157c5326c835b1a260eec0819b19633adb573bc158a41b337b9d388
  summary_generated_at: '2026-08-12T20:13:03Z'
  summary_source_hash: 9164ae64b157c5326c835b1a260eec0819b19633adb573bc158a41b337b9d388
  faq_generated_at: '2026-08-12T20:13:03Z'
  faq_source_hash: 9164ae64b157c5326c835b1a260eec0819b19633adb573bc158a41b337b9d388
  summary: >-
    You'll run an ExecuTorch model on the FRDM i.MX 93 Cortex-M33 with Ethos-U65 acceleration.
    First, you'll prepare a build environment, compile `executor_runner` firmware and a U65-targeted `.pte`
    model. Then, you'll transfer both artifacts to the board. You'll start the firmware from Linux with
    RemoteProc and observe inference across the Cortex-M33 and NPU.
  faqs:
  - question: Which USB connector should I use for the serial console, and what do I need on macOS?
    answer: >-
      Use the DEBUG USB-C connector on the board. On macOS, install the Silicon Labs USB-to-UART
      driver and a serial terminal such as `picocom` (for example, install it with `brew install picocom`).
  - question: Why build ExecuTorch inside a Docker container on macOS?
    answer: >-
      Building inside a Docker container provides an Ubuntu build environment that matches the toolchains used in this Learning Path, and
      avoids gaps in macOS-native cross-compilers. The container is only for building and produces
      prebuilt ExecuTorch libraries and `.pte` files that you'll copy to the FRDM i.MX 93.
  - question: After installing ExecuTorch, how do I confirm the package is available?
    answer: >-
      Run `pip list | grep executorch` and check that `executorch` appears in the output.
  - question: What artifacts must be present before starting the firmware with Linux RemoteProc?
    answer: >-
      Copy the U65-compiled `.pte` model and the `executor_runner` ELF to the board. The runner loads
      the `.pte`, prepares buffers, and invokes the NPU or CPU backend on the Cortex-M33.
  - question: What output should I expect when the MobileNet V2 model compiles successfully?
    answer: >-
      The compilation output reports the number of NPU operators and their coverage. For the example
      MobileNet V2 model, expect an output reporting 100% NPU utilization.
# END generated_summary_faq

author:
    - Waheed Brown
    - Fidel Makatia Omusilibwa

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

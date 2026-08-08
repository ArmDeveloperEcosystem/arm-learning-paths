---
title: Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85
description: Run MNIST digit classification on an Alif Ensemble E8 DevKit with ExecuTorch and Ethos-U85 NPU acceleration, from setup through firmware deployment.

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for embedded developers and ML engineers who want to run TinyML inference on physical hardware with Arm Ethos-U85 NPU acceleration.

learning_objectives:
    - Set up the Alif Ensemble E8 DevKit for ML applications.
    - (Optional) Train, compile and export an MNIST PyTorch model to ExecuTorch .pte format using a Docker container.
    - Configure CMSIS project files, memory layout, and linker scripts for an ML workload on the Alif Ensemble E8.
    - Build and flash firmware to the Alif Ensemble E8 DevKit.
    - Run MNIST digit classification on the Ethos-U85 NPU, and monitor inference results through SEGGER Real-Time Transfer (RTT).

prerequisites:
    - Experience with C or C++ and embedded development concepts
    - Alif [Ensemble E8 Series Development Kit](https://alifsemi.com/ensemble-e8-series/) (contact [Alif Sales](https://alifsemi.com/support/sales-support/))
    - USB Type-C cable for programming
    - A SEGGER J-Link debug probe, included in the DevKit
    - A development machine running Windows, Linux, or macOS with Visual Studio Code installed

author_primary: Waheed Brown

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-06T16:38:27Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a8c3641566a9b8fc3c599a6ea72b54b311f6822f9e761b7de834c37b9a57540b
  summary_generated_at: '2026-08-06T16:38:27Z'
  summary_source_hash: a8c3641566a9b8fc3c599a6ea72b54b311f6822f9e761b7de834c37b9a57540b
  faq_generated_at: '2026-08-06T16:38:27Z'
  faq_source_hash: a8c3641566a9b8fc3c599a6ea72b54b311f6822f9e761b7de834c37b9a57540b
  summary: >-
    You'll run MNIST digit classification on an Alif Ensemble E8 DevKit with ExecuTorch and Ethos-U85
    acceleration. First, you'll connect and configure the board, optionally use Docker to train and export a
    PyTorch model to ExecuTorch `.pte`, and prepare the firmware artifacts. Then, you'll configure CMSIS
    project files, memory layout, and linker scripts, and build and flash the firmware. Finally, you'll
    run inference on the Ethos-U85 NPU and monitor the results with SEGGER Real-Time Transfer.
  faqs:
  - question: What should I check on the DevKit before connecting it to my computer?
    answer: >-
      Before you connect the DevKit, unplug all USB cables before changing any jumpers.  Verify
      that the jumpers match the factory defaults documented in the DK-E8 User Guide. This helps
      you avoid power or boot issues during setup.
  - question: Which USB port do I use for programming, and how do I confirm the board is powered?
    answer: >-
      Connect a USB-C cable to the PRG USB port on the bottom edge of the DevKit. You can confirm
      that the board has power when a green LED illuminates near the E1 device.
  - question: Do I need to set up Docker for this workflow?
    answer: >-
      Use Docker only if you plan to train and export the MNIST model to ExecuTorch format yourself.
      If you use the provided `.pte` file, skip the Docker setup and model export, and proceed to preparing the
      firmware artifacts.
  - question: What files must be ready before building the firmware, and where do they come from?
    answer: >-
      You need `mnist_ethos_u85.pte` and `et_bundle.tar.gz`. If you completed the optional export,
      you can find them in `~/mnist_alif/executorch-alif/output/`. Otherwise, download the provided
      artifacts into your output directory.
  - question: How do I verify that inference is running as expected on the NPU?
    answer: >-
      Run the firmware and monitor its output with SEGGER Real-Time Transfer. You should see the
      firmware load `mnist_ethos_u85.pte`, execute inference on the Ethos-U85 NPU, and report a
      predicted digit in the RTT console.
# END generated_summary_faq

author:
    - Waheed Brown
    - Fidel Makatia Omusilibwa
    - Kwashie Andoh

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false


### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-M
    - Ethos-U

operatingsystems:
    - Linux
    - macOS
    - Windows

tools_software_languages:
    - C
    - CMSIS
    - SEGGER JLink
    - SEGGER RTT
    - GCC
    - Arm Compiler

further_reading:
    - resource:
        title: Introduction to TinyML on Arm using PyTorch and ExecuTorch
        link: /learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/
        type: documentation
    - resource:
        title: Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85
        link: /learning-paths/embedded-and-microcontrollers/alif-image-classification/
        type: documentation
    - resource:
        title: Visualize Ethos-U NPU performance with ExecuTorch on Arm FVPs
        link: /learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/
        type: documentation
    - resource:
        title: Alif Semiconductor Ensemble E8 Series
        link: https://alifsemi.com/ensemble-e8-series/
        type: website
    - resource:
        title: Arm Ethos-U85 NPU
        link: https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u85
        type: website
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

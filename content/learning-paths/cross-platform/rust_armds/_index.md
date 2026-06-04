---
title: Build an Embedded Application with Rust and Debug with Arm Development Studio
minutes_to_complete: 60

description: Learn how to build an embedded Rust application for Arm processors, run it on a Fixed Virtual Platform, and debug it using Arm Development Studio.

who_is_this_for: This is an introductory topic for embedded application developers to get started with Rust.

learning_objectives: 
    - Build an embedded application in Rust.
    - Run the application on a Fixed Virtual Platform (FVP).
    - Debug the application with Arm Development Studio.

prerequisites:
    - An installation of Arm Development Studio.
    - A basic understanding of Rust programming.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:50:10Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f237cd239e5886b21bd5bee88dcd9f95d88eda9a5c2eea363cc9db252e0c6e9f
  summary_generated_at: '2026-06-01T21:16:47Z'
  summary_source_hash: f237cd239e5886b21bd5bee88dcd9f95d88eda9a5c2eea363cc9db252e0c6e9f
  faq_generated_at: '2026-06-02T21:50:10Z'
  faq_source_hash: f237cd239e5886b21bd5bee88dcd9f95d88eda9a5c2eea363cc9db252e0c6e9f
  summary: >-
    This introductory path guides you through building a bare-metal embedded Rust application
    for Armv7-M, running it on a Fixed Virtual Platform, and debugging with Arm Development Studio.
    You will install the Rust compiler with cross-compilation support, build the example, and
    run it on the FVP_MPS2_Cortex-M3 model included with Arm Development Studio. The steps show
    how to launch the FVP with the built binary and verify the runtime output; an option is provided
    to disable visualization to reduce startup time. Prerequisites are an installation of Arm
    Development Studio (license-managed) and a basic understanding of Rust. The path is designed
    to be completed in about 60 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an installation of Arm Development Studio and a basic understanding of Rust programming.
      Arm Development Studio is license-managed.
  - question: Which Arm architecture and FVP model does the example use?
    answer: >-
      The example targets Armv7-M and runs on the FVP_MPS2_Cortex-M3 model that comes with Arm
      Development Studio. Cross-compilation support for the chosen Arm architecture is added following
      the Rust for Embedded Applications Install Guide.
  - question: How do I run the built application on the FVP?
    answer: >-
      Use the FVP provided by Arm Development Studio with the command: FVP_MPS2_Cortex-M3.exe
      -a target/thumbv7m-none-eabi/debug/examples/armds. This launches the model and executes
      the example to completion.
  - question: How can I reduce the FVP start time?
    answer: >-
      Add the option -C fvp_mps2.mps2_visualisation.disable-visualisation=1 to disable visualization.
      This reduces startup time and has no other effect on FVP behavior.
  - question: What result should I expect when the program runs on the FVP?
    answer: >-
      The application should run to completion and print messages similar to "Total sum to 1 is
      1" and "Calculated sum is 1." Seeing this output confirms the run succeeded.
# END generated_summary_faq

author: Ronan Synnott


### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Cortex-R
    - Cortex-M
operatingsystems:
    - Baremetal
tools_software_languages:
    - IP Explorer

### Cross-platform metadata only
shared_path: true
shared_between:
    - embedded-and-microcontrollers

further_reading:
    - resource:
        title: The Embedded Rust Book
        link: https://docs.rust-embedded.org/book/
        type: documentation
    - resource:
        title: Cortex-M Quickstart (Github)
        link: https://github.com/rust-embedded/cortex-m-quickstart
        type: website
    - resource:
        title: Arm Development Studio
        link: https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


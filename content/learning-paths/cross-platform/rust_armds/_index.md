---
title: Build an embedded application with Rust and debug with Arm Development Studio
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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-29T16:47:33Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f237cd239e5886b21bd5bee88dcd9f95d88eda9a5c2eea363cc9db252e0c6e9f
  summary_generated_at: '2026-07-29T16:47:33Z'
  summary_source_hash: f237cd239e5886b21bd5bee88dcd9f95d88eda9a5c2eea363cc9db252e0c6e9f
  faq_generated_at: '2026-07-29T16:47:33Z'
  faq_source_hash: f237cd239e5886b21bd5bee88dcd9f95d88eda9a5c2eea363cc9db252e0c6e9f
  summary: >-
    You'll build a bare-metal Rust example for Armv7-M, run it on an Arm Fixed Virtual Platform (FVP), and
    prepare to debug it with Arm Development Studio. You'll install the tools, compile for the
    `thumbv7m-none-eabi` target, and launch `FVP_MPS2_Cortex-M3` with the binary. Optionally, you can disable
    visualization to shorten startup. You'll verify the calculation from console output, then load the
    same example in Arm Debugger.
  faqs:
  - question: Which Rust target do I build for this example?
    answer: >-
      Build for Armv7-M with the `thumbv7m-none-eabi` target. The run command uses output under
      `target/thumbv7m-none-eabi`.
  - question: Which FVP model should I use to run the application?
    answer: >-
      Use the `FVP_MPS2_Cortex-M3.exe` model included with Arm Development Studio. The example run
      command invokes this executable.
  - question: Where do I point the FVP -a option after building?
    answer: >-
      Point `-a` to the built binary under `target/thumbv7m-none-eabi/debug/examples/armds`. Ensure
      that the path matches your build output directory and example name.
  - question: How do I start the FVP without visualization to reduce startup time?
    answer: >-
      Add `-C fvp_mps2.mps2_visualisation.disable-visualisation=1` to the FVP command. This
      affects only visualization and doesn't change FVP behavior.
  - question: What output should I expect to verify the run completed?
    answer: >-
      The console shows output similar to “Total sum to 1 is 1” and “Calculated sum is 1.” The
      application then runs to completion on the FVP.
# END generated_summary_faq

author: Ronan Synnott

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

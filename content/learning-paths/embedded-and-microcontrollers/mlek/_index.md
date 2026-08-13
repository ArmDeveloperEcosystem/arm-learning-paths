---
title: Build and run the Arm Machine Learning Evaluation Kit examples

description: Learn how to build examples from the Machine Learning Evaluation Kit (MLEK) and run them on the Arm Ecosystem FVP for machine learning application development on microcontrollers.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for embedded software developers interested in machine learning applications.

learning_objectives:
    - Build examples from Machine Learning Evaluation Kit (MLEK)
    - Run the examples on Arm Ecosystem Fixed Virtual Platform (FVP)

prerequisites:
    - Some familiarity with embedded programming
    - A Linux host machine running Ubuntu

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-12T20:11:50Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 16d20cd59e8460c16434ea01a11f40aa68724347e32ae407cebdad051a3ebfa7
  summary_generated_at: '2026-08-12T20:11:50Z'
  summary_source_hash: 16d20cd59e8460c16434ea01a11f40aa68724347e32ae407cebdad051a3ebfa7
  faq_generated_at: '2026-08-12T20:11:50Z'
  faq_source_hash: 16d20cd59e8460c16434ea01a11f40aa68724347e32ae407cebdad051a3ebfa7
  summary: >-
    You'll build machine learning examples from the Arm Machine Learning Evaluation Kit and run
    them on the Corstone-320 FVP. You'll locate generated AXF images, prepare
    the FVP, and launch an image with `-a`. You'll configure the Ethos-U MAC count to match the
    build and verify that the application starts successfully.
  faqs:
  - question: How do I know the build succeeded and where are the output binaries?
    answer: >-
      The build produces `.axf` images in a `cmake-*/bin` directory that reflects your configuration.
      List the files with `ls *.axf` to confirm the outputs exist.
  - question: Which FVP should I install to run these examples?
    answer: >-
      Install the Corstone-320 Ecosystem FVP on your local machine. Download it from the Arm Developer
      website and follow the referenced [Fast Model and FVP install guide](/install-guides/fm_fvp/). 
  - question: How can I shorten a long FVP command line?
    answer: >-
      Put the model configuration options in a file such as `config.txt`. Remove `-C` from each
      option in the file, then pass the file to the FVP with `-f config.txt`.
  - question: How do I load a specific example into the FVP?
    answer: >-
      Use the `-a` option to pass your desired `.axf` image location. Select an image from the `cmake-*/bin`
      directory that matches your build configuration.
  - question: How do I configure Ethos-U for the run, and what must match?
    answer: >-
      Set the NPU MACs using `-C mps4_board.subsystem.ethosu.num_macs` on the FVP command line.
      The number of MACs must match the value used when building the example.
# END generated_summary_faq

author: Ronan Synnott

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### RS: Learning Path hidden until AWS instance updated
draft: false
cascade:
    draft: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-M
    - Ethos-U
    - Corstone
operatingsystems:
    - Baremetal
tools_software_languages:
    - Arm Virtual Hardware
    - FVP
    - GCC
    - Arm Compiler for Embedded

further_reading:
    - resource:
        title: ML Evaluation Kit Quick Start Guide
        link: https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/main/docs/quick_start.md
        type: documentation
    - resource:
        title: Creating ML applications for embedded devices on Arm Virtual Hardware
        link: https://devsummit.arm.com/flow/arm/devsummit22/sessions-catalog/page/sessions/session/1656589322296001Tbrk
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

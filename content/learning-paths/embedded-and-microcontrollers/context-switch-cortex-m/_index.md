---
title: Learn about context switching on Arm Cortex-M processors

description: Learn how to implement context switching operations on Arm Cortex-M processors using the Memory Protection Unit and SysTick exception in a bare-metal environment.

minutes_to_complete: 15

who_is_this_for: This is an introductory topic for software developers who would like to learn about context switching operations on Cortex-M processors in a bare-metal environment.

learning_objectives: 
    - Understand the basics of context switching 
    - Learn how to program the Memory Protection Unit (MPU)
    - Learn how to use the SysTick exception with context switching operations
    - Build and run an example project with Arm Development Studio (Arm DS)

prerequisites:
    - Basic knowledge and familiarity with Cortex-M processors.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:14:04Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0b7a5895a87de83903c223215845b6c840602663838c0682f46e50d139d69c59
  summary_generated_at: '2026-06-01T21:31:37Z'
  summary_source_hash: 0b7a5895a87de83903c223215845b6c840602663838c0682f46e50d139d69c59
  faq_generated_at: '2026-06-02T22:14:04Z'
  faq_source_hash: 0b7a5895a87de83903c223215845b6c840602663838c0682f46e50d139d69c59
  summary: >-
    This introductory path shows how to implement context switching on Arm Cortex-M processors
    in a bare-metal environment using the Memory Protection Unit (MPU) and the SysTick exception.
    You will build and run an open-source example from the Armv8-M Memory Model and MPU User Guide
    repository that demonstrates simple real-time kernel context switching between two threads
    using MPU regions. The workflow uses Arm Development Studio 2022.1 with Arm Compiler for Embedded
    6.18, Fast Models Fixed Virtual Platforms 11.18, and CMSIS 5.8.0. By completing the steps,
    you will understand context switching basics, program the MPU, apply SysTick with context
    switching operations, and successfully build and run the example. Basic familiarity with Cortex-M
    is expected.
  faqs:
  - question: Where do I get the example project used in this Learning Path?
    answer: >-
      The source code is available in the GitHub repository that accompanies the Armv8-M Memory
      Model and MPU User Guide. The example demonstrates simple real-time kernel context switching
      between two threads.
  - question: Which tool versions should I use to build and run the example?
    answer: >-
      Use Arm Development Studio 2022.1, Arm Compiler for Embedded 6.18, Fast Models Fixed Virtual
      Platforms (FVP) 11.18, and CMSIS 5.8.0 as listed in the Learning Path.
  - question: Where is the example intended to run?
    answer: >-
      The example targets a bare-metal environment on Arm Cortex-M processors. The listed tools
      include Fast Models Fixed Virtual Platforms (FVP) 11.18 for running the example.
  - question: How do MPU and SysTick feature in the example?
    answer: >-
      You will program MPU regions and use the SysTick exception as part of the context switching
      operations. The example shows switching between two threads using these features.
  - question: What should I check if the project does not build or run as expected?
    answer: >-
      Confirm you are using the specified tool versions and CMSIS 5.8.0. Also ensure you are building
      the example from the GitHub repository associated with the Armv8-M Memory Model and MPU
      User Guide.
# END generated_summary_faq

author: Uma Ramalingam

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-M
operatingsystems:
    - Baremetal
tools_software_languages:
    - CMSIS
    - Arm Development Studio

further_reading:
    - resource:
        title: Learn the Architecture - M-profile
        link: https://www.arm.com/architecture/learn-the-architecture/m-profile
        type: documentation
    - resource:
        title: Learn the Architecture - M-profile - Open source examples
        link: https://github.com/ARM-software/m-profile-user-guide-examples
        type: Open-source example projects

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


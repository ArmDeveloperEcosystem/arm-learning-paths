---
title: Port Code to Arm Scalable Vector Extension (SVE)

minutes_to_complete: 30   

who_is_this_for: This is an introductory topic for software developers using SIMD instructions for High-Performance Computing, Machine Learning, Digital Signal Processing, Audio and Video Codec applications.

learning_objectives: 
    - Understand the differences between SVE and Neon for vectorization
    - Compile code for SVE-capable Arm processors
    - Run SVE instructions on any Armv8-A processor

prerequisites:
    - General knowledge about SIMD processing, vectorization or Arm Neon.
    - An Arm computer running Linux. Cloud instances can be used, refer to the list of [Arm cloud service providers](/learning-paths/servers-and-cloud-computing/csp/).

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:08:37Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 7b2074e39243a5cd0ccb6a01317c700a4797d8c66353f39aa4197237b6672027
  summary_generated_at: '2026-06-02T05:14:53Z'
  summary_source_hash: 7b2074e39243a5cd0ccb6a01317c700a4797d8c66353f39aa4197237b6672027
  faq_generated_at: '2026-06-03T02:08:37Z'
  faq_source_hash: 7b2074e39243a5cd0ccb6a01317c700a4797d8c66353f39aa4197237b6672027
  summary: >-
    This introductory Learning Path shows how to port SIMD code to Arm Scalable Vector Extension
    (SVE) on Linux. You will compare Neon and SVE to understand how SVE reduces fixed-length vector
    constraints, compile C and Fortran code for SVE-capable Arm processors using the GNU toolchain,
    and run SVE instructions on any Armv8-A system using QEMU or the Arm Instruction Emulator
    (ArmIE) when dedicated SVE hardware is unavailable. You will build and run a small example
    and inspect compiler vectorization via disassembly. Prerequisites are general SIMD or Arm
    Neon knowledge and access to an Arm Linux machine; cloud instances from AWS, Microsoft Azure,
    Google Cloud, or Oracle can be used. Estimated time to complete is about 30 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need general knowledge of SIMD processing and Arm Neon, and access to an Arm computer
      running Linux. Arm-based cloud instances can be used; see the listed cloud service providers.
  - question: Which GCC options enable SVE for my build?
    answer: >-
      Use -march=armv8-a+sve when compiling (for example, gcc -march=armv8-a+sve myapp.c -o myapp_c.out
      or gfortran -march=armv8-a+sve myapp.f90 -o myapp_f90.out). Autovectorization with GCC is
      enabled with -O3 and can be disabled with -fno-tree-vectorize.
  - question: How can I run SVE instructions if my system lacks SVE hardware?
    answer: >-
      Use QEMU or the Arm Instruction Emulator (ArmIE). The path demonstrates both approaches
      on an Armv8-A system running Ubuntu 22.04 without SVE support.
  - question: How do I know if the compiler vectorized my code?
    answer: >-
      The steps have you compare the disassembly of a simple program with and without autovectorization
      enabled. You should observe differences in the generated code when building with -O3 versus
      disabling vectorization.
  - question: What should I consider when moving from Neon to SVE?
    answer: >-
      Neon uses 32 fixed 128-bit vector registers (V0–V31) for integer and floating-point types,
      while SVE reduces restrictions related to fixed-length vector sizes. The path introduces
      these differences to guide porting decisions.
# END generated_summary_faq

author: Florent Lebeau

### Tags
skilllevels: Introductory
subjects: ML
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
armips:
    - Neoverse
    - Cortex-A
operatingsystems:
    - Linux
tools_software_languages:
    - SVE
    - Neon
    - armie
    - GCC
    - armclang
    - Runbook

further_reading:
    - resource:
        title: Introduction to SVE
        link: https://developer.arm.com/documentation/102476/latest/
        type: website
    - resource:
        title: SVE Optimization Guide
        link: https://developer.arm.com/documentation/102699/0100/?lang=en
        type: documentation
    - resource:
        title: Tutorials - Introduction to SVE2
        link: https://developer.arm.com/documentation/102340/0001/?lang=en
        type: documentation
    - resource:
        title: Arm Instruction Emulator user guide
        link: https://developer.arm.com/documentation/102190/22-0/Get-started/Get-started-with-Arm-Instruction-Emulator
        type: documentation
    - resource:
        title: Accelerating DSP functions with dot product instructions
        link: https://developer.arm.com/documentation/102651/a/?lang=en
        type: documentation
    - resource:
        title: Optimizing HPCG for Arm SVE
        link: https://developer.arm.com/community/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/optimizing-hpcg-for-arm-sve
        type: blog



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


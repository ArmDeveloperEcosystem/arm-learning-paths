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

generate_summary_faq: true

# rerun_summary: false
# rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:59Z'
  generator: template
  source_hash: 7b2074e39243a5cd0ccb6a01317c700a4797d8c66353f39aa4197237b6672027
  summary: >-
    Port Code to Arm Scalable Vector Extension (SVE) walks you through an end-to-end Arm software
    workflow. It is designed for software developers using SIMD instructions for High-Performance
    Computing, Machine Learning, Digital Signal Processing, Audio and Video Codec applications.
    By the end, you will be able to understand the differences between SVE and Neon for vectorization,
    compile code for SVE-capable Arm processors, and run SVE instructions on any Armv8-A processor.
    It focuses on tools and technologies such as SVE, Neon, armie, GCC, and armclang, Linux environments,
    Arm platforms including Neoverse and Cortex-A, and cloud platforms such as AWS, Microsoft
    Azure, Google Cloud, and Oracle. The main steps cover From Arm Neon to SVE, Compile for SVE,
    and Run SVE without capable hardware.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will understand the differences between SVE and Neon for vectorization, compile code
      for SVE-capable Arm processors, and run SVE instructions on any Armv8-A processor.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for software developers using SIMD instructions for High-Performance
      Computing, Machine Learning, Digital Signal Processing, Audio and Video Codec applications.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: General knowledge about SIMD processing,
      vectorization or Arm Neon.; An Arm computer running Linux. Cloud instances can be used,
      refer to the list of [Arm cloud service providers](/learning-paths/servers-and-cloud-computing/csp/).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including SVE, Neon, armie, GCC, and armclang, Linux environments,
      Arm platforms such as Neoverse and Cortex-A, and cloud platforms such as AWS, Microsoft
      Azure, Google Cloud, and Oracle.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around From Arm Neon to SVE, Compile for SVE, and Run SVE
      without capable hardware.
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


---
title: Learn about optimization techniques using the g++ compiler
description: Learn how to apply g++ compiler optimization techniques and flags to improve C++ application performance on Arm systems with hands-on examples.

minutes_to_complete: 60

who_is_this_for: This Learning Path is for beginner C++ developers who are looking to optimize applications on Arm-based cloud instances using compiler flags. 

learning_objectives: 
    - Compile a C++ program for a specific Arm target.
    - Use compiler flags to manage optimizations.

prerequisites:
    - Basic understanding of C++
    - Basic understanding of compilers

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-27T18:45:15Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 22f845b8ea4dbb9ffc63fafb76c17c79aedde14a28417d49e1ab0833bbbc1eba
  summary_generated_at: '2026-07-27T18:45:15Z'
  summary_source_hash: 22f845b8ea4dbb9ffc63fafb76c17c79aedde14a28417d49e1ab0833bbbc1eba
  faq_generated_at: '2026-07-27T18:45:15Z'
  faq_source_hash: 22f845b8ea4dbb9ffc63fafb76c17c79aedde14a28417d49e1ab0833bbbc1eba
  summary: >-
    You'll compile and tune a C++ application with `g++` on an Arm Neoverse-based Linux system.
    You'll inspect the CPU with `lscpu`, choose between `-march` for portability and `-mcpu` for
    processor-specific tuning, and consider size-sensitive container builds. You'll build and run
    the example, then learn to make flag choices based on portability, binary size, and performance.
  faqs:
  - question: How do I confirm the Arm CPU model on the instance before choosing flags?
    answer: >-
      Run `lscpu | grep -i model` and look for a `Model name` line such as `Neoverse-*`. If `lscpu`
      omits the model name, use the tip in the step to read the CPU part number.
  - question: Which compiler flag should I use for portability versus CPU-specific tuning?
    answer: >-
      Use `-march=` with a value that matches the lowest Arm architecture across your target
      systems for portability. Use `-mcpu=` to tune for a specific processor when you plan to run only on
      that CPU.
  - question: Do I have to use an AWS Graviton 4-based instance?
    answer: >-
      No. Any Neoverse-based system running Ubuntu 24.04 LTS works, including the examples mentioned.
      The workflow assumes an Arm-native environment on such a system.
  - question: What should I do if I’m deploying in a memory-constrained container?
    answer: >-
      Optimize for size as outlined in the example step. Choose compiler options that reduce binary
      size and accept the trade-offs they introduce.
  - question: What result should I expect after building and running the example?
    answer: >-
      The program should compile and run on the Arm instance. A portable build using `-march` is
      intended to run on other Arm servers that meet that baseline, while a CPU-tuned build targets
      the specified processor.
# END generated_summary_faq

author: Kieran Hejmadi

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
armips:
    - Neoverse
tools_software_languages:
    - CPP
    - Runbook
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Runtime Detection of CPU features 
        link: https://community.arm.com/arm-community-blogs/b/operating-systems-blog/posts/runtime-detection-of-cpu-features-on-an-armv8-a-cpu
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

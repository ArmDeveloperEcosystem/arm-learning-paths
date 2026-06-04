---
title: Learn about the C++ memory model for porting applications to Arm
description: Learn how to write correct concurrent C++ code when porting applications from x86 to Arm by understanding memory ordering differences and using best practices to avoid race conditions.

minutes_to_complete: 45

who_is_this_for: This is an advanced topic for C++ developers porting applications from x86 to Arm and optimizing performance.

learning_objectives: 
    - Describe at a high level what a memory model does, and the types of memory ordering.
    - Describe the differences between the Arm and x86 memory model.
    - Employ best practices for writing C++ on Arm to avoid race conditions.

prerequisites:
    - Access to an x86 and an Arm cloud instance (virtual machine).
    - Proficiency in C++ programming.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:18:10Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3a4bc8b2ab548be507b6d528844b0593b27f2dab3ab3c9649e807abdf4887ce0
  summary_generated_at: '2026-06-02T03:06:00Z'
  summary_source_hash: 3a4bc8b2ab548be507b6d528844b0593b27f2dab3ab3c9649e807abdf4887ce0
  faq_generated_at: '2026-06-03T00:18:10Z'
  faq_source_hash: 3a4bc8b2ab548be507b6d528844b0593b27f2dab3ab3c9649e807abdf4887ce0
  summary: >-
    This Learning Path helps experienced C++ developers port concurrent code from x86 to Arm by
    explaining the C++ memory model, highlighting key memory ordering differences, and demonstrating
    how subtle races can appear on Arm. You will run a simple race condition example on both x86
    and Arm cloud instances (Linux), with an example using an Arm-based AWS t4g.xlarge instance
    running Ubuntu 22.04 LTS, though other instance types can be used. You will use ThreadSanitizer
    (TSan) to detect infrequent data races and learn best practices for writing correct C++ on
    Arm. Prerequisites include access to both an x86 and an Arm VM and proficiency in C++. Estimated
    time to complete is about 45 minutes.
  faqs:
  - question: What do I need before running the example?
    answer: >-
      You need access to both an x86 and an Arm cloud instance (virtual machine) and proficiency
      in C++ programming. The Learning Path assumes a Linux environment.
  - question: Which Arm instance and OS are used in the walkthrough?
    answer: >-
      The example uses an AWS t4g.xlarge instance running Ubuntu 22.04 LTS. You can use other
      Arm instance types if preferred.
  - question: Which compiler/toolchain should I use for ThreadSanitizer (TSan)?
    answer: >-
      Use a recent version of the clang toolchain that includes TSan support. TSan instruments
      the code at compile time to detect data races.
  - question: How do I know if the race condition has been reproduced?
    answer: >-
      Expect differences in program behavior between x86 and Arm due to memory ordering, as illustrated
      by the example. When you run with TSan, it will report data races if they are present, including
      details to help you debug.
  - question: What operating system is assumed for this Learning Path?
    answer: >-
      Linux is the target operating system. The example specifically references Ubuntu 22.04 LTS
      on an Arm instance.
# END generated_summary_faq

author: Kieran Hejmadi

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - CPP
    - TSan
    - Runbook
operatingsystems:
    - Linux
   
further_reading:
    - resource:
        title: C++ Memory Order Reference Manual 
        link: https://en.cppreference.com/w/cpp/atomic/memory_order
        type: documentation
    - resource:
        title: Thread Sanitizer Manual 
        link: https://github.com/google/sanitizers/wiki/threadsanitizercppmanual
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


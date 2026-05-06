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

# rerun_summary: false
# rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:56Z'
  generator: template
  source_hash: 3a4bc8b2ab548be507b6d528844b0593b27f2dab3ab3c9649e807abdf4887ce0
  summary: >-
    Learn how to write correct concurrent C++ code when porting applications from x86 to Arm by
    understanding memory ordering differences and using best practices to avoid race conditions.
    It is designed for C++ developers porting applications from x86 to Arm and optimizing performance.
    By the end, you will be able to describe at a high level what a memory model does, and the
    types of memory ordering, describe the differences between the Arm and x86 memory model, and
    employ best practices for writing C++ on Arm to avoid race conditions. It focuses on tools
    and technologies such as CPP, TSan, and Runbook, Linux environments, and Arm platforms including
    Neoverse. The main steps cover Introduction to C++ Memory Models, The C++ Memory Model and
    Atomics, Walk through a Race condition example, and Detecting race conditions.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will describe at a high level what a memory model does, and the types of memory ordering,
      describe the differences between the Arm and x86 memory model, and employ best practices
      for writing C++ on Arm to avoid race conditions. Learn how to write correct concurrent C++
      code when porting applications from x86 to Arm by understanding memory ordering differences
      and using best practices to avoid race conditions.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for C++ developers porting applications from x86 to Arm and optimizing
      performance.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: Access to an x86 and an Arm cloud instance
      (virtual machine).; Proficiency in C++ programming.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including CPP, TSan, and Runbook, Linux environments, and
      Arm platforms such as Neoverse.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Introduction to C++ Memory Models, The C++ Memory
      Model and Atomics, Walk through a Race condition example, and Detecting race conditions.
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


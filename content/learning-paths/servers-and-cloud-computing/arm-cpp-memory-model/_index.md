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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-26T17:26:18Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3a4bc8b2ab548be507b6d528844b0593b27f2dab3ab3c9649e807abdf4887ce0
  summary_generated_at: '2026-06-26T17:26:18Z'
  summary_source_hash: 3a4bc8b2ab548be507b6d528844b0593b27f2dab3ab3c9649e807abdf4887ce0
  faq_generated_at: '2026-06-26T17:26:18Z'
  faq_source_hash: 3a4bc8b2ab548be507b6d528844b0593b27f2dab3ab3c9649e807abdf4887ce0
  summary: >-
    You'll explore the C++ memory model, see how compiler and hardware reordering
    interact with multithreaded code, and compare Arm and x86 memory ordering. First, you'll examine atomics
    and memory ordering concepts before running a small concurrent C++ example on both x86 and
    Arm cloud instances to expose a race that can appear differently across architectures. Then, you'll detect data races with ThreadSanitizer (TSan) and use its diagnostic output to guide fixes.
    By the end, you'll be able to recognize code that relies on implicit x86 ordering and apply C++ best
    practices to write correct, portable concurrency for Arm.
  faqs:
  - question: Do I have to use the exact instance type shown in the example?
    answer: >-
      No. The example uses an Arm-based AWS `t4g.xlarge` instance, but other instance types can
      be used.
  - question: What result should I expect when I run the race condition example on x86 and Arm?
    answer: >-
      Code with a latent race can appear to work on x86 but exhibit different or nondeterministic
      behavior on Arm due to memory ordering differences. The example is designed to make this
      contrast visible.
  - question: Which compiler should I use to run ThreadSanitizer (TSan)?
    answer: >-
      Use a recent version of the `clang` compiler that includes ThreadSanitizer. TSan instruments
      your program at compile time and reports potential data races at runtime.
  - question: Why does my program run slower when built with TSan?
    answer: >-
      TSan adds instrumentation and runtime checks, which introduce significant overhead. Use
      TSan builds for debugging data races, not for measuring performance.
  - question: What should I check if code that seemed correct on x86 behaves differently on Arm?
    answer: >-
      Don't assume x86 memory ordering semantics on Arm. Revisit the code with the C++ memory
      model in mind and use atomics and proper synchronization instead of relying on implicit
      ordering.
# END generated_summary_faq

author: Kieran Hejmadi

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

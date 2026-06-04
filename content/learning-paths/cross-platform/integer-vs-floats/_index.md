---
title: Learn about integer and floating-point conversions

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for C/C++ developers who are interested in learning about the intricacies of conversions between floating-point numbers and integers.

description: Learn how to identify and fix potential problems with integer and floating-point conversions in C/C++ code on Arm, including explicit conversions, implicit conversions, and type demotion issues.

learning_objectives: 
    - Learn how to identify and fix potential problems in integer/float conversions in C/C++ on Arm

prerequisites:
    - An Arm computer running Linux and a recent version of a C++ compiler (Clang or GCC) installed

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:41:57Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 1895767d551ba0fa249c5002d3e2e471acacdec06ddb7c2f5314a2fa0df94f2e
  summary_generated_at: '2026-06-01T21:07:38Z'
  summary_source_hash: 1895767d551ba0fa249c5002d3e2e471acacdec06ddb7c2f5314a2fa0df94f2e
  faq_generated_at: '2026-06-02T21:41:57Z'
  faq_source_hash: 1895767d551ba0fa249c5002d3e2e471acacdec06ddb7c2f5314a2fa0df94f2e
  summary: >-
    This Learning Path teaches advanced C/C++ developers on Arm how to identify and fix issues
    in integer and floating-point conversions. Using an Arm computer running Linux with a recent
    GCC or Clang, you will review data type ranges, explore explicit and implicit conversions,
    and examine data type demotions. You will implement concise examples—a Fibonacci-based golden
    ratio calculator in C and a C++ demotion test—to see where conversions and narrowing can change
    results. By the end, you will be able to recognize risky conversions and decide when to use
    explicit casts or different types on AArch64 (Armv8-A/Armv9-A). The estimated time to complete
    is about 30 minutes.
  faqs:
  - question: What do I need before running the examples?
    answer: >-
      You need an Arm computer running Linux and a recent version of a C++ compiler, either Clang
      or GCC. No additional prerequisites are explicitly listed.
  - question: Which compiler should I use and are any specific flags required?
    answer: >-
      You can use either GCC or Clang on Linux. The Learning Path does not specify compiler flags;
      the focus is on understanding code behavior around conversions.
  - question: How do I know the golden_ratio.c program worked?
    answer: >-
      The program computes the golden ratio from consecutive Fibonacci numbers, so the output
      should approach 1.618033988749894 as N increases. Compare the printed results to this value
      to gauge correctness.
  - question: What should I check if I see unexpected truncation or loss of precision?
    answer: >-
      Look for demotions, such as assigning a wider type to a narrower one (for example, double
      to float or 64-bit to 16-bit) or performing integer division where floating-point was intended.
      Remember that demotions are not detected in C and only in a few cases in C++, so verify
      variable types against the ranges reviewed earlier.
  - question: Which Arm platforms and operating system does this target?
    answer: >-
      The path targets AArch64 on Armv8-A and Armv9-A and assumes a Linux environment. The examples
      are designed to be compiled and run on this setup.
# END generated_summary_faq

author: Konstantinos Margaritis

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Aarch64
    - Armv8-a
    - Armv9-a
tools_software_languages:
    - GCC
    - Clang
    - Runbook

operatingsystems:
    - Linux
shared_path: true
shared_between:
    - laptops-and-desktops
    - servers-and-cloud-computing
    - mobile-graphics-and-gaming


further_reading:
    - resource:
        title: Arm Neoverse™ N1 Software Optimization Guide
        link: https://developer.arm.com/documentation/PJDOC-466751330-9707/r4p1/?lang=en
        type: documentation
    - resource:
        title: Arm Neoverse N2 Software Optimization Guide
        link: https://developer.arm.com/documentation/PJDOC-466751330-18256/0003/?lang=en
        type: documentation
    - resource:
        title: Data Types in C - Integer, Floating Point, and Void Explained
        link: https://www.freecodecamp.org/news/data-types-in-c-integer-floating-point-and-void-explained/
        type: website
    - resource:
        title: Half-precision floating-point format
        link: https://en.wikipedia.org/wiki/Half-precision_floating-point_format
        type: website
    - resource:
        title: bfloat16 floating-point format
        link: https://en.wikipedia.org/wiki/Bfloat16_floating-point_format
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


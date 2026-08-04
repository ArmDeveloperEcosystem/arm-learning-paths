---
title: Learn about integer and floating-point conversions

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for C/C++ developers who are interested in learning about the intricacies of conversions between floating-point numbers and integers.

description: Learn how to identify and fix potential problems with integer and floating-point conversions in C/C++ code on Arm, including explicit conversions, implicit conversions, and type demotion issues.

learning_objectives: 
    - Learn how to identify and fix potential problems in integer/float conversions in C/C++ on Arm

prerequisites:
    - An Arm computer running Linux and a recent version of a C++ compiler (Clang or GCC) installed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-29T16:37:05Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 1895767d551ba0fa249c5002d3e2e471acacdec06ddb7c2f5314a2fa0df94f2e
  summary_generated_at: '2026-07-29T16:37:05Z'
  summary_source_hash: 1895767d551ba0fa249c5002d3e2e471acacdec06ddb7c2f5314a2fa0df94f2e
  faq_generated_at: '2026-07-29T16:37:05Z'
  faq_source_hash: 1895767d551ba0fa249c5002d3e2e471acacdec06ddb7c2f5314a2fa0df94f2e
  summary: >-
    You'll explore how C and C++ convert integers and floating-point values on Arm Linux, and how those
    conversions affect correctness. You'll review numeric ranges, compare explicit and implicit conversions,
    and run short programs that expose integer-division and narrowing pitfalls. You'll also compare C++
    list-initialization diagnostics with C's permissive behavior, then adjust types or add explicit casts
    to produce the intended results.
  faqs:
  - question: How do I build the examples?
    answer: >-
      Compile the C source as C and the C++ source as C++ with a recent GCC or Clang on your
      Arm Linux system. Run the binaries and compare their output. A narrowing diagnostic from the
      C++ brace-initialization example is expected.
  - question: What result should I expect from the golden ratio program?
    answer: >-
      The ratio approaches 1.6180339887… as the Fibonacci index increases. If the output stays at
      whole numbers or fails to converge, check for integer division and promote one operand to a
      floating-point type.
  - question: How do I know an implicit conversion is changing my calculation?
    answer: >-
      Inspect the operand types in each expression. Two integer operands produce integer arithmetic,
      so promote one value or cast it to `float` or `double` when you need a fractional result.
  - question: Why does the C++ demotion example behave differently with braces?
    answer: >-
      C++ list initialization with braces can diagnose narrowing conversions at compile time, so
      `float z{w}` can produce a diagnostic. An assignment such as `float y = w` usually compiles
      and truncates the value at runtime.
  - question: What should I change if the demotion test prints unexpected values?
    answer: >-
      Use a wider destination type for intermediate results when you need to preserve range and
      precision. Add an explicit conversion only when truncation is intentional, then rebuild and
      recheck the output.
# END generated_summary_faq

author: Konstantinos Margaritis

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

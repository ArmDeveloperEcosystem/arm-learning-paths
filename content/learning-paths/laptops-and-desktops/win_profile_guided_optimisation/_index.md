---
title: Optimize C++ applications on Windows on Arm using Profile-Guided Optimization

description: Learn how to apply Profile-Guided Optimization (PGO) to build performance-tuned C++ binaries and measure improvements using Google Benchmark on Windows on Arm.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers who want to optimize C++ application performance on Windows on Arm using Profile-Guided Optimization (PGO).

learning_objectives: 
    - Microbenchmark a function using Google Benchmark
    - Apply profile-guided optimization to build performance-tuned binaries for Windows on Arm
    - Measure and compare performance improvements from PGO-optimized builds

prerequisites:
    - Familiarity with C++ development and compiling programs from the command line
    - A Windows on Arm machine with [Visual Studio](/install-guides/vs-woa/) and the C++ desktop development tools installed

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:29:33Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b975cc83674410ec50ca49a31744eee4ac5a63c994dd28e46ed84f7afda0568d
  summary_generated_at: '2026-06-01T22:18:09Z'
  summary_source_hash: b975cc83674410ec50ca49a31744eee4ac5a63c994dd28e46ed84f7afda0568d
  faq_generated_at: '2026-06-02T23:29:33Z'
  faq_source_hash: b975cc83674410ec50ca49a31744eee4ac5a63c994dd28e46ed84f7afda0568d
  summary: >-
    This Learning Path guides you through applying Profile-Guided Optimization (PGO) to C++ code
    and measuring the impact with Google Benchmark on Windows on Arm. You start by understanding
    PGO fundamentals, then create a baseline microbenchmark of an integer division function. Using
    MSVC on a Windows on Arm system, you build an instrumented binary, run it to collect profile
    data, and rebuild using that profile to produce a PGO-optimized binary. You then compare benchmark
    results between the baseline and optimized builds. Prerequisites are C++ command-line experience
    and a Windows on Arm machine with Visual Studio and the C++ desktop development tools installed.
    Estimated time: about 30 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Windows on Arm machine with Visual Studio and the C++ desktop development tools
      installed. Familiarity with C++ and compiling from the command line is expected.
  - question: Which build environment should I use on Windows on Arm?
    answer: >-
      Open an ARM64 Native Tools Command Prompt and use PowerShell if instructed. Navigate to
      your project directory and set any environment variables (such as VCPKG) as shown in the
      steps.
  - question: What does the baseline benchmark measure, and why was it chosen?
    answer: >-
      The baseline measures an integer division operation. Division is used because it typically
      has higher latency and lower throughput than addition, subtraction, or multiplication, making
      changes measurable.
  - question: How do I apply PGO here, and how do I know it worked?
    answer: >-
      You build an instrumented binary, run it to collect profile data, and rebuild using that
      profile with MSVC. You then run Google Benchmark to compare the optimized build against
      the baseline and observe the measured differences.
  - question: Do I need to install Google Benchmark before starting?
    answer: >-
      No. The path first introduces Google Benchmark, then guides you through setting up your
      environment and running your first benchmark in the following section.
# END generated_summary_faq

author: Tom Dunkle

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
tools_software_languages:
    - C
    - MSVC
    - Google Benchmark
    - PGO
operatingsystems:
    - Windows
armips:
    - Cortex-A

further_reading:
    - resource:
        title: MSVC profile-guided optimization documentation
        link: https://learn.microsoft.com/en-us/cpp/build/profile-guided-optimizations?view=msvc-170
        type: documentation
    - resource:
        title: Google Benchmark Library 
        link: https://github.com/google/benchmark
        type: documentation
    - resource:
        title: Windows on Arm developer documentation
        link: https://learn.microsoft.com/en-us/windows/arm/overview
        type: documentation
    - resource:
        title: Arm performance optimization resources
        link: https://learn.arm.com/learning-paths/laptops-and-desktops/
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


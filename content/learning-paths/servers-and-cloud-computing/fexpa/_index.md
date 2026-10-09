---
title: Optimize exponential functions with FEXPA
description: Learn how to implement exponential functions using Arm SVE intrinsics with the FEXPA instruction for hardware-accelerated computations on Neoverse processors.

minutes_to_complete: 15

who_is_this_for: This is an introductory topic for developers interested in accelerating exponential function computations using Arm's Scalable Vector Extension (SVE). The Floating Point Exponential Accelerator (FEXPA) instruction provides hardware acceleration for exponential calculations on Arm Neoverse processors.

learning_objectives: 
    - Implement the exponential function using SVE intrinsics
    - Optimize the function with FEXPA

prerequisites:
    - Access to an [AWS Graviton4, Google Axion, or Azure Cobalt 100 virtual machine from a cloud service provider](/learning-paths/servers-and-cloud-computing/csp/)
    - Some familiarity with SIMD programming and SVE intrinsics

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-10T21:56:41Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 563340ba17896ecf0cf53113038c7662873abfbf67998475241444c888ccc480
  summary_generated_at: '2026-09-10T21:56:41Z'
  summary_source_hash: 563340ba17896ecf0cf53113038c7662873abfbf67998475241444c888ccc480
  faq_generated_at: '2026-09-10T21:56:41Z'
  faq_source_hash: 563340ba17896ecf0cf53113038c7662873abfbf67998475241444c888ccc480
  summary: >-
    You'll implement an exponential function with Arm SVE intrinsics, starting with range reduction and polynomial approximation. First, you'll select an approximation interval, choose a polynomial degree, and validate your result against a reference. Then, you'll use the SVE FEXPA instruction for hardware-assisted reconstruction, reducing the polynomial work while preserving accuracy for your performance-sensitive Neoverse code.
  faqs:
  - question: How do I compile the SVE example?
    answer: >-
      Install `gcc`, then compile `exp_sve.c` with `gcc -O3 -march=armv8-a+sve exp_sve.c -o exp_sve -lm`.
      Use an SVE-capable Arm processor to execute the SVE implementation.
  - question: Which floating-point precision am I building with in this example?
    answer: >-
      The provided implementation uses single precision: its coefficients are `float` values and
      its SVE vectors use `svfloat32_t`. The example therefore builds the FP32 version described in
      the precision table.
  - question: When should I switch my code from the polynomial-only version to the FEXPA-optimized
      version?
    answer: >-
      After the baseline SVE polynomial version compiles and produces correct results, replace
      the range-reduction sequence with the FEXPA-based approach. Re-validate accuracy against your target error before continuing.
  - question: What result should I expect after I enable FEXPA?
    answer: >-
      FEXPA performs table lookup and bit manipulation in hardware, which lets you use a lower-degree
      polynomial for the same target precision. Confirm this by checking approximation error over
      a representative input range.
  - question: How do I choose my polynomial degree and input range?
    answer: >-
      Use range reduction to map inputs into an interval where the polynomial is accurate, then
      tune the polynomial degree to meet your error goal. Evaluate absolute or relative error
      across representative inputs before finalizing the choice.
# END generated_summary_faq

author:
    - Arnaud Grasset
    - Claudio Martino
    - Alexandre Romana

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

further_reading:
    - resource:
        title: Arm Optimized Routines
        link: https://github.com/ARM-software/optimized-routines
        type: website
    - resource:
        title: Scalable Vector Extensions documentation
        link: https://developer.arm.com/Architectures/Scalable%20Vector%20Extensions
        type: documentation
    - resource:
        title: FEXPA documentation
        link: https://developer.arm.com/documentation/ddi0602/2025-12/SVE-Instructions/FEXPA--Floating-point-exponential-accelerator-?lang=en
        type: documentation

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
platforms:
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
armips:
    - Neoverse
operatingsystems:
    - Linux
    - macOS
tools_software_languages:
    - C
    - CPP

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

---
title: Optimize exponential functions with FEXPA
description: Learn how to implement exponential functions using Arm SVE intrinsics with the FEXPA instruction for hardware-accelerated computations on Neoverse processors.

    
minutes_to_complete: 15

who_is_this_for: This is an introductory topic for developers interested in accelerating exponential function computations using Arm's Scalable Vector Extension (SVE). The FEXPA instruction provides hardware acceleration for exponential calculations on Arm Neoverse processors.

learning_objectives: 
    - Implement the exponential function using SVE intrinsics
    - Optimize the function with FEXPA

prerequisites:
    - Access to an [AWS Graviton4, Google Axion, or Azure Cobalt 100 virtual machine from a cloud service provider](/learning-paths/servers-and-cloud-computing/csp/)
    - Some familiarity with SIMD programming and SVE intrinsics

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:51:30Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a67c552b76df6323eccc331c9146d0fcbdb8ad222fe81dbf2e1c2339c7609b61
  summary_generated_at: '2026-06-02T03:49:04Z'
  summary_source_hash: a67c552b76df6323eccc331c9146d0fcbdb8ad222fe81dbf2e1c2339c7609b61
  faq_generated_at: '2026-06-03T00:51:30Z'
  faq_source_hash: a67c552b76df6323eccc331c9146d0fcbdb8ad222fe81dbf2e1c2339c7609b61
  summary: >-
    Learn how to implement the exponential function on Arm Neoverse processors using SVE intrinsics
    and then refine it with the FEXPA instruction. You will review range reduction and polynomial
    approximation trade-offs, write a C implementation with SVE intrinsics, and build it with
    gcc on a cloud VM. The path lists Linux and macOS, shows installing gcc on Linux, and was
    tested on an AWS Graviton4 r8g.medium instance. You will apply FEXPA to reduce the polynomial
    degree needed for a target precision, with SME support noted for integrating the approximation
    into matrix computation paths. Prerequisites include access to an AWS Graviton4, Google Axion,
    or Azure Cobalt 100 VM and some familiarity with SIMD programming and SVE intrinsics.
  faqs:
  - question: What do I need before running the example?
    answer: >-
      You need access to an AWS Graviton4, Google Axion, or Azure Cobalt 100 virtual machine,
      plus some familiarity with SIMD programming and SVE intrinsics. The path uses gcc on Linux
      or macOS.
  - question: Which instance type should I pick, and what was used to validate the steps?
    answer: >-
      You can use an Arm-based VM from AWS Graviton4, Google Axion, or Azure Cobalt 100. The steps
      were tested on an AWS Graviton4 r8g.medium instance.
  - question: How do I set up the build environment and source file?
    answer: >-
      Install gcc; the steps show using apt on Linux to install it. Then create the exp_sve.c
      file with the provided SVE-based implementation.
  - question: What changes when I enable FEXPA compared to the initial SVE implementation?
    answer: >-
      You begin with a polynomial approximation using SVE intrinsics, then apply FEXPA for hardware-accelerated
      exponential computation. With FEXPA, the approximation can reach a specified target precision
      using a lower-degree polynomial than alternative implementations.
  - question: I’m on macOS—what should I do if the Linux package commands don’t work?
    answer: >-
      macOS is listed as supported, but the explicit setup commands use Linux’s apt. Use a C compiler
      available on macOS; the path does not provide macOS-specific install commands.
# END generated_summary_faq

author: 
- Arnaud Grasset
- Claudio Martino
- Alexandre Romana

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
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
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


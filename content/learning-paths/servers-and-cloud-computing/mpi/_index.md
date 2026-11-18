---
title: Get started with parallel application development

minutes_to_complete: 30   

who_is_this_for: This is an advanced topic for high-performance computing software developers writing MPI applications.

description: Debug, profile, and optimize MPI parallel applications on Arm servers using Linaro Forge, gdb, and Arm Performance Libraries.

learning_objectives: 
    - Debug and fix a parallel application
    - Profile and optimize your code
    - Use optimized routines for common math operations

prerequisites:
    - General knowledge about distributed parallelism (MPI)
    - Some understanding of C, Python, and Linux commands
    - An Arm computer running Linux. Cloud instances can be used, refer to the list of [Arm cloud service providers](/learning-paths/servers-and-cloud-computing/csp/).

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-28T19:53:27Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 1792620763f82898a3b9f5286c06cc7ad5c8e9b16aae443dc64094c74991b3e9
  summary_generated_at: '2026-09-28T19:53:27Z'
  summary_source_hash: 1792620763f82898a3b9f5286c06cc7ad5c8e9b16aae443dc64094c74991b3e9
  faq_generated_at: '2026-09-28T19:53:27Z'
  faq_source_hash: 1792620763f82898a3b9f5286c06cc7ad5c8e9b16aae443dc64094c74991b3e9
  summary: >-
    You'll debug and profile an MPI matrix-multiplication application on Arm Linux with Linaro Forge.
    First, you'll build C, Fortran, or Python variants that contain intentional defects, then configure debugging
    flags and `AddressSanitizer`. You'll then identify and fix errors before rebuilding the application to
    confirm stable execution. Finally, you'll profile unoptimized and optimized builds, compare equivalent
    math libraries, and use profiler output to assess each build and library choice.
  faqs:
  - question: How do I confirm that Linaro Forge is installed correctly?
    answer: >-
      Run `ddt --version` and confirm that it prints Linaro Forge version information. 
  - question: After setup, where can I find the example application that I need to build and debug?
    answer: >-
      Open the `src` directory. You’ll find C, Fortran, and Python matrix-multiplication implementations,
      each with an intentional bug.
  - question: Which compiler flags should I use while debugging?
    answer: >-
      Edit `make.def` and set `CFLAGS = -O0 -g -fsanitize=address`. You disable optimization, add
      debug symbols, and enable `AddressSanitizer` with these flags.
  - question: How do I compare performance between unoptimized and optimized builds?
    answer: >-
      Build with `-O0` and profile the application for a baseline. Then, update `CFLAGS` in `make.def`
      to enable optimization, rebuild, and profile the new executable for comparison.
  - question: What should I check before moving from debugging to profiling?
    answer: >-
      Confirm that the program finishes without crashes or `AddressSanitizer` errors. Resolve any
      reported issues before profiling so that faults don’t distort your measurements.
# END generated_summary_faq

author: Florent Lebeau

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
platforms:
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
  - Oracle Cloud Infrastructure (OCI) Ampere Compute
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Fortran
    - GCC
    - Linaro Forge
    - gdb
    - mpi
    - Runbook

further_reading:
    - resource:
        title: Parallel Programming for Science Engineering by Victor Eijkhout
        link: https://theartofhpc.com/pcse/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

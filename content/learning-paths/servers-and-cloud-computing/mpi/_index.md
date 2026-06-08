---
title: Get started with parallel application development

minutes_to_complete: 30   

who_is_this_for: This is an advanced topic for HPC software developers writing MPI applications.

description: Debug, profile, and optimize MPI parallel applications on Arm servers using Linaro Forge, gdb, and Arm Performance Libraries.

learning_objectives: 
    - Debug and fix a parallel application
    - Profile and optimize your code
    - Use optimized routines for common math operations

prerequisites:
    - General knowledge about distributed parallelism (MPI)
    - Some understanding of C, Python, and Linux commands
    - An Arm computer running Linux. Cloud instances can be used, refer to the list of [Arm cloud service providers](/learning-paths/servers-and-cloud-computing/csp/).

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:34:00Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 300794f4010658d945212c74c5257635d620cbb6230cac0de92bf23e4e9e29fe
  summary_generated_at: '2026-06-02T04:29:07Z'
  summary_source_hash: 300794f4010658d945212c74c5257635d620cbb6230cac0de92bf23e4e9e29fe
  faq_generated_at: '2026-06-03T01:34:00Z'
  faq_source_hash: 300794f4010658d945212c74c5257635d620cbb6230cac0de92bf23e4e9e29fe
  summary: >-
    This advanced Learning Path is for HPC developers building MPI applications on Arm-based Linux
    servers or cloud instances. You will install and validate Linaro Forge, then build, debug,
    and profile a parallel matrix multiplication example implemented in C, Fortran, and Python.
    The steps show how to compile with -O0 -g -fsanitize=address to expose bugs and memory issues,
    use gdb and Forge for debugging, and compare profiling results across compiler options and
    alternative libraries, including Arm Performance Libraries for common math routines. The path
    was tested on Ubuntu 20.04 and assumes general MPI knowledge plus some familiarity with C,
    Python, and Linux commands. Cloud instances from AWS, Microsoft Azure, Google Cloud, or Oracle
    may be used.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an Arm computer running Linux; cloud instances from AWS, Microsoft Azure, Google
      Cloud, or Oracle can be used. General MPI knowledge and some familiarity with C, Python,
      and Linux commands are expected. The instructions are tested on Ubuntu 20.04; other distributions
      may require adjustments.
  - question: How do I verify that Linaro Forge installed correctly?
    answer: >-
      Run ddt --version. If the command is not found or does not report a version, revisit the
      Linaro Forge install guide and confirm your PATH and environment are set.
  - question: Where is the example application and which languages are available?
    answer: >-
      The parallel matrix multiplication application is in the src directory. Implementations
      are provided in C, Fortran, and Python, and each contains a bug that must be fixed.
  - question: Which build flags should I use for debugging and where do I set them?
    answer: >-
      Edit make.def in the src directory and set CFLAGS = -O0 -g -fsanitize=address. This disables
      compiler optimizations, adds debug symbols, and enables AddressSanitizer to help find memory
      issues.
  - question: How should I approach profiling and comparing alternatives?
    answer: >-
      Profile a baseline build with -O0, then enable compiler optimizations and compare results.
      You can also try alternative coding approaches and libraries implementing equivalent functions,
      including Arm Performance Libraries for common math routines.
# END generated_summary_faq

author: Florent Lebeau

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
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


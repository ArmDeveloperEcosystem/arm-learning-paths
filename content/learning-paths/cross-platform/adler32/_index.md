---
title: Write Neon intrinsics using GitHub Copilot to improve Adler32 performance

description: Learn how to use GitHub Copilot to write Neon intrinsics that accelerate the Adler32 checksum algorithm on Arm platforms, achieving significant performance improvements over standard C implementations.

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for C/C++ developers who are interested in using GitHub Copilot to improve performance using Neon intrinsics.

learning_objectives: 
    - Use GitHub Copilot to write Neon intrinsics that accelerate the Adler32 checksum algorithm.

prerequisites:
    - An Arm computer running Linux with the GNU compiler (gcc) installed.
    - Visual Studio Code with the GitHub Copilot extension installed. 

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:30:35Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 37b19106fba70423ba8c58f82097d9251f0ae208e882c852f9c4531afcebb46c
  summary_generated_at: '2026-06-01T21:00:08Z'
  summary_source_hash: 37b19106fba70423ba8c58f82097d9251f0ae208e882c852f9c4531afcebb46c
  faq_generated_at: '2026-06-02T21:30:35Z'
  faq_source_hash: 37b19106fba70423ba8c58f82097d9251f0ae208e882c852f9c4531afcebb46c
  summary: >-
    This introductory Learning Path shows C/C++ developers on Arm Linux how to use GitHub Copilot
    in Visual Studio Code to implement and accelerate the Adler32 checksum with Arm Neon intrinsics.
    You will start by prompting Copilot to generate a baseline C implementation, create a test
    program that validates correctness and measures runtime on random inputs from 1 KB to 10 MB,
    and have Copilot produce a gcc Makefile optimized for Neoverse N1. You then build and run
    the project to validate results and use Copilot to add Neon intrinsics, aiming for significant
    speedups over the C baseline. Prerequisites: an Arm computer running Linux with gcc, and VS
    Code with the GitHub Copilot extension.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an Arm computer running Linux with gcc installed, and Visual Studio Code with the
      GitHub Copilot extension. No other prerequisites are explicitly listed.
  - question: Which GitHub Copilot mode or model should I use?
    answer: >-
      Open GitHub Copilot, choose the Large Language Model you prefer, and select Agent mode.
      Results vary by model; the example output shown in the path was produced with Claude 3.7
      Sonnet.
  - question: How is the project built, and which CPU is it tuned for?
    answer: >-
      Copilot generates a Makefile that builds the project with gcc and selects optimization flags
      for the Neoverse N1. Use the provided Makefile targets to compile and run the tests.
  - question: What should I verify when I run the test program?
    answer: >-
      Check that the checksum results are correct for all listed data sizes. The test program
      also measures performance to provide a baseline before introducing Neon intrinsics.
  - question: When do I implement Neon intrinsics for Adler32?
    answer: >-
      After establishing the baseline C implementation and test harness, the path guides you to
      use GitHub Copilot to write Neon intrinsics for Adler32. This step focuses on leveraging
      Arm Advanced SIMD to accelerate the algorithm.
# END generated_summary_faq

author: Jason Andrews

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
    - Cortex-A
tools_software_languages:
    - GCC
    - Runbook

operatingsystems:
    - Linux
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - mobile-graphics-and-gaming


further_reading:
    - resource:
        title: Arm C Language Extensions
        link: https://arm-software.github.io/acle/
        type: Documentation
    - resource:
        title: Adler-32 Checksum Algorithm
        link: https://en.wikipedia.org/wiki/Adler-32
        type: Article
    - resource:
        title: Neon Programming Quick Reference
        link: https://developer.arm.com/documentation/den0018/a
        type: Documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


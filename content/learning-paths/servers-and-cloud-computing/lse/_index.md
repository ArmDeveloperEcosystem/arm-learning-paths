---
title: Learn about Large System Extensions 

minutes_to_complete: 30 

who_is_this_for: This is an introductory topic for software developers who want to learn about Large System Extensions (LSEs) and use them in an application.

description: Understand Large System Extensions (LSEs) for Arm processors and verify whether applications use LSE for improved atomic operation performance.

learning_objectives:
    - Understand LSEs.
    - Find out if an application uses LSE.

prerequisites:
    - Access to an AWS Graviton-based instance, an Arm AGI CPU platform, or other Arm Linux computers with LSE support 

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-28T19:45:44Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 650f26e707e62f858c1b6fd9de6b9a3022c414a0e473e7e86c0ce6b237285c3d
  summary_generated_at: '2026-09-28T19:45:44Z'
  summary_source_hash: 650f26e707e62f858c1b6fd9de6b9a3022c414a0e473e7e86c0ce6b237285c3d
  faq_generated_at: '2026-09-28T19:45:44Z'
  faq_source_hash: 650f26e707e62f858c1b6fd9de6b9a3022c414a0e473e7e86c0ce6b237285c3d
  summary: >-
    You'll explore how LSEs support atomic operations on many-core systems.
    First, you'll create a C program that uses C11 threads and standard atomics for concurrent updates,
    then compile and run it on Arm Linux. You'll compare atomic and non-atomic counters under contention
    and inspect the compiled output. Finally, you'll verify whether your compiler generated LSE
    instructions for the target system.
  faqs:
  - question: Where should I save the example and which headers does it need?
    answer: >-
      Save the program as `atomic.c`. Include `stdio.h`, `threads.h`, and `stdatomic.h`.
  - question: How many threads and iterations does the example use?
    answer: >-
      You'll create 10 threads, with each thread performing 1,000 increments of both the non-atomic
      and atomic counters.
  - question: What result should I expect when I run the program?
    answer: >-
      Confirm that the atomic counter reports the total increments across all threads. Your non-atomic
      counter can report a different value because concurrent updates create data races.
  - question: How do I verify whether the compiler generated LSE instructions?
    answer: >-
      Run the `objdump` command and check its count of LSE atomic instructions. You can
      also inspect the disassembly for instructions such as `ldaddal`.
  - question: How can I check whether my Arm-based Linux system supports LSE?
    answer: >-
      Run `sudo dmesg | grep LSE` and look for a message that reports detected LSE atomic
      instructions. You can also run `lscpu | grep Flags`. The `atomics` flag indicates LSE support.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
platforms:
  - Arm AGI CPU
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
  - Oracle Cloud Infrastructure (OCI) Ampere Compute
armips:
    - Neoverse 
operatingsystems:
    - Linux 
tools_software_languages:
    - GCC
    - Runbook

further_reading:
    - resource:
        title: Improving Java performance on Neoverse N1 systems
        link: https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/java-performance-on-neoverse-n1
        type: blog
    - resource:
        title: Arm's LSE for atomics and MySQL
        link: https://mysqlonarm.github.io/ARM-LSE-and-MySQL/
        type: blog
    - resource:
        title: Learn about glibc with Large System Extensions (LSE) for performance improvement
        link: /learning-paths/servers-and-cloud-computing/glibc-with-lse/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

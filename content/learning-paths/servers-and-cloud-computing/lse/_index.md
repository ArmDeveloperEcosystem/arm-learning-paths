---
title: Learn about Large System Extensions (LSE)

minutes_to_complete: 30 

who_is_this_for: This is an introductory topic for software developers who want to learn about Large System Extensions and use them in an application.

description: Understand Large System Extensions (LSE) for Arm processors and verify whether applications use LSE for improved atomic operation performance.

learning_objectives:
    - Learn about Large System Extensions
    - Find out if an application uses Large System Extensions

prerequisites:
    - An [AWS account](/learning-paths/servers-and-cloud-computing/csp/aws/) to access instance types with different AWS Graviton processors. If you don't have an AWS account, you can substitute other Arm Linux computers.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:24:38Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 9610291239b88c67e21055f94cd03fe7cf80f7d875d53ebe0d8de7837ce99fa7
  summary_generated_at: '2026-06-02T04:18:56Z'
  summary_source_hash: 9610291239b88c67e21055f94cd03fe7cf80f7d875d53ebe0d8de7837ce99fa7
  faq_generated_at: '2026-06-03T01:24:38Z'
  faq_source_hash: 9610291239b88c67e21055f94cd03fe7cf80f7d875d53ebe0d8de7837ce99fa7
  summary: >-
    This Learning Path introduces Large System Extensions (LSE) on Arm processors and shows how
    to check whether your application and toolchain use LSE for atomic operations. You will build
    and run a short C example on a Linux system to observe multi-threaded atomic increments and
    verify if the compiler emits LSE instructions. The path is introductory and relevant to developers
    targeting Arm servers based on Neoverse, using AWS Graviton instances or another Arm Linux
    machine. You will use GCC and follow a runbook to create the sample, compile it, and assess
    LSE usage. No additional prerequisites are explicitly listed beyond access to an Arm Linux
    environment; an AWS account is suggested for convenient access to Arm instances.
  faqs:
  - question: What do I need before running the example?
    answer: >-
      You need access to an Arm Linux computer. An AWS account is recommended to use instance
      types with different AWS Graviton processors, but you can substitute other Arm Linux systems
      if you prefer.
  - question: Which compiler should I use to build the example program?
    answer: >-
      Use GCC on your Arm Linux computer. The Learning Path uses GCC to build the C example that
      exercises atomic operations.
  - question: How do I know if my build is using Large System Extensions?
    answer: >-
      The steps guide you to build and run an example and then verify whether the compiler generated
      LSE instructions. Follow the verification instructions in the path to confirm LSE usage.
  - question: Can I complete this Learning Path without an AWS account?
    answer: >-
      Yes. If you do not have an AWS account, you can use any other Arm Linux computer as a substitute.
  - question: What result should I expect after running the example program?
    answer: >-
      You will compile and run a multithreaded C program that uses atomic operations. The expected
      outcome is that you can determine whether LSE instructions were generated for the example.
# END generated_summary_faq

author: Jason Andrews

### Tags
skilllevels: Introductory
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


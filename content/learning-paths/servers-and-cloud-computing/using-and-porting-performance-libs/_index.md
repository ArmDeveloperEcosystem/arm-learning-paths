---
title: Migrate applications that leverage performance libraries 

minutes_to_complete: 60

who_is_this_for: This Learning Path is for both C and C++ developers who want to migrate applications that rely on optimized performance libraries from x86 to Arm Architecture.

learning_objectives: 
    - Describe the differences between standard and performance libraries.
    - Incorporate optimized libraries. 
    - Port a basic application from x86 to AArch64. 
prerequisites:
    - Access to both an Arm and an x86-based cloud instance.
    - Intermediate understanding of C++, compilers, and Linux. 

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:14:44Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 035bd363fc8ae772acf52d7e392f2db27087267706aeec86b4098c497e5fe91d
  summary_generated_at: '2026-06-02T05:24:08Z'
  summary_source_hash: 035bd363fc8ae772acf52d7e392f2db27087267706aeec86b4098c497e5fe91d
  faq_generated_at: '2026-06-03T02:14:44Z'
  faq_source_hash: 035bd363fc8ae772acf52d7e392f2db27087267706aeec86b4098c497e5fe91d
  summary: >-
    This Learning Path guides C and C++ developers through migrating applications that depend
    on optimized performance libraries from x86 to Arm Architecture on Linux. You will compare
    the C++ standard library with performance libraries, set up an Arm-based AWS instance running
    Ubuntu 22.04 LTS, install build tools and Arm Performance Libraries, and use libamath to access
    optimized math routines. You will then port a basic application that uses Intel’s Vector Statistics
    Library (VSL) to AArch64 using OpenRNG as a drop-in replacement. Prerequisites include access
    to both an Arm and an x86 cloud instance and intermediate knowledge of C++, compilers, and
    Linux. Estimated time to complete is about 60 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need access to both an Arm-based and an x86-based cloud instance, plus an intermediate
      understanding of C++, compilers, and Linux. No additional prerequisites are explicitly listed.
  - question: Which Arm instance and OS are used in the setup example?
    answer: >-
      The example uses an Arm-based AWS instance, such as t4g.2xlarge, running Ubuntu 22.04 LTS.
      You connect to the instance via SSH before installing packages.
  - question: Which compiler should I use to build the examples?
    answer: >-
      The setup installs GCC and G++ from the Ubuntu repositories for building the examples. Although
      Arm Compiler for Linux is listed as a tool, the walkthrough uses GCC.
  - question: How do I install Arm Performance Libraries on the instance?
    answer: >-
      After connecting via SSH, run apt update and install gcc, g++, and make, then download and
      install Arm Performance Libraries using the commands provided in the Learning Path. For
      details, follow the Arm Performance Libraries install guide referenced in the steps.
  - question: How do I replace Intel Vector Statistics Library when migrating to AArch64?
    answer: >-
      Use OpenRNG, included with Arm Performance Libraries 24.04, as a drop-in replacement for
      Intel’s Vector Statistics Library. It supports a range of RNG types and utilities to help
      transition existing code to Arm.
# END generated_summary_faq

author: Kieran Hejmadi

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
tools_software_languages:
    - Arm Compiler for Linux
    - CPP
    - Runbook
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Arm Performance Library Reference Guide
        link: https://developer.arm.com/documentation/101004/latest/
        type: documentation
    - resource:
        title: Software Ecosystem Dashboard for Arm
        link: https://www.arm.com/developer-hub/ecosystem-dashboard
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


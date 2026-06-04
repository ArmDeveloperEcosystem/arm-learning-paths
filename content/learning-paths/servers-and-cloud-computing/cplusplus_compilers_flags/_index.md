---
title: Learn about optimization techniques using the g++ compiler
description: Learn how to apply g++ compiler optimization techniques and flags to improve C++ application performance on Arm systems with hands-on examples.

minutes_to_complete: 60

who_is_this_for: This Learning Path is for beginner C++ developers who are looking to optimize applications on Arm-based cloud instances using compiler flags. 

learning_objectives: 
    - Compile a C++ program for a specific Arm target.
    - Use compiler flags to manage optimizations.

prerequisites:
    - Basic understanding of C++.
    - Basic understanding of compilers.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:37:16Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 22f845b8ea4dbb9ffc63fafb76c17c79aedde14a28417d49e1ab0833bbbc1eba
  summary_generated_at: '2026-06-02T03:28:45Z'
  summary_source_hash: 22f845b8ea4dbb9ffc63fafb76c17c79aedde14a28417d49e1ab0833bbbc1eba
  faq_generated_at: '2026-06-03T00:37:16Z'
  faq_source_hash: 22f845b8ea4dbb9ffc63fafb76c17c79aedde14a28417d49e1ab0833bbbc1eba
  summary: >-
    Learn how to apply g++ compiler optimization flags when building C++ applications for Arm-based
    servers. You will provision and connect to an AWS Graviton4 (r8g.xlarge) instance running
    Ubuntu 24.04 LTS, then build and run a sample C++ program on Linux while selecting an appropriate
    target architecture and optimization strategy. The path also reviews Neoverse-based instance
    generations (for example, Graviton3/V1 and Graviton4/V2) to inform choices like the -march
    flag for portability, size, or focusing on a specific CPU. This introductory, 60‑minute path
    assumes a basic understanding of C++ and compilers and focuses on compiling for a specific
    Arm target and managing optimizations with g++.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a basic understanding of C++ and compilers, and access to an AWS account to create
      a Graviton4 (r8g.xlarge) instance running Ubuntu 24.04 LTS. You also need a way to connect
      to the instance.
  - question: Which -march value should I use for my build?
    answer: >-
      Choose the lowest Arm architecture among the systems you plan to run on if you need portability.
      If you want the highest performance on a specific processor, target that processor (for
      example, AWS Graviton4) instead.
  - question: How do I know my environment and compiler are ready?
    answer: >-
      After connecting to the instance, the path has you run commands to confirm the OS and compiler
      setup on Ubuntu 24.04 LTS. Proceed once you have verified that your build environment is
      available.
  - question: What result should I expect after I build and run the example?
    answer: >-
      You will produce a compiled C++ application built with the selected g++ optimization flags
      for an Arm target and run it on the AWS Graviton4 instance. The path helps you compare choices
      such as portability versus targeting a specific CPU or optimizing for size.
  - question: Can I follow this on other Arm-based cloud instances?
    answer: >-
      Most cloud providers offer Arm-based instances on Neoverse, but the hands-on steps use AWS
      Graviton4. If you plan to run across different Arm servers, select an -march value that
      matches the lowest target in your set.
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
    - CPP
    - Runbook
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Runtime Detection of CPU features 
        link: https://community.arm.com/arm-community-blogs/b/operating-systems-blog/posts/runtime-detection-of-cpu-features-on-an-armv8-a-cpu
        type: blog


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


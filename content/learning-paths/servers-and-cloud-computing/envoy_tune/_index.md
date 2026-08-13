---
title: Learn how to tune Envoy
description: Learn how to optimize Envoy proxy performance on Arm servers using Transparent Huge Pages and Profile-Guided Optimization techniques.

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for software developers who want to use Envoy on Arm.

learning_objectives:
    - Tune Envoy by Transparent Huge Pages (THP)
    - Tune Envoy with profile-guided optimization (PGO)
    - Learn about kernel parameters that can impact Envoy performance
    - Learn about compiler and libraries that can impact Envoy performance

prerequisites:
    - Cloud or bare-metal installation of an Envoy service
    - Review [Learn how to deploy Envoy](/learning-paths/servers-and-cloud-computing/envoy/) if you do not already have an Envoy setup

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-12T20:19:33Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 06090a1659fc83424284ccabaa440122d6bfd0f7a8ab16f14ddda1153039a685
  summary_generated_at: '2026-08-12T20:19:33Z'
  summary_source_hash: 06090a1659fc83424284ccabaa440122d6bfd0f7a8ab16f14ddda1153039a685
  faq_generated_at: '2026-08-12T20:19:33Z'
  faq_source_hash: 06090a1659fc83424284ccabaa440122d6bfd0f7a8ab16f14ddda1153039a685
  summary: >-
    You'll tune Envoy on an Arm-based Ubuntu server with THP and
    PGO. First, you'll inspect the kernel configuration, confirm THP support,
    and configure memory management for Envoy. Then, you'll build Envoy with current Bazel and
    LLVM and Clang toolchains, identifying the kernel parameters and compiler choices that influence
    performance.
  faqs:
  - question: How do I check the kernel configuration on Ubuntu before tuning THP?
    answer: >-
      Run `cat /boot/config-$(uname -r)` to inspect the configuration for the running kernel.
      Use this command to confirm that the necessary options for THP are present.
  - question: Do I need an existing Envoy deployment before running these tuning steps?
    answer: >-
      Yes. You need a cloud or bare-metal Envoy service in place. If you don't already have Envoy
      set up, complete the [Learn how to deploy Envoy](/learning-paths/servers-and-cloud-computing/envoy/) Learning Path.
  - question: Which compiler should I use when building Envoy with PGO?
    answer: >-
      Use the latest available version of LLVM and Clang when building Envoy with Bazel. 
  - question: Should I build Bazel from source for the PGO workflow?
    answer: >-
      Build Bazel from the most recent source code. Doing so aligns your build
      with the latest LLVM and Clang toolchains.
  - question: What result should I expect after enabling THP or applying PGO?
    answer: >-
      The reported example shows an 18% enhancement from THP and a 10% enhancement from PGO.
      Actual results depend on how you apply the techniques to your Envoy
      deployment.
# END generated_summary_faq

author: Zhengjun Xing

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Web
platforms:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
armips:
    - Neoverse
tools_software_languages:
    - Envoy  
    - Runbook

operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Envoy Documentation
        link: https://www.envoyproxy.io/docs/envoy/latest
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

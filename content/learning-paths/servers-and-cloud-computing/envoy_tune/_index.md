---
title: Learn how to tune Envoy
description: Learn how to optimize Envoy proxy performance on Arm servers using Transparent Huge Pages and Profile-Guided Optimization techniques.

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for software developers who want to use Envoy on Arm.

learning_objectives:
    - Tune Envoy by THP
    - Tune Envoy with PGO
    - Learn about kernel parameters that can impact Envoy performance
    - Learn about compiler and libraries that can impact Envoy performance

prerequisites:
    - Cloud or bare-metal installation of an Envoy service
    - Review [Learn how to deploy Envoy](/learning-paths/servers-and-cloud-computing/envoy/) if you do not already have an Envoy setup

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:48:49Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: cbbcc8fa33f864e422f8db7d58fba32c26f6070be2846b246837c63ccf37e1c7
  summary_generated_at: '2026-06-02T03:45:17Z'
  summary_source_hash: cbbcc8fa33f864e422f8db7d58fba32c26f6070be2846b246837c63ccf37e1c7
  faq_generated_at: '2026-06-03T00:48:49Z'
  faq_source_hash: cbbcc8fa33f864e422f8db7d58fba32c26f6070be2846b246837c63ccf37e1c7
  summary: >-
    Learn how to tune Envoy on Arm servers running Linux—on bare metal or Arm instances from AWS,
    Microsoft Azure, Google Cloud, or Oracle—using Transparent Huge Pages (THP) and Profile-Guided
    Optimization (PGO). You will review kernel parameters that affect Envoy, check THP configuration
    (with an Ubuntu example), and rebuild Envoy with Bazel and LLVM/Clang to apply PGO, using
    the latest compiler and a recent Bazel as recommended. This advanced path expects an existing
    Envoy service; if you do not have one, follow the Deploy Envoy Learning Path first. By the
    end, you will have applied THP settings and produced a PGO-built Envoy binary.
  faqs:
  - question: What do I need before running these tuning steps?
    answer: >-
      You need a cloud or bare-metal installation of an Envoy service. If you do not already have
      Envoy set up, review Learn how to deploy Envoy.
  - question: Which environments does this Learning Path target?
    answer: >-
      Linux on Arm servers, including Arm Neoverse in the cloud (AWS, Microsoft Azure, Google
      Cloud, Oracle) or on bare metal. The guidance is for developers running Envoy on Arm.
  - question: How do I check my Linux kernel configuration for THP on Ubuntu?
    answer: >-
      Run: cat /boot/config-$(uname -r) to inspect your kernel configuration. Use this to verify
      settings relevant to Transparent Huge Pages.
  - question: Which toolchain should I use to build Envoy with PGO?
    answer: >-
      Build Envoy using Bazel and LLVM/Clang, and use the latest compiler version. It is advisable
      to build Bazel from the most recent source; refer to the LLVM and Clang documentation for
      details.
  - question: What performance improvement should I expect from THP or PGO?
    answer: >-
      The Learning Path notes that applying THP can result in an 18% enhancement in performance,
      and PGO can result in a 10% enhancement. These figures are presented as general guidance.
# END generated_summary_faq

author: Zhengjun Xing

### Tags
skilllevels: Advanced
subjects: Web
cloud_service_providers:
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


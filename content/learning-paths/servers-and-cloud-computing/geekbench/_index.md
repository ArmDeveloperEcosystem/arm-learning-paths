---
title: Run Geekbench on Arm Linux systems
description: Run Geekbench on Arm systems to benchmark CPU performance, interpret the results, and compare different Arm configurations.

minutes_to_complete: 15

who_is_this_for: This is an introductory topic for software developers interested in comparing the performance of Arm Linux computers using Geekbench.

learning_objectives:
- Learn how to install and run Geekbench
- Use Geekbench to help determine the appropriate hardware configuration for your workload

prerequisites:
- An Arm computer running Linux. You can use a cloud instance, refer to [Get started with Arm-based cloud instances](/learning-paths/servers-and-cloud-computing/csp/).

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:01:02Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 85a0a44bde6f217bdfc7fd0660ed6a86279b24c7ede302307ef6efb2626d83d9
  summary_generated_at: '2026-06-02T03:59:40Z'
  summary_source_hash: 85a0a44bde6f217bdfc7fd0660ed6a86279b24c7ede302307ef6efb2626d83d9
  faq_generated_at: '2026-06-03T01:01:02Z'
  faq_source_hash: 85a0a44bde6f217bdfc7fd0660ed6a86279b24c7ede302307ef6efb2626d83d9
  summary: >-
    This introductory Learning Path shows how to download and run Geekbench on Arm Linux systems
    to benchmark CPU performance. You will install and execute Geekbench, obtain single-core and
    multi-core scores, and use the results to compare different Arm configurations when selecting
    hardware for your workload. The path targets Arm computers running Linux, including cloud
    instances, and takes about 15 minutes to complete. Tools include Geekbench (with Preview Versions
    available for Linux on Arm) and a Runbook. By the end, you will be able to run Geekbench on
    an Arm Linux system, interpret the reported core scores, and apply them to basic hardware
    selection decisions.
  faqs:
  - question: What do I need before running this benchmark?
    answer: >-
      You need an Arm computer running Linux. A cloud instance is acceptable; refer to Get started
      with Arm-based cloud instances.
  - question: Which Geekbench package should I download for Arm Linux?
    answer: >-
      Use a Geekbench Preview Version for Linux on Arm. Check the Geekbench downloads area for
      the appropriate Arm Linux build.
  - question: What result should I expect after a successful run?
    answer: >-
      Geekbench reports a single-core score, a multi-core score, and individual performance scores.
      You will use these values to assess and compare systems.
  - question: How should I compare different Arm systems using Geekbench?
    answer: >-
      Run Geekbench on each system you want to evaluate and compare the reported single-core,
      multi-core, and individual performance scores. Use these comparisons to help determine a
      suitable hardware configuration for your workload.
  - question: Can I use an operating system other than Linux for this path?
    answer: >-
      This path targets Linux on Arm. Geekbench provides downloads for additional operating systems,
      but those are not covered here.
# END generated_summary_faq

author: Jason Andrews

skilllevels: Introductory

subjects: Performance and Architecture

armips:
    - Neoverse
operatingsystems:
    - Linux
test_maintenance: true
test_images:
    - ubuntu:latest
tools_software_languages:
    - Geekbench
    - Runbook


further_reading:
    - resource:
        title: Performance Analysis for Arm vs x86 CPUs in the Cloud
        link: https://www.infoq.com/articles/arm-vs-x86-cloud-performance/
        type: blog
    - resource:
        title: GCP, AWS, and Azure ARM-based server performance comparison
        link: https://apisix.apache.org/blog/2022/08/12/arm-performance-google-aws-azure-with-apisix/
        type: blog
    - resource:
        title: Geekbench How it actually works
        link: https://www.xda-developers.com/geekbench/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: learningpathall
learning_path_main_page: 'yes'
---


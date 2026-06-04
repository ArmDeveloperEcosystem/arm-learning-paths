---
title: Learn how to tune Redis

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for software developers who want to deploy Redis on Arm-based servers and follow best practices to get performance benefits.

learning_objectives:
    - Learn about kernel parameters that can impact Redis performance
    - Learn about compiler and libraries that can impact Redis performance
    - Tune a Redis configuration file for deployment

prerequisites:
    - Cloud or bare-metal installation of an Redis file server
    - Review [Learn how to deploy Redis](/learning-paths/servers-and-cloud-computing/redis/) if you do not already have Redis setup

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:00:24Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a6ed103f2d5a00f4cb6c5df1c0812eb68bbad8746d3f351adc959c6880002bbc
  summary_generated_at: '2026-06-02T05:00:17Z'
  summary_source_hash: a6ed103f2d5a00f4cb6c5df1c0812eb68bbad8746d3f351adc959c6880002bbc
  faq_generated_at: '2026-06-03T02:00:24Z'
  faq_source_hash: a6ed103f2d5a00f4cb6c5df1c0812eb68bbad8746d3f351adc959c6880002bbc
  summary: >-
    This advanced Learning Path shows how to tune Redis on Arm-based servers built on Neoverse,
    running Linux in the cloud (AWS, Microsoft Azure, Google Cloud, Oracle) or on bare metal.
    You will review Linux kernel parameters along with compiler and OpenSSL settings that can
    impact Redis performance, then apply guidance to tune a Redis configuration file for deployment.
    The material emphasizes workload-specific choices rather than a single preset and introduces
    practical mechanisms such as /proc and sysctl for memory-related adjustments. Prerequisite:
    a cloud or bare-metal installation of a Redis file server; if Redis is not set up, review
    Learn how to deploy Redis first. Estimated time to complete: 30 minutes.
  faqs:
  - question: What do I need before running the tuning steps?
    answer: >-
      You need a cloud or bare-metal installation of a Redis file server. If you do not already
      have Redis set up, review Learn how to deploy Redis before starting.
  - question: Where do I change Linux memory-related kernel parameters during this path?
    answer: >-
      You can change them temporarily through the /proc filesystem or permanently using the sysctl
      command. The path discusses these options as part of general guidance.
  - question: How should I decide which kernel, compiler, and OpenSSL settings to use?
    answer: >-
      There is no one-size-fits-all configuration; the right choices depend on your client request
      profile and use case. Use the provided guidance to evaluate and select settings that match
      your workload characteristics.
  - question: Which Redis configuration does this path focus on?
    answer: >-
      It focuses on Redis file configuration and references the Configure Redis single-node section
      of the Learn how to deploy Redis path. Cluster-specific configuration is not explicitly
      listed.
  - question: Can I follow these steps on my preferred cloud provider?
    answer: >-
      Yes. The path targets Linux on Arm-based servers and can be used in cloud or bare-metal
      environments, including AWS, Microsoft Azure, Google Cloud, and Oracle; provider-specific
      instructions are not detailed.
# END generated_summary_faq

author: Elham Harirpoush

### Tags
skilllevels: Advanced
subjects: Databases
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
armips:
    - Neoverse
tools_software_languages:
    - Redis    
    - Runbook

operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Redis Documentation
        link: https://redis.io/docs/
        type: documentation
    


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


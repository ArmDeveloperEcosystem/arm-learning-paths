---
title: Install Vectorscan (Hyperscan on Arm) and use it with Snort 3

minutes_to_complete: 15

who_is_this_for: This is an introductory topic for software developers using Hyperscan who want to migrate to Arm.


learning_objectives:
    - Install and run Vectorscan on an Arm-based instance
    - Install and run Snort 3 on your instance
    - Run Snort 3 with Vectorscan on capture files and and measure performance

prerequisites:
    - An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or an Arm server with Ubuntu 20.04 or Ubuntu 22.04 installed.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:15:15Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: beb244c7766c474b47942b86f1cdd0d124c1cccb74dbe40f0b6c0917d0b3d31a
  summary_generated_at: '2026-06-02T05:24:57Z'
  summary_source_hash: beb244c7766c474b47942b86f1cdd0d124c1cccb74dbe40f0b6c0917d0b3d31a
  faq_generated_at: '2026-06-03T02:15:15Z'
  faq_source_hash: beb244c7766c474b47942b86f1cdd0d124c1cccb74dbe40f0b6c0917d0b3d31a
  summary: >-
    Learn how to migrate regex-based workloads from Hyperscan to Arm by installing and running
    Vectorscan on an Arm-based Ubuntu instance, then integrating it with Snort 3. You will set
    up on Ubuntu 20.04 or 22.04, install Snort 3 and its dependencies, and run Snort 3 with Vectorscan
    on capture files to measure performance. This introductory path targets developers familiar
    with Hyperscan who want to adopt Arm, including Arm-based cloud instances from AWS, Microsoft
    Azure, Google Cloud, or Oracle, or an Arm server. The steps are concise and practical, designed
    to complete in about 15 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an Arm-based instance from a cloud service provider or an Arm server with Ubuntu
      20.04 or Ubuntu 22.04 installed. No other explicit prerequisites are listed.
  - question: Should I install Hyperscan or Vectorscan on Arm?
    answer: >-
      Install Vectorscan. Hyperscan runs only on x86_64, and Vectorscan is the architecture-inclusive
      fork that supports Arm.
  - question: Can I use a cloud instance from AWS, Microsoft Azure, Google Cloud, or Oracle?
    answer: >-
      Yes. Any Arm-based instance from these cloud providers is in scope, as long as it runs Ubuntu
      20.04 or Ubuntu 22.04.
  - question: Which Ubuntu versions are these steps intended for?
    answer: >-
      Ubuntu 20.04 and Ubuntu 22.04 on Arm are explicitly listed and are the tested environments
      for this Learning Path.
  - question: What result should I expect after completing the steps?
    answer: >-
      You will have Vectorscan installed and running on your Arm instance, and Snort 3 installed
      and run with Vectorscan on capture files. You will also measure performance as directed
      in the steps.
# END generated_summary_faq

author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Libraries
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
armips:
    - Neoverse
tools_software_languages:
    - Vectorscan
operatingsystems:
    - Linux

test_images:
- ubuntu:latest
test_link: https://github.com/armflorentlebeau/arm-learning-paths/actions/runs/4312122327
test_maintenance: true

further_reading:
    - resource:
        title: Snort documentation
        link: https://www.snort.org/documents
        type: documentation
    - resource:
        title: Accelerate Deep Packet Inspection with Neon on Arm
        link: https://developer.arm.com/community/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/accelerating-deep-packet-inspection-with-neon-on-arm-neoverse
        type: blog



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


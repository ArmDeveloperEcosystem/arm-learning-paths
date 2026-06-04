---
title: Measure performance of ClickHouse on Arm servers
description: Learn how to install ClickHouse on Arm-based cloud instances and measure database performance using ClickBench to determine appropriate instance configurations.

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for software developers who want to use ClickHouse on Arm-based cloud instances.

learning_objectives:
    - Learn how to install and measure ClickHouse performance
    - Determine the appropriate instance configuration needed for your workloads

prerequisites:
    - An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or an on-premise Arm server.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:34:16Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0d1390198cf2f0e87f509c5269fc2405cffcb2e57311024150d47e60a3273178
  summary_generated_at: '2026-06-02T03:24:05Z'
  summary_source_hash: 0d1390198cf2f0e87f509c5269fc2405cffcb2e57311024150d47e60a3273178
  faq_generated_at: '2026-06-03T00:34:16Z'
  faq_source_hash: 0d1390198cf2f0e87f509c5269fc2405cffcb2e57311024150d47e60a3273178
  summary: >-
    This Learning Path shows how to install ClickHouse on an Arm-based cloud instance or Arm server
    running Ubuntu for Arm, then measure query latency with ClickBench using a web‑analytics dataset.
    It is an introductory, hands-on path for developers evaluating ClickHouse on Arm to choose
    appropriate instance configurations across cloud providers or on‑premises. You will set up
    ClickHouse, run ClickBench to capture processing times, and use the results to inform instance
    selection for your workloads. Prerequisites include access to an Arm-based instance and sufficient
    storage for the dataset; no additional tools beyond ClickHouse and ClickBench are listed.
    Expected duration is about 45 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an Arm-based instance from a cloud service provider or an on-premise Arm server.
      Ensure it runs a recent version of Ubuntu for Arm and has enough storage for the web-analytics
      dataset used in the benchmark.
  - question: Which cloud platforms can I use for the Arm instance?
    answer: >-
      You can use Arm-based instances from AWS, Microsoft Azure, Google Cloud, or Oracle. An on-premise
      Arm server is also suitable.
  - question: Which operating system should I run on the instance?
    answer: >-
      Use a recent version of Ubuntu for Arm. The path assumes a Linux environment.
  - question: What result should I expect after running ClickBench?
    answer: >-
      ClickBench reports processing time (query latency) for ClickHouse on the web-analytics workload.
      You can use these measurements to evaluate performance and inform your instance configuration
      choices.
  - question: What should I check if the benchmark fails or seems unusually slow?
    answer: >-
      Confirm you are using an Arm-based instance with a recent Ubuntu for Arm and that sufficient
      storage is available for the dataset. Also ensure the dataset required by the steps is present
      before running ClickBench.
# END generated_summary_faq

author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Databases
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
armips:
    - Neoverse
tools_software_languages:
    - ClickHouse
    - ClickBench
operatingsystems:
    - Linux

test_images:
- ubuntu:latest
test_link: https://github.com/armflorentlebeau/arm-learning-paths/actions/runs/4312122327
test_maintenance: true

further_reading:
    - resource:
        title: ClickHouse Documentation
        link: https://clickhouse.com/docs/en/home/
        type: documentation
    - resource:
        title: ClickBench source repository
        link: https://github.com/ClickHouse/ClickBench/#readme
        type: documentation
    - resource:
        title: Improve ClickHouse performance on Arm-based AWS Graviton3 servers
        link: https://developer.arm.com/community/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/improve-clickhouse-performance-up-to-26-by-using-aws-graviton3
        type: blog


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


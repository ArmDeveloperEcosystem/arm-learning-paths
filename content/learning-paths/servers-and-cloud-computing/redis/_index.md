---
title: Deploy Redis on Arm

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers who want to deploy Redis on Arm based virtual machines.

learning_objectives: 
    - Understand Redis deployment configurations
    - Install and run Redis in a single-node Arm based instance  

prerequisites:

    - An Arm based instance from a cloud service provider, or an on-premise Arm server.
    - If you do not have an Arm node, the next section discusses some options.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:58:39Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 7b9906a3c16ebd3c6b41618be7db76d7a97cc4b16c4da927257fb39a66753e12
  summary_generated_at: '2026-06-02T04:57:15Z'
  summary_source_hash: 7b9906a3c16ebd3c6b41618be7db76d7a97cc4b16c4da927257fb39a66753e12
  faq_generated_at: '2026-06-03T01:58:39Z'
  faq_source_hash: 7b9906a3c16ebd3c6b41618be7db76d7a97cc4b16c4da927257fb39a66753e12
  summary: >-
    Deploy Redis on Arm is an introductory, 30-minute path that guides you through installing,
    configuring, and connecting to Redis on an Arm-based Linux instance. You will learn about
    Redis deployment configurations and set up a single-node server, including adjusting the default
    binding so the service is reachable beyond localhost on the default port 6379. The path applies
    to Arm virtual machines from major cloud providers (AWS, Microsoft Azure, Google Cloud, Oracle)
    or an on-premise Arm server. The outcome is a running Redis instance on Arm and a clear understanding
    of the core setup choices; tuning and advanced configuration are covered in a separate path.
    Prerequisite: access to an Arm node.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need access to an Arm based instance on a cloud service provider or an on-premise Arm
      server running Linux. If you do not have an Arm node, the next section discusses options.
  - question: Which cloud providers can I use for the Arm instance?
    answer: >-
      You can use AWS, Microsoft Azure, Google Cloud, or Oracle. The path targets Arm-based virtual
      machines on these platforms.
  - question: How do I enable remote access to my single-node Redis server?
    answer: >-
      By default Redis binds to 127.0.0.1 on port 6379. To accept remote connections, set the
      bind option in redis.conf to 0.0.0.0.
  - question: What port does Redis use in this setup?
    answer: >-
      Redis runs on port 6379 by default. The path focuses on adjusting the bind address for a
      single-node deployment; changing the port is not explicitly listed.
  - question: What should I do after I have Redis running with the default configuration?
    answer: >-
      Once Redis is working, follow the Learn how to Tune Redis learning path. It is recommended
      for improving the configuration beyond the default setup.
# END generated_summary_faq

author: Elham Harirpoush
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
operatingsystems:
    - Linux
tools_software_languages:
    - Redis
    - Runbook


further_reading:
    - resource:
        title: Redis documentation
        link: https://redis.io/docs/
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


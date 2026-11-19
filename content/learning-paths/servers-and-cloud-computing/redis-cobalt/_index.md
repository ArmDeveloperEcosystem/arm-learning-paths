---
title: Deploy Redis messaging on Azure Cobalt 100 Arm64 VMs
description: Learn how to install and configure Redis on an Azure Cobalt 100 Arm64 virtual machine, implement real-time messaging with Pub/Sub and Streams, and benchmark throughput and latency on Arm infrastructure.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers, DevOps engineers, and platform engineers who want to build real-time messaging systems and event-driven applications using Redis on Arm-based cloud environments.

learning_objectives:
    - Install and configure Redis on Arm64 virtual machines powered by Azure Cobalt 100.
    - Implement real-time messaging using Redis Pub/Sub.
    - Build event-driven pipelines using Redis Streams and consumer groups.
    - Benchmark Redis performance and validate throughput and latency on Arm.

prerequisites:
  - A [Microsoft Azure account](https://azure.microsoft.com/) with access to Cobalt 100-based instances (Dpsv6)
  - Basic knowledge of Linux command-line operations
  - Familiarity with SSH and remote server access
  - Basic understanding of databases, caching, and messaging systems

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-19T16:03:25Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 06b2317b6273703a23729a1c59e8c11450d494f7634699020778ff53a573edad
  summary_generated_at: '2026-11-19T16:03:25Z'
  summary_source_hash: 06b2317b6273703a23729a1c59e8c11450d494f7634699020778ff53a573edad
  faq_generated_at: '2026-11-19T16:03:25Z'
  faq_source_hash: 06b2317b6273703a23729a1c59e8c11450d494f7634699020778ff53a573edad
  summary: >-
    You'll deploy Redis on an Azure Cobalt VM and use it for messaging and event processing. First, you'll
    provision a Dpsv6 instance, install Redis, and check server connectivity. You'll then publish
    and subscribe to messages, create Streams and consumer groups, and acknowledge processed
    events. Finally, you'll use Python workload scripts and `redis-benchmark` to measure
    throughput and latency on the Arm-based VM.
  faqs:
  - question: How do I verify that the Redis server started?
    answer: >-
      Run `src/redis-cli` after starting Redis, then enter `PING` at the CLI prompt. You
      should receive `PONG` before testing messaging.
  - question: Do I need multiple terminals for Pub/Sub and Streams?
    answer: >-
      Yes. Keep the Redis server running in one terminal and use other terminals for the
      publisher and consumers.
  - question: What should I see when Pub/Sub works?
    answer: >-
      Subscribe to a channel, then publish a message from another terminal. You should see
      that message arrive in the subscriber terminal.
  - question: When should I use Pub/Sub or Streams?
    answer: >-
      Use Pub/Sub for immediate message delivery to active subscribers. Use Streams and
      consumer groups when you need to distribute and acknowledge queued work.
  - question: How do I run a Redis benchmark?
    answer: >-
      Run `src/redis-benchmark -q -n 100000 -c 50` from the Redis source directory. You can
      review the reported request rates for each operation.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
### Tags
skilllevels: Introductory
subjects: Databases
platforms:
  - Microsoft Azure Cobalt

armips:
    - Neoverse

tools_software_languages:
    - Redis
    - Python

operatingsystems:
    - Linux

further_reading:
  - resource:
      title: Redis Official Website
      link: https://redis.io
      type: website
  - resource:
      title: Redis Documentation
      link: https://redis.io/docs/
      type: documentation
  - resource:
      title: Redis Streams Introduction
      link: https://redis.io/docs/data-types/streams/
      type: documentation
  - resource:
      title: Azure Cobalt 100 processors
      link: https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---


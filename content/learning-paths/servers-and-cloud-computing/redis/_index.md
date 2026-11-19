---
title: Deploy Redis on Arm

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers who want to deploy Redis on Arm based virtual machines.

learning_objectives: 
    - Identify Redis deployment configurations.
    - Install and run Redis in a single-node Arm based instance.

prerequisites:

    - An Arm based instance from a cloud service provider, or an on-premise Arm server

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-19T16:03:01Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e8e8c501fb3a45836ddd838ba397139f4a050e39d750dda05e2baa9333c6a782
  summary_generated_at: '2026-11-19T16:03:01Z'
  summary_source_hash: e8e8c501fb3a45836ddd838ba397139f4a050e39d750dda05e2baa9333c6a782
  faq_generated_at: '2026-11-19T16:03:01Z'
  faq_source_hash: e8e8c501fb3a45836ddd838ba397139f4a050e39d750dda05e2baa9333c6a782
  summary: >-
    You'll deploy a single-node Redis server on an Arm-based Linux instance. First, you'll install Redis,
    start the service, and confirm a local connection. You'll then set the `bind` directive in `redis.conf`, and use
    `redis-cli` to check connectivity from another machine.
  faqs:
  - question: What address does Redis listen on by default?
    answer: >-
     By default, Redis listens on `127.0.0.1:6379`.
  - question: Why can't I connect from another machine?
    answer: >-
      Redis binds to `127.0.0.1` by default. Set the `bind` directive in `redis.conf` to
      `0.0.0.0`, then restart Redis.
  - question: How do I test a remote connection?
    answer: >-
      Run `redis-cli -h <public-IP-address> -p 6379` from your client, then send `PING`. You
      should receive `PONG`.
  - question: Which port does this deployment use?
    answer: >-
      Use the Redis default TCP port, `6379`, for local and remote connection checks.
  - question: How do I check that Redis stores and retrieves data?
    answer: >-
      In `redis-cli`, run `SET name test`, then `GET name`. You should receive `"test"`.
# END generated_summary_faq

author: Elham Harirpoush

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Databases
platforms:
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
  - Oracle Cloud Infrastructure (OCI) Ampere Compute
  - Arm AGI CPU
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


---
title: Deploy Elasticsearch on Azure Cobalt 100 Arm virtual machines

description: Learn how to deploy Elasticsearch on an Azure Cobalt 100 Arm virtual machine, validate the service, and run a baseline ESRally benchmark.

minutes_to_complete: 120

who_is_this_for: This Learning Path is for developers who want to deploy and benchmark Elasticsearch on Azure Cobalt 100 Arm virtual machines (VMs).

learning_objectives: 
    - Provision an Arm-based Azure Cobalt 100 VM using Azure
    - Install and validate Elasticsearch on the Cobalt 100 VM
    - Run a baseline ESRally benchmark and interpret key performance metrics

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 instances (Epdsv6 series)
    - Basic familiarity with SSH
    - Familiarity with Elasticsearch and ESRally

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-12T20:17:13Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 1eb86273af3c057becaa0e868cd7f8ab6f197d0b03f0b8d65af58b8d69cd1758
  summary_generated_at: '2026-08-12T20:17:13Z'
  summary_source_hash: 1eb86273af3c057becaa0e868cd7f8ab6f197d0b03f0b8d65af58b8d69cd1758
  faq_generated_at: '2026-08-12T20:17:13Z'
  faq_source_hash: 1eb86273af3c057becaa0e868cd7f8ab6f197d0b03f0b8d65af58b8d69cd1758
  summary: >-
    You'll deploy and benchmark Elasticsearch on an Arm-based Azure Cobalt 100 VM.
    First, you'll provision an Epdsv6 VM, install OpenJDK 21, Elasticsearch, and ESRally, and validate the
    service. Then, you'll run ESRally's geonames workload, interpret indexing throughput, and query
    latency to establish a repeatable performance baseline for future benchmark runs.
  faqs:
  - question: Which Azure VM size should I choose for this deployment?
    answer: >-
      Use a memory-optimized VM in the Epdsv6 series with the Arm-based Cobalt 100 processor. You configure this instance through the Azure portal.
  - question: Do I need Java, and which version should I install?
    answer: >-
      Yes. Install OpenJDK 21 (`openjdk-21-jdk`) because Elasticsearch needs it.
  - question: Should I run ESRally on the same VM as Elasticsearch?
    answer: >-
      Yes. Install both Elasticsearch and ESRally on the same Cobalt 100 VM.
  - question: What should I check to confirm Elasticsearch is ready before benchmarking?
    answer: >-
      Ensure the service starts without errors and is ready to accept connections. Proceed to
      ESRally only after the service is running and healthy.
  - question: Which ESRally track should I run, and what results should I focus on?
    answer: >-
      Run the geonames track. Focus on key metrics reported by ESRally, including indexing throughput
      and query latency under mixed ingest and search conditions.
# END generated_summary_faq

author: Doug Anson

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
platforms:
  - Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - Elasticsearch
    - ESRally
    - Bash

operatingsystems:
    - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
  - resource:
      title: Azure Virtual Machines documentation
      link: https://learn.microsoft.com/en-us/azure/virtual-machines/
      type: documentation
  - resource:
      title: Elasticsearch documentation
      link: https://www.elastic.co/docs/reference/elasticsearch
      type: documentation
  - resource:
      title: ESRally documentation
      link: https://esrally.readthedocs.io/en/stable/index.html
      type: documentation

weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"
---

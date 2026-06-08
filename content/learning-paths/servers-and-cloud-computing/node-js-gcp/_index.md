---
title:  Deploy Node.js on Google Cloud C4A Arm-based Axion VMs



minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers migrating Node.js workloads from x86_64 to Arm-based servers, specifically on Google Cloud C4A virtual machines built on Axion processors.


learning_objectives:
  - Provision an Arm-based SUSE Linux Enterprise Server virtual machine on Google Cloud C4A instances with Axion processors
  - Install and configure Node.js on a SUSE Arm64 (C4A) instance
  - Validate Node.js functionality with baseline HTTP server tests
  - Benchmark Node.js performance using Autocannon on Arm64 (AArch64) architecture 


prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Familiarity with networking concepts and [Node.js event-driven architecture](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick)

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:41:19Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 800eed835763098d4b369789d10de642bbdbaa390e8bfe0cb6ea2c4c78f7ecbd
  summary_generated_at: '2026-06-02T04:39:16Z'
  summary_source_hash: 800eed835763098d4b369789d10de642bbdbaa390e8bfe0cb6ea2c4c78f7ecbd
  faq_generated_at: '2026-06-03T01:41:19Z'
  faq_source_hash: 800eed835763098d4b369789d10de642bbdbaa390e8bfe0cb6ea2c4c78f7ecbd
  summary: >-
    Learn how to deploy and evaluate Node.js on Google Cloud C4A virtual machines powered by Axion
    processors built on Arm Neoverse-V2 cores. You will provision a SUSE Linux Enterprise Server
    VM (for example, c4a-standard-4) in the Google Cloud Console, install and manage Node.js with
    Node Version Manager (NVM), validate the runtime with baseline REPL and HTTP server tests,
    and benchmark using Autocannon on Arm64 (AArch64). This introductory path is aimed at developers
    migrating Node.js workloads from x86_64 to Arm on GCP. Prerequisites include a GCP account
    with billing enabled and familiarity with networking concepts and the Node.js event-driven
    architecture.
  faqs:
  - question: What do I need before provisioning the VM?
    answer: >-
      You need a Google Cloud Platform account with billing enabled. Familiarity with networking
      concepts and Node.js’s event-driven architecture is also expected.
  - question: Which Google Cloud instance type and OS image are used in the steps?
    answer: >-
      The path uses Google Cloud C4A Arm-based instances, with c4a-standard-4 (4 vCPUs, 16 GB
      memory) shown as an example. The VM runs SUSE Linux Enterprise Server on Arm64 (AArch64).
  - question: How do I install Node.js on the Arm VM?
    answer: >-
      Use Node Version Manager (NVM). Run the provided NVM install script, load NVM in your shell,
      then install and select a Node.js version using the official Node.js packages.
  - question: How do I confirm the Node.js setup before benchmarking?
    answer: >-
      Start the Node.js REPL and print a message such as "Hello from Node.js" to verify the runtime.
      Then run the simple HTTP server baseline test to confirm the server starts and responds.
  - question: What should I expect from the Autocannon benchmark, and what should I check if it
      fails?
    answer: >-
      Autocannon reports metrics such as throughput and latency for your HTTP server on Arm64.
      If it fails to reach the server, first confirm the baseline HTTP server is running and reachable,
      then rerun the benchmark.
# END generated_summary_faq

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Web
cloud_service_providers:
  - Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - Node.js
  - npm
  - Autocannon

operatingsystems:
  - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
  - resource:
      title: Google Cloud documentation
      link: https://cloud.google.com/docs
      type: documentation

  - resource:
      title: Node.js documentation
      link: https://nodejs.org/en
      type: documentation

  - resource:
      title: Autocannon documentation
      link: https://www.npmjs.com/package/autocannon/v/5.0.0
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---


---
title: Deploy TypeScript on Google Cloud C4A virtual machines
    
minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers deploying and optimizing TypeScript workloads on Arm64 Linux environments, specifically using Google Cloud C4A virtual machines powered by Axion processors.

learning_objectives:
  - Provision an Arm-based SUSE Linux Enterprise Server (SLES) virtual machine (VM) on Google Cloud 
  - Install TypeScript on a SUSE Arm64 C4A instance
  - Validate TypeScript functionality by creating, compiling, and running a simple TypeScript script on a Arm64 VM
  - Benchmark TypeScript performance using a JMH-style custom benchmark with the perf_hooks module on Arm64 architecture

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with [TypeScript](https://www.typescriptlang.org/) and Node.js runtime environment


generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:14:07Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ee805f703acd45612c9a94e60c6322866dc1c8ff25d48de2fb4cd9067948c93e
  summary_generated_at: '2026-06-02T05:23:36Z'
  summary_source_hash: ee805f703acd45612c9a94e60c6322866dc1c8ff25d48de2fb4cd9067948c93e
  faq_generated_at: '2026-06-03T02:14:07Z'
  faq_source_hash: ee805f703acd45612c9a94e60c6322866dc1c8ff25d48de2fb4cd9067948c93e
  summary: >-
    Provision a SUSE Linux Enterprise Server (SLES) VM on Google Cloud’s Arm-based C4A instances
    powered by Axion processors, install a TypeScript toolchain, validate it, and benchmark it.
    You will create a c4a-standard-4 VM via the Google Cloud Console, then install Node.js, npm,
    TypeScript, and ts-node on an Arm64 environment. After initializing a minimal project, you
    will compile and run a simple TypeScript file to confirm the setup. Finally, you will implement
    a JMH-style benchmark using Node.js perf_hooks to collect average runtime across multiple
    iterations. Prerequisites are a GCP account with billing enabled and basic familiarity with
    TypeScript and Node.js. Estimated time to complete is about 30 minutes.
  faqs:
  - question: What do I need before creating the VM on Google Cloud?
    answer: >-
      You need a Google Cloud Platform (GCP) account with billing enabled. Basic familiarity with
      TypeScript and the Node.js runtime is assumed.
  - question: Which machine type and OS should I use for the instance?
    answer: >-
      Use the c4a-standard-4 machine type, which provides four virtual CPUs and 16 GB of memory.
      Provision a SUSE Linux Enterprise Server (SLES) Arm64 VM from the Google Cloud Console under
      Compute Engine > VM Instances.
  - question: Which packages are installed to run TypeScript on the SUSE Arm64 VM?
    answer: >-
      You install Node.js, npm, TypeScript, and ts-node. These components enable you to develop,
      compile, and run TypeScript code on the Arm64 instance.
  - question: How do I verify the TypeScript environment is working?
    answer: >-
      Create a minimal project, then create, compile, and run a simple TypeScript file. Successful
      compilation and execution confirm the environment is ready for benchmarking.
  - question: What result should I expect from the benchmarking step?
    answer: >-
      The JMH-style benchmark implemented with Node.js perf_hooks runs multiple iterations and
      reports an average runtime. This produces stable, repeatable performance data for your workload
      on the C4A Arm64 VM.
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
  - TypeScript
  - node.js
  - npm

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
      title: TypeScript documentation
      link:  https://www.typescriptlang.org/docs/
      type: documentation

  - resource:
      title: TypeScript Benchmark documentation
      link: https://tech.spiko.io/posts/benchmarking-typescript-type-checking/
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---


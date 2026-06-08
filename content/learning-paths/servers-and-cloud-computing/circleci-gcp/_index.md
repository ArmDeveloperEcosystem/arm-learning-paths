---
title: Run CircleCI Arm Native Workflows on a SUSE Arm GCP VM
description: Learn how to set up CircleCI self-hosted machine runners on Google Cloud Axion C4A SUSE VMs and execute Arm-native CI/CD workflows using custom resource classes.
    
minutes_to_complete: 45

who_is_this_for: This is an introductory topic for developers and DevOps engineers looking to set up and run CircleCI Arm native workflows on SUSE Linux Arm64 virtual machines (VMs), specifically on Google Cloud C4A with Axion processors, using self-hosted runners.

learning_objectives:
  - Provision a SUSE Arm64 virtual machine on Google Cloud (C4A with Axion processors)
  - Install and configure CircleCI self-hosted machine runners on Arm64
  - Create a cloud-native Node.js demo app to run on the self-hosted Arm runner
  - Write and execute a CircleCI workflow using a custom Arm resource class
  - Test CircleCI workflows locally and understand job execution on Arm64 runners

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with Linux command line, Node.js, and npm
  - Basic understanding of CircleCI concepts such as 
    [workflows](https://circleci.com/docs/guides/orchestrate/workflows/), 
    [jobs](https://circleci.com/docs/guides/orchestrate/jobs-steps/),
    [resource classes](https://circleci.com/docs/guides/execution-managed/resource-class-overview/), and 
    [runners](https://circleci.com/docs/guides/execution-runner/runner-overview/)


generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:33:06Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ec9cdca7aa9a5670f54ea3646f965149460d8e66d9d5d904e1b6dcf09867df39
  summary_generated_at: '2026-06-02T03:22:01Z'
  summary_source_hash: ec9cdca7aa9a5670f54ea3646f965149460d8e66d9d5d904e1b6dcf09867df39
  faq_generated_at: '2026-06-03T00:33:06Z'
  faq_source_hash: ec9cdca7aa9a5670f54ea3646f965149460d8e66d9d5d904e1b6dcf09867df39
  summary: >-
    Set up a SUSE Linux Arm64 virtual machine on Google Cloud C4A with Axion processors and run
    CircleCI Arm-native CI/CD workflows using self-hosted machine runners. You will provision
    a c4a instance via the Google Cloud Console, install the CircleCI CLI and Machine Runner on
    SUSE, create a custom resource class in the CircleCI dashboard, and target it from a workflow.
    The path also includes creating a simple Node.js demo app and testing workflows locally to
    understand job execution on Arm64 runners. Prerequisites include a GCP account with billing
    enabled, basic Linux command line, Node.js/npm familiarity, and a basic understanding of CircleCI
    workflows, jobs, resource classes, and runners. Estimated time to complete is about 45 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Google Cloud Platform account with billing enabled, plus basic familiarity with
      the Linux command line, Node.js and npm. You should also understand CircleCI concepts such
      as workflows, jobs, resource classes, and runners.
  - question: Which Google Cloud VM type and OS should I use for the self-hosted runner?
    answer: >-
      Provision a SUSE Linux (Arm64) VM using the C4A series, specifically c4a-standard-4 in the
      Google Cloud Console. This VM runs on Google’s Axion processors based on Arm Neoverse-V2
      cores.
  - question: How is the CircleCI CLI used in this path?
    answer: >-
      The CLI lets you validate CircleCI configuration, run jobs locally, and manage runners from
      the terminal. You will install it on SUSE Arm64 to test workflows and interact with your
      setup.
  - question: How do resource classes direct jobs to my Arm VM?
    answer: >-
      You create a custom resource class in the CircleCI dashboard that links your self-hosted
      runner to your organization. Reference this resource class in your workflow so jobs target
      the SUSE Arm64 VM.
  - question: How do I know the self-hosted runner is working with my Node.js demo workflow?
    answer: >-
      Run the provided CircleCI workflow that specifies your custom Arm resource class; the job
      should execute on the SUSE Arm64 VM. You can also use the CircleCI CLI to test and validate
      the configuration locally.
# END generated_summary_faq

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: CI-CD
cloud_service_providers:
  - Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - CircleCI
  - Node.js
  - npm
  - Docker

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
      title: CircleCI Self-Hosted Runner Documentation
      link:  https://circleci.com/docs/guides/execution-runner/install-machine-runner-3-on-linux/
      type: documentation

  - resource:
      title: CircleCI CLI Documentation
      link: https://circleci.com/docs/guides/toolkit/local-cli/
      type: documentation

  - resource:
      title: Node.js Express Documentation
      link: https://expressjs.com/
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---


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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-30T21:44:47Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ec9cdca7aa9a5670f54ea3646f965149460d8e66d9d5d904e1b6dcf09867df39
  summary_generated_at: '2026-06-30T21:44:47Z'
  summary_source_hash: ec9cdca7aa9a5670f54ea3646f965149460d8e66d9d5d904e1b6dcf09867df39
  faq_generated_at: '2026-06-30T21:44:47Z'
  faq_source_hash: ec9cdca7aa9a5670f54ea3646f965149460d8e66d9d5d904e1b6dcf09867df39
  summary: >-
    You'll provision a SUSE Linux Google Cloud C4A virtual machine (VM) powered by Google Axion,
    install the CircleCI CLI, create a custom resource class, and deploy the CircleCI Machine
    Runner so CI/CD jobs execute natively on Arm. After configuring a self-hosted runner linked
    to a CircleCI namespace, you'll author and dispatch a workflow that targets the resource class and runs a
    small Node.js demo app on the Arm VM. You'll then verify its execution in the CircleCI dashboard
    and on the VM.
  faqs:
  - question: How do I know I created the correct C4A Arm VM in Google Cloud?
    answer: >-
      During creation, select the `c4a-standard-4` machine type in the Google Cloud Console. After
      launch, open the VM details in Compute Engine and verify the machine type shows `c4a-standard-4`.
  - question: What should I verify after installing the CircleCI CLI on SUSE?
    answer: >-
      The CLI should be available to validate configuration files, run jobs locally, and manage
      runners. If it can't be installed or used, recheck that the required repositories were
      added to the SUSE environment as shown in the steps.
  - question: Which namespace should I use when creating the CircleCI resource class?
    answer: >-
      Use the CircleCI organization (namespace) where your project workflows run. The resource
      class links your self-hosted runner to that namespace so only authorized jobs can target
      the VM.
  - question: How can I confirm the machine runner is registered and ready to accept jobs?
    answer: >-
      Check the CircleCI web dashboard for the resource class and runner status. On the VM, the
      runner setup completes with a connection to CircleCI and then waits for jobs that reference
      its resource class.
  - question: How do I target the self-hosted Arm runner from my workflow, and what result should
      I expect?
    answer: >-
      Configure the job to use the custom resource class created for the Arm runner. When triggered,
      the job runs on the SUSE arm64 VM and the CircleCI UI shows the job associated with that
      resource class.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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


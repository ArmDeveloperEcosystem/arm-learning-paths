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


generate_summary_faq: true

rerun_summary: false
rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:57Z'
  generator: template
  source_hash: ec9cdca7aa9a5670f54ea3646f965149460d8e66d9d5d904e1b6dcf09867df39
  summary: >-
    Learn how to set up CircleCI self-hosted machine runners on Google Cloud Axion C4A SUSE VMs
    and execute Arm-native CI/CD workflows using custom resource classes. It is designed for developers
    and DevOps engineers looking to set up and run CircleCI Arm native workflows on SUSE Linux
    Arm64 virtual machines (VMs), specifically on Google Cloud C4A with Axion processors, using
    self-hosted runners. By the end, you will be able to provision a SUSE Arm64 virtual machine
    on Google Cloud (C4A with Axion processors), install and configure CircleCI self-hosted machine
    runners on Arm64, and create a cloud-native Node.js demo app to run on the self-hosted Arm
    runner. It focuses on tools and technologies such as CircleCI, Node.js, npm, and Docker, Linux
    environments, Arm platforms including Neoverse, and cloud platforms such as Google Cloud.
    The main steps cover Get started with CircleCI on Google Axion C4A, Create a Google Axion
    C4A Arm virtual machine on GCP, Install CircleCI, Create a resource class, and Install CircleCI
    Machine Runner on SUSE Arm.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will provision a SUSE Arm64 virtual machine on Google Cloud (C4A with Axion processors),
      install and configure CircleCI self-hosted machine runners on Arm64, and create a cloud-native
      Node.js demo app to run on the self-hosted Arm runner. Learn how to set up CircleCI self-hosted
      machine runners on Google Cloud Axion C4A SUSE VMs and execute Arm-native CI/CD workflows
      using custom resource classes.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for developers and DevOps engineers looking to set up and
      run CircleCI Arm native workflows on SUSE Linux Arm64 virtual machines (VMs), specifically
      on Google Cloud C4A with Axion processors, using self-hosted runners.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Google Cloud Platform (GCP)](https://cloud.google.com/free)
      account with billing enabled; Basic familiarity with Linux command line, Node.js, and npm;
      Basic understanding of CircleCI concepts such as [workflows](https://circleci.com/docs/guides/orchestrate/workflows/),
      [jobs](https://circleci.com/docs/guides/orchestrate/jobs-steps/), [resource classes](https://circleci.com/docs/guides/execution-managed/resource-class-overview/),
      and [runners](https://circleci.com/docs/guides/execution-runner/runner-overview/).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including CircleCI, Node.js, npm, and Docker, Linux environments,
      Arm platforms such as Neoverse, and cloud platforms such as Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Get started with CircleCI on Google Axion C4A, Create
      a Google Axion C4A Arm virtual machine on GCP, Install CircleCI, Create a resource class,
      and Install CircleCI Machine Runner on SUSE Arm.
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


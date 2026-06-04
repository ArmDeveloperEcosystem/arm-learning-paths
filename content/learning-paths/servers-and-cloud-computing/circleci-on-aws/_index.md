---
title: Deploy CircleCI Arm Native Workflows on AWS EC2 Graviton
description: Learn how to install and configure CircleCI self-hosted machine runners on AWS Graviton Arm64 instances to execute CI/CD workflows natively on Arm.
    
minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers and DevOps engineers who want to set up and run CircleCI Arm native workflows on Linux Arm64 virtual machines. You'll use AWS EC2 Graviton instances (Neoverse N1) and self-hosted runners. 

learning_objectives:
  - Create an AWS EC2 Graviton Arm64 virtual machine
  - Install and configure CircleCI self-hosted machine runners on Arm64
  - Verify the runner by running a simple workflow and test computation

prerequisites:
  - An [AWS account](https://aws.amazon.com/free/) with billing enabled
  - A CircleCI account
  - Basic understanding of CircleCI workflows, jobs and resource classes

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:33:29Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e04982fd668765fa2ab25f943f020b8d2b4a5e9b5ff3a51b7431cc4d93730180
  summary_generated_at: '2026-06-02T03:22:34Z'
  summary_source_hash: e04982fd668765fa2ab25f943f020b8d2b4a5e9b5ff3a51b7431cc4d93730180
  faq_generated_at: '2026-06-03T00:33:29Z'
  faq_source_hash: e04982fd668765fa2ab25f943f020b8d2b4a5e9b5ff3a51b7431cc4d93730180
  summary: >-
    Learn how to set up CircleCI self-hosted machine runners on AWS EC2 Graviton (Arm64) to execute
    CI/CD jobs natively on Arm. You will create a Linux Arm64 VM on an m6g.large instance, install
    the CircleCI CLI, register a resource class in the CircleCI dashboard, and install and configure
    the machine runner. Finally, you verify the setup by running a simple workflow and test computation
    on the runner. This introductory path targets developers and DevOps engineers using CircleCI,
    Bash, and Git. Prerequisites include an AWS account with billing enabled, a CircleCI account,
    and a basic understanding of CircleCI workflows, jobs, and resource classes. Estimated time:
    about 30 minutes.
  faqs:
  - question: Which EC2 instance type and OS should I use for this setup?
    answer: >-
      The steps use an AWS Graviton Arm64 instance with the m6g.large type. Choose an appropriate
      Linux AMI, such as an Ubuntu AMI, during instance creation.
  - question: What do I need before launching the instance and configuring CircleCI?
    answer: >-
      You need an AWS account with billing enabled, a CircleCI account, and a basic understanding
      of CircleCI workflows, jobs, and resource classes. No other prerequisites are explicitly
      listed.
  - question: How do I install the CircleCI CLI on the Graviton instance?
    answer: >-
      Update your package index and install tools like curl, tar, gzip, coreutils, gpg, and git.
      Then download and extract the CircleCI CLI binary as described in the steps.
  - question: How do I register and link a self-hosted runner to my CircleCI organization?
    answer: >-
      Create a resource class in the CircleCI Web Dashboard, which uniquely identifies your runner
      and links it to your namespace. If you do not have an organization, create one first to
      access the dashboard features.
  - question: How is the CircleCI machine runner installed on the EC2 instance?
    answer: >-
      Add the official CircleCI package repository for Debian/Ubuntu on Arm64, then install the
      CircleCI Runner via apt and configure it to use your resource class. Follow the path steps
      to complete the configuration.
# END generated_summary_faq

author: Annie Tallund

##### Tags
skilllevels: Introductory
subjects: CI-CD
cloud_service_providers:
  - AWS

armips:
  - Neoverse

tools_software_languages:
  - CircleCI
  - Bash
  - Git


operatingsystems:
  - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
  - resource:
      title: AWS EC2 Graviton Documentation
      link: https://aws.amazon.com/ec2/graviton/
      type: documentation

  - resource:
      title: CircleCI Self-Hosted Runner Documentation
      link:  https://circleci.com/docs/guides/execution-runner/install-machine-runner-3-on-linux/
      type: documentation

  - resource:
      title: CircleCI CLI Documentation
      link: https://circleci.com/docs/guides/toolkit/local-cli/
      type: documentation


weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---


---
title: Deploy CircleCI Arm Native Workflows on AWS EC2 Graviton
description: Learn how to install and configure CircleCI self-hosted machine runners on AWS Graviton Arm64 instances to execute CI/CD workflows natively on Arm.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers and DevOps engineers who want to set up and run CircleCI Arm native workflows on Linux Arm64 virtual machines. You'll use Amazon EC2 instances powered by AWS Graviton (Neoverse N1) and self-hosted runners. 

learning_objectives:
  - Create an Amazon EC2 Arm64 virtual machine
  - Install and configure CircleCI self-hosted machine runners on Arm64
  - Verify the runner by running a simple workflow and test computation

prerequisites:
  - An [AWS account](https://aws.amazon.com/free/) with billing enabled
  - A CircleCI account
  - Basic understanding of CircleCI workflows, jobs and resource classes

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-30T21:45:26Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e04982fd668765fa2ab25f943f020b8d2b4a5e9b5ff3a51b7431cc4d93730180
  summary_generated_at: '2026-06-30T21:45:26Z'
  summary_source_hash: e04982fd668765fa2ab25f943f020b8d2b4a5e9b5ff3a51b7431cc4d93730180
  faq_generated_at: '2026-06-30T21:45:26Z'
  faq_source_hash: e04982fd668765fa2ab25f943f020b8d2b4a5e9b5ff3a51b7431cc4d93730180
  summary: >-
    You'll deploy CircleCI Arm-native workflows on Amazon
    EC2 instances powered by AWS Graviton. Using the AWS Management Console, you'll provision an Arm64 instance (for
    example, `m6g.large`) on Linux and install the CircleCI CLI to work with configurations and
    pipelines from the terminal. In the CircleCI dashboard, you'll create a resource class to link
    a self-hosted machine runner to the correct namespace. Then, you'll installs the CircleCI
    machine runner on the Arm64 instance using the CircleCI package repository for Debian/Ubuntu
    systems. By the end, you'll execute a workflow and test computation to verify that jobs
    run on the self-hosted Graviton runner as configured.
  faqs:
  - question: Which EC2 instance and AMI should I select to follow the steps?
    answer: >-
      Use an Amazon EC2 instance powered by AWS Graviton, such as `m6g.large`, and choose a Linux AMI such as Ubuntu
      in the AWS Management Console. You'll follow a console-based instance launch workflow.
  - question: What should I install before setting up the CircleCI CLI?
    answer: >-
      Install curl, tar, gzip, coreutils, gpg, and git using your package manager. These tools
      enable downloading, verifying, and extracting the CLI.
  - question: What do I need before creating a resource class for the self-hosted runner?
    answer: >-
      Access the CircleCI dashboard and ensure an organization/namespace is available. The resource
      class links your runner to that namespace so jobs can target it.
  - question: How do I confirm the machine runner is installed and connected?
    answer: >-
      After adding the CircleCI package repository and installing the runner, the agent registers
      to your resource class. Running the sample workflow should start on the EC2 instance and
      complete the test computation.
  - question: What should I check if a job does not run on the self-hosted runner?
    answer: >-
      Verify the job targets the resource class you created, the EC2 instance is running, and
      the runner process is installed on that instance. Then re-run the workflow from the CircleCI
      dashboard.
# END generated_summary_faq

author: Annie Tallund

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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


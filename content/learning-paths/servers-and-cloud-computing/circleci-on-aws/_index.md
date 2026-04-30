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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:17Z'
  generator: template
  source_hash: e04982fd668765fa2ab25f943f020b8d2b4a5e9b5ff3a51b7431cc4d93730180
  summary: >-
    Learn how to install and configure CircleCI self-hosted machine runners on AWS Graviton Arm64
    instances to execute CI/CD workflows natively on Arm. It is designed for developers and DevOps
    engineers who want to set up and run CircleCI Arm native workflows on Linux Arm64 virtual
    machines. You'll use AWS EC2 Graviton instances (Neoverse N1) and self-hosted runners. By
    the end, you will be able to create an AWS EC2 Graviton Arm64 virtual machine, install and
    configure CircleCI self-hosted machine runners on Arm64, and verify the runner by running
    a simple workflow and test computation. It focuses on tools and technologies such as CircleCI,
    Bash, and Git, Linux environments, Arm platforms including Neoverse, and cloud platforms such
    as AWS. The main steps cover Get Started with CircleCI on AWS Graviton, Create an AWS EC2
    Arm64 Graviton Instance, Install CircleCI CLI, Create a resource class in CircleCI, and Install
    CircleCI machine runner on AWS Graviton.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will create an AWS EC2 Graviton Arm64 virtual machine, install and configure CircleCI
      self-hosted machine runners on Arm64, and verify the runner by running a simple workflow
      and test computation. Learn how to install and configure CircleCI self-hosted machine runners
      on AWS Graviton Arm64 instances to execute CI/CD workflows natively on Arm.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for developers and DevOps engineers who want to set up and
      run CircleCI Arm native workflows on Linux Arm64 virtual machines. You'll use AWS EC2 Graviton
      instances (Neoverse N1) and self-hosted runners.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An [AWS account](https://aws.amazon.com/free/)
      with billing enabled; A CircleCI account; Basic understanding of CircleCI workflows, jobs
      and resource classes.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including CircleCI, Bash, and Git, Linux environments, Arm
      platforms such as Neoverse, and cloud platforms such as AWS.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Get Started with CircleCI on AWS Graviton, Create
      an AWS EC2 Arm64 Graviton Instance, Install CircleCI CLI, Create a resource class in CircleCI,
      and Install CircleCI machine runner on AWS Graviton.
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


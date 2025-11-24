---
title: CircleCI Arm Native Workflows on AWS Graviton2 (EC2)
    
minutes_to_complete: 30

draft: true
cascade:
    draft: true

draft: true
cascade:
    draft: true

who_is_this_for: This learning path is intended for software developers and DevOps engineers looking to set up and run CircleCI Arm native workflows on Linux Arm64 VMs, specifically on AWS EC2 Graviton2 instances (Neoverse N1), using self-hosted runners.

learning_objectives:
  - Create an AWS EC2 Graviton2 Arm64 virtual machine
  - Install and configure CircleCI self-hosted machine runners on Arm64
  - Verify the runner by running a simple workflow and test computation

prerequisites:
  - An [AWS account](https://aws.amazon.com/free/) with billing enabled
  - A CircleCI account
  - Basic understanding of CircleCI workflows, jobs and resource classes

author: Annie Tallund

##### Tags
skilllevels: Introductory
subjects: CI-CD
cloud_service_providers: AWS

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

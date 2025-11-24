---
title: Deploy CircleCI Arm Native Workflows on AWS EC2 Graviton2 
    
minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers and DevOps engineers who want to set up and run CircleCI Arm native workflows on Linux Arm64 virtual machines. You'll use AWS EC2 Graviton2 instances (Neoverse N1) and self-hosted runners. 

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

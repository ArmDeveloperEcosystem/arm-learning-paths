---
title: Deploy CircleCI Arm Native Workflows on AWS EC2 Graviton2 
    
minutes_to_complete: 45

who_is_this_for: This is an introductory topic for developers and DevOps engineers who want to set up and run CircleCI Arm native workflows on Linux Arm64 virtual machines. You'll use AWS EC2 Graviton2 instances (Neoverse N1) and self-hosted runners. 

learning_objectives:
  - Provision an AWS EC2 Graviton2 Arm64 virtual machine
  - Install and configure a CircleCI self-hosted machine runners on Arm64
  - Verify the runner by running a simple workflow and test computation
  - Define and execute CircleCI job using a machine executor
  - Check CPU architecture and execute a basic script to confirm if the runner is operational
  - Display CPU information and validate outputs from the sample computation

prerequisites:
  - An [AWS account](https://aws.amazon.com/free/) with billing enabled
  - Basic familiarity with Linux command line
  - Basic understanding of CircleCI concepts such as 
    [workflows](https://circleci.com/docs/guides/orchestrate/workflows/), 
    [jobs](https://circleci.com/docs/guides/orchestrate/jobs-steps/),
    [resource classes](https://circleci.com/docs/guides/execution-managed/resource-class-overview/), and 
    [runners](https://circleci.com/docs/guides/execution-runner/runner-overview/)


author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: CI-CD
cloud_service_providers: AWS

armips:
  - Neoverse

tools_software_languages:
  - CircleCI
  - Bash/Shell scripting
  - Git


operatingsystems:
  - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
  - resource:
      title: AWS EC2 Documentation
      link: https://docs.aws.amazon.com/ec2/index.html
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

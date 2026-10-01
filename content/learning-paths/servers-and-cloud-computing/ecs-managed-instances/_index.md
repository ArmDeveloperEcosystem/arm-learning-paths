---
title: Deploy a container on AWS Graviton processors with Amazon ECS Managed Instances
description: Deploy an NGINX container with Amazon ECS Managed Instances and verify that your task runs on AWS Graviton-based compute.
draft: true

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for developers who want to deploy containers on AWS Graviton processors with Amazon Elastic Container Service (ECS) using Amazon ECS Managed Instances.

learning_objectives:
    - Create an Amazon ECS cluster for ECS Managed Instances.
    - Create a capacity provider that selects Arm-based instances powered by AWS Graviton.
    - Create and run an Arm-compatible Amazon ECS task, and verify that it runs on AWS Graviton-based compute.

prerequisites:
    - An AWS account with permissions to create AWS IAM roles and access Amazon ECS
    - A VPC with public subnets and a security group that allows inbound traffic on port 80
    - The [AWS CLI](/install-guides/aws-cli/) installed on your development machine

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-01T16:25:09Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 8bb38cf155cb25da350710e313987f1d1d05e22b866897c621ae53d1cda541a6
  summary_generated_at: '2026-10-01T16:25:09Z'
  summary_source_hash: 8bb38cf155cb25da350710e313987f1d1d05e22b866897c621ae53d1cda541a6
  faq_generated_at: '2026-10-01T16:25:09Z'
  faq_source_hash: 8bb38cf155cb25da350710e313987f1d1d05e22b866897c621ae53d1cda541a6
  summary: >-
    You'll deploy an NGINX container on Amazon ECS Managed Instances and verify that it runs on AWS
    Graviton-based compute. First, you'll create the required IAM roles and register a task definition for
    the `ARM64` architecture. You'll then create a cluster and capacity provider that filters for
    Amazon CPUs, run a standalone task, and verify the selected instance type. Finally, you'll clean up the AWS resources that you created.
  faqs:
  - question: Why do I need both an ARM64 task definition and a CPU manufacturer filter?
    answer: >-
      You need to set `runtimePlatform.cpuArchitecture` to `ARM64` in your task definition so that your task uses an Arm-compatible runtime.
      You need a CPU manufacturer filter so that Amazon ECS selects AWS
      Graviton-based instance types.
  - question: Which CPU manufacturer value selects Graviton-based instances with the AWS CLI?
    answer: >-
      Set `cpuManufacturers` to `amazon-web-services` in the capacity provider's instance
      requirements. This value corresponds to the **Amazon** option in the console.
  - question: How do I know that my task ran on Graviton?
    answer: >-
      Check the backing container instance's type in the Amazon ECS console or with the AWS CLI.
      Confirm that its family name contains `g`, such as `m6g` or `c6g`, which indicates that it's based on an AWS
      Graviton processor.
  - question: Should I run a standalone task or create a service to test placement?
    answer: >-
      To test placement, run a standalone task. A service is better suited for when you need
      Amazon ECS to maintain a desired task count, replace failed tasks, or integrate with a load
      balancer.
  - question: Why doesn't my task have its own public IP address?
    answer: >-
      For test purposes, the task uses the `host` network mode, so it uses the instance's public IP
      address. If that instance has no public IP address, confirm that its subnet automatically
      assigns public IPv4 addresses.
# END generated_summary_faq

author: Anupras Mohapatra

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

##### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
platforms:
  - AWS Graviton
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Amazon ECS

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
    - resource:
        title: Amazon ECS Managed Instances
        link: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ManagedInstances.html
        type: documentation
    - resource:
        title: Amazon ECS Managed Instances capacity providers
        link: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instances-capacity-providers-concept.html
        type: documentation
    - resource:
        title: Create a security group for your Amazon EC2 instance
        link: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-security-group.html
        type: documentation
    - resource:
        title: Amazon ECS infrastructure IAM role
        link: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/infrastructure_IAM_role.html
        type: documentation
    - resource:
        title: Amazon ECS Managed Instances instance profile
        link: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instances-instance-profile.html
        type: documentation


weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

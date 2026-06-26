---
title: Deploy containers on Arm-based compute using Amazon ECS and the AWS CDK
description: Learn how to define and deploy a containerized application on Arm-based compute using the AWS Cloud Development Kit.

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for software developers who want to use the AWS Cloud Development Kit (AWS CDK) to deploy containerized applications on Arm-based AWS infrastructure.

learning_objectives:
    - Create an example AWS CDK application in JavaScript
    - Define AWS infrastructure using the AWS CDK
    - Deploy application resources on Arm-based AWS compute using Amazon ECS and the AWS CDK

prerequisites:
    - An Amazon Web Services (AWS) account 
    - A local computer with the AWS CLI, AWS CDK CLI, and Node.js installed, with AWS credentials configured.
    - Familiarity with the Linux command line and JavaScript

author: Anupras Mohapatra
generate_summary_faq: true
rerun_summary: true
rerun_faqs: true

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
cloud_service_providers:
  - AWS
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - AWS CDK CLI
    - Amazon Elastic Container Service (Amazon ECS)
    - AWS CLI
    - Node.js
    - JavaScript

further_reading:
    - resource:
        title: AWS CDK Developer Guide
        link: https://docs.aws.amazon.com/cdk/v2/guide/home.html
        type: documentation
    - resource:
        title: AWS CDK CLI install guide
        link: /install-guides/aws-cdk/
        type: install-guide
    - resource:
        title: AWS CLI install guide
        link: /install-guides/aws-cli/
        type: install-guide
    - resource:
        title: Amazon ECS task definitions for 64-bit Arm workloads
        link: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-arm64.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

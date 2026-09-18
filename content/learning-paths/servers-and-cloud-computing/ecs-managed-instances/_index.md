---
title: Deploy containers on AWS Graviton processors with Amazon ECS Managed Instances
description: Learn how to create an Amazon ECS cluster and capacity provider for ECS Managed Instances, then run containerized tasks on AWS Graviton processors.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for developers who want to deploy containers on AWS Graviton processors using Amazon ECS Managed Instances.

learning_objectives:
    - Create an Amazon ECS cluster for ECS Managed Instances.
    - Create a capacity provider that selects Arm-based instances powered by AWS Graviton.
    - Create and run an Arm64 Amazon ECS task.

prerequisites:
    - An AWS account
    - A container image that supports the Arm64 architecture

author: Anupras Mohapatra

generate_summary_faq: true
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

weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

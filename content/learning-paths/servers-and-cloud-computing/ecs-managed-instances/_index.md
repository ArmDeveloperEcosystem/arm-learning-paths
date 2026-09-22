---
title: Deploy containers on AWS Graviton processors with Amazon ECS Managed Instances
description: Learn how to deploy containerized tasks on AWS Graviton processors using Amazon ECS Managed Instances.

draft: true
cascade:
    draft: true

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for developers who want to deploy containers on AWS Graviton processors with Amazon Elastic Container Service (ECS) using Amazon ECS Managed Instances.

learning_objectives:
    - Create an Amazon ECS cluster for ECS Managed Instances.
    - Create a capacity provider that selects Arm-based instances powered by AWS Graviton.
    - Create and run an Arm64 Amazon ECS task.

prerequisites:
    - An AWS account with permissions to create AWS IAM roles and access Amazon ECS, a VPC with public subnets, and a security group that allows inbound traffic on port `80` 
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
    - resource:
        title: Create a security group for your Amazon EC2 instance
        link: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-security-group.html
        type: documentation
    - resource:
        title: Amazon ECS infrastructure IAM role
        link: http://docs.aws.amazon.com/AmazonECS/latest/developerguide/infrastructure_IAM_role.html
        type: documentation
    - resource:
        title: Amazon ECS Managed Instances instance profile
        link: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instances-instance-profile.html
        type: documentation
    

weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

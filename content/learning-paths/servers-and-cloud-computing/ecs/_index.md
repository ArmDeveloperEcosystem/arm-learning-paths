---
title: "Deploy containers on Amazon ECS with AWS Graviton processors"

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for developers who want to use AWS Graviton processors with Amazon Elastic Container Service (ECS).

learning_objectives:
    - Create an AWS ECS cluster with Fargate and AWS Graviton processors
    - Create and run an AWS ECS task
    - Use Terraform to automate deployment of an ECS cluster

prerequisites:
    - An AWS account
    - A computer with Docker, AWS CLI, and Terraform installed

author: Jason Andrews

##### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
cloud_service_providers:
  - AWS
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Terraform
    - AWS Elastic Container Service (ECS)

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
    - resource:
        title: Amazon Elastic Container Registry
        link: https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html?pg=ln&sec=hs
        type: documentation
    - resource:
        title: What is IAM?
        link: https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html
        type: documentation



weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

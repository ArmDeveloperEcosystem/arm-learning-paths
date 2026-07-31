---
title: Deploy containers on Amazon ECS with AWS Graviton processors
description: Learn how to create an Amazon ECS cluster with Fargate and AWS Graviton processors, then create and run containerized tasks on Arm infrastructure.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for developers who want to use AWS Graviton processors with Amazon Elastic Container Service (ECS).

learning_objectives:
    - Create an Amazon ECS cluster with Fargate and AWS Graviton processors
    - Create and run an Amazon ECS task
    - Use Terraform to automate deployment of an ECS cluster

prerequisites:
    - An AWS account
    - A computer with Docker, AWS CLI, and Terraform installed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-27T18:54:28Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ef5f9e7c8844b20b9044b43f4758bc1d74374521093d7738a7f8832d21f1dcac
  summary_generated_at: '2026-07-27T18:54:28Z'
  summary_source_hash: ef5f9e7c8844b20b9044b43f4758bc1d74374521093d7738a7f8832d21f1dcac
  faq_generated_at: '2026-07-27T18:54:28Z'
  faq_source_hash: ef5f9e7c8844b20b9044b43f4758bc1d74374521093d7738a7f8832d21f1dcac
  summary: >-
    You'll deploy a containerized application on Amazon ECS with AWS
    Fargate and Graviton processors. You'll create an ECS cluster and task, run it on Arm-based
    AWS Fargate infrastructure, and then automate the workflow with Terraform.
    The Terraform configuration creates an Amazon Elastic Container Registry (ECR) repository and
    deploys an NGINX task to ECS on Graviton.
  faqs:
  - question: Do I need to manually provision EC2 instances for this deployment?
    answer: >-
      No. Fargate is a serverless option for ECS, so you don't manually provision or maintain EC2 instances.
  - question: What result should I expect after I create and run the ECS task?
    answer: >-
      The task should start on the Fargate cluster and show a running status in ECS. That confirms
      the container runs on AWS Graviton-backed infrastructure.
  - question: What is the source for container images in this workflow?
    answer: >-
      Create an Amazon ECR repository and use it as the source
      for images referenced by your ECS task. This lets ECS pull the image when the task starts.
  - question: What does the Terraform configuration in `main.tf` create?
    answer: >-
      It automates the same deployment steps by defining AWS resources such as an ECR repository
      and ECS components to run an NGINX task on Fargate with AWS Graviton processors.
  - question: What should I check if my ECS task stays in PENDING or fails to run?
    answer: >-
      Verify that the cluster and task definition target the Fargate launch type and that required
      AWS resources and permissions from earlier steps exist. Also check that the container image
      is available in the ECR repository you created.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
    - Amazon ECS

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

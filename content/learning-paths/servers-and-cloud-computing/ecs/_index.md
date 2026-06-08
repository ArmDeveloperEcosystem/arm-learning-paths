---
title: "Deploy containers on Amazon ECS with AWS Graviton processors"
description: Learn how to create an AWS ECS cluster with Fargate and AWS Graviton processors, then create and run containerized tasks on Arm infrastructure.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for developers who want to use AWS Graviton processors with Amazon Elastic Container Service (ECS).

learning_objectives:
    - Create an AWS ECS cluster with Fargate and AWS Graviton processors
    - Create and run an AWS ECS task
    - Use Terraform to automate deployment of an ECS cluster

prerequisites:
    - An AWS account
    - A computer with Docker, AWS CLI, and Terraform installed

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:45:33Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ef5f9e7c8844b20b9044b43f4758bc1d74374521093d7738a7f8832d21f1dcac
  summary_generated_at: '2026-06-02T03:40:50Z'
  summary_source_hash: ef5f9e7c8844b20b9044b43f4758bc1d74374521093d7738a7f8832d21f1dcac
  faq_generated_at: '2026-06-03T00:45:33Z'
  faq_source_hash: ef5f9e7c8844b20b9044b43f4758bc1d74374521093d7738a7f8832d21f1dcac
  summary: >-
    Learn to deploy containerized applications on Amazon Elastic Container Service (ECS) using
    Fargate with AWS Graviton processors. You will create an ECS cluster, configure required identity
    settings, and run a container task on Arm-based infrastructure. The path also shows how to
    automate the same workflow with Terraform by incrementally building a main.tf file, including
    creating an Amazon ECR repository and deploying an example Nginx service. This introductory,
    Linux-focused path targets developers new to ECS on Graviton. Prerequisites are an AWS account
    and a computer with Docker, AWS CLI, and Terraform installed. By the end, you will have a
    running ECS task on Fargate and a Terraform configuration that reproduces the deployment.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an AWS account and a computer with Docker, AWS CLI, and Terraform installed. The
      path targets Linux.
  - question: Do I need to manage EC2 instances for this deployment?
    answer: >-
      No. The path uses the Fargate launch type, which is serverless, so you do not provision
      or maintain EC2 instances.
  - question: Which architecture should my container image target to run on AWS Graviton?
    answer: >-
      Build your container image for the Arm architecture. Fargate supports AWS Graviton processors
      so your containers can run on Arm.
  - question: Where will I store and pull my container images in this workflow?
    answer: >-
      The path creates a repository in Amazon Elastic Container Registry (ECR). The Terraform
      section builds a main.tf that sets up ECR and uses it for the ECS deployment.
  - question: What result should I expect after completing the Terraform section?
    answer: >-
      You will have a main.tf that automates the same steps for deploying Nginx on ECS. This includes
      provisioning the required ECS resources and using an ECR repository for the container image.
# END generated_summary_faq

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


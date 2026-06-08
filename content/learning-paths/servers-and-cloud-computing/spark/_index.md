---
title: Learn how to deploy Spark on AWS Graviton2

minutes_to_complete: 60   

who_is_this_for: This is an advanced topic for anyone who wants to deploy Spark on AWS Graviton2.

learning_objectives: 
    - Automate Spark EC2 instance creation using Terraform and Ansible
    - Deploy a single instance of Spark on AWS Graviton2 
    
prerequisites:
    - An Amazon Web Services (AWS) [account](https://aws.amazon.com/)
    - A machine with [Terraform](/install-guides/terraform/), [AWS CLI](/install-guides/aws-cli/), [AWS IAM authenticator](https://docs.aws.amazon.com/eks/latest/userguide/install-aws-iam-authenticator.html), and [Ansible](/install-guides/ansible/) installed 

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:07:05Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 7a612e45aa64ac93fa9a1fe83da8a7c63ffbc3a4b159184b1a7b04fd46e8ee4b
  summary_generated_at: '2026-06-02T05:12:06Z'
  summary_source_hash: 7a612e45aa64ac93fa9a1fe83da8a7c63ffbc3a4b159184b1a7b04fd46e8ee4b
  faq_generated_at: '2026-06-03T02:07:05Z'
  faq_source_hash: 7a612e45aa64ac93fa9a1fe83da8a7c63ffbc3a4b159184b1a7b04fd46e8ee4b
  summary: >-
    Deploy a single-node Apache Spark environment on an AWS Graviton2 EC2 instance using Terraform
    and Ansible on Linux. This Learning Path focuses on automating instance creation with Terraform
    and configuring Spark with Ansible, targeting Arm Neoverse-based Graviton2 hardware on AWS.
    It is presented as an advanced topic and estimated to take about 60 minutes. Prerequisites
    include an AWS account and a local setup with Terraform, AWS CLI, AWS IAM authenticator, and
    Ansible. If you are new to Terraform, review the Automate AWS EC2 instance creation using
    Terraform Learning Path before starting. By the end, you will have deployed a single Spark
    instance on AWS Graviton2.
  faqs:
  - question: What do I need before running the deployment?
    answer: >-
      You need an AWS account and a machine with Terraform, AWS CLI, AWS IAM authenticator, and
      Ansible installed. These are the explicit prerequisites for the Learning Path.
  - question: Do I need prior Terraform experience to follow this path?
    answer: >-
      If you are new to Terraform, you should review the Automate AWS EC2 instance creation using
      Terraform Learning Path first. This will help you follow the provisioning steps more easily.
  - question: What result should I expect after completing the steps?
    answer: >-
      You will deploy a single Apache Spark instance on an AWS EC2 instance using AWS Graviton2.
      The deployment is automated with Terraform and Ansible.
  - question: Which operating system and platform does this deployment target?
    answer: >-
      The deployment targets Linux on AWS. The EC2 instance is based on AWS Graviton2 (Arm Neoverse).
  - question: Do I need to choose a specific AWS instance type or region?
    answer: >-
      A specific instance type or region is not explicitly listed. Use the Terraform configuration
      provided in the Learning Path and ensure the EC2 instance uses AWS Graviton2.
# END generated_summary_faq

author: Jason Andrews
### Tags
skilllevels: Introductory
subjects: Databases
cloud_service_providers:
  - AWS

armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Terraform

further_reading:
    - resource:
        title: Optimize Spark on AWS Graviton2
        link: https://developer.arm.com/community/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/optimize-spark-on-aws-graviton2-best-practices-k-means-clustering
        type: blog

    - resource:
        title: Achieve better performance for Spark workloads
        link: https://aws.amazon.com/blogs/big-data/achieve-up-to-27-better-price-performance-for-spark-workloads-with-aws-graviton2-on-amazon-emr-serverless/
        type: blog 


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


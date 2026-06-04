---
title: Deploy Arm Instances on AWS using Terraform
description: Learn how to automate the creation and deployment of AWS Graviton instances using Terraform with jump server access for secure infrastructure management.

minutes_to_complete: 60   

who_is_this_for: This is an introductory topic for software developers who are new to deploying Arm instances on AWS using Terraform.
 
learning_objectives: 
    - Automate AWS EC2 instance creation using Terraform
    - Deploy Arm instances on AWS and provide access via Jump Server
    - Provide infrastructure basics, code knowledge and files that could help with future learning paths

prerequisites:
    - An Amazon Web Services (AWS) [account](https://aws.amazon.com/)
    - A computer with [Terraform](/install-guides/terraform) installed

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:21:25Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 087a4d56914e5b53cec5ad17e8d682e72d04ba6b394237c081efe4a3f939e04e
  summary_generated_at: '2026-06-02T03:09:04Z'
  summary_source_hash: 087a4d56914e5b53cec5ad17e8d682e72d04ba6b394237c081efe4a3f939e04e
  faq_generated_at: '2026-06-03T00:21:25Z'
  faq_source_hash: 087a4d56914e5b53cec5ad17e8d682e72d04ba6b394237c081efe4a3f939e04e
  summary: >-
    This Learning Path shows how to automate the provisioning of Arm-based AWS Graviton instances
    using Terraform, with access provided through a Jump Server (bastion) for secure infrastructure
    management. You will use Terraform Cloud to define and deploy EC2 resources on AWS and work
    with reusable infrastructure-as-code files that you can adapt for future Learning Paths. Prerequisites
    are an AWS account and a computer with Terraform installed; any desktop, laptop, or VM with
    the required tools is suitable. By the end, you will have Arm instances deployed on AWS with
    jump server access and a foundation for modifying the provided Terraform for related exercises.
    Estimated time to complete is about 60 minutes.
  faqs:
  - question: What do I need before running the Terraform steps?
    answer: >-
      You need an AWS account and a computer with Terraform installed. Any computer with the required
      tools can be used.
  - question: Does this path use Terraform Cloud or local Terraform?
    answer: >-
      The steps use Terraform Cloud to automate the creation of Arm instances. Follow the instructions
      in the path to run the workflow in Terraform Cloud.
  - question: What infrastructure gets created by the configuration?
    answer: >-
      It provisions AWS EC2 Arm instances (Graviton) and sets up access through a Jump Server
      (bastion). The Jump Server provides a supervised, secure channel between networks.
  - question: How do I access the deployed instances?
    answer: >-
      Access is provided via the Jump Server (bastion). Traffic is funneled through this intermediary
      host to add a security barrier between networks.
  - question: Can I reuse or modify the Terraform files for other Learning Paths?
    answer: >-
      Yes. The Terraform files are intended as a platform you can adapt to support other Learning
      Paths that require one or more server nodes.
# END generated_summary_faq

author: Jason Andrews

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
cloud_service_providers:
  - AWS
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Terraform
    - Bastion

further_reading:
    - resource:
        title: Terraform docs for AWS
        link: https://registry.terraform.io/providers/hashicorp/aws/latest/docs
        type: documentation
    - resource:
        title: Amazon EC2 C7g Instances, Powered by AWS Graviton3 Processors
        link: https://aws.amazon.com/blogs/aws/new-amazon-ec2-c7g-instances-powered-by-aws-graviton3-processors/
        type: Blog



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


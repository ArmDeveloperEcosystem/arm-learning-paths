---
title: Deploy Arm Instances on AWS using Terraform
description: Learn how to automate the creation and deployment of AWS Graviton instances using Terraform with jump server access for secure infrastructure management.

minutes_to_complete: 60   

who_is_this_for: This is an introductory topic for software developers who are new to deploying Arm instances on AWS using Terraform.

learning_objectives: 
    - Automate Amazon EC2 instance creation using Terraform
    - Deploy Arm instances on AWS and provide access via Jump Server
    - Provide infrastructure basics, code knowledge and files that could help with future learning paths

prerequisites:
    - An Amazon Web Services (AWS) [account](https://aws.amazon.com/)
    - A computer with [Terraform](/install-guides/terraform) installed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-26T17:39:51Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 087a4d56914e5b53cec5ad17e8d682e72d04ba6b394237c081efe4a3f939e04e
  summary_generated_at: '2026-06-26T17:39:51Z'
  summary_source_hash: 087a4d56914e5b53cec5ad17e8d682e72d04ba6b394237c081efe4a3f939e04e
  faq_generated_at: '2026-06-26T17:39:51Z'
  faq_source_hash: 087a4d56914e5b53cec5ad17e8d682e72d04ba6b394237c081efe4a3f939e04e
  summary: >-
    You'll define and apply Terraform automation to provision AWS Graviton-based EC2
    instances and expose secure access through a jump server, also known as a bastion host. First, you'll
    review the provided Terraform files, run the workflow using Terraform Cloud, and adapt the
    configuration as needed to fit related projects. You'll learn a practical pattern:
    create Arm-based EC2 instances, place a supervised access point in front, and validate that
    the deployed nodes are reachable only through the jump server. The resulting configuration
    provides a reusable baseline for future Arm-focused work on AWS that requires one or more
    server nodes.
  faqs:
  - question: Can I run the steps from any machine?
    answer: >-
      Yes. Any computer with the required tools installed can be used, including a desktop, laptop,
      or virtual machine.
  - question: Should I use Terraform Cloud or the local CLI for this workflow?
    answer: >-
      This Learning Path uses Terraform Cloud to automate the creation of Arm instances. Follow
      the steps that reference Terraform Cloud to run the provisioning.
  - question: How do I know the provisioned instances are Arm-based (Graviton)?
    answer: >-
      The configuration in this Learning Path provisions Arm instances. After `apply`, check the
      instance details in AWS or the resource attributes shown by Terraform to confirm the architecture.
  - question: What result should I expect after applying the Terraform configuration?
    answer: >-
      You should see one or more AWS instances created and a jump server configured to broker
      access. Verify that the resources are present in AWS and that the jump server is the access
      point.
  - question: What should I modify to reuse this setup for other Learning Paths?
    answer: >-
      Use the provided Terraform files as a starting point and adjust them to match the needs
      of the other activity. Keep the jump server pattern and update the configuration where needed
      to align with your target environment.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

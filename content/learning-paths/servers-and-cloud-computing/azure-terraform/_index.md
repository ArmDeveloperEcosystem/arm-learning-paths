---
title: Deploy Arm virtual machines on Microsoft Azure with Terraform

description: Learn how to automate the creation of Azure Arm virtual machines using Terraform

minutes_to_complete: 60   

who_is_this_for: This is an introductory topic for software developers who are new to deploying Arm instances on Azure using Terraform.

learning_objectives: 
    - Automate Arm virtual machine creation using Terraform
    - Deploy Arm VMs on Azure and provide access via Jump Server
    - Provide infrastructure basics, code knowledge and files that could help with future learning paths

prerequisites:
    - An Azure account
    - A computer with Terraform installed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-26T18:35:34Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 6713af3d70887933cf54c7fa36bdc88d71a51fa34fb29a4ce90636ff1de624c7
  summary_generated_at: '2026-06-26T18:35:34Z'
  summary_source_hash: 6713af3d70887933cf54c7fa36bdc88d71a51fa34fb29a4ce90636ff1de624c7
  faq_generated_at: '2026-06-26T18:35:34Z'
  faq_source_hash: 6713af3d70887933cf54c7fa36bdc88d71a51fa34fb29a4ce90636ff1de624c7
  summary: >-
    In this Learning Path, you provision Arm virtual machines on Microsoft Azure using Terraform
    Cloud and expose controlled access through a jump server, also known as a bastion host. You
    work with provided Terraform files to instantiate Arm instances, apply the configuration, and
    verify the deployment in Azure. You learn how a jump server supports secure access and how
    the Terraform code provides a reusable base for future Learning Paths that require
    one or more server nodes. By the end, you have deployed Arm VMs accessible through the jump
    server and know how to adapt the infrastructure-as-code for related exercises.
  faqs:
  - question: Can I run the steps from any machine?
    answer: >-
      Yes. Any computer with the required tools installed can be used, including a desktop, laptop,
      or a virtual machine.
  - question: Do I need to use Terraform Cloud for this Learning Path?
    answer: >-
      Yes. The steps use Terraform Cloud to automate the creation of Arm instances on Azure.
  - question: What result should I expect when Terraform finishes applying?
    answer: >-
      A successful `apply` creates the Arm virtual machines in Azure and the associated access through
      the jump server. You can verify the resources in the Azure portal.
  - question: Are the Terraform files provided here reusable for other Learning Paths?
    answer: >-
      Yes. The files are intended as a platform you can modify to support other Learning Paths
      that need one or more server nodes.
  - question: Do these steps apply to Linux and Windows on Arm?
    answer: >-
      Yes. Use these instructions to deploy Linux, and see the related references for deploying
      Windows on Arm on Azure.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
cloud_service_providers:
  - Microsoft Azure

armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Terraform
    - Bastion

further_reading:
    - resource:
        title: Terraform on Azure
        link: https://www.udemy.com/course/terraform-on-azure-basic-tutorial
        type: Tutorial
    - resource:
        title: Azure Virtual Machines with Ampere Altra Arm–based processors—generally available
        link: https://azure.microsoft.com/en-us/blog/azure-virtual-machines-with-ampere-altra-arm-based-processors-generally-available/
        type: Blog
    - resource:
        title: About Azure bastion
        link: https://learn.microsoft.com/en-us/azure/bastion/bastion-overview
        type: Documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

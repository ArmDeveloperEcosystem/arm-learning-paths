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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:23:24Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 6713af3d70887933cf54c7fa36bdc88d71a51fa34fb29a4ce90636ff1de624c7
  summary_generated_at: '2026-06-02T03:10:40Z'
  summary_source_hash: 6713af3d70887933cf54c7fa36bdc88d71a51fa34fb29a4ce90636ff1de624c7
  faq_generated_at: '2026-06-03T00:23:24Z'
  faq_source_hash: 6713af3d70887933cf54c7fa36bdc88d71a51fa34fb29a4ce90636ff1de624c7
  summary: >-
    This Learning Path shows how to automate the creation of Arm-based virtual machines on Microsoft
    Azure using Terraform and Terraform Cloud. You will deploy Azure Arm VMs (Neoverse) and configure
    access through a Jump Server (bastion host), using provided Terraform code you can adapt for
    future Learning Paths. The steps require an Azure account and a computer with Terraform installed;
    any desktop, laptop, or VM with the required tools will work. Positioned as an introductory
    topic for developers new to deploying Arm instances on Azure with Terraform, the same instructions
    can be used to deploy Linux as well. By the end, you will have automated infrastructure and
    a controlled access path to your instances.
  faqs:
  - question: What do I need before running the Terraform steps?
    answer: >-
      You need an Azure account and a computer with Terraform installed. Any desktop, laptop,
      or virtual machine with the required tools can be used. You will also need access to the
      Azure portal.
  - question: Which Terraform workflow does this Learning Path use?
    answer: >-
      It uses Terraform Cloud to automate the instantiation of Arm instances on Azure. The provided
      Terraform files form the basis of the deployment.
  - question: Can I deploy Linux or Windows on Arm with these instructions?
    answer: >-
      The same instructions can be used to deploy Linux. A related guide for deploying a Windows
      on Arm virtual machine on Microsoft Azure is referenced.
  - question: How is access to the deployed VMs provided?
    answer: >-
      Access is provided via a Jump Server (also known as a bastion host). The Jump Server funnels
      traffic through firewalls using a supervised secure channel to create a barrier between
      networks.
  - question: What should I expect to have at the end of this Learning Path?
    answer: >-
      You will have Arm virtual machines deployed on Azure and access set up through a Jump Server.
      You will also have Terraform files that you can modify and reuse as a platform for other
      Learning Paths.
# END generated_summary_faq

author: Jason Andrews

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


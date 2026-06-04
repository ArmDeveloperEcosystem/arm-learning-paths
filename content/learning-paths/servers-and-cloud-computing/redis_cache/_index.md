---
title: Deploy Redis as a cache for MySQL and PostgreSQL on Arm servers

minutes_to_complete: 90   

who_is_this_for: This is an advanced topic for developers who want to deploy Redis as a cache on Arm based virtual machines.

learning_objectives: 
    - Deploy Redis as a cache for MySQL on AWS, Azure and GCP Arm based instance
    - Deploy Redis as a cache for Postgres on AWS, Azure and GCP Arm based instance

prerequisites:
    - An Amazon Web Services (AWS) [account](https://aws.amazon.com/)
    - An Azure portal [account](https://azure.microsoft.com/en-in/get-started/azure-portal)
    - A Google Cloud [account](https://console.cloud.google.com/)
    - A machine with [Terraform](/install-guides/terraform/), [AWS CLI](/install-guides/aws-cli), [Google Cloud CLI](/install-guides/gcloud), [Azure CLI](/install-guides/azure-cli), [AWS IAM authenticator](https://docs.aws.amazon.com/eks/latest/userguide/install-aws-iam-authenticator.html), and [Ansible](/install-guides/ansible/) installed

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:59:56Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 9146285feb38ee45171ac234f605eee08467bbf675a77df231a6dc63c38282f2
  summary_generated_at: '2026-06-02T04:59:18Z'
  summary_source_hash: 9146285feb38ee45171ac234f605eee08467bbf675a77df231a6dc63c38282f2
  faq_generated_at: '2026-06-03T01:59:56Z'
  faq_source_hash: 9146285feb38ee45171ac234f605eee08467bbf675a77df231a6dc63c38282f2
  summary: >-
    Deploy Redis as a cache for MySQL and PostgreSQL on Arm Neoverse-based Linux virtual machines
    across AWS, Microsoft Azure, and Google Cloud. Using Terraform and Ansible, you will provision
    cloud instances and configure Redis as a caching layer for your databases. The path provides
    provider-specific sections; MySQL deployments are covered on AWS, Azure, and GCP, and PostgreSQL
    deployments on AWS and Azure. Prerequisites include active accounts on the three clouds and
    a machine with Terraform, AWS CLI, Google Cloud CLI, Azure CLI, AWS IAM authenticator, and
    Ansible installed. Expect to complete the hands-on steps in about 90 minutes and finish with
    repeatable automation for your target platform.
  faqs:
  - question: What do I need before running the deployment steps?
    answer: >-
      You need AWS, Azure, and Google Cloud accounts, plus Terraform, AWS CLI, Azure CLI, Google
      Cloud CLI, AWS IAM authenticator, and Ansible installed. You can run the steps from any
      computer that has these tools installed.
  - question: Which section should I follow for my database and cloud provider?
    answer: >-
      Use the MySQL sections for AWS, Azure, or Google Cloud. Use the PostgreSQL sections for
      AWS or Azure.
  - question: I am new to Terraform—what should I read before starting?
    answer: >-
      Each section references an introductory guide: Automate AWS EC2 instance creation using
      Terraform, Automate Azure instance creation using Terraform, or Automate GCP instance creation
      using Terraform. Review the guide that matches your target cloud before proceeding.
  - question: What result should I expect, and how long will it take?
    answer: >-
      Expect a provisioned Arm-based Linux instance on your chosen cloud with Redis configured
      as a cache for the selected database. The Learning Path is designed to take approximately
      90 minutes.
  - question: Is there a section for deploying Redis as a cache for PostgreSQL on Google Cloud?
    answer: >-
      A PostgreSQL section for Google Cloud is not explicitly listed in the provided steps. Follow
      the available PostgreSQL sections for AWS or Azure.
# END generated_summary_faq

author: Jason Andrews
### Tags
skilllevels: Advanced
subjects: Databases
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Terraform
    - Ansible
    - Redis
    - SQL
    - MySQL
    - Runbook


further_reading:
    - resource:
        title: Redis documentation
        link: https://redis.io/docs/
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


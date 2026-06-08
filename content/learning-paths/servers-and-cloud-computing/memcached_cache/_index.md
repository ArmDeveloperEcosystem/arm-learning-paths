---
title: Deploy Memcached as a cache for MySQL and PostgreSQL on Arm based servers


description: Deploy Memcached as a cache for MySQL and PostgreSQL on Arm servers

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for developers who want to use memcached as their in-memory key-value store.

learning_objectives:
- Deploy memcached as a cache for MySQL on AWS, Azure and GCP Arm based Instance
- Deploy memcached as a cache for PostgreSQL on AWS, Azure and GCP Arm based Instance

prerequisites:
- An Amazon Web Services (AWS) [account](https://aws.amazon.com/)
- An Azure portal [account](https://azure.microsoft.com/en-in/get-started/azure-portal)
- A Google Cloud [account](https://console.cloud.google.com/)
- A machine with [Terraform](/install-guides/terraform/), [AWS CLI](/install-guides/aws-cli), [Google Cloud CLI](/install-guides/gcloud), [Azure CLI](/install-guides/azure-cli), [AWS IAM authenticator](https://docs.aws.amazon.com/eks/latest/userguide/install-aws-iam-authenticator.html), and [Ansible](/install-guides/ansible/) installed

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:27:30Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 4efe46aaf4580a6b8f263b69e8f072211bfd24fcf7f7a885689c927fc05a4c63
  summary_generated_at: '2026-06-02T04:20:49Z'
  summary_source_hash: 4efe46aaf4580a6b8f263b69e8f072211bfd24fcf7f7a885689c927fc05a4c63
  faq_generated_at: '2026-06-03T01:27:30Z'
  faq_source_hash: 4efe46aaf4580a6b8f263b69e8f072211bfd24fcf7f7a885689c927fc05a4c63
  summary: >-
    Learn how to deploy Memcached as a cache for MySQL and PostgreSQL on Arm-based cloud instances
    using Terraform and Ansible. You will provision Linux instances on AWS, Microsoft Azure, and
    Google Cloud, then install and configure Memcached to serve as a cache layer for your database
    workload. The path includes sections for MySQL on AWS, Azure, and GCP, and for PostgreSQL
    on AWS and Azure; PostgreSQL on GCP is not explicitly listed in the provided steps. No explicit
    prior Terraform knowledge is required, but related automation guides are referenced. Prerequisites
    include cloud accounts and a machine with Terraform, AWS CLI, Google Cloud CLI, Azure CLI,
    AWS IAM authenticator, and Ansible installed. Estimated time to complete is 60 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need AWS, Azure, and Google Cloud accounts, and a machine with Terraform, AWS CLI, Google
      Cloud CLI, Azure CLI, AWS IAM authenticator, and Ansible installed. These tools are required
      to provision infrastructure and configure Memcached.
  - question: Which database and cloud combinations are covered in the sections?
    answer: >-
      MySQL on AWS, Azure, and Google Cloud Arm-based instances, and PostgreSQL on AWS and Azure.
      PostgreSQL on Google Cloud is listed in the objectives but is not explicitly shown in the
      provided section excerpts.
  - question: Where do I run Terraform and Ansible from?
    answer: >-
      From any computer that has the required tools installed; a desktop or laptop is suitable.
      The deployed target instances run Linux.
  - question: I'm new to Terraform—what should I read first?
    answer: >-
      Each cloud-specific section recommends reviewing the corresponding “Automate [cloud] instance
      creation using Terraform” guide before you start. Use the AWS, Azure, or GCP guide referenced
      by the section you plan to follow.
  - question: What result should I expect after completing a section?
    answer: >-
      A running Arm-based cloud instance with Memcached configured to act as a cache for the chosen
      database (MySQL or PostgreSQL). The deployment is performed with Terraform and configured
      with Ansible as described in the section.
# END generated_summary_faq

author: Pareena Verma


test_images:
- ubuntu:latest
test_link: https://github.com/armflorentlebeau/arm-learning-paths/actions/runs/4312122327
test_maintenance: true

### Tags
skilllevels: Advanced
subjects: Web
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
armips:
- Neoverse
tools_software_languages:
- Memcached
- SQL
- MySQL
- PostgreSQL
operatingsystems:
- Linux

further_reading:
    - resource:
        title: Memcached Wiki
        link: https://github.com/memcached/memcached/wiki
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


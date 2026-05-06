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

generate_summary_faq: true

# rerun_summary: false
# rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:58Z'
  generator: template
  source_hash: 4efe46aaf4580a6b8f263b69e8f072211bfd24fcf7f7a885689c927fc05a4c63
  summary: >-
    Deploy Memcached as a cache for MySQL and PostgreSQL on Arm servers. It is designed for developers
    who want to use memcached as their in-memory key-value store. By the end, you will be able
    to deploy memcached as a cache for MySQL on AWS, Azure and GCP Arm based Instance and deploy
    memcached as a cache for PostgreSQL on AWS, Azure and GCP Arm based Instance. It focuses on
    tools and technologies such as Memcached, SQL, MySQL, and PostgreSQL, Linux environments,
    Arm platforms including Neoverse, and cloud platforms such as AWS, Microsoft Azure, and Google
    Cloud. The main steps cover Deploy Memcached as a cache for MySQL on an AWS Arm based Instance,
    Deploy Memcached as a cache for MySQL on an Azure Arm based Instance, Deploy Memcached as
    a cache for MySQL on a Google Cloud Arm based Instance, Deploy Memcached as a cache for Postgres
    on an AWS Arm based Instance, and Deploy Memcached as a cache for Postgres on an Azure Arm
    based Instance.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will deploy memcached as a cache for MySQL on AWS, Azure and GCP Arm based Instance
      and deploy memcached as a cache for PostgreSQL on AWS, Azure and GCP Arm based Instance.
      Deploy Memcached as a cache for MySQL and PostgreSQL on Arm servers.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for developers who want to use memcached as their in-memory key-value
      store.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An Amazon Web Services (AWS) [account](https://aws.amazon.com/);
      An Azure portal [account](https://azure.microsoft.com/en-in/get-started/azure-portal); A
      Google Cloud [account](https://console.cloud.google.com/); A machine with [Terraform](/install-guides/terraform/),
      [AWS CLI](/install-guides/aws-cli), [Google Cloud CLI](/install-guides/gcloud), [Azure CLI](/install-guides/azure-cli),
      [AWS IAM authenticator](https://docs.aws.amazon.com/eks/latest/userguide/install-aws-iam-authenticator.html),
      and [Ansible](/install-guides/ansible/) installed.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Memcached, SQL, MySQL, and PostgreSQL, Linux environments,
      Arm platforms such as Neoverse, and cloud platforms such as AWS, Microsoft Azure, and Google
      Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Deploy Memcached as a cache for MySQL on an AWS Arm
      based Instance, Deploy Memcached as a cache for MySQL on an Azure Arm based Instance, Deploy
      Memcached as a cache for MySQL on a Google Cloud Arm based Instance, Deploy Memcached as
      a cache for Postgres on an AWS Arm based Instance, and Deploy Memcached as a cache for Postgres
      on an Azure Arm based Instance.
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


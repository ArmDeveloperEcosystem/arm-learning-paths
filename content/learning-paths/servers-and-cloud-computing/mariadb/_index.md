---
title: Deploy MariaDB on Arm servers

minutes_to_complete: 90   

who_is_this_for: This is an introductory topic for software developers who want to deploy MariaDB on Arm servers.

description: Deploy MariaDB on Arm cloud instances across AWS, Azure, and Google Cloud using Docker, Amazon RDS, and automation with Terraform and Ansible.

learning_objectives: 
    - Deploy MariaDB on virtual machines from different cloud service providers 
    - Deploy MariaDB using Docker
    - Deploy MariaDB using Amazon RDS (Relational Database Service)
    - Automate MariaDB EC2 instance creation using Terraform and Ansible

prerequisites:
    - Cloud service provider accounts for each service you want to use including AWS, Azure, and GCP
    - A local computer with [Docker](/install-guides/docker/), [Terraform](/install-guides/terraform/), [AWS CLI](/install-guides/aws-cli/), [Azure CLI](/install-guides/azure-cli/), [Google Cloud CLI](/install-guides/gcloud/), and [Ansible](/install-guides/ansible/) installed

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:18Z'
  generator: template
  source_hash: db4ce1c59ad10bd127b4990c82ce876311d7dc7e1ad5d39ec132daf82ceb8b79
  summary: >-
    Deploy MariaDB on Arm cloud instances across AWS, Azure, and Google Cloud using Docker, Amazon
    RDS, and automation with Terraform and Ansible. It is designed for software developers who
    want to deploy MariaDB on Arm servers. By the end, you will be able to deploy MariaDB on virtual
    machines from different cloud service providers, deploy MariaDB using Docker, and deploy MariaDB
    using Amazon RDS (Relational Database Service). It focuses on tools and technologies such
    as Terraform, Ansible, MariaDB, Docker, and Runbook, Linux environments, Arm platforms including
    Neoverse, and cloud platforms such as AWS, Microsoft Azure, and Google Cloud. The main steps
    cover Install MariaDB on an AWS Arm based instance, Deploy MariaDB using RDS(AWS), Install
    MariaDB on an Azure Arm based instance, Install MariaDB on a GCP Arm based instance, and Deploy
    MariaDB via Docker.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will deploy MariaDB on virtual machines from different cloud service providers, deploy
      MariaDB using Docker, and deploy MariaDB using Amazon RDS (Relational Database Service).
      Deploy MariaDB on Arm cloud instances across AWS, Azure, and Google Cloud using Docker,
      Amazon RDS, and automation with Terraform and Ansible.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for software developers who want to deploy MariaDB on Arm
      servers.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: Cloud service provider accounts for
      each service you want to use including AWS, Azure, and GCP; A local computer with [Docker](/install-guides/docker/),
      [Terraform](/install-guides/terraform/), [AWS CLI](/install-guides/aws-cli/), [Azure CLI](/install-guides/azure-cli/),
      [Google Cloud CLI](/install-guides/gcloud/), and [Ansible](/install-guides/ansible/) installed.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Terraform, Ansible, MariaDB, Docker, and Runbook,
      Linux environments, Arm platforms such as Neoverse, and cloud platforms such as AWS, Microsoft
      Azure, and Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Install MariaDB on an AWS Arm based instance, Deploy
      MariaDB using RDS(AWS), Install MariaDB on an Azure Arm based instance, Install MariaDB
      on a GCP Arm based instance, and Deploy MariaDB via Docker.
# END generated_summary_faq

author: Jason Andrews
### Tags
skilllevels: Introductory
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
    - MariaDB
    - Docker
    - Runbook


further_reading:
    - resource:
        title: MariaDB Manual
        link: https://mariadb.org/documentation/ 
        type: documentation
    - resource:
        title: RDS
        link: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MariaDB.html 
        type: documentation
    - resource:
        title: Ansible
        link: https://docs.ansible.com/
        type: documentation
    - resource:
        title: Key considerations in moving to Graviton2 for Amazon RDS and Amazon Aurora databases
        link: https://aws.amazon.com/blogs/database/key-considerations-in-moving-to-graviton2-for-amazon-rds-and-amazon-aurora-databases/
        type: blog


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


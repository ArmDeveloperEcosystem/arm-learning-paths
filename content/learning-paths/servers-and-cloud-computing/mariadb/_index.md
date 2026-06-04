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

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:25:42Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: db4ce1c59ad10bd127b4990c82ce876311d7dc7e1ad5d39ec132daf82ceb8b79
  summary_generated_at: '2026-06-02T04:19:21Z'
  summary_source_hash: db4ce1c59ad10bd127b4990c82ce876311d7dc7e1ad5d39ec132daf82ceb8b79
  faq_generated_at: '2026-06-03T01:25:42Z'
  faq_source_hash: db4ce1c59ad10bd127b4990c82ce876311d7dc7e1ad5d39ec132daf82ceb8b79
  summary: >-
    Learn how to deploy MariaDB on Arm-based cloud infrastructure across AWS, Microsoft Azure,
    and Google Cloud using Terraform, Ansible, Docker, and Amazon RDS. You will provision single
    virtual machines on each provider with automation, deploy MariaDB in a Docker container using
    Ansible, and create a managed MariaDB database with Amazon RDS via Terraform. The steps target
    Linux hosts and assume cloud accounts for the services you plan to use. Work from a local
    computer with Docker, Terraform, the AWS/Azure/Google Cloud CLIs, and Ansible installed. This
    introductory path takes about 90 minutes and results in MariaDB running on Arm servers and
    as a managed RDS service.
  faqs:
  - question: What do I need installed locally before starting?
    answer: >-
      Install Docker, Terraform, AWS CLI, Azure CLI, Google Cloud CLI, and Ansible on your local
      computer. You also need cloud accounts for the services you plan to use.
  - question: Can I follow only the sections for the cloud provider I use?
    answer: >-
      Yes. The Learning Path includes AWS, Azure, and GCP; complete the sections that match the
      accounts and services you have available.
  - question: Which tools does each deployment method use?
    answer: >-
      EC2, Azure, and GCP VM deployments use Terraform and Ansible to provision a single Arm-based
      instance and install MariaDB. The Amazon RDS section uses Terraform. The Docker section
      uses Ansible to deploy a MariaDB container.
  - question: What additional setup is required for the Docker-based deployment?
    answer: >-
      You need a cloud instance, VM, or physical machine with Ubuntu installed, running, and ready
      to deploy MariaDB. Ansible must be installed locally, and you can reuse the same SSH key
      pair.
  - question: What credentials are required for the Amazon RDS section?
    answer: >-
      An AWS account is required along with an AWS access key ID and secret access key. You also
      need Terraform and the AWS CLI installed on the computer you use to run the steps.
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


---
title: Deploy MariaDB on Arm servers

minutes_to_complete: 90   

who_is_this_for: This is an introductory topic for software developers who want to deploy MariaDB on Arm servers.

description: Deploy MariaDB on Arm cloud instances across Amazon Web Services (AWS), Azure, and Google Cloud Platform (GCP) using Docker, Amazon RDS, and automation with Terraform and Ansible.

learning_objectives: 
    - Deploy MariaDB on virtual machines (VMs) from different cloud service providers. 
    - Deploy MariaDB using Docker.
    - Deploy MariaDB using Amazon Relational Database Service (RDS).
    - Automate MariaDB EC2 instance creation using Terraform and Ansible. 

prerequisites:
    - Cloud service provider accounts for each service you want to use including AWS, Azure, and GCP
    - A local computer with [Docker](/install-guides/docker/), [Terraform](/install-guides/terraform/), [AWS CLI](/install-guides/aws-cli/), [Azure CLI](/install-guides/azure-cli/), [Google Cloud CLI](/install-guides/gcloud/), and [Ansible](/install-guides/ansible/) installed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-28T19:46:18Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 6ae54841912ce9e663138b616884d6c8ea8bce168608273955b4a99efc256875
  summary_generated_at: '2026-09-28T19:46:18Z'
  summary_source_hash: 6ae54841912ce9e663138b616884d6c8ea8bce168608273955b4a99efc256875
  faq_generated_at: '2026-09-28T19:46:18Z'
  faq_source_hash: 6ae54841912ce9e663138b616884d6c8ea8bce168608273955b4a99efc256875
  summary: >-
    You'll deploy MariaDB on Arm-based cloud infrastructure with Terraform and Ansible. After provisioning a
    virtual machine on AWS Graviton, Azure Cobalt, or Google Axion, you'll automate MariaDB configuration.
    You can also create a managed MariaDB instance on Amazon RDS or run MariaDB in a Docker container
    on Ubuntu. By following provider-specific instructions for your environment, you'll build a repeatable
    deployment that matches your preferred operating model.
  faqs:
  - question: What Learning Paths should I review before provisioning instances?
    answer: >-
      Review provider-specific Learning Paths, such as [Automate Amazon EC2 instance creation using Terraform](/learning-paths/servers-and-cloud-computing/aws-terraform/terraform/), [Automate Azure instance creation using Terraform](/learning-paths/servers-and-cloud-computing/azure-terraform/terraform/),
      and [Automate GCP instance creation using Terraform](/learning-paths/servers-and-cloud-computing/gcp/terraform/).
  - question: Which option should I use if I want a managed MariaDB service instead of managing
      VMs?
    answer: >-
      Deploy MariaDB using Amazon RDS with
      Terraform, so that you don’t have to manage the database on a VM.
  - question: What credentials do I need before running the deployment on Amazon RDS?
    answer: >-
      You need an AWS account along with an AWS access key ID and secret access key.
  - question: What result should I expect after completing an AWS, Azure, or GCP deployment?
    answer: >-
      You should have one Arm-based VM on your chosen cloud provider with MariaDB
      configured by Ansible.
  - question: What do I need for the Docker-based deployment?
    answer: >-
     For the Docker deployment, use an Ubuntu cloud instance,
      VM, or physical machine, then run Ansible from your control machine.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Databases
platforms:
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
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

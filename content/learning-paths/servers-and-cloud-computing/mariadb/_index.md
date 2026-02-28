---
title: Deploy MariaDB on Arm servers

minutes_to_complete: 90   

who_is_this_for: This is an introductory topic for software developers who want to deploy MariaDB on Arm servers.

learning_objectives: 
    - Deploy MariaDB on virtual machines from different cloud service providers 
    - Deploy MariaDB using Docker
    - Deploy MariaDB using Amazon RDS (Relational Database Service)
    - Automate MariaDB EC2 instance creation using Terraform and Ansible

prerequisites:
    - Cloud service provider accounts for each service you want to use including AWS, Azure, and GCP
    - A local computer with [Docker](/install-guides/docker/), [Terraform](/install-guides/terraform/), [AWS CLI](/install-guides/aws-cli/), [Azure CLI](/install-guides/azure-cli/), [Google Cloud CLI](/install-guides/gcloud/), and [Ansible](/install-guides/ansible/) installed

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

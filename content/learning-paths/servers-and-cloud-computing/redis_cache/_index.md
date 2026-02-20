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

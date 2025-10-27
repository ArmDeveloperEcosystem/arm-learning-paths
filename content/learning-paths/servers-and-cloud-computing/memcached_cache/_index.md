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

author: Pareena Verma


test_images:
- ubuntu:latest
test_link: https://github.com/armflorentlebeau/arm-learning-paths/actions/runs/4312122327
test_maintenance: true

### Tags
skilllevels: Advanced
subjects: Web
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

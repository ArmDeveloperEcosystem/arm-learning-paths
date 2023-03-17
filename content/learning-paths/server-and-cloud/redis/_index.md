---
title: Deploying Redis on Arm

minutes_to_complete: 60   

who_is_this_for: This is an advanced topic for anyone who wants to deploy Redis.

learning_objectives: 
    - Understand Redis deployment configurations
    - Install Redis on a single AWS Arm based instance
    - Install Redis on a single Azure Arm based instance
    - Install Redis on a single GCP Arm based instance
    - Install Redis with a docker container on a single node
    - Install Redis in a multi-node configuration (sharding)

prerequisites:
    - An Amazon Web Services (AWS) [account](https://aws.amazon.com/)
    - An Azure portal [account](https://azure.microsoft.com/en-in/get-started/azure-portal)
    - A Google Cloud [account](https://console.cloud.google.com/?hl=en-au)
    - A machine with [Terraform](/install-tools/terraform/), [AWS CLI](/install-tools/aws-cli), [Google Cloud CLI](/install-tools/gcloud), [Azure CLI](/install-tools/azure-cli), [AWS IAM authenticator](https://docs.aws.amazon.com/eks/latest/userguide/install-aws-iam-authenticator.html), and [Ansible](/install-tools/ansible/) installed

author_primary: Jason Andrews
### Tags
skilllevels: Introductory
subjects: Databases
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Terraform
    - Ansible

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


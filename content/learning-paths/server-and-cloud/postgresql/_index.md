---
title: Learn how to deploy PostgreSQL on AWS 

minutes_to_complete: 60   

who_is_this_for: This is an advanced topic for anyone who wants to deploy PostgreSQL on AWS Graviton processors.

learning_objectives: 
    - Automate PostgreSQL EC2 instance creation using Terraform and Ansible
    - Deploy a single instance of PostgreSQL on AWS Graviton 
    - Deploy a 3-node PostgreSQL cluster with two hot, read-only standby servers on AWS Graviton

prerequisites:
    - An Amazon Web Services (AWS) [account](https://aws.amazon.com/)
    - A machine with [Terraform](/install-tools/terraform/), [AWS CLI](/install-tools/aws-cli), [AWS IAM authenticator](https://docs.aws.amazon.com/eks/latest/userguide/install-aws-iam-authenticator.html), and [Ansible](/install-tools/ansible/) installed

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




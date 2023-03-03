---
title: "Deploy WordPress with MySQL on Elastic Kubernetes Service"

minutes_to_complete: 80

who_is_this_for: >
    This is an introductory topic for software developers new to AWS EC2, EKS, and Kubernetes.

learning_objectives:
    - Provision an EKS cluster on an Arm-based instance
    - Deploy Wordpress (with Mysql) on AWS Elastic Kubernetes Service

prerequisites:
    - [An Amazon Web Services (AWS) account](https://aws.amazon.com/)
    - [Terraform](install-tools/terraform/)
    - [The AWS CLI](install-tools/aws-cli/)
    - [The Kubernetes CLI also known as kubectl](install-tools/kubectl/)

author_primary: Jason Andrews

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Terraform
    - AWS CLI
    - kubectl

#       FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

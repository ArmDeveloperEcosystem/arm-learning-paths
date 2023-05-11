---
title: Deploy MySQL on Arm

minutes_to_complete: 30   

who_is_this_for: This is an introductory topic for software developers who want to deploy MySQL.

learning_objectives: 
    - Deploy single instance of MySQL through Docker, RDS and an AWS EC2
    - Deploy single instance of MySQL through an Azure
    - Deploy single instance of MySQL through GCP
    - Automate MySQL EC2 instance creation using Terraform and Ansible

prerequisites:
    - An [AWS account](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start). Create an account if needed.
    - A computer with [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) installed
    - A computer with [AWS IAM authenticator](https://docs.aws.amazon.com/eks/latest/userguide/install-aws-iam-authenticator.html) installed
    - A computer with [Ansible](https://www.cyberciti.biz/faq/how-to-install-and-configure-latest-version-of-ansible-on-ubuntu-linux/) installed
    - A computer with [Terraform](/install-guides/terraform) installed
    - A computer with [Docker](https://www.simplilearn.com/tutorials/docker-tutorial/how-to-install-docker-on-ubuntu) installed

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


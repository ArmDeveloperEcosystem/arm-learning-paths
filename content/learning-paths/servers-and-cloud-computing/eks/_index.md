---
title: "Deploy WordPress with MySQL on Elastic Kubernetes Service (EKS)"
description: Learn how to provision an Amazon EKS cluster on Arm-based Graviton instances and deploy a WordPress application with MySQL database.

minutes_to_complete: 60

who_is_this_for: >
    This is an introductory topic for software developers new to Kubernetes on AWS who want to gain experience with cloud applications.

learning_objectives:
    - Provision an Amazon Elastic Kubernetes Service (EKS) cluster on Arm-based instances
    - Deploy Wordpress with MySQL on EKS

prerequisites:
    - An Amazon Web Services (AWS) [account](https://aws.amazon.com/)

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:45:59Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 4f1c448eef66300e024bda27c420f9746047c0c4b76e8556d3d8693382206055
  summary_generated_at: '2026-06-02T03:42:15Z'
  summary_source_hash: 4f1c448eef66300e024bda27c420f9746047c0c4b76e8556d3d8693382206055
  faq_generated_at: '2026-06-03T00:45:59Z'
  faq_source_hash: 4f1c448eef66300e024bda27c420f9746047c0c4b76e8556d3d8693382206055
  summary: >-
    Provision an Amazon EKS cluster on Arm-based Graviton instances and deploy a WordPress application
    with a MySQL database. Working from a machine with the AWS CLI, EKS CLI, and Kubernetes CLI
    installed, you will configure AWS credentials, create the cluster, and use three Kubernetes
    YAML files (kustomization.yaml, mysql-deployment.yaml, and wordpress-deployment.yaml) to deploy
    the application with kubectl. The path is introductory and aimed at developers new to Kubernetes
    on AWS. It focuses on practical setup and deployment steps, including setting a MySQL password
    via Kustomize. An AWS account is required; no other explicit prerequisites are listed. Estimated
    time to complete is about 60 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an AWS account and must configure your AWS access key ID and secret access key.
      Install the EKS CLI, AWS CLI, and Kubernetes CLI, and confirm you can run the aws, ekscli,
      and kubectl commands.
  - question: Which machine can I use to run the setup?
    answer: >-
      Any computer with the required tools installed can be used. The operating system listed
      for this path is Linux.
  - question: How do I create an EKS cluster on Arm-based instances?
    answer: >-
      Follow the Create an EKS cluster step to provision an Amazon EKS cluster on Arm-based Graviton
      instances. You will use the EKS CLI together with the AWS CLI during this step.
  - question: Which files are required to deploy WordPress and where do I set the MySQL password?
    answer: >-
      You need kustomization.yaml, mysql-deployment.yaml, and wordpress-deployment.yaml. In kustomization.yaml,
      the secretGenerator named mysql-pass sets the database password using a literal such as
      password=YourPassword.
  - question: How do I apply the deployment and know it targets my EKS cluster?
    answer: >-
      Use kubectl with the kustomization.yaml that references the MySQL and WordPress resources.
      Ensure kubectl is configured to communicate with your newly created EKS cluster before applying
      the files.
# END generated_summary_faq

author: Jason Andrews

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
cloud_service_providers:
  - AWS
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - AWS Elastic Kubernetes Service (EKS)
    - Kubernetes
    - SQL
    - MySQL
    - WordPress

#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
    - resource:
        title: EKS documentation
        link: https://aws.amazon.com/eks/
        type: documentation
    - resource:
        title: Wordpress deployment documentation
        link: https://kubernetes.io/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/
        type: Blog


weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


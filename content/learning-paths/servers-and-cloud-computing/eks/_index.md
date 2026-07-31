---
title: Deploy WordPress with MySQL on Arm-based instances using Amazon EKS
description: Learn how to provision an Amazon EKS cluster on Arm-based Graviton instances and deploy a WordPress application with MySQL database.

minutes_to_complete: 60

who_is_this_for: >
    This is an introductory topic for software developers new to Kubernetes on AWS who want to gain experience with cloud applications.

learning_objectives:
    - Provision an Amazon Elastic Kubernetes Service (EKS) cluster on Arm-based instances
    - Deploy Wordpress with MySQL on EKS

prerequisites:
    - An Amazon Web Services (AWS) [account](https://aws.amazon.com/)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-28T15:05:40Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 6a3058af47e4fe4890928a8e2505a7833a0e1936977e092d3036bdbead2ce680
  summary_generated_at: '2026-07-28T15:05:40Z'
  summary_source_hash: 6a3058af47e4fe4890928a8e2505a7833a0e1936977e092d3036bdbead2ce680
  faq_generated_at: '2026-07-28T15:05:40Z'
  faq_source_hash: 6a3058af47e4fe4890928a8e2505a7833a0e1936977e092d3036bdbead2ce680
  summary: >-
   You’ll provision an Amazon EKS cluster on AWS Graviton instances and deploy WordPress with MySQL. You’ll validate access to the AWS CLI, `eksctl`, and `kubectl`, configure AWS credentials, and create Kubernetes manifests for the database and application. You’ll apply the manifests with `kubectl`, confirm that the workloads run, and finish with a basic, auditable WordPress deployment on EKS.
  faqs:
  - question: Can I use any machine to complete the steps?
    answer: >-
      Yes. You can use any desktop, laptop, or virtual machine that has the AWS CLI, `eksctl`,
      and `kubectl` installed and working.
  - question: How do I confirm the CLIs and my AWS credentials are ready?
    answer: >-
      Make sure you can run the `aws`, `eksctl`, and `kubectl` commands. Configure your AWS access key
      ID and secret access key so programmatic requests succeed.
  - question: Which YAML files do I need to deploy WordPress and what do they do?
    answer: >-
      Create `kustomization.yaml`, `mysql-deployment.yaml`, and `wordpress-deployment.yaml`. The `kustomization.yaml`
      sets the MySQL password and selects the two deployment files as resources.
  - question: How do I set the MySQL database password for the deployment?
    answer: >-
      Edit `kustomization.yaml` and set the `secretGenerator` literal password to your chosen value
      (`password=YourPassword`). This creates a Kubernetes Secret named `mysql-pass`.
  - question: What should I look for after applying the manifests?
    answer: >-
      Expect Kubernetes to create a Secret for the MySQL password and start the WordPress and
      MySQL workloads. Use `kubectl` to check that the WordPress and MySQL workloads appear and transition to a running
      state.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
    - Amazon EKS
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


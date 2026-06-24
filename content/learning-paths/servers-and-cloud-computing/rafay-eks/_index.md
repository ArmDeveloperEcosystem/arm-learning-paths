---
title: "Deploy an EKS cluster with Graviton nodes using Rafay"

description: Use the Rafay Kubernetes Operations Platform to provision an Amazon EKS cluster with an Arm Graviton node group and deploy NGINX to verify the setup.

draft: true
cascade:
    draft: true

minutes_to_complete: 60

who_is_this_for: >
    This is an advanced topic for software developers familiar with Kubernetes and AWS who want to learn how to use the Rafay platform to provision and manage EKS clusters backed by Arm Graviton instances.

learning_objectives:
    - Connect your AWS account to the Rafay platform using a cross-account IAM role
    - Provision an Amazon EKS cluster with an Arm Graviton node group using Rafay
    - Deploy and verify NGINX on Arm nodes and clean up all cloud resources

prerequisites:
    - An Amazon Web Services (AWS) [account](https://aws.amazon.com/)
    - A [Rafay account](https://rafay.co)
    - The [AWS CLI](/install-guides/aws-cli/) installed and configured

author: Jason Andrews

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
cloud_service_providers:
    - AWS
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Kubernetes
    - AWS Elastic Kubernetes Service (EKS)
    - Rafay
    - NGINX
    - rctl

#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
    - resource:
        title: Rafay CLI overview
        link: https://docs.rafay.co/cli/overview/
        type: documentation
    - resource:
        title: Amazon EKS documentation
        link: https://aws.amazon.com/eks/
        type: documentation
    - resource:
        title: AWS Graviton processors
        link: https://aws.amazon.com/ec2/graviton/
        type: documentation
    - resource:
        title: Kubernetes documentation
        link: https://kubernetes.io/docs/home/
        type: documentation

weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

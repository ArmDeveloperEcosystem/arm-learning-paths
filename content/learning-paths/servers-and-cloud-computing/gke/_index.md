---
title: Create an Arm-based Kubernetes cluster on Google Cloud Platform (GCP)
description: Learn how to automate the deployment of an Arm-based Google Kubernetes Engine cluster using Terraform for container orchestration.
 
minutes_to_complete: 60   

who_is_this_for: This is an advanced topic for software developers who want to deploy an Arm-based Kubernetes cluster using Google Kubernetes Engine (GKE).

learning_objectives:
    - Automate the deployment of an Arm-based GKE cluster using Terraform

prerequisites:
    - A Google Cloud account
    - A computer with the following tools installed`:` Terraform, Google Cloud CLI (gcloud), Kubernetes CLI (kubectl)

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:04:26Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 7c3d37545c93db584d6e0ce88d8feaf0bf690e0c8786b664a6643be713d0336f
  summary_generated_at: '2026-06-02T04:01:56Z'
  summary_source_hash: 7c3d37545c93db584d6e0ce88d8feaf0bf690e0c8786b664a6643be713d0336f
  faq_generated_at: '2026-06-03T01:04:26Z'
  faq_source_hash: 7c3d37545c93db584d6e0ce88d8feaf0bf690e0c8786b664a6643be713d0336f
  summary: >-
    Automate the creation of an Arm-based Kubernetes cluster on Google Cloud using Terraform.
    This advanced Learning Path focuses on deploying Google Kubernetes Engine (GKE) on Tau T2A
    virtual machines powered by Ampere Altra Arm-based processors. You will prepare a Linux environment
    with Terraform, the Google Cloud CLI (gcloud), and kubectl, create a new Google Cloud project,
    and use infrastructure-as-code to provision the cluster for container orchestration. The expected
    outcome is a deployed Arm-based GKE cluster managed via Terraform. Prerequisites are a Google
    Cloud account and a computer with Terraform, gcloud, and kubectl installed; no other prerequisites
    are explicitly listed.
  faqs:
  - question: What do I need before running the Terraform configuration?
    answer: >-
      You need a Google Cloud account and a computer with Terraform, Google Cloud CLI (gcloud),
      and kubectl installed. The Learning Path lists Linux as the operating system and notes that
      any computer with the required tools can be used.
  - question: How do I ensure the GKE nodes are Arm-based?
    answer: >-
      Configure the cluster to use the Tau T2A VM family in GKE. Tau T2A is powered by Ampere
      Altra Arm-based processors.
  - question: Will I create a new Google Cloud project or use an existing one?
    answer: >-
      The steps include creating a new Google Cloud project before provisioning the cluster with
      Terraform. Using an existing project is not explicitly listed.
  - question: What result should I expect when the Terraform apply completes?
    answer: >-
      A GKE cluster will be deployed on Google Cloud with Arm-based nodes (Tau T2A). You can then
      interact with the cluster using kubectl.
  - question: Does this Learning Path cover deploying workloads or only cluster creation?
    answer: >-
      The objective is to automate the deployment of an Arm-based GKE cluster using Terraform.
      Additional tasks such as deploying applications or tearing down the cluster are not explicitly
      listed.
# END generated_summary_faq

author: Jason Andrews

##### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
cloud_service_providers:
  - Google Cloud

armips:
    - Neoverse

tools_software_languages:
    - Terraform
    - Kubernetes

operatingsystems:
    - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
    - resource:
        title: Create Arm based clusters and node pools 
        link: https://cloud.google.com/kubernetes-engine/docs/how-to/create-arm-clusters-nodes
        type: documentation
    - resource:
        title: Configure cluster access to use kubectl
        link: https://cloud.google.com/kubernetes-engine/docs
        type: documentation
    - resource:
        title: GKE documentation
        link: https://cloud.google.com/kubernetes-engine/docs
        type: documentation


weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


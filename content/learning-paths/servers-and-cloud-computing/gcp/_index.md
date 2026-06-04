---
title: "Deploy Arm virtual machines on Google Cloud Platform (GCP) using Terraform"
description: Learn how to automate the creation of Arm virtual machines on Google Cloud Platform using Terraform with jump server access configuration.

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for anyone new to using Arm virtual machines in the Google Cloud Platform (GCP)

learning_objectives:
    - Automate Arm virtual machine creation using Terraform
    - Deploy Arm instances on GCP and provide access via Jump Server
    - Provide infrastructure basics, code knowledge and files that could help with future learning paths

prerequisites:
    - A [Google Cloud account](https://console.cloud.google.com/). Create an account if needed.
    - A computer with [Terraform](/install-guides/terraform) installed.
    - A computer with [Google Cloud CLI](/install-guides/gcloud) installed.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:00:09Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 24e2ffcf9b7cda919e6e864f18bb9424c0c328242c92f491c1b284e317ed7e1c
  summary_generated_at: '2026-06-02T03:58:46Z'
  summary_source_hash: 24e2ffcf9b7cda919e6e864f18bb9424c0c328242c92f491c1b284e317ed7e1c
  faq_generated_at: '2026-06-03T01:00:09Z'
  faq_source_hash: 24e2ffcf9b7cda919e6e864f18bb9424c0c328242c92f491c1b284e317ed7e1c
  summary: >-
    Learn to automate the deployment of Arm-based virtual machines on Google Cloud Platform using
    Terraform, with secure access configured through a Jump Server (bastion host). You will generate
    an SSH key pair, obtain GCP user credentials so Terraform can authenticate, and apply Terraform
    files that serve as a base for future Learning Paths that need one or more server nodes. This
    introductory, Linux-based path targets developers new to Arm VMs on GCP and takes about 20
    minutes. By the end, you will have Terraform-managed infrastructure that deploys Arm instances
    on GCP and provides access via a Jump Server, along with reusable Terraform code you can modify
    for related tasks.
  faqs:
  - question: What do I need before running the Terraform steps?
    answer: >-
      You need a Google Cloud account and a computer with Terraform and the Google Cloud CLI installed.
      These are the only explicit prerequisites listed.
  - question: Do I need to generate a new SSH key pair, and where should it be located?
    answer: >-
      Generate an SSH key pair with ssh-keygen if you do not already have one. If you have keys
      in the ~/.ssh directory, you can skip key generation and use the existing pair.
  - question: How do I authenticate Terraform with my Google Cloud project?
    answer: >-
      Obtain GCP user credentials by following the provided guide so Terraform can communicate
      with GCP. This authentication step is required before running Terraform.
  - question: What gets created when I apply the Terraform configuration?
    answer: >-
      The configuration deploys Arm-based virtual machine instances on GCP and provides access
      via a Jump Server (bastion). Any additional resources are not explicitly listed.
  - question: How do I access the deployed Arm instances after provisioning?
    answer: >-
      Use SSH via the Jump Server (bastion) with the SSH key pair you generated or reused. The
      Learning Path explains how to configure this bastion-based access.
# END generated_summary_faq

author: Jason Andrews

##### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
cloud_service_providers:
  - Google Cloud

armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Terraform
    - Bastion

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
    - resource:
        title: Create an Arm VM instance
        link: https://cloud.google.com/compute/docs/instances/create-arm-vm-instance#startinstanceconsole
        type: documentation
    - resource:
        title: Connect to Linux VMs 
        link: https://cloud.google.com/compute/docs/instances/connecting-to-instance#console
        type: documentation
    - resource:
        title: About bastion hosts
        link: https://cloud.google.com/solutions/connecting-securely#bastion
        type: documentation


weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


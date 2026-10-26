---
title: "Deploy Arm virtual machines on Google Cloud Platform (GCP) using Terraform"
description: Learn how to automate the creation of Arm virtual machines on Google Cloud Platform using Terraform with jump server access configuration.

minutes_to_complete: 20

who_is_this_for: This Learning Path is an introductory topic for developers using Arm virtual machines (VMs) in Google Cloud Platform (GCP).

learning_objectives:
    - Automate Arm VM creation using Terraform
    - Deploy Arm instances on GCP and provide access through Jump Server
    - Provide infrastructure basics, code knowledge, and files that can help with future Learning Paths

prerequisites:
    - A [Google Cloud account](https://console.cloud.google.com/)
    - Terraform [installed](/install-guides/terraform)
    - The [Google Cloud CLI](/install-guides/gcloud) installed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-10T22:03:24Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0e9f1da08af59f36c2d46866d499f15b34abe31093a2c8582dda85f717fb675c
  summary_generated_at: '2026-09-10T22:03:24Z'
  summary_source_hash: 0e9f1da08af59f36c2d46866d499f15b34abe31093a2c8582dda85f717fb675c
  faq_generated_at: '2026-09-10T22:03:24Z'
  faq_source_hash: 0e9f1da08af59f36c2d46866d499f15b34abe31093a2c8582dda85f717fb675c
  summary: >-
    You'll automate Arm VM provisioning on Google Cloud with Terraform and control access through a Jump Server. First, you'll create an SSH key pair, authenticate Terraform, and apply the configuration to create Google Axion instances. Then, you'll verify the deployment and connect through the bastion host to reach the target VMs.
  faqs:
  - question: What should I check about my SSH keys before I run Terraform?
    answer: >-
      Verify that a key pair exists in `~/.ssh`. If no key pair exists, generate a new pair and keep the
      private key secure. You'll use the private key to connect to the VMs created by Terraform.
  - question: How do I know I’m authenticated to GCP for Terraform?
    answer: >-
      Use the Google Cloud CLI to confirm an active account and project, then obtain user credentials. Terraform can communicate with GCP using those credentials.
  - question: What result should I expect after applying the Terraform configuration?
    answer: >-
      You should see new Arm-based instances and a Jump Server in the GCP console. You can SSH
      to the Jump Server with your private key and connect from there to the target instances.
  - question: How do I confirm the VMs are Arm-based on Google Cloud?
    answer: >-
      Open the instance details in the GCP console and check that the machine type indicates an
      Arm-based option, such as Google Axion.
  - question: How do I connect to the private instance through the Jump Server?
    answer: >-
      Run `ssh -J username@jump-host-IP username@target-server-IP`. Replace `jump-host-IP` with the
      bastion's external IP and `target-server-IP` with the private instance's internal IP. Use your
      IAM email address in the SSH username format (`abc@1234.com` -> `abc_1234_com`).
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

##### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
platforms:
  - Google Axion

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

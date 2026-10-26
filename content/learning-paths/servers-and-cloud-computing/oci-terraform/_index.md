---
title: Deploy Arm Instances on Oracle Cloud Infrastructure using Terraform

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for software developers who are new to deploying Arm instances on Oracle Cloud Infrastructure (OCI) using Terraform.

learning_objectives: 
    - Automate Arm virtual machine (VM) creation on OCI using Terraform

prerequisites:
    - An [OCI account](/learning-paths/servers-and-cloud-computing/csp/oci/)
    - A computer with Terraform installed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-01T19:41:27Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f927b34764047b05b4bd225ef1080f9cc345d6bd91ec8220fd23d710a478013d
  summary_generated_at: '2026-10-01T19:41:27Z'
  summary_source_hash: f927b34764047b05b4bd225ef1080f9cc345d6bd91ec8220fd23d710a478013d
  faq_generated_at: '2026-10-01T19:41:27Z'
  faq_source_hash: f927b34764047b05b4bd225ef1080f9cc345d6bd91ec8220fd23d710a478013d
  summary: >-
    You'll use Terraform to automate the creation of an Arm VM on 
    OCI Ampere Compute. First, you'll prepare a Linux control environment, then define the OCI resources as
    code and run the Terraform workflow to provision the instance. You can use the resulting
    configuration as a repeatable foundation for additional Arm infrastructure on OCI.
  faqs:
  - question: Which computer can I use to run Terraform?
    answer: >-
      You can use any computer with the required tools installed, including a desktop, laptop,
      or a virtual machine. The command format assumes that you're working on a Linux machine.
  - question: What are the OCI API keys and SSH keys used for?
    answer: >-
      The OCI API key pair is used to authenticate Terraform's requests to OCI. The
      SSH key pair is used to connect to the provisioned instance. Set `private_key_path` for the API
      private key and `ssh_authorized_keys_path` and `ssh_private_key_path` for your SSH keys.
  - question: How can I test OCI authentication before creating the VM?
    answer: >-
      Create `availability-domains.tf` with the provided data source and output definition, then
      run `terraform plan`. If authentication succeeds, you'll see the availability domains in your
      tenancy. Keep this file in the same directory as `provider.tf`.
  - question: How can I display the provisioned instance's public IP address?
    answer: >-
      Create `outputs.tf` with the provided `public_ip` output definition, which reads
      `oci_core_instance.Ampere.public_ip`. After provisioning the instance, run `terraform refresh`
      to display its public IP address.
  - question: What result should I expect after I complete the workflow?
    answer: >-
      You'll finish with an OCI Arm instance provisioned from your Terraform configuration.
# END generated_summary_faq

author: Frédéric -lefred- Descamps

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
platforms:
  - Oracle Cloud Infrastructure (OCI) Ampere Compute

armips:
    - Neoverse

operatingsystems:
    - Linux

tools_software_languages:
    - Terraform

further_reading:
    - resource:
        title: Terraform docs for OCI 
        link: https://registry.terraform.io/providers/oracle/oci/latest/docs
        type: documentation
    - resource:
        title: Arm-based cloud computing is the next big thing Introducing Arm on Oracle Cloud Infrastructure
        link: https://blogs.oracle.com/cloud-infrastructure/post/arm-based-cloud-computing-is-the-next-big-thing-introducing-arm-on-oracle-cloud-infrastructure
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

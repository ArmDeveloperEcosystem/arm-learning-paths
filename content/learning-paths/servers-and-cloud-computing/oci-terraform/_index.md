---
title: Deploy Arm Instances on Oracle Cloud Infrastructure (OCI) using Terraform

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for software developers who are new to deploying Arm instances on Oracle Cloud Infrastructure (OCI) using Terraform.

learning_objectives: 
    - Automate Arm virtual machine creation on OCI using Terraform

prerequisites:
    - An OCI account
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
    Use Terraform to automate the creation of an Arm virtual machine on Oracle Cloud Infrastructure
    (OCI) Ampere Compute. You prepare a Linux control environment, define the OCI resources as
    code, and run the Terraform workflow to provision the instance. You can use the resulting
    configuration as a repeatable foundation for additional Arm infrastructure on OCI.
  faqs:
  - question: Which computer can I use to run Terraform?
    answer: >-
      You can use any computer with the required tools installed, including a desktop, laptop,
      or a virtual machine. The command format assumes you are working on a Linux machine.
  - question: What do I need in OCI before I start?
    answer: >-
      Yes, you need an Oracle Cloud Infrastructure (OCI) account. If you are new to OCI, review
      the Getting Started with Oracle OCI Learning Path before you begin.
  - question: Where do I find installation instructions for Terraform?
    answer: >-
      See the Terraform install guide and follow its instructions on
      the computer you plan to use.
  - question: Can I use a virtual machine as my control environment for running Terraform?
    answer: >-
      Yes. A virtual machine with the required tools installed works the same as a desktop or
      laptop for running the commands.
  - question: What result should I expect after I complete the workflow?
    answer: >-
      Terraform automates the creation of an Arm virtual machine instance on OCI Ampere Compute.
      You finish with an OCI Arm instance provisioned from your Terraform configuration.
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

---
title: Deploy OpenStack on Azure Cobalt 100 Arm64 Virtual Machine
description: Deploy OpenStack on Azure Cobalt 100 Arm64 virtual machines using DevStack for development and Kolla-Ansible for containerized production deployments.

    
minutes_to_complete: 90

who_is_this_for: This learning path is designed for developers, DevOps engineers, and platform engineers who want to deploy and manage OpenStack on Arm-based cloud environments using Kolla-Ansible and DevStack.

learning_objectives:
   - Deploy OpenStack on Azure Cobalt 100 Arm64 virtual machines
   - Configure core OpenStack services (Keystone, Nova, Neutron, Glance, Cinder)
   - Deploy containerized OpenStack using Kolla-Ansible
   - Set up networking and storage for OpenStack
   - Launch and manage virtual machine instances
   - Access OpenStack using CLI and Horizon dashboard

prerequisites:
  - A [Microsoft Azure account](https://azure.microsoft.com/) with access to Cobalt 100 based instances (Dpsv6)
  - Basic knowledge of Linux command-line operations
  - Familiarity with SSH and remote server access
  - Basic understanding of cloud computing and virtualization concepts

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:44:49Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 42628afa923ce6e89693bdfc72469ac0803610c3decb6cd4f36bd1a003874d0d
  summary_generated_at: '2026-06-02T04:43:52Z'
  summary_source_hash: 42628afa923ce6e89693bdfc72469ac0803610c3decb6cd4f36bd1a003874d0d
  faq_generated_at: '2026-06-03T01:44:49Z'
  faq_source_hash: 42628afa923ce6e89693bdfc72469ac0803610c3decb6cd4f36bd1a003874d0d
  summary: >-
    Learn how to deploy OpenStack on Arm-based Microsoft Azure Cobalt 100 (Arm64) virtual machines.
    You will provision an Azure Dpsv6 series VM and use DevStack to bring up a single-node development
    environment with core services. Then you will prepare a second Ubuntu 24.04 Arm64 VM with
    two NICs and a data disk, and use Kolla-Ansible to deploy containerized OpenStack services.
    Along the way, you will configure networking and storage, launch and manage instances, and
    access OpenStack via the CLI and Horizon dashboard. Prerequisites include an Azure account
    with access to Cobalt 100 instances, basic Linux command-line skills, familiarity with SSH,
    and a basic understanding of cloud and virtualization concepts.
  faqs:
  - question: What do I need before I start?
    answer: >-
      You need a Microsoft Azure account with access to Cobalt 100 based instances (Dpsv6), basic
      Linux command-line skills, familiarity with SSH and remote access, and a basic understanding
      of cloud computing and virtualization concepts.
  - question: Which Azure VM size and disk setup should I use for the DevStack deployment?
    answer: >-
      Use a single-NIC D4ps_v6 instance with at least 80 GB of disk. The steps in this Learning
      Path use the Azure Portal to create the VM.
  - question: Can I run DevStack and Kolla-Ansible on the same VM?
    answer: >-
      No. You can't run DevStack and Kolla-Ansible on the same VM; the Kolla-Ansible deployment
      must run on a separate Azure VM.
  - question: What specifications and OS are required for the Kolla-Ansible host?
    answer: >-
      Create a separate Azure VM with 4 vCPUs (8 recommended), 16 GB RAM (recommended), a 100
      GB OS disk, a 32 GB data disk (for Cinder/Docker), and two NICs. Use Ubuntu 24.04 on Arm64.
  - question: After deployment, how do I access OpenStack and what should I expect to be running?
    answer: >-
      Access OpenStack using the CLI and the Horizon dashboard. The environment runs core services
      such as Nova, Neutron, Keystone, and Glance on Arm64 and allows launching virtual machine
      instances.
# END generated_summary_faq

author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
cloud_service_providers:
  - Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - OpenStack
    - Kolla-Ansible
    - DevStack
    - Python 
    - OpenStack CLI

operatingsystems:
    - Linux

further_reading:
  - resource:
        title: OpenStack Official Website
        link: https://www.openstack.org/
        type: website
  - resource:
      title: OpenStack Documentation
      link: https://docs.openstack.org/
      type: documentation
  - resource:
      title: Kolla-Ansible Documentation
      link: https://docs.openstack.org/kolla-ansible/latest/
      type: documentation
  - resource:
      title: Azure Cobalt 100 processors
      link: https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---


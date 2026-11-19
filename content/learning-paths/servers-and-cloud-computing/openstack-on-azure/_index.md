---
title: Deploy OpenStack on Arm64 virtual machines on Azure Cobalt 100
description: Deploy OpenStack on Azure Cobalt 100 Arm64 virtual machines using DevStack for development and Kolla-Ansible for containerized production deployments.

minutes_to_complete: 90

who_is_this_for: This learning path is designed for developers, DevOps engineers, and platform engineers who want to deploy and manage OpenStack on Arm-based cloud environments using Kolla-Ansible and DevStack.

learning_objectives:
   - Deploy OpenStack on Azure Cobalt 100 Arm64 virtual machines (VMs).
   - Configure core OpenStack services (Keystone, Nova, Neutron, Glance, Cinder).
   - Deploy containerized OpenStack using Kolla-Ansible.
   - Set up networking and storage for OpenStack.
   - Launch and manage virtual machine instances.
   - Access OpenStack using CLI and Horizon dashboard.

prerequisites:
  - A [Microsoft Azure account](https://azure.microsoft.com/) with access to Cobalt 100 based instances (Dpsv6)
  - Basic knowledge of Linux command-line operations
  - Familiarity with SSH and remote server access
  - Basic understanding of cloud computing and virtualization concepts

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-18T20:21:13Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a0b28b8f7cc05d1d6b545a90222421d518c28d14c8ea86cac119e3c14ecaef96
  summary_generated_at: '2026-11-18T20:21:13Z'
  summary_source_hash: a0b28b8f7cc05d1d6b545a90222421d518c28d14c8ea86cac119e3c14ecaef96
  faq_generated_at: '2026-11-18T20:21:13Z'
  faq_source_hash: a0b28b8f7cc05d1d6b545a90222421d518c28d14c8ea86cac119e3c14ecaef96
  summary: >-
    You'll deploy OpenStack on Arm-based Azure Cobalt 100 virtual machines using two approaches.
    First, you'll create a VM and use DevStack to set up a development environment. Then, you'll
    prepare a separate VM with two network interfaces and a data disk for Kolla-Ansible.
    Finally, you'll deploy containerized services, verify them, and launch a VM through OpenStack.
  faqs:
  - question: Which Azure VM size should I use for DevStack, and do I need extra NICs or disks on my VM?
    answer: >-
      Use a single-NIC `D4ps_v6` instance with at least 80 GB of disk. You don't need an extra
      NIC or a separate data disk for DevStack.
  - question: Can I run DevStack and Kolla-Ansible on the same VM?
    answer: >-
      Use separate Azure VMs for DevStack and Kolla-Ansible. 
  - question: How do I decide between DevStack and Kolla-Ansible for what I need?
    answer: >-
      Use DevStack for a script-based, single-node environment aimed at development and testing.
      Choose Kolla-Ansible to deploy OpenStack services as containers for a modular,
      reproducible, production-like setup.
  - question: What VM specs should I provision for the Kolla-Ansible host on Azure, and how should I assign the NICs?
    answer: >-
      Provision at least 4 vCPUs (8 recommended), 16 GB RAM, a 100 GB OS disk, and a 32 GB
      data disk for Cinder/Docker on Ubuntu 24.04. Use two NICs: `eth0` for management and
      `eth1` for external networking.
  - question: How do I verify that my OpenStack deployment worked before I move on?
    answer: >-
      For DevStack, expect a single node running Keystone, Nova, Glance, and Horizon. Verify
      access using the CLI and Horizon. For Kolla-Ansible, confirm that core services such as Nova,
      Neutron, Keystone, and Glance are running in containers. Ensure that you can access the CLI
      and Horizon to launch instances.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
platforms:
  - Microsoft Azure Cobalt

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


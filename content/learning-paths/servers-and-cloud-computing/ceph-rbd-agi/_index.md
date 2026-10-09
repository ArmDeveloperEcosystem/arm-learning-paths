---
title: Deploy Ceph RBD block storage on an Arm AGI CPU host

description: Build a Ceph cluster in Ubuntu 26.04 Arm64 virtual machines, use an RBD block volume, and extend the cluster from one node to three nodes on an Arm AGI CPU host.

minutes_to_complete: 90

who_is_this_for: This Learning Path is for infrastructure developers who want a hands-on introduction to Ceph block storage on an Arm server.

learning_objectives:
    - Create three networked Ubuntu 26.04 Arm64 virtual machines on one Arm AGI CPU host.
    - Bootstrap a single-node Ceph cluster and use an RBD block volume.
    - Extend the cluster to three Ceph nodes with one OSD per node.
    - Verify replicated storage during a controlled OSD failure and recovery.

prerequisites:
    - An Arm AGI CPU host running Ubuntu 24.04 Arm64 with KVM hardware virtualization support
    - Root or `sudo` access on the AGI CPU host
    - Familiarity with Linux block devices, and virtual machines
    - Outbound internet access from the AGI CPU host and virtual machines

author: Pareena Verma

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
armips:
    - Neoverse
platforms:
  - Arm AGI CPU
tools_software_languages:
    - Ceph
    - Bash
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Arm AGI CPU
        link: https://www.arm.com/products/cloud-datacenter/arm-agi-cpu
        type: website
    - resource:
        title: Cephadm installation
        link: https://docs.ceph.com/en/squid/cephadm/install/
        type: documentation
    - resource:
        title: Ceph block device commands
        link: https://docs.ceph.com/en/squid/rbd/rados-rbd-cmds/
        type: documentation
    - resource:
        title: Cephadm host management
        link: https://docs.ceph.com/en/squid/cephadm/host-management/
        type: documentation
    - resource:
        title: Install libvirt on Ubuntu
        link: https://ubuntu.com/server/docs/how-to/virtualisation/libvirt/
        type: documentation
    - resource:
        title: Launch Ubuntu cloud images with libvirt
        link: https://ubuntu.com/docs/public-images/public-images-how-to/launch-with-libvirt/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

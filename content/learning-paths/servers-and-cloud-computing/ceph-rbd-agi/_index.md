---
title: Deploy Ceph RADOS Block Device storage on an Arm AGI CPU host

description: Build a Ceph cluster in Ubuntu 26.04 Arm64 virtual machines, use an RBD block volume, and extend the cluster from one node to three nodes on an Arm AGI CPU host.

minutes_to_complete: 90

who_is_this_for: This Learning Path is for infrastructure developers who want a hands-on introduction to Ceph block storage on an Arm server.

learning_objectives:
    - Create three networked Ubuntu 26.04 Arm64 virtual machines (VMs) on one Arm AGI CPU host.
    - Bootstrap a single-node Ceph cluster and use an RADOS Block Device (RBD) block volume.
    - Extend the cluster to three Ceph nodes with one object storage daemon (OSD) per node.
    - Verify replicated storage during a controlled OSD failure and recovery.

prerequisites:
    - An Arm AGI CPU host running Ubuntu 24.04 with kernel-based VM (KVM) hardware virtualization support
    - At least 12 available CPU cores, 12 GB of available memory, and 90 GB of available storage on the AGI CPU host
    - Root or `sudo` access on the AGI CPU host
    - Familiarity with Linux block devices and VMs
    - Outbound internet access from the AGI CPU host and the VMs


# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-16T16:23:37Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: c7c7c1e8983617e4b303c2531a22ae18915d1ba16c21e5189c2f62f58a068e8e
  summary_generated_at: '2026-10-16T16:23:37Z'
  summary_source_hash: c7c7c1e8983617e4b303c2531a22ae18915d1ba16c21e5189c2f62f58a068e8e
  faq_generated_at: '2026-10-16T16:23:37Z'
  faq_source_hash: c7c7c1e8983617e4b303c2531a22ae18915d1ba16c21e5189c2f62f58a068e8e
  summary: >-
    You'll build and test replicated Ceph RBD storage on an Arm AGI CPU host. First, you'll create three Ubuntu
    26.04 Arm64 VMs, prepare them, and bootstrap a single-node cluster. You'll map an RBD
    image, mount it, and verify file persistence on the single node. After authorizing cluster SSH access to the other
    nodes, you'll add their OSDs and increase replication. Finally, you'll stop and restart an OSD to
    check continued access and recovery.
#   faqs:
#   - question: Which `cephadm` release should I install on Ubuntu 26.04 and why?
#     answer: >-
#       Use `cephadm` 19.2.6 to match the Ceph Squid 19.2.6 cluster release. Ubuntu 26.04 repositories
#       provide Ceph 20.2.0, so download `cephadm` 19.2.6 directly to keep the deployment tools and
#       cluster on the same version.
#   - question: 'Where do I run commands during each phase: host setup, VM prep, and cluster operations?'
#     answer: >-
#       Run VM creation commands on the Arm AGI CPU host. Run preparation commands inside each VM.
#       During expansion, authorize the cluster's SSH key on the new nodes from the AGI host. Run
#       cluster bootstrap, RBD usage, and the remaining expansion commands inside `ceph1`.
#   - question: How do I know each VM is ready before bootstrapping Ceph?
#     answer: >-
#       Confirm each VM has 4 vCPUs, 4 GB memory, a 20 GB OS disk, a separate unused data disk of
#       at least 10 GB, stable IP addressing, SSH access, hostname resolution, and synchronized
#       clocks. Identify the empty data disk that Ceph will use on each node.
#   - question: What device should appear after mapping the RBD image, and how do I verify persistence?
#     answer: >-
#       You should see a block device such as `/dev/rbd0`. Format and mount it, write a test file, then
#       unmap and remap the image and compare checksums to verify the file persists in Ceph.
#   - question: What changes when expanding to three nodes, and how is replication tested?
#     answer: >-
#       You add two more Ceph nodes so the cluster runs one OSD per node. A controlled OSD failure
#       tests whether you can keep reading and writing the RBD volume. After the OSD returns, you
#       verify that Ceph repairs changed objects and both the original and outage files retain their
#       checksums.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
armips:
    - Neoverse
platforms:
  - Arm AGI CPU
tools_software_languages:
    - Ceph
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

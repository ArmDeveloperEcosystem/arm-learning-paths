---
title: Nested Virtualization on an Arm64 Server
description: Configure an Arm server to allow guest virtual machines to act as hypervisors, enabling users to run virtual machines inside a virtual machine.

minutes_to_complete: 20

who_is_this_for: This is an advanced topic for System Administrators who are interested in enabling users to run VMs inside virtual machines.

learning_objectives: 
    - Starting a Virtual Machine on Linux using virsh
    - Configuring a host and guest VM to allow the guest VM to function as a hypervisor
    - Using a standard benchmark suite, measure the performance impact of running software inside a nested virtual machine against a regular guest VM and on bare metal

prerequisites:
    - An Arm64 server supporting FEAT_NV2 (available in Arm v8.4-A and later)
    - Fedora 44 (or any distribution with a version 7.2 or later Linux kernel)

author: David Neary <nearyd@amperecomputing.com>

# New Learning Paths are opted in for the next manual generated summary/FAQ run.
# The generator resets this to false after a successful write.
generate_summary_faq: true

# Optional one-shot controls: set either field to true to regenerate just that
# generated section the next time the summary/FAQ tool runs. The tool resets
# them to false after a successful write.
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Virtualization
armips:
    - Arm v8.6-A or later
    - Arm v9.0-A or later
    - Neoverse N2+, V2+
tools_software_languages:
    - KVM
    - libvirt
    - virsh / virt-manager
operatingsystems:
    - Fedora 44+
    - Linux 7.2 kernel or later

further_reading:
    - resource:
        title: PLACEHOLDER MANUAL 
        link: PLACEHOLDER MANUAL LINK
        type: documentation
    - resource:
        title: PLACEHOLDER BLOG 
        link: PLACEHOLDER BLOG LINK
        type: blog
    - resource:
        title: PLACEHOLDER GENERAL WEBSITE 
        link: PLACEHOLDER GENERAL WEBSITE LINK
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

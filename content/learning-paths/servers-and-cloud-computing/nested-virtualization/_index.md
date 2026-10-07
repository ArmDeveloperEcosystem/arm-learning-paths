---
title: Configure and run nested virtualization on an Arm server

draft: true
cascade:
    draft: true
      
description: Set up nested virtualization on an Arm server so guest virtual machines can act as hypervisors and run other virtual machines inside them.

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for system administrators who want to enable nested virtualization, so users can run virtual machines inside other virtual machines.

learning_objectives: 
    - Enable nested virtualization on an Arm server and verify the host supports it
    - Create and start Arm64 guest virtual machines using virt-install, cloud-init, and virsh
    - Configure a guest VM to act as a hypervisor and run a nested VM inside it
    - Measure the performance overhead of a nested VM against a standard guest VM and bare metal using sysbench

prerequisites:
    - An Arm64 bare metal server with 64 cores or more, supporting FEAT_NV2 (available in Arm v8.4-A and later), with Fedora 44 installed

author: Dave Neary 

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
subjects: Containers and Virtualization
armips:
    - Neoverse
tools_software_languages:
    - KVM
    - libvirt
    - virsh
    - virt-install
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Nested virtualization in the Arm AArch64 virtualization guide
        link: https://support.arm.com/documentation/102142/0100/Nested-virtualization?lang=en
        type: documentation
    - resource:
        title: 'Unlocking Layers: Powering Nested Virtualization with Ampere CPUs'
        link: https://amperecomputing.com/blogs/unlocking-layers
        type: blog
    - resource:
        title: 'Fedora Discussion: nested virtualization on Arm64'
        link: https://discussion.fedoraproject.org/t/nested-virtualization/179358
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

---
title: Configure and run nested virtualization on an Arm server
      
description: Set up nested virtualization on an Arm server so guest virtual machines can act as hypervisors and run other virtual machines inside them.

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for system administrators who want to enable users to run virtual machines (VMs) inside VMs.

learning_objectives: 
    - Start a VM on Linux using virsh.
    - Configure a host and guest VM to allow the guest VM to function as a hypervisor.
    - Use a standard benchmark suite to measure the performance impact of running software inside a nested VM against a regular guest VM and on bare metal.

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

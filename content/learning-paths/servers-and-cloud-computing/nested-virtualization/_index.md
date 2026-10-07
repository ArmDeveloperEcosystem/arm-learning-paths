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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-07T22:16:51Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 662c23953f5143207ed9869e697fa68f89865d9c1f20dce28dc0c6d3521515c7
  summary_generated_at: '2026-10-07T22:16:51Z'
  summary_source_hash: 662c23953f5143207ed9869e697fa68f89865d9c1f20dce28dc0c6d3521515c7
  faq_generated_at: '2026-10-07T22:16:51Z'
  faq_source_hash: 662c23953f5143207ed9869e697fa68f89865d9c1f20dce28dc0c6d3521515c7
  summary: >-
    You'll enable nested virtualization on a bare-metal Arm64 server and build a hypervisor
    that runs a guest VM. First, you'll install virtualization tools and verify NV2 support on
    the host. You'll then create a baseline guest VM, configure a second VM
    as a hypervisor, and boot a guest VM inside the hypervisor. Finally, you'll pin CPU cores and compare
    `sysbench` throughput across the bare metal host and the guest VMs.
  faqs:
  - question: Why do I need a bare-metal Arm64 server?
    answer: >-
      You need direct access to the processor's EL2 virtualization support and hardware that
      supports FEAT_NV2. A standard VM doesn't provide the access needed to enable nested
      virtualization with these steps.
  - question: How do I confirm nested virtualization is enabled on the host?
    answer: >-
      Check the host's kernel messages for `VHE+NV2 mode initialized successfully`. If you see
      `VHE mode initialized successfully` without `+NV2`, nested virtualization isn't enabled.
      Check whether the kernel argument was applied and whether the hardware supports FEAT_NV2.
  - question: How do I verify that the L1 hypervisor VM can run a nested guest?
    answer: >-
      Inside the L1 hypervisor VM, check the kernel messages for `CPU: All CPU(s) started at EL2`
      and confirm that `/dev/kvm` exists. These checks show that virtualization support is
      available to the VM.
  - question: How do I connect to the L2 guest after it starts?
    answer: >-
      In the L1 hypervisor VM, use `virsh net-dhcp-leases default` to find the L2 guest's IP
      address. Connect with `ssh -i ~/guest_key fedora@<L2-guest-IP-address>` using the private
      key that you copied into the hypervisor VM.
  - question: Which result should I compare across bare metal, L1, and L2?
    answer: >-
      Compare `events per second` from your `sysbench` output to assess throughput. After pinning
      each system to the specified cores, calculate each guest's overhead against your bare-metal
      result rather than treating the example numbers as expected results.
# END generated_summary_faq

author: Dave Neary 

# New Learning Paths are opted in for the next manual generated summary/FAQ run.
# The generator resets this to false after a successful write.
generate_summary_faq: false

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

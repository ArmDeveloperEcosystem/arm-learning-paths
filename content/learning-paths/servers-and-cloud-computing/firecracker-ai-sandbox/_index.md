---
title: Build an ephemeral AI code sandbox with Firecracker on Arm

description: Build a Firecracker microVM sandbox on an Arm Linux server based on processors such as Arm AGI CPU or AWS Graviton, that runs generated shell code with bounded resources and restricted networking.

minutes_to_complete: 45

who_is_this_for: This Learning Path is for developers who want to isolate AI-generated code in disposable microVMs on an Arm Linux server.

learning_objectives:
    - Prepare an Arm Linux kernel-based virtual machine (KVM) host and an aarch64 Firecracker guest image.
    - Run generated shell code in a dedicated disposable microVM.
    - Apply CPU, memory, timeout, filesystem, and network boundaries to each execution.
    - Verify native Arm execution and confirm that guest filesystem changes don't persist.

prerequisites:
    - An Arm AGI CPU platform or another Arm-based bare-metal server, such as an AWS Graviton4-based bare-metal instance, running Ubuntu 24.04 with KVM available as `/dev/kvm`
    - Root or `sudo` access on the server
    - Familiarity with Bash, SSH, and Linux networking
    - Outbound internet access to download Firecracker and guest artifacts

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-29T18:28:24Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 5e953cbca66f4549afe82812530fc745f15ebe4fcb355d74ffa098fd115df1f8
  summary_generated_at: '2026-09-29T18:28:24Z'
  summary_source_hash: 5e953cbca66f4549afe82812530fc745f15ebe4fcb355d74ffa098fd115df1f8
  faq_generated_at: '2026-09-29T18:28:24Z'
  faq_source_hash: 5e953cbca66f4549afe82812530fc745f15ebe4fcb355d74ffa098fd115df1f8
  summary: >-
    You'll build an ephemeral Firecracker microVM sandbox for generated shell code on an Arm Linux
    KVM host. First, you'll examine the per-job isolation model, then install Firecracker and prepare
    a reusable aarch64 guest image. Next, you'll run a sample program with bounded CPU, memory,
    execution time, disposable filesystem state, and restricted networking. Finally, you'll verify
    filesystem disposability, timeout behavior, and cleanup of per-job network and runtime resources.
  faqs:
  - question: How do I confirm that KVM is available before I start?
    answer: >-
      Check that `/dev/kvm` exists on your Arm host. If you use a VM, ensure that it exposes nested
      virtualization and passes `/dev/kvm` through. Otherwise, use an Arm-based bare-metal server.
  - question: What does the sandbox runner download, and where does it go?
    answer: >-
      The runner downloads `00-common.sh`, `run-job.sh`, and `demo.sh` into `sandbox/`, and the example
      programs `hello-arm.sh`, `write-marker.sh`, and `timeout.sh` into `sandbox/examples/`.
  - question: What result should I expect when I run an example job?
    answer: >-
      You should see the runner start a Firecracker microVM and execute the selected script inside
      the guest. For the default example, confirm `architecture=aarch64`, `cpus=1`,
      `outcome=succeeded`, and `exit_code=0`. The kernel version and job identifier can vary.
  - question: How do I know that guest filesystem changes don’t persist between jobs?
    answer: >-
      Run `write-marker.sh` twice. Each job checks for `/tmp/ai-sandbox-marker` before creating it.
      Confirm that the second job doesn't find the marker from the first job, because each job
      starts with a fresh copy of the base image.
  - question: How do I confirm network and runtime cleanup after a job finishes?
    answer: >-
      After the job exits, confirm that the `fc-ai0` TAP device is absent and that
      `/opt/firecracker-ai/runtime` contains no job directories. The reusable `runner.lock` file
      remains in the runtime directory.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
armips:
    - Neoverse
platforms:
  - Arm AGI CPU
  - AWS Graviton
tools_software_languages:
    - Firecracker
    - KVM
    - Bash
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Arm AGI CPU
        link: https://www.arm.com/products/cloud-datacenter/arm-agi-cpu
        type: website
    - resource:
        title: Firecracker getting started guide
        link: https://github.com/firecracker-microvm/firecracker/blob/main/docs/getting-started.md
        type: documentation
    - resource:
        title: Firecracker production host setup recommendations
        link: https://github.com/firecracker-microvm/firecracker/blob/main/docs/prod-host-setup.md
        type: documentation
    - resource:
        title: Firecracker design
        link: https://github.com/firecracker-microvm/firecracker/blob/main/docs/design.md
        type: documentation
    - resource:
        title: Linux Kernel-based Virtual Machine
        link: https://linux-kvm.org/page/Main_Page
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

---
title: Deploy firmware on hybrid edge systems using containers

description: Learn how to deploy containerized embedded applications and firmware onto an Arm Cortex-M core from a Cortex-A core using containerd, K3s, and the hybrid-runtime on Arm Virtual Hardware.

minutes_to_complete: 20

who_is_this_for: This learning path is for developers interested in learning how to deploy software (embedded applications and firmware) onto other processors in the system, using Linux running on the application core.

learning_objectives:
    - Deploy a containerized embedded application onto an Arm Cortex-M core from an Arm Cortex-A core using containerd and K3s.
    - Build a firmware container image.
    - Build the hybrid-runtime components.

prerequisites:
    - A valid account with [Arm Virtual Hardware](https://app.avh.arm.com/login)
    - An Arm Linux host machine (if you want to build your own runtime and container image)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-08T15:26:26Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3394bf994039e441d57dced2abb64d725077d4672e0e68dc71f1de50e58f0408
  summary_generated_at: '2026-07-08T15:26:26Z'
  summary_source_hash: 3394bf994039e441d57dced2abb64d725077d4672e0e68dc71f1de50e58f0408
  faq_generated_at: '2026-07-08T15:26:26Z'
  faq_source_hash: 3394bf994039e441d57dced2abb64d725077d4672e0e68dc71f1de50e58f0408
  summary: >-
    You'll use a hybrid container runtime to deploy containerized
    firmware and embedded applications onto a Cortex-M target from a Linux-based Cortex-A host
    on Arm Virtual Hardware. First, you'll set up the i.MX 8M Plus model, then run a sample workload
    with `containerd` using the `io.containerd.hybrid` runtime and confirm container state with `containerd`
    tooling. You'll also learn about the `hybrid-runtime` OCI-compatible interface and install a single-node K3s configured to use `containerd`. By the end, you'll have executed
    a Hello World firmware container and prepared K3s to deploy the SMARTER demo on an Arm-based
    hybrid edge system.
  faqs:
  - question: Which Arm Virtual Hardware device should I create to follow the steps?
    answer: >-
      Create a device in the **Default Project** and select the **i.MX 8M Plus** model as shown in the
      setup step.
  - question: How do I confirm the Hello World container ran with the hybrid runtime?
    answer: >-
      After running the example with containerd, list containers with `ctr c ls` and check that
      the RUNTIME column shows `io.containerd.hybrid` and the test container is present.
  - question: What container image is used for the example workload?
    answer: >-
      The example uses `ghcr.io/smarter-project/hybrid-runtime/hello_world_imx8mp:latest`. The steps
      pull the image before running it with containerd.
  - question: Which container runtime does K3s use in this setup?
    answer: >-
      K3s is configured to use containerd via the container-runtime-endpoint flag set to `unix://var/run/containerd/containerd.sock`
      in the provided install command.
  - question: How long should the K3s installation take, and what should I do next?
    answer: >-
      The installation can take a few minutes. When the script completes without errors, continue
      with deploying the SMARTER demo as described.
# END generated_summary_faq

author: Basma El Gaabouri

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
armips:
    - Cortex-M
    - Cortex-A
tools_software_languages:
    - Docker
    - Arm Virtual Hardware
    - K3s
    - Containerd
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: K3s Quick start Guide 
        link: https://docs.k3s.io/quick-start
        type: documentation
    - resource:
        title: Smarter Project GitHub page
        link: https://github.com/smarter-project/
        type: website
    - resource:
        title: Hybrid-runtime GitHub page 
        link: https://github.com/smarter-project/hybrid-runtime/tree/main
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

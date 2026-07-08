---
title: Deploy a machine learning application to the Arm Ethos-U65 NPU on NXP FRDM i.MX 93 with Topo

description: Use Topo to build and deploy a Cortex-A web application that sends MobileNetV2 image classification requests to Cortex-M33 firmware accelerated by the Ethos-U65 NPU.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for embedded/edge software developers who want to deploy machine learning workloads to heterogeneous Arm-based Linux targets using Topo, including leveraging Arm Ethos-U NPUs.

learning_objectives:
    - Explain how Topo deploys an application that spans Cortex-A, Cortex-M, and Ethos-U
    - Deploy the topo-imx93-npu-deployment Template, which operates across Cortex-A, Cortex-M, and Ethos-U, to perform image classification using an ExecuTorch MobileNetV2 model
    - Describe how the Template is bootstrapped from Compose services, Remoteproc Runtime metadata, and Topo arguments and follow this process yourself
    - Understand how to take similar projects and create Topo Templates, including using Agent Skills

prerequisites:
    - A host machine (x86 or Arm) with Linux, macOS, or Windows
    - An NXP FRDM i.MX 93 target board with Linux setup, accessible over SSH with root access. To do this, see [Use Linux on the NXP FRDM i.MX 93 board](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/linux-nxp-board/).
    - Docker installed on the host and target. For installation steps, see [Install Docker](https://learn.arm.com/install-guides/docker/).
    - At least 25 GB of free disk space on the host if you're building without cache images.
    - The Device Tree Compiler (`dtc`) installed on the host.
    - lscpu installed on the target (pre-installed on most Linux distributions)
    - Topo installed on the host. For installation steps, see [Deploy containerized workloads to Arm-based Linux targets with Topo](https://learn.arm.com/learning-paths/cross-platform/deploy-containerized-workloads-with-topo/).
    - Basic familiarity with containers, SSH, and CLI tools
    - (Optional) Access to an agent, such as Codex or Claude Code

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-08T15:30:00Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 6469ed1daadf6dd4fe5436b42234282d32e14c97f772447009eabda8350f130b
  summary_generated_at: '2026-07-08T15:30:00Z'
  summary_source_hash: 6469ed1daadf6dd4fe5436b42234282d32e14c97f772447009eabda8350f130b
  faq_generated_at: '2026-07-08T15:30:00Z'
  faq_source_hash: 6469ed1daadf6dd4fe5436b42234282d32e14c97f772447009eabda8350f130b
  summary: >-
    You'll build and deploy a heterogeneous image classification
    application to an NXP FRDM i.MX 93 board using Topo. First, you'll assemble a Topo Template from two
    base projects: a Cortex-A web application and a Cortex-M33 ExecuTorch runner, then convert
    the combined sources into a Compose project with Topo metadata and Remoteproc Runtime services.
    The application preprocesses images on Cortex-A, shares model and tensor data through shared
    memory, and issues RPMsg commands to Cortex-M33 firmware that delegates inference to the Arm
    Ethos-U65 NPU via the ExecuTorch backend. After validating target readiness with `topo health`
    and deploying, containers run on the board, and you'll be able to access a browser-based MobileNetV2 classifier.
  faqs:
  - question: How do I confirm the FRDM i.MX 93 target is ready before deploying?
    answer: >-
      Run topo health --target <user>@<target-ip>. The host and target sections should show successful
      checks for SSH and the container engine, and the target should also report Remoteproc Runtime
      and Remoteproc as healthy.
  - question: Which components run on Cortex-A and Cortex-M33, and how do they communicate?
    answer: >-
      The Cortex-A side runs the web application that prepares images, writes model and tensor
      data into shared memory, and sends inference commands. The Cortex-M33 runs the ExecuTorch
      firmware and receives commands over RPMsg.
  - question: What should I expect after deploying the Topo Template?
    answer: >-
      Topo builds images on the host, transfers them to the target, and starts services on the
      board. Remoteproc Runtime starts the Cortex-M firmware, and the browser-based MobileNetV2
      classifier becomes available.
  - question: What are the key steps to turn the two base projects into a Topo Template?
    answer: >-
      Combine the Cortex-A web app and the Cortex-M33 ExecuTorch firmware sources into a single
      repository, make it a normal Compose project, then add Topo metadata and Remoteproc Runtime
      services. The Template is bootstrapped from Compose services, Remoteproc Runtime metadata,
      and Topo arguments.
  - question: What should I check if topo health reports a failure?
    answer: >-
      Resolve the specific errors shown by topo health before continuing. Confirm SSH access to
      the target, verify the container engine is available on both host and target, and ensure
      Remoteproc Runtime is present on the target.
# END generated_summary_faq

author: Tomas Agustin Gonzalez Orlando

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
armips:
    - Cortex-A
    - Cortex-M
    - Ethos-U
tools_software_languages:
    - Topo
    - Docker
    - SSH
    - ExecuTorch
    - remoteproc-runtime
operatingsystems:
    - Linux
    - macOS
    - Windows

further_reading:
    - resource:
        title: Topo repository
        link: https://github.com/arm/topo
        type: documentation
    - resource:
        title: Topo template format
        link: https://github.com/arm/topo-template-format
        type: documentation
    - resource:
        title: Topo releases
        link: https://github.com/arm/topo/releases/latest
        type: website
    - resource:
        title: remoteproc-runtime
        link: https://github.com/arm/remoteproc-runtime
        type: documentation
    - resource:
        title: ExecuTorch
        link: https://docs.pytorch.org/executorch/stable/index.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

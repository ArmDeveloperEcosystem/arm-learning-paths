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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:09:54Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3394bf994039e441d57dced2abb64d725077d4672e0e68dc71f1de50e58f0408
  summary_generated_at: '2026-06-01T21:29:58Z'
  summary_source_hash: 3394bf994039e441d57dced2abb64d725077d4672e0e68dc71f1de50e58f0408
  faq_generated_at: '2026-06-02T22:09:54Z'
  faq_source_hash: 3394bf994039e441d57dced2abb64d725077d4672e0e68dc71f1de50e58f0408
  summary: >-
    This introductory path shows how to deploy containerized embedded applications and firmware
    to a Cortex-M core from a Linux-based Cortex-A application core using the OCI-compatible hybrid-runtime
    with containerd and K3s on Arm Virtual Hardware. You provision an i.MX 8M Plus model in AVH,
    review the hybrid-runtime components, run a Hello World firmware container via containerd’s
    io.containerd.hybrid runtime, and verify creation with ctr commands. You also set up a single-node
    K3s cluster configured to use containerd with selected components disabled for embedded use.
    Objectives include building the hybrid-runtime components and a firmware container image.
    Prerequisites are an AVH account and, if you will build locally, an Arm Linux host machine.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      You need a valid Arm Virtual Hardware account. If you plan to build your own runtime and
      container image, you also need access to an Arm Linux host machine.
  - question: Which Arm Virtual Hardware device should I create?
    answer: >-
      Create a device in the Default Project and select the i.MX 8M Plus platform. This model
      runs four Cortex-A53 processors and is used for the hybrid edge setup.
  - question: Which runtime should I specify when starting a container with containerd?
    answer: >-
      Use the hybrid runtime by passing --runtime io.containerd.hybrid to ctr run. The example
      image is ghcr.io/smarter-project/hybrid-runtime/hello_world_imx8mp:latest with a container
      name such as test.
  - question: How do I verify that the container started correctly with containerd?
    answer: >-
      Run ctr c ls to list containers. You should see your container (for example, test) with
      the hello_world_imx8mp:latest image and the io.containerd.hybrid runtime.
  - question: How should I install and configure K3s for this demo?
    answer: >-
      Set INSTALL_K3S_EXEC for a single-node server and include the provided flags to disable
      traefik, metrics-server, coredns, and local-storage, set flannel-backend=none, cluster-dns
      to 169.254.0.2, and point to containerd via --container-runtime-endpoint. Then run: curl
      -sfL https://get.k3s.io | INSTALL_K3S_EXEC=$INSTALL_K3S_EXEC sh -s -
# END generated_summary_faq

author: Basma El Gaabouri

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


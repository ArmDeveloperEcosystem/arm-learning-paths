---
title: Deploy containerized workloads to Arm-based Linux targets with Topo

description: Use Topo to detect Arm processor capabilities on a target device, select a compatible Topo Project, and deploy containerized workloads to Arm-based Linux targets over SSH using the CLI or VS Code extension.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for embedded, edge, and cloud software developers who want to deploy containerized workloads to Arm-based Linux targets using Topo.

learning_objectives:
    - Install Topo and verify that the host and target environments are ready for deployment
    - Run health checks and list compatible projects for your target
    - Clone a Topo Project and deploy a containerized workload to an Arm-based Linux target
    - (Optional) Use the Topo VS Code extension to run the same target, project, and deployment workflow from Visual Studio Code
    - (Optional) Deploy firmware and applications to heterogeneous Cortex-A + Cortex-M devices using remoteproc-runtime

prerequisites:
    - A host machine (x86 or Arm) with Linux, macOS, or Windows
    - An Arm-based Linux target accessible over SSH, for example an Arm-based Linux VM, Raspberry Pi, DGX Spark, or NXP i.MX 93
    - Docker installed on the host and target. For installation steps, see [Install Docker](/install-guides/docker/).
    - lscpu installed on the target (pre-installed on most Linux distributions)
    - (Optional) Visual Studio Code installed if you want to use the Topo VS Code extension.
    - Basic familiarity with containers and CLI tools

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-02T19:14:35Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 49368c669c0d44931ed68ba65bcd88321025a685cfd23ed73d43de7b35cacd07
  summary_generated_at: '2026-07-02T19:14:35Z'
  summary_source_hash: 49368c669c0d44931ed68ba65bcd88321025a685cfd23ed73d43de7b35cacd07
  faq_generated_at: '2026-07-02T19:14:35Z'
  faq_source_hash: 49368c669c0d44931ed68ba65bcd88321025a685cfd23ed73d43de7b35cacd07
  summary: >-
    You'll use Topo to deploy containerized workloads to Arm-based Linux targets
    over SSH. You'll install Topo on a host machine, run a health check to validate host and target
    readiness, and list projects compatible with the target's Arm CPU features and hardware capabilities.
    You'll then clone a starter project using an LLM chat example and deploy. Topo builds the container image
    on the host, transfers it to the target, and starts the services on the target; it can also
    build directly on the target. You'll also see how to run the same workflow using
    the Topo Visual Studio Code extension.
  faqs:
  - question: How do I verify that my host and target are ready before deploying?
    answer: >-
      Run `topo health` on the host to confirm Topo, SSH, and the container engine are available.
      To include the target in the check, provide `--target` or set the `TOPO_TARGET` environment
      variable.
  - question: How do I tell Topo which target to use for health checks and deployment?
    answer: >-
      Pass `--target` to the Topo command or set `TOPO_TARGET` in your environment. The health check
      output prompts you when a target is not specified.
  - question: How does Topo determine if a project is compatible with my Arm target?
    answer: >-
      Topo detects hardware capabilities on the target, including Arm CPU features such as Neon and
      SVE, and uses them to identify compatible projects when you run `topo projects --target`.
  - question: What should I expect when cloning the example project and responding to prompts?
    answer: >-
      Clone the LLM chat project with `topo clone`. The default configuration uses the
      `unsloth/SmolLM2-135M-Instruct-GGUF` model and can be deployed immediately.
  - question: Where are images built and what happens after deployment starts?
    answer: >-
      Topo builds container images on the host, transfers them to the target over SSH, and starts
      the services on the target. It can also build and deploy directly on the target if you choose
      that workflow.
# END generated_summary_faq

author: Matt Cossins

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
armips:
    - Neoverse
    - Cortex-A
    - Cortex-M
tools_software_languages:
    - Topo
    - Docker
    - SSH
    - Visual Studio Code
operatingsystems:
    - Linux
    - macOS
    - Windows

### Cross-platform metadata only
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - embedded-and-microcontrollers

further_reading:
    - resource:
        title: Topo repository
        link: https://github.com/arm/topo
        type: documentation
    - resource:
        title: Topo Project specification
        link: https://github.com/arm/topo/tree/main/docs/project-specification
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
        title: Topo VS Code extension
        link: https://marketplace.visualstudio.com/items?itemName=Arm.topo
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

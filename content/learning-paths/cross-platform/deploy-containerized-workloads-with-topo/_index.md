---
title: Deploy containerized workloads to Arm-based Linux targets with Topo

description: Use Topo to detect Arm processor capabilities on a target device, select a compatible container template, and deploy containerized workloads to Arm-based Linux targets over SSH using the CLI or VS Code extension.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for embedded, edge, and cloud software developers who want to deploy containerized workloads to Arm-based Linux targets using Topo.

learning_objectives:
    - Install Topo and verify that the host and target environments are ready for deployment
    - Run health checks and generate a target description to identify compatible Arm processor features and templates
    - Clone a Topo template and deploy a containerized workload to an Arm-based Linux target
    - (Optional) Use the Topo VS Code extension to run the same target, template, and deployment workflow from Visual Studio Code
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
  generated_at: '2026-07-02T17:18:43Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 49368c669c0d44931ed68ba65bcd88321025a685cfd23ed73d43de7b35cacd07
  summary_generated_at: '2026-07-02T17:18:43Z'
  summary_source_hash: 49368c669c0d44931ed68ba65bcd88321025a685cfd23ed73d43de7b35cacd07
  faq_generated_at: '2026-07-02T17:18:43Z'
  faq_source_hash: 49368c669c0d44931ed68ba65bcd88321025a685cfd23ed73d43de7b35cacd07
  summary: >-
    This Learning Path shows how to use Topo to deploy containerized workloads to Arm-based Linux
    targets over SSH from a Linux, macOS, or Windows host. Learners install Topo, run health checks
    to validate the host and target, and generate a target description that identifies Arm CPU
    features such as Neon and SVE to guide template selection. Using a Topo template, you clone
    the LLM chatbot example and deploy it to the target; Topo builds the image on the host, transfers
    it, and starts services on the target. Optional sections demonstrate running the same workflow
    from the Topo Visual Studio Code extension and outline deployment to heterogeneous Cortex-A
    + Cortex-M systems using remoteproc-runtime.
  faqs:
  - question: How do I check that my host and target are ready before deploying?
    answer: >-
      Run topo health on the host. Use --target or set TOPO_TARGET to include the target check;
      confirm Topo, SSH, and Docker show as available.
  - question: How do I point Topo at the correct target device?
    answer: >-
      Provide the target using the --target option or set the TOPO_TARGET environment variable.
      Topo then connects to the Arm-based Linux target over SSH.
  - question: What should I expect after deploying the LLM chatbot template?
    answer: >-
      Topo builds the container image on the host, transfers it to the target, and starts the
      services on the target. You should see deployment and service start messages in the Topo
      output.
  - question: How do I know whether to use Neon or SVE optimizations?
    answer: >-
      Topo detects the target’s Arm CPU features and surfaces them in the target description.
      The LLM chatbot template defaults to Neon; choose an SVE option only if your target reports
      SVE support and the template prompts for it.
  - question: Can I perform the same workflow from Visual Studio Code?
    answer: >-
      Yes. Install the Topo extension from the Visual Studio Marketplace to use a graphical interface
      for the same target, template, and deployment steps.
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
        title: Topo VS Code extension
        link: https://marketplace.visualstudio.com/items?itemName=Arm.topo
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


---
title: Develop and validate firmware pre-silicon on Arm Neoverse CSS V3

minutes_to_complete: 90

who_is_this_for: This advanced topic is for firmware developers, system architects, and silicon validation engineers working on Arm Neoverse CSS platforms who require a pre-silicon workflow for the CSS-V3 reference design using Fixed Virtual Platforms (FVPs).

learning_objectives:
    - Understand the CSS-V3 architecture and the RD-V3 firmware boot sequence.
    - Set up a containerized build environment and sync sources with a pinned manifest using repo.
    - Build and boot the RD-V3 firmware stack on FVP and map UART consoles to components.
    - Interpret boot logs to verify bring-up and diagnose boot-stage issues.
    - Modify platform control firmware such as System Control Processor (SCP) and Manageability Control Processor (MCP), and validate changes through pre-silicon simulation.
    - Launch a dual-chip RD-V3-R1 simulation and verify application processor (AP) and MCP coordination.

prerequisites:
    - Access to an Arm Neoverse-based Linux machine (cloud or local) with at least 80 GB of free storage
    - Familiarity with Linux command-line tools and basic scripting
    - Understanding of firmware boot stages and SoC-level architecture
    - Docker installed, or a GitHub Codespaces-compatible development environment

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-01T19:38:48Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: edcf755937689018d68a687def84b27f119fcfa2542949294f965c21e0d0d642
  summary_generated_at: '2026-10-01T19:38:48Z'
  summary_source_hash: edcf755937689018d68a687def84b27f119fcfa2542949294f965c21e0d0d642
  faq_generated_at: '2026-10-01T19:38:48Z'
  faq_source_hash: edcf755937689018d68a687def84b27f119fcfa2542949294f965c21e0d0d642
  summary: >-
    You'll build the Arm Neoverse RD-V3 firmware stack and test it on an Arm FVP
    before hardware is available. First, you'll prepare a repeatable environment, sync pinned sources, compile
    the boot chain, and select the FVP version that matches your release. You'll then map UART consoles,
    follow the boot to a Buildroot Linux shell, validate firmware changes, and run the dual-chip
    RD-V3-R1 simulation.
  faqs:
  - question: How do I choose the correct FVP model for my RD-V3 build?
    answer: >-
      Match the FVP model version to the RD-V3 release tag that you're using. Use the
      example mapping as reference and refer to the release tags list for the full set of supported versions.
  - question: What result should I expect when the single-die simulation boots successfully?
    answer: >-
      The system boots from BL1 through the firmware stack to a Buildroot Linux shell on the FVP.
      You should see logs across the mapped UART consoles for each stage and a Linux prompt on
      the application processor path.
  - question: Where can I find the UART logs from the RD-V3 simulation?
    answer: >-
      Look in `~/rdv3/model-scripts/rdinfra/platforms/rdv3/rdv3`, where each UART is redirected
      to its own log file. Use the UART-to-terminal mapping to identify the subsystem you
      want to inspect, such as Linux, TF-A and UEFI, SCP, RSE, MCP, or LCP.
  - question: How do I validate a change to SCP, MCP, or LCP firmware?
    answer: >-
      Rebuild the affected platform control firmware, then rerun the FVP simulation. Inspect the
      corresponding UART logs for your expected messages or behavior and confirm that the system still
      reaches the Linux shell.
  - question: How do I know the dual-chip RD-V3-R1 simulation is running correctly?
    answer: >-
      Look for a dual-AP boot flow and MCP activity coordinating across dies. Both dies should
      produce console output, and the expected cross-die management
      behavior should be visible in the logs.
# END generated_summary_faq

author:
    - Odin Shen
    - Ann Cheng

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
platforms:
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
  - Oracle Cloud Infrastructure (OCI) Ampere Compute
armips:
    - Neoverse
tools_software_languages:
    - C
    - Docker
    - FVP
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Neoverse Compute Subsystems V3
        link: https://www.arm.com/products/neoverse-compute-subsystems/css-v3
        type: website
    - resource:
        title: Reference Design software stack architecture
        link: https://neoverse-reference-design.docs.arm.com/en/latest/about/software_stack.html
        type: website
    - resource:
        title: GitLab infra-refdesign-manifests
        link: https://git.gitlab.arm.com/infra-solutions/reference-design/infra-refdesign-manifests
        type: gitlab    

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

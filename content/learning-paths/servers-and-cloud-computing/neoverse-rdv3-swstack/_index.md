---
title: Develop and Validate Firmware Pre-Silicon on Arm Neoverse CSS V3

minutes_to_complete: 90

who_is_this_for: This advanced topic is for firmware developers, system architects, and silicon validation engineers working on Arm Neoverse CSS platforms who require a pre-silicon workflow for the CSS-V3 reference design using Fixed Virtual Platforms (FVPs).

learning_objectives:
    - Explain the CSS-V3 architecture and the RD-V3 firmware boot sequence (TF-A, RSE, SCP/MCP/LCP, UEFI/GRUB, Linux)
    - Set up a containerized build environment and sync sources with a pinned manifest using repo
    - Build and boot the RD-V3 firmware stack on FVP and map UART consoles to components
    - Interpret boot logs to verify bring-up and diagnose boot-stage issues
    - Modify platform control firmware (for example, SCP/MCP) and validate changes via pre-silicon simulation
    - Launch a dual-chip RD-V3-R1 simulation and verify AP/MCP coordination
   
prerequisites:
    - Access to an Arm Neoverse-based Linux machine (cloud or local) with at least 80 GB of free storage
    - Familiarity with Linux command-line tools and basic scripting
    - Understanding of firmware boot stages and SoC-level architecture
    - Docker installed, or a GitHub Codespaces-compatible development environment

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:38:16Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 65336a8f8d1d11c4b127ea13982a581afffa94cbfd1af10a9e4df2becbc34b5a
  summary_generated_at: '2026-06-02T04:35:16Z'
  summary_source_hash: 65336a8f8d1d11c4b127ea13982a581afffa94cbfd1af10a9e4df2becbc34b5a
  faq_generated_at: '2026-06-03T01:38:16Z'
  faq_source_hash: 65336a8f8d1d11c4b127ea13982a581afffa94cbfd1af10a9e4df2becbc34b5a
  summary: >-
    This advanced Learning Path shows how to develop and validate firmware pre-silicon for Arm
    Neoverse CSS‑V3 using the RD‑V3 reference design and Arm Fixed Virtual Platforms (FVPs). You
    will examine the CSS‑V3 architecture and coordinated boot sequence (TF‑A, RSE, SCP/MCP/LCP,
    UEFI/GRUB, Linux), set up a containerized build environment, sync sources with a pinned repo
    manifest, then build and boot the RD‑V3 firmware stack on an FVP. The steps include mapping
    UART consoles, interpreting boot logs, and bringing the stack to a Linux shell with Buildroot.
    You will also modify platform control firmware and run a dual‑chip RD‑V3‑R1 simulation. This
    path takes about 90 minutes and assumes an Arm Neoverse‑based Linux machine, Docker or Codespaces,
    and prior firmware knowledge.
  faqs:
  - question: What do I need before running the build and simulation steps?
    answer: >-
      You need access to an Arm Neoverse‑based Linux machine with at least 80 GB of free storage,
      Docker installed or a GitHub Codespaces‑compatible environment, and familiarity with Linux
      command‑line tools and basic scripting. An understanding of firmware boot stages and SoC‑level
      architecture is also required.
  - question: Which FVP model version should I use with my RD‑V3 release tag?
    answer: >-
      Each RD‑V3 release tag maps to a specific FVP version. For example, the RD‑INFRA‑2025.07.03
      tag is designed to work with FVP version 11.29.35; consult the RD‑V3 Release Tags to select
      and install the matching model.
  - question: What result should I expect when the FVP simulation completes successfully?
    answer: >-
      The simulation brings up the full firmware stack from BL1 to a Linux shell using Buildroot.
      You should see boot logs across the mapped UART consoles for components including TF‑A,
      RSE, SCP/MCP/LCP, and UEFI/GRUB, ending at a Linux shell prompt.
  - question: How do I diagnose issues if the boot sequence stalls?
    answer: >-
      Use the mapped UART consoles and boot logs to identify the active or failing stage and verify
      the expected handoffs across TF‑A, RSE, SCP/MCP/LCP, and UEFI. The steps show how to interpret
      logs to verify bring‑up and locate boot‑stage issues.
  - question: What is different about running the dual‑chip RD‑V3‑R1 simulation, and what should
      I verify?
    answer: >-
      RD‑V3‑R1 models a dual‑chip platform with two application processors and a Management Control
      Processor (Cortex‑M7) for cross‑die management. You will launch the dual‑chip simulation
      and verify AP/MCP coordination and the chiplet‑style boot flow.
# END generated_summary_faq

author:
    - Odin Shen
    - Ann Cheng

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
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


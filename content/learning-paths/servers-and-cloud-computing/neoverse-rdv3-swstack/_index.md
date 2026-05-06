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

# rerun_summary: false
# rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:58Z'
  generator: template
  source_hash: 65336a8f8d1d11c4b127ea13982a581afffa94cbfd1af10a9e4df2becbc34b5a
  summary: >-
    Develop and Validate Firmware Pre-Silicon on Arm Neoverse CSS V3 walks you through an end-to-end
    Arm software workflow. It is designed for This advanced topic is for firmware developers,
    system architects, and silicon validation engineers working on Arm Neoverse CSS platforms
    who require a pre-silicon workflow for the CSS-V3 reference design using Fixed Virtual Platforms
    (FVPs). By the end, you will be able to explain the CSS-V3 architecture and the RD-V3 firmware
    boot sequence (TF-A, RSE, SCP/MCP/LCP, UEFI/GRUB, Linux), set up a containerized build environment
    and sync sources with a pinned manifest using repo, and build and boot the RD-V3 firmware
    stack on FVP and map UART consoles to components. It focuses on tools and technologies such
    as C, Docker, and FVP, Linux environments, Arm platforms including Neoverse, and cloud platforms
    such as AWS, Microsoft Azure, Google Cloud, and Oracle. The main steps cover Learn about the
    Arm RD-V3 Platform, Understand the CSS-V3 boot flow and firmware stack, Build the RD-V3 Reference
    Platform Software Stack, Simulate RD-V3 Boot Flow on Arm FVP, and Simulate Dual Chip RD-V3-R1
    Platform.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will explain the CSS-V3 architecture and the RD-V3 firmware boot sequence (TF-A, RSE,
      SCP/MCP/LCP, UEFI/GRUB, Linux), set up a containerized build environment and sync sources
      with a pinned manifest using repo, and build and boot the RD-V3 firmware stack on FVP and
      map UART consoles to components.
  - question: Who is this Learning Path for?
    answer: >-
      This advanced topic is for firmware developers, system architects, and silicon validation
      engineers working on Arm Neoverse CSS platforms who require a pre-silicon workflow for the
      CSS-V3 reference design using Fixed Virtual Platforms (FVPs).
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: Access to an Arm Neoverse-based Linux
      machine (cloud or local) with at least 80 GB of free storage; Familiarity with Linux command-line
      tools and basic scripting; Understanding of firmware boot stages and SoC-level architecture;
      Docker installed, or a GitHub Codespaces-compatible development environment.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including C, Docker, and FVP, Linux environments, Arm platforms
      such as Neoverse, and cloud platforms such as AWS, Microsoft Azure, Google Cloud, and Oracle.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Learn about the Arm RD-V3 Platform, Understand the
      CSS-V3 boot flow and firmware stack, Build the RD-V3 Reference Platform Software Stack,
      Simulate RD-V3 Boot Flow on Arm FVP, and Simulate Dual Chip RD-V3-R1 Platform.
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


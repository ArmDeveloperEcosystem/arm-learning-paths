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

author:
    - Odin Shen
    - Ann Cheng

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
cloud_service_providers:
  - AWS
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

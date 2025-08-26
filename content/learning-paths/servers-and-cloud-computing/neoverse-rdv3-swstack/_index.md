---
title: CSS-V3 Pre-Silicon Software Development Using Neoverse Servers

minutes_to_complete: 90

who_is_this_for: This Learning Path is for firmware developers, system architects, and silicon validation engineers building Arm Neoverse CSS  platforms. It focuses on pre-silicon development using Fixed Virtual Platforms (FVPs) for the CSS‑V3 reference design. You’ll learn how to build, customize, and validate firmware on the RD‑V3 platform using Fixed Virtual Platforms (FVPs) before hardware is available.

learning_objectives:
    - Understand the architecture of Arm Neoverse CSS‑V3 as the foundation for scalable server-class platforms
    - Build and boot the RD‑V3 firmware stack using TF‑A, SCP, RSE, and UEFI
    - Simulate multi-core, multi-chip systems with Arm FVP models and interpret boot logs
    - Modify platform control firmware to test custom logic and validate it via pre-silicon simulation 

prerequisites:
    - Access to an Arm Neoverse-based Linux machine (cloud or local), with at least 80 GB of storage
    - Familiarity with Linux command-line tools and basic scripting
    - Understanding of firmware boot stages and SoC-level architecture
    - Docker installed, or GitHub Codespaces-compatible development environment

author:
    - Odin Shen
    - Ann Cheng

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
armips:
    - Neoverse
tools_software_languages:
    - C
    - Docker
    - FVP
peratingsystems:
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

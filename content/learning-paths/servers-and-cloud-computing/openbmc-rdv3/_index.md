---
title: Simulate Pre-Silicon Integration of OpenBMC and UEFI on Neoverse RD-V3

minutes_to_complete: 120

who_is_this_for: This Learning Path is for firmware developers, platform software engineers, and system integrators working on Arm Neoverse-based platforms. It is especially useful for those exploring pre-silicon development, testing, and integration of Baseboard Management Controllers (BMC) with UEFI firmware. If you are building or validating server-class reference platforms—such as RD-V3—before hardware is available, this guide will help you simulate and debug the full boot path using Fixed Virtual Platforms (FVPs).

learning_objectives:
    - Understand the role of OpenBMC and UEFI in Arm server boot flow
    - Set up and simulate firmware integration using the RD-V3 FVP
    - Build and launch OpenBMC and UEFI images in a pre-silicon environment
    - Validate host-BMC communication via UART and Serial-over-LAN
    - Implement and validate a custom IPMI command in OpenBMC

prerequisites:
    - Access to an Arm Neoverse-based Linux machine (either cloud-based or local) is required, with at least 80 GB of free disk space, 48 GB of RAM, and running Ubuntu 22.04 LTS.
    - Working knowledge of Docker, Git, and Linux terminal tools
    - Basic understanding of server firmware stack (UEFI, BMC, TF-A, etc.)
    - Docker installed, or GitHub Codespaces-compatible development environment

author:
    - Odin Shen
    - Ken Zhang

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
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
        title: Reference Design software stack architecture
        link: https://neoverse-reference-design.docs.arm.com/en/latest/about/software_stack.html
        type: website
    - resource:
        title: OpenBMC website
        link: https://www.openbmc.org/
        type: website
    - resource:
        title: Meta FVP base
        link: https://github.com/openbmc/openbmc/tree/master/meta-evb/meta-evb-arm/meta-evb-fvp-base
        type: github
    - resource:
        title: OpenBMC on FVP PoC
        link: https://gitlab.arm.com/server_management/PoCs/fvp-poc
        type: gitlab
    - resource:
        title: ipmitool documentation
        link: https://linux.die.net/man/1/ipmitool
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

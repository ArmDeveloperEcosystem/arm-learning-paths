---
title: Simulate OpenBMC and UEFI pre-silicon on Neoverse RD-V3

minutes_to_complete: 120

who_is_this_for: This advanced topic is for firmware developers, platform software engineers, and system integrators working on Arm Neoverse-based platforms. It is especially useful for developers exploring pre-silicon development, testing, and integration of Baseboard Management Controllers (BMC) with UEFI firmware. If you are building or validating server-class reference platforms such as RD-V3, before hardware is available, this Learning Path shows you how to simulate and debug the full boot path using Fixed Virtual Platforms (FVPs).

learning_objectives:
  - Understand the role of OpenBMC and UEFI in the Arm server boot flow
  - Simulate the firmware using the RD-V3 FVP
  - Build and launch OpenBMC and UEFI images on the RD-V3 FVP
  - Validate host–BMC communication using UART and Serial over LAN (SoL)
  - Implement and validate a custom IPMI command in OpenBMC

prerequisites:
  - An Arm Neoverse-based Linux machine (cloud or local) running Ubuntu 22.04 LTS
  - At least 80 GB free disk space and 48 GB RAM
  - Working knowledge of Docker, Git, and common Linux terminal tools
  - Basic understanding of the server firmware stack (such as UEFI, BMC, and TF-A)

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
  - OpenBMC
  - Yocto/BitBake
  - ipmitool
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
      title: Meta FVP base (OpenBMC)
      link: https://github.com/openbmc/openbmc/tree/master/meta-evb/meta-evb-arm/meta-evb-fvp-base
      type: website
  - resource:
      title: OpenBMC on FVP PoC
      link: https://gitlab.arm.com/server_management/PoCs/fvp-poc
      type: website
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

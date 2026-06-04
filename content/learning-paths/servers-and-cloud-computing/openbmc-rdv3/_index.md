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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:43:38Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: dec913a7a15e82ebf129e2ac64cba8d9140694840f8f9e817fb091b0c82c4cab
  summary_generated_at: '2026-06-02T04:41:47Z'
  summary_source_hash: dec913a7a15e82ebf129e2ac64cba8d9140694840f8f9e817fb091b0c82c4cab
  faq_generated_at: '2026-06-03T01:43:38Z'
  faq_source_hash: dec913a7a15e82ebf129e2ac64cba8d9140694840f8f9e817fb091b0c82c4cab
  summary: >-
    This advanced Learning Path shows how to build and simulate OpenBMC and UEFI firmware pre-silicon
    on the Arm Neoverse RD-V3 r1 Fixed Virtual Platform (FVP). You will set up a Docker-based
    build environment, compile OpenBMC and host UEFI images, launch the RD-V3 FVP, and observe
    the boot across multiple UART consoles. You will validate host–BMC communication using UART
    and Serial over LAN (SoL), access the host console through the OpenBMC web UI, and implement
    a custom IPMI command in C++ for validation. Prerequisites include an Arm Neoverse-based Ubuntu
    22.04 LTS system with 80 GB free disk space, 48 GB RAM, and familiarity with Docker, Git,
    and Linux tools. Tools include OpenBMC, Yocto/BitBake, FVP, C/C++, and ipmitool.
  faqs:
  - question: What do I need before running the builds?
    answer: >-
      Use an Arm Neoverse-based Linux machine running Ubuntu 22.04 LTS with at least 80 GB free
      disk space and 48 GB RAM. You should be comfortable with Docker, Git, common Linux terminal
      tools, and have a basic understanding of UEFI, BMC, and TF-A.
  - question: How do I know the RD-V3 FVP booted OpenBMC and UEFI correctly?
    answer: >-
      After launching the FVP, you should see multiple UART consoles for subsystems such as Neoverse
      V3, Cortex-M55, Cortex-M7, and the Cortex-A BMC. Successful boot is indicated by visible
      boot logs on these consoles for both the BMC and the host UEFI firmware.
  - question: What should I check if the UART console windows do not appear?
    answer: >-
      The simulation opens multiple graphical UART terminals and requires a desktop session. If
      you connect over SSH only, these consoles will not render; switch to a desktop environment
      or an appropriate session that supports GUI windows.
  - question: How do I access the host console through OpenBMC?
    answer: >-
      Use OpenBMC Serial over LAN (SoL). Create a virtual UART bridge with socat between the host-side
      and BMC-side ports (for example, tcp:localhost:5005 to tcp:localhost:5067), verify the mappings,
      then open the host console from the BMC web UI.
  - question: How do I add and validate a custom IPMI command in OpenBMC?
    answer: >-
      Implement a custom IPMI command handler in C++, package it with Yocto/BitBake, and rebuild
      the OpenBMC image. Run it on the FVP and confirm it returns the expected simple string response,
      using the steps provided (you can invoke it with ipmitool).
# END generated_summary_faq

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


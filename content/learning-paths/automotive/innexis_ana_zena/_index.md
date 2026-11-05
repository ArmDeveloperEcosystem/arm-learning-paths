---
title: Get Started with Arm Zena CSS on Siemens Innexis ANA
description: With Siemens Innexis ANA 2026.2, start a Zena CSS virtual platform, boot EWAOL Linux, connect to the guest, and exchange a file.

minutes_to_complete: 60

who_is_this_for: Automotive and embedded Linux developers with access to an Innexis ANA chamber.

learning_objectives:
    - Create and start an Arm Zena CSS virtual platform in Innexis ANA.
    - Identify the boot consoles, verify EWAOL Linux boot, and inspect the guest environment.
    - Connect to the Linux guest through ANA's authorized SSH tunnel.
    - Exchange a test file with the Linux guest and check its contents. 
prerequisites:
    - Access to an operating Siemens Innexis ANA chamber with the Arm-Zena-CSS vSoC and its EWAOL software stack.
    - Permission to use the chamber and its supplied software assets.
    - Basic familiarity with the Linux command line.
    - A local SSH client and a public key that you can authorize for the selected virtual platform.

author: Odin Shen

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
armips:
    - Cortex-A
    - Cortex-R
    - Cortex-M
tools_software_languages:
    - Arm Zena CSS
    - Siemens Innexis ANA
    - SSH
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Zena CSS
        link: https://www.arm.com/products/autonomous-machines/zena-compute-subsystems
        type: documentation
    - resource:
        title: Siemens Innexis Architecture Native Acceleration
        link: https://www.siemens.com/en-gb/products/ic/hav/innexis/architecture-native-acceleration/
        type: documentation
    - resource:
        title: EWAOL development
        link: https://gitlab.com/soafee/ewaol/meta-ewaol
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

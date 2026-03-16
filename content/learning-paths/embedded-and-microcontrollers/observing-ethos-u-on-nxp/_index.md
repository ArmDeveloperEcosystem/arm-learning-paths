---
title: Deploy ExecuTorch firmware on NXP FRDM i.MX 93 for Ethos-U65 acceleration

draft: true
cascade:
    draft: true
    
minutes_to_complete: 120

who_is_this_for: This is an introductory topic for developers and data scientists new to Tiny Machine Learning (TinyML), who want to observe ExecuTorch performance on a physical device.

learning_objectives:
    - Bring up a custom ExecuTorch `executor_runner` firmware on the FRDM i.MX 93 Cortex-M33 using Linux RemoteProc.
    - Compile an ExecuTorch `.pte` model for Ethos-U65 and run inference with NPU acceleration.
    - Understand how heterogeneous Arm systems split responsibilities across application cores, microcontrollers, and NPUs.
prerequisites:
    - An NXP [FRDM i.MX 93](https://www.nxp.com/design/design-center/development-boards-and-designs/frdm-i-mx-93-development-board:FRDM-IMX93) development board.
    - A USB Mini-B to USB Type-A cable, or a USB Mini-B to USB Type-C cable.
    - Completion of [Linux on an NXP FRDM i.MX 93 board](/learning-paths/embedded-and-microcontrollers/linux-nxp-board/) (Linux setup, login access, and file transfer).
    - Basic knowledge of Machine Learning concepts.
    - A host computer to compile ExecuTorch libraries.

author: 
- Waheed Brown
- Fidel Makatia Omusilibwa

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A
    - Cortex-M
    - Ethos-U

operatingsystems:
    - Linux
    - macOS

tools_software_languages:
    - Baremetal
    - Python
    - PyTorch
    - ExecuTorch
    - Arm Compute Library
    - GCC

further_reading:
    - resource:
        title: TinyML Brings AI to Smallest Arm Devices
        link: https://newsroom.arm.com/blog/tinyml
        type: blog
    - resource:
        title: Arm Machine Learning Resources
        link: https://www.arm.com/developer-hub/embedded-and-microcontrollers/ml-solutions/getting-started
        type: documentation
    - resource:
        title: Arm Developers Guide for Cortex-M Processors and Ethos-U NPU
        link: https://developer.arm.com/documentation/109267/0101
        type: documentation




### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

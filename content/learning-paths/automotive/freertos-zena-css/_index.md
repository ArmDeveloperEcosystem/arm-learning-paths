---
title: Port FreeRTOS to the Arm Zena CSS Safety Island
description: Port a FreeRTOS SMP application to Cortex-R82AE, run it on the Arm Zena CSS Safety Island, and prepare it for Yocto integration.

minutes_to_complete: 120

who_is_this_for: This advanced topic is for embedded and automotive software developers who want to replace the Zephyr Safety Island image in the Arm Zena CSS Reference Software Stack with FreeRTOS.

learning_objectives:
  - Build and validate a four-core FreeRTOS SMP port on the Cortex-R82AE FVP
  - Adapt the port's boot, memory, and UART configuration for the Zena CSS Safety Island
  - Load the FreeRTOS binary directly into the Zena CSS FVP and verify execution
  - Plan a Yocto recipe and image-selection flow that packages FreeRTOS instead of Zephyr

prerequisites:
  - An Ubuntu 22.04 or later development host
  - Experience with FreeRTOS, CMake, linker scripts, and Arm exception levels
  - Arm GNU Toolchain 15.2 or Arm Compiler for Embedded 6.24
  - Access to the FreeRTOS Cortex-R82AE port repository
  - A working Arm Zena CSS Reference Software Stack build and its FVP

draft: true
cascade:
  draft: true

author: Julien Jayat

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
  - Cortex-R
operatingsystems:
  - Linux
  - RTOS
tools_software_languages:
  - FreeRTOS
  - Arm Zena CSS
  - FVP
  - GCC
  - Arm Compiler for Embedded
  - CMake
  - Yocto
  - BitBake

further_reading:
  - resource:
      title: FreeRTOS Kernel
      link: https://github.com/FreeRTOS/FreeRTOS-Kernel
      type: website
  - resource:
      title: FreeRTOS Cortex-R82 SMP MPU FVP demo
      link: https://github.com/FreeRTOS/FreeRTOS-Partner-Supported-Demos/tree/main/CORTEX_R82_SMP_MPU_FVP_GCC_ARMCLANG
      type: website
  - resource:
      title: Arm Zena CSS Reference Software Stack documentation
      link: https://arm-zena-css.docs.arm.com/en/latest/
      type: documentation
  - resource:
      title: Arm Cortex-R82AE
      link: https://developer.arm.com/Processors/Cortex-R82AE
      type: website
  - resource:
      title: Yocto Project development tasks manual
      link: https://docs.yoctoproject.org/dev-manual/index.html
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: learningpathall
learning_path_main_page: "yes"
---

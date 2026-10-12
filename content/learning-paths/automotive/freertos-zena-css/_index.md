---
title: Port and integrate FreeRTOS on the Arm Zena CSS Safety Island

draft: true
cascade:
    draft: true

description: Port a FreeRTOS SMP application to Cortex-R82AE and integrate it as signed, Yocto-built firmware for the Arm Zena CSS Safety Island.

minutes_to_complete: 180

who_is_this_for: This advanced topic is for embedded and automotive software developers who want to replace the Zephyr Safety Island image in the Arm Zena CSS Reference Software Stack with FreeRTOS.

learning_objectives:
  - Build and validate a four-core FreeRTOS SMP port on the standalone Cortex-R82AE FVP
  - Adapt the port's boot, memory, and UART configuration for the Zena CSS Safety Island and verify direct loading
  - Validate FreeRTOS as the Cluster 1 firmware through the standard Zena CSS secure boot flow
  - Implement and validate a selectable Yocto recipe that builds, signs, and packages FreeRTOS instead of Zephyr

prerequisites:
  - An Ubuntu 22.04 instance; later Ubuntu versions do not work for this build
  - Experience with FreeRTOS, CMake, linker scripts, and Arm exception levels
  - Arm GNU Toolchain 15.2 or Arm Compiler for Embedded 6.24
  - Access to the Cortex-R82AE demo and kernel repositories
  - A working Arm Zena CSS Reference Software Stack build and its FVP

author:
    - Julien Jayat
    - Jaxson Han

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
      title: FreeRTOS Cortex-R82AE Kernel branch
      link: https://github.com/JulienJayat-Arm/FreeRTOS-Kernel/tree/R82AE-demo
      type: website
  - resource:
      title: FreeRTOS Cortex-R82AE SMP MPU FVP demo
      link: https://github.com/JulienJayat-Arm/FreeRTOS-Partner-Supported-Demos/tree/R82AE-demo/CORTEX_R82AE_SMP_FVP_MPU_GCC_ARMCLANG
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

---
title: Port and integrate FreeRTOS on the Arm Zena CSS Safety Island

description: Port a FreeRTOS SMP application to Cortex-R82AE and integrate it as signed, Yocto-built firmware for the Arm Zena CSS Safety Island.

minutes_to_complete: 180

who_is_this_for: This advanced topic is for embedded and automotive software developers who want to replace the Zephyr Safety Island image in the Arm Zena CSS Reference Software Stack with FreeRTOS.

learning_objectives:
  - Build and validate a four-core FreeRTOS SMP port on the standalone Cortex-R82AE FVP.
  - Adapt the port's boot, memory, and UART configuration for the Zena CSS Safety Island and verify direct loading.
  - Validate FreeRTOS as the Cluster 1 firmware through the standard Zena CSS secure boot flow.
  - Implement and validate a selectable Yocto recipe that builds, signs, and packages FreeRTOS instead of Zephyr.

prerequisites:
  - An Ubuntu 22.04 instance
  - Experience with FreeRTOS, CMake, linker scripts, and Arm exception levels
  - Arm [GNU Toolchain 15.3](https://gitlab.arm.com/tooling/gnu-toolchains-for-arm/-/tree/releases/15.3.rel1?ref_type=heads#linux) or [Arm Compiler for Embedded 6.24](https://support.arm.com/downloads/view/ACOMPE?sortBy=availableBy&revision=r6p24-00rel0), CMake 3.22.1, and [`FVP_BaseR_AEMv8R` from Fast Models 11.32](https://support.arm.com/tools-and-software/fixed-virtual-platforms/arm-architecture-fvps)
  - Access to the Cortex-R82AE demo and kernel repositories
  - A working Arm Zena CSS Reference Software Stack build and its FVP

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-21T18:44:21Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d0ae0dee80bfc0bf8cba7fdaf74e429ced3012a3694da73d065b532d1215b0d0
  summary_generated_at: '2026-10-21T18:44:21Z'
  summary_source_hash: d0ae0dee80bfc0bf8cba7fdaf74e429ced3012a3694da73d065b532d1215b0d0
  faq_generated_at: '2026-10-21T18:44:21Z'
  faq_source_hash: d0ae0dee80bfc0bf8cba7fdaf74e429ced3012a3694da73d065b532d1215b0d0
  summary: >-
    You'll port a four-core FreeRTOS application to the Arm Zena CSS Safety Island and integrate it
    into the reference software stack. First, you'll verify the Cortex-R82 demo, then adapt and debug
    it on the standalone Cortex-R82AE FVP. You'll then configure Zena CSS and load the binary directly
    into Safety Island Cluster 1. Next, you'll substitute the firmware to validate secure boot. Finally, you'll apply
    and inspect a Yocto patch that makes FreeRTOS selectable.
  # faqs:
  # - question: What should I check if the FreeRTOS application fails early on the standalone Cortex-R82AE FVP?
  #   answer: Check each bring-up stage before moving to the next. You can use Arm Development Studio for source-level debugging or Tarmac Trace to locate where startup stops.
  # - question: What must I change before loading FreeRTOS directly into Zena CSS Cluster 1?
  #   answer: You need to use the Zena CSS memory map, Safety Island UART address, and Cluster 1 interrupt configuration. For direct loading, configure GIC view 0 and start the FVP reference counter so the scheduler tick can run.
  # - question: How do I test FreeRTOS through the normal Zena CSS secure boot flow?
  #   answer: Build the `zena_css_fvp` binary, substitute it for the Cluster 1 payload in `do_sign_images()`, rebuild the signed firmware image, and boot the Zena CSS FVP. At the SI CL1 console, enter `ping` and check for responses from cores 0 through 3.
  # - question: How do I select FreeRTOS instead of Zephyr in the Yocto build?
  #   answer: Apply the supplied `freertos-yocto-integration.patch` to a clean Zena CSS checkout. In `kas menu`, select **RD-Aspen Cfg2** and **FreeRTOS** under **Safety Island RTOS**, then run `kas build`.
  # - question: How can I verify that Yocto built and booted the FreeRTOS image?
  #   answer: Check that `pn-buildlist` contains `freertos-demos-cl1` instead of `zephyr-demos-cl1`, then inspect the deployed FreeRTOS binary and RSE flash image. Boot the FVP and enter `ping` at the SI CL1 console; responses from all four cores confirm runtime operation.
# END generated_summary_faq

author:
    - Julien Jayat
    - Jaxson Han

generate_summary_faq: false
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

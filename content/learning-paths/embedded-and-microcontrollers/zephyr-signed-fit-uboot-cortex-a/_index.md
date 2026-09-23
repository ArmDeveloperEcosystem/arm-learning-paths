---
title: Boot Zephyr from a signed FIT image with U-Boot on Arm Cortex-A

description: Learn how to sign a Zephyr image in a FIT, build the public key into U-Boot, and start Zephyr on Arm Cortex-A only after U-Boot verifies it, in QEMU with no hardware and then on a TI AM62L EVM.

minutes_to_complete: 120

who_is_this_for: This is an advanced topic for embedded developers who run Zephyr on an Arm Cortex-A processor behind U-Boot and want the bootloader to verify the Zephyr image before starting it.

learning_objectives:
    - Explain where a Zephyr image sits in the Cortex-A boot chain and which stage can verify it
    - Build and sign a Zephyr image in a FIT, and build the public key into U-Boot without changing U-Boot source
    - Write a U-Boot boot command that starts Zephyr only after the signature and hash checks pass, and optionally prove on the target that it refuses a wrong key and a tampered image
    - Explain what a board in its development state, and what an emulator, each leave unverified, and what a production device needs on top

prerequisites:
    - One of two targets, either QEMU, which needs no hardware at all, or a TI [AM62L EVM](https://www.ti.com/tool/TMDS62LEVM) with a micro-SD card and an SD card reader for your host, a micro-USB cable for the console and a USB-C Power Delivery (PD) power supply
    - A Linux host running Ubuntu 22.04 or 24.04, with about 5 GB of free disk space for QEMU or 20 GB for the AM62L EVM; the EVM also needs an x86_64 host, because the TI SDK ships its installer and cross compiler as x86_64 binaries only
    - Visual Studio Code with the [Workbench for Zephyr extension](https://marketplace.visualstudio.com/items?itemName=Ac6.zephyr-workbench) and its host tools installed, as in the first steps of [Build Zephyr projects with Workbench for Zephyr in VS Code](/learning-paths/embedded-and-microcontrollers/zephyr_vsworkbench/)
    - Basic knowledge of U-Boot and the Linux command line

author:
    - Roy Jamil
    - Odin Shen

# New Learning Paths are opted in for the next manual generated summary/FAQ run.
# The generator resets this to false after a successful write.
generate_summary_faq: true

# Optional one-shot controls: set either field to true to regenerate just that
# generated section the next time the summary/FAQ tool runs. The tool resets
# them to false after a successful write.
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Security
armips:
    - Cortex-A
tools_software_languages:
    - Zephyr
    - Workbench for Zephyr
    - Visual Studio Code
    - U-Boot
    - QEMU
    - OpenSSL
    - GCC
    - C
operatingsystems:
    - RTOS
    - Linux

further_reading:
    - resource:
        title: U-Boot FIT signature verification
        link: https://docs.u-boot.org/en/latest/usage/fit/signature.html
        type: documentation
    - resource:
        title: U-Boot documentation for TI K3 boards, including the secure boot chain of trust
        link: https://docs.u-boot.org/en/latest/board/ti/k3.html
        type: documentation
    - resource:
        title: Zephyr AM62L EVM board documentation
        link: https://docs.zephyrproject.org/latest/boards/ti/am62l_evm/doc/index.html
        type: documentation
    - resource:
        title: U-Boot documentation for the QEMU Arm board
        link: https://docs.u-boot.org/en/latest/board/emulation/qemu-arm.html
        type: documentation
    - resource:
        title: Zephyr QEMU Cortex-A53 board documentation
        link: https://docs.zephyrproject.org/latest/boards/qemu/cortex_a53/doc/index.html
        type: documentation
    - resource:
        title: Workbench for Zephyr
        link: https://z-workbench.com/
        type: website
    - resource:
        title: Ac6 training, Zephyr RTOS programming
        link: https://www.ac6-training.com/en/rt5/zephyr-rtos-programming
        type: website
    - resource:
        title: Ac6 training, Secured embedded Linux platform build
        link: https://www.ac6-training.com/en/sec8/secured-embedded-linux-platform-build
        type: website
    - resource:
        title: Ac6 training, AI-assisted embedded development
        link: https://www.ac6-training.com/en/ai1/ai-assisted-embedded-development
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

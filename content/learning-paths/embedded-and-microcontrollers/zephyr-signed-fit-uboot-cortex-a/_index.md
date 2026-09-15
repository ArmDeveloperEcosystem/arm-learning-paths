---
title: Boot Zephyr from a signed FIT image with U-Boot on Arm Cortex-A

description: Learn how to sign a Zephyr image in a FIT, build the public key into U-Boot, and start Zephyr on an Arm Cortex-A board only after U-Boot verifies it, using the TI AM62L EVM as the example.

minutes_to_complete: 120

who_is_this_for: This is an advanced topic for embedded developers who run Zephyr on an Arm Cortex-A processor behind U-Boot and want the bootloader to verify the Zephyr image before it starts.

learning_objectives:
    - Explain where a Zephyr image sits in the Cortex-A boot chain and which stage can verify it
    - Build and sign a Zephyr image in a FIT, and build the public key into U-Boot without changing U-Boot source
    - Write a U-Boot boot command that starts Zephyr only after the signature and hash checks pass, and prove it on the board with a wrong key and a tampered image
    - Explain what an HS-FS board leaves unverified and what a production device needs, such as a fused key, a locked console and no unverified boot path

prerequisites:
    - A TI [AM62L EVM](https://www.ti.com/tool/TMDS62LEVM) with a micro-SD card, a micro-USB cable for the console, and a USB-C PD power supply
    - An x86_64 Linux host running Ubuntu 22.04 or 24.04, with about 20 GB of free disk space
    - A Zephyr workspace with Zephyr 4.4 or later and the Zephyr SDK, set up as described in the [Zephyr Getting Started Guide](https://docs.zephyrproject.org/latest/develop/getting_started/index.html)
    - Basic knowledge of U-Boot and the Linux command line

author: Roy Jamil

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
    - U-Boot
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
        title: TI Processor SDK Linux for AM62Lx 12.01.00.05.03
        link: https://www.ti.com/tool/download/AM62L-LINUX-SDK/12.01.00.05.03
        type: website
    - resource:
        title: AM62L EVM User's Guide
        link: https://www.ti.com/lit/pdf/SPRUJG8
        type: documentation
    - resource:
        title: AC6 Zephyr Training
        link: https://www.ac6-training.com/en/cours.php/cat_oRT/ref_oRT5/zephyr-rtos-programming
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

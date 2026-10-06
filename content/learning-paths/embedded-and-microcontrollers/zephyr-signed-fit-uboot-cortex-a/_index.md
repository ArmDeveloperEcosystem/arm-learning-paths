---
title: Boot a signed Zephyr image with U-Boot on Arm Cortex-A

description: Sign a Zephyr FIT image and configure U-Boot to verify its signature and payload hash before booting on Arm Cortex-A in QEMU or on a TI AM62L EVM.

minutes_to_complete: 120

who_is_this_for: This is an advanced topic for embedded developers who boot Zephyr from U-Boot on an Arm Cortex-A processor and want U-Boot to verify the Zephyr image before starting it.

learning_objectives:
    - Identify where U-Boot verifies Zephyr in the Arm Cortex-A boot chain.
    - Build and sign a Flattened Image Tree (FIT) containing Zephyr, and embed the public key in U-Boot without changing its source.
    - Configure U-Boot to verify Zephyr before booting, and optionally test rejection of wrong-key and tampered images.
    - Identify the verification boundary in QEMU and on a development board, and how fusing your key extends trust in production.

prerequisites:
    - One of two targets - QEMU, which needs no hardware, or a TI [AM62L EVM](https://www.ti.com/tool/TMDS62LEVM) with accessories to power it, write an SD card, and attach a serial console
    - A Linux host running Ubuntu 22.04 or 24.04, with about 20 GB of free disk space; QEMU runs on x86_64 or arm64, while the AM62L EVM needs x86_64 for the TI SDK
    - Visual Studio Code with the [Workbench for Zephyr extension](https://marketplace.visualstudio.com/items?itemName=Ac6.zephyr-workbench) installed
    - Basic knowledge of U-Boot and the Linux command line

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-06T18:12:37Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d29bf65cd5b55f7b412beeb0a62873a02eec10189fb6c259f2a5f84f9d016416
  summary_generated_at: '2026-10-06T18:12:37Z'
  summary_source_hash: d29bf65cd5b55f7b412beeb0a62873a02eec10189fb6c259f2a5f84f9d016416
  faq_generated_at: '2026-10-06T18:12:37Z'
  faq_source_hash: d29bf65cd5b55f7b412beeb0a62873a02eec10189fb6c259f2a5f84f9d016416
  summary: >-
    You'll build a Zephyr image for Arm Cortex-A and configure U-Boot to verify its signed FIT before booting. After choosing QEMU or a TI AM62L evaluation module (EVM), you'll set up the host
    tools, build Zephyr, sign the FIT, and embed the trusted public key in U-Boot. You'll then boot
    the image, optionally test rejection of untrusted or tampered images, and examine what remains
    outside the verification boundary.
  faqs:
  - question: Do I need an AM62L EVM to follow this Learning Path?
    answer: >-
      No. You can use QEMU without hardware. If you have an AM62L EVM, follow its target-specific
      setup and boot-media instructions instead.
  - question: Why does U-Boot need the public key in its control device tree?
    answer: >-
      You'll embed the trusted public key in U-Boot's control device tree so that it can verify the FIT
      configuration signature. The key's `required = "conf"` setting makes U-Boot reject a FIT
      without a valid signature from that key.
  - question: How can I check the signed FIT before booting the target?
    answer: >-
      Use U-Boot's `fit_check_sign` with your signed FIT and built `u-boot.dtb`. This checks the
      FIT against the public key in the control device tree before you prepare the boot media.
  - question: How do I confirm that verification succeeded on the target?
    answer: >-
      Look for `sha256,rsa2048:key-a+ OK` in U-Boot's output, followed by the Zephyr image A banner.
      You can also run the optional wrong-key and tampered-image tests to check that U-Boot refuses
      to start either image.
  - question: Does this setup authenticate U-Boot as well as Zephyr?
    answer: >-
      No. In QEMU, you run U-Boot without an earlier stage that authenticates it. On the AM62L EVM,
      you leave the device in High Security, Field Securable (HS-FS) development state, where earlier stages accept boot files
      signed with any key. To extend trust to U-Boot in production, you need to provision your key,
      move the device to High Security, Security Enforced (HS-SE), and sign the earlier boot files.
# END generated_summary_faq

author:
    - Roy Jamil
    - Odin Shen

# New Learning Paths are opted in for the next manual generated summary/FAQ run.
# The generator resets this to false after a successful write.
generate_summary_faq: false

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

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

---
title: Port Zephyr RTOS and run applications on the Arm Corstone-320 MPS4 platform
description: Port Zephyr RTOS to the Arm Corstone-320 MPS4 FPGA platform by creating board support files and device tree configuration, then build and run a hello_world sample on the physical board.

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for embedded developers who want to port Zephyr RTOS to the Arm Corstone-320 MPS4 FPGA platform.

learning_objectives: 
  - Set up the Zephyr build environment and Arm GNU Toolchain for Corstone-320 MPS4 development
  - Create board support files, including device tree, Kconfig, and board metadata, to port Zephyr to the Corstone-320 MPS4 FPGA platform
  - Build and run the hello_world sample on the Corstone-320 MPS4 board to validate the port

prerequisites: 
  - Basic familiarity with embedded C programming
  - Basic knowledge of Zephyr RTOS
  - A Corstone-320 MPS4 FPGA development board
  - A Linux development environment, for example Ubuntu 22.04 or later
  - Git and Python

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-13T19:02:39Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 6b08ed7a12b4f4ff6283dc5423ccd2f6a1fcca6535a3a2f67039a63d9623d457
  summary_generated_at: '2026-08-13T19:02:39Z'
  summary_source_hash: 6b08ed7a12b4f4ff6283dc5423ccd2f6a1fcca6535a3a2f67039a63d9623d457
  faq_generated_at: '2026-08-13T19:02:39Z'
  faq_source_hash: 6b08ed7a12b4f4ff6283dc5423ccd2f6a1fcca6535a3a2f67039a63d9623d457
  summary: >-
    You'll add Zephyr board support for the Arm Corstone-320 MPS4 FPGA platform on Linux. First,
    you'll prepare a Zephyr workspace, configure the Arm GNU Toolchain, and review the FPGA image
    documentation. Then, you'll create the device tree, Kconfig, and board metadata, build `hello_world`,
    and confirm its console output on the MPS4 board.
  faqs:
  - question: Which Corstone-320 FPGA image should I use with the MPS4 board?
    answer: >-
      Use the Arm Corstone SSE-320 FPGA Image for MPS4 (FI101). Follow
      the platform documentation to obtain and prepare the image.
  - question: Where can I find the output image after I build `hello_world`?
    answer: >-
      You'll find the ELF image at `build/zephyr/zephyr.elf`. Use this file to create the images
      that you load onto the MPS4 board.
  - question: Which option enables ROM-start relocation for the MPS4 FPGA build?
    answer: >-
      Add `-- -DCONFIG_ROMSTART_RELOCATION_ROM=y` to the `west build` command. This enables
      the ROM-start relocation configuration used for the Corstone-320 FPGA variant.
  - question: What output should I expect when the hello_world sample runs correctly?
    answer: >-
      The program prints `Hello World` to the console on the Arm Corstone-320 MPS4 board.
  - question: Which files do I copy to the MPS4 SD card?
    answer: >-
      Copy `vector.bin` and `app.bin` to the `\SOFTWARE\` folder. You'll create both files from
      `build/zephyr/zephyr.elf` with `arm-none-eabi-objcopy`.
# END generated_summary_faq

author: Sue Wu

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

skilllevels: Introductory
subjects: RTOS Fundamentals
armips:
  - Cortex-M
tools_software_languages:
  - Zephyr
  - GCC
  - C
operatingsystems:
  - Linux

further_reading:
  - resource:
      title: Zephyr Project documentation
      link: https://docs.zephyrproject.org/latest/index.html
      type: website
  - resource:
      title: Zephyr sample applications and demos
      link: https://docs.zephyrproject.org/latest/samples/index.html
      type: website
  - resource:
      title: Arm Corstone SSE-320 FPGA image for MPS4 (FI101)
      link: https://developer.arm.com/downloads/view/FI101
      type: website
  - resource:
      title: SSE-320 FPGA image for MPS4 application note
      link: https://developer.arm.com/documentation/109762/0100/?lang=en
      type: website
  - resource:
      title: Arm MPS4 FPGA prototyping board technical reference manual
      link: https://developer.arm.com/documentation/102577/latest/
      type: website

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

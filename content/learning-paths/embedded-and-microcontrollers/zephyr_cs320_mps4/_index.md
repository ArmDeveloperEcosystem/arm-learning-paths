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

author: Sue Wu

generate_summary_faq: true
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

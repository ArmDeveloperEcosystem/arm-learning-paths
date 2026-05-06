---
title: Design an AXI-Lite peripheral to control GPIOs

minutes_to_complete: 60

description: Learn how to design and integrate a custom AXI-Lite peripheral with a Cortex-A9 processor on the Zybo Z7-10 board using Vivado, configuring GPIOs to control LEDs based on switch inputs.

who_is_this_for: This is an introductory topic for software developers interested in System on Chip Design.

learning_objectives: 
    - Configure and integrate an AXI-Lite peripheral with a Cortex-A9 Processing System.
    - Program the Cortex-A9 processor to read the state of switches and control the LEDs using a C program.
    - Demonstrate a basic functional system that lights up the LEDs based on the status of the switches.  

prerequisites:
    - Some familiarity with Verilog
    - Basic understanding of System on Chip design
    - A 'Zybo Z7-10' development board 

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:54Z'
  generator: template
  source_hash: d8c48c293b2d316d5e68e18ab9e81157ad114a64cf2efa6951374a55d25238d6
  summary: >-
    Learn how to design and integrate a custom AXI-Lite peripheral with a Cortex-A9 processor
    on the Zybo Z7-10 board using Vivado, configuring GPIOs to control LEDs based on switch inputs.
    It is designed for software developers interested in System on Chip Design. By the end, you
    will be able to configure and integrate an AXI-Lite peripheral with a Cortex-A9 Processing
    System, program the Cortex-A9 processor to read the state of switches and control the LEDs
    using a C program, and demonstrate a basic functional system that lights up the LEDs based
    on the status of the switches. It focuses on tools and technologies such as C, Baremetal environments,
    and Arm platforms including Cortex-A. The main steps cover Setup a Workspace in Xilinx Vivado,
    Create a custom AXI4 Peripheral, Connect AXI4 Peripheral to ZYNQ Processing System, and Generate
    the bitstream and write your application using Vitis IDE.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will configure and integrate an AXI-Lite peripheral with a Cortex-A9 Processing System,
      program the Cortex-A9 processor to read the state of switches and control the LEDs using
      a C program, and demonstrate a basic functional system that lights up the LEDs based on
      the status of the switches. Learn how to design and integrate a custom AXI-Lite peripheral
      with a Cortex-A9 processor on the Zybo Z7-10 board using Vivado, configuring GPIOs to control
      LEDs based on switch inputs.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for software developers interested in System on Chip Design.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: Some familiarity with Verilog; Basic
      understanding of System on Chip design; A 'Zybo Z7-10' development board.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including C, Baremetal environments, and Arm platforms such
      as Cortex-A.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Setup a Workspace in Xilinx Vivado, Create a custom
      AXI4 Peripheral, Connect AXI4 Peripheral to ZYNQ Processing System, and Generate the bitstream
      and write your application using Vitis IDE.
# END generated_summary_faq

author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
operatingsystems:
    - Baremetal
tools_software_languages:
    - C

further_reading:
    - resource:
        title: Zybo Z7 10 Documentation
        link: https://digilent.com/shop/zybo-z7-zynq-7000-arm-fpga-soc-development-board/
        type: documentation

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
# ================================================================================

# Prereqs
---


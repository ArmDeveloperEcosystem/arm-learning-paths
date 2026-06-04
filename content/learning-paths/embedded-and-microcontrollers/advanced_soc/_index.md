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

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:57:22Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d8c48c293b2d316d5e68e18ab9e81157ad114a64cf2efa6951374a55d25238d6
  summary_generated_at: '2026-06-01T21:24:18Z'
  summary_source_hash: d8c48c293b2d316d5e68e18ab9e81157ad114a64cf2efa6951374a55d25238d6
  faq_generated_at: '2026-06-02T21:57:22Z'
  faq_source_hash: d8c48c293b2d316d5e68e18ab9e81157ad114a64cf2efa6951374a55d25238d6
  summary: >-
    This Learning Path guides you through designing and integrating a custom AXI-Lite peripheral
    with the Cortex-A9 Processing System on a Zybo Z7-10 board using Xilinx Vivado, then generating
    a bitstream and writing a bare-metal C application in Vitis to read board switches and drive
    LEDs. You will set up a Windows-based workspace, create and package a new AXI-Lite peripheral,
    connect GPIO-style ports to the Zynq PS, and build a simple end-to-end system that demonstrates
    LEDs reflecting switch states. This introductory path assumes some Verilog and basic SoC design
    knowledge and requires a Zybo Z7-10. Estimated time to complete is about 60 minutes.
  faqs:
  - question: What do I need before starting this Learning Path?
    answer: >-
      You need a Zybo Z7-10 development board, some familiarity with Verilog, and a basic understanding
      of System on Chip design. The flow targets a bare-metal application on a Cortex-A9.
  - question: What project setup should I use in Vivado?
    answer: >-
      Create a new RTL Project in Vivado. On Windows, place your workspace in a path without spaces
      (for example, C:/Workspace).
  - question: Which option should I use to create the custom AXI-Lite peripheral?
    answer: >-
      In Vivado, select Tools -> Create and Package New IP, then choose the option to create a
      new AXI4 peripheral. Provide a name for the IP and accept the default IP location if appropriate.
  - question: How do I expose LEDs and switches from the custom peripheral?
    answer: >-
      Create ports in the block design: an led output (4 bits) and an sw input, then connect them
      appropriately in the Vivado diagram. Ensure directions and widths match the intended board
      connections.
  - question: What steps complete the design and what should I expect when running the application?
    answer: >-
      Create the HDL Wrapper and generate the bitstream in Vivado, then use the Xilinx Vitis IDE
      to write and run a bare-metal C program on the Cortex-A9. The program reads the switch state
      and lights the LEDs based on the status of the switches.
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


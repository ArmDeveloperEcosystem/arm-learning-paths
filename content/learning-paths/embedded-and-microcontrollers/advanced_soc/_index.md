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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-08T15:18:26Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d8c48c293b2d316d5e68e18ab9e81157ad114a64cf2efa6951374a55d25238d6
  summary_generated_at: '2026-07-08T15:18:26Z'
  summary_source_hash: d8c48c293b2d316d5e68e18ab9e81157ad114a64cf2efa6951374a55d25238d6
  faq_generated_at: '2026-07-08T15:18:26Z'
  faq_source_hash: d8c48c293b2d316d5e68e18ab9e81157ad114a64cf2efa6951374a55d25238d6
  summary: >-
    You'll design and integrate a custom AXI4-Lite peripheral
    with the ZYNQ Processing System on a Zybo Z7-10 board. First, you'll create a clean Vivado workspace,
    then you'll follow the **Create and Package New IP** flow to build the peripheral, and add external ports for LEDs and
    switches with the shown bit widths. You'll create a block design that connects the peripheral to
    the Cortex-A9–based processing system, followed by generating an HDL wrapper and a bitstream.
    Using Vitis IDE, you'll write a bare-metal C program that reads switch inputs over AXI-Lite and drives LED outputs.
    You'll see LEDs responding to switch states through the custom IP.
  faqs:
  - question: What should I check about the Vivado workspace path before creating the project?
    answer: >-
      Use a path with no spaces. A simple top-level directory such as `C:/Workspace` avoids path
      issues.
  - question: Which option should I select in the **Create and Package New IP** wizard?
    answer: >-
      Select **Create a new AXI4 peripheral**. This generates the template files for an AXI-compliant
      custom IP block.
  - question: How do I know the led and sw ports are configured correctly?
    answer: >-
      Confirm led is an output and sw is an input, each with the width shown in the steps (four
      bits). They should appear as external ports in the block design and connect to your custom
      peripheral.
  - question: What should I do before generating the bitstream?
    answer: >-
      Create the HDL wrapper for `design1.bd` using the default options and save all changes. Then
      proceed to generate the bitstream.
  - question: What result should I expect when I run the C application in Vitis?
    answer: >-
      The LEDs change based on the state of the switches. Toggling a switch updates the corresponding
      LED as defined by your application.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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


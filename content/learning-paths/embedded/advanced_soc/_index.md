---
title: AXI-Lite and GPIOs

description: Design and implement AXI-Lite peripheral to control General Purpose Input and Output Ports (GPIOs). 

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for software developers interested in System on Chip Design.

learning_objectives: 
    - Configure and integrate an AXI-Lite peripheral with a Cortex-A9 Processing System.
    - Modify a C code to program the Cortex-A9 processor so that it reads the state of switches and control the LEDs.
    - Demonstrate a functional simple system that lights up the LEDs based on the status of the switches.  

prerequisites:
    - Some familiarity with Verilog
    - Basic understanding of System on Chip
    - Have a 'Zybo Z7-10' development board 

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
operatingsystems:
    - Windows
tools_software_languages:
    - Verilog
    - Xilinx Vivado
    - Xilinx Vitis

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
# ================================================================================

# Prereqs
---

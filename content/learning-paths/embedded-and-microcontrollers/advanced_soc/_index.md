---
title: Design an AXI-Lite peripheral to control GPIOs

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for software developers interested in System on Chip Design.

learning_objectives: 
    - Configure and integrate an AXI-Lite peripheral with a Cortex-A9 Processing System.
    - Program the Cortex-A9 processor to read the state of switches and control the LEDs using a C program.
    - Demonstrate a basic functional system that lights up the LEDs based on the status of the switches.  

prerequisites:
    - Some familiarity with Verilog
    - Basic understanding of System on Chip design
    - A 'Zybo Z7-10' development board 

author_primary: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
operatingsystems:
    - Baremetal
tools_software_languages:
    - FPGA

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
# ================================================================================

# Prereqs
---

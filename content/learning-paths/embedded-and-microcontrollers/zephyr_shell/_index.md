---
title: Create an interactive shell for Zephyr RTOS on Arm Cortex-M

description: Learn how to enable and configure the Zephyr shell subsystem on Arm Cortex-M, then build and run MQTT and UART shell backend examples using Workbench for Zephyr in Visual Studio Code.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for embedded developers who want to add an interactive command-line shell to a Zephyr RTOS application on Arm Cortex-M.

learning_objectives:
    - Enable and tailor Zephyr shell (Kconfig/prj.conf) to produce a minimal CLI footprint
    - Build and flash shell-enabled Zephyr apps using MQTT and UART shell backends on an Arm Cortex-M board
    - Use the Zephyr shell for board bring-up, diagnostics, and interactive testing

prerequisites:
    - Basic familiarity with embedded C programming
    - Visual Studio Code with the Workbench for Zephyr extension installed and configured
    - Docker Desktop, Docker Engine, or another Docker-compatible runtime installed on your host computer (for the MQTT shell example, if you're not installing Mosquitto on host)
    - A Zephyr-supported Arm Cortex-M board (for example, NXP FRDM-MCXN947)

author: 
    - Ayoub Bourjilat
    - Odin Shen
    - Akash Malik

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

skilllevels: Introductory
subjects: RTOS Fundamentals
armips:
    - Cortex-M
operatingsystems:
    - RTOS
tools_software_languages:
    - Zephyr
    - C

further_reading:
    - resource:
        title: Zephyr Project Documentation
        link: https://docs.zephyrproject.org/latest/index.html
        type: documentation
    - resource:
        title: Workbench for Zephyr Official Website
        link: https://z-workbench.com/
        type: website
    - resource:
        title: Zephyr Shell subsystem documentation
        link: https://docs.zephyrproject.org/latest/services/shell/index.html
        type: documentation
    - resource:
        title: AC6 Zephyr Training
        link: https://www.ac6-training.com/en/cours.php/cat_oRT/ref_oRT5/zephyr-rtos-programming
        type: website

# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

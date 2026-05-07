---
title: Build a Lightweight Shell on Cortex-M with Zephyr RTOS

minutes_to_complete: 30

who_is_this_for: This learning path is for embedded developers targeting Arm Cortex-M microcontrollers who want a small, configurable command-line shell (CLI) for bring-up, diagnostics, and interactive testing using Zephyr RTOS. You will use VS Code with the Workbench for Zephyr extension to build, flash, and debug on supported boards.

learning_objectives:
    - Enable and tailor Zephyr Shell (Kconfig/prj.conf) to produce a minimal CLI footprint
    - Build, flash, and debug the shell-enabled Zephyr app on an Arm Cortex-M board (UART/RTT logging, breakpoints)

prerequisites:
    - Basic familiarity with embedded C programming
    - Visual Studio Code with the Workbench for Zephyr extension installed and configured. Follow the [Build Zephyr projects with Workbench for Zephyr in VS Code](/learning-paths/embedded-and-microcontrollers/zephyr_vsworkbench/) Learning Path if you have not done this yet.
    - A Zephyr-supported Arm Cortex-M board (for example, NXP FRDM-MCXN947) 
    - Windows 10+ (64-bit), macOS with Homebrew, or Linux (preferably Ubuntu 20.04+)

author: 
    - Ayoub Bourjilat
    - Odin Shen

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
        title: AC6 Zephyr Training
        link: https://www.ac6-training.com/en/cours.php/cat_oRT/ref_oRT5/zephyr-rtos-programming
        type: website

# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

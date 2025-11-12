---
title: Run the Zephyr RTOS on Arm Corstone-300

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers getting started
  with the Zephyr RTOS.


learning_objectives:
- Build and run Zephyr applications on the Corstone-300

prerequisites:
- Some familiarity with embedded C programming
- A Linux machine running Ubuntu, or an AWS account to use [Arm Virtual Hardware](https://www.arm.com/products/development-tools/simulation/virtual-hardware)

author: Pareena Verma

test_images:
- amd64/ubuntu:latest
test_link: null
test_maintenance: false

### Tags
skilllevels: Introductory
subjects: RTOS Fundamentals
armips:
- Cortex-M
operatingsystems:
- RTOS
tools_software_languages:
- Zephyr
- Arm Virtual Hardware
- FVP

further_reading:
    - resource:
        title: Zephyr Project Documentation
        link: https://docs.zephyrproject.org/latest/index.html
        type: documentation
    - resource:
        title: Zephyr Sample applications and Demo
        link: https://docs.zephyrproject.org/latest/samples/index.html
        type: documentation
    - resource:
        title: List of Arm boards and platforms supported by Zephyr
        link: https://docs.zephyrproject.org/latest/boards/arm/index.html
        type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.

---
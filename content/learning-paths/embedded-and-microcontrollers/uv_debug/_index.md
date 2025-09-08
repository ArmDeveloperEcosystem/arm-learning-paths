---
title: "Start Debugging with µVision"
# Should start with a verb, have no adjectives (amazing, cool, etc.), and be as concise as possible.

minutes_to_complete: 90
# Always measured in minutes. Should be an integer, to complete the learning path (not just read it).

author: Christopher Seidl

who_is_this_for: >
    This is an advanced topic for software developers who want to debug microcontrollers using µVision.
# One sentence that should indicate exactly who the target audience is (developers in X industries using Y tools/software for Z use-case).

learning_objectives: 
    - Use basic run/stop debug
    - Learn advanced debug techniques using Event Recorder and Serial Wire Viewer
    - Learn to use ETM Trace for optimum performance
    - Measure your power consumption with ULINKplus
# 2-5 bullet points, one sentence each. Should start with a verb (Deploy, Measure) and indicate the value of the objective if possible.

prerequisites:
    - Some familiarity with embedded programming is assumed
    - An [Arm Account](https://developer.arm.com/register) is required
    - A Windows machine
    - Installation of [Arm Keil MDK](/install-guides/mdk/) with an active MDK-Community license
    - Installation of the [Corstone-300 Ecosystem FVP](/install-guides/fm_fvp/eco_fvp/)
# List any prereqs needed before this learning path can be completed. Can include:
    # Online service accounts                                   (An Amazon Web Services account)
    # Prior knowledge                                           (Some familiarity with embedded programming)
    # Previous learning paths                                   (The Learning Path: Getting Started with Arm Virtual Hardware)
    # Particular tools/environments already being initialized   (An EC2 instance with AVH installed)


##### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Cortex-M
operatingsystems:
    - RTOS
    - Baremetal
tools_software_languages:
<<<<<<< HEAD
    - Keil MDK
    - FVP
=======
    - Coding
    - Keil
    - Fixed Virtual Platform
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)



further_reading:
    - resource:
        title: Keil MDK
        link: https://developer.arm.com/Tools%20and%20Software/Keil%20MDK
        type: website
    - resource:
        title: µVision User's guide
        link: https://developer.arm.com/documentation/101407/latest
        type: documentation
    - resource:
        title: ULINKplus User's guide
        link: https://developer.arm.com/documentation/101636/latest
        type: documentation
    - resource:
        title: Arm CoreSight basics for Keil tools
        link: https://developer.arm.com/documentation/kan339/latest
        type: documentation
    - resource:
        title: List of supported boards
        link: https://keil.arm.com/boards
        type: website


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
# ================================================================================

# Prereqs
---


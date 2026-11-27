---
title: Run an industrial AI visual inspection application on Siemens Innexis ANA
minutes_to_complete: 30
who_is_this_for: Industrial AI developers building camera-based inspection applications and engineers testing workload functionality before Arm-based hardware is available.
learning_objectives:
    - Generate a conveyor video and use it as the Innexis virtual camera input.
    - Build the inspection application with CMake on an Arm Linux guest.
    - Deploy a pre-optimized vision-language model.
    - Verify a gear inspection result in a local browser.
prerequisites:
    - Complete the [introductory Innexis ANA Learning Path](https://github.com/odincodeshen/arm-learning-paths/tree/main/content/learning-paths/automotive/innexis_ana_zena).
    - Access to a Zena CSS virtual platform.
    - A host workstation with OpenSSH, a shell, and desktop browser.
author: 
    - Kieran Hejmadi
    - Pramod Mynampati
generate_summary_faq: true
rerun_summary: false
rerun_faqs: false
skilllevels: Advanced
subjects: AI/ML
armips:
    - Zena CSS
tools_software_languages:
    - Siemens Innexis ANA
    - llama.cpp
    - GStreamer
operatingsystems:
    - Linux
further_reading:
    - resource:
        title: Arm AI Portal
        link: https://developer.arm.com/ai
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

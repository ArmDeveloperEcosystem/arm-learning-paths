---
title: Run an industrial AI vision application on Siemens Innexis ANA
minutes_to_complete: 45
who_is_this_for: Industrial AI developers running camera-based inspection applications on virtual hardware.
learning_objectives:
    - Configure an Innexis virtual camera to play a sample conveyor recording.
    - Build llama.cpp from source on an Arm Linux guest.
    - Deploy a pre-optimized vision-language model and its matching projector.
    - Verify a gear inspection result in a local browser.
prerequisites:
    - Complete the [introductory Innexis ANA Learning Path](https://github.com/odincodeshen/arm-learning-paths/tree/main/content/learning-paths/automotive/innexis_ana_zena).
    - Access to a Zena CSS virtual platform with the Innexis camera-enabled Linux image, root SSH access, and outbound HTTPS to GitHub and Hugging Face.
    - A local development computer with Git, OpenSSH, a shell, and a web browser.
author: Kieran Hejmadi
generate_summary_faq: true
rerun_summary: false
rerun_faqs: false
skilllevels: Advanced
subjects: ML
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
        title: Siemens Innexis ANA user guide
        link: https://arm-262-g4-alb-1313921337.us-west-2.elb.amazonaws.com/docs/user-guide/overview/introduction.html
        type: documentation
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

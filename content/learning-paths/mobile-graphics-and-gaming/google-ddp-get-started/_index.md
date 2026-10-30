---
title: Use Google Developer Device Platform with an AI agent

draft: true
cascade:
    draft: true

description: Set up Google Developer Device Platform, verify CLI access, and direct an AI agent to explore Arm SVE2 and TinyStories performance on a remote Pixel phone.

minutes_to_complete: 45

who_is_this_for: Developers who want to access remote Android hardware through Google Cloud and direct a coding agent to inspect and use a real Arm-based phone.

learning_objectives:
    - Configure a Google Cloud project and local tools for Developer Device Platform
    - Verify CLI authentication, enabled services, and device catalog access
    - Use Google's agent skill to discover, reserve, inspect, and release a remote phone
    - Direct an on-phone TinyStories experiment with runtime feature checks and a measured performance report

prerequisites:
    - A development machine with a terminal and internet access
    - The [Google Cloud CLI](/install-guides/gcloud/) and permission to install its beta commands
    - A coding agent that supports Agent Skills and can run local commands and inspect screenshots, such as [Google Antigravity](/install-guides/antigravity/)

author: Annie Tallund

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

skilllevels: Introductory
subjects: ML
armips:
    - Arm C1
tools_software_languages:
    - Google Cloud
    - Agent Skills
    - Android
    - llama.cpp
operatingsystems:
    - Android

further_reading:
    - resource:
        title: Google Developer Device Platform overview
        link: https://docs.cloud.google.com/developer-device-platform/overview
        type: documentation
    - resource:
        title: Google Developer Device Platform quickstart
        link: https://docs.cloud.google.com/developer-device-platform/quickstart
        type: documentation
    - resource:
        title: Google's Developer Device Platform agent skill
        link: https://docs.cloud.google.com/developer-device-platform/agent-skill
        type: documentation
    - resource:
        title: llama.cpp build instructions and KleidiAI support
        link: https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md
        type: documentation
    - resource:
        title: Termux installation instructions
        link: https://github.com/termux/termux-app#installation
        type: documentation
### FIXED, DO NOT MODIFY
weight: 1
layout: learningpathall
learning_path_main_page: "yes"
---

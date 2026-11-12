---
title: Use Google Developer Device Platform with an AI agent

draft: true
cascade:
    draft: true

description: Use Google Developer Device Platform and an AI agent to compare TinyStories CPU inference with and without KleidiAI optimizations on a remote Pixel phone.

minutes_to_complete: 45

who_is_this_for: Developers who want to use a coding agent to access remote Android hardware and compare machine learning performance on an Arm-based phone.

learning_objectives:
    - Configure a Google Cloud project and local tools for Developer Device Platform (DDP).
    - Verify CLI authentication, enabled DDP services, and device catalog access.
    - Use Google's DDP agent skill with Antigravity to discover, reserve, inspect, and release a remote phone.
    - Use Antigravity to compare TinyStories CPU inference with and without KleidiAI optimizations.

prerequisites:
    - Access to a Google Cloud project with billing enabled and permissions to enable APIs and reserve Developer Device Platform devices
    - A local macOS or Ubuntu 26.04 computer with a desktop session and permission to install software
    - The [Google Cloud CLI](/install-guides/gcloud/) and permission to install beta commands
    - The [Antigravity CLI](/install-guides/antigravity/) coding agent

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
    - Antigravity
    - llama.cpp
    - KleidiAI
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

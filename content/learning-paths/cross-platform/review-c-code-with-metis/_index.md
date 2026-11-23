---
title: Review C code for security vulnerabilities with Arm Metis

description: Install Arm Metis, review vulnerable C code, and triage findings from a prepared libpng target.

minutes_to_complete: 45

who_is_this_for: This Learning Path is for developers who want to add AI-assisted security review to an existing code-review workflow. The code in the Learning Path is in C, but Metis is applicable to other languages as well.

learning_objectives:
    - Identify how Metis uses language-aware source analysis and model reasoning.
    - Install Metis and connect it to a supported model provider.
    - Review vulnerable C code, export JSON and SARIF reports, and inspect JSON findings.
    - Triage Metis findings against source code and a Magma-derived libpng diff.

prerequisites:
    - An Arm64 computer running macOS (Apple silicon) or Ubuntu or Debian Linux, or a Windows computer with an Ubuntu or Debian WSL2 environment
    - An API key and sufficient quota for a [Metis-supported model provider](https://github.com/arm/metis/blob/metis-v2.0.0/README.md#2-set-up-llm-provider)
    - Basic familiarity with C, Git, command-line tools, and security code-review procedures

author:
    - Matt Cossins
    - Michalis Spyrou
    - Michael Koslov

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Security
armips:
    - Neoverse
    - Cortex-A
operatingsystems:
    - Linux
    - macOS
    - Windows
tools_software_languages:
    - Arm Metis
    - C
    - Python
    - Git
    - JSON
    - SARIF

shared_path: true
shared_between:
    - laptops-and-desktops
    - servers-and-cloud-computing

further_reading:
    - resource:
        title: Arm Metis GitHub repository
        link: https://github.com/arm/metis
        type: website
    - resource:
        title: Empowering engineers with AI-enabled security code review
        link: https://developer.arm.com/community/arm-community-blogs/b/ai-blog/posts/empowering-engineers-with-ai-enabled-security-code-review
        type: blog
    - resource:
        title: Arm Metis brings agentic AI to software security
        link: https://newsroom.arm.com/blog/arm-metis-agentic-ai-security
        type: blog
    - resource:
        title: Magma ground-truth fuzzing benchmark
        link: https://hexhive.epfl.ch/magma/
        type: website
    - resource:
        title: Damn Vulnerable C Program repository
        link: https://github.com/hardik05/Damn_Vulnerable_C_Program
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

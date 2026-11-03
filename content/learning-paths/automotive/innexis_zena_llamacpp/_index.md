---
title: Run Local LLM Inference with llama.cpp on Arm Zena CSS
description: Build llama.cpp in a Zena CSS Linux guest, verify a text model, and run two recorded CPU inference requests.

minutes_to_complete: 60

who_is_this_for: AI and application developers who can access a Zena CSS virtual platform in Siemens Innexis ANA.

learning_objectives:
    - Check that the Zena CSS Linux guest has the tools and storage needed for a CPU AI workload.
    - Build and identify a fixed llama.cpp revision in the guest.
    - Verify the identity of one GGUF text model before using it.
    - Run two controlled inference requests and preserve their results.

prerequisites:
    - Access to a running Arm Zena CSS virtual platform and its EWAOL Linux guest in Siemens Innexis ANA.
    - A working guest console or authorized SSH connection, plus a way to transfer files to and from the guest.
    - Outbound HTTPS access from the guest to GitHub and Hugging Face for the tested download and build workflow.
    - Permission to obtain the selected llama.cpp source and text model.
    - Basic Linux command-line knowledge.

author: Odin Shen

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
armips:
    - Cortex-A
tools_software_languages:
    - Arm Zena CSS
    - Siemens Innexis ANA
    - llama.cpp
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Arm Zena Compute Subsystem
        link: https://www.arm.com/products/autonomous-machines/zena-compute-subsystems
        type: documentation
    - resource:
        title: llama.cpp
        link: https://github.com/ggml-org/llama.cpp
        type: documentation

### FIXED, DO NOT MODIFY
weight: 1
layout: learningpathall
learning_path_main_page: "yes"
---
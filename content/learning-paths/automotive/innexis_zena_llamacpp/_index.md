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

## Run local LLM inference on Zena CSS

You can use an [Arm Zena CSS virtual platform](https://www.arm.com/products/autonomous-machines/zena-compute-subsystems) to bring up an arm64 AI workload before physical hardware is available. In this Learning Path, you build a CPU-only [llama.cpp](https://github.com/ggml-org/llama.cpp) binary inside the Linux guest, verify one text model, run two prompts, and save the results.

The tested setup used [Siemens Innexis ANA](https://www.siemens.com/en-gb/products/ic/hav/innexis/architecture-native-acceleration/) 2026.02 on a g4 chamber with the supplied Zena CSS virtual platform and EWAOL v2.1.0 (`styhead`) Linux 6.6.54 image. The CPU and memory settings were unchanged: ANA showed **Simulation CPUs: 4**, while Linux reported **16 online CPUs** (`0-15`) and about 8 GB of guest memory. The ANA simulation setting is separate from the CPU count visible inside Linux.

The final result is a record of the guest environment, source and model identities, commands, generated text, and exit status. It shows that this workload can run in the selected virtual platform. It does not assess the quality of the answers or predict performance on a physical SoC.

The [Zena CSS onboarding Learning Path](../innexis_ana_zena/) establishes the virtual platform, Linux access, and file exchange used here. Complete that workflow first, or obtain an equivalent working guest from your chamber administrator. You do not need to deploy ANA or rebuild the Zena firmware for this exercise.

The commands on the following pages run inside the **Primary Compute Linux guest** unless a step says otherwise. Keep one guest shell open across the pages because it holds the paths you choose for the build, model, and result files.

---
title: Measure whether LLM token generation is memory-bound on Arm CPUs with llama-roofline

description: Use llama-roofline and llama-bench on a Raspberry Pi 5 or another Arm Linux system to measure the memory bandwidth ceiling, check how close llama.cpp decode runs to it, and pick decode and prefill thread counts from the results.

minutes_to_complete: 45

who_is_this_for: This is an advanced topic for developers and performance engineers who run llama.cpp on Arm CPUs, such as a Raspberry Pi 5 or another Arm Linux system, and want to know which setting actually changes their tokens per second.

learning_objectives:
    - Measure the sustained memory-read bandwidth of an Arm Linux system.
    - Determine whether llama.cpp token generation is memory-bound on your Arm CPU, and by how much, using llama-roofline.
    - Choose a decode thread count and a model size from measured data instead of defaults.
    - Explain why prompt processing and token generation need different thread counts.

prerequisites:
    - A Raspberry Pi 5 with 2 GB of RAM or more, running 64-bit Raspberry Pi OS with an active cooler, or another 64-bit Arm Linux system.
    - Python 3 with the venv module.
    - About 3.3 GB of free disk space for llama.cpp and three GGUF models.
    - Familiarity with building software with CMake on Linux.

author: Manu Nicholas Jacob

# New Learning Paths are opted in for the next manual generated summary/FAQ run.
# The generator resets this to false after a successful write.
generate_summary_faq: true

# Optional one-shot controls: set either field to true to regenerate just that
# generated section the next time the summary/FAQ tool runs. The tool resets
# them to false after a successful write.
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Neoverse
tools_software_languages:
    - llama.cpp
    - llama-roofline
    - Python
    - GCC
    - CMake
    - Hugging Face
    - Raspberry Pi
operatingsystems:
    - Linux
shared_path: true
shared_between:
    - embedded-and-microcontrollers
    - laptops-and-desktops
    - servers-and-cloud-computing

further_reading:
    - resource:
        title: llama-roofline source code and method
        link: https://github.com/manunicholasjacob/llama-roofline
        type: website
    - resource:
        title: llama.cpp llama-bench documentation
        link: https://github.com/ggml-org/llama.cpp/tree/master/tools/llama-bench
        type: documentation
    - resource:
        title: Roofline, an insightful visual performance model for multicore architectures
        link: https://doi.org/10.1145/1498765.1498785
        type: website
    - resource:
        title: Characterize the memory subsystem of an Arm Linux system using ASCT
        link: /learning-paths/servers-and-cloud-computing/memory-subsystem/
        type: website
    - resource:
        title: Profile llama.cpp performance with Arm Streamline and KleidiAI LLM kernels
        link: /learning-paths/servers-and-cloud-computing/llama_cpp_streamline/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

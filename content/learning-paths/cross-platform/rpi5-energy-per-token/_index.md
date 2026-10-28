---
title: Measure energy per token for llama.cpp on a Raspberry Pi 5 using the PMIC ADC

draft: true
cascade:
    draft: true

description: Use the Raspberry Pi 5 PMIC ADC and llama.cpp to measure joules per token, then compare energy efficiency across CPU clock caps and thread counts to find the most efficient inference settings.

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for developers who run llama.cpp on a Raspberry Pi 5 and want to measure the energy each generated token costs, and to choose a clock frequency and thread count from measured energy instead of speed alone.

learning_objectives:
    - Read current and voltage from each Raspberry Pi 5 power rail using vcgencmd pmic_read_adc, and interpret what the rail sum measures.
    - Log timestamped PMIC power samples to a CSV file and align them with the llama.cpp token-generation phase.
    - Compute joules per token from aligned power samples, with and without idle power subtracted.
    - Compare energy per token across CPU clock caps and thread counts to identify the most efficient inference settings.

prerequisites:
    - A Raspberry Pi 5 running 64-bit Raspberry Pi OS with an active cooler
    - About 1 GB of free disk space for llama.cpp and one GGUF model
    - Familiarity with building software with CMake and running Python scripts on Linux

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
tools_software_languages:
    - llama.cpp
    - Python
    - Raspberry Pi
operatingsystems:
    - Linux

### Cross-platform metadata only
shared_path: true
shared_between:
    - laptops-and-desktops
    - embedded-and-microcontrollers

further_reading:
    - resource:
        title: Raspberry Pi documentation for vcgencmd
        link: https://www.raspberrypi.com/documentation/computers/os.html#vcgencmd
        type: documentation
    - resource:
        title: llama.cpp llama-bench documentation
        link: https://github.com/ggml-org/llama.cpp/tree/master/tools/llama-bench
        type: documentation
    - resource:
        title: Linux kernel CPUFreq documentation
        link: https://docs.kernel.org/admin-guide/pm/cpufreq.html
        type: documentation
    - resource:
        title: Measure and compare performance per watt on an Arm Linux system
        link: /learning-paths/servers-and-cloud-computing/perf-per-watt/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

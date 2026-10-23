---
title: Measure llama.cpp energy per token on a Raspberry Pi 5 with the PMIC ADC

description: Read the Raspberry Pi 5 power management IC with vcgencmd, log rail power with time stamps, align it with llama.cpp token generation, and compare joules per token across CPU clock caps and thread counts.

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for developers who run llama.cpp on a Raspberry Pi 5 and want to measure the energy each generated token costs, and to choose a clock frequency and thread count from measured energy instead of speed alone.

learning_objectives:
    - Read the current and voltage of each Raspberry Pi 5 power rail with vcgencmd pmic_read_adc, and explain what the rail sum includes and leaves out.
    - Log rail power to a CSV file with a time stamp on every sample.
    - Compute joules per token for llama.cpp token generation from power samples aligned to the generation phase only, with and without the idle power.
    - Compare energy per token across CPU clock caps and thread counts, and measure how much the power sampler itself slows down the workload.

prerequisites:
    - A Raspberry Pi 5 running 64-bit Raspberry Pi OS with an active cooler.
    - About 1 GB of free disk space for llama.cpp and one GGUF model.
    - Python 3, which is installed with Raspberry Pi OS.
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
tools_software_languages:
    - llama.cpp
    - Python
    - Raspberry Pi
operatingsystems:
    - Linux

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

---
title: Measure llama.cpp energy per token on a Raspberry Pi 5

description: Use the Raspberry Pi 5 PMIC ADC and llama.cpp to measure joules per token, then compare energy efficiency across CPU clock caps and thread counts to find the most efficient inference settings.

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for developers who run llama.cpp on a Raspberry Pi 5 and want to measure the energy each generated token costs, and to choose a clock frequency and thread count from measured energy instead of speed alone.

learning_objectives:
    - Read current and voltage from each Raspberry Pi 5 power rail, and interpret what the rail sum measures.
    - Log timestamped power management integrated circuit (PMIC) power samples to a CSV file and align them with the llama.cpp token-generation phase.
    - Compute joules per token from aligned power samples, with and without idle power subtracted.
    - Compare energy per token across CPU clock caps and thread counts to identify the most efficient inference settings.

prerequisites:
    - A Raspberry Pi 5 running 64-bit Raspberry Pi OS with an active cooler
    - About 1 GB of free disk space for llama.cpp and one GGUF model
    - Familiarity with building software with CMake and running Python scripts on Linux

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-28T15:51:45Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 402e4009047e96efad7fd6cc707b2a79193d40f17b16f4b3857b92cf7be91abe
  summary_generated_at: '2026-10-28T15:51:45Z'
  summary_source_hash: 402e4009047e96efad7fd6cc707b2a79193d40f17b16f4b3857b92cf7be91abe
  faq_generated_at: '2026-10-28T15:51:45Z'
  faq_source_hash: 402e4009047e96efad7fd6cc707b2a79193d40f17b16f4b3857b92cf7be91abe
  summary: >-
    You'll measure llama.cpp energy per generated token on a Raspberry Pi 5 using its PMIC readings.
    First, you'll check the available power data and read the PMIC rails. You'll then log timestamped
    samples and align them with token-generation windows to calculate joules per token, with or
    without idle power. Finally, you'll compare clock caps and thread counts across repeated runs,
    accounting for variation and sampler overhead.
#   faqs:
#   - question: How do I check whether the Raspberry Pi 5 exposes power data through `hwmon`?
#     answer: >-
#       You can list the sensors under `/sys/class/hwmon/` and check for power or current files.
#       On the Raspberry Pi 5, you use `vcgencmd pmic_read_adc` to read current and voltage from the
#       onboard PMIC rails instead.
#   - question: What does the PMIC sampling script write?
#     answer: >-
#       You choose the output CSV path when you run `pmic_sampler.py`, for example `idle.csv` in
#       your working directory. In your CSV, each row contains `time_s`, `total_W`, and a watts column for
#       each rail with both current and voltage readings.
#   - question: How do I align power samples with token generation?
#     answer: >-
#       When you run `energy_per_token.py`, it starts the sampler before `llama-bench`. You can
#       trace each generation window from the script's timestamp for a `--progress` start marker
#       and the corresponding `samples_ns` duration; the script selects samples inside that window.
#   - question: How do I calculate joules per token with and without idle power?
#     answer: >-
#       You multiply the mean power during a generation window by its duration, then divide by
#       the generated token count for `J/token`. For `net_J/token`, you subtract the measured idle
#       baseline from the mean window power before multiplying and dividing.
#   - question: How should I compare clock caps and thread counts?
#     answer: >-
#       You set `scaling_max_freq` and check `scaling_cur_freq` during token generation to
#       confirm the cap. You then repeat the sweep at least five times, alternating the setting order.
#       You compare `J/token` and `net_J/token` separately, and avoid ranking settings whose
#       differences fall within run-to-run variation.
# END generated_summary_faq

author: Manu Nicholas Jacob

# New Learning Paths are opted in for the next manual generated summary/FAQ run.
# The generator resets this to false after a successful write.
generate_summary_faq: false

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

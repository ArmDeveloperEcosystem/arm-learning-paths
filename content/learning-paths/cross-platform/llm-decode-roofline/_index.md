---
title: Measure LLM decode bandwidth limits on Arm with llama-roofline


description: Use llama-roofline on Arm Linux to diagnose memory-bound llama.cpp token generation and choose thread counts and model size from measurements.

minutes_to_complete: 45

who_is_this_for: This topic helps developers and performance engineers choose llama.cpp settings from measured token throughput on Arm CPUs, using a Raspberry Pi 5 or another Arm Linux system.

learning_objectives:
    - Measure the sustained memory-read bandwidth of an Arm Linux system.
    - Determine whether llama.cpp token generation is memory-bound on your Arm CPU, and by how much, using llama-roofline.
    - Choose a decode thread count and a model size from measured data instead of defaults.
    - Identify why prompt processing and token generation need different thread counts.

prerequisites:
    - A 64-bit Arm Linux system, such as a Raspberry Pi 5 with 2 GB of RAM and an active cooler
    - Python 3 with the venv module
    - About 3.3 GB of free disk space for llama.cpp and three GGUF models
    - Familiarity with building software with CMake on Linux

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-29T16:23:18Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a4304fd508f4b7113d5fd1cacfa673ca687db9d92640b851f6cf123032edfb8f
  summary_generated_at: '2026-10-29T16:23:18Z'
  summary_source_hash: a4304fd508f4b7113d5fd1cacfa673ca687db9d92640b851f6cf123032edfb8f
  faq_generated_at: '2026-10-29T16:23:18Z'
  faq_source_hash: a4304fd508f4b7113d5fd1cacfa673ca687db9d92640b851f6cf123032edfb8f
  summary: >-
    You'll use llama-roofline with llama.cpp on Arm Linux to find out whether token generation is
    limited by memory bandwidth.  First, you'll check your CPU
    features, build llama-bench, and prepare the system and models. Then, you'll measure sustained
    read bandwidth and inspect how many bytes each model reads per token. Finally, you'll compare
    decode and prefill across thread counts. You'll diagnose memory limits, and choose a model size and
    thread settings.
#   faqs:
#   - question: How do I confirm my system is 64-bit Arm and see which CPU features are present?
#     answer: >-
#       Run `uname -m` and `grep -m1 Features /proc/cpuinfo`. Look for `aarch64` and flags such as
#       `asimd` (Neon) and `asimddp` (DotProd). llama.cpp detects DotProd at build time and uses it
#       for quantized kernels on the Cortex-A76.
#   - question: What should I check before measuring memory bandwidth?
#     answer: >-
#       Close other applications and ensure your system is idle. Use `uptime` and `free -m` to
#       confirm low load and that available memory exceeds the largest model file (1,066 MB).
#       Background load lowers measured bandwidth and distorts results that depend on it.
#   - question: How do I see how many bytes per token a model reads during decode?
#     answer: >-
#       Run `llama-roofline inspect` on the GGUF file. Check the `per token` line in its report to
#       see how many megabytes decode reads from the file for each token.
#   - question: How do I know whether decode is memory-bound after inspection and measurement?
#     answer: >-
#       Compare the bytes per token reported by `llama-roofline inspect` with the measured
#       bandwidth ceiling. If decode approaches that ceiling, memory bandwidth limits performance,
#       so adding threads might not help.
#   - question: What result should I expect from the `llama-bench` thread sweep, and how do I pick
#       a thread count?
#     answer: >-
#       Read the `llama-bench` table, which reports threads and tokens per second (`t/s`). Choose
#       the thread count with the highest `t/s` for your test. Decode can saturate quickly when
#       memory-bound, while prefill can benefit from more threads.
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

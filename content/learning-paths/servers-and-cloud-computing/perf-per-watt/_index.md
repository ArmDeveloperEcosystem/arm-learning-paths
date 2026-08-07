---
title: Measure and compare performance per watt on an Arm Linux system

description: Use Linux CPUFreq, hwmon, and OpenSSL to measure and compare how CPU governors and frequency limits affect throughput, SoC power, temperature, and energy efficiency on an Arm system.

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for software developers and performance engineers who want to measure and compare energy efficiency across CPU frequency configurations on Arm Linux systems.

learning_objectives:
    - Discover CPU frequency controls and power, temperature, and fan sensors on an Arm Linux system
    - Collect synchronized CPU frequency, power, temperature, and fan telemetry during a workload
    - Compare Linux CPUFreq governors and maximum-frequency limits using a repeatable OpenSSL workload
    - Calculate throughput per watt and energy consumed per unit of work

prerequisites:
    - An Arm Linux system with root or sudo access and Python 3 installed
    - CPU frequency policies available under `/sys/devices/system/cpu/cpufreq/`
    - CPU and I/O power sensors exposed through Linux hwmon

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-07T17:23:14Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: da3e266ba10841d9329bbc6ca8e0d2c2f4e96ff6232887643f0c84bf948f80d4
  summary_generated_at: '2026-08-07T17:23:14Z'
  summary_source_hash: da3e266ba10841d9329bbc6ca8e0d2c2f4e96ff6232887643f0c84bf948f80d4
  faq_generated_at: '2026-08-07T17:23:14Z'
  faq_source_hash: da3e266ba10841d9329bbc6ca8e0d2c2f4e96ff6232887643f0c84bf948f80d4
  summary: >-
    You'll measure and compare performance per watt on an Arm Linux system with CPUFreq controls,
    `hwmon` telemetry, and an OpenSSL SHA-256 workload. You'll inspect
    frequency policies and sensors, create a synchronized telemetry logger, and establish a baseline. Then, you'll
    compare governors and frequency caps, and calculate throughput per watt and energy per gigabyte.
  faqs:
  - question: How do I choose which hwmon power channels to include in SoC power?
    answer: >-
      Use the CPU and I/O power channels exposed by your platform's `hwmon` driver. On the example
      Thelio Astra, `apm_xgene` provides those channels. On another system, identify the equivalent
      labeled inputs before you run the logger. Treat the sum as an SoC estimate that excludes memory,
      storage, fans, and power-supply losses.
  - question: How do I verify CPUFreq policies before changing settings?
    answer: >-
      List the policy directories under `/sys/devices/system/cpu/cpufreq/` and compare their count
      with `nproc`. If the counts differ, your system might group multiple CPUs into one policy. Use
      this layout to understand which CPUs change together before you run experiments.
  - question: What do I need to edit in collect-telemetry.sh for my machine?
    answer: >-
      Replace `apm_xgene` and `system76_thelio_io` with the device names reported by
      `/sys/class/hwmon/hwmon*/name`, then update sensor labels if your drivers use different labels.
      The logger accepts an output filename and sampling interval as its first and second arguments.
  - question: How do I run the OpenSSL workload and know it exercised all CPUs?
    answer: >-
      Run `sudo ./run-openssl.sh LABEL SECONDS`. The script uses `openssl speed` with SHA-256, a
      fixed 16384-byte buffer, and `-multi "$(nproc)"` to start one worker per online CPU. Check
      the saved `openssl-output.txt` file for the aggregate throughput.
  - question: What should I check if changing a CPU governor fails?
    answer: >-
      Confirm that the requested governor appears in each policy's `scaling_available_governors`
      file. The `set-governor.sh` script validates this and exits if any policy lacks the governor.
      Check that `scaling_min_freq` and `scaling_max_freq` remain unchanged across runs.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - CPUFreq
    - cpupower
    - hwmon
    - OpenSSL
    - Python
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Linux CPU Performance Scaling
        link: https://docs.kernel.org/admin-guide/pm/cpufreq.html
        type: documentation
    - resource:
        title: Linux hwmon sysfs interface
        link: https://docs.kernel.org/hwmon/sysfs-interface.html
        type: documentation
    - resource:
        title: OpenSSL speed command
        link: https://docs.openssl.org/master/man1/openssl-speed/
        type: documentation
    - resource:
        title: First questions to answer when running on Ampere Altra
        link: https://amperecomputing.com/en/tutorials/the-first-10-questions-to-answer-while-running-on-ampere-altra-based-instances
        type: website
    - resource:
        title: Characterize the memory subsystem of an Arm Linux system using ASCT
        link: /learning-paths/servers-and-cloud-computing/memory-subsystem/
        type: learning-path

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: learningpathall
learning_path_main_page: "yes"
---

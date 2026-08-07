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

author: Jason Andrews

generate_summary_faq: true
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

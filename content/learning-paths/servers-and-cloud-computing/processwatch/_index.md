---
title: Run Process watch on your Arm machine

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for software developers who want to build and run the Process Watch tool on an Arm-based machine.
learning_objectives: 
    - Build and run the Process Watch tool on your Arm machine.
    - Describe how Process Watch works.
    - Check in real-time whether any workloads are using specific Arm instructions or features.

prerequisites:
    - An Arm-based system (bare metal server, cloud instance, or developer board) running Linux with kernel version 5.8.0 or later.
    - Root access, or the ability to run the sudo command.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:53:34Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ed85d6171f3c05bfdf1b396065fb0c73ce88724ff63fd1c3c8a93d4c27dd59f8
  summary_generated_at: '2026-06-02T04:49:56Z'
  summary_source_hash: ed85d6171f3c05bfdf1b396065fb0c73ce88724ff63fd1c3c8a93d4c27dd59f8
  faq_generated_at: '2026-06-03T01:53:34Z'
  faq_source_hash: ed85d6171f3c05bfdf1b396065fb0c73ce88724ff63fd1c3c8a93d4c27dd59f8
  summary: >-
    This Learning Path shows you how to build and run the Process Watch tool on an Arm-based Linux
    machine to monitor, in real time, whether workloads use specific Arm instructions and features.
    You will install required build dependencies (such as CMake, Clang/LLVM, and libelf), clone
    the Process Watch repository with submodules, and run the tool—preferably as root or by configuring
    capabilities and sysctl settings for non-root use. It explains how Process Watch samples retired
    instructions via Linux perf_events and a BPF program, and how to interpret output fields like
    PID, NAME, NEON, SVE, and SVE2. You will compile and run a simple C workload to observe instruction
    usage, including a no-optimization case. Prerequisites are an Arm-based Linux system (kernel
    5.8+), with root or sudo access.
  faqs:
  - question: What do I need before running the steps in this Learning Path?
    answer: >-
      Use an Arm-based system running Linux with kernel version 5.8.0 or later, and have root
      access or the ability to use sudo. No other prerequisites are explicitly listed.
  - question: Which packages should I install on Ubuntu 20.04 or later?
    answer: >-
      Run: sudo apt-get update, then sudo apt-get install libelf-dev cmake clang llvm llvm-dev
      -y. These provide CMake, Clang/LLVM, and libelf required to build Process Watch.
  - question: How should I clone the Process Watch repository to include all submodules?
    answer: >-
      Clone with submodules using: git clone --recursive https://github.com/intel/processwatch.git.
      The --recursive option ensures all submodules are fetched.
  - question: Should I run Process Watch as root, or can I enable it for non-root users?
    answer: >-
      Running as root is recommended. To allow a non-root user, run these as root: sudo setcap
      CAP_PERFMON,CAP_BPF=+ep ./processwatch, sudo sysctl -w kernel.perf_event_paranoid=-1, and
      sudo sysctl kernel.unprivileged_bpf_disabled=0.
  - question: How do I run Process Watch and interpret its output for NEON or SVE usage?
    answer: >-
      View options with: sudo ./processwatch -h, then run the tool and observe columns like FPARMv8,
      NEON, SVE, SVE2, %TOTAL, and TOTAL. Create and run the provided C workload with different
      optimization settings; the NEON and SVE columns indicate whether those instruction sets
      are being exercised.
# END generated_summary_faq

author: Graham Woodward

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Neoverse
tools_software_languages:
    - bpftool
    - libbpf
    - Capstone
    - C
    - CPP
    - Runbook

operatingsystems:
    - Linux


further_reading:
    - resource:
        title: Perf for Linux on Arm (LinuxPerf)
        link: /install-guides/perf/
        type: website
    - resource:
        title: Capstone 
        link: https://github.com/capstone-engine/capstone
        type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


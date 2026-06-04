---
title: Get started with WindowsPerf

description: Learn how to install WindowsPerf on Windows on Arm machines and generate sample performance reports for CPU profiling.

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for software developers working on laptops and desktops and new to the Arm architecture.

learning_objectives:
    - Install WindowsPerf on Windows on Arm machine
    - Generate a sample report

prerequisites:
    - Windows on Arm desktop or development machine

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:36:06Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 61a6390d42ce6bfc37a3bb981710dc23b8566070733f7979f9ec37bc63ab7d78
  summary_generated_at: '2026-06-02T02:36:31Z'
  summary_source_hash: 61a6390d42ce6bfc37a3bb981710dc23b8566070733f7979f9ec37bc63ab7d78
  faq_generated_at: '2026-06-02T23:36:06Z'
  faq_source_hash: 61a6390d42ce6bfc37a3bb981710dc23b8566070733f7979f9ec37bc63ab7d78
  summary: >-
    This introductory Learning Path shows how to install WindowsPerf on a Windows on Arm desktop
    or development machine and generate sample CPU profiling reports. You will use the wperf command-line
    interface to count ARM64 PMU events with wperf stat and to collect samples with wperf sample
    and wperf record, producing example outputs at function, basic block, or instruction granularity.
    The steps focus on practical, minimal commands and a cheat sheet to help you run counting
    and sampling quickly. By the end, you will have WindowsPerf installed and be able to execute
    basic profiling runs and view sample results. No additional prerequisites are explicitly listed
    beyond a Windows on Arm machine.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Windows on Arm desktop or development machine. No additional prerequisites are
      explicitly listed.
  - question: Which wperf command should I use for counting versus sampling?
    answer: >-
      Use wperf stat for counting occurrences of PMU events. Use wperf sample or wperf record
      for sampling to analyze where events occur in your code.
  - question: How do I limit a count to a specific core and time window?
    answer: >-
      The cheat sheet includes an example: wperf stat -e inst_spec,vfp_spec,ase_spec,ld_spec -c
      0 --timeout 3. This counts the listed events on core 0 for 3 seconds.
  - question: What result should I expect from counting and sampling runs?
    answer: >-
      Counting provides aggregate totals of selected PMU events. Sampling reports event frequencies
      attributed to program locations at the function, basic block, and/or instruction levels.
  - question: Where can I find example PMU events and metrics to try?
    answer: >-
      Refer to the WindowsPerf cheat sheet, which shows practical examples including events like
      inst_spec, vfp_spec, ase_spec, ld_spec and a metric example such as imix with an additional
      event.
# END generated_summary_faq

author: Ronan Synnott

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Neoverse
operatingsystems:
    - Windows
tools_software_languages:
    - WindowsPerf

further_reading:
    - resource:
        title: Announcing WindowsPerf Open-source performance analysis tool for Windows on Arm
        link: https://developer.arm.com/community/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/announcing-windowsperf
        type: blog
    - resource:
        title: WindowsPerf release 2.4.0 introduces the first stable version of sampling model support
        link: https://www.linaro.org/blog/windowsperf-release-2-4-0-introduces-the-first-stable-version-of-sampling-model-support/
        type: blog
    - resource:
        title: WindowsPerf Release 2.5.1
        link: https://www.linaro.org/blog/windowsperf-release-2-5-1/
        type: blog
    - resource:
        title: WindowsPerf Release 3.0.0
        link: https://www.linaro.org/blog/windowsperf-release-3-0-0/
        type: blog
    - resource:
        title: Windows on Arm overview
        link: https://learn.microsoft.com/en-us/windows/arm/overview
        type: website
    - resource:
        title: Linaro Windows on Arm project
        link: https://www.linaro.org/windows-on-arm/
        type: website
    - resource:
        title: WindowsPerf releases
        link: https://gitlab.com/Linaro/WindowsPerf/windowsperf/-/releases
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


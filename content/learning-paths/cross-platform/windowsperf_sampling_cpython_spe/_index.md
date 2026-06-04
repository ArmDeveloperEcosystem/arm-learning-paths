---
title: Sample Instructions with WindowsPerf and Arm SPE

minutes_to_complete: 30

description: Learn how to sample and profile CPU instructions using WindowsPerf with Arm Statistical Profiling Extension (SPE) on Windows on Arm, demonstrated with CPython workload analysis.

who_is_this_for: This is an introductory topic for developers who would like to learn about sampling CPU instructions with WindowsPerf and the Arm Statistical Profiling Extension (SPE).

learning_objectives:
    - Use WindowsPerf with a native Windows on Arm workload.
    - Describe the basic concepts of sampling with Arm SPE.
    - Explore the WindowsPerf command line.
    - Build CPython from sources for Windows on Arm (AArch64).

prerequisites:
    - A Windows on Arm desktop or development machine, with CPU support for SPE.
    - An installation of [WindowsPerf](/install-guides/wperf).
    - An installation of [Visual Studio](/install-guides/vs-woa/).
    - An installation of [Git](/install-guides/git-woa/).
  

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:55:45Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: bf887ef2481b51cf6c32e49e3eb1d5577346b7b9b1e4d6a604c559597b5306f0
  summary_generated_at: '2026-06-01T21:22:34Z'
  summary_source_hash: bf887ef2481b51cf6c32e49e3eb1d5577346b7b9b1e4d6a604c559597b5306f0
  faq_generated_at: '2026-06-02T21:55:45Z'
  faq_source_hash: bf887ef2481b51cf6c32e49e3eb1d5577346b7b9b1e4d6a604c559597b5306f0
  summary: >-
    This introductory path shows how to sample and profile CPU instructions on Windows on Arm
    using WindowsPerf with the Arm Statistical Profiling Extension (SPE), demonstrated on a CPython
    workload. You will install and use the SPE-enabled WindowsPerf build, verify that your Windows
    on Arm machine supports SPE, and build CPython from source for AArch64 with Visual Studio
    and Git. The steps pin the CPython debug binary to a specific core, run a large integer computation,
    and use WindowsPerf sampling and record commands to collect and explore SPE events (such as
    load events) from the workload. By the end, you will understand the basics of SPE sampling
    and have hands-on experience collecting instruction-level samples for a native Windows on
    Arm application.
  faqs:
  - question: What do I need before running the examples?
    answer: >-
      You need a Windows on Arm machine with CPU support for Arm SPE, WindowsPerf (driver and
      wperf CLI) installed, Visual Studio, and Git. These are explicitly listed in the Setup step.
  - question: How do I check if my Arm CPU supports SPE?
    answer: >-
      The Setup step includes guidance on verifying CPU support for Arm SPE. Follow that section
      before proceeding with sampling or recording.
  - question: Which WindowsPerf build should I use for SPE?
    answer: >-
      WindowsPerf release 3.8.0 includes a separate build with Arm SPE support located in the
      SPE/ subdirectory of the release assets. Use that build when following the SPE steps.
  - question: What workload is used to exercise CPython during sampling?
    answer: >-
      The path uses a debug-built CPython (python_d.exe) to compute 10**10**100, and pins the
      process to CPU core 1. The Windows start command is used to launch and pin the process as
      shown in the steps.
  - question: In the wperf record example, what does the “--” mean and what data is captured?
    answer: >-
      The double dash separates wperf options from the arguments passed to the profiled program
      (python_d.exe). The example records Arm SPE load events using arm_spe_0/ld=1/ on core 1
      for 5 seconds, producing a recording you can inspect.
# END generated_summary_faq

author: Przemyslaw Wirkus

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
    - Cortex-A
operatingsystems:
    - Windows
tools_software_languages:
    - WindowsPerf
    - Python
    - perf

## Cross-platform metadata only
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops

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
        title: WindowsPerf Release 3.3.0
        link: https://www.linaro.org/blog/windowsperf-release-3-3-0/
        type: blog
    - resource:
        title: WindowsPerf Release 3.7.2
        link: https://www.linaro.org/blog/expanding-profiling-capabilities-with-windowsperf-372-release
        type: blog
    - resource:
        title: "Introducing the WindowsPerf GUI: the Visual Studio 2022 extension"
        link: https://www.linaro.org/blog/introducing-the-windowsperf-gui-the-visual-studio-2022-extension
        type: blog
    - resource:
        title: "Introducing 1.0.0-beta release of WindowsPerf Visual Studio extension"
        link: https://www.linaro.org/blog/introducing-1-0-0-beta-release-of-windowsperf-visual-studio-extension
        type: blog
    - resource:
        title: "New Release: WindowsPerf Visual Studio Extension v1.0.0"
        link: https://www.linaro.org/blog/new-release-windowsperf-visual-studio-extension-v1000
        type: blog
    - resource:
        title: "Launching WindowsPerf Visual Studio Extension v2.1.0"
        link: https://www.linaro.org/blog/launching--windowsperf-visual-studio-extension-v210
        type: blog
    - resource:
        title: "Windows on Arm overview"
        link: https://learn.microsoft.com/en-us/windows/arm/overview
        type: website
    - resource:
        title: "Linaro Windows on Arm project"
        link: https://www.linaro.org/windows-on-arm/
        type: website
    - resource:
        title: "WindowsPerf releases"
        link: https://github.com/arm-developer-tools/windowsperf/releases
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


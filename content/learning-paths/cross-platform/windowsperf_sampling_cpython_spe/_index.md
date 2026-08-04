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
    - An installation of [WindowsPerf](/install-guides/wperf/).
    - An installation of [Visual Studio](/install-guides/vs-woa/).
    - An installation of [Git](/install-guides/git-woa/).

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-04T20:54:25Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 39be992807e2925699e242a6995fa2d782afaa32ce083e51399ac64066b8f0a4
  summary_generated_at: '2026-08-04T20:54:25Z'
  summary_source_hash: 39be992807e2925699e242a6995fa2d782afaa32ce083e51399ac64066b8f0a4
  faq_generated_at: '2026-08-04T20:54:25Z'
  faq_source_hash: 39be992807e2925699e242a6995fa2d782afaa32ce083e51399ac64066b8f0a4
  summary: >-
    This Learning Path shows you how to sample and profile CPU instructions on Windows on Arm using
    WindowsPerf with the Arm Statistical Profiling Extension (SPE). You build a debug CPython for
    AArch64, pin the Python process to a specific core, and run a compute-heavy expression to
    generate activity. You use `wperf sample` with an SPE event while the process is pinned, then
    use `wperf record` to spawn the workload and capture events. You also select the SPE-enabled
    WindowsPerf build and review samples with annotation and disassembly.
  faqs:
  - question: Which WindowsPerf build should I use to profile with Arm SPE?
    answer: >-
      Use the SPE-enabled build included in WindowsPerf release 3.8.0. Download the release asset
      and select the WindowsPerf build in the `SPE/` subdirectory.
  - question: Do I need a debug build of CPython for this path?
    answer: >-
      Yes. The examples use `python_d.exe`, which you build from CPython sources in debug mode for
      Windows on Arm (AArch64).
  - question: How do I pass Python arguments without wperf parsing them?
    answer: >-
      Use `--` to separate `wperf` options from the arguments passed to `python_d.exe`. Everything
      after `--` is forwarded to the Python process.
  - question: Why pin the CPython process to one CPU core, and which core is used?
    answer: >-
      Pinning keeps the workload on a known CPU so collected samples map to that core consistently.
      The steps pin the process to core 1.
  - question: What result should I expect after running wperf record with an SPE event?
    answer: >-
      WindowsPerf records SPE load events for the run. Use the `--annotate` and `--disassemble`
      options to review where sampled instructions map to source code and assembly.
# END generated_summary_faq

author: Przemyslaw Wirkus

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

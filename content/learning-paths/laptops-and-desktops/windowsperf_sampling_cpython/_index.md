---
title: Sampling CPython with WindowsPerf

description: Learn how to use WindowsPerf for performance sampling on Windows on Arm, build CPython from sources, and analyze native workload performance.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers keen to understand sampling and who are new to the Arm architecture.

learning_objectives:
    - Use WindowsPerf with native Windows on Arm workload
    - Understand the basics of sampling
    - Explore the WindowsPerf command line
    - Build CPython from sources for Windows on Arm ARM64 target

prerequisites:
    - Windows on Arm desktop or development machine with [WindowsPerf installed](/install-guides/wperf)
    - Windows x86_64 desktop machine with [Visual Studio 2022 Community Edition](https://visualstudio.microsoft.com/vs/) installed.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:37:32Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e23de84e7e05d771072ab799f5cc802476fd5e3c23da41a202c9c50fe9980e25
  summary_generated_at: '2026-06-02T02:37:39Z'
  summary_source_hash: e23de84e7e05d771072ab799f5cc802476fd5e3c23da41a202c9c50fe9980e25
  faq_generated_at: '2026-06-02T23:37:32Z'
  faq_source_hash: e23de84e7e05d771072ab799f5cc802476fd5e3c23da41a202c9c50fe9980e25
  summary: >-
    This Learning Path shows how to use WindowsPerf to sample a native Windows on Arm workload
    by building CPython from sources for the ARM64 target and analyzing its runtime. You will
    create a debug build, run CPython interactively, pin python_d.exe to a selected core, and
    collect both counting and sampling data to locate hot code paths using PMU event frequencies.
    The path also shows how to streamline the workflow with the WindowsPerf record command to
    spawn and pin the process and forward arguments. Prerequisites include a Windows on Arm machine
    with WindowsPerf installed and a Windows x86_64 desktop with Visual Studio 2022 Community
    Edition. After completing, you will understand basic sampling and the WindowsPerf command
    line for this scenario.
  faqs:
  - question: What do I need before running the examples?
    answer: >-
      You need a Windows on Arm desktop or development machine with WindowsPerf installed, and
      a Windows x86_64 desktop with Visual Studio 2022 Community Edition installed. The sampling
      examples are run on a native ARM64 Windows on Arm machine.
  - question: Which CPython build should I use during the sampling exercises?
    answer: >-
      Use the debug build of CPython targeting ARM64 that you built from sources in the previous
      step. The examples reference these pre-built ARM64 debug binaries.
  - question: Which WindowsPerf command should I use to spawn and pin CPython to a core?
    answer: >-
      Use the record command with the -c option to pin to a specific core. You can specify the
      process with --pe_file or place the process to spawn at the end of the wperf command.
  - question: How do I pass command-line arguments to my program when using WindowsPerf?
    answer: >-
      Place all application arguments after the WindowsPerf options. They are passed verbatim
      to the spawned program.
  - question: What result should I expect when I run counting and sampling on the Googolplex workload?
    answer: >-
      Counting provides aggregate event counts, while sampling reports frequencies of PMU events.
      Together they help you see hot locations in the CPython runtime image under the chosen workload.
# END generated_summary_faq

author: Przemyslaw Wirkus

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
operatingsystems:
    - Windows
tools_software_languages:
    - WindowsPerf
    - Python
    - perf

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


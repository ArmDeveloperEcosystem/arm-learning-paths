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
    - Windows on Arm desktop or development machine with [WindowsPerf installed](/install-guides/wperf/)
    - Windows x86_64 desktop machine with [Visual Studio 2022 Community Edition](https://visualstudio.microsoft.com/vs/) installed.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-11T16:27:41Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f20e21b475671828f98ca275e54e3f3b35b717bf40d17e67756ae42184071b9d
  summary_generated_at: '2026-08-11T16:27:41Z'
  summary_source_hash: f20e21b475671828f98ca275e54e3f3b35b717bf40d17e67756ae42184071b9d
  faq_generated_at: '2026-08-11T16:27:41Z'
  faq_source_hash: f20e21b475671828f98ca275e54e3f3b35b717bf40d17e67756ae42184071b9d
  summary: >-
    You'll build a debug CPython for the ARM64 Windows on Arm target, then use WindowsPerf to measure
    a Python workload. First, you'll pin the
    CPython interpreter (`python_d.exe`) to a single core, run both counting and sampling, and examine
    event frequencies to locate hot locations in the CPython runtime image. Then, you'll use the
    `record` command to spawn the interpreter, select the core with `-c`, and pass arguments directly,
    reducing setup steps. By the end, you'll be able to run repeatable measurements and recognize output
    that differentiates aggregate counts from sampled hot locations.
  faqs:
  - question: What result should I expect from counting versus sampling?
    answer: >-
      Counting returns aggregate totals for the selected events across the run. Sampling reports
      event frequencies tied to locations in the CPython runtime image so you can see where activity
      is concentrated.
  - question: Which CPU core should I pin `python_d.exe` to?
    answer: >-
      Any single core is acceptable; choose one and use it consistently across runs. Pinning reduces
      variability and makes results easier to compare.
  - question: How do I launch CPython with WindowsPerf without starting it first?
    answer: >-
      Use the `record` command to spawn the process and pin it with the `-c` option. Specify the target
      either with `--pe_file` or by appending the `python_d.exe` command at the end of the WindowsPerf
      invocation.
  - question: How do I pass arguments to CPython when using the record command?
    answer: >-
      Place all application arguments after the WindowsPerf options. WindowsPerf forwards them
      verbatim to the spawned program.
  - question: What should I look for after running the Googolplex calculation?
    answer: >-
      Expect a sustained workload that exercises integer computation in CPython. Sampling output
      should attribute activity to hot locations in the CPython runtime image; if you see only
      totals, you ran counting instead of sampling.
# END generated_summary_faq

author: Przemyslaw Wirkus

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

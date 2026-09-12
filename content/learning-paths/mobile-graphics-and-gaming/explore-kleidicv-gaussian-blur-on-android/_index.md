---
title: Compare KleidiCV Gaussian blur performance across Neon, SVE2, and SME on Android
description: Build a KleidiCV Gaussian blur benchmark for Android and evaluate how Neon, SVE2, and SME performance changes with image resolution and kernel size.

minutes_to_complete: 45

who_is_this_for: This is an advanced topic for C and C++ developers who want to evaluate SIMD image-processing implementations on an Arm-based Android device.

learning_objectives:
    - Build KleidiCV Gaussian blur examples with the Android NDK.
    - Run a minimal SME Gaussian blur example on an Android device.
    - Explore the performance of Neon, SVE2, and SME implementations with controlled CPU affinity.
    - Interpret how kernel size and image resolution affect SME speedup.

prerequisites:
    - A Ubuntu or Debian x86_64 Linux development machine with Git, CMake, Python 3, and Android Debug Bridge (`adb`) installed
    - A 64-bit Arm Android device with SVE2 and SME support
    - Basic familiarity with C++, CMake, and `adb`

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-10T20:09:50Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e8606fd9d582feb919c169d0257d525e6392759ddc4e23092dadf2b2b1384e20
  summary_generated_at: '2026-09-10T20:09:50Z'
  summary_source_hash: e8606fd9d582feb919c169d0257d525e6392759ddc4e23092dadf2b2b1384e20
  faq_generated_at: '2026-09-10T20:09:50Z'
  faq_source_hash: e8606fd9d582feb919c169d0257d525e6392759ddc4e23092dadf2b2b1384e20
  summary: >-
    You'll set up an Android NDK environment, build a KleidiCV SME Gaussian blur example, and run it
    on a compatible 64-bit Arm Android device. Next, you'll confirm its output, add and build a
    performance explorer, and use it to compare Neon, SVE2, and SME. Finally, you'll run controlled
    tests with fixed CPU affinity, compare p50 latency, and see how image resolution and kernel
    size affect SME speedup.
  faqs:
  - question: How do I know the SME Gaussian blur example ran correctly on the device?
    answer: >-
      After the filter runs, compare the printed pixel values with the documented sample. The 20
      output rows are identical. Each row has its highest value, `40`, at column 10. The `15x15`
      kernel spreads the original line from columns 3 through 17.
  - question: Where should I push and run the performance explorer binary?
    answer: >-
      Push `build/extract-android-benchmark/gaussian_blur_benchmark` to `/data/local/tmp/`, set it
      executable, and run `/data/local/tmp/gaussian_blur_benchmark` with `adb shell`.
  - question: How do I bind the benchmark to a specific CPU on the device?
    answer: >-
      Run `adb shell` with `taskset <mask>` before the binary path. On the test device, the masks
      `1`, `10`, and `80` select CPUs 0, 4, and 7. Replace them with masks appropriate for your
      device.
  - question: Which option sets the Gaussian kernel size and how many iterations get measured?
    answer: >-
      Use `--kernel` to select `3`, `5`, `7`, `9`, or `15`. Use `--iterations` to set the
      measurement count. The comparison loop uses `--iterations 3000`, and the explorer completes
      `100` warm-up calls before timing.
  - question: What should I look for in the benchmark output to confirm correctness before comparing
      performance?
    answer: >-
      Review the CSV output only after the explorer completes without an `output differs from NEON
      reference` error. It compares SVE2 and SME output byte-for-byte with its Neon reference
      after warm-up and before timing each backend.
# END generated_summary_faq

author: Jett Zhou

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Cortex-X
operatingsystems:
    - Android
tools_software_languages:
    - ADB
    - C
    - CPP
    - CMake
    - Android NDK
    - Neon
    - SVE2
    - SME

further_reading:
    - resource:
        title: Android NDK guides
        link: https://developer.android.com/ndk/guides
        type: documentation
    - resource:
        title: KleidiCV
        link: https://gitlab.arm.com/kleidi/kleidicv
        type: documentation
    - resource:
        title: Arm Scalable Vector Extension
        link: https://support.arm.com/documentation/102340/latest/
        type: documentation
    - resource:
        title: Arm Scalable Matrix Extension
        link: https://support.arm.com/documentation/110636/latest/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

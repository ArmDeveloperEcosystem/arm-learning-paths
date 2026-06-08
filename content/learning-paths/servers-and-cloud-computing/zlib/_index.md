---
title: Improve data compression performance on Arm servers with zlib-ng

description: Learn how to build and use zlib-ng on Arm servers, using its Neon SIMD and ARMv8 CRC32 optimizations to improve compression performance compared to the system default zlib.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers who want to improve data compression performance on Arm servers by replacing the default zlib with zlib-ng, an actively maintained fork that includes Neon SIMD and ARMv8 CRC32 optimizations.

learning_objectives:
- Build zlib-ng in zlib-compatible mode on an Arm server
- Run example applications using zlib-ng as a drop-in replacement
- Measure and analyze performance improvements with zlib-ng

prerequisites:
- An Arm Linux computer or an [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider running Ubuntu 22.04 or Ubuntu 24.04.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:18:20Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 8916f83f621505dc5406f14e70d04e702ea304950e34b4b76dc1bbc987bcc4e3
  summary_generated_at: '2026-06-02T05:27:47Z'
  summary_source_hash: 8916f83f621505dc5406f14e70d04e702ea304950e34b4b76dc1bbc987bcc4e3
  faq_generated_at: '2026-06-03T02:18:20Z'
  faq_source_hash: 8916f83f621505dc5406f14e70d04e702ea304950e34b4b76dc1bbc987bcc4e3
  summary: >-
    Build and use zlib-ng on an Arm Linux server to take advantage of Neon SIMD and ARMv8 CRC32
    enhancements for compression-heavy workloads. You will compile zlib-ng in zlib-compatible
    mode, run example applications as a drop-in replacement for the system zlib, and compare a
    Python file-compression workload before and after switching to zlib-ng. The path also shows
    how to install and use Linux perf to analyze where time is spent, including enabling access
    to PMU registers and kernel symbols. Prerequisite: an Arm Linux computer or Arm-based cloud
    instance running Ubuntu 22.04 or 24.04; no other explicit prerequisites are listed.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      Use an Arm Linux computer or an Arm-based cloud instance running Ubuntu 22.04 or Ubuntu
      24.04. The steps use sudo to install packages and adjust perf settings.
  - question: Which zlib-ng build mode should I use for a drop-in replacement?
    answer: >-
      Build zlib-ng in zlib-compatible mode. This enables the zlib API so existing applications
      can use zlib-ng without source changes.
  - question: What result should I expect after running the Python compression example?
    answer: >-
      You will compress a large file with Python and measure the time difference when using zlib-ng
      versus the system zlib. The outcome is a measured performance comparison rather than a specific
      numeric target.
  - question: Which packages are installed during this Learning Path?
    answer: >-
      The steps install python-is-python3 for running Python and the perf tooling via linux-tools-common,
      linux-tools-generic, and linux-tools-uname -r. These enable running the example and analyzing
      performance.
  - question: What should I check if perf reports permission or access errors?
    answer: >-
      Follow the steps that allow user access to PMU registers and kernel symbol addresses using
      the provided sudo commands. After applying those settings, rerun perf to collect data.
# END generated_summary_faq

author: Pareena Verma

test_images:
- ubuntu:latest
test_link:
test_maintenance: true

### Tags
armips:
- Neoverse
skilllevels: Introductory
subjects: Libraries
operatingsystems:
- Linux
tools_software_languages:
- zlib

further_reading:
    - resource:
        title: zlib-ng on GitHub
        link: https://github.com/zlib-ng/zlib-ng
        type: documentation
    - resource:
        title: Improving zlib-cloudflare and comparing performance with other zlib forks
        link: https://aws.amazon.com/blogs/opensource/improving-zlib-cloudflare-and-comparing-performance-with-other-zlib-forks/
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


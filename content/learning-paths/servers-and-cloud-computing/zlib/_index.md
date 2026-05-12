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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:59Z'
  generator: template
  source_hash: 8916f83f621505dc5406f14e70d04e702ea304950e34b4b76dc1bbc987bcc4e3
  summary: >-
    Learn how to build and use zlib-ng on Arm servers, using its Neon SIMD and ARMv8 CRC32 optimizations
    to improve compression performance compared to the system default zlib. It is designed for
    software developers who want to improve data compression performance on Arm servers by replacing
    the default zlib with zlib-ng, an actively maintained fork that includes Neon SIMD and ARMv8
    CRC32 optimizations. By the end, you will be able to build zlib-ng in zlib-compatible mode
    on an Arm server, run example applications using zlib-ng as a drop-in replacement, and measure
    and analyze performance improvements with zlib-ng. It focuses on tools and technologies such
    as zlib, Linux environments, and Arm platforms including Neoverse. The main steps cover Build
    and install zlib-ng on Arm servers, Improve Python application performance using zlib-ng,
    and Use perf to analyze zlib-ng performance.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will build zlib-ng in zlib-compatible mode on an Arm server, run example applications
      using zlib-ng as a drop-in replacement, and measure and analyze performance improvements
      with zlib-ng. Learn how to build and use zlib-ng on Arm servers, using its Neon SIMD and
      ARMv8 CRC32 optimizations to improve compression performance compared to the system default
      zlib.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for software developers who want to improve data compression
      performance on Arm servers by replacing the default zlib with zlib-ng, an actively maintained
      fork that includes Neon SIMD and ARMv8 CRC32 optimizations.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An Arm Linux computer or an [Arm based
      instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider
      running Ubuntu 22.04 or Ubuntu 24.04.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including zlib, Linux environments, and Arm platforms such
      as Neoverse.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Build and install zlib-ng on Arm servers, Improve
      Python application performance using zlib-ng, and Use perf to analyze zlib-ng performance.
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


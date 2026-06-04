---
title: Run x265 (H.265 codec) on Arm servers
description: Learn how to build and run the x265 H.265 codec on Arm servers with performance benchmarking across various video resolutions and encoding presets.

minutes_to_complete: 10

who_is_this_for: This is an introductory topic for software developers who want to
  build and run an x265 codec on Arm servers and measure performance.


learning_objectives:
- Build x265 codec on Arm server
- Run x265 codec on Arm server with the same video of various resolutions and encoding
  presets to measure the performance impact

prerequisites:
- An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from an appropriate
  cloud service provider. This Learning Path has been verified on AWS EC2 and Oracle cloud services, running `Ubuntu Linux 20.04.`

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:36:00Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 908a750f2a891a0c4c9d1183c2130ac5ac0fdcfb4a45185cef6ed6da47c9aaa9
  summary_generated_at: '2026-06-02T03:26:25Z'
  summary_source_hash: 908a750f2a891a0c4c9d1183c2130ac5ac0fdcfb4a45185cef6ed6da47c9aaa9
  faq_generated_at: '2026-06-03T00:36:00Z'
  faq_source_hash: 908a750f2a891a0c4c9d1183c2130ac5ac0fdcfb4a45185cef6ed6da47c9aaa9
  summary: >-
    Build and run the x265 H.265 encoder on Arm servers and benchmark its performance across different
    video resolutions and encoding presets. You will use an Arm-based cloud instance—verified
    on AWS EC2 and Oracle Cloud Services—running Ubuntu Linux 20.04, install GCC, CMake, and required
    packages, then compile x265 and execute the same video under varied configurations to observe
    performance impact. The open-source libx265 includes optimizations for Arm Neoverse with Neon,
    and optimized code is available on Bitbucket. This introductory path focuses on practical
    build-and-run steps so you finish with a working x265 on Arm and comparative measurements.
    Estimated time to complete is about 10 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      An Arm-based instance from a cloud service provider. This Learning Path has been verified
      on AWS EC2 and Oracle Cloud, running Ubuntu Linux 20.04.
  - question: Which packages should I install to build x265 on Ubuntu?
    answer: >-
      Update apt and install wget, git, cmake, cmake-curses-gui, and build-essential. You also
      need GCC for your Arm Linux distribution.
  - question: Where do the Arm optimizations for x265 come from?
    answer: >-
      The path uses the open-source libx265, which includes optimizations for Arm Neoverse platforms
      with Neon support. The optimized code is available on Bitbucket.
  - question: How will I measure the performance impact of different settings?
    answer: >-
      You will run x265 on the same video using various resolutions and encoding presets. Compare
      the results to assess the performance impact of those choices.
  - question: Which operating systems and platforms are validated for these steps?
    answer: >-
      The steps target Linux and have been verified on Ubuntu 20.04 running on Arm-based servers
      from AWS EC2 and Oracle Cloud. Other operating systems are not explicitly listed.
# END generated_summary_faq

author: Pareena Verma

test_images:
- ubuntu:latest
test_link: null
test_maintenance: true

### Tags
skilllevels: Introductory
subjects: Libraries
cloud_service_providers:
  - AWS
  - Oracle
armips:
- Neoverse
tools_software_languages:
- x265
operatingsystems:
- Linux

further_reading:
    - resource:
        title: x265 Documentation
        link: https://x265.readthedocs.io/en/master/
        type: documentation
    - resource:
        title: Ampere Altra Max Delivers Sustainable High-Resolution H.265 Encoding
        link: https://developer.arm.com/community/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/ampere-altra-max-delivers-sustainable-high-resolution-h-265-video-encoding-without-compromise
        type: blog
    - resource:
        title: Optimized Video Encoding with FFmpeg on AWS Graviton Processors
        link: https://aws.amazon.com/blogs/opensource/optimized-video-encoding-with-ffmpeg-on-aws-graviton-processors/
        type: blog
    - resource:
        title: OCI Ampere A1 Compute instances can significantly reduce video encoding costs versus modern CPUs
        link: https://developer.arm.com/community/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/oracle-cloud-infrastructure-arm-based-a1
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


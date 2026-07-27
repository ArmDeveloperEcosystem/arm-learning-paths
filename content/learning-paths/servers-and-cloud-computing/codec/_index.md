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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-27T18:42:45Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 908a750f2a891a0c4c9d1183c2130ac5ac0fdcfb4a45185cef6ed6da47c9aaa9
  summary_generated_at: '2026-07-27T18:42:45Z'
  summary_source_hash: 908a750f2a891a0c4c9d1183c2130ac5ac0fdcfb4a45185cef6ed6da47c9aaa9
  faq_generated_at: '2026-07-27T18:42:45Z'
  faq_source_hash: 908a750f2a891a0c4c9d1183c2130ac5ac0fdcfb4a45185cef6ed6da47c9aaa9
  summary: >-
    You'll build the open-source x265 (HEVC) encoder on an Arm server and run it on sample videos.
    You'll install GCC, CMake, and supporting packages, obtain the referenced Arm-optimized libx265
    source with Neoverse Neon support, and compile it. You'll then run repeatable tests while varying
    the resolution and encoder preset to compare encoding behavior on Arm.
  faqs:
  - question: Which x265 source should I use to get Arm-specific optimizations?
    answer: >-
      Use the `libx265` repository referenced in the steps on Bitbucket, which includes Arm Neoverse
      Neon support. Follow the clone or checkout instructions provided in the path to ensure you
      build the optimized tree.
  - question: What should I verify after installing the required packages?
    answer: >-
      Confirm the package installation completes without errors and that the listed tools are
      available on your system. Then proceed to the configure and build steps as shown in the
      path.
  - question: How should I structure the benchmarking across resolutions and presets?
    answer: >-
      Keep the input video constant and vary only the resolution and the encoder preset between
      runs. Use the same process for each run so results are comparable.
  - question: How do I know the build used Arm NEON optimizations?
    answer: >-
      Build the Bitbucket-based source referenced in the steps on an Arm server to enable the
      NEON-supported paths. If configuration targets a non-Arm platform, recheck that you're
      building on the intended Arm instance.
  - question: What result should I expect when an encoding run finishes?
    answer: >-
      The encoder should complete and produce output consistent with the chosen resolution and preset.
      Record the run’s output information so you can compare it with other configurations.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

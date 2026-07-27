---
title: Run the AV1 and VP9 codecs on Arm Linux
description: Learn how to build and run the AV1 and VP9 video codecs on Arm Linux systems with performance benchmarking across various resolutions and encoding configurations.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-27T18:43:40Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: c0643a788cdb0b3e33fe645fbb61d99a1899806e3ee197541c1eb8134b2876c1
  summary_generated_at: '2026-07-27T18:43:40Z'
  summary_source_hash: c0643a788cdb0b3e33fe645fbb61d99a1899806e3ee197541c1eb8134b2876c1
  faq_generated_at: '2026-07-27T18:43:40Z'
  faq_source_hash: c0643a788cdb0b3e33fe645fbb61d99a1899806e3ee197541c1eb8134b2876c1
  summary: >-
    You'll build the AV1 and VP9 reference codecs from source on Arm Linux and run them on sample
    videos. You'll compile libxaom and libvpx with common development tools, then vary resolution
    and encoding settings to compare runs. The workflow covers Arm Neoverse optimizations that use
    Neon and SVE2 and supports basic performance benchmarking.
  faqs:
  - question: Which source repositories should I use for AV1 and VP9?
    answer: >-
      For AV1, use the `libxaom` reference implementation with Arm-optimized code available on
      Google Git. For VP9, use the `libvpx` repository from the Chromium WebM project as shown in
      the steps.
  - question: Do I need to pass special flags to enable Neon or SVE2 optimizations?
    answer: >-
      The implementations include optimizations for Arm Neoverse that use Neon and SVE2. The path
      does not list extra flags to set; follow the build steps on an Arm Linux system and proceed
      to run and benchmark.
  - question: What should I expect after a successful build?
    answer: >-
      A successful build produces libraries and codec executables that run on your Arm Linux system.
      Confirm you can encode or decode the example videos without errors before moving on to benchmarking.
  - question: How should I choose resolutions and settings for benchmarking?
    answer: >-
      Use example videos and vary resolution and encoding parameters to create comparable test
      runs. Keep inputs consistent across runs and record the command lines so you can repeat
      and compare results.
  - question: What should I check if the build fails early?
    answer: >-
      Verify that required development tools, including CMake and the GNU compiler, are available.
      Ensure you can access the referenced repositories and that you are building on an Arm Linux
      system.
# END generated_summary_faq

author: Odin Shen

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers who want to
  build and run the VP9 and AV1 codecs on Arm servers and measure performance.

learning_objectives:
- Build the AV1 and VP9 codecs on Arm Linux.
- Run the AV1 and VP9 codecs on Arm Linux using example videos with various resolutions and encodings.

armips:
- Neoverse
- Cortex-A

prerequisites:
- An Arm Linux system or an [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a 
  cloud service provider. 

operatingsystems:
    - Linux

skilllevels: Introductory
subjects: Libraries

test_images:
- ubuntu:latest
test_link: null
test_maintenance: false

tools_software_languages:

further_reading:
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

weight: 1
layout: learningpathall
learning_path_main_page: "yes"
---

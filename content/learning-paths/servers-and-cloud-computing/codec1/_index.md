---
title: Run the AV1 and VP9 codecs on Arm Linux
description: Learn how to build and run the AV1 and VP9 video codecs on Arm Linux systems with performance benchmarking across various resolutions and encoding configurations.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:36:28Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: c0643a788cdb0b3e33fe645fbb61d99a1899806e3ee197541c1eb8134b2876c1
  summary_generated_at: '2026-06-02T03:27:16Z'
  summary_source_hash: c0643a788cdb0b3e33fe645fbb61d99a1899806e3ee197541c1eb8134b2876c1
  faq_generated_at: '2026-06-03T00:36:28Z'
  faq_source_hash: c0643a788cdb0b3e33fe645fbb61d99a1899806e3ee197541c1eb8134b2876c1
  summary: >-
    Learn how to build and run the AV1 (libaom) and VP9 (libvpx) video codecs on Arm Linux, then
    benchmark them on example videos using multiple resolutions and encoding configurations. You
    will install build dependencies such as CMake and the GNU compiler, obtain the codec sources,
    compile on an Arm server or Arm-based cloud instance, and execute encoding and decoding workloads.
    The reference implementations include Arm-focused optimizations, including use of Neon and
    SVE2 on Arm Neoverse platforms. By the end, you will be able to run these codecs on your Arm
    system and record performance results. No further prerequisites are listed beyond access to
    an Arm Linux environment.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need access to an Arm Linux system or an Arm-based instance from a cloud service provider.
      No other explicit prerequisites are listed.
  - question: Which codecs and libraries are used in this path?
    answer: >-
      AV1 is built and run using the libxaom reference implementation, and VP9 is built and run
      using libvpx. Both libraries support encoding and decoding.
  - question: Which development tools do I need to install to build the codecs?
    answer: >-
      You need various development tools including CMake and the GNU compiler. The steps provide
      installation instructions for the required packages.
  - question: Where do I obtain the source code for the codecs?
    answer: >-
      For VP9, the path clones libvpx from https://chromium.googlesource.com/webm/libvpx. For
      AV1, the reference implementation and Arm-optimized code for libxaom are available on Google
      Git.
  - question: What results should I expect after completing the path?
    answer: >-
      You will have built the AV1 and VP9 codecs on Arm Linux and run them on example videos at
      various resolutions and encodings. You will also collect performance measurements to compare
      configurations, with notes on Arm Neoverse optimizations using Neon and SVE2.
# END generated_summary_faq

author: Odin Shen

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


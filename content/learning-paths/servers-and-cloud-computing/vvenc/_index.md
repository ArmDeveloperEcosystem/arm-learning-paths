---
title: Run the vvenc H.266 encoder on Arm servers

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:16:42Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 4ed20056b2d82bd2c9ab1afe3d74657df9ac09808592d843c1b143626a8668ac
  summary_generated_at: '2026-06-02T05:26:21Z'
  summary_source_hash: 4ed20056b2d82bd2c9ab1afe3d74657df9ac09808592d843c1b143626a8668ac
  faq_generated_at: '2026-06-03T02:16:42Z'
  faq_source_hash: 4ed20056b2d82bd2c9ab1afe3d74657df9ac09808592d843c1b143626a8668ac
  summary: >-
    Learn how to build and run the open-source VVenC (vvenc) H.266/VVC encoder on Arm-based Linux
    servers to encode a real 1080p video and measure performance. This introductory path targets
    Arm Neoverse platforms and highlights available optimizations in vvenc for Neon and SVE/SVE2,
    with optimized code in the project’s GitHub repository. You will build the vvenc project and
    run an encode on an Arm server to gather performance measurements. Prerequisites are an Arm
    Linux system or an Arm-based cloud instance; the path was tested on an Arm Neoverse N2-based
    Alibaba Cloud ECS instance (g8y) running Ubuntu 22.04. Estimated completion time is about
    20 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an Arm Linux system or an Arm-based instance from a cloud service provider. This
      Learning Path has been tested on a Neoverse N2-based Alibaba Cloud ECS (g8y) running Ubuntu
      22.04. No other prerequisites are explicitly listed.
  - question: Which cloud platforms can I use for the Arm instance?
    answer: >-
      The path lists AWS, Microsoft Azure, Google Cloud, and Oracle as cloud service providers.
      It was tested on an Alibaba Cloud ECS instance with a Neoverse N2 CPU and Ubuntu 22.04.
  - question: Where do I get the encoder source and which tool will I run?
    answer: >-
      The optimized code for Arm Neoverse platforms is available in the vvenc GitHub repository.
      You will build the project and run the vvenc encoder to process a real 1080p video.
  - question: Do I need Neon or SVE/SVE2 to follow this path?
    answer: >-
      The encoder includes optimizations for Arm Neoverse that use Neon and SVE/SVE2 instructions.
      The path does not list specific instruction-set requirements as prerequisites.
  - question: What result should I expect after running vvenc on a 1080p video?
    answer: >-
      You should complete an encode of a real 1080p video and gather performance measurements
      as directed. The steps focus on building vvenc, running the encoder, and measuring performance
      on the Arm server.
# END generated_summary_faq

author: Willen Yang

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for software developers who want to build and run the VVenC® (Fraunhofer Versatile Video Encoder) H.266 project on Arm servers and measure the performance.

learning_objectives:
- Build the VVenC® H.266 encoder project on an Arm-based server.
- Run vvenc on an Arm-based server to encode a real 1080p video file and measure the performance.

armips:
- Neoverse

prerequisites:
- An Arm Linux system or an [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider. This Learning Path has been tested on an Arm Neoverse N2-based Alibaba cloud ECS instance(g8y), running Ubuntu 22.04.

operatingsystems:
    - Linux

skilllevels: Introductory
subjects: Libraries
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle

tools_software_languages:
- vvenc

further_reading:
    - resource:
        title: vvenc Documentation
        link: https://github.com/fraunhoferhhi/vvenc/wiki/Usage
        type: documentation
    - resource:
        title: Delivering the best H.265 video experience on Arm Neoverse N2 Platform
        link: https://developer.arm.com/community/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/h265-video-on-neoverse-n2
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


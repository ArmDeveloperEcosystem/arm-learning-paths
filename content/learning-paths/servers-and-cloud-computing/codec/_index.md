---
armips:
- Neoverse
author: Pareena Verma
layout: learningpathall
learning_objectives:
- Build x265 codec on Arm server
- Run x265 codec on Arm server with the same video of various resolutions and encoding
  presets to measure the performance impact
learning_path_main_page: 'yes'
minutes_to_complete: 10
operatingsystems:
- Linux
prerequisites:
- An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from an appropriate
  cloud service provider. This Learning Path has been verified on AWS EC2 and Oracle cloud services, running `Ubuntu Linux 20.04.`
skilllevels: Introductory
subjects: Libraries
test_images:
- ubuntu:latest
test_link: null
test_maintenance: true
test_status:
- passed
title: Run x265 (H.265 codec) on Arm servers
tools_software_languages:
- x265
further_reading:
    - resource:
        title: x265 Documentation
        link: https://x265.readthedocs.io/en/master/
        type: documentation
    - resource:
        title: Ampere Altra Max Delivers Sustainable High-Resolution H.265 Encoding
        link: https://community.arm.com/arm-community-blogs/b/infrastructure-solutions-blog/posts/ampere-altra-max-delivers-sustainable-high-resolution-h-265-video-encoding-without-compromise
        type: blog
    - resource:
        title: Optimized Video Encoding with FFmpeg on AWS Graviton Processors
        link: https://aws.amazon.com/blogs/opensource/optimized-video-encoding-with-ffmpeg-on-aws-graviton-processors/
        type: blog
    - resource:
        title: OCI Ampere A1 Compute instances can significantly reduce video encoding costs versus modern CPUs
        link: https://community.arm.com/arm-community-blogs/b/operating-systems-blog/posts/oracle-cloud-infrastructure-arm-based-a1
        type: blog


weight: 1
who_is_this_for: This is an introductory topic for software developers who want to
  build and run an x265 codec on Arm servers and measure performance.
---

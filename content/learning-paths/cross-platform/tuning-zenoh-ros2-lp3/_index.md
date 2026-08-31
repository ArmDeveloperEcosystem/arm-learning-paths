---
title: Tune Zenoh for ROS 2 traffic over wireless networks

minutes_to_complete: 120

description: Measure ROS 2 sensor traffic, tune Zenoh with compression, access control, downsampling, and QoS, and select a suitable wireless deployment policy.

who_is_this_for: This Learning Path is for robotics developers who want to understand how Zenoh manages ROS 2 sensor traffic over Wi-Fi. You should already have basic experience setting up and distributing a ROS 2 Jazzy system with rmw_zenoh, as covered in the previous Learning Paths in this series.

learning_objectives:
    - Measure the rate, bandwidth, and regularity of ROS 2 sensor data at a remote receiver
    - Reproduce a constrained wireless link with Linux traffic control
    - Configure Zenoh compression, access control, downsampling, and quality of service policies
    - Validate the policies over real Wi-Fi and select a suitable deployment configuration

prerequisites:
    - The ROS 2 simulation environment from [Build a ROS 2 and Zenoh simulation environment on an Arm server](/learning-paths/cross-platform/ros2-zenoh-arm/), with the `robot` and `control` containers available
    - The distributed Zenoh configuration from [Distribute a ROS 2 robotic system across Arm devices with Zenoh](/learning-paths/cross-platform/distributed-ros2-zenoh-lp2/), with the `control` container connected in client mode
    - An **Arm server** with the Docker Compose configuration used in Learning Paths 1 and 2
    - A **Raspberry Pi** connected over Wi-Fi
    - Familiarity with ROS 2 topics, Docker, and basic Linux commands

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-31T16:20:42Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: fceb2d9bb41f1efe4abf9c5c797503597be212dbf55059b06506247a9f1990c3
  summary_generated_at: '2026-08-31T16:20:42Z'
  summary_source_hash: fceb2d9bb41f1efe4abf9c5c797503597be212dbf55059b06506247a9f1990c3
  faq_generated_at: '2026-08-31T16:20:42Z'
  faq_source_hash: fceb2d9bb41f1efe4abf9c5c797503597be212dbf55059b06506247a9f1990c3
  summary: >-
    You measure ROS 2 sensor traffic, emulate a constrained wireless link, and tune Zenoh policies
    to manage ROS 2 traffic over Wi-Fi. You first record baseline rates for `/scan`,
    `/camera/image_raw`, and `/camera/points`. You then apply `tc` and `netem`, test compression,
    access control, downsampling, and QoS, and compare the results. Finally, you repeat the policy
    tests with a Raspberry Pi over real Wi-Fi and choose a deployment policy.
  faqs:
  - question: How do I start and verify the ROS 2 and Zenoh environment before measuring?
    answer: >-
      From the Arm server host, run `docker compose up -d` in `~/ros_zenoh`, then use `docker compose
      ps`. Both services should report `Up` before you proceed.
  - question: Where do I run the network emulation command?
    answer: >-
      Open a terminal in the `robot` container desktop and run `source ~/workshop_env.bash`, followed
      by `just network_limit`. You apply the `tc`/`netem` limits from within the container environment
      used for the experiments.
  - question: How do I know the emulated wireless limits are active?
    answer: >-
      `just network_limit` prints the applied parameters, including rate, latency variation, loss,
      and reordering. Look for output that states the simulation is applied with values such as a
      `25mbit` rate and nonzero latency and loss.
  - question: Which ROS 2 topics should I target first when the link is constrained?
    answer: >-
      The `/camera/image_raw` and `/camera/points` streams dominate bandwidth, while `/scan` is
      small. Prioritize compression or access control for the camera and point-cloud streams.
  - question: If I only need remote monitoring, which Zenoh settings should I use?
    answer: >-
      Use compression for the camera stream. If you do not need point-cloud data, use access control
      to block it; if you need complete point-cloud frames, use compression with the QoS `block_first`
      policy.
# END generated_summary_faq

author:
    - Kwashie Andoh
    - Odin Shen
    - Habib Ogunbanwo

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Neoverse
tools_software_languages:
    - ROS 2
    - rmw_zenoh
    - Zenoh
    - Docker
    - Linux traffic control
operatingsystems:
    - Linux

### Cross-platform metadata only
shared_path: true
shared_between:
    - automotive
    - embedded-and-microcontrollers

further_reading:
    - resource:
        title: Build a ROS 2 and Zenoh simulation environment on an Arm server
        link: /learning-paths/cross-platform/ros2-zenoh-arm/
        type: documentation
    - resource:
        title: Distribute a ROS 2 robotic system across Arm devices with Zenoh
        link: /learning-paths/cross-platform/distributed-ros2-zenoh-lp2/
        type: documentation
    - resource:
        title: ROS 2 middleware implementation for Eclipse Zenoh
        link: https://github.com/ros2/rmw_zenoh
        type: documentation
    - resource:
        title: Eclipse Zenoh documentation
        link: https://zenoh.io/docs/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

---
title: Build and deploy multi-node Zenoh systems on Raspberry Pi

minutes_to_complete: 45

description: Learn how to build and deploy distributed Zenoh systems on Arm devices like Raspberry Pi, using pub/sub, storage, and queryable models for scalable robotics and IoT applications.

who_is_this_for: This Learning Path is for robotics developers, industrial automation engineers, and IoT system architects who are building distributed, scalable, and low-latency applications. Whether you're using the Robot Operating System (ROS), developing autonomous systems, or designing multi-node communication frameworks, you can use Eclipse Zenoh on Arm-based platforms, both in the cloud and on local devices like Raspberry Pi.

learning_objectives: 
    - Understand Zenoh's architecture and how it integrates pub/sub, storage, querying, and computation models
    - Build and run Zenoh examples on both Arm servers and Raspberry Pi
    - Set up and deploy a multi-node Zenoh system

prerequisites:
    - At least two local Cortex-A devices running Linux, such as Raspberry Pi 4 or Pi 5. You can also use Arm servers or cloud instances
    - Experience with ROS 2 applications

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-04T20:55:36Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d196e9204523c1aea84c1e6a60060a83480ec929edc31b1b50cca43b2e305739
  summary_generated_at: '2026-08-04T20:55:36Z'
  summary_source_hash: d196e9204523c1aea84c1e6a60060a83480ec929edc31b1b50cca43b2e305739
  faq_generated_at: '2026-08-04T20:55:36Z'
  faq_source_hash: d196e9204523c1aea84c1e6a60060a83480ec929edc31b1b50cca43b2e305739
  summary: >-
    This Learning Path guides you through building and deploying Eclipse Zenoh on Arm-based Linux
    devices, including Raspberry Pi, to create a multi-node communication system for robotics and
    IoT. You build Zenoh from source, then distribute it across multiple devices by copying release
    binaries or using Docker for consistent multi-node testing. You explore three communication
    patterns: real-time publish/subscribe messaging, in-memory storage and queries, and a queryable
    node that computes results on demand. You validate cross-device messaging and retrieve published
    values through queries.
  faqs:
  - question: How do I know my Zenoh build is ready to deploy to other devices?
    answer: >-
      After building, check for compiled binaries under `~/zenoh/target/release`. If the Zenoh
      examples run locally, you can copy the release binaries to your other Arm devices.
  - question: Which files do I need to copy when deploying binaries to additional Raspberry Pi
      boards?
    answer: >-
      Copy the compiled Zenoh binaries from `~/zenoh/target/release` to each target device. Keep
      the files together so you can run the same examples across all nodes.
  - question: What result should I expect when I run the pub/sub example on two devices?
    answer: >-
      The subscriber should receive updates for keys that match the `demo/example/**` expression.
      When the publisher sends messages under matching keys, the subscriber observes those updates
      in real time over the local network.
  - question: Should I run Zenoh directly on the host or use Docker for multi-node tests?
    answer: >-
      Both approaches are supported. Run the release binaries directly on each device, or use Docker
      to distribute Zenoh and provide a consistent multi-node test environment.
  - question: What should I check if a z_get query returns no data in the storage example?
    answer: >-
      Confirm that the Zenoh daemon is running and that `z_put` and `z_get` use the same key. This
      example uses in-memory storage, so only values published after the daemon starts are available
      to query.
# END generated_summary_faq

author: 
    - Odin Shen
    - William Liang
    - ChenYing Kuo

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
    - C
    - Raspberry Pi
    - Zenoh
    - Rust

operatingsystems:
    - Linux
### Cross-platform metadata only
shared_path: true
shared_between:
    - automotive

further_reading:
    - resource:
        title: Eclipse Zenoh Website
        link: https://zenoh.io/
        type: documentation
    - resource:
        title: Eclipse Zenoh Github
        link: https://github.com/eclipse-zenoh/zenoh
        type: documentation
    - resource:
        title: Zenoh and ROS 2 Integration Guide
        link: https://github.com/eclipse-zenoh/zenoh-plugin-ros2dds
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

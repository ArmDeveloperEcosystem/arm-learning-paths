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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:56:40Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a56dce27c6a846bcf35b6e9505142f1445b22ff71530f1189700049d7b14e994
  summary_generated_at: '2026-06-01T21:23:51Z'
  summary_source_hash: a56dce27c6a846bcf35b6e9505142f1445b22ff71530f1189700049d7b14e994
  faq_generated_at: '2026-06-02T21:56:40Z'
  faq_source_hash: a56dce27c6a846bcf35b6e9505142f1445b22ff71530f1189700049d7b14e994
  summary: >-
    Learn to build and deploy a distributed Eclipse Zenoh system on Arm Linux devices, including
    Raspberry Pi 4/5 and Arm servers or cloud instances. You will install the Rust-based Zenoh
    stack, build core examples, and run a two-node publish/subscribe test, then add in-memory
    storage and querying using a Zenoh daemon with z_put and z_get. The path also shows how to
    containerize Zenoh with Docker to streamline multi-node distribution and repeatable testing.
    Prerequisites include at least two Cortex-A devices running Linux and experience with ROS
    2 applications. By the end, you can stand up and validate a basic multi-node Zenoh deployment
    on Arm.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need at least two local Cortex-A devices running Linux, such as Raspberry Pi 4 or 5.
      You can also use Arm servers or cloud instances. Experience with ROS 2 applications is expected.
  - question: Do I have to use Docker to deploy across multiple devices?
    answer: >-
      No. You can copy the compiled binaries from ~/zenoh/target/release/ to each device. The
      path also shows how to containerize with Docker for streamlined and consistent multi-node
      testing.
  - question: How do I know the Zenoh build on Raspberry Pi completed correctly?
    answer: >-
      After building Zenoh and its core examples, you should see release binaries under ~/zenoh/target/release/.
      You will use these binaries in the deployment and example steps to confirm they run on your
      devices.
  - question: What network setup and topics are used in the pub/sub example?
    answer: >-
      Run the example across two devices on the same local network. The subscriber listens on
      the key expression demo/example/**, and you should see it receive messages published under
      that prefix.
  - question: How do I validate the storage and query example is working?
    answer: >-
      Start the Zenoh daemon with in-memory storage, publish values with z_put, and retrieve them
      with z_get. Being able to query previously published data—even after the publisher is offline—confirms
      the storage engine is functioning.
# END generated_summary_faq

author: 
    - Odin Shen
    - William Liang
    - ChenYing Kuo

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


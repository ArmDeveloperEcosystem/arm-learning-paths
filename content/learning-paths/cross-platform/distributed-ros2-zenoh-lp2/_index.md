---
title: Distribute a ROS 2 robotic system across Arm devices with Zenoh

minutes_to_complete: 60

description: Learn how to use rmw_zenoh to extend a containerized ROS 2 robotic simulation from an Arm server to a remote control environment and a Raspberry Pi.

who_is_this_for: This Learning Path is for robotics developers who want to distribute an existing ROS 2 system across Arm-based cloud and edge devices. It is intended for learners who have completed the preceding Learning Path, or already have an equivalent ROS 2 Jazzy simulation running with rmw_zenoh and Docker.

learning_objectives:
    - Explain how Zenoh router and client modes support ROS 2 communication across containers and physical devices
    - Configure a remote control container to connect to a ROS 2 simulation through rmw_zenoh
    - Connect a Raspberry Pi to the Zenoh router running on an Arm server
    - Verify ROS 2 sensor data and messages flowing in both directions between the server and Raspberry Pi

prerequisites:
    - Complete the [Build a ROS 2 and Zenoh simulation environment on an Arm server](/learning-paths/cross-platform/ros2-zenoh-arm/) learning path, with the `robot` container running the Zenoh router and ROX simulation
    - A Raspberry Pi 4 or Raspberry Pi 5 (16 GB SD card or larger), aarch64, on the same network as the server
    - Familiarity with ROS 2 topics, Docker, and basic Linux command-line operations

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-31T16:18:50Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e57d5914984dfe1275e9c9b22f373ae45646cc168eca88ebfe369f6eba6b421d
  summary_generated_at: '2026-08-31T16:18:50Z'
  summary_source_hash: e57d5914984dfe1275e9c9b22f373ae45646cc168eca88ebfe369f6eba6b421d
  faq_generated_at: '2026-08-31T16:18:50Z'
  faq_source_hash: e57d5914984dfe1275e9c9b22f373ae45646cc168eca88ebfe369f6eba6b421d
  summary: >-
    You extend a single-server ROS 2 system across an Arm server, a control container, and a
    Raspberry Pi. You first understand Zenoh router and client roles, then configure the control
    container and verify remote RViz communication. Next, you connect a 64-bit Raspberry Pi, start
    its edge container, and verify graph discovery, sensor data, and bidirectional messages. You
    finish by comparing ROS namespaces, `ROS_DOMAIN_ID`, and Zenoh namespaces for separating
    multiple robots.
  faqs:
  - question: Which Zenoh roles do the server, control container, and Raspberry Pi use?
    answer: >-
      You use the Zenoh router in the `robot` container on the Arm server. You use a Zenoh client
      session in the `control` container and another on the Raspberry Pi; both connect to that
      router.
  - question: How do I get the control container ID before configuring its Zenoh client session?
    answer: >-
      Run `docker ps` on the Arm server, find `ros_zenoh-control-1`, copy its `CONTAINER ID`, and
      run `docker exec -it <container_id> /bin/bash` before editing the session configuration.
  - question: Do I need to log out and back in after installing Docker on the Raspberry Pi?
    answer: >-
      Yes. After adding your user to the docker group, log out and log back in so the new group
      membership takes effect.
  - question: What result should I expect when I run `ros2 topic list` on the Raspberry Pi, and
      what does it confirm?
    answer: >-
      Expect a full list of topics, roughly 80 entries, including `/camera/image_raw`, `/cmd_vel`,
      `/map`, and `/scan`. This confirms that you have ROS 2 graph discovery through the Zenoh
      client, but it doesn't by itself prove that message data is arriving.
  - question: Which option should I use to prevent crosstalk when adding multiple robots?
    answer: >-
      Use ROS namespaces to keep robots distinguishable on a shared graph, separate `ROS_DOMAIN_ID`
      values for complete isolation between groups, or a Zenoh namespace in the session configuration
      to partition at the transport layer.
# END generated_summary_faq

author:
    - Odin Shen
    - Kwashie Andoh
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
    - Docker
    - Raspberry Pi
    - Zenoh

operatingsystems:
    - Linux

### Cross-platform metadata only
shared_path: true
shared_between:
    - automotive
    - embedded-and-microcontrollers

further_reading:
    - resource:
        title: Build and deploy multi-node Zenoh systems on Raspberry Pi
        link: https://learn.arm.com/learning-paths/cross-platform/zenoh-multinode-ros2/
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

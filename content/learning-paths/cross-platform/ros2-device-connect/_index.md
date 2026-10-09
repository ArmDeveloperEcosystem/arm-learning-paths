---
title: Expose an Arm-based ROS 2 system as a discoverable device on Device Connect 
    
description: Learn how to expose a ROS 2 system running in Docker on an Arm-based Linux device as a discoverable Device Connect device, and inspect its ROS 2 graph through remote procedure calls.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for robotics and edge developers who want to get started with making a Robot Operating System 2 (ROS 2) system discoverable and callable by other devices and AI agents using Device Connect, without changing the ROS 2 application itself.

learning_objectives:
    - Identify how a Device Connect adapter bridges a containerized ROS 2 system to a Device Connect network.
    - Set up ROS 2 in Docker and the Device Connect Python packages on an Arm-based Linux machine.
    - Run the adapter in device-to-device (D2D) mode and call read-only ROS 2 inspection remote procedure calls (RPCs) from a Python client.
    - Describe how deployment profiles map the same adapter onto real hardware such as a Raspberry Pi 5 with a camera.

prerequisites:
    - An Arm-based Linux machine, such as a Raspberry Pi 5, an Arm cloud instance, or an Arm-based laptop, running Ubuntu 22.04 or later
    - Basic familiarity with Python, the Linux command line, and ROS 2 concepts such as nodes and topics

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-07T15:00:20Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e1f06683cf335325ef5db1e966a052360ecda2873847de0e2f7e19144e53d467
  summary_generated_at: '2026-10-07T15:00:20Z'
  summary_source_hash: e1f06683cf335325ef5db1e966a052360ecda2873847de0e2f7e19144e53d467
  faq_generated_at: '2026-10-07T15:00:20Z'
  faq_source_hash: e1f06683cf335325ef5db1e966a052360ecda2873847de0e2f7e19144e53d467
  summary: >-
    You'll expose a containerized ROS 2 system on Arm-based Linux as a discoverable Device Connect
    device. You'll see how the Device Connect adapter wraps ROS 2 commands as RPCs without
    changing the application. First, you'll start a ROS 2 Humble container, install the Device Connect
    packages, and run the adapter in D2D mode. Then, you'll inspect the ROS 2 graph from a
    Python client and explore profiles for a Raspberry Pi 5 camera or robot.
  faqs:
  - question: How do I confirm that I’m running on the right architecture before starting?
    answer: >-
      Run `uname -m` on your Arm-based Linux host. You should see `aarch64`.
  - question: What should I see to confirm that the ROS 2 container is working?
    answer: >-
      After starting the demo publisher, run `docker exec ros2_test bash -lc 'source
      /opt/ros/humble/setup.bash && ros2 node list && ros2 topic list'`. You should see `/chatter`,
      `/parameter_events`, and `/rosout`. You can expect an empty node list because the publisher
      runs as a hidden node.
  - question: How do I know that the adapter is running in D2D mode correctly?
    answer: >-
      Look for `D2D mode: skipping registry registration, using presence announcements` in the adapter
      log. Then, run `.venv/bin/python client.py` with the client environment settings. You should
      discover `rpi5-d2d`, and `get_ros_topics` should return `/chatter`.
  - question: Which profile should I use if I’m testing without a robot attached?
    answer: >-
      Use `rpi5` with `ROS_CONTAINER=ros2_test` and `WORKSPACE_SETUP=/opt/ros/humble/setup.bash`. You can validate the shared inspection RPCs without PuppyPi
      hardware. You can expect `ros_ok: false` in `get_status` because the robot packages are absent.
  - question: Which profile should I use for a Raspberry Pi 5 camera?
    answer: >-
      Use `rpi_camera` for the Raspberry Pi 5 camera example. Run
      `./ros2-device-connect/start_camera_ros2.sh` to start the `pi_ros` container and `/image_raw`
      publisher, then run `DEVICE_PROFILE=rpi_camera ./ros2-device-connect/start_d2d.sh`. For other
      hardware, create or edit a `profiles/<name>.env` file to select the driver, container, and ROS 2
      setup scripts.
# END generated_summary_faq

author: 
    - Kieran Hejmadi
    - Odin Shen

# New Learning Paths are opted in for the next manual generated summary/FAQ run.
# The generator resets this to false after a successful write.
generate_summary_faq: false

# Optional one-shot controls: set either field to true to regenerate just that
# generated section the next time the summary/FAQ tool runs. The tool resets
# them to false after a successful write.
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Libraries
armips:
    - Cortex-A
    - Neoverse
tools_software_languages:
    - ROS 2
    - Docker
    - Python
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
        title: ros2-device-connect example repository
        link: https://github.com/odincodeshen/ros2-device-connect
        type: website
    - resource:
        title: Device Connect repository
        link: https://github.com/arm/device-connect
        type: website
    - resource:
        title: ROS 2 documentation
        link: https://docs.ros.org/en/humble/
        type: documentation
    - resource:
        title: Device-to-Device communication with Device Connect
        link: /learning-paths/embedded-and-microcontrollers/device-connect-d2d/
        type: website
    - resource:
        title: Build a ROS 2 and Zenoh simulation environment on an Arm server
        link: /learning-paths/cross-platform/ros2-zenoh-arm/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

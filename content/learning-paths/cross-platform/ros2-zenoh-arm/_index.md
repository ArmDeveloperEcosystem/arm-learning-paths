---
title: Build a ROS 2 and Zenoh simulation environment on an Arm server

description: Set up ROS 2 Jazzy with rmw_zenoh in Docker, then run and evaluate a Neobotix ROX simulation on an Arm server.

minutes_to_complete: 60

who_is_this_for: This Learning Path is for developers who want to build and examine a containerized ROS 2 robotics simulation on an Arm server.

learning_objectives:
    - Set up a Docker-based ROS 2 Jazzy development and simulation environment on an Arm server
    - Configure rmw_zenoh as the ROS 2 middleware and explore communication between ROS 2 nodes
    - Launch and interact with a Neobotix ROX robot simulation using Gazebo, Navigation2, and RViz
    - Evaluate Zenoh router behavior and the effect of shared-memory transport

prerequisites:
    - An Arm server running Linux with at least 8 CPU cores, 16 GB of RAM, and 30 GB of free disk space
    - Docker and Docker Compose installed
    - Network access to ports 6080 and 6081 on the Arm server
    - Familiarity with launching bash shells within a running Docker container
    - Basic familiarity with Linux terminal commands within bash shells

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-31T16:18:00Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0c0836a15d9c03e95e1f5bda22cd0165aa6bbd28f89177e5ac593ebb48ab9987
  summary_generated_at: '2026-08-31T16:18:00Z'
  summary_source_hash: 0c0836a15d9c03e95e1f5bda22cd0165aa6bbd28f89177e5ac593ebb48ab9987
  faq_generated_at: '2026-08-31T16:18:00Z'
  faq_source_hash: 0c0836a15d9c03e95e1f5bda22cd0165aa6bbd28f89177e5ac593ebb48ab9987
  summary: >-
    You'll build a containerized ROS 2 Jazzy environment with `rmw_zenoh` on an Arm server and use it
    to run a Neobotix ROX simulation. First, you'll start the `robot` and `control` containers, configure
    Zenoh, and observe discovery with talker and listener nodes. Then, you'll launch Gazebo and
    Navigation2 and inspect the robot in RViz. Finally, you'll measure resource use, control the robot, and compare
    shared-memory transport with TCP loopback.
  faqs:
  - question: What should I check if the desktop UI in my browser doesn’t load?
    answer: >-
      Confirm the containers are running and that your Arm server allows access to the published
      web ports. Ensure network access to ports `6080` and `6081` is available from your client.
  - question: How do I open and prepare multiple bash shells inside the robot container?
    answer: >-
      Run `docker ps`, copy the `CONTAINER ID` for `ros_zenoh-robot-1`, then run `docker exec -it
      <container_id> /bin/bash` in each shell. In every shell, run `source ~/workshop_env.bash`.
  - question: What result should I expect when I stop the Zenoh router after the talker and listener
      connect?
    answer: >-
      You'll see the talker and listener continue communicating without interruption. This
      shows that you established a direct peer-to-peer connection and that the router isn't carrying
      their messages.
  - question: Should the Zenoh router stay running when launching the simulation and Navigation2?
    answer: >-
      Yes. After the router experiment, stop the talker and listener but keep the router running
      before starting the simulation and Navigation2.
  - question: What should I look for in RViz to confirm the simulation and Navigation2 are active?
    answer: >-
      Expect to see the robot model, map, global and local costmaps, and sensor visualizations.
      Use **Nav2 Goal** to set a navigation target and watch the robot plan and move in RViz.
# END generated_summary_faq

author:
    - Odin Shen
    - Kwashie Andoh
    - Habib Ogunbanwo

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

shared_path: true
shared_between:
    - automotive
    - embedded-and-microcontrollers

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
armips:
    - Neoverse
tools_software_languages:
    - ROS 2
    - rmw_zenoh
    - Docker
    - Gazebo
    - Navigation2
    - RViz
operatingsystems:
    - Linux

shared_between:
    - embedded-and-microcontrollers
    - automotive

further_reading:
    - resource:
        title: ROS 2 Jazzy RMW implementations
        link: https://docs.ros.org/en/jazzy/Installation/RMW-Implementations.html
        type: documentation
    - resource:
        title: rmw_zenoh source and documentation
        link: https://github.com/ros2/rmw_zenoh
        type: documentation
    - resource:
        title: Navigation2 getting started
        link: https://docs.nav2.org/getting_started/index.html
        type: documentation
    - resource:
        title: Gazebo Harmonic getting started
        link: https://gazebosim.org/docs/harmonic/getstarted/
        type: documentation
    - resource:
        title: ROS 2 and Zenoh on Arm source repository
        link: https://github.com/odincodeshen/ros2-zenoh-arm
        type: website
    - resource:
        title: Install Docker
        link: /install-guides/docker/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

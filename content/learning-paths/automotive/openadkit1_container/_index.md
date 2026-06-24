---
title: Deploy Open AD Kit containerized autonomous driving simulation on Arm Neoverse
description: Learn how to deploy and run containerized autonomous driving simulations using Autoware Open AD Kit on Arm Neoverse with Docker, demonstrating SOAFEE-based Shift-Left development workflows.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for automotive developers, aimed at helping them accelerate autonomous driving software development before automotive hardware is available.

learning_objectives: 
    - Understand the SOAFEE architecture and its role in supporting Shift-Left software development strategies to optimize the autonomous driving development process
    - Use the Autoware Open AD Kit simulation environment
    - Run containerized workloads on Arm Neoverse processors with Docker, supporting execution on both cloud-based and on-premise servers
    - Explore advanced configurations and future development prospects
prerequisites:
    - An Arm Neoverse cloud instance, or a local Arm Neoverse Linux computer with at least 16 CPUs and 32GB of RAM
    - Familiarity with Docker and Docker Compose

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-24T15:35:34Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 37913b2c4aed914d32dbdad054ebdd2b1d4587da3ede1a33ba81e3e68bf504a3
  summary_generated_at: '2026-06-24T15:35:34Z'
  summary_source_hash: 37913b2c4aed914d32dbdad054ebdd2b1d4587da3ede1a33ba81e3e68bf504a3
  faq_generated_at: '2026-06-24T15:35:34Z'
  faq_source_hash: 37913b2c4aed914d32dbdad054ebdd2b1d4587da3ede1a33ba81e3e68bf504a3
  summary: >-
    This Learning Path guides learners through deploying and running a containerized Autoware
    Open AD Kit simulation on Arm Neoverse using Docker and Docker Compose, within a SOAFEE-aligned
    Shift-Left workflow. It introduces Software-Defined Vehicles and SOAFEE, then outlines ROS
    2 and Open AD Kit concepts used in the demo. Learners prepare an Arm Neoverse Linux system
    and use Docker Compose to start the Visualizer first, followed by continuously executing Planning
    and Simulation services defined in docker/docker-compose.yml. The workflow has been exercised
    on both cloud (AWS EC2) and on-premise Arm Neoverse platforms, enabling evaluation on available
    infrastructure. By the end, learners can launch the containers, inspect the compose file,
    and recognize a running simulation on Arm Neoverse.
  faqs:
  - question: What result should I expect after launching the Docker Compose stack?
    answer: >-
      The Visualizer service starts in detached mode, followed by continuously running Planning
      and Simulation services. Active containers for these components indicate the demo is operating
      as intended.
  - question: Where are the ROS 2 commands and service configurations defined?
    answer: >-
      They are defined in the docker/docker-compose.yml file. Reviewing that file shows the launch
      order, container settings, and ROS 2 commands used by the demo.
  - question: Can I run the same workflow on cloud and on-prem Arm Neoverse systems?
    answer: >-
      Yes. The example has been tested on AWS EC2 and an Ampere Altra workstation, so you can
      choose either a cloud instance or an on-premise Arm Neoverse system.
  - question: What should I check before starting the demo to avoid resource-related failures?
    answer: >-
      Verify the Arm Neoverse system provides at least 16 CPUs and 32 GB of RAM. Ensure Docker
      and Docker Compose are installed and available.
  - question: If I stop and restart the demo, do I need to reconfigure anything?
    answer: >-
      No. Docker Compose enables you to start with the previous session’s settings without modifications,
      so the configuration persists between runs.
# END generated_summary_faq

author: Odin Shen

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
armips:
    - Neoverse
tools_software_languages:
    - Python
    - Docker
    - ROS 2
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Autoware OpenAD Kit demo project
        link: https://github.com/autowarefoundation/openadkit_demo.autoware/
        type: documentation
    - resource:
        title: SOAFEE (Scalable Open Architecture For Embedded Edge)
        link: https://soafee.io/
        type: documentation
    - resource:
        title: Autoware Foundation
        link: https://www.autoware.org/
        type: documentation
    - resource:
        title: ROS 2 Documentation
        link: https://docs.ros.org/en/humble/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:26:58Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 37913b2c4aed914d32dbdad054ebdd2b1d4587da3ede1a33ba81e3e68bf504a3
  summary_generated_at: '2026-06-01T20:57:21Z'
  summary_source_hash: 37913b2c4aed914d32dbdad054ebdd2b1d4587da3ede1a33ba81e3e68bf504a3
  faq_generated_at: '2026-06-02T21:26:58Z'
  faq_source_hash: 37913b2c4aed914d32dbdad054ebdd2b1d4587da3ede1a33ba81e3e68bf504a3
  summary: >-
    This Learning Path shows how to deploy and run a containerized autonomous driving simulation
    using Autoware Open AD Kit on Arm Neoverse with Docker, illustrating SOAFEE-aligned Shift-Left
    development. You will use a Linux Arm Neoverse instance—cloud or on‑prem—and Docker Compose
    to launch the Open AD Kit demo, which starts a Visualizer and then runs Planning and Simulation
    services defined in docker/docker-compose.yml. It introduces the SOAFEE architecture plus
    the roles of ROS 2 and Open AD Kit. Prerequisites are an Arm Neoverse system with at least
    16 CPUs and 32GB RAM, and familiarity with Docker and Docker Compose. Estimated time is 60
    minutes; the example was tested on AWS EC2 and an Ampere Altra workstation.
  faqs:
  - question: What do I need before running the demo?
    answer: >-
      You need an Arm Neoverse cloud instance or a local Arm Neoverse Linux computer with at least
      16 CPUs and 32GB of RAM. Familiarity with Docker and Docker Compose is also required.
  - question: Should I use a cloud instance or an on-prem Arm Neoverse system?
    answer: >-
      You can use either. The example has been tested on AWS EC2 and an Ampere Altra workstation,
      so choose the environment you have access to or that best fits your needs.
  - question: Do I need to install Docker and Docker Compose?
    answer: >-
      Yes. Docker is required to run Open AD Kit, and the demo uses Docker Compose; refer to the
      Docker install guide to set it up on Linux.
  - question: What should I expect when I start the demo with Docker Compose?
    answer: >-
      The Visualizer service starts first in detached mode, followed by continuous execution of
      the Planning and Simulation components. The ROS 2 commands and service definitions are specified
      in docker/docker-compose.yml.
  - question: Where can I inspect or adjust what gets executed?
    answer: >-
      Open the docker/docker-compose.yml file to review the service configuration, startup order,
      and ROS command lines. You can use it as the basis for exploring advanced configurations
      mentioned in the path.
# END generated_summary_faq

author: Odin Shen

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


---
title: Connect AI agents to edge devices using Device Connect and Strands
description: Learn how to connect AI agents to Arm-based edge devices using Device Connect for structured device access and Strands for agent orchestration, with examples for both simulated and physical robots.
minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers who want to connect AI agents to edge devices. You'll use Device Connect, Arm's platform for structured device access, and Strands, AWS's open-source agent SDK. The examples cover both physical and simulated devices.


learning_objectives:
    - Understand how Device Connect and Strands work together to give AI agents structured access to Arm-based edge devices
    - Set up a Python environment with the Device Connect SDK and agent tools installed from source
    - Start a simulated robot that registers itself on the local network and is discovered automatically by an agent
    - Discover and invoke the robot using the Device Connect agent tools and the robot_mesh Strands tool

prerequisites:
    - A development machine with git installed
    - Basic familiarity with command-line tools
    - (Optional) A Raspberry Pi for testing a full device-to-device (D2D) setup

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:17:42Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: c31d398d3ce965a4193fca45cd025182d788a2fc603fbe8c828dfbd5a1c599ba
  summary_generated_at: '2026-06-01T21:38:36Z'
  summary_source_hash: c31d398d3ce965a4193fca45cd025182d788a2fc603fbe8c828dfbd5a1c599ba
  faq_generated_at: '2026-06-02T22:17:42Z'
  faq_source_hash: c31d398d3ce965a4193fca45cd025182d788a2fc603fbe8c828dfbd5a1c599ba
  summary: >-
    Learn to connect AI agents to Arm-based edge devices using Device Connect for structured device
    access and Strands for agent orchestration. You will set up a Python environment from source
    by cloning the strands-labs/robots repository and running its setup script to install dependencies
    and create a Python 3.12 virtual environment. Then you will start a simulated robot that registers
    on the local network and use Device Connect agent tools with the robot_mesh Strands tool to
    discover and invoke it. An optional section runs Zenoh, etcd, and a registry via Docker and
    connects a Raspberry Pi for a full device-to-device setup. Target platforms are Linux and
    macOS; prerequisites are Git and basic command-line skills. Core steps take about 30 minutes.
  faqs:
  - question: What do I need before cloning the repository?
    answer: >-
      Use a Linux or macOS machine with git installed and basic command-line familiarity. Docker
      is only required for the optional infrastructure section. A Raspberry Pi is optional if
      you want to test a full device-to-device setup.
  - question: How do I set up the Python environment?
    answer: >-
      Clone the robots repository and run the provided setup.sh script. The script installs uv,
      creates a Python 3.12 virtual environment, and installs all required packages; then source
      the environment as directed in the steps.
  - question: Which option should I choose for device discovery and control?
    answer: >-
      Choose the single-machine option to follow a conceptual implementation using two terminal
      windows on your machine. Choose the real hardware option if you have an external device;
      your machine acts as the agent machine and the external device serves as the remote device.
  - question: How do I know the agent discovered the robot?
    answer: >-
      After starting the simulated robot, it registers on the local network and is discovered
      automatically by the agent. Use the Device Connect agent tools and the robot_mesh Strands
      tool to list and invoke the robot.
  - question: What changes when I run with the full Device Connect infrastructure?
    answer: >-
      You will run a Zenoh router, an etcd state store, and a registry service on your machine
      using Docker, then connect a Raspberry Pi on the same network as the remote device. This
      goes beyond the local-only discovery used in the earlier section.
# END generated_summary_faq

author: 
    - Annie Tallund
    - Kavya Sri Chennoju



### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A
    - Neoverse
operatingsystems:
    - Linux
    - macOS
tools_software_languages:
    - Python
    - Docker
    - strands-agents

further_reading:
    - resource:
        title: Strands Agents SDK documentation
        link: https://strandsagents.com/
        type: website
    - resource:
        title: Strands robots repository
        link: https://github.com/strands-labs/robots
        type: website
    - resource:
        title: device-connect-agent-tools on PyPI
        link: https://pypi.org/project/device-connect-agent-tools
        type: website
    - resource:
        title: device-connect-sdk on PyPI
        link: https://pypi.org/project/device-connect-sdk
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


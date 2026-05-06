---
title: Device-to-Device communication with Device Connect

minutes_to_complete: 25


who_is_this_for: This is an introductory topic for developers wiring up heterogeneous edge fleets, where devices need a shared way to find each other and a shared way to be controlled by agents. Device Connect provides this communication protocol between agents and devices, and standardizes how devices from different vendors advertise themselves and exchange structured messages, so both peer devices and AI agents can discover and invoke them through the same driver model. You'll use it to stand up peer-to-peer communication between two devices, with no broker or cloud service in between.

learning_objectives:
    - Understand Device Connect Edge SDK primitives 
    - Set up a Python environment for Device Connect with no hardware required
    - Build two simulated devices
    - Use the Device Connect agent tools to discover both devices on the mesh and invoke their RPCs

prerequisites:
    - Basic familiarity with Python and the command line

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:54Z'
  generator: template
  source_hash: 9d9e4c170fa318a9875c888c2c812ceb27c59f56c4b0dd7e0ae87dd31bb5783c
  summary: >-
    Device-to-Device communication with Device Connect walks you through an end-to-end Arm software
    workflow. It is designed for developers wiring up heterogeneous edge fleets, where devices
    need a shared way to find each other and a shared way to be controlled by agents. Device Connect
    provides this communication protocol between agents and devices, and standardizes how devices
    from different vendors advertise themselves and exchange structured messages, so both peer
    devices and AI agents can discover and invoke them through the same driver model. You'll use
    it to stand up peer-to-peer communication between two devices, with no broker or cloud service
    in between. By the end, you will be able to understand Device Connect Edge SDK primitives,
    set up a Python environment for Device Connect with no hardware required, and build two simulated
    devices. It focuses on tools and technologies such as Python, Linux, macOS, and Windows environments,
    and Arm platforms including Cortex-A. The main steps cover Why device-to-device at the edge,
    Device Connect developer model, and Set up D2D communication between a sensor and a monitor.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will understand Device Connect Edge SDK primitives, set up a Python environment for
      Device Connect with no hardware required, and build two simulated devices.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for developers wiring up heterogeneous edge fleets, where
      devices need a shared way to find each other and a shared way to be controlled by agents.
      Device Connect provides this communication protocol between agents and devices, and standardizes
      how devices from different vendors advertise themselves and exchange structured messages,
      so both peer devices and AI agents can discover and invoke them through the same driver
      model. You'll use it to stand up peer-to-peer communication between two devices, with no
      broker or cloud service in between.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: Basic familiarity with Python and the
      command line.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Python, Linux, macOS, and Windows environments,
      and Arm platforms such as Cortex-A.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Why device-to-device at the edge, Device Connect developer
      model, and Set up D2D communication between a sensor and a monitor.
# END generated_summary_faq

author:
    - Kavya Sri Chennoju
    - Annie Tallund

### Tags
skilllevels: Introductory
subjects: Libraries
armips:
    - Cortex-A
operatingsystems:
    - Linux
    - macOS
    - Windows
tools_software_languages:
    - Python

further_reading:
    - resource:
        title: Device Connect repository
        link: https://github.com/arm/device-connect
        type: website
    - resource:
        title: device-connect-edge package
        link: https://github.com/arm/device-connect/tree/main/packages/device-connect-edge
        type: documentation
    - resource:
        title: Zenoh
        link: https://zenoh.io/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---


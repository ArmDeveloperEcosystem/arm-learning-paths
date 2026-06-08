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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:16:41Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 9d9e4c170fa318a9875c888c2c812ceb27c59f56c4b0dd7e0ae87dd31bb5783c
  summary_generated_at: '2026-06-01T21:38:11Z'
  summary_source_hash: 9d9e4c170fa318a9875c888c2c812ceb27c59f56c4b0dd7e0ae87dd31bb5783c
  faq_generated_at: '2026-06-02T22:16:41Z'
  faq_source_hash: 9d9e4c170fa318a9875c888c2c812ceb27c59f56c4b0dd7e0ae87dd31bb5783c
  summary: >-
    Learn how to establish peer-to-peer device-to-device communication at the edge using the Device
    Connect Edge SDK in a Python environment, with no hardware required. You will build two simulated
    devices on the same mesh: a sensor that publishes temperature and humidity readings, and a
    threshold monitor that subscribes and raises an alert when a configurable limit is crossed.
    Along the way, you will work with the SDK’s developer model (DeviceDriver, decorators, and
    DeviceRuntime) and see how discovery, pub/sub, and RPC fit together. The walkthrough uses
    uv to manage the project and dependencies, and includes using Device Connect agent tools to
    discover devices and invoke their RPCs. Target platforms include Linux, macOS, and Windows.
    Prerequisite: basic familiarity with Python and the command line. Estimated time: about 25
    minutes.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      You should be comfortable with Python and the command line. The steps support Linux, macOS,
      and Windows, and no hardware is required.
  - question: Do I need a broker or cloud service to complete the device-to-device setup?
    answer: >-
      No. The walkthrough stands up peer-to-peer communication between two devices with no broker
      or cloud service in between.
  - question: Which tool is used to manage the Python project and dependencies?
    answer: >-
      The walkthrough uses uv to manage the project and its Python dependencies. uv will resolve
      a compatible Python for the environment.
  - question: How are devices defined and brought online with Device Connect?
    answer: >-
      You subclass DeviceDriver from device_connect_edge.drivers and annotate methods and properties
      with primitives. DeviceRuntime brings the driver online and wires it into discovery, pub/sub,
      and RPC.
  - question: How do I know the two simulated devices are discoverable and callable?
    answer: >-
      You will use the Device Connect agent tools to discover both devices on the mesh and invoke
      their RPCs. Successful discovery and RPC calls indicate the setup is working as intended.
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


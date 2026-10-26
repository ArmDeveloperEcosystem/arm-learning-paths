---
title: Device-to-Device communication with Device Connect
description: Learn how to connect simulated edge devices directly with Device Connect and build a sensor-to-monitor workflow without cloud infrastructure.

minutes_to_complete: 25

who_is_this_for: This is an introductory topic for developers wiring up heterogeneous edge fleets, where devices need a shared way to find each other and a shared way to be controlled by agents. Device Connect provides this communication protocol between agents and devices, and standardizes how devices from different vendors advertise themselves and exchange structured messages, so both peer devices and AI agents can discover and invoke them through the same driver model. You'll use a Raspberry Pi 5 as the example primary edge device, but the same flow works with another device or with your development machine acting as a simulated device.

learning_objectives:
    - Understand Device Connect Edge SDK primitives 
    - Set up a Python environment for Device Connect on an example edge device and a development machine
    - Build two device runtimes, with the primary sensor runtime shown on a Raspberry Pi 5
    - Use the Device Connect agent tools to discover both devices on the mesh and invoke their RPCs

prerequisites:
    - Basic familiarity with Python and the command line
    - A Raspberry Pi 5, another Linux device, or your development machine to use as the example primary device
    - A development machine on the same local network if you run the example across two machines

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-08T15:30:43Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 5a0b83867d9a7c5785f8cb52100e8dbbff47737e55e4237afb246993e546fd4a
  summary_generated_at: '2026-07-08T15:30:43Z'
  summary_source_hash: 5a0b83867d9a7c5785f8cb52100e8dbbff47737e55e4237afb246993e546fd4a
  faq_generated_at: '2026-07-08T15:30:43Z'
  faq_source_hash: 5a0b83867d9a7c5785f8cb52100e8dbbff47737e55e4237afb246993e546fd4a
  summary: >-
    You'll build two Python-based device runtimes with
    the Device Connect Edge SDK and wire them into a local device-to-device workflow without
    cloud infrastructure. First, you'll define device behavior by subclassing `DeviceDriver`, annotating methods
    with SDK decorators, and bringing the driver online with `DeviceRuntime`. A Raspberry Pi 5 acts
    as the primary sensor device publishing temperature and humidity, while a threshold monitor
    on a development machine subscribes to those readings and raises an alert when a limit is
    crossed. Using Device Connect agent tools, you'll discover both devices on the mesh, verify
    pub/sub traffic, and invoke exposed RPCs to confirm the runtimes are visible and controllable
    end to end.
  faqs:
  - question: How do I know both runtimes joined the same mesh?
    answer: >-
      Use the Device Connect agent tools to discover devices on the mesh. You'll see both
      the sensor and the monitor listed, and the monitor should receive the sensor’s periodic
      readings.
  - question: Can I run the example without a Raspberry Pi 5?
    answer: >-
      Yes. The same flow works with another device or with your development machine acting as
      a simulated device.
  - question: Which parts of the Device Connect Edge SDK do I implement to describe a device?
    answer: >-
      Subclass `DeviceDriver` and annotate its methods and properties with the SDK’s decorators.
      Start a `DeviceRuntime` to bring the driver online for discovery, pub/sub, and RPC.
  - question: What result should I expect from the threshold monitor when everything is working?
    answer: >-
      The monitor subscribes to the sensor’s temperature and humidity readings and raises an alert
      when the temperature crosses the configured threshold.
  - question: What should I check if devices aren't discovering each other or RPC calls fail?
    answer: >-
      Confirm both runtimes are running on the same local network and that the agent tools can
      list each device. Verify the Python environments are set up as shown and that each runtime
      started without errors.
# END generated_summary_faq

author:
    - Kavya Sri Chennoju
    - Annie Tallund

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

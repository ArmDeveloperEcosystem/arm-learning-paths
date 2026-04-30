---
title: Access remote devices with Remote.It

minutes_to_complete: 45

description: Learn how to install and configure Remote.It for secure remote device access using SSH and other services, with proxy and peer-to-peer connection options.

who_is_this_for: This is an introductory topic for software developers who want to use Remote.It to establish private network connections between users and devices or devices to device.

learning_objectives:
    - Install Remote.It on target devices (devices you would like to access remotely)
    - Access your Remote.It enabled devices from anywhere
    - Understand the different types of network connections (proxy vs. Peer to peer)

prerequisites:
    - A Windows, macOS, or Linux computer which you will use to configure your devices as well as connect to your remote devices.
    - A device/computer to which you would like remote access. A device can be a Windows, Mac, or Linux computer including development kits such as Raspberry Pi or cloud-hosted such as within Arm Virtual Hardware or within AWS. You will need a method to control this device before Remote.It is deployed which can be local access or access via another remote connectivity solution (Remote Desktop, VPN, etc.)
    - Determine if your device that you would like to access remotely also needs to make connections to other Remote.It devices.

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:15Z'
  generator: template
  source_hash: 927cfebb8ebf9595922dad115c9a8d10900e43c4f80e73e6102a71e3e4ca2da1
  summary: >-
    Learn how to install and configure Remote.It for secure remote device access using SSH and
    other services, with proxy and peer-to-peer connection options. It is designed for software
    developers who want to use Remote.It to establish private network connections between users
    and devices or devices to device. By the end, you will be able to install Remote.It on target
    devices (devices you would like to access remotely), access your Remote.It enabled devices
    from anywhere, and understand the different types of network connections (proxy vs. Peer to
    peer). It focuses on tools and technologies such as Remote.It, Linux, Windows, and macOS environments,
    and Arm platforms including Neoverse and Cortex-A. The main steps cover Remote.It Packages,
    Installing the Remote.It Device Package, Remote.It CLI, and Connections.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will install Remote.It on target devices (devices you would like to access remotely),
      access your Remote.It enabled devices from anywhere, and understand the different types
      of network connections (proxy vs. Peer to peer). Learn how to install and configure Remote.It
      for secure remote device access using SSH and other services, with proxy and peer-to-peer
      connection options.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for software developers who want to use Remote.It to establish
      private network connections between users and devices or devices to device.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A Windows, macOS, or Linux computer
      which you will use to configure your devices as well as connect to your remote devices.;
      A device/computer to which you would like remote access. A device can be a Windows, Mac,
      or Linux computer including development kits such as Raspberry Pi or cloud-hosted such as
      within Arm Virtual Hardware or within AWS. You will need a method to control this device
      before Remote.It is deployed which can be local access or access via another remote connectivity
      solution (Remote Desktop, VPN, etc.); Determine if your device that you would like to access
      remotely also needs to make connections to other Remote.It devices.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Remote.It, Linux, Windows, and macOS environments,
      and Arm platforms such as Neoverse and Cortex-A.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Remote.It Packages, Installing the Remote.It Device
      Package, Remote.It CLI, and Connections.
# END generated_summary_faq

author: Brenda Strech

further_reading:
  - resource:
      title: Developer Documentation
      link: https://docs.remote.it
      type: documentation
  - resource:
      title: GraphQL API Documentation
      link: https://link.remote.it/docs/graphql
      type: documentation
  - resource:
      title: User Forum
      link: https://forum.remote.it
      type: website
  - resource:
      title: Help Center
      link: https://support.remote.it/hc/en-us
      type: website

### Tags
skilllevels: Introductory
subjects: CI-CD
armips:
    - Neoverse
    - Cortex-A
tools_software_languages:
    - Remote.It
operatingsystems:
    - Linux
    - Windows
    - macOS

### Test
test_images:
- ubuntu:latest
test_maintenance: false

### Cross-platform metadata only
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - embedded-and-microcontrollers

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


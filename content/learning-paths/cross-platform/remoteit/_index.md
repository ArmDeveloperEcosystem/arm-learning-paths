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

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:49:07Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 927cfebb8ebf9595922dad115c9a8d10900e43c4f80e73e6102a71e3e4ca2da1
  summary_generated_at: '2026-06-01T21:15:32Z'
  summary_source_hash: 927cfebb8ebf9595922dad115c9a8d10900e43c4f80e73e6102a71e3e4ca2da1
  faq_generated_at: '2026-06-02T21:49:07Z'
  faq_source_hash: 927cfebb8ebf9595922dad115c9a8d10900e43c4f80e73e6102a71e3e4ca2da1
  summary: >-
    This introductory Learning Path shows how to install and configure Remote.It to access remote
    devices using SSH and other services, and how to choose between proxy and peer-to-peer connection
    options. You will install the Remote.It device package on a target device, connect from an
    initiator computer, and use the Web Dashboard or CLI to create connections. The path applies
    to Windows, macOS, and Linux environments and supports devices ranging from laptops and Raspberry
    Pi to cloud-hosted targets such as Arm Virtual Hardware or within AWS. Prerequisites include
    a Windows, macOS, or Linux computer for setup, control access to the target before deploying
    Remote.It, and a decision on whether the target must also connect to other Remote.It devices.
  faqs:
  - question: What do I need before running the setup?
    answer: >-
      Have a Windows, macOS, or Linux computer to configure and connect, plus a target device
      (Windows, Mac, or Linux) you can control locally or through another remote solution before
      deploying Remote.It. Targets can include development kits like Raspberry Pi or cloud-hosted
      systems such as Arm Virtual Hardware or AWS. Also determine whether your target will need
      to make connections to other Remote.It devices.
  - question: How do I install the Remote.It device package when I already have access to the
      target?
    answer: >-
      Use a local console or SSH to access the target and follow the steps to install the Remote.It
      device package. If you need SSH on the target, refer to the SSH guidance referenced in the
      path.
  - question: Do I need to install anything on the initiator computer to connect?
    answer: >-
      If you use the Remote.It Web Dashboard, proxy connections require only standard tools like
      SSH on the initiator and no additional Remote.It software. For headless use or automation,
      install the Remote.It CLI; if you already installed the Desktop software, the CLI binary
      is included. On Linux, ensure the CLI binary has execute permission.
  - question: Which connection type should I use, proxy or peer-to-peer?
    answer: >-
      The Web Dashboard creates proxy connections and is the easiest to set up because only the
      target needs Remote.It installed; all traffic is routed through a Remote.It server. Peer-to-peer
      connections are direct between initiator and target. Choose proxy for the simplest setup,
      or peer-to-peer when you want a direct connection.
  - question: What result should I expect after completing the steps, and how do I know it worked?
    answer: >-
      You should be able to initiate an SSH session to your Remote.It-enabled target from another
      location using the connection type you configured. For proxy connections, traffic will route
      through a Remote.It server; for peer-to-peer, the link is direct. A successful SSH login
      indicates the setup is working.
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


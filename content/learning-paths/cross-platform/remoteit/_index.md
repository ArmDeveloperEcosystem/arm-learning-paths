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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-29T16:46:14Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 927cfebb8ebf9595922dad115c9a8d10900e43c4f80e73e6102a71e3e4ca2da1
  summary_generated_at: '2026-07-29T16:46:14Z'
  summary_source_hash: 927cfebb8ebf9595922dad115c9a8d10900e43c4f80e73e6102a71e3e4ca2da1
  faq_generated_at: '2026-07-29T16:46:14Z'
  faq_source_hash: 927cfebb8ebf9595922dad115c9a8d10900e43c4f80e73e6102a71e3e4ca2da1
  summary: >-
    Install the Remote.It device package on a target system and establish private access to services
    such as SSH. You use the Remote.It Web Dashboard to create proxy connections, compare them with
    peer-to-peer connections, and route traffic through either a Remote.It server or a direct path.
    You also use the Remote.It CLI for headless or scripted initiators, then verify SSH access and
    choose the connection method that fits your requirements.
  faqs:
  - question: What result should I expect after installing the Remote.It device package on the
      target?
    answer: >-
      The device appears in the Remote.It Web Dashboard. Start a connection and reach it with a
      standard tool such as SSH from the initiator.
  - question: Do I need to install anything on the initiator to make the first connection?
    answer: >-
      No. For a proxy connection created in the Web Dashboard, use SSH from the initiator without
      additional software. Install the Remote.It CLI only for a headless or scripted workflow.
  - question: Which connection type should I use for my first test, proxy or peer-to-peer?
    answer: >-
      Use a proxy connection for the simplest setup: only the target needs Remote.It, and traffic
      goes through a Remote.It server. Use peer-to-peer when you need a direct path between the
      initiator and target.
  - question: How do I run the Remote.It CLI on Linux without a desktop environment?
    answer: >-
      Download the CLI binary for your platform, rename it if needed, and make it executable. Use
      it to create connections from the initiator without installing the Desktop app.
  - question: What should I check if SSH fails after I start a connection?
    answer: >-
      Verify that SSH is installed and configured on the target. Confirm that the device is visible
      in the Web Dashboard and that the connection is active before retrying the SSH command.
# END generated_summary_faq

author: Brenda Strech

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

---
title: Deploy multi-network device meshes using Device Connect server and NATS

description: Connect an example edge device, secondary devices, and AI agents across networks using Device Connect server. Learn to provision NATS credentials, commission devices, manage persistent registry, and orchestrate multi-network IoT fleets with secure authentication.
minutes_to_complete: 30

who_is_this_for: This Learning Path is for developers who have completed the Device-to-device Learning Path and want to build a globally connected fleet of devices and AI agents on top of their Device Connect mesh. You'll add a server layer that gives you persistent registry, distributed state, and security features (commissioning, ACLs) so devices and agents on different networks can find and call each other through a single namespace. If you're new to Device Connect, start with the device-to-device Learning Path first.

learning_objectives:
    - Understand what the Device Connect server adds on top of the edge SDK and when you'd reach for it
    - Provision a hosted tenant on the Device Connect portal and download per-device NATS credentials
    - Commission an example primary device and a secondary device against your tenant using the credentials the portal issues
    - Discover and invoke commissioned devices from a Python client using `device-connect-agent-tools`
    - Connect a Strands AI agent to the same tenant

prerequisites:
    - Complete the [Device-to-device Learning Path](/learning-paths/embedded-and-microcontrollers/device-connect-d2d/) to understand Device Connect edge SDK basics
    - An account on the [Device Connect portal](https://portal.deviceconnect.dev/)
    - A Raspberry Pi 5, another Linux device, or your development machine to use as the example primary device
    - A development machine for the secondary device and Python client
    - Basic familiarity with Python and the command line

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-12T20:03:14Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ff80157611a84755964dc9809f497b46bdb352ffeb5f99b0df5bd97ce8ae4f76
  summary_generated_at: '2026-08-12T20:03:14Z'
  summary_source_hash: ff80157611a84755964dc9809f497b46bdb352ffeb5f99b0df5bd97ce8ae4f76
  faq_generated_at: '2026-08-12T20:03:14Z'
  faq_source_hash: ff80157611a84755964dc9809f497b46bdb352ffeb5f99b0df5bd97ce8ae4f76
  summary: >-
    You'll extend a Device Connect mesh across networks with a server and NATS authentication.
    First, you'll provision a private tenant, download device credentials, and commission primary and
    secondary devices. Then, you'll discover devices and invoke RPCs from Python to verify reachability. You'll connect a Strands AI agent so devices and agents share one authenticated registry.
  faqs:
  - question: How do I know my tenant is ready before I commission devices?
    answer: >-
      After you sign in to the Device Connect portal, a private tenant is created. You should
      be able to download per-device NATS credentials and use them to commission a device. If
      the Python client can discover that device, your tenant is ready.
  - question: Which credentials should I use on the primary and secondary devices?
    answer: >-
      Use the per-device NATS credentials you download from the portal for each specific device.
      Don't reuse a single credential across multiple devices.
  - question: What result should I expect when discovery works from the Python client?
    answer: >-
      The client lists commissioned devices in your tenant and can invoke their RPCs. Successful
      calls confirm that routing over the Device Connect server and NATS is working across networks.
  - question: What should I check if the client cannot discover a commissioned device?
    answer: >-
      Verify the device was commissioned to the same tenant and is running with the correct NATS
      credentials. Also confirm the client is targeting that tenant and repeat discovery after
      the device is online.
  - question: How do I connect a Strands AI agent to the same tenant?
    answer: >-
      Configure the agent with the tenant details and portal-issued credentials, then start it.
      The agent should appear under the tenant’s namespace and be able to discover and invoke commissioned
      devices such as the Python client.
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
    - Neoverse
operatingsystems:
    - Linux
    - macOS
tools_software_languages:
    - Python
    - Docker

further_reading:
    - resource:
        title: Device Connect
        link: https://deviceconnect.dev/
        type: website
    - resource:
        title: device-connect-server package
        link: https://github.com/arm/device-connect/tree/main/packages/device-connect-server
        type: documentation
    - resource:
        title: device-to-device Learning Path
        link: /learning-paths/embedded-and-microcontrollers/device-connect-d2d/
        type: website
    - resource:
        title: NATS documentation
        link: https://docs.nats.io/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

---
title: Run a Minecraft server on an Arm-based Oracle Cloud Infrastructure instance

description: Deploy a Minecraft Java Edition server on an Arm-based OCI A1 instance, open port `25565`, and connect from the Minecraft client.

minutes_to_complete: 10

who_is_this_for: This is an introductory topic for developers who are new to Oracle Cloud Infrastructure (OCI) and want to provision an arm64 instance and run a persistent Minecraft server on it.

learning_objectives: 
    - Provision an OCI A1 arm64 virtual machine instance suitable for running a Minecraft server
    - Deploy and configure Minecraft server software
    - Expose the Minecraft service from OCI by editing the network policy for the instance and the virtual machine instance firewall 
    - Connect to the running Minecraft server from the Minecraft client application

prerequisites:
    - An Oracle Cloud Infrastructure (OCI) account
    - A copy of the [Minecraft Java Edition client](https://www.minecraft.net/en-us/download) installed, and [a license for the game](https://www.minecraft.net/en-us/store/minecraft-java-bedrock-edition-pc)
    - A Microsoft account for starting a Minecraft client application

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-09T20:00:42Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d04787946bee50f6b196f22d0b9c890a69df2ed32a0b9769f5f6320912c925a6
  summary_generated_at: '2026-07-09T20:00:42Z'
  summary_source_hash: d04787946bee50f6b196f22d0b9c890a69df2ed32a0b9769f5f6320912c925a6
  faq_generated_at: '2026-07-09T20:00:42Z'
  faq_source_hash: d04787946bee50f6b196f22d0b9c890a69df2ed32a0b9769f5f6320912c925a6
  summary: >-
    You'll provision an Arm-based Ampere A1 virtual machine (VM) on Oracle
    Cloud Infrastructure (OCI), install the required Java runtime, and deploy a Minecraft Java Edition
    server. First, you'll set up the OCI VM instance and update security ingress rules. Then, you'll configure a persistent terminal session so the server continues running after
    SSH disconnects. With the server running, you'll update the server-side local firewall, start the Minecraft Java Edition
    client, and connect to the server to validate the deployment.
  faqs:
  - question: Which OCI shape and image should I choose for the server?
    answer: >-
      Create an Arm-based Ampere A1 instance with Oracle Linux 9.
  - question: Which Java package should I install on the Arm instance?
    answer: >-
      For Minecraft 26 or earlier, install Java 25 OpenJDK for aarch64. Use: `sudo dnf install
      java-25-openjdk.aarch64 -y`.
  - question: How do I keep the Minecraft server running after I close my SSH session?
    answer: >-
      Use tmux to create a persistent terminal session and start the server inside that session.
      You can disconnect and later reattach to the `tmux` session without stopping the server.
  - question: Which port do I need to open on the VM, and how?
    answer: >-
      Open TCP port `25565` in the Linux firewall. Run: `sudo firewall-cmd --permanent --add-port=25565/tcp`
      and `sudo firewall-cmd --reload`.
  - question: I opened the VM firewall but the client still can't connect. What should I check?
    answer: >-
      Verify the OCI network policy for the instance allows inbound TCP traffic on port `25565`
      to the VM. Update the OCI security settings if needed, then try connecting again.
# END generated_summary_faq

author: Dave Neary

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Web
armips:
    - Neoverse
tools_software_languages:
    - Java
    - Minecraft
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: How to create a powerful Minecraft Server for free using Oracle Cloud
        link: https://www.youtube.com/watch?v=0kFjEUDJexI
        type: video
    - resource:
        title: Deploy Arm instances on Oracle Cloud Infrastructure (OCI) using Terraform
        link: /learning-paths/servers-and-cloud-computing/oci-terraform/
        type: learning-path
    - resource:
        title: Getting started with Oracle Cloud Infrastructure 
        link: /learning-paths/servers-and-cloud-computing/csp/oci/
        type: learning-path 


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


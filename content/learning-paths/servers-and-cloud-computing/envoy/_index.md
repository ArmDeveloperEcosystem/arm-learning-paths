---
title: Learn how to deploy Envoy
description: Learn how to build, install, and run Envoy proxy on Arm servers and configure it as a web server for traffic management.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for engineers who want to use Envoy on Arm.

learning_objectives:
    - Build, install, and run Envoy on Arm servers
    - Setup Envoy as a web server
    - Verify Envoy is working correctly

prerequisites:
    - To run Envoy as a web server, you will need at least one [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or an on-premises Arm server.
    - Network settings (firewalls and security groups) which allow communication on port 22 (SSH) and port 80 (HTTP).

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:47:28Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d492b6dce11b7d8f6591ff3b3ce9aa2c382a6a7a749add228c3ac1f6ae57e218
  summary_generated_at: '2026-06-02T03:43:48Z'
  summary_source_hash: d492b6dce11b7d8f6591ff3b3ce9aa2c382a6a7a749add228c3ac1f6ae57e218
  faq_generated_at: '2026-06-03T00:47:28Z'
  faq_source_hash: d492b6dce11b7d8f6591ff3b3ce9aa2c382a6a7a749add228c3ac1f6ae57e218
  summary: >-
    This Learning Path shows how to build, install, and run Envoy on Arm-based Linux servers and
    configure it as a basic web server for traffic management. You will provision an Arm instance
    in the cloud (AWS, Microsoft Azure, Google Cloud, or Oracle) or use an on-premises Arm server,
    ensure network access on SSH (22) and HTTP (80), and then set up Envoy with a sample configuration
    to run it as a service. The steps focus on practical setup and conclude with checks to verify
    Envoy is working correctly. Aimed at an introductory audience, the path is designed to be
    completed in about 60 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need at least one Arm-based instance from a cloud service provider or an on-premises
      Arm server. Ensure your network settings (firewalls and security groups) allow communication
      on port 22 (SSH) and port 80 (HTTP).
  - question: Which platforms can I use for the Arm-based instance?
    answer: >-
      You can use Arm-based instances from AWS, Microsoft Azure, Google Cloud, or Oracle. An on-premises
      Arm server also works for this Learning Path.
  - question: Which operating system do the steps target?
    answer: >-
      The steps target Linux. Ensure your Arm instance is running a Linux distribution.
  - question: How do I run Envoy as a service in this path?
    answer: >-
      You will create a sample configuration file at configs/config-http.yaml and use it to start
      Envoy. The sample config defines a listener on port 80 with an HTTP connection manager.
  - question: What should I check if I cannot reach the Envoy web server?
    answer: >-
      Verify that your security groups and firewalls allow inbound traffic on port 80 and that
      SSH access on port 22 is permitted for management. Also confirm that Envoy is running with
      the provided configuration file.
# END generated_summary_faq

author: Zhengjun Xing

### Tags
skilllevels: Introductory
subjects: Web
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
armips:
    - Neoverse
tools_software_languages:
    - Envoy   
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Envoy documentation
        link: https://www.envoyproxy.io/docs/envoy/latest/
        type: documentation
    - resource:
        title: Envoy build documentation
        link: https://www.envoyproxy.io/docs/envoy/latest/start/building
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


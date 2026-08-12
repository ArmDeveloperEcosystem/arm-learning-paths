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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-12T20:18:01Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 8659e88d5c24a5a5f47bc8f4436900bb146c6758477e87728b7f14a473d67b00
  summary_generated_at: '2026-08-12T20:18:01Z'
  summary_source_hash: 8659e88d5c24a5a5f47bc8f4436900bb146c6758477e87728b7f14a473d67b00
  faq_generated_at: '2026-08-12T20:18:01Z'
  faq_source_hash: 8659e88d5c24a5a5f47bc8f4436900bb146c6758477e87728b7f14a473d67b00
  summary: >-
    You'll build, install, and run Envoy on an Arm-based Linux server in the cloud or on premises.
    First, you'll review installation and connection options, then create a minimal YAML configuration
    with an HTTP listener on `0.0.0.0:80`. You'll run Envoy as a service, open SSH and HTTP access,
    and verify traffic on port 80.
  faqs:
  - question: How do I know Envoy started with my configuration?
    answer: >-
      Envoy should load the YAML without errors, bind to `0.0.0.0:80`, and begin handling HTTP traffic.
      If startup fails, recheck the YAML formatting and location of `configs/config-http.yaml`.
  - question: Which address and port does the sample listener use?
    answer: >-
      The sample configuration sets the listener to `0.0.0.0` on port 80 in the `socket_address` section.
      This makes Envoy accept HTTP connections on all interfaces.
  - question: Where should I save the sample configuration file?
    answer: >-
      Save the file as `configs/config-http.yaml`. Start Envoy so it reads
      that file, and it will apply the listener and HTTP settings.
  - question: What should I check if I can't reach Envoy on port 80?
    answer: >-
      Confirm that firewalls and security groups allow inbound HTTP on port 80. Also
      verify the YAML listener uses `0.0.0.0:80` and that Envoy is running.
  - question: Can I skip the build and install steps if Envoy is already present?
    answer: >-
      Yes. Use the provided configuration to run Envoy as a service and proceed to verifying HTTP
      access on port 80.
# END generated_summary_faq

author: Zhengjun Xing

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Web
platforms:
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

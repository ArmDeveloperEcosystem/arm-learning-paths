---
title: Microbenchmark and tune network performance with iPerf3 and Linux traffic control

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for performance engineers, Linux system administrators, and application developers who want to microbenchmark, simulate, or tune the networking performance of distributed systems.

learning_objectives: 
    - Run accurate network microbenchmark tests using iPerf3.
    - Simulate real-world network conditions using Linux traffic control (tc).
    - Tune basic Linux kernel parameters to improve network performance.

prerequisites:
    - Basic understanding of networking principles such as Transmission Control Protocol/Internet Protocol (TCP/IP) and User Datagram Protocol (UDP).
    - Access to two [Arm-based cloud instances](/learning-paths/servers-and-cloud-computing/csp/).

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-28T19:48:55Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 2b3db5074d3815ccef1cca54910f28d3ee409c6ddce0676ae53615c443849987
  summary_generated_at: '2026-09-28T19:48:55Z'
  summary_source_hash: 2b3db5074d3815ccef1cca54910f28d3ee409c6ddce0676ae53615c443849987
  faq_generated_at: '2026-09-28T19:48:55Z'
  faq_source_hash: 2b3db5074d3815ccef1cca54910f28d3ee409c6ddce0676ae53615c443849987
  summary: >-
    You'll measure TCP and UDP network performance between Arm-based Linux systems with iPerf3. First, you'll configure
    a server and client, choose an alternate port when needed, and confirm that the server is listening.
    Next, you'll identify the active interface and use Linux traffic control to introduce delay and loss,
    then compare the results. Finally, you'll apply basic kernel tuning and test traffic between a
    local machine and a cloud instance.
  faqs:
  - question: How do I know that the iPerf3 server started correctly?
    answer: >-
      Confirm that the server prints output similar to `Server listening on 5201 (test #1)`. If
      the default port is busy, restart it on another port with the `-p` option.
  - question: What should I check if the client can't connect to the server?
    answer: >-
      Verify network reachability and confirm that you used the correct IP address or hostname.
      Ensure that your cloud security group allows inbound TCP traffic to the selected iPerf3
      port.
  - question: Which system do I run the iPerf3 server and the test on?
    answer: >-
      Start iPerf3 in server mode on the system designated as `SERVER`. Run the test from the other
      system, which acts as the client.
  - question: How do I choose the network interface when applying Linux tc?
    answer: >-
      Run `ip addr show` on the client to identify the active network interface. Use that interface
      name, such as `ens5`, when you apply delay or loss with `tc`.
  - question: What result should I expect after adding delay or testing from a local machine to
      the cloud?
    answer: >-
      Rerun iPerf3 and compare its output with your instance-to-instance baseline. Use the measured
      throughput, jitter, and packet-loss values to see how the new network conditions affect performance.
# END generated_summary_faq

author: Kieran Hejmadi

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
platforms:
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
  - Oracle Cloud Infrastructure (OCI) Ampere Compute
armips:
    - Neoverse
tools_software_languages:
    - iPerf3
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: iPerf3 user manual 
        link: https://iperf.fr/iperf-doc.php
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

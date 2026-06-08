---
title: Microbenchmark and tune network performance with iPerf3 and Linux traffic control

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for performance engineers, Linux system administrators, and application developers who want to microbenchmark, simulate, or tune the networking performance of distributed systems.

learning_objectives: 
    - Run accurate network microbenchmark tests using iPerf3.
    - Simulate real-world network conditions using Linux Traffic Control (tc).
    - Tune basic Linux kernel parameters to improve network performance.

prerequisites:
    - Basic understanding of networking principles such as Transmission Control Protocol/Internet Protocol (TCP/IP) and User Datagram Protocol (UDP).
    - Access to two [Arm-based cloud instances](/learning-paths/servers-and-cloud-computing/csp/).

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:29:10Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a67d36fb650b77c170c15f193049490286a3f097801d0c79d701d3f5610fe1dc
  summary_generated_at: '2026-06-02T04:23:38Z'
  summary_source_hash: a67d36fb650b77c170c15f193049490286a3f097801d0c79d701d3f5610fe1dc
  faq_generated_at: '2026-06-03T01:29:10Z'
  faq_source_hash: a67d36fb650b77c170c15f193049490286a3f097801d0c79d701d3f5610fe1dc
  summary: >-
    Learn to microbenchmark and tune network performance on Arm-based Linux systems using iPerf3
    and Linux traffic control (tc). You will provision two Arm-based instances—such as AWS EC2
    with Graviton within a VPC or equivalent Arm-based VMs from other cloud providers—and run
    TCP/UDP tests in cloud-to-cloud and local-to-cloud scenarios. The steps show how to start
    iPerf3, simulate latency and packet loss with tc, and adjust basic Linux kernel parameters,
    then compare results across environments. This introductory path assumes a basic understanding
    of TCP/IP and UDP and access to two Arm-based cloud instances. By the end, you can run accurate
    iPerf3 tests, model adverse network conditions, and apply simple tunables to evaluate behavior.
  faqs:
  - question: What do I need before running the tests?
    answer: >-
      You need two Arm-based Linux cloud instances and a basic understanding of TCP/IP and UDP.
      Ensure the systems can reach each other over the network, and if you use AWS, the setup
      follows EC2 instances within a VPC.
  - question: How do I start the iPerf3 server and confirm it’s ready?
    answer: >-
      Run iperf3 -s on the server node. You should see “Server listening on 5201” by default;
      if that port is in use, start the server with -p to select another port.
  - question: Can I use a cloud provider other than AWS for this Learning Path?
    answer: >-
      Yes. While the setup examples use AWS EC2 with Graviton, you can use Linux virtual machines
      from other cloud service providers.
  - question: How do I simulate latency or packet loss with tc and which interface should I modify?
    answer: >-
      First, identify the network interface on the client system using ip addr show. Apply tc
      rules (such as delay or loss) to that interface to simulate different network conditions.
  - question: What should I check if a local-to-cloud test cannot connect?
    answer: >-
      Update the cloud server’s security group to allow incoming TCP connections from your local
      machine. Also ensure iPerf3 is installed on the local system as described in the iPerf3
      installation guide.
# END generated_summary_faq

author: Kieran Hejmadi

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
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


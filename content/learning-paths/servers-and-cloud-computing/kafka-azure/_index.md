---
title: Deploy Apache Kafka on Arm-based Microsoft Azure Cobalt 100 virtual machines 

minutes_to_complete: 30   

who_is_this_for: This is an advanced topic for developers looking to migrate their Apache Kafka workloads from x86_64 to Arm-based platforms, specifically on Microsoft Azure Cobalt 100 (arm64) virtual machines (VMs).

description: Deploy Apache Kafka on Azure Cobalt 100 Arm virtual machines and benchmark message throughput performance.

learning_objectives: 
    - Provision an Azure Arm64 VM using Azure console, with Ubuntu Pro 24.04 LTS as the base image.
    - Deploy Kafka on an Ubuntu VM.
    - Perform Kafka baseline testing and benchmarking on Arm64 VMs.

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 based instances (Dpsv6)
    - Basic understanding of the Linux command line
    - Familiarity with the [Apache Kafka architecture](https://kafka.apache.org/) and deployment practices on Arm64 platforms

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-15T21:20:39Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: c1f6038eaba282ca168d1826dfce644ecb21fd01b627fd274e23e513fcac3a36
  summary_generated_at: '2026-09-15T21:20:39Z'
  summary_source_hash: c1f6038eaba282ca168d1826dfce644ecb21fd01b627fd274e23e513fcac3a36
  faq_generated_at: '2026-09-15T21:20:39Z'
  faq_source_hash: c1f6038eaba282ca168d1826dfce644ecb21fd01b627fd274e23e513fcac3a36
  summary: >-
    You'll provision an Arm64 Azure Cobalt 100 VM, install Java and Kafka, and configure Kafka
    `4.1.0` in KRaft mode. First, you'll create a topic and verify producer-to-consumer message flow, then
    run Kafka’s official performance tools to capture throughput and latency. You'll finish
    with a working Kafka deployment and baseline benchmark results from an Arm64 instance on
    Microsoft Azure.
  faqs:
  - question: Which Azure VM series should I use?
    answer: >-
      Select a D-Series v6 VM from the Dpsv6 size series, which uses the Cobalt 100
      Arm-based CPU. 
  - question: Which operating system image do I choose when creating the VM?
    answer: >-
      Use Ubuntu Pro 24.04 (Arm64).
  - question: Do I need ZooKeeper for this Kafka setup?
    answer: >-
      No. Kafka `4.1.0` supports KRaft mode, which removes the need for ZooKeeper. Start the broker in
      KRaft mode.
  - question: How do I verify that Kafka is working after installation?
    answer: >-
      Open separate terminals for each of the following tasks: starting the Kafka broker (KRaft), creating a topic, running a consumer, and
      running a producer. If the consumer receives the messages that you produce, the end-to-end flow works.
  - question: What should I look for when running the Kafka benchmarks?
    answer: >-
      Ensure that the broker is running and the topic is ready, then run the official
      `kafka-producer-perf-test.sh` and `kafka-consumer-perf-test.sh` tools. Review the reported throughput and latency metrics
      to confirm that the benchmark completed, and to capture baseline results.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Storage
platforms:
  - Microsoft Azure Cobalt

armips:
    - Neoverse

tools_software_languages:
    - Kafka

operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Kafka Manual
        link: https://kafka.apache.org/documentation/
        type: documentation
    - resource:
        title: Kafka Performance Tool
        link: https://codemia.io/knowledge-hub/path/use_kafka-producer-perf-testsh_how_to_set_producer_config_at_kafka_210-0820
        type: documentation
    - resource:        
        title: Kafka on Azure
        link: https://learn.microsoft.com/en-us/samples/azure/azure-quickstart-templates/kafka-ubuntu-multidisks/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

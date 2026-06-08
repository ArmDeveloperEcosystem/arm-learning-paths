---
title: Deploy Apache Kafka on Arm-based Microsoft Azure Cobalt 100 virtual machines 

minutes_to_complete: 30   

who_is_this_for: This is an advanced topic for developers looking to migrate their Apache Kafka workloads from x86_64 to Arm-based platforms, specifically on Microsoft Azure Cobalt 100 (arm64) virtual machines.

description: Deploy Apache Kafka on Azure Cobalt 100 Arm virtual machines and benchmark message throughput performance.

learning_objectives: 
    - Provision an Azure Arm64 virtual machine using Azure console, with Ubuntu Pro 24.04 LTS as the base image
    - Deploy Kafka on an Ubuntu virtual machine
    - Perform Kafka baseline testing and benchmarking on Arm64 virtual machines

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 based instances (Dpsv6)
    - Basic understanding of Linux command line
    - Familiarity with the [Apache Kafka architecture](https://kafka.apache.org/) and deployment practices on Arm64 platforms

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:16:31Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d510dd43a485e1c2fac404ef9a2e00b5be2449b99b1095c9a1841cd2fcba9b0e
  summary_generated_at: '2026-06-02T04:12:27Z'
  summary_source_hash: d510dd43a485e1c2fac404ef9a2e00b5be2449b99b1095c9a1841cd2fcba9b0e
  faq_generated_at: '2026-06-03T01:16:31Z'
  faq_source_hash: d510dd43a485e1c2fac404ef9a2e00b5be2449b99b1095c9a1841cd2fcba9b0e
  summary: >-
    Provision an Arm-based Microsoft Azure Cobalt 100 (Dpsv6) virtual machine using the Azure
    portal, install Apache Kafka on Ubuntu Pro 24.04 LTS (arm64), and validate end-to-end messaging
    before running official Kafka benchmarks. You will set up Java, deploy Kafka, start the broker
    in KRaft mode, and perform a baseline producer/consumer test to confirm the environment is
    working. Finally, use Kafka’s bundled performance tools to measure throughput and latency
    on the Arm64 VM. This advanced path targets developers migrating Kafka workloads to Arm on
    Azure. Prerequisites include an Azure account with access to Cobalt 100 instances, basic Linux
    command-line skills, and familiarity with Kafka architecture and Arm64 deployment practices.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      You need a Microsoft Azure account with access to Cobalt 100 based instances (Dpsv6), basic
      Linux command-line skills, and familiarity with the Apache Kafka architecture and deployment
      on Arm64. No other prerequisites are explicitly listed.
  - question: Which Azure VM size and OS image should I select?
    answer: >-
      Use a Dpsv6 series virtual machine based on the Arm-based Cobalt 100 CPU and select Ubuntu
      Pro 24.04 LTS (Arm64) as the base image. The steps use the Azure portal to create the VM.
  - question: Do I need ZooKeeper for this Kafka setup?
    answer: >-
      No. Kafka 4.1.0 in KRaft mode integrates the control and data planes and removes the need
      for ZooKeeper, simplifying deployment.
  - question: How do I know the baseline test worked?
    answer: >-
      Start the Kafka broker in KRaft mode and run the producer and consumer in separate terminals.
      Successful end-to-end message production and consumption indicates the setup is working.
  - question: Which tools are used for benchmarking and what should be running first?
    answer: >-
      Use kafka-producer-perf-test.sh and kafka-consumer-perf-test.sh bundled with Kafka to measure
      throughput, latency, and end-to-end efficiency. Ensure your Kafka broker is already active
      in a separate terminal before running these tools.
# END generated_summary_faq

author: Pareena Verma

### Tags
skilllevels: Advanced
subjects: Storage
cloud_service_providers:
  - Microsoft Azure

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


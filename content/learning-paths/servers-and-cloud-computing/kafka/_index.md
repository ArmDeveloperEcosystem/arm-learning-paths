---
title: Deploy a Kafka Cluster on Arm

minutes_to_complete: 90

who_is_this_for: This is an advanced topic for software developers who want to learn how to use Kafka and Zookeeper.

description: Deploy and configure a Kafka cluster with Zookeeper on Arm servers, test event streaming, and automate deployment on AWS and Google Cloud.

learning_objectives:
    - Install Zookeeper and Kafka.
    - Configure Zookeeper to work with Kafka.
    - Test write and read events into the Kafka cluster.
    - Deploy a cluster automatically on AWS.
    - Deploy a cluster automatically on GCP.

prerequisites:
    - Seven physical Arm machines or cloud instances with either Ubuntu or Debian installed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-15T21:20:05Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 779059246dff45332eb117c70425b02a81a2a0b07d8a85e4f1c810f8343e8501
  summary_generated_at: '2026-09-15T21:20:05Z'
  summary_source_hash: 779059246dff45332eb117c70425b02a81a2a0b07d8a85e4f1c810f8343e8501
  faq_generated_at: '2026-09-15T21:20:05Z'
  faq_source_hash: 779059246dff45332eb117c70425b02a81a2a0b07d8a85e4f1c810f8343e8501
  summary: >-
    You'll deploy a three-node Apache Kafka cluster on Arm, beginning with a three-node
    ZooKeeper ensemble. First, you'll prepare network ports and configure the brokers. Then, you'll start the services
    in order and validate end-to-end messaging by creating a topic, producing events, and
    reading them from a client. You'll also use Terraform and Ansible to automate the same
    topology on AWS Graviton.
  faqs:
  - question: How do I know that the ZooKeeper cluster is ready before I configure Kafka?
    answer: >-
      The cluster is ready when all three ZooKeeper nodes are started and reachable from the Kafka nodes. The
      Kafka configuration will reference the three ZooKeeper IPs, so confirm those addresses are
      correct and accessible.
  - question: Which IPs should I put into Kafka’s server properties?
    answer: >-
      Replace `zk_1_ip`, `zk_2_ip`, and `zk_3_ip` with the IP addresses of the three ZooKeeper nodes
      that you set up. Use the same addresses that you used when bringing up the ZooKeeper cluster.
  - question: Which ports should be open on the nodes?
    answer: >-
      Open ports `8080`, `2888`, `3888`, `2181`, and `9092` in the security groups for these machines. Ensure
      that the rules allow traffic between cluster nodes and from the client where you run Kafka commands.
  - question: What result should I expect after I produce and consume events?
    answer: >-
      You should see the consumer read the same message that you wrote in the producer terminal.
      This verifies that the Kafka cluster is working.
  - question: Where do I run the AWS automation, and which tools does it use?
    answer: >-
      Run the automation from any computer with the required tools installed. The AWS deployment
      uses Terraform and Ansible to provision a three-node ZooKeeper cluster, a three-node Kafka
      cluster, and one client on AWS Graviton.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Storage
platforms:
  - AWS Graviton
  - Google Axion
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Kafka
    - ZooKeeper

further_reading:
    - resource:
        title: Kafka Manual
        link: https://kafka.apache.org/documentation/
        type: documentation
    - resource:
        title: Benchmarking Apache Kafka
        link: https://armkeil.blob.core.windows.net/developer/Files/pdf/white-paper/benchmarking-apache-kafka.pdf
        type: documentation
    - resource: 
        title: Zookeeper Documentation
        link: https://zookeeper.apache.org/documentation.html
        type: documentation
    - resource:
        title: Apache Kafka Benchmarks on AWS Graviton2
        link: https://developer.arm.com/community/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/apache-kafka-benchmarks-on-aws-graviton2
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

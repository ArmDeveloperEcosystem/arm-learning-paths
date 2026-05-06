---
title: Deploy a Kafka Cluster on Arm

minutes_to_complete: 90

who_is_this_for: This is an advanced topic for software developers who want to learn how to use Kafka and Zookeeper.

description: Deploy and configure a Kafka cluster with Zookeeper on Arm servers, test event streaming, and automate deployment on AWS and Google Cloud.

learning_objectives:
    - Install Zookeeper and Kafka
    - Configure Zookeeper to work with Kafka
    - Test write/read events into the Kafka cluster
    - Deploy a cluster automatically on AWS
    - Deploy a cluster automatically on GCP

prerequisites:
    - Seven physical Arm machines or cloud instances with either Ubuntu or Debian installed. 

generate_summary_faq: true

# rerun_summary: false
# rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:58Z'
  generator: template
  source_hash: b7f36df881c2c436143c1e5579d2c54cb5930f52998904098829c52fa7290f38
  summary: >-
    Deploy and configure a Kafka cluster with Zookeeper on Arm servers, test event streaming,
    and automate deployment on AWS and Google Cloud. It is designed for software developers who
    want to learn how to use Kafka and Zookeeper. By the end, you will be able to install Zookeeper
    and Kafka, configure Zookeeper to work with Kafka, and test write/read events into the Kafka
    cluster. It focuses on tools and technologies such as Kafka and ZooKeeper, Linux environments,
    Arm platforms including Neoverse, and cloud platforms such as AWS and Google Cloud. The main
    steps cover Introduction to Kafka and Zookeeper, Setup a 3 node Zookeeper Cluster, Set up
    a 3 node Kafka Cluster, Verify that the Kafka Cluster is working, and Deploy Cluster Automatically
    (AWS).
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will install Zookeeper and Kafka, configure Zookeeper to work with Kafka, and test write/read
      events into the Kafka cluster. Deploy and configure a Kafka cluster with Zookeeper on Arm
      servers, test event streaming, and automate deployment on AWS and Google Cloud.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for software developers who want to learn how to use Kafka and
      Zookeeper.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: Seven physical Arm machines or cloud
      instances with either Ubuntu or Debian installed.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Kafka and ZooKeeper, Linux environments, Arm platforms
      such as Neoverse, and cloud platforms such as AWS and Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Introduction to Kafka and Zookeeper, Setup a 3 node
      Zookeeper Cluster, Set up a 3 node Kafka Cluster, Verify that the Kafka Cluster is working,
      and Deploy Cluster Automatically (AWS).
# END generated_summary_faq

author: Pareena Verma

### Tags
skilllevels: Advanced
subjects: Storage
cloud_service_providers:
  - AWS
  - Google Cloud
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


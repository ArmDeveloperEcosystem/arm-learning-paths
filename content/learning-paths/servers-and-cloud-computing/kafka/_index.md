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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:15:30Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b7f36df881c2c436143c1e5579d2c54cb5930f52998904098829c52fa7290f38
  summary_generated_at: '2026-06-02T04:11:38Z'
  summary_source_hash: b7f36df881c2c436143c1e5579d2c54cb5930f52998904098829c52fa7290f38
  faq_generated_at: '2026-06-03T01:15:30Z'
  faq_source_hash: b7f36df881c2c436143c1e5579d2c54cb5930f52998904098829c52fa7290f38
  summary: >-
    This advanced Learning Path guides you through deploying a production-style Kafka event streaming
    cluster on Arm-based Linux servers. You will install and configure a three-node ZooKeeper
    ensemble and a three-node Kafka cluster on Ubuntu or Debian, then validate the setup by creating
    a topic and writing/reading events from a client node. The path also covers automating deployment
    on AWS Graviton processors using Terraform and Ansible, with objectives that include automation
    on Google Cloud. You need seven Arm machines or cloud instances and appropriate network ports
    opened. After about 90 minutes, you will have a working Kafka cluster on Arm and a repeatable
    deployment approach for cloud environments.
  faqs:
  - question: What do I need before running the setup?
    answer: >-
      You need seven physical Arm machines or cloud instances running Ubuntu or Debian. Ensure
      ports 8080, 2888, 3888, 2181, and 9092 are open in the security groups for these machines.
  - question: How should I assign roles to the seven machines?
    answer: >-
      Use three machines for the ZooKeeper cluster, three machines for the Kafka cluster, and
      one machine as the client.
  - question: Which configuration values do I change on Kafka nodes to connect to ZooKeeper?
    answer: >-
      Edit config/server.properties on each Kafka node and replace zk_1_ip, zk_2_ip, and zk_3_ip
      with the IP addresses of your three ZooKeeper nodes.
  - question: Where do I run the validation and what result should I expect?
    answer: >-
      Install Kafka on the client machine, create a topic, write events to it, and read them back.
      Successfully reading the events you produced confirms the Kafka cluster is working.
  - question: Which options are available for automated deployment on cloud platforms?
    answer: >-
      The path covers automated deployment on AWS and Google Cloud. On AWS, Terraform and Ansible
      are used to deploy a three-node ZooKeeper cluster, a three-node Kafka cluster, and one client
      on AWS Graviton, and you should have the required tools installed on a computer you can
      run them from.
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


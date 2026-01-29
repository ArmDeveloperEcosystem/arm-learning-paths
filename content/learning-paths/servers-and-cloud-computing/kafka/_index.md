---
title: Deploy a Kafka Cluster on Arm

minutes_to_complete: 90

who_is_this_for: This is an advanced topic for software developers who want to learn how to use Kafka and Zookeeper.

learning_objectives:
    - Install Zookeeper and Kafka
    - Configure Zookeeper to work with Kafka
    - Test write/read events into the Kafka cluster
    - Deploy a cluster automatically on AWS
    - Deploy a cluster automatically on GCP

prerequisites:
    - Seven physical Arm machines or cloud instances with either Ubuntu or Debian installed. 

author: Pareena Verma

### Tags
skilllevels: Advanced
subjects: Storage
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

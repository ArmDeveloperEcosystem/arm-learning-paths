---
title: Deploy Cassandra on a Google Axion C4A virtual machine

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers migrating Cassandra workloads from x86_64 to Arm-based servers, specifically on Google Cloud C4A virtual machines built on Axion processors.


learning_objectives:
  - Provision an Arm-based SUSE SLES virtual machine on Google Cloud (C4A with Axion processors)
  - Install and configure Apache Cassandra on a SUSE Arm64 (C4A) instance
  - Validate Cassandra functionality using CQLSH and baseline keyspace/table operations
  - Benchmark Cassandra performance using cassandra-stress for read and write workloads on Arm64 (Aarch64) architecture

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Familiarity with Cassandra architecture, replication, and [Cassandra partitioning and event-driven I/O](https://cassandra.apache.org/doc/stable/cassandra/architecture/)

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Databases
cloud_service_providers: Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - Apache Cassandra
  - Java
  - cqlsh
  - cassandra-stress

operatingsystems:
  - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
  - resource:
      title: Google Cloud documentation
      link: https://cloud.google.com/docs
      type: documentation

  - resource:
      title: Apache Cassandra documentation
      link: https://cassandra.apache.org/doc/latest/
      type: documentation

  - resource:
      title: Cassandra-stress documentation
      link: https://cassandra.apache.org/doc/4.0/cassandra/tools/cassandra_stress.html
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

---
title: Deploy RabbitMQ on Google Cloud C4A (Arm-based Axion VMs)

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software engineers and platform engineers migrating messaging and event-driven workloads from x86_64 to Arm-based servers, specifically on Google Cloud C4A virtual machines powered by Axion processors.

learning_objectives:
  - Provision an Arm-based SUSE SLES virtual machine on Google Cloud (C4A with Axion processors)
  - Install and configure RabbitMQ on a SUSE Arm64 (C4A) instance
  - Validate RabbitMQ deployment using baseline messaging tests
  - Implement real-world RabbitMQ use cases such as event-driven processing and notification pipelines

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic understanding of message queues and messaging concepts (publishers, consumers)
  - Familiarity with Linux command-line operations

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Databases
cloud_service_providers: Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - RabbitMQ
  - Erlang
  - Python
  - pika

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
      title: RabbitMQ documentation
      link: https://www.rabbitmq.com/documentation.html 
      type: documentation

  - resource:
      title: RabbitMQ Tutorials
      link: https://www.rabbitmq.com/getstarted.html
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

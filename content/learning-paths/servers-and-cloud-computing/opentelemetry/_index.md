---
title: Deploy OpenTelemetry on Google Cloud C4A Axion processors

minutes_to_complete: 40

who_is_this_for: This learning path is for DevOps engineers, platform engineers, and software developers who want to deploy and observe a cloud-native microservice on Arm64-based Google Cloud C4A Axion processors using OpenTelemetry.

learning_objectives:
 - Deploy an instrumented Python Flask microservice on Google Cloud C4A Axion processors
 - Configure OpenTelemetry Collector to process and route distributed traces and metrics
 - Integrate Prometheus and Jaeger for comprehensive metrics collection and distributed tracing visualization
 - Generate and analyze telemetry data to monitor application performance on Arm-based infrastructure

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with Python and Flask
  - Basic understanding of containers and Kubernetes concepts

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:58Z'
  generator: template
  source_hash: cb4227a3f8375d6ae63801891703d6e615bdc60a01fca099a2f76453775ef460
  summary: >-
    Deploy OpenTelemetry on Google Cloud C4A Axion processors walks you through an end-to-end
    Arm software workflow. It is designed for DevOps engineers, platform engineers, and software
    developers who want to deploy and observe a cloud-native microservice on Arm64-based Google
    Cloud C4A Axion processors using OpenTelemetry. By the end, you will be able to deploy an
    instrumented Python Flask microservice on Google Cloud C4A Axion processors, configure OpenTelemetry
    Collector to process and route distributed traces and metrics, and integrate Prometheus and
    Jaeger for comprehensive metrics collection and distributed tracing visualization. It focuses
    on tools and technologies such as Flask, Docker, Prometheus, and Jaeger, Linux environments,
    Arm platforms including Neoverse, and cloud platforms such as Google Cloud. The main steps
    cover Get started with OpenTelemetry on Google Axion C4A, Create firewall rules on GCP for
    Flask and observability components, Create a Google Axion C4A Arm virtual machine on GCP,
    Set up OpenTelemetry environment and application on Arm64, and Deploy the OpenTelemetry observability
    stack on Arm64.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will deploy an instrumented Python Flask microservice on Google Cloud C4A Axion processors,
      configure OpenTelemetry Collector to process and route distributed traces and metrics, and
      integrate Prometheus and Jaeger for comprehensive metrics collection and distributed tracing
      visualization.
  - question: Who is this Learning Path for?
    answer: >-
      This learning path is for DevOps engineers, platform engineers, and software developers
      who want to deploy and observe a cloud-native microservice on Arm64-based Google Cloud C4A
      Axion processors using OpenTelemetry.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Google Cloud Platform (GCP)](https://cloud.google.com/free)
      account with billing enabled; Basic familiarity with Python and Flask; Basic understanding
      of containers and Kubernetes concepts.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Flask, Docker, Prometheus, and Jaeger, Linux environments,
      Arm platforms such as Neoverse, and cloud platforms such as Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Get started with OpenTelemetry on Google Axion C4A,
      Create firewall rules on GCP for Flask and observability components, Create a Google Axion
      C4A Arm virtual machine on GCP, Set up OpenTelemetry environment and application on Arm64,
      and Deploy the OpenTelemetry observability stack on Arm64.
# END generated_summary_faq

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
  - Google Cloud

armips:
- Neoverse

tools_software_languages:
- Flask
- Docker
- Prometheus
- Jaeger

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
      title: OpenTelemetry documentation
      link: https://opentelemetry.io/docs/
      type: documentation

  - resource:
      title: Prometheus documentation
      link: https://prometheus.io/docs/introduction/overview/
      type: documentation
  
  - resource:
      title: Jaeger documentation
      link: https://www.jaegertracing.io/docs/
      type: documentation
  
  - resource:
      title: Docker documentation
      link: https://docs.docker.com/
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: yes
---


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

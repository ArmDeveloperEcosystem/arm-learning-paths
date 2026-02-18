---
title: Deploy OpenTelemetry on Google Cloud C4A Arm-based Axion VMs

draft: true
cascade:
    draft: true
    
minutes_to_complete: 40

who_is_this_for: This learning path is designed for DevOps engineers, platform engineers, and software developers who want to deploy and observe a cloud-native microservice on Arm64-based Google Cloud C4A Axion processors using OpenTelemetry, along with industry-standard observability tools.

learning_objectives:
  - Provision a SUSE Linux Enterprise Server (SLES) virtual machine on Google Cloud C4A Arm-based Axion processors
  - Install and configure Docker and Docker Compose on an Arm64 environment
  - Build and run an Arm-native Python Flask microservice in containers
  - Instrument the microservice using OpenTelemetry SDK for distributed tracing and metrics
  - Deploy and configure OpenTelemetry Collector for telemetry processing
  - Integrate Prometheus for metrics collection and visualization
  - Integrate Jaeger for distributed tracing and service visualization
  - Expose and validate observability dashboards
  - Generate traffic to observe telemetry data flow and performance behavior
  - Understand observability best practices on Arm-based cloud infrastructure

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with Python and Flask
  - Basic understanding of containers and Kubernetes concepts

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers: Google Cloud

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

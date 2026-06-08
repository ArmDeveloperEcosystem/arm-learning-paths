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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:45:22Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: cb4227a3f8375d6ae63801891703d6e615bdc60a01fca099a2f76453775ef460
  summary_generated_at: '2026-06-02T04:44:29Z'
  summary_source_hash: cb4227a3f8375d6ae63801891703d6e615bdc60a01fca099a2f76453775ef460
  faq_generated_at: '2026-06-03T01:45:22Z'
  faq_source_hash: cb4227a3f8375d6ae63801891703d6e615bdc60a01fca099a2f76453775ef460
  summary: >-
    This Learning Path guides you through deploying and observing a Python Flask microservice
    on Arm64-based Google Cloud C4A Axion processors. You will provision a c4a-standard-4 VM running
    SUSE Linux, configure GCP firewall rules for the service and observability endpoints, and
    prepare container tooling to run an instrumented Flask app that emits OpenTelemetry traces
    and metrics. You then deploy the OpenTelemetry Collector and integrate Prometheus and Jaeger
    so metrics and traces flow from the service through the collector to their UIs. By the end,
    you can generate and analyze telemetry for the service on Arm infrastructure. Prerequisites
    include a GCP account with billing enabled and basic Python/Flask and container/Kubernetes
    familiarity.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Google Cloud Platform account with billing enabled, basic familiarity with Python
      and Flask, and a basic understanding of containers and Kubernetes concepts.
  - question: Which Google Cloud VM and operating system does this path use?
    answer: >-
      You will create a Google Axion C4A Arm-based VM using the c4a-standard-4 machine type with
      4 vCPUs and 16 GB of memory. The setup uses an arm64-based SUSE Linux virtual machine.
  - question: Which firewall ports should I open and why?
    answer: >-
      Open TCP ports: 8080 for the Flask application, 16686 for the Jaeger UI, 9090 for the Prometheus
      UI, 4317 for OTLP gRPC ingestion, and 4318 for OTLP HTTP ingestion.
  - question: How are the telemetry components connected in this setup?
    answer: >-
      The Flask microservice uses the OpenTelemetry SDK to emit telemetry to the OpenTelemetry
      Collector. The Collector routes metrics to Prometheus and traces to Jaeger.
  - question: How do I validate that telemetry is flowing end-to-end?
    answer: >-
      Access the Prometheus UI on port 9090 and the Jaeger UI on port 16686 to verify data from
      the Flask service. Generate requests to the Flask app on port 8080 to produce new traces
      and metrics.
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


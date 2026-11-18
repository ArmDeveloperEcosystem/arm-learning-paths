---
title: Deploy OpenTelemetry on Google Cloud C4A Axion processors

minutes_to_complete: 40

who_is_this_for: This learning path is for DevOps engineers, platform engineers, and software developers who want to deploy and observe a cloud-native microservice on Arm64-based Google Cloud C4A Axion processors using OpenTelemetry.

learning_objectives:
 - Deploy an instrumented Python Flask microservice on Google Cloud C4A Axion processors.
 - Configure OpenTelemetry Collector to process and route distributed traces and metrics.
 - Integrate Prometheus and Jaeger for comprehensive metrics collection and distributed tracing visualization.
 - Generate and analyze telemetry data to monitor application performance on Arm-based infrastructure.

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with Python and Flask
  - Basic understanding of containers and Kubernetes concepts

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-18T20:21:41Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d795b2fa981f5baed1b0bc6ad05494aed765fc22a875d0e7b9aea3268387e3e7
  summary_generated_at: '2026-11-18T20:21:41Z'
  summary_source_hash: d795b2fa981f5baed1b0bc6ad05494aed765fc22a875d0e7b9aea3268387e3e7
  faq_generated_at: '2026-11-18T20:21:41Z'
  faq_source_hash: d795b2fa981f5baed1b0bc6ad05494aed765fc22a875d0e7b9aea3268387e3e7
  summary: >-
    You'll run an instrumented Flask application and an OpenTelemetry stack on a Google Axion
    C4A VM. First, you'll create the VM and allow application and telemetry traffic through the
    firewall. Then, you'll build the application and deploy the Collector, Prometheus, and Jaeger.
    Finally, you'll generate requests and inspect metrics and traces to verify the pipeline.
  faqs:
  - question: Which Google Cloud C4A instance type should I use?
    answer: >-
      Use a `c4a-standard-4` VM, which has four vCPUs and 16 GB of memory. Run the Flask
      application and observability components on this instance.
  - question: Which firewall ports should be opened to access the app and observability tools?
    answer: >-
      Open TCP ports `8080` for Flask, `16686` for Jaeger, and `9090` for Prometheus. Also open `4317` and
      `4318` for OTLP, and `8889` for Collector metrics. Add the inbound firewall rule to your
      Google Cloud VM.
  - question: How do I know the Flask microservice is emitting telemetry correctly?
    answer: >-
      Generate traffic to the Flask service on port `8080`. Check that traces appear in the
      Jaeger UI and metrics populate in Prometheus. If nothing appears, verify that the OpenTelemetry
      Collector is running and reachable on the OTLP ports you opened.
  - question: Should the application send OTLP over gRPC or HTTP?
    answer: >-
      Use OTLP gRPC on port `4317` for the `app.py` example, which configures the Python
      exporters to send to `otel-collector:4317`. You can use OTLP HTTP on port `4318` if you
      change the SDK configuration to match.
  - question: Where do I view the telemetry after deployment?
    answer: >-
      Use a browser to connect to the IP address of the VM on port `16686` for Jaeger and port `9090`
      for Prometheus. Confirm that the firewall rules allow inbound access to these ports.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

##### Tags
skilllevels: Introductory
subjects: Performance and Architecture
platforms:
  - Google Axion

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


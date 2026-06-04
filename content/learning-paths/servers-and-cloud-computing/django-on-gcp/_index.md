---
title: Deploy Django on Arm-based Google Cloud C4A 
    
minutes_to_complete: 60
description: Learn how to deploy a production-grade Django REST API on Google Kubernetes Engine with Arm64 Axion node pools integrated with Google Cloud managed data services.
who_is_this_for: This is an introductory topic for DevOps engineers and software developers who want to deploy, operate, and benchmark a production-grade Django REST API on Google Kubernetes Engine (GKE) running on Arm64 Axion processors, integrated with managed Google Cloud data services

learning_objectives:
  - Provision Arm-based Axion compute on Google Cloud using virtual machines and GKE node pools
  - Package a Django REST API into an Arm-native Docker container
  - Push container images to Google Artifact Registry
  - Deploy Django on GKE using Kubernetes manifests (Deployment, Service, ConfigMap, Secrets)
  - Integrate Django with Cloud SQL (PostgreSQL) over private IP
  - Integrate Django with Memorystore (Redis) for caching and sessions
  - Expose Django using a Kubernetes LoadBalancer
  - Validate application connectivity to PostgreSQL and Redis
  - Measure throughput and p95 latency using ApacheBench against Gunicorn on Arm

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled  
  - Basic familiarity with [Django](https://www.djangoproject.com/)
  - Basic understanding of containers and Kubernetes concepts

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:41:54Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 6675df4c91126b157dcbf39c96a773130f1a95e2f5680913979da96f6f6c97cd
  summary_generated_at: '2026-06-02T03:34:24Z'
  summary_source_hash: 6675df4c91126b157dcbf39c96a773130f1a95e2f5680913979da96f6f6c97cd
  faq_generated_at: '2026-06-03T00:41:54Z'
  faq_source_hash: 6675df4c91126b157dcbf39c96a773130f1a95e2f5680913979da96f6f6c97cd
  summary: >-
    This Learning Path shows how to deploy a production-grade Django REST API on Google Cloud
    using Arm-based Axion compute. You will provision Arm64 Axion C4A virtual machines and GKE
    node pools, package the application into an Arm-native Docker image, push it to Google Artifact
    Registry, and deploy on GKE using Kubernetes manifests (Deployment, Service, ConfigMap, Secrets).
    The path integrates Django with Cloud SQL (PostgreSQL) over private IP and Memorystore (Redis),
    exposes the service via a LoadBalancer, and validates connectivity to both services. You also
    set up a SUSE Linux Enterprise Server VM, open port 8000, run the Django development server,
    and benchmark Gunicorn on Arm with ApacheBench to measure throughput and p95 latency. Prerequisites
    are a GCP account with billing enabled and basic familiarity with Django, containers, and
    Kubernetes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Google Cloud Platform account with billing enabled. The path assumes basic familiarity
      with Django and a basic understanding of containers and Kubernetes.
  - question: How do I run and reach the Django development server on the Axion VM?
    answer: >-
      You will install Python 3.11 on a SUSE Linux Enterprise Server VM, create a Django project,
      and start the development server. Then, create a firewall rule to allow inbound traffic
      on port 8000 so you can access the server from your browser.
  - question: Which container and registry steps are included before deploying to GKE?
    answer: >-
      You will package the Django REST API into an Arm-native Docker container and push the image
      to Google Artifact Registry. These steps prepare the application for deployment on Arm64
      GKE node pools.
  - question: Which Kubernetes resources and exposure method are used on GKE?
    answer: >-
      The deployment uses Kubernetes manifests including a Deployment, Service, ConfigMap, and
      Secrets. The application is exposed externally using a LoadBalancer Service on Arm64 Axion
      node pools.
  - question: How does the app connect to managed data services and how is performance evaluated?
    answer: >-
      Django is integrated with Cloud SQL (PostgreSQL) over private IP and Memorystore (Redis)
      for caching and sessions, with steps to validate application connectivity. Performance is
      measured using ApacheBench to report throughput and p95 latency against Gunicorn on Arm.
# END generated_summary_faq

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Web
cloud_service_providers:
  - Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - Django
  - Docker
  - Kubernetes
  - Google Artifact Registry
  - Cloud SQL (PostgreSQL)
  - Memorystore (Redis)

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
      title: Django documentation
      link: https://docs.djangoproject.com/
      type: documentation
  - resource:
      title: Cloud SQL for PostgreSQL
      link: https://cloud.google.com/sql/docs/postgres
      type: documentation

  - resource:
      title: Memorystore for Redis
      link: https://cloud.google.com/memorystore/docs/redis
      type: documentation

  - resource:
      title: Apache Bench documentation
      link: https://httpd.apache.org/docs/2.4/programs/ab.html 
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: yes
---


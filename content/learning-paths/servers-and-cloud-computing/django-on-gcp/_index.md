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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-27T18:50:52Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 6675df4c91126b157dcbf39c96a773130f1a95e2f5680913979da96f6f6c97cd
  summary_generated_at: '2026-07-27T18:50:52Z'
  summary_source_hash: 6675df4c91126b157dcbf39c96a773130f1a95e2f5680913979da96f6f6c97cd
  faq_generated_at: '2026-07-27T18:50:52Z'
  faq_source_hash: 6675df4c91126b157dcbf39c96a773130f1a95e2f5680913979da96f6f6c97cd
  summary: >-
    You'll deploy a Django REST API on Google Cloud Axion C4A. You'll create a SUSE Linux Enterprise
    Server VM, install Python and Django, and verify the development server. You'll then containerize
    the application for Google Kubernetes Engine, connect Cloud SQL PostgreSQL over private IP and
    Memorystore Redis, expose the service with a LoadBalancer, and measure throughput and p95 latency
    with ApacheBench against Gunicorn on Arm.
  faqs:
  - question: Which Axion C4A VM configuration should I use for the initial setup?
    answer: >-
      The steps use `c4a-standard-4`, which provides four vCPUs and 16 GB of memory. Create the
      instance from Compute Engine in the Google Cloud Console.
  - question: How do I open and verify access to the Django development server?
    answer: >-
      Create a firewall rule that allows inbound TCP traffic on port 8000 to your VM. After starting
      the server, browse to the VM’s external IP on port 8000 to confirm it responds.
  - question: What should I see after creating the Django project?
    answer: >-
      You should see a `manage.py` file and a project module directory containing `settings.py`,
      `urls.py`, `asgi.py`, and `wsgi.py`. Running the development server should serve a Django page from the
      VM on port 8000.
  - question: Which Linux distribution and Python version do the installation steps use?
    answer: >-
      The steps use SUSE Linux Enterprise Server (SLES) and install Python 3.11 with zypper. Verify
      the installation with `python3.11 --version` before creating the Django project.
  - question: How is state handled when deploying to GKE later in the path?
    answer: >-
      The deployment integrates Cloud SQL (PostgreSQL) over private IP and Memorystore (Redis)
      for caching and sessions. Kubernetes manifests use objects such as ConfigMap and Secrets
      to configure the application.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

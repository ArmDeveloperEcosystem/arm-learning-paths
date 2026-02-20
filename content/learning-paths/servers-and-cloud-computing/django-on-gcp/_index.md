---
title: Deploy Django on Arm-based Google Cloud C4A 
    
minutes_to_complete: 60

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
